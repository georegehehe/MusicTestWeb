import random
import math
from mingus.containers import NoteContainer, Note, Bar, Track
from mingus.midi.fluidsynth import FluidSynthSequencer
from mingus.midi import fluidsynth
from threading import Thread
import musicdeterminationdemo
import time
from mingus.containers.instrument import MidiInstrument
otherhandmusicthinny = FluidSynthSequencer()
otherhandmusicthinny.init(volume=1.75)
lefthandmusicthinny = FluidSynthSequencer()
lefthandmusicthinny.init(volume=1)
speed = 150
offbeat = False
first_time = True
firstbar = True
lastbar = False
highorlow = random.randint(0,1)
musicpiece1 = ""
musicpiece2 = ""
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

chordI = [["C-2","E-2","G-2","C-3"]]
chordII = [["D-2","F-2","A-2","D-3"]]
chordIII = [["E-2","G-2","B-2","E-3"]]
chordIV = [["F-2","A-2","C-3","F-3"]]
chordV = [["G-2","B-2","D-3","G-3"]]
chordVI = [["A-2","C-3","E-3","A-3"]]
chordV7 = [["G-2","B-2","D-3","F-3"]]
chordIi = [["C-3","E-3","G-3","C-4"]]
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
right_hand_music = input("enter a list of right hand music in form")
righthandbar = Bar()
righthandtrack = Track()
lefthandtrack = Track()
snaretrack = Track()
highhattrack = Track()
basetrack = Track()
cymbaltrack = Track()
tomtrack = Track()
def addsimplechord(chord):
    for x in chord:
        lefthandtrack.add_notes(x, 1)
def addcomplexchord(chord):
    for x in chord:
        lefthandtrack.add_notes(x,0.5)
def addchord(chord):
    for x in chord:
        lefthandtrack.add_notes(x,2)
def transnum(var1,var2):
    for i in var1:
        if i[0] == "C":
            var2 += "1"
        if i[0] == "D":
            var2 += "2"
        if i[0] == "E":
            var2 += "3"
        if i[0] == "F":
            var2 += "4"
        if i[0] == "G":
            var2 += "5"
        if i[0] == "A":
            var2 += "6"
        if i[0] == "B":
            var2 += "7"
    return var2
for i in right_hand_music:
    if i[2] == "None":
        right_hand_list.append([i[2],i[1]])
        if first_time:
            lefthandtrack.add_notes(None,4)
        first_time = False
    else:
        right_hand_list.append([i[2],i[1]])
        if math.floor(i[0]/2) == i[0]/2:
            left_hand_music.append(i[2])
            first_time = False
            if i[1] > 2:
                if math.floor((i[0] + i[1]) / 2) > math.floor(i[0] / 2):
                    left_hand_music.append(i[2])
        else:
            if math.floor((i[0]+i[1])/2) > math.floor(i[0]/2):
                if i[1] >= 3:
                    first_time = False
                    left_hand_music.append(i[2])
                else:
                    if math.floor((i[0]+i[1])/2) != (i[0]+i[1]) /2 :
                        first_time = False
                        left_hand_music.append(i[2])
print left_hand_music
print len(left_hand_music)
for i in range(0,64):
    if i < 8:
        part1.append(left_hand_music[i])
    if 8 <= i < 16:
        part2.append(left_hand_music[i])
    if 16 <= i < 24:
        part3.append(left_hand_music[i])
    if 24 <= i < 32:
        part4.append(left_hand_music[i])
    if 32 <= i < 40:
        part5.append(left_hand_music[i])
    if 40 <= i < 48:
        part6.append(left_hand_music[i])
    if 48 <= i < 56:
        part7.append(left_hand_music[i])
    if 56 <= i < 64:
        part8.append(left_hand_music[i])
