from dataclasses import dataclass


@dataclass(frozen=True)
class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    light_green = (51, 255, 0)
    main_menu_background = (255, 186, 171)
    gray = (200, 200, 200)
    light_blue = (65, 238, 254)
