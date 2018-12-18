import sys
from pylab import *
from numpy import *
from scipy import *
from random import *
from ipywidgets import *
import math as mt
import cmath
from scipy.io import wavfile


def getSignalParameters(samples, samplingFreq):
    numberOfSamples = len(samples)

    complexNumbers = fft(samples)
    phaseShifts = [degrees(cmath.phase(cnumber)) for cnumber in complexNumbers]
    amplitudes = abs(complexNumbers) / (numberOfSamples/2)
    amplitudes[0] /= 2

    harmonicFreqs = [(i/numberOfSamples) *
                     samplingFreq for i in range(int(numberOfSamples))]

    return complexNumbers, harmonicFreqs, amplitudes, phaseShifts

print(sys.argv[1])  # sciezka do pliku

samplingFreq, signal = wavfile.read(sys.argv[1])
print(samplingFreq)

signal = [s[0] for s in signal]
fftNumbers, freqs, amps, shifts = getSignalParameters(
    signal[::10], samplingFreq)

# Rysowanie spektrogramu
fig = plt.figure(figsize=(15, 15), dpi=80)
ax = fig.add_subplot(111)
plt.yscale('log')
ax.stem(freqs, amps, '-')
plt.show()