print part1
musicpiece1 = transnum(part1,musicpiece1)
musicpiece2 = transnum(part2,musicpiece2)
musicpiece3 = transnum(part3,musicpiece3)
musicpiece4 = transnum(part4,musicpiece4)
musicpiece5 = transnum(part5,musicpiece5)
musicpiece6 = transnum(part6,musicpiece6)
musicpiece7 = transnum(part7,musicpiece7)
musicpiece8 = transnum(part8,musicpiece8)

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
piece = [[0.0,2,"E-4"],[2.0,1.5,"C-5"],[3.5,0.5,"B-4"],[4.0,2,"B-4"],[6.0,2,"A-4"],[8.0,3,"A-4"],[11.0,1,"D-4"],[12.0,0.33,"D-4"],[12.33,0.33,"E-4"],[12.66,0.34,"F-4"],[13.0,1,"E-4"],[14.0,2,"G-4"],[16.0,2,""]]
[[0.0,2,"E-5"],[2.0,2,"D-5"],[4.0,2,"C-5"],[6.0,2,"B-4"],[8.0,2,"A-4"],[10.0,2,"G-4"],[12.0,2,"A-4"],[14.0,1,"B-4"],[15.0,1,"G-4"]]
piece2 = [[0.0, 0.75, 'G-4'], [0.75, 0.25, 'G-4'], [1.0, 0.75, 'G-4'], [1.75, 0.25, 'F-4'], [2.0, 0.75, 'E-4'], [2.75, 0.25, 'G-4'], [3.0, 0.75, 'C-5'], [3.75, 0.25, 'D-5'], [4.0, 0.75, 'E-5'], [4.75, 0.25, 'E-5'], [5.0, 0.75, 'E-5'], [5.75, 0.25, 'D-5'], [6.0, 1.0, 'C-5'], [7.0, 0.75, 'C-5'], [7.75, 0.25, 'B-4'], [8.0, 0.75, 'A-4'], [8.75, 0.25, 'A-4'], [9.0, 0.75, 'A-4'], [9.75, 0.25, 'B-4'], [10.0, 0.75, 'C-5'], [10.75, 0.25, 'B-4'], [11.0, 0.75, 'C-5'], [11.75, 0.25, 'A-4'], [12.0, 0.5, 'G-4'], [12.5, 0.5, 'A-4'], [13.0, 0.5, 'G-4'], [13.5, 0.5, 'E-4'], [14.0, 1.0, 'G-4'], [15.0, 0.5, 'G-4'], [15.5, 0.5, 'G-4'], [16.0, 0.5, 'G-4'], [16.5, 0.5, 'G-4'], [17.0, 0.5, 'G-4'], [17.5, 0.5, 'F-4'], [18.0, 0.5, 'E-4'], [18.5, 0.25, 'G-4'], [18.75, 0.75, 'C-5'], [19.5, 0.25, 'D-5'], [19.75, 0.25, 'E-5'], [20.0, 0.5, 'None'], [20.5, 0.25, 'E-5'], [20.75, 0.75, 'E-5'], [21.5, 0.25, 'D-5'], [21.75, 1.0, 'C-5'], [22.75, 1.0, 'C-5'], [23.75, 0.25, 'D-5'], [24.0, 0.75, 'None'], [24.75, 1.0, 'D-5'], [25.75, 1.0, 'C-5'], [26.75, 1.25, 'B-5'], [28.0, 4.0, 'C-5']]

