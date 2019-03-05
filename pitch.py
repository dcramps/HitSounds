import os
import sys
sys.path.append(os.path.abspath("pydub"))
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path

soundsPath = Path("./Sounds/")
for soundPath in soundsPath.glob('**/*_src.wav'):
  suffix = str(soundPath.suffix)
  soundName = str(soundPath.stem.replace("_src",""))
  folder = str(soundPath.parent)

  midName = folder + "/" + soundName + "_mid" + suffix
  lowName = folder + "/" + soundName + "_low" + suffix
  highName = folder + "/" + soundName + "_high" + suffix

  print("Writing " + soundName + " to " + folder)
  print("...Mid")
  sound = AudioSegment.from_file(soundPath, format="wav")
  sound.export(midName, format="wav")

  octaves_high = 1.5
  octaves_low = -1.5

  sample_high = int(sound.frame_rate * (2.0 ** octaves_high))

  print("...Low")
  sample_low = int(sound.frame_rate * (2.0 ** octaves_low))
  sound_low = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_low})
  sound_low = sound_low.set_frame_rate(sound.frame_rate)
  sound_low.export(lowName, format="wav")

  print("...High")
  sound_high = sound._spawn(sound.raw_data, overrides={'frame_rate': sample_high})
  sound_high = sound_high.set_frame_rate(sound.frame_rate)
  sound_high.export(highName, format="wav")

  print("---")
