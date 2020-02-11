from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.widget import Widget
from mingus.midi import fluidsynth,sequencer
from threading import Thread
from mingus.containers import Note,Bar,Track,NoteContainer
from mingus.midi.fluidsynth import FluidSynthSequencer
from kivy.properties import ObjectProperty
from mingus.midi import midi_file_out
import random
import time
import math
import norepeatmusictheory


"""
eighth measure qushi
"""
solidarityforever = "55555435+1+2+3+3+3+2+1+176667+17+165653555555435+1+2+3+3+3+2+1+1+2+2+17+1"
internationale = "+17+2+153644+2+1765435+17+2+153644+2+17+2+47+1"
song = "32323+175323565536553651332212+17532323+1753235655365536532211"
hua = "3356+1+1655653356+1+165565555356653235322321"
lunar = "7+1+2+35+4+3+2+23+3+27+13+2+167+1656667+157+174+3+2+1+27+1+2+35+4+3+2+23+3+27+1+27+1+27+15+1+54+1+14+1+1+5+5+5"
ode = "555556+17665+3+3+3+3+3+3+2+2+3+2+5+5+53+4+4+4+3+3+3+3+2+1+17+2"
preinitialized = False
downbeat = False
firtpreinitialized = True
downbeatrequired = 0
downbeatduration = 0.0
ended = False
speed = 100.0
firsttimepress = True
listttomt = []
downbettomt = []
notelist = []
downbeatnotelist = []
notesintext = 0
numberrequired = 0
keep = 0.0
turn = 0
lastnumber = 100.0
lastnumber2 = 100.0
possiblevalues = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16.0, 16.25, 16.5, 16.75, 17.0, 17.25, 17.5, 17.75, 18.0, 18.25, 18.5, 18.75, 19.0, 19.25, 19.5, 19.75, 20.0, 20.25, 20.5, 20.75, 21.0, 21.25, 21.5, 21.75, 22.0, 22.25, 22.5, 22.75, 23.0, 23.25, 23.5, 23.75, 24.0, 24.25, 24.5, 24.75, 25.0, 25.25, 25.5, 25.75, 26.0, 26.25, 26.5, 26.75, 27.0, 27.25, 27.5, 27.75, 28.0, 28.25, 28.5, 28.75, 29.0, 29.25, 29.5, 29.75, 30.0, 30.25, 30.5, 30.75, 31.0, 31.25, 31.5, 31.75]
downbeatpossiblevalues = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0]
possiblenote = ["C","D","E","F","G","A","B"]
initialized = False
uiplayer = FluidSynthSequencer()
fluidsynth.init('goodtry.sf2',uiplayer)
cymbal = Note()
cymbal.from_int(37)
snare = Note()
snare.from_int(26)
highhat = Note()
highhat.from_int(30)
base = NoteContainer()
basenote = Note()
basenote.from_int(23)
base.add_note(basenote)
soundtrack = Track()
starttrack = Track()
starttrack.add_notes(highhat,1)
starttrack.add_notes(highhat,1)
starttrack.add_notes(highhat,1)
starttrack.add_notes(highhat,1)

for i in range(0,32):
    if math.floor(i / 4.0) == i / 4.0:
        soundtrack.add_notes([basenote,cymbal],1.0)
    else:
        soundtrack.add_notes(base,1.0)
finalist2 = []
durationlist = []
downbeatlist = []
downbeatlist2 = []
downbeatlist3 = []
finallist = []
ultimatelist = []
actuallastlist = []
timestart = 0.0
timeend = 0.0
control = 0.0

startrecord = False
endrecord = True
soundstart = False
def playsound():
    global soundstart
    global initialized
    global startrecord
    global timestart
    global timeend
    global ended
    global control
    global turn
    global lastnumber
    global keep
    global numberrequired
    global preinitialized
    global downbeatlist
    global downbeatlist2
    global downbeatrequired
    global lastnumber2
    if soundstart == False:
        soundstart = True
        preinitialized = True
        timestart = time.time()
        startrecord = True
        uiplayer.play_Track(starttrack, channel=9, bpm=speed)
        preinitialized = False
        initialized = True
        startrecord = True
        timestart = time.time()
        uiplayer.play_Track(soundtrack, channel=9, bpm=speed)
        initialized = False
        fluidsynth.initialized = False
        print downbeatlist
        for durations in downbeatlist:
            if float(min(downbeatpossiblevalues, key=lambda x: abs(x - durations))) != 4.0:
                downbeatlist2.append(float(min(downbeatpossiblevalues, key=lambda x: abs(x - durations))))
            else:
                pass
        for i in downbeatlist2:
            if i == lastnumber2:
                pass
            else:
                downbeatlist3.append(float(i))
            lastnumber2 = i
        downbeatrequired = len(downbeatlist3)
        downbeatlist3.append(4.0)
        print downbeatlist3
        print downbeatrequired
        for durations in durationlist:
            control += float(durations)
            finalist2.append(control)
        for durations in finalist2:
            print min(possiblevalues, key=lambda x: abs(x - durations))
            finallist.append(float(min(possiblevalues, key=lambda x: abs(x - durations))))
        print finallist
        for i in finallist:
            if i == lastnumber:
                pass
            else:
                ultimatelist.append(float(i))
            lastnumber = i
        numberrequired = len(ultimatelist)
        ultimatelist.append(32.0)
        for number in ultimatelist:
            print number
            if math.floor(float(number) / 4) > math.floor(keep / 4):
                if math.floor(float(number) / 4) == float(number) / 4:
                    if math.floor(float(number) / 4) - math.floor(keep / 4) <= 1:
                        actuallastlist.append(number)
                    else:
                        for i in range(0, int(math.floor(float(number) / 4 - math.floor(keep / 4)))):
                            actuallastlist.insert(turn, [math.floor(float(number) / 4) * 4 - (
                                    (int(math.floor(float(number) / 4 - math.floor(keep / 4))) - 1 - i) * 4),"None"])
                            turn += 1
                        actuallastlist.append(number)

                else:
                    for i in range(0, int(math.floor(float(number) / 4 - math.floor(keep / 4)))):
                        actuallastlist.insert(turn, [math.floor(float(number) / 4) * 4 - (
                                (int(math.floor(float(number) / 4 - math.floor(keep / 4))) - 1 - i) * 4),"None"])
                        turn += 1
                    actuallastlist.append(number)
            else:
                actuallastlist.append(number)
            keep = number
            turn += 1
        if actuallastlist[0] != 0.0:
            actuallastlist.insert(0, 0.0)
            numberrequired += 1

        print actuallastlist
        print numberrequired
        numberrequired += downbeatrequired
        ended = True
    else:
        pass