[[0.0, 3.0, 'D-5'], [3.0, 1.0, 'A-5'], [4.0, 3.0, 'F-3'], [7.0, 1.0, 'C-6'], [8.0, 2.0, 'B-3'], [10.0, 2.0, 'C-3'], [12.0, 2.0, 'C-6'], [14.0, 2.0, 'C-4'], [16.0, 1.0, 'A-4'], [17.0, 1.0, 'G-3'], [18.0, 2.0, 'A-4'], [20.0, 3.0, 'E-4'], [23.0, 0.5, 'D-5'], [23.5, 0.5, 'E-5'], [24.0, 1.0, 'A-5'], [25.0, 2.0, 'D-4'], [27.0, 1.0, 'F-3'], [28.0, 1.0, 'D-3'], [29.0, 3.0, 'G-5'], [32.0, 3.0, 'D-5'], [35.0, 1.0, 'G-4'], [36.0, 0.5, 'F-5'], [36.5, 3.0, 'F-3'], [39.5, 0.5, 'D-4'], [40.0, 1.0, 'A-5'], [41.0, 3.0, 'E-3'], [44.0, 0.5, 'C-5'], [44.5, 3.0, 'G-4'], [47.5, 0.25, 'E-3'], [47.75, 0.25, 'C-4'], [48.0, 1.0, 'D-3'], [49.0, 3.0, 'B-4'], [52.0, 0.5, 'C-5'], [52.5, 3.0, 'F-4'], [55.5, 0.5, 'F-3'], [56.0, 1.0, 'B-4'], [57.0, 2.0, 'G-5'], [59.0, 0.34, 'G-4'], [59.34, 0.33, 'C-4'], [59.67, 0.33, 'E-4'], [60.0, 1.0, 'E-5'], [61.0, 3.0, 'B-3'], [64.0, 0.5, 'E-3'], [64.5, 2.0, 'F-3'], [66.5, 0.33, 'D-4'], [66.83, 0.34, 'C-5'], [67.17, 0.33, 'C-3'], [67.5, 0.5, 'E-3'], [68.0, 2.0, 'B-4'], [70.0, 2.0, 'G-3'], [72.0, 1.0, 'A-5'], [73.0, 2.0, 'F-5'], [75.0, 1.0, 'C-4'], [76.0, 2.0, 'B-3'], [78.0, 2.0, 'C-6'], [80.0, 1.0, 'G-5'], [81.0, 3.0, 'A-4'], [84.0, 0.5, 'G-5'], [84.5, 3.0, 'G-5'], [87.5, 0.5, 'C-3'], [88.0, 0.34, 'G-3'], [88.34, 2.0, 'B-3'], [90.34, 0.25, 'A-4'], [90.59, 0.25, 'G-3'], [90.84, 0.5, 'D-5'], [91.34, 0.33, 'D-3'], [91.67, 0.33, 'G-3'], [92.0, 1.0, 'B-4'], [93.0, 3.0, 'E-3'], [96.0, 2.0, 'A-4'], [98.0, 1.0, 'D-3'], [99.0, 0.25, 'D-3'], [99.25, 0.5, 'F-4'], [99.75, 0.25, 'D-5'], [100.0, 2.0, 'B-4'], [102.0, 2.0, 'E-4'], [104.0, 2.0, 'C-6'], [106.0, 2.0, 'F-5'], [108.0, 3.0, 'E-4'], [111.0, 1.0, 'F-3'], [112.0, 2.0, 'G-4'], [114.0, 2.0, 'E-5'], [116.0, 1.0, 'A-5'], [117.0, 3.0, 'E-4'], [120.0, 0.5, 'D-5'], [120.5, 3.0, 'E-4'], [123.5, 0.5, 'D-4'], [124.0, 1.0, 'D-4'], [125.0, 2.0, 'E-4'], [127.0, 1.0, 'E-3']]
[[0.0, 2.0, 'A-4'], [2.0, 2.0, 'A-5'], [4.0, 4.0, 'D-4'], [8.0, 1.0, 'A-3'], [9.0, 2.0, 'A-3'], [11.0, 1.0, 'E-3'], [12.0, 2.0, 'F-3'], [14.0, 2.0, 'B-5'], [16.0, 4.0, 'E-4'], [20.0, 1.0, 'C-3'], [21.0, 3.0, 'G-5'], [24.0, 4.0, 'A-4'], [28.0, 1.0, 'D-5'], [29.0, 1.0, 'F-3'], [30.0, 2.0, 'E-5'], [32.0, 2.0, 'B-4'], [34.0, 2.0, 'A-5'], [36.0, 1.0, 'G-4'], [37.0, 2.0, 'A-3'], [39.0, 1.0, 'C-4'], [40.0, 2.0, 'G-3'], [42.0, 2.0, 'B-5'], [44.0, 2.0, 'A-3'], [46.0, 2.0, 'C-6'], [48.0, 1.0, 'G-5'], [49.0, 3.0, 'A-4'], [52.0, 3.0, 'A-3'], [55.0, 0.5, 'A-3'], [55.5, 0.5, 'F-3'], [56.0, 1.0, 'A-4'], [57.0, 3.0, 'G-3'], [60.0, 1.0, 'G-4'], [61.0, 2.0, 'F-4'], [63.0, 1.0, 'F-4'], [64.0, 0.25, 'A-3'], [64.25, 0.5, 'F-5'], [64.75, 2.0, 'A-4'], [66.75, 0.25, 'A-4'], [67.0, 1.0, 'A-4'], [68.0, 0.33, 'F-3'], [68.33, 2.0, 'C-6'], [70.33, 1.0, 'D-3'], [71.33, 0.33, 'A-3'], [71.66, 0.34, 'F-4'], [72.0, 0.33, 'E-3'], [72.33, 0.34, 'C-4'], [72.67, 0.34, 'C-5'], [73.01, 1.0, 'B-5'], [74.01, 0.33, 'G-4'], [74.34, 1.0, 'B-3'], [75.34, 0.33, 'E-5'], [75.67, 0.33, 'G-5'], [76.0, 0.33, 'F-5'], [76.33, 0.25, 'F-5'], [76.58, 0.5, 'A-5'], [77.08, 0.25, 'C-3'], [77.33, 0.33, 'D-4'], [77.66, 2.0, 'D-3'], [79.66, 0.34, 'E-3'], [80.0, 0.5, 'A-3'], [80.5, 0.5, 'A-4'], [81.0, 1.0, 'D-4'], [82.0, 2.0, 'A-4'], [84.0, 0.5, 'G-4'], [84.5, 1.0, 'C-4'], [85.5, 0.5, 'G-4'], [86.0, 2.0, 'F-5'], [88.0, 3.0, 'E-3'], [91.0, 0.33, 'B-3'], [91.33, 0.34, 'G-3'], [91.67, 0.33, 'F-4'], [92.0, 2.0, 'A-5'], [94.0, 1.0, 'F-3'], [95.0, 0.5, 'C-5'], [95.5, 0.5, 'G-3'], [96.0, 3.0, 'A-4'], [99.0, 1.0, 'A-3'], [100.0, 2.0, 'C-4'], [102.0, 2.0, 'G-3'], [104.0, 4.0, 'F-5'], [108.0, 1.0, 'E-3'], [109.0, 1.0, 'C-6'], [110.0, 2.0, 'D-3'], [112.0, 4.0, 'D-5'], [116.0, 1.0, 'F-3'], [117.0, 3.0, 'A-4'], [120.0, 4.0, 'C-4'], [124.0, 2.0, 'E-3'], [126.0, 2.0, 'C-6']]
[[0.0, 4.0, 'D-4'], [4.0, 2.0, 'G-5'], [6.0, 0.5, 'A-5'], [6.5, 1.0, 'C-6'], [7.5, 0.5, 'A-4'], [8.0, 2.0, 'C-3'], [10.0, 2.0, 'G-4'], [12.0, 4.0, 'G-3'], [16.0, 1.0, 'F-5'], [17.0, 2.0, 'G-4'], [19.0, 1.0, 'A-3'], [20.0, 1.0, 'F-4'], [21.0, 1.0, 'B-3'], [22.0, 2.0, 'F-4'], [24.0, 4.0, 'E-5'], [28.0, 4.0, 'C-3'], [32.0, 1.0, 'G-4'], [33.0, 2.0, 'D-5'], [35.0, 1.0, 'A-5'], [36.0, 2.0, 'E-3'], [38.0, 2.0, 'D-4'], [40.0, 1.0, 'C-4'], [41.0, 3.0, 'F-4'], [44.0, 1.0, 'D-4'], [45.0, 3.0, 'C-5'], [48.0, 2.0, 'D-4'], [50.0, 2.0, 'A-5'], [52.0, 2.0, 'G-4'], [54.0, 2.0, 'F-3'], [56.0, 3.0, 'F-5'], [59.0, 1.0, 'F-3'], [60.0, 2.0, 'F-4'], [62.0, 2.0, 'C-4'], [64.0, 0.34, 'F-5'], [64.34, 0.33, 'A-3'], [64.67, 0.33, 'C-3'], [65.0, 1.0, 'E-5'], [66.0, 2.0, 'D-4'], [68.0, 0.5, 'C-5'], [68.5, 1.0, 'E-4'], [69.5, 2.0, 'A-5'], [71.5, 0.5, 'E-5'], [72.0, 0.34, 'C-6'], [72.34, 0.33, 'F-3'], [72.67, 0.33, 'B-5'], [73.0, 2.0, 'G-5'], [75.0, 1.0, 'A-5'], [76.0, 2.0, 'B-4'], [78.0, 0.25, 'C-3'], [78.25, 1.0, 'G-3'], [79.25, 0.25, 'F-4'], [79.5, 0.5, 'C-5'], [80.0, 1.0, 'C-3'], [81.0, 1.0, 'E-5'], [82.0, 1.0, 'F-4'], [83.0, 1.0, 'G-5'], [84.0, 0.5, 'C-6'], [84.5, 2.0, 'C-6'], [86.5, 1.0, 'A-3'], [87.5, 0.5, 'A-3'], [88.0, 2.0, 'E-5'], [90.0, 0.5, 'D-4'], [90.5, 1.0, 'F-3'], [91.5, 0.5, 'A-5'], [92.0, 1.0, 'F-3'], [93.0, 0.5, 'C-6'], [93.5, 1.0, 'C-3'], [94.5, 0.5, 'A-4'], [95.0, 1.0, 'F-5'], [96.0, 4.0, 'C-4'], [100.0, 1.0, 'E-4'], [101.0, 3.0, 'G-4'], [104.0, 0.33, 'E-4'], [104.33, 3.0, 'B-4'], [107.33, 0.33, 'C-4'], [107.66, 0.34, 'E-3'], [108.0, 4.0, 'C-6'], [112.0, 3.0, 'F-4'], [115.0, 1.0, 'G-3'], [116.0, 4.0, 'E-3'], [120.0, 4.0, 'C-5'], [124.0, 2.0, 'E-3'], [126.0, 2.0, 'C-5']]

