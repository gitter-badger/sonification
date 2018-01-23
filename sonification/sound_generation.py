import numpy as np


def make_sound(frequency = 1, duration = 0.1, volume = 16, sampling_rate=48000):
    time_scale = np.arange(make_sound.phase, duration + make_sound.phase, 1./sampling_rate)
    sin_wave = np.sin(time_scale * 2 * np.pi * frequency) * volume
    make_sound.phase = (duration + make_sound.phase) % (1/frequency)
    return sin_wave
make_sound.phase = 0
