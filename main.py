import sys
import pygame
from utils.display_functions import ScreenTools
from utils.standart_functions import print_text
from constants import Constant


def main():
    screen_tools = ScreenTools()
    screen = screen_tools.screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen = screen_tools.event_apply(event, screen)
            screen.fill(Constant.color.white)
            print_text(
                'Hello',
                Constant.font.minotaure_font_file_path,
                Constant.font.minotaure_font_size,
                200,
                200,
                screen,
                Constant.color.black
            )
            pygame.display.update()


if __name__ == '__main__':
    main()
