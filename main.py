import os
import sys

import pygame

from constants import Constant
from utils.display_functions import ScreenTools
from utils.standart_functions import print_text
from utils.main_menu_functions import background_fill
from utils.main_menu_functions import create_main_menu


def main():
    screen_tools = ScreenTools()
    screen = screen_tools.screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen = screen_tools.event_apply(event, screen)
            screen.fill(Constant.color.white)
            create_main_menu(screen)
            pygame.display.update()


if __name__ == "__main__":
    main()