print left_hand_music
for i in range(0,8):
    print i
    if i == 0 or i == 1:
        if i == 0:
            chords_needed = musicdeterminationdemo.determination(musicpiece1)
            print chords_needed
        if i == 1:
            print chords_needed
            chords_needed = musicdeterminationdemo.determination(musicpiece2)
        for i in chords_needed:
            if i == 1:
                if highorlow == 0:
                    addchord(chordI)
                if highorlow == 1:
                    addchord(chordIi)
            if i == 2:
                addchord(chordII)
            if i == 3:
                addchord(chordIII)
            if i == 4:
                addchord(chordIV)
            if i == 5:
                addchord(chordV)
            if i == 6:
                addchord(chordVI)
            if i == 7:
                addchord(chordV7)
        continue
    if i == 2 or i == 3:
        if i == 2:
            chords_needed = musicdeterminationdemo.determination(musicpiece3)
        if i == 3:
            chords_needed = musicdeterminationdemo.determination(musicpiece4)
            print chords_needed
        for i in chords_needed:
            if i == 1:
                if highorlow == 0:
                    addsimplechord(simple_chordI)
                if highorlow == 1:
                    addsimplechord(simple_chordIi)
            if i == 2:
                addsimplechord(simple_chordII)
            if i == 3:
                addsimplechord(simple_chordIII)
            if i == 4:
                addsimplechord(simple_chordIV)
            if i == 5:
                addsimplechord(simple_chordV)
            if i == 6:
                addsimplechord(simple_chordVI)
            if i == 7:
                addsimplechord(simple_chordV7)
        continue
    if i == 4 or i == 5:
        if i == 4:
            chords_needed = musicdeterminationdemo.determination(musicpiece5)
        if i == 5:
            chords_needed = musicdeterminationdemo.determination(musicpiece6)
        for i in chords_needed:
            if i == 1:
                if highorlow == 0:
                    addcomplexchord(complex_chordI)
                if highorlow == 1:
                    addcomplexchord(complex_chordIi)
            if i == 2:
                addcomplexchord(complex_chordII)
            if i == 3:
                addcomplexchord(complex_chordIII)
            if i == 4:
                addcomplexchord(complex_chordIV)
            if i == 5:
                addcomplexchord(complex_chordV)
            if i == 6:
                addcomplexchord(complex_chordVI)
            if i == 7:
                addcomplexchord(complex_chordV7)
        continue
    if i == 6 or i == 7:
        if i == 6:
            chords_needed = musicdeterminationdemo.determination(musicpiece7)
        if i == 7:
            chords_needed = musicdeterminationdemo.determination(musicpiece8)
        for i in chords_needed:
            if i == 1:
                if highorlow == 0:
                    addchord(chordI)
                if highorlow == 1:
                    addchord(chordIi)
            if i == 2:
                addchord(chordII)
            if i == 3:
                addchord(chordIII)
            if i == 4:
                addchord(chordIV)
            if i == 5:
                addchord(chordV)
            if i == 6:
                addchord(chordVI)
            if i == 7:
                addchord(chordV7)
