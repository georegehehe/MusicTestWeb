import itertools
import math
import os
import random
import shutil
import time

from midi2audio import FluidSynth
from mingus.containers import Note, Bar, Track
from mingus.containers.instrument import MidiInstrument
from mingus.containers.mt_exceptions import NoteFormatError
from mingus.midi import fluidsynth, midi_file_out
from mingus.midi.fluidsynth import FluidSynthSequencer
from pydub import AudioSegment

import finalpercussion
import latestmusic

snareplayer = FluidSynthSequencer()
baseplayer = FluidSynthSequencer()
highhatplayer = FluidSynthSequencer()
cymbalplayer = FluidSynthSequencer()
tomplayer = FluidSynthSequencer()
lefthandplayer = FluidSynthSequencer()
righthandplayer = FluidSynthSequencer()

basse = MidiInstrument()
basse.instrument_nr = 32

guitar = MidiInstrument()
guitar.instrument_nr = 25

string = MidiInstrument()
string.instrument_nr = 48

brass = MidiInstrument()
brass.instrument_nr = 61

synth = MidiInstrument()
synth.instrument_nr = 81

frhorn = MidiInstrument()
frhorn.instrument_nr = 60

electricguitar = MidiInstrument()
electricguitar.instrument_nr = 30

brightpiano = MidiInstrument()
brightpiano.instrument_nr = 1
timeconstant = 400.05
reserved = ""
speed1 = 100
speed2 = 140
offbeat = False
first_time = True
firstbar = True
lastbar = False
soundtrue = True
highorlow = random.randint(0,1)
musicpiece1 = []
musicpiece2 = []
musicpiece3 = ""
musicpiece4 = ""
musicpiece5 = ""
musicpiece6 = ""
musicpiece7 = ""
musicpiece8 = ""
part1 = []
part2 = []
part3 = []
part4 = []
part5 = []
part6 = []
part7 = []
part8 = []

chordI = [["C-2","E-2","G-2"]]
chordII = [["D-2","F-2","A-2"]]
chordIII = [["E-2","G-2","B-2"]]
chordIV = [["F-2","A-2","C-3"]]
chordV = [["G-2","B-2","D-3"]]
chordVI = [["A-2","C-3","E-3"]]
chordV7 = [["G-2","B-2","D-3"]]
chordIi = [["C-3","E-3","G-3"]]
simple_chordI = ["C-2",["E-2","G-2","C-3"]]
simple_chordII = ["D-2",["F-2","A-2","D-3"]]
simple_chordIII = ["E-2",["G-2","B-2","E-3"]]
simple_chordIV = ["F-2",["A-2","C-3","F-3"]]
simple_chordV = ["G-2",["B-2","D-3","G-3"]]
simple_chordVI = ["A-2",["C-3","E-3","A-3"]]
simple_chordV7 = ["G-2",["B-2","D-3","F-3"]]
simple_chordIi = ["C-3",["E-3","G-3","C-4"]]
complex_chordI = [["C-2","E-2","G-2","C-3"],"E-2","G-2","C-3"]
complex_chordII = [["D-2","F-2","A-2","D-3"],"F-2","A-2","D-3"]
complex_chordIII = [["E-2","G-2","B-2","E-3"],"G-2","B-2","E-3"]
complex_chordIV = [["F-2","A-2","C-3","F-3"],"A-2","C-3","F-3"]
complex_chordV = [["G-2","B-2","D-3","G-3"],"B-2","D-3","G-3"]
complex_chordVI = [["A-2","C-3","E-3","A-3"],"C-3","E-3","A-3"]
complex_chordV7 = [["G-2","B-2","D-3","F-3"],"B-2","D-3","F-3"]
complex_chordIi = [["C-3","E-3","G-3","C-4"],"E-3","G-3","C-4"]
snare = Note()
snare.from_int(26)
highhat = Note()
highhat.from_int(30)
base = Note()
base.from_int(23)
hightom = Note()
hightom.from_int(38)
midtom = Note()
midtom.from_int(36)
lowtom = Note()
lowtom.from_int(35)
cymbal = Note()
cymbal.from_int(37)
startbasepercussion = [base,None,base,None]
starthighhatpercussion = [highhat,None,highhat,None]
transitioncymbalpercussion = [cymbal]
transitionsnarepercussion = [snare,snare,snare,snare,snare]
basepercussion = [base,None,None,base]
highhatpercussion = [highhat,highhat,highhat,highhat]
snarepercussion = [None,None,snare,None]
cymbalpercussion = []
tompercussion = []
major_chords = [simple_chordI,simple_chordIV,simple_chordV,simple_chordIi,complex_chordI,complex_chordIV,complex_chordV,
                complex_chordIi]
minor_chords = [simple_chordII,simple_chordIII,simple_chordVI,simple_chordV7,complex_chordII,complex_chordIII
    ,complex_chordVI,complex_chordV7]
