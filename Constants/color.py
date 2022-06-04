from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
