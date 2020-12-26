import contextlib
import wave

fname="D:/the-project-phoenix-server/the-project-phoenix/darted.wav"
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print(duration)