left_hand_music = []
right_hand_list = []
right_hand_music = []
downbeatbar = Bar()
righthandbar = Bar()
synthtrack1 = Track()
synthtrack1.instrument = synth
electricguitartrack1 = Track()
electricguitartrack1.instrument = electricguitar
brasstrack1 = Track()
brasstrack1.instrument = brass
bassetrack1 = Track()
bassetrack1.instrument = basse
strintrack1 = Track()
strintrack1.instrument = string
guitartrack1 = Track()
guitartrack1.instrument = guitar
frhorntrack1 = Track()
frhorntrack1.instrument = frhorn
righthandtrack1 = Track()
righthandtrack1.instrument = brightpiano
righthandtrack2 = Track()
lefthandtrack1 = Track()
lefthandtrack2 = Track()
lefthandtrack3 = Track()
lefthandtrack4 = Track()
tracknum = 0
snaretrack1 = Track()
snaretrack2 = Track()
snaretrack3 = Track()
snaretrack4 = Track()
highhattrack1 = Track()
highhattrack2 = Track()
highhattrack3 = Track()
highhattrack4 = Track()
basetrack1 = Track()
basetrack2 = Track()
basetrack3 = Track()
basetrack4 = Track()
cymbaltrack1 = Track()
cymbaltrack2 = Track()
cymbaltrack3 = Track()
cymbaltrack4 = Track()
tomtrack1 = Track()
tomtrack2 = Track()
tomtrack3 = Track()
tomtrack4 = Track()

def addsimplechord(chord):
    for x in chord:
        lefthandtrack2.add_notes(x, 1)
def addcomplexchord(chord):
    for x in chord:
        guitartrack1.add_notes(x,1)
        guitartrack1.add_notes(x,0.5)
        guitartrack1.add_notes(x,0.25)
        guitartrack1.add_notes(x,0.25)
def addchord(chord):
    for x in chord:
        guitartrack1.add_notes(x,2)
def addchordfin(chord):
    for x in chord:
        lefthandtrack4.add_notes(x,2)
def addlefthand(var1,func1,mode):
    if mode == "simple":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1(simple_chordI)
                if highorlow == 1:
                    func1(simple_chordIi)
            if i == 2:
                func1(simple_chordII)
            if i == 3:
                func1(simple_chordIII)
            if i == 4:
                func1(simple_chordIV)
            if i == 5:
                func1(simple_chordV)
            if i == 6:
                func1(simple_chordVI)
            if i == 7:
                func1(simple_chordV7)
        print "simple"

    if mode == "chordinit":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1(chordI)
                if highorlow == 1:
                    func1(chordIi)
            if i == 2:
                func1(chordII)
            if i == 3:
                func1(chordIII)
            if i == 4:
                func1(chordIV)
            if i == 5:
                func1(chordV)
            if i == 6:
                func1(chordVI)
            if i == 7:
                func1(chordV7)
        print "chord"
    if mode == "chordfin":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1(chordI)
                if highorlow == 1:
                    func1(chordIi)
            if i == 2:
                func1(chordII)
            if i == 3:
                func1(chordIII)
            if i == 4:
                func1(chordIV)
            if i == 5:
                func1(chordV)
            if i == 6:
                func1(chordVI)
            if i == 7:
                func1(chordV7)
    if mode == "complex":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1(chordI)
                if highorlow == 1:
                    func1(chordIi)
            if i == 2:
                func1(chordII)
            if i == 3:
                func1(chordIII)
            if i == 4:
                func1(chordIV)
            if i == 5:
                func1(chordV)
            if i == 6:
                func1(chordVI)
            if i == 7:
                func1(chordV7)
        print "complex"
    if mode == "basic":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1.add_notes('C-2',2)
                if highorlow == 1:
                    func1.add_notes('C-3', 2)
            if i == 2:
                func1.add_notes('D-2', 2)
            if i == 3:
                func1.add_notes('E-2', 2)
            if i == 4:
                func1.add_notes('F-2', 2)
            if i == 5:
                func1.add_notes('G-2', 2)
            if i == 6:
                func1.add_notes('A-2', 2)
            if i == 7:
                func1.add_notes('B-2', 2)
    if mode == "basiccomplex":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1.add_notes('C-2',1)
                    func1.add_notes('C-2',0.5)
                    func1.add_notes('C-2',0.25)
                    func1.add_notes('C-2',0.25)
                if highorlow == 1:
                    func1.add_notes('C-3', 1)
                    func1.add_notes('C-3', 0.5)
                    func1.add_notes('C-3', 0.25)
                    func1.add_notes('C-3', 0.25)
            if i == 2:
                func1.add_notes('D-2', 1)
                func1.add_notes('D-2', 0.5)
                func1.add_notes('D-2', 0.25)
                func1.add_notes('D-2', 0.25)
            if i == 3:
                func1.add_notes('E-2', 1)
                func1.add_notes('E-2', 0.5)
                func1.add_notes('E-2', 0.25)
                func1.add_notes('E-2', 0.25)
            if i == 4:
                func1.add_notes('F-2', 1)
                func1.add_notes('F-2', 0.5)
                func1.add_notes('F-2', 0.25)
                func1.add_notes('F-2', 0.25)
            if i == 5:
                func1.add_notes('G-2', 1)
                func1.add_notes('G-2', 0.5)
                func1.add_notes('G-2', 0.25)
                func1.add_notes('G-2', 0.25)
            if i == 6:
                func1.add_notes('A-2', 1)
                func1.add_notes('A-2', 0.5)
                func1.add_notes('A-2', 0.25)
                func1.add_notes('A-2', 0.25)
            if i == 7:
                func1.add_notes('B-2', 1)
                func1.add_notes('B-2', 0.5)
                func1.add_notes('B-2', 0.25)
                func1.add_notes('B-2', 0.25)
    if mode == "basichigh":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1.add_notes('C-3',2)
                if highorlow == 1:
                    func1.add_notes('C-4', 2)
            if i == 2:
                func1.add_notes('D-3', 2)
            if i == 3:
                func1.add_notes('E-3', 2)
            if i == 4:
                func1.add_notes('F-3', 2)
            if i == 5:
                func1.add_notes('G-3', 2)
            if i == 6:
                func1.add_notes('A-3', 2)
            if i == 7:
                func1.add_notes('B-3', 2)
    if mode == "basiccomplexhigh":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1.add_notes('C-3',1)
                    func1.add_notes('C-3',0.5)
                    func1.add_notes('C-3',0.25)
                    func1.add_notes('C-3',0.25)
                if highorlow == 1:
                    func1.add_notes('C-4', 1)
                    func1.add_notes('C-4', 0.5)
                    func1.add_notes('C-4', 0.25)
                    func1.add_notes('C-4', 0.25)
            if i == 2:
                func1.add_notes('D-3', 1)
                func1.add_notes('D-3', 0.5)
                func1.add_notes('D-3', 0.25)
                func1.add_notes('D-3', 0.25)
            if i == 3:
                func1.add_notes('E-3', 1)
                func1.add_notes('E-3', 0.5)
                func1.add_notes('E-3', 0.25)
                func1.add_notes('E-3', 0.25)
            if i == 4:
                func1.add_notes('F-3', 1)
                func1.add_notes('F-3', 0.5)
                func1.add_notes('F-3', 0.25)
                func1.add_notes('F-3', 0.25)
            if i == 5:
                func1.add_notes('G-3', 1)
                func1.add_notes('G-3', 0.5)
                func1.add_notes('G-3', 0.25)
                func1.add_notes('G-3', 0.25)
            if i == 6:
                func1.add_notes('A-3', 1)
                func1.add_notes('A-3', 0.5)
                func1.add_notes('A-3', 0.25)
                func1.add_notes('A-3', 0.25)
            if i == 7:
                func1.add_notes('B-3', 1)
                func1.add_notes('B-3', 0.5)
                func1.add_notes('B-3', 0.25)
                func1.add_notes('B-3', 0.25)
    if mode == "basic2":
        for i in var1:
            if i == 1:
                if highorlow == 0:
                    func1.add_notes('E-2',2)
                if highorlow == 1:
                    func1.add_notes('E-3', 2)
            if i == 2:
                func1.add_notes('F-2', 2)
            if i == 3:
                func1.add_notes('G-2', 2)
            if i == 4:
                func1.add_notes('A-2', 2)
            if i == 5:
                func1.add_notes('B-2', 2)
            if i == 6:
                func1.add_notes('C-2', 2)
            if i == 7:
                func1.add_notes('D-2', 2)