def keeptime():
    global endrecord
    global startrecord
    global timestart, timeend
    global initialized
    global preinitialized
    global downbeatduration
    global durationlist
    global downbeatlist
    global downbeat
    global firtpreinitialized
    if initialized or preinitialized:
        if firtpreinitialized:
            firtpreinitialized = False
        else:
            uiplayer.play_Note(snare, channel=9)
            if startrecord:
                timeend = time.time()
                startrecord = False
                endrecord = True
            duration = (timeend - timestart) * (speed / 60.0)
            downbeatduration += (timeend - timestart) * (speed / 60.0)
            if preinitialized:
                downbeat = True
                downbeatlist.append(downbeatduration)
            if initialized:
                durationlist.append(duration)
            print duration
            print durationlist
            if endrecord:
                timestart = time.time()
                startrecord = True
                endrecord = False
class FirstGrid(Widget):
    text1 = ObjectProperty(None)
    record_bttn = ObjectProperty(None)
    label1 = ObjectProperty(None)
    octave = 0
    def check(self):
        while not ended:
            if ended:
                self.record_bttn.visible = False
                self.label1.text = "Notes still needed: " + str(numberrequired - notesintext)
                break
    def callback(self):
        t1 = Thread(target=playsound)
        t2 = Thread(target=keeptime)
        t3 = Thread(target=self.check)
        t1.start()
        t2.start()
        t3.start()
    def callback1(self):
        global notesintext
        global numberrequired

        for characters in self.text1.text:
            try:
                int(characters)
                notesintext += 1
            except ValueError:
                pass
        self.label1.text = "Notes still needed: "+str(numberrequired-notesintext)
        notesintext = 0

    def callback2(self):
        pass
    def callback3(self):
        global notesintext
        global notelist
        global numberrequired
        global listttomt
        global downbeatlist3
        global downbeatrequired
        global downbeatnotelist
        lastnumberfin = 0
        lastnumber3 = 0.0
        noteinputrounds = 0
        noterounds = 0
        timerounds = 0
        for characters in self.text1.text:
            try:
                int(characters)
                notesintext += 1
            except ValueError:
                pass
        if notesintext == numberrequired:
            for notes in self.text1.text:
                if notes == "+":
                    self.octave += 1
                elif notes == "-":
                    self.octave -= 1
                else:
                    try:
                        if abs(self.octave) > 2:
                            print ("the largest variation of octave you can have is 2")
                            break
                            notelist = []
                            downbeatnotelist = []
                            self.octave = 0
                        else:
                            if noteinputrounds >= downbeatrequired:
                                notelist.append(possiblenote[int(notes)-1]+"-"+str(4+self.octave))
                            else:
                                downbeatnotelist.append(possiblenote[int(notes)-1]+"-"+str(4+self.octave))
                                noteinputrounds += 1
                            self.octave = 0
                    except ValueError:
                        pass

            print actuallastlist
            print notelist
            downbettomt.append([None, downbeatlist3[0]])
            for downbeats in downbeatlist3:
                if downbeats == 4.0:
                    pass
                else:
                    downbettomt.append([downbeatnotelist[lastnumberfin],downbeatlist3[lastnumberfin+1]-downbeatlist3[lastnumberfin]])
                    lastnumberfin += 1
            for times in actuallastlist:
                if type(times) == float:
                    if times != 32.0:
                        if type(actuallastlist[timerounds+1]) != list:
                            listttomt.append([times,actuallastlist[timerounds+1]-times,notelist[noterounds]])
                        else:
                            listttomt.append([times,actuallastlist[timerounds+1][0]-times,notelist[noterounds]])
                        timerounds += 1
                        noterounds += 1
                    else:
                        continue
                else:
                    if times != [32.0,"None"]:
                        if type(actuallastlist[timerounds + 1]) != list:
                            listttomt.append([times[0],actuallastlist[timerounds+1]-times[0],times[1]])
                        else:
                            listttomt.append([times[0], actuallastlist[timerounds + 1][0] - times[0], times[1]])
                        timerounds += 1
            print listttomt
            print downbettomt
            print "The final list is: " + str(downbettomt) + str(listttomt)
            norepeatmusictheory.determinelefthand(listttomt,downbettomt,nameoffile='finalversion.wav')
        else:
            notesintext = 0
            print"You have to reach the required amount of number!"

class FirstApp(App):
    def build(self):
        return FirstGrid()


FirstApp().run()
