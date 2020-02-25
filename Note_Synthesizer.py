import numpy as np
from pylab import plot, show, axis
from scipy.io import wavfile
from matplotlib import pyplot as plt
from os import system


def getFrequency(note):
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    if len(note) == 3:
        octave = note[2]
    else:
        octave = note[1]

    keyNumber = notes.index(note[0:1])
    if keyNumber < 3:
        keyNumber = keyNumber + 12 + ((int(octave) - 1) * 12) + 1
    else:
        keyNumber = keyNumber + ((int(octave) - 1) * 12) + 1

    return 440 * pow(2, (keyNumber - 49) / 12)


def getNote(freq, duration, amplitude, rate=44100):
    time = np.linspace(0, duration, duration * rate, False)

    note = np.sin(freq * time * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    data = note * (2 ** 15 - 1) / np.max(np.abs(note))
    return data.astype(np.int16)


def main():
    tone = getNote(262, 2, 10000, 44100)
    wavfile.write("/home/silverlined/Downloads/DSP/sin_test.wav", 44100, tone)
    system("aplay -f cd /home/silverlined/Downloads/DSP/sin_test.wav")


if __name__ == "__main__":
    main()
