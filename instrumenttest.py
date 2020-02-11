from mingus.midi import fluidsynth,midi_file_out
from mingus.midi.fluidsynth import FluidSynthSequencer
from mingus.containers import Bar,Track,Composition
from mingus.containers.instrument import MidiInstrument
from midi2audio import FluidSynth



ins = MidiInstrument()
ins.instrument_nr = 1
player = FluidSynthSequencer()
fluidsynth.init('Timbre.sf2', player)
t = Track()
t.add_notes("C-3", 4)
t.instrument = ins
midi_file_out.write_Track('instrumenttest1.mid', t, bpm=500)
FluidSynth("Timbre.sf2").midi_to_audio('instrumenttest1.mid', 'instrumenttest1.wav')
