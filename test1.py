

# Import modules including Mingus and midi2audio
from mingus.containers import Note,NoteContainer, Bar,Track,Composition,Suite
from mingus.midi import midi_file_out,midi_file_in
from mingus.containers.instrument import MidiInstrument, MidiPercussionInstrument,Guitar,Piano
from mingus.midi.fluidsynth import FluidSynthSequencer
from threading import Thread
from midi2audio import FluidSynth
from pydub import AudioSegment
import os
import time
player1 = FluidSynthSequencer()
player2 = FluidSynthSequencer()
timeconstant = 400.05
from mingus.midi import fluidsynth
fluidsynth.init('Timbre.sf2',player1,file='x1.wav')

# Set up the Bar objects and fill them with notes
b = Bar()
b2 = Bar()
b3 = Bar()
b4 = Bar()
b5 = Bar()
b6 = Bar()
b7 = Bar()
b8 = Bar()
t = Track()
t2 = Track()
t3 = Track()
b.place_notes("C-3", 1)
b.place_notes("E-2", 1)
b.place_notes("G-3", 2)
b2.place_notes("A-4", 2)
b2.place_notes("G-5", 0.5)
b2.place_notes("G-5", 0.5)
b2.place_notes("G-5", 0.5)
b2.place_notes("G-5", 0.5)
b3.place_notes("F-5", 0.5)
b3.place_notes("F-5", 0.5)
b3.place_notes("F-5", 0.5)
b3.place_notes("F-5", 0.5)
b3.place_notes("E-5", 0.5)
b3.place_notes("E-5", 0.5)
b3.place_notes("E-5", 0.5)
b3.place_notes("E-5", 0.5)
b4.place_notes("D-5", 0.5)
b4.place_notes("D-5", 0.5)
b4.place_notes("D-5", 0.5)
b4.place_notes("D-5", 0.5)
b4.place_notes("C-5", 2)
b5.place_notes("C-3",1)
b5.place_notes("C-4",1)
b5.place_notes("G-2",1)
b5.place_notes("G-3",1)
b6.place_notes("F-2",1)
b6.place_notes("F-3",1)
b6.place_notes("C-2",1)
b6.place_notes("C-3",1)
b7.place_notes("F-2",1)
b7.place_notes("F-3",1)
b7.place_notes("C-2",1)
b7.place_notes("C-3",1)
b8.place_notes("G-2",1)
b8.place_notes("G-3",1)
b8.place_notes("C-3",1)
b8.place_notes("C-4",1)
# Add bars to two tracks, one is the melody, one is the chord harmony
t.add_bar(b)
t.add_bar(b2)
t.add_bar(b3)
t.add_bar(b4)
t.add_bar(b)
t.add_bar(b2)
t.add_bar(b3)
t.add_bar(b4)

t2.add_bar(b5)
t2.add_bar(b6)
t2.add_bar(b7)
t2.add_bar(b8)
t2.add_bar(b5)
t2.add_bar(b6)
t2.add_bar(b7)
t2.add_bar(b8)

t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
t3.add_notes("D",0.5)
# Add instrument attribute to both tracks, track "t" should be guitar and track "t2" should be piano
guitar = MidiInstrument()
guitar.instrument_nr = 3
t.instrument = guitar

player1.play_Track(t2,channel=9,bpm=100)
fluidsynth.initialized = False
fluidsynth.init('Timbre.sf2',player2,file='x2.wav')
player2.play_Track(t3,channel=9,bpm=100)
midi_file_out.write_Track('x.mid',t,bpm=timeconstant)
FluidSynth('Timbre.sf2').midi_to_audio('x.mid', 'x.wav')

# Define and add tracks to Composition
# c = Composition()
#
# c.add_track(t)
#
# c.add_track(t2)

# Use the write_composition function to put composition into midi
#midi_file_out.write_Composition('star6.mid',c,bpm=120)

# Use the function in midi2audio module and export that into flac file, mp3 and wav work as well
#FluidSynth('Timbre.sf2').midi_to_audio('star6.mid', 'star6.mp3')


sound1 = AudioSegment.from_wav("x1.wav")
sound2 = AudioSegment.from_wav("x.wav")
sound3 = AudioSegment.from_wav("x2.wav")

combined = sound1.overlay(sound3.overlay(sound2))
time.sleep(1)
combined.export("combo.wav", format='wav')
print os.getcwd()
