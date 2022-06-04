import sys
import pygame
from utils import display_functions
from utils.standart_functions import print_text
from constants import Constant


# standart_font = pygame.font.Font(, 36)
# minotaure_font = pygame.font.Font(os.path.join(_cwd, 'constants', 'fonts', 'Minotaure.ttf'), 36)


def main(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen = display_functions.fullscreenMode(event, screen)
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
    screen_init = display_functions.displayInit()
    main(screen_init)
