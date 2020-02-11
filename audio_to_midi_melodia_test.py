# CREATED: 11/9/15 3:57 PM by Justin Salamon <justin.salamon@nyu.edu>
import math
import string
import sys

import numpy as np
import resampy
import soundfile
import vamp
from midiutil.MidiFile import MIDIFile
from scipy.signal import medfilt
import norepeatmusictheory

'''
Extract the melody from an audio file and convert it to MIDI.

The script extracts the melody from an audio file using the Melodia algorithm,
and then segments the continuous pitch sequence into a series of quantized
notes, and exports to MIDI using the provided BPM. If the --jams option is
specified the script will also save the output as a JAMS file. Note that the
JAMS file uses the original note onset/offset times estimated by the algorithm
and ignores the provided BPM value.

Note: Melodia can work pretty well and is the result of several years of
research. The note segmentation/quantization code was hacked in about 30
minutes. Proceed at your own risk... :)

usage: audio_to_midi_melodia.py [-h] [--smooth SMOOTH]
                                [--minduration MINDURATION] [--jams]
                                infile outfile bpm


Examples:
python audio_to_midi_melodia.py --smooth 0.25 --minduration 0.1 --jams
                                ~/song.wav ~/song.mid 60
'''
downbeatbar = []
possiblevalues = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25,
                  4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75,
                  9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75,
                  13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16.0, 16.25, 16.5,
                  16.75, 17.0, 17.25, 17.5, 17.75, 18.0, 18.25, 18.5, 18.75, 19.0, 19.25, 19.5, 19.75, 20.0, 20.25,
                  20.5, 20.75, 21.0, 21.25, 21.5, 21.75, 22.0, 22.25, 22.5, 22.75, 23.0, 23.25, 23.5, 23.75, 24.0,
                  24.25, 24.5, 24.75, 25.0, 25.25, 25.5, 25.75, 26.0, 26.25, 26.5, 26.75, 27.0, 27.25, 27.5, 27.75,
                  28.0, 28.25, 28.5, 28.75, 29.0, 29.25, 29.5, 29.75, 30.0, 30.25, 30.5, 30.75, 31.0, 31.25, 31.5,
                  31.75]

whole_beats = [0, 16.0, 32.0, 48.0, 64.0, 80.0, 96.0, 112.0]


def save_midi(outfile, notes, tempo):
    track = 0
    time = 0
    midifile = MIDIFile(1)

    # Add track name and tempo.
    midifile.addTrackName(track, time, "MIDI TRACK")
    midifile.addTempo(track, time, tempo)

    channel = 0
    volume = 100

    for note in notes:
        onset = note[0] * (tempo / 60.)
        duration = note[1] * (tempo / 60.)
        # duration = 1
        pitch = note[2]
        midifile.addNote(track, channel, pitch, onset, duration, volume)

    # And write it to disk.
    binfile = open(outfile, 'wb')
    midifile.writeFile(binfile)
    binfile.close()


