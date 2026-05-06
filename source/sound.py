import pygame as pg
import os

def play_music(filename=None, volume=0.5):
    pg.mixer.init()
    if filename is None:
        # Default sound path
        filename = os.path.join("source", "sounds", "grasswalk.mp3")
    else:
        # If a relative filename is passed, treat it as inside source/sounds/
        if not os.path.isabs(filename):
            filename = os.path.join("source", "sounds", filename)
    pg.mixer.music.load(filename)
    pg.mixer.music.set_volume(volume)
    pg.mixer.music.play(-1)  # Loop indefinitely
