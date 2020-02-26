import numpy as np
from pylab import plot, show, axis
from scipy.io import wavfile
from matplotlib import pyplot as plt
from os import system, name

if name == "nt":
    import winsound

input = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

def getFrequency(note):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    if len(note) == 3:
        octave = note[2]
    else:
        octave = note[1]

    keyNumber = notes.index(note[0:-1])
    if keyNumber < 3:
        keyNumber = keyNumber + 12 + ((int(octave) - 1) * 12) + 1
    else:
        keyNumber = keyNumber + ((int(octave) - 1) * 12) + 1

    return 440 * pow(2, (keyNumber - 49) / 12)


def getNote(freq, duration, amplitude, rate=44100):
    time = np.linspace(0, duration, duration * rate, False)

    note = amplitude * np.sin(freq * time * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    data = note * (2 ** 15 - 1) / np.max(np.abs(note))
    return data.astype(np.int16)

def playScale(scale, interval):
    for freq in scale:
        winsound.Beep(int(freq+0.5), interval)

def getHarmonics(freq, duration, n):
    amplitude = 1
    note = 0
    for i in range(n):
        note += getNote(freq * (i + 1), duration, amplitude, 44100)
        amplitude = amplitude * 0.6
    return note

def main():
    tone = getHarmonics(440, 2, 6)
    wavfile.write("sin_test.wav", 44100, tone)
    # wavfile.write("/home/silverlined/Downloads/DSP/sin_test.wav", 44100, tone)
    # system("aplay -f cd /home/silverlined/Downloads/DSP/sin_test.wav")
    winsound.PlaySound("sin_test.wav", winsound.SND_ALIAS)
    playScale(input, 100)


if __name__ == "__main__":
    main()
