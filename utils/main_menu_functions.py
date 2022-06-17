import os
import sys

import pygame

from objects.main_menu import Game_logo
from objects.main_menu import Background
from constants import Constant
from objects.button import Button


class Game:
    def __init__(self):
        self.objects = []
        self.menu_buttons = []
        self.mouse_handlers = []


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
    game_logo_pic = Game_logo(
        os.path.join("content", "Pictures", picture_name), [screen.get_width() // 20, screen.get_height() // 30]
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


def on_play(button):
    print("game start")


def on_quit(button):
    sys.exit()


def create_menu(screen, event):
    for i, (text, handler) in enumerate((('PLAY', on_play),
                                         ('QUIT', on_quit))):
        b = Button(500, 400 + (200) * i,
                   100, 100,
                   text,
                   Constant.font.standart_font_file_path, Constant.font.realy_big_font_size,
                   screen,
                   Constant.color.white, Constant.color.main_menu_background,
                   bold=False, italic=False, underline=False,
                   on_click=handler,
                   padding=5)
        b.handle_mouse_event(type=event.type)


def create_main_menu(screen, event):
    background_fill("penis-background.jpg", screen)
    game_logo_fill("mrPenisGame.png", screen)
    create_menu(screen, event)



    '''new_game = print_text(
        "Новая игра",
        Constant.font.standart_font_file_path,
        Constant.font.realy_big_font_size,
        screen.get_width() - screen.get_width() // 2,
        screen.get_height() - screen.get_height() // 7 * 4,
        screen,
        Constant.color.white,
        Constant.color.main_menu_background,  # Constant.color.white
        bold=False,
        italic=False,
        underline=True
    )
    options = print_text(
        "Опции",
        Constant.font.standart_font_file_path,
        Constant.font.realy_big_font_size,
        screen.get_width() - screen.get_width() // 2,
        screen.get_height() - screen.get_height() // 7 * 3,
        screen,
        Constant.color.white,
        Constant.color.main_menu_background,  # Constant.color.white
        bold=False,
        italic=False,
        underline=True
    )
    exit = print_text(
        "Выйти",
        Constant.font.standart_font_file_path,
        Constant.font.realy_big_font_size,
        screen.get_width() - screen.get_width() // 2,
        screen.get_height() - screen.get_height() // 7 ,
        screen,
        Constant.color.white,
        Constant.color.main_menu_background,  # Constant.color.white
        bold=False,
        italic=False,
        underline=True
    )
    exit.rect
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if event.pos'''