def transnum(var1,var2):
    global reserved
    for i in var1:
        if i[0] == "C":
            var2.append("1")
            reserved = "1"
        if i[0] == "D":
            var2.append("2")
            reserved = "2"
        if i[0] == "E":
            var2.append("3")
            reserved = "3"
        if i[0] == "F":
            var2.append("4")
            reserved = "4"
        if i[0] == "G":
            var2.append("5")
            reserved = "5"
        if i[0] == "A":
            var2.append("6")
            reserved = "6"
        if i[0] == "B":
            var2.append("7")
            reserved = "7"
        if i[0] == "N":
            var2.append(reserved)
    return var2

def determinelefthand(right_hand_music,down_beat_music,nameoffile='music.mp3'):
    global musicpiece2,musicpiece1
    global part1,part2
    global first_time
    global downbeatbar
    global soundtrue
    for i in down_beat_music:
        if i[0] == "None":
            print "went through None"
            lefthandtrack2.add_notes(None, i[1])
        else:
            print "went through normal"
            lefthandtrack2.add_notes(i[0], i[1])
    for i in right_hand_music:
        if i[2] == "None":
            right_hand_list.append([i[2], i[1]])
            if math.floor(i[0] / 2) == i[0] / 2:
                left_hand_music.append(i[2])
                first_time = False
                if i[1] > 2:
                    if math.floor((i[0] + i[1]) / 2) > math.floor(i[0] / 2):
                        left_hand_music.append(i[2])
            else:
                if i[1] > 2:
                    first_time = False
                    left_hand_music.append(i[2])
                else:
                    if math.floor((i[0] + i[1]) / 2) > math.floor(i[0] / 2) and math.floor((i[0]+i[1])/2) != (i[0]+i[1])/2:
                        first_time = False
                        left_hand_music.append(i[2])
        else:
            right_hand_list.append([i[2], i[1]])
            if math.floor(i[0] / 2) == i[0] / 2:
                left_hand_music.append(i[2])
                first_time = False
                if i[1] > 2:
                    if math.floor((i[0] + i[1]) / 2) > math.floor(i[0] / 2):
                        left_hand_music.append(i[2])
            else:
                if i[1] > 2:
                    first_time = False
                    left_hand_music.append(i[2])
                else:
                    if math.floor((i[0] + i[1]) / 2) > math.floor(i[0] / 2) and math.floor((i[0]+i[1])/2) != (i[0]+i[1])/2:
                        first_time = False
                        left_hand_music.append(i[2])



    print left_hand_music
    for i in range(0,16):
        if i < 9:
            part1.append(left_hand_music[i])
        if 8 <= i < 16:
            part2.append(left_hand_music[i])
    part2.append("C-4")
    musicpiece1 = transnum(part1,musicpiece1)
    musicpiece2 = transnum(part2,musicpiece2)
    for i in range(0, 2):
        print i
        if i == 0:
            print musicpiece1
            chords_needed = latestmusic.determination(musicpiece1,1)
            del chords_needed[-1]
            print chords_needed
        if i == 1:
            musicpiece2.insert(0,str(chords_needed[-1]))
            chords_needed2 = latestmusic.determination(musicpiece2,2)
            del chords_needed2[-1]
            print chords_needed2
    print lefthandtrack2
    righthandtrack1.add_notes(None,4)
    guitartrack1.add_notes(None,4)
    strintrack1.add_notes(None,4)
    bassetrack1.add_notes(None,4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    brasstrack1.add_notes(None, 4)
    for i in range(0,9):
        electricguitartrack1.add_notes(None,4)
        synthtrack1.add_notes(None,4)
        frhorntrack1.add_notes(None,4)


    addlefthand(chords_needed, addchord, "chordinit")
    addlefthand(chords_needed2, addchord, "chordinit")
    addlefthand(chords_needed, addcomplexchord, "complex")
    addlefthand(chords_needed2, addcomplexchord, "complex")
    addlefthand(chords_needed, addsimplechord, "simple")
    addlefthand(chords_needed2, addsimplechord, "simple")
    addlefthand(chords_needed, addsimplechord, "simple")
    addlefthand(chords_needed2, addsimplechord, "simple")
    addlefthand(chords_needed, strintrack1,"basic")
    addlefthand(chords_needed2, strintrack1,"basic")
    addlefthand(chords_needed, strintrack1,"basic")
    addlefthand(chords_needed2, strintrack1,"basic")
    addlefthand(chords_needed, bassetrack1,"basic")
    addlefthand(chords_needed2, bassetrack1,"basic")
    addlefthand(chords_needed, bassetrack1,"basiccomplex")
    addlefthand(chords_needed2, bassetrack1,"basiccomplex")
    addlefthand(chords_needed, brasstrack1,"basichigh")
    addlefthand(chords_needed2, brasstrack1,"basichigh")
    addlefthand(chords_needed, electricguitartrack1,"basiccomplexhigh")
    addlefthand(chords_needed2, electricguitartrack1,"basiccomplexhigh")
    addlefthand(chords_needed, frhorntrack1,"basic2")
    addlefthand(chords_needed2,frhorntrack1,"basic2")
    sounditeration = 0.0
    soundtrue = True
    lastnote = 'C-4'
    print "righthandlist is : " + str(right_hand_list)
    for i in right_hand_list:
        if i[0] == "None":
            righthandtrack1.add_notes(None, i[1])
        else:
            righthandtrack1.add_notes(i[0], i[1])
    for i in right_hand_list:
        if sounditeration % 4 == 0 and sounditeration % 8 != 0:
            soundtrue = False
        elif sounditeration % 4 == 0 and sounditeration % 8 == 0:
            soundtrue = True
        else:
            if i[0] == "None":
                righthandtrack1.add_notes(None, i[1])
            else:
                righthandtrack1.add_notes(i[0], i[1])
            if soundtrue:
                if i[0] == "None":
                    synthtrack1.add_notes(None, i[1])
                else:
                    synthtrack1.add_notes(i[0], i[1])
            sounditeration += i[1]
            lastnote = i[0]
            print "normal sound iteration : " + str(sounditeration)
            continue
        if soundtrue:
            if i[0] == "None":
                synthtrack1.add_notes(None, i[1])
            else:
                synthtrack1.add_notes(i[0], i[1])
        else:
            if i[0] == "None":
                try:
                    synthtrack1.add_notes(lastnote[0],2)
                    synthtrack1.add_notes(None,2)
                except NoteFormatError:
                    synthtrack1.add_notes(None,4)
            else:
                synthtrack1.add_notes(i[0],2)
                synthtrack1.add_notes(None, 2)
        if i[0] == "None":
            righthandtrack1.add_notes(None, i[1])
        else:
            righthandtrack1.add_notes(i[0], i[1])
        lastnote = i[0]
        sounditeration += i[1]
        print str(sounditeration)
    synthtrack1.add_notes(None,4)
    synthtrack1.add_notes("C-3",4)
    lefthandtrack2.add_notes(None,4)
    righthandtrack1.add_notes(None,4)
    righthandtrack1.add_notes("C-3",4)
    guitartrack1.add_notes(None,4)
    guitartrack1.add_notes("C-3",4)
    strintrack1.add_notes(None,4)
    strintrack1.add_notes("C-3",4)
    brasstrack1.add_notes(None,4)
    brasstrack1.add_notes("C-3",4)
    bassetrack1.add_notes("C-3",0.75)
    bassetrack1.add_notes("E-3", 0.75)
    bassetrack1.add_notes("G-3", 1)
    bassetrack1.add_notes("C-4", 1.5)
    electricguitartrack1.add_notes(["C-3","E-3","G-3"],4)
    frhorntrack1.add_notes(None,4)
    frhorntrack1.add_notes("C",4)
    print brasstrack1
    print snaretrack2
    time.sleep(1)
    # lefthandmusicthinny.play_Bar(downbeatbar,channel=0,bpm=speed1)
    play(nameoffile)

'''
for i in left_hand_music:
    if i[0] == "C":
        addcomplexchord(complex_chordI)
    if i[0] == "D":
        addsimplechord(simple_chordII)
    if i[0] == "E":
        addsimplechord(simple_chordIII)
    if i[0] == "F":
        addsimplechord(simple_chordIV)
    if i[0] == "G":
        addcomplexchord(complex_chordV7)
    if i[0] == "A":
        addsimplechord(simple_chordVI)
    if i[0] == "B":
        addsimplechord(simple_chordV7)
        '''
[[0.0,3,"None"],[3.0,1,"G-4"],[4.0,1,"C-5"],[5.0,0.75,"G-4"],[5.75,0.25,"A-4"],[6.0,1,"B-4"],[7.0,1,"E-4"],[8.0,1,"A-4"],[9.0,0.75,"G-4"],[9.75,0.25,"F-4"],[10.0,1,"G-4"],[11.0,1,"C-4"],[12.0,1,"D-4"],[13.0,0.75,"D-4"],[13.75,0.25,"E-4"],[14.0,1,"F-4"],[15.0,0.75,"F-4"],[15.75,0.25,"G-4"],[16.0,1,"A-4"],[17.0,0.5,"B-4"],[17.5,0.5,"C-5"],[18.0,2,"D-5"]]
piece = [[0.0, 1.0, 'C-4'], [1.0, 1.0, 'C-4'], [2.0, 1.0, 'G-4'], [3.0, 1.0, 'G-4'], [4.0, 1.0, 'A-4'], [5.0, 1.0, 'A-4'], [6.0, 1.0, 'G-4'], [7.0, 1.0, 'F-4'], [8.0, 1.0, 'F-4'], [9.0, 1.0, 'E-4'], [10.0, 1.0, 'E-4'], [11.0, 1.0, 'D-4'], [12.0, 1.0, 'D-4'], [13.0, 1.0, 'C-4'], [14.0, 1.0, 'G-4'], [15.0, 1.0, 'G-4'], [16.0, 1.0, 'F-4'], [17.0, 1.0, 'F-4'], [18.0, 1.0, 'E-4'], [19.0, 1.0, 'E-4'], [20.0, 1.0, 'D-4'], [21.0, 1.0, 'G-4'], [22.0, 1.0, 'G-4'], [23.0, 1.0, 'F-4'], [24.0, 1.0, 'F-4'], [25.0, 1.0, 'E-4'], [26.0, 1.0, 'E-4'], [27.0, 1.0, 'D-4'], [28.0, 1.0, 'C-4'], [29.0, 0.5, 'C-4'], [29.5, 0.75, 'G-4'], [30.25, 0.5, 'G-4'], [30.75, 0.25, 'A-4'], [31.0, 0.25, 'A-4'], [31.25, 0.5, 'G-4'], [31.75, 0.25, 'F-4']]
piece2 = [[0.0, 0.75, 'G-4'], [0.75, 0.25, 'G-4'], [1.0, 0.75, 'G-4'], [1.75, 0.25, 'F-4'], [2.0, 0.75, 'E-4'], [2.75, 0.25, 'G-4'], [3.0, 0.75, 'C-5'], [3.75, 0.25, 'D-5'], [4.0, 0.75, 'E-5'], [4.75, 0.25, 'E-5'], [5.0, 0.75, 'E-5'], [5.75, 0.25, 'D-5'], [6.0, 1.0, 'C-5'], [7.0, 0.75, 'C-5'], [7.75, 0.25, 'B-4'], [8.0, 0.75, 'A-4'], [8.75, 0.25, 'A-4'], [9.0, 0.75, 'A-4'], [9.75, 0.25, 'B-4'], [10.0, 0.5, 'C-5'], [10.5, 0.5, 'B-4'], [11.0, 0.75, 'C-5'], [11.75, 0.25, 'A-4'], [12.0, 0.75, 'G-4'], [12.75, 0.25, 'A-4'], [13.0, 0.75, 'G-4'], [13.75, 0.25, 'E-4'], [14.0, 1.0, 'G-4'], [15.0, 0.75, 'G-4'], [15.75, 0.25, 'G-4'], [16.0, 0.75, 'G-4'], [16.75, 0.25, 'G-4'], [17.0, 0.75, 'G-4'], [17.75, 0.25, 'F-4'], [18.0, 0.75, 'E-4'], [18.75, 0.25, 'G-4'], [19.0, 0.75, 'C-5'], [19.75, 0.25, 'D-5'], [20.0, 0.75, 'E-5'], [20.75, 0.25, 'E-5'], [21.0, 0.75, 'E-5'], [21.75, 0.25, 'D-5'], [22.0, 1.0, 'C-5'], [23.0, 1.0, 'C-5'], [24.0, 1.0, 'D-5'], [25.0, 1.0, 'D-5'], [26.0, 1.0, 'C-5'], [27.0, 1.0, 'B-5'], [28.0, 4.0, 'C-5']]

[[0.0,2,"E-4"],[2.0,1.5,"None"],[3.5,0.5,"B-4"],[4.0,2,"None"],[6.0,2,"A-4"],[8.0,3,"A-4"],[11.0,1,"D-4"],[12.0,0.33,"D-4"],[12.33,0.33,"E-4"],[12.66,0.34,"F-4"],[13.0,1,"E-4"],[14.0,2,"G-4"],[16.0,2,"G-4"],[18.0,2,"G-4"],[20.0,1.0,"F-4"],[21.0,1.0,"E-4"],[22.0,1.5,"D-4"],[23.5,0.5,"E-4"],[24.0,1.75,"F-4"],[25.75,0.25,"F-4"],[26.0,2.0,"A-4"],[28.0,0.5,"B-4"],[28.5,0.5,"C-5"],[29.0,3,"G-4"]]
[[0.0,2,"E-5"],[2.0,2,"D-5"],[4.0,2,"C-5"],[6.0,2,"B-4"],[8.0,2,"A-4"],[10.0,2,"G-4"],[12.0,2,"A-4"],[14.0,1,"B-4"],[15.0,1,"G-4"]]
[[0.0, 3.0, 'D-5'], [3.0, 1.0, 'A-5'], [4.0, 3.0, 'F-3'], [7.0, 1.0, 'C-6'], [8.0, 2.0, 'B-3'], [10.0, 2.0, 'C-3'], [12.0, 2.0, 'C-6'], [14.0, 2.0, 'C-4'], [16.0, 1.0, 'A-4'], [17.0, 1.0, 'G-3'], [18.0, 2.0, 'A-4'], [20.0, 3.0, 'E-4'], [23.0, 0.5, 'D-5'], [23.5, 0.5, 'E-5'], [24.0, 1.0, 'A-5'], [25.0, 2.0, 'D-4'], [27.0, 1.0, 'F-3'], [28.0, 1.0, 'D-3'], [29.0, 3.0, 'G-5'], [32.0, 3.0, 'D-5'], [35.0, 1.0, 'G-4'], [36.0, 0.5, 'F-5'], [36.5, 3.0, 'F-3'], [39.5, 0.5, 'D-4'], [40.0, 1.0, 'A-5'], [41.0, 3.0, 'E-3'], [44.0, 0.5, 'C-5'], [44.5, 3.0, 'G-4'], [47.5, 0.25, 'E-3'], [47.75, 0.25, 'C-4'], [48.0, 1.0, 'D-3'], [49.0, 3.0, 'B-4'], [52.0, 0.5, 'C-5'], [52.5, 3.0, 'F-4'], [55.5, 0.5, 'F-3'], [56.0, 1.0, 'B-4'], [57.0, 2.0, 'G-5'], [59.0, 0.34, 'G-4'], [59.34, 0.33, 'C-4'], [59.67, 0.33, 'E-4'], [60.0, 1.0, 'E-5'], [61.0, 3.0, 'B-3'], [64.0, 0.5, 'E-3'], [64.5, 2.0, 'F-3'], [66.5, 0.33, 'D-4'], [66.83, 0.34, 'C-5'], [67.17, 0.33, 'C-3'], [67.5, 0.5, 'E-3'], [68.0, 2.0, 'B-4'], [70.0, 2.0, 'G-3'], [72.0, 1.0, 'A-5'], [73.0, 2.0, 'F-5'], [75.0, 1.0, 'C-4'], [76.0, 2.0, 'B-3'], [78.0, 2.0, 'C-6'], [80.0, 1.0, 'G-5'], [81.0, 3.0, 'A-4'], [84.0, 0.5, 'G-5'], [84.5, 3.0, 'G-5'], [87.5, 0.5, 'C-3'], [88.0, 0.34, 'G-3'], [88.34, 2.0, 'B-3'], [90.34, 0.25, 'A-4'], [90.59, 0.25, 'G-3'], [90.84, 0.5, 'D-5'], [91.34, 0.33, 'D-3'], [91.67, 0.33, 'G-3'], [92.0, 1.0, 'B-4'], [93.0, 3.0, 'E-3'], [96.0, 2.0, 'A-4'], [98.0, 1.0, 'D-3'], [99.0, 0.25, 'D-3'], [99.25, 0.5, 'F-4'], [99.75, 0.25, 'D-5'], [100.0, 2.0, 'B-4'], [102.0, 2.0, 'E-4'], [104.0, 2.0, 'C-6'], [106.0, 2.0, 'F-5'], [108.0, 3.0, 'E-4'], [111.0, 1.0, 'F-3'], [112.0, 2.0, 'G-4'], [114.0, 2.0, 'E-5'], [116.0, 1.0, 'A-5'], [117.0, 3.0, 'E-4'], [120.0, 0.5, 'D-5'], [120.5, 3.0, 'E-4'], [123.5, 0.5, 'D-4'], [124.0, 1.0, 'D-4'], [125.0, 2.0, 'E-4'], [127.0, 1.0, 'E-3']]
[[0.0, 2.0, 'A-4'], [2.0, 2.0, 'A-5'], [4.0, 4.0, 'D-4'], [8.0, 1.0, 'A-3'], [9.0, 2.0, 'A-3'], [11.0, 1.0, 'E-3'], [12.0, 2.0, 'F-3'], [14.0, 2.0, 'B-5'], [16.0, 4.0, 'E-4'], [20.0, 1.0, 'C-3'], [21.0, 3.0, 'G-5'], [24.0, 4.0, 'A-4'], [28.0, 1.0, 'D-5'], [29.0, 1.0, 'F-3'], [30.0, 2.0, 'E-5'], [32.0, 2.0, 'B-4'], [34.0, 2.0, 'A-5'], [36.0, 1.0, 'G-4'], [37.0, 2.0, 'A-3'], [39.0, 1.0, 'C-4'], [40.0, 2.0, 'G-3'], [42.0, 2.0, 'B-5'], [44.0, 2.0, 'A-3'], [46.0, 2.0, 'C-6'], [48.0, 1.0, 'G-5'], [49.0, 3.0, 'A-4'], [52.0, 3.0, 'A-3'], [55.0, 0.5, 'A-3'], [55.5, 0.5, 'F-3'], [56.0, 1.0, 'A-4'], [57.0, 3.0, 'G-3'], [60.0, 1.0, 'G-4'], [61.0, 2.0, 'F-4'], [63.0, 1.0, 'F-4'], [64.0, 0.25, 'A-3'], [64.25, 0.5, 'F-5'], [64.75, 2.0, 'A-4'], [66.75, 0.25, 'A-4'], [67.0, 1.0, 'A-4'], [68.0, 0.33, 'F-3'], [68.33, 2.0, 'C-6'], [70.33, 1.0, 'D-3'], [71.33, 0.33, 'A-3'], [71.66, 0.34, 'F-4'], [72.0, 0.33, 'E-3'], [72.33, 0.34, 'C-4'], [72.67, 0.34, 'C-5'], [73.01, 1.0, 'B-5'], [74.01, 0.33, 'G-4'], [74.34, 1.0, 'B-3'], [75.34, 0.33, 'E-5'], [75.67, 0.33, 'G-5'], [76.0, 0.33, 'F-5'], [76.33, 0.25, 'F-5'], [76.58, 0.5, 'A-5'], [77.08, 0.25, 'C-3'], [77.33, 0.33, 'D-4'], [77.66, 2.0, 'D-3'], [79.66, 0.34, 'E-3'], [80.0, 0.5, 'A-3'], [80.5, 0.5, 'A-4'], [81.0, 1.0, 'D-4'], [82.0, 2.0, 'A-4'], [84.0, 0.5, 'G-4'], [84.5, 1.0, 'C-4'], [85.5, 0.5, 'G-4'], [86.0, 2.0, 'F-5'], [88.0, 3.0, 'E-3'], [91.0, 0.33, 'B-3'], [91.33, 0.34, 'G-3'], [91.67, 0.33, 'F-4'], [92.0, 2.0, 'A-5'], [94.0, 1.0, 'F-3'], [95.0, 0.5, 'C-5'], [95.5, 0.5, 'G-3'], [96.0, 3.0, 'A-4'], [99.0, 1.0, 'A-3'], [100.0, 2.0, 'C-4'], [102.0, 2.0, 'G-3'], [104.0, 4.0, 'F-5'], [108.0, 1.0, 'E-3'], [109.0, 1.0, 'C-6'], [110.0, 2.0, 'D-3'], [112.0, 4.0, 'D-5'], [116.0, 1.0, 'F-3'], [117.0, 3.0, 'A-4'], [120.0, 4.0, 'C-4'], [124.0, 2.0, 'E-3'], [126.0, 2.0, 'C-6']]
[[0.0, 4.0, 'D-4'], [4.0, 2.0, 'G-5'], [6.0, 0.5, 'A-5'], [6.5, 1.0, 'C-6'], [7.5, 0.5, 'A-4'], [8.0, 2.0, 'C-3'], [10.0, 2.0, 'G-4'], [12.0, 4.0, 'G-3'], [16.0, 1.0, 'F-5'], [17.0, 2.0, 'G-4'], [19.0, 1.0, 'A-3'], [20.0, 1.0, 'F-4'], [21.0, 1.0, 'B-3'], [22.0, 2.0, 'F-4'], [24.0, 4.0, 'E-5'], [28.0, 4.0, 'C-3'], [32.0, 1.0, 'G-4'], [33.0, 2.0, 'D-5'], [35.0, 1.0, 'A-5'], [36.0, 2.0, 'E-3'], [38.0, 2.0, 'D-4'], [40.0, 1.0, 'C-4'], [41.0, 3.0, 'F-4'], [44.0, 1.0, 'D-4'], [45.0, 3.0, 'C-5'], [48.0, 2.0, 'D-4'], [50.0, 2.0, 'A-5'], [52.0, 2.0, 'G-4'], [54.0, 2.0, 'F-3'], [56.0, 3.0, 'F-5'], [59.0, 1.0, 'F-3'], [60.0, 2.0, 'F-4'], [62.0, 2.0, 'C-4'], [64.0, 0.34, 'F-5'], [64.34, 0.33, 'A-3'], [64.67, 0.33, 'C-3'], [65.0, 1.0, 'E-5'], [66.0, 2.0, 'D-4'], [68.0, 0.5, 'C-5'], [68.5, 1.0, 'E-4'], [69.5, 2.0, 'A-5'], [71.5, 0.5, 'E-5'], [72.0, 0.34, 'C-6'], [72.34, 0.33, 'F-3'], [72.67, 0.33, 'B-5'], [73.0, 2.0, 'G-5'], [75.0, 1.0, 'A-5'], [76.0, 2.0, 'B-4'], [78.0, 0.25, 'C-3'], [78.25, 1.0, 'G-3'], [79.25, 0.25, 'F-4'], [79.5, 0.5, 'C-5'], [80.0, 1.0, 'C-3'], [81.0, 1.0, 'E-5'], [82.0, 1.0, 'F-4'], [83.0, 1.0, 'G-5'], [84.0, 0.5, 'C-6'], [84.5, 2.0, 'C-6'], [86.5, 1.0, 'A-3'], [87.5, 0.5, 'A-3'], [88.0, 2.0, 'E-5'], [90.0, 0.5, 'D-4'], [90.5, 1.0, 'F-3'], [91.5, 0.5, 'A-5'], [92.0, 1.0, 'F-3'], [93.0, 0.5, 'C-6'], [93.5, 1.0, 'C-3'], [94.5, 0.5, 'A-4'], [95.0, 1.0, 'F-5'], [96.0, 4.0, 'C-4'], [100.0, 1.0, 'E-4'], [101.0, 3.0, 'G-4'], [104.0, 0.33, 'E-4'], [104.33, 3.0, 'B-4'], [107.33, 0.33, 'C-4'], [107.66, 0.34, 'E-3'], [108.0, 4.0, 'C-6'], [112.0, 3.0, 'F-4'], [115.0, 1.0, 'G-3'], [116.0, 4.0, 'E-3'], [120.0, 4.0, 'C-5'], [124.0, 2.0, 'E-3'], [126.0, 2.0, 'C-5']]

def play(file_name):
    for i in itertools.count():
        path = os.getcwd()+"/musicpiece" + str(i)
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            break
    fluidsynth.init("Timbre.sf2",snareplayer,file=path + '/snare.wav')
    snareplayer.main_volume(channel=9,value=70)
    snareplayer.play_Track(finalpercussion.snaretrack,channel=9,bpm=100)
    fluidsynth.initialized = False
    fluidsynth.init("Timbre.sf2",highhatplayer,file=path + '/highhat.wav')
    highhatplayer.main_volume(channel=9,value=50)
    highhatplayer.play_Track(finalpercussion.highhattrack,channel=9,bpm=100)
    fluidsynth.initialized = False
    fluidsynth.init("Timbre.sf2",cymbalplayer,file=path + '/cymbal.wav')
    cymbalplayer.main_volume(channel=9,value=70)
    cymbalplayer.play_Track(finalpercussion.cymbaltrack,channel=9,bpm=100)
    fluidsynth.initialized = False
    fluidsynth.init("Timbre.sf2",tomplayer,file=path + '/tom.wav')
    tomplayer.main_volume(channel=9,value=70)
    tomplayer.play_Track(finalpercussion.tomtrack,channel=9,bpm=100)
    fluidsynth.initialized = False
    fluidsynth.init("Timbre.sf2",baseplayer,file=path + '/base.wav')
    baseplayer.main_volume(channel=9,value=100)
    baseplayer.play_Track(finalpercussion.basetrack,channel=9,bpm=100)
    fluidsynth.initialized = False
    fluidsynth.init("Timbre.sf2",lefthandplayer,file=path + '/lefthand.wav')
    lefthandplayer.main_volume(channel=1,value=70)
    lefthandplayer.play_Track(lefthandtrack2,channel=1,bpm=100)
    midi_file_out.write_Track(path + '/guitar.mid',guitartrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/guitar.mid',path+'/guitar.wav')
    midi_file_out.write_Track(path + '/string.mid',strintrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/string.mid',path+'/string.wav')
    midi_file_out.write_Track(path + '/basse.mid',bassetrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/basse.mid',path+'/basse.wav')
    midi_file_out.write_Track(path + '/brass.mid',brasstrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/brass.mid',path+'/brass.wav')
    midi_file_out.write_Track(path + '/electricguitar.mid',electricguitartrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/electricguitar.mid',path+'/electricguitar.wav')
    midi_file_out.write_Track(path + '/synth.mid',synthtrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/synth.mid',path+'/synth.wav')
    midi_file_out.write_Track(path + '/frhorn.mid',frhorntrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/frhorn.mid',path+'/frhorn.wav')

    midi_file_out.write_Track(path + '/righthand.mid',righthandtrack1,bpm=timeconstant)
    FluidSynth('Timbre.sf2').midi_to_audio(path+'/righthand.mid',path+'/righthand.wav')

    sound1 = AudioSegment.from_wav(path + "/righthand.wav")
    sound1 += 5
    sound2 = AudioSegment.from_wav(path + "/lefthand.wav")
    sound2 += 2
    sound3 = AudioSegment.from_wav(path + "/snare.wav")
    sound4 = AudioSegment.from_wav(path + "/base.wav")
    sound5 = AudioSegment.from_wav(path + "/highhat.wav")
    sound6 = AudioSegment.from_wav(path + "/cymbal.wav")
    sound7 = AudioSegment.from_wav(path + "/tom.wav")
    sound8 = AudioSegment.from_wav(path + "/guitar.wav")
    sound9 = AudioSegment.from_wav(path + "/string.wav")
    sound9 -= 5
    sound10 = AudioSegment.from_wav(path + "/basse.wav")
    sound11 = AudioSegment.from_wav(path + "/brass.wav")
    sound11 -= 5
    sound12 = AudioSegment.from_wav(path + "/electricguitar.wav")
    sound12 -= 10
    sound13 = AudioSegment.from_wav(path + "/synth.wav")
    sound13 -= 15
    sound14 = AudioSegment.from_wav(path + "/frhorn.wav")

    combined = sound2.overlay(sound1.overlay(sound3.overlay(sound4.overlay(sound5.overlay(sound6.overlay(sound7.overlay(sound8.overlay(sound9.overlay(sound10.overlay(sound11.overlay(sound12.overlay(sound13.overlay(sound14)))))))))))))
    combined.export(path + "/" + file_name, format='wav')

    shutil.copy(path + "/" + file_name,  os.getcwd()+"/static")

    print "the file name is " + file_name



"""""
def playrighthand():
    lefthandmusicthinny.play_Track(righthandtrack,channel=0,bpm=speed1)
def playlefthand():
    midi_file_out.write_Track('test3.mid',lefthandtrack2,bpm=1000)
    lefthandmusicthinny.play_Track(lefthandtrack2,channel=1,bpm=speed1)
def playsnare():
    lefthandmusicthinny.play_Track(snaretrack2,channel=9,bpm=speed1)
def playhighhat():
    lefthandmusicthinny.play_Track(highhattrack2,channel=9,bpm=speed1)
def playcymbal():
    lefthandmusicthinny.play_Track(cymbaltrack2,channel=9,bpm=speed1)
def playtom():
    lefthandmusicthinny.play_Track(tomtrack2,channel=9,bpm=speed1)
def playbase():
    lefthandmusicthinny.play_Track(basetrack2,channel=9,bpm=speed1)

def play():
    t0 = Thread(target=playrighthand)
    t1 = Thread(target=playlefthand)
    t2 = Thread(target=playsnare)
    t3 = Thread(target=playbase)
    t4 = Thread(target=playhighhat)
    t5 = Thread(target=playcymbal)
    t6 = Thread(target=playtom)
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
"""""