def note_number_to_name(note_number):
    # Note names within one octave
    semis = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Ensure the note is an int
    note_number = int(np.round(note_number))

    # Get the semitone and the octave, and concatenate to create the name
    return semis[note_number % 12] + "-" + str(note_number // 12 - 1)


def midi_to_notes(midi, fs, hop, smooth, minduration):
    # smooth midi pitch sequence first
    if (smooth > 0):
        filter_duration = smooth  # in seconds
        filter_size = int(filter_duration * fs / float(hop))
        if filter_size % 2 == 0:
            filter_size += 1
        midi_filt = medfilt(midi, filter_size)
    else:
        midi_filt = midi
    # print(len(midi),len(midi_filt))

    notes = []
    p_prev = None
    duration = 0
    onset = 0
    for n, p in enumerate(midi_filt):
        if p == p_prev:
            duration += 1
        else:
            # treat 0 as silence
            if p_prev > 0:
                # add note
                duration_sec = duration * hop / float(fs)
                # only add notes that are long enough
                if duration_sec >= minduration:
                    onset_sec = onset * hop / float(fs)
                    notes.append((onset_sec, duration_sec, p_prev))

            # start new note
            onset = n
            duration = 1
            p_prev = p

    # add last note
    if p_prev > 0:
        # add note
        duration_sec = duration * hop / float(fs)
        onset_sec = onset * hop / float(fs)
        notes.append((onset_sec, duration_sec, p_prev))

    return notes


def hz2midi(hz):
    # convert from Hz to midi note
    hz_nonneg = hz.copy()
    idx = hz_nonneg <= 0
    hz_nonneg[idx] = 1
    midi = 69 + 12 * np.log2(hz_nonneg / 440.)
    midi[idx] = 0

    # round
    midi = np.round(midi)

    return midi


def audio_to_midi_melodia(infile, outfile, bpm, smooth=0.25, minduration=0.1):
    # define analysis parameters
    fs = 44100
    hop = 128

    # load audio using librosa
    print("Loading audio...")
    data, sr = soundfile.read(infile)
    # mixdown to mono if needed
    if len(data.shape) > 1 and data.shape[1] > 1:
        data = data.mean(axis=1)
    # resample to 44100 if needed
    if sr != fs:
        data = resampy.resample(data, sr, fs)
        sr = fs

    # extract melody using melodia vamp plugin
    print("Extracting melody f0 with MELODIA...")
    melody = vamp.collect(data, sr, "mtg-melodia:melodia",
                          parameters={"voicing": 0.2})

    # hop = melody['vector'][0]
    pitch = melody['vector'][1]

    # impute missing 0's to compensate for starting timestamp
    pitch = np.insert(pitch, 0, [0] * 8)

    # debug
    # np.asarray(pitch).dump('f0.npy')
    # print(len(pitch))

    # convert f0 to midi notes
    print("Converting Hz to MIDI notes...")
    midi_pitch = hz2midi(pitch)

    # segment sequence into individual midi notes
    notes = midi_to_notes(midi_pitch, fs, hop, smooth, minduration)

    # print notes

    # save note sequence to a midi file
    print("Saving MIDI to disk...")
    save_midi(outfile, notes, bpm)

    print("Conversion complete.")


def audio_to_midi_notes(infile, fs=44100, smooth=0.001, minduration=0.11, speed=100):
    # define analysis parameters
    hop = 128

    # load audio using librosa
    print("Loading audio...")
    data, sr = soundfile.read(infile)
    # mixdown to mono if needed
    if len(data.shape) > 1 and data.shape[1] > 1:
        data = data.mean(axis=1)
    # resample to 44100 if needed
    if sr != fs:
        data = resampy.resample(data, sr, fs)
        sr = fs

    # extract melody using melodia vamp plugin
    print("Extracting melody f0 with MELODIA...")
    melody = vamp.collect(data, sr, "mtg-melodia:melodia",
                          parameters={"voicing": 0.2})

    # hop = melody['vector'][0]
    pitch = melody['vector'][1]

    # impute missing 0's to compensate for starting timestamp
    pitch = np.insert(pitch, 0, [0] * 8)

    # convert f0 to midi notes
    print("Converting Hz to MIDI notes...")
    midi_pitch = hz2midi(pitch)

    # segment sequence into individual midi notes
    notes = midi_to_notes(midi_pitch, fs, hop, smooth, minduration)

    # print notes
    print("Conversion complete.")

    named_notes = []

    for note in notes:
        nn = []

        start = note[0] * (speed / 60.0)
        duration = note[1] * (speed / 60.0)

        start = float(min(possiblevalues, key=lambda x: abs(x - start)))
        duration = float(min(possiblevalues, key=lambda x: abs(x - duration)))

        nn.append(start)
        nn.append(duration)
        nn.append(note_number_to_name(note[2]))
        named_notes.append(nn)

    turn = 0
    keep = 0

    added_notes = []

    for note in named_notes:

        start = note[0]
        duration = note[1]
        name = note[2]

        if math.floor(float(start) / 4) > math.floor(keep / 4):
            if math.floor(float(start) / 4) == float(start) / 4:
                if math.floor(float(start) / 4) - math.floor(keep / 4) <= 1:
                    added_notes.append([start, duration, name])
                else:
                    for i in range(0, int(math.floor(float(start) / 4 - math.floor(keep / 4)))):
                        none_start = math.floor(float(start) / 4) * 4 - (
                                (int(math.floor(float(start) / 4 - math.floor(keep / 4))) - 1 - i) * 4);
                        added_notes.insert(turn, [none_start, start - none_start, "None"])
                        turn += 1
                    added_notes.append([start, duration, name])

            else:
                for i in range(0, int(math.floor(float(start) / 4 - math.floor(keep / 4)))):
                    none_start = math.floor(float(start) / 4) * 4 - (
                            (int(math.floor(float(start) / 4 - math.floor(keep / 4))) - 1 - i) * 4)
                    added_notes.insert(turn, [none_start, start - none_start, "None"])
                    turn += 1
                added_notes.append([start, duration, name])
        else:
            added_notes.append([start, duration, name])
        keep = start
        turn += 1

    return added_notes


def get_ui_note_name(note):
    return note.split("|")[0]


def get_ui_note_beat(note):
    return int(note.split("|")[1])


def cmp_ui_beat_case(s1, s2):
    s1 = int(s1.split('|')[1])
    s2 = int(s2.split('|')[1])
    if s1 < s2:
        return -1
    if s1 > s2:
        return 1
    return 0
def detach_down_beats(ui_input):
    global downbeatbar
    firstbeat = True
    detached_notes = []
    for i in range(0,len(ui_input)):
        if i == len(ui_input)-1:
            n_beat = 0
        else:
            n_beat = get_ui_note_beat(ui_input[i + 1])
        beat = get_ui_note_beat(ui_input[i])
        name = get_ui_note_name(ui_input[i])
        if beat < 0:
            if firstbeat:
                if beat != -16:
                    if n_beat >= 0:
                        downbeatbar.append(['None',4])
                        firstbeat = False
                        continue
                    else:
                        beatneeded = (16 - abs(beat)) * 0.25
                        downbeatbar.append(['None',beatneeded])
                        firstbeat = False

            if n_beat >= 0:
                beatneeded = abs(beat)*0.25
            else:
                beatneeded = (abs(beat)-abs(n_beat))*0.25
            downbeatbar.append([string.capitalize(name).encode('raw_unicode_escape'),beatneeded])
        else:
            detached_notes.append("%s|%d" % (name, beat))
            print "note appended " + "%s|%d" % (name, beat)
    if downbeatbar == []:
        downbeatbar = [[None,4]]
    print "the downbeatbar is " + str(downbeatbar)
    print "the detached bar is" + str(detached_notes)
    return detached_notes

def fill_ui_beats(ui_beats):
    ui_beats = sorted(ui_beats, cmp_ui_beat_case)

    filled_notes = ui_beats
    for c_whole_beat in whole_beats:

        checked = False
        for i in range(0, len(ui_beats)):
            beat = get_ui_note_beat(ui_beats[i])
            name = get_ui_note_name(ui_beats[i])
            if c_whole_beat == 0.0:
                checked = True
                if c_whole_beat == beat:
                    break
                else:
                    filled_notes.insert(i, "%s|%d" % (name, c_whole_beat))
                    break
                filled_notes.insert(i, "%s|%d" % (name, c_whole_beat))
            if c_whole_beat <= beat < c_whole_beat * 16.0:
                checked = True
                if c_whole_beat == beat:
                    break
                else:
                    if c_whole_beat == 0.0:
                        filled_notes.insert(i, "%s|%d" % (name, c_whole_beat))
                    else:
                        filled_notes.insert(i, "%s|%d" % ('None', c_whole_beat))
                    break
            else:
                continue

        if not checked:
            filled_notes.append("%s|%d" % ('None', c_whole_beat))

    return filled_notes


def ui_beats_to_notes(filled_ui_beats):
    notes = []
    first_not_none_notes = 'C-4'  # first_not_none_notes = 'None'
    for i in range(0, len(filled_ui_beats)):
        c = filled_ui_beats[i]
        n = string.capitalize(get_ui_note_name(c))
        if n != 'None':
            first_not_none_notes = n
            break

    for i in range(0, len(filled_ui_beats)):
        c = filled_ui_beats[i]
        next = None
        if i == len(filled_ui_beats) - 1:
            next = "None|128"
        else:
            next = filled_ui_beats[i + 1]

        c_beat = get_ui_note_beat(c)
        n_beat = get_ui_note_beat(next)

        if (n_beat - c_beat) // 16 > 0:
            duration = 4.0
        else:
            duration = ((n_beat - c_beat) % 16) * 0.25

        if c_beat == 0:
            n = string.capitalize(get_ui_note_name(c))
            # beat 1 can't be none.s
            if n == 'None':
                n = first_not_none_notes
                notes.append([0.0, duration, n])
            else:
                notes.append([0.0, duration, n])
        else:
            notes.append([c_beat * 0.25, duration, string.capitalize(get_ui_note_name(c))])
    return notes


def notes_to_ui(filled_ui_beats):
    global downbeatbar
    accumulate = 0.0
    ui_beats = []
    print "ready to return " + str(filled_ui_beats)
    for i in downbeatbar:
        name = i[0].replace('#', '')
        ui_beats.append("%s|%d" % (name, (-4 + accumulate)*4))
        accumulate += i[1]
    for i in filled_ui_beats:
        name = i[2].replace('#', '')
        ui_beats.append("%s|%d" % (name, i[0] * 4))
    return sorted(ui_beats, cmp_ui_beat_case)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        data_raw = eval(sys.argv[1])
        downbeatbar = eval(sys.argv[2])

        norepeatmusictheory.determinelefthand(data_raw, downbeatbar, nameoffile='finalversionAd.wav')
        print 'Music has been mixed.'
    else:
        print 'Miss data argument.'
    # c = ['D-6|1', 'C-6|13', 'C-5|14', 'C-3|15', 'D-1|17', 'D-6|24', 'C-6|32', 'C-6|47', 'C-6|53']
    # d = fill_ui_beats(c)
    # e = ui_beats_to_notes(d)
    # print c
    # print d
    # print e

# notes = audio_to_midi_notes(infile="./sample/humming-star.wav",
#                             smooth=0.001, minduration=0.11, speed=100)
# print notes

# for note in notes:
#     print note


# save_midi("temp.mid", notes, 140)
