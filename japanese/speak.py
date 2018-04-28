import japanese
from gtts import gTTS
from mutagen.mp3 import MP3 as mp3
import pygame
import time
import os
BUFFER_FILE_NAME = '.python-japanese-buffer.mp3'


def string(string: str):
    """Speak string by gTTS
    Arg:
        string: speak this string.
    """
    tts = gTTS(text=string, lang='ja')
    tts.save(BUFFER_FILE_NAME)  # buffer file(MP3)
    pygame.mixer.init()
    pygame.mixer.music.load(BUFFER_FILE_NAME)
    # get buffer file(MP3)'s length (second)
    mp3_length = mp3(BUFFER_FILE_NAME).info.length
    pygame.mixer.music.play(1)  # play only one time
    time.sleep(mp3_length + 0.25)  # continue play
    pygame.mixer.music.stop()
    os.remove(BUFFER_FILE_NAME)  # delete buffer file(MP3)


def save(string: str, filename: str):
    """Speak to file
    Arg:
        string: speak this string
        filename: speak to this file
    """
    tts = gTTS(text=string, lang='ja')
    tts.save(filename)
