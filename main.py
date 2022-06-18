import os
import sys

import pygame

from constants import Constant
from utils.display_functions import ScreenTools
from utils.standart_functions import print_text
from utils.main_menu_functions import background_fill
from utils.main_menu_functions import create_main_menu
from utils.sounds_functions import play_background_sound


def main():
    screen_tools = ScreenTools()
    screen = screen_tools.screen
    play_background_sound(Constant.sound.main_menu_sound)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen = screen_tools.event_apply(event, screen)
            screen.fill(Constant.color.white)
            create_main_menu(screen, event)
            pygame.display.update()


if __name__ == "__main__":
    main()
