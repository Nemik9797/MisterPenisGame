from dataclasses import dataclass


@dataclass(frozen=True)
class Display:
    wight_fullscreen = 1920
    height_fullscreen = 1080
    default_size_fullscreen = (wight_fullscreen, height_fullscreen)
    wight_window_screen = 1024
    height_window_screen = 768
    default_size_window_screen = (wight_window_screen, height_window_screen)
    fullscreen = True