for i in range(0,8):
    cymbaltrack.add_notes(None,4)
    tomtrack.add_notes(None,4)
    if i != 7:
        snaretrack.add_notes(None,4)
        for i in startbasepercussion:
            basetrack.add_notes(i,1)
        for i in starthighhatpercussion:
            highhattrack.add_notes(i,1)

    else:
        snaretrack.add_notes(None,2)
        snaretrack.add_notes(snare,0.5)
        snaretrack.add_notes(snare,0.25)
        snaretrack.add_notes(snare, 0.25)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        basetrack.add_notes(base,2)
        basetrack.add_notes(base,2)
        highhattrack.add_notes(highhat,2)
        highhattrack.add_notes(highhat,2)
for i in range (0,8):
    if i != 7:
        if i == 0:
            cymbaltrack.add_notes(cymbal, 4)
        else:
            cymbaltrack.add_notes(None,4)
        tomtrack.add_notes(None, 4)
        for i in snarepercussion:
            snaretrack.add_notes(i,1)
        for i in basepercussion:
            basetrack.add_notes(i,1)
        for i in highhatpercussion:
            highhattrack.add_notes(i,1)
    else:
        cymbaltrack.add_notes(None, 4)
        snaretrack.add_notes(snare,1)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare,0.25)
        snaretrack.add_notes(snare, 0.25)
        snaretrack.add_notes(None,1.5)
        basetrack.add_notes(base,2)
        basetrack.add_notes(base,2)
        highhattrack.add_notes(highhat,1)
        highhattrack.add_notes(highhat, 1)
        highhattrack.add_notes(highhat, 1)
        highhattrack.add_notes(highhat, 1)
        tomtrack.add_notes(None,2.5)
        tomtrack.add_notes(hightom, 0.25)
        tomtrack.add_notes(hightom, 0.25)
        tomtrack.add_notes(midtom, 0.25)
        tomtrack.add_notes(midtom, 0.25)
        tomtrack.add_notes(lowtom, 0.25)
        tomtrack.add_notes(lowtom, 0.25)
