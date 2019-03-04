import os
import sys

sys.path.append(os.path.abspath("pydub"))

from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file('HitsoundQuakeChampions.wav', format="wav")

octaves_high = 1.75
octaves_low = -1.75


sample_high = int(sound.frame_rate * (2.0 ** octaves_high))

sound_high = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_high})
sound_high = sound_high.set_frame_rate(sound.frame_rate)
sound_high.export("HitsoundQuakeChampionsHigh.wav", format="wav")

sample_low = int(sound.frame_rate * (2.0 ** octaves_low))
sound_low = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_low})
sound_low = sound_low.set_frame_rate(sound.frame_rate)
sound_low.export("HitsoundQuakeChampionsLow.wav", format="wav")
