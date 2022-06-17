import pygame


def play_background_sound(sound_name):
    pygame.mixer.music.load(sound_name)
    pygame.mixer.music.play()