for i in range(0, 8):

    if i != 7:
        if i == 0:
            cymbaltrack.add_notes(cymbal, 4)
        else:
            cymbaltrack.add_notes(None, 4)
        tomtrack.add_notes(None, 4)
        for i in snarepercussion:
            snaretrack.add_notes(i, 1)
        for i in basepercussion:
            basetrack.add_notes(i, 1)
        for i in range(0,2):
            for i in highhatpercussion:
                highhattrack.add_notes(i, 0.5)
    else:
        basetrack.add_notes(base,1)
        basetrack.add_notes(base,1)
        basetrack.add_notes(base, 1)
        basetrack.add_notes(base, 1)
        cymbaltrack.add_notes(None,1)
        cymbaltrack.add_notes(cymbal, 1)
        cymbaltrack.add_notes(cymbal, 1)
        cymbaltrack.add_notes(cymbal, 1)
        snaretrack.add_notes(snare,1)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        tomtrack.add_notes(None,1)
        tomtrack.add_notes(hightom, 0.5)
        tomtrack.add_notes(hightom, 0.5)
        tomtrack.add_notes(midtom, 0.5)
        tomtrack.add_notes(midtom, 0.5)
        tomtrack.add_notes(lowtom, 0.5)
        tomtrack.add_notes(lowtom, 0.5)
