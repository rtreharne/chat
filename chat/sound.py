import sounddevice as sd
import numpy as np
import time
import pyttsx3
import os
import pygame

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def string_to_morse(text):
    text = text.upper()
    morse_code = []
    
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append(' ')  # Leave a space for characters not in the dictionary
    
    return ' '.join(morse_code)

def morse_to_sound(morse_code, frequency=880, duration=0.2):
    
    for char in morse_code:
        if char == '.':
            play_sound(frequency, duration*2)
        elif char == '-':
            play_sound(frequency, duration * 6)
        else:
            time.sleep(duration*5)
        time.sleep(duration)

def play_sound(frequency, duration):
    sample_rate = 44100  # Standard audio sample rate
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(wave, sample_rate, blocksize=4096)
    sd.wait()

def text_to_speech(text, voice_id='com.apple.speech.synthesis.voice.Alex', filename=None, pitch_shift=0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 0.4)
        
    if filename:
        engine.save_to_file(text, filename)
        engine.runAndWait()
    else:
        engine.say(text)
        engine.runAndWait()


def play_wav_file(file_name = "chat/sound_files/taunt.wav"):

    # Get the absolute path of the current directory
    current_directory = os.getcwd()

    # Construct the full file path
    file_path = os.path.join(current_directory, file_name)
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    frequency = 440  # A4 note frequency (Hz)
    duration = 2     # Duration in seconds

    play_sound(frequency, duration)


    # Specify the path to your .wav file
    file_name = "chat/sound_files/taunt.wav"

    # Get the absolute path of the current directory
    current_directory = os.getcwd()

    # Construct the full file path
    file_path = os.path.join(current_directory, file_name)

    if os.path.exists(file_path):
        play_wav_file(file_path)
    else:
        print("WAV file not found.")
