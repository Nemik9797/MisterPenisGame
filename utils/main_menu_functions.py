import os
import sys

import pygame

from objects.pictures import Colorkey_image
from objects.pictures import Background
from constants import Constant
from objects.button import Button


def stretching(screen):
    return (screen.get_width() / Constant.display.wight_fullscreen,
            screen.get_height() / Constant.display.height_fullscreen)


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


def game_logo_fill(picture_name, screen):
    game_logo_pic = Colorkey_image(
        os.path.join("content", "Pictures", picture_name),
        [screen.get_width() // 20, screen.get_height() // 30],
        Constant.color.main_menu_background
    )
    screen.blit(
        pygame.transform.scale(
            game_logo_pic.image,
            (game_logo_pic.image.get_width() * stretching(screen)[0],
             game_logo_pic.image.get_height() * stretching(screen)[1]
             )
        ),
        game_logo_pic.rect,
    )


def on_play():
    print("game start")


def on_options():
    print("game options")


def on_quit():
    sys.exit()


def create_main_menu(screen, event):
    background_fill("penis-background-redacted.png", screen)
    game_logo_fill("mrPenisGame.png", screen)
    for i, (text, handler) in enumerate((('Новая игра', on_play),
                                         ('Настройки', on_options),
                                         ('Выход', on_quit))):
        b = Button(screen.get_width() // 2,
                   screen.get_height() // 2 + 100 * i,
                   text,
                   Constant.font.standart_font_file_path, Constant.font.realy_big_font_size,
                   screen,
                   Constant.color.white,
                   bold=False, italic=False, underline=False,
                   on_click=handler)
        b.handle_mouse_event(type=event.type)
