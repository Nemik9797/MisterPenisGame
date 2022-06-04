from dataclasses import dataclass


@dataclass(frozen=True)
class Display:
    wight = 1024
    height = 768
    default_size = (wight, height)
    fullscreen = False