for i in range(0,8):
    cymbaltrack.add_notes(None,4)
    tomtrack.add_notes(None,4)
    if i != 7:
        snaretrack.add_notes(None,4)
        for i in startbasepercussion:
            basetrack.add_notes(i,1)
        for i in starthighhatpercussion:
            highhattrack.add_notes(i,1)
    else:
        snaretrack.add_notes(None,2)
        snaretrack.add_notes(snare,0.5)
        snaretrack.add_notes(snare,0.25)
        snaretrack.add_notes(snare, 0.25)
        snaretrack.add_notes(snare, 0.5)
        snaretrack.add_notes(snare, 0.5)
        basetrack.add_notes(base,2)
        basetrack.add_notes(base,2)
        highhattrack.add_notes(highhat,2)
        highhattrack.add_notes(highhat,2)
cymbaltrack.add_notes(cymbal,4)
lefthandtrack.add_notes(["C-3","E-3","G-3","C-4"],4)

print right_hand_list
for i in right_hand_list:
    righthandtrack.add_notes(i[0],i[1])
print righthandtrack
print lefthandtrack
def lefthandmusicthinnyfunc():
    fluidsynth.init("goodtry.sf2", lefthandmusicthinny)
def righthandmusicthinnyfunc():
    fluidsynth.init("goodtry.sf2", otherhandmusicthinny)
def playrighthand():
    otherhandmusicthinny.play_Track(righthandtrack,channel=0,bpm=speed)
def playlefthand():
    lefthandmusicthinny.play_Track(lefthandtrack,channel=0,bpm=speed)
def playsnare():
    lefthandmusicthinny.play_Track(snaretrack,channel=9,bpm=speed)
def playhighhat():
    lefthandmusicthinny.play_Track(highhattrack,channel=9,bpm=speed)
def playcymbal():
    lefthandmusicthinny.play_Track(cymbaltrack,channel=9,bpm=speed)
def playtom():
    lefthandmusicthinny.play_Track(tomtrack,channel=9,bpm=speed)
def playbase():
    lefthandmusicthinny.play_Track(basetrack,channel=9,bpm=speed)
def init():
    thread0 = Thread(target=lefthandmusicthinnyfunc)
    thread1 = Thread(target=righthandmusicthinnyfunc)
    thread0.start()
    thread1.start()
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
init()


