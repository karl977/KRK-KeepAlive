import numpy as np
import sounddevice as sd
import time
from datetime import datetime

#python -m sounddevice

# Substring of audio device name
device_name = 'VoiceMeeter Aux Input (VB-Audio, MME'

# Sample rate of the audio device
fs = 44100

# Length of the signal
t = 5

# Timeout between 'wake up' signals in minutes
timeout = 10

# Frequency to wake up the subwoofer
f_low = 10

# Frequency to wake up the monitors
f_high = 15000

samples_low = np.linspace(0, t, int(fs*t), endpoint=False)

signal_low = np.sin(2 * np.pi * f_low * samples_low)
signal_low *= 32767
signal_low = np.int16(signal_low)


samples_high = np.linspace(0, t, int(fs*t), endpoint=False)

signal_high = np.sin(2 * np.pi * f_low * samples_high)
signal_high *= 32767
signal_high = np.int16(signal_high)

sd.default.samplerate = fs
sd.default.device = device_name


while True:
    print('Playing wakeup signals at: ', datetime.now())
    sd.play(signal_high)
    sd.play(signal_low)
    time.sleep(60 * timeout)
