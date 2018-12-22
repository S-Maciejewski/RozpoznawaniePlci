import sys
from pylab import *
from numpy import *
from scipy import *
from random import *
import cmath
from scipy.io import wavfile
from scipy.signal import decimate
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter("ignore")

def getSignalParameters(samples, samplingFreq):
    numberOfSamples = len(samples)
    complexNumbers = fft(samples)
    amplitudes = abs(complexNumbers) / (numberOfSamples/2)
    amplitudes[0] = 0
    harmonicFreqs = [(i/numberOfSamples) * samplingFreq for i in range(int(numberOfSamples))]
    return harmonicFreqs, amplitudes


samplingFreq, signal = wavfile.read(sys.argv[1])
if len(signal.shape) == 2 : signal = np.asarray([sample[0] for sample in signal])
signal = signal[int(len(signal)/2):int(len(signal)/4*3)]

freqs, amps = getSignalParameters(signal, samplingFreq)

lower_bound = int(80/freqs[1])
voiceRange = int(400/freqs[1])
halfRange = amps[0:int(len(freqs)/2)]

result = amps[0:voiceRange]

# fig = plt.figure(figsize=(20, 15), dpi=80)
# ax = fig.add_subplot(211)
# ax.stem(freqs[:half:100], amps[:half:100], '-')
for i in range(2, 5):
    temp = decimate(halfRange, i)
    result = result * temp[0:voiceRange]

max = freqs[np.argmax(result[lower_bound:])+lower_bound]
print(max)
if max < 165 :
    print('M')
else :
    print('K')


# ax = fig.add_subplot(212)
# ax.stem(freqs[lower_bound:voiceRange], result[lower_bound:], '-')
# plt.show()

# 2-5    próg 170  92%