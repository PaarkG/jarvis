import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100

def record(seconds):
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write('output.wav', fs, myrecording)
