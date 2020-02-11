from mingus.midi import fluidsynth
from mingus.containers import Note,Track
import time
fluidsynth.init("Timbre.sf2",fluidsynth.midi)
a = 43
b = Note()

while True:
    b.from_int(a)
    print a
    fluidsynth.play_Note(b,channel=9)
    time.sleep(1)
    a += 1
snare = 26
rimshot = 25
electricsnare = 28
openhighhat = 34
base = 23
high_tom = 38
mid_tom = 36
low_tom = 35
hit_hat = 30
cymbal = 37
