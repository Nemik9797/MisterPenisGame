import os

import pygame

from objects.main_menu import Background
from constants import Constant
from utils.standart_functions import print_text


def background_fill(picture_name, screen):
    back_ground_pic = Background(
        os.path.join("content", "Pictures", picture_name), [0, 0]
    )
    screen.blit(
        pygame.transform.scale(
            back_ground_pic.image, (screen.get_width(), screen.get_height())
        ),
        back_ground_pic.rect,
    )


def create_main_menu(screen):
    background_fill("penis-background.jpg", screen)
    print_text(
        "Hello",
        Constant.font.cocuette_font_file_path,
        Constant.font.big_font_size,
        screen.get_width() - screen.get_width() // 2,
        screen.get_height() - screen.get_height() // 4 * 3,
        screen,
        Constant.color.black,
        Constant.color.white,
        bold=False,
        italic=True
    )
