import os
from string import upper

from mingus.containers import Track
from mingus.midi import fluidsynth
from mingus.midi.fluidsynth import FluidSynthSequencer

speed1 = 100
speed2 = 240  # 1 second per beat.
lefthandmusicthinny = FluidSynthSequencer()

# notes = ['E-6|1.25', 'D-7|1.25', 'E-7|1.50', 'C-7|1.25', 'C-7|1.25', 'A-6|1.50', 'C-7|1.25', 'B-6|1.25', 'A-6|1.50',
#          'A-6|1.25', 'B-6|1.25', 'A-6|1.50', 'B-6|1.25', 'C-7|1.25', 'C-7|1.50', 'B-6|1.25', 'A-6|1.25', 'A-6|1.50',
#          'A-6|1.25', 'D-7|1.25', 'C-7|1.50', 'C-7|1.25', 'C-7|1.25', 'B-6|1.50']

snaretrack2 = Track()
# i = 0
# for note in notes:
#     notePair = note.split("|")
#     snaretrack2.add_notes(notePair[0], float(notePair[1]))
#
#     i += 1
#
# print notes
# print snaretrack2

# #
# snaretrack2.add_notes('C--4')
# snaretrack2.add_notes('D4')
# snaretrack2.add_notes('E-4')
# snaretrack2.add_notes('F-4')
# snaretrack2.add_notes('G-4')
# snaretrack2.add_notes('A-4')
# snaretrack2.add_notes('B4')
# snaretrack2.add_notes('C-5')
# #
# #
#
# lefthandmusicthinny.init()
# fluidsynth.init(os.path.dirname(__file__) + "/goodtry.sf2", lefthandmusicthinny)
# lefthandmusicthinny.main_volume(channel=0, value=100)
# lefthandmusicthinny.main_volume(channel=1, value=75)
# lefthandmusicthinny.main_volume(channel=9, value=75)
#
# lefthandmusicthinny.play_Track(snaretrack2, channel=1, bpm=speed2)
