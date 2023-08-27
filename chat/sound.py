import sounddevice as sd
import numpy as np
import time

def play_sound(frequency, duration):
    sample_rate = 44100  # Standard audio sample rate
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, sample_rate, blocksize=2048)
    sd.wait()

if __name__ == "__main__":
    frequency = 440  # A4 note frequency (Hz)
    duration = 2     # Duration in seconds

    play_sound(frequency, duration)