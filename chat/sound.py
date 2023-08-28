import sounddevice as sd
import numpy as np
import time
import pyttsx3

def play_sound(frequency, duration):
    sample_rate = 44100  # Standard audio sample rate
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, sample_rate, blocksize=4096)
    sd.wait()

def text_to_speech(text, voice_id='com.apple.speech.synthesis.voice.Alex', filename=None, pitch_shift=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', engine.getProperty('rate') + pitch_shift)
        
    if filename:
        engine.save_to_file(text, filename)
        engine.runAndWait()
    else:
        engine.say(text)
        engine.runAndWait()


if __name__ == "__main__":
    frequency = 440  # A4 note frequency (Hz)
    duration = 2     # Duration in seconds

    play_sound(frequency, duration)

    # Using pyttsx3 to convert text to speech and play the output
    text_to_speech("Hello, this is a test.", voice_id='com.apple.speech.synthesis.voice.Alex')
