import pygame

from constants import Constant
from utils.standart_functions import print_text


# @property
def back_color(state):
    return dict(normal=Constant.color.main_menu_background,
                hover=Constant.color.light_blue,
                pressed=Constant.color.light_green)[state]


class Button(object):
    def __init__(self,
                 x, y,
                 text,
                 font_file_path, font_size,
                 screen,
                 text_color,
                 bold, italic, underline,
                 on_click=lambda x: None):
        self.state = 'normal'
        self.on_click = on_click
        self.text = text
        self.font_file_path = font_file_path
        self.font_size = font_size
        self.x = x
        self.y = y
        self.screen = screen
        self.text_color = text_color
        self.bold = bold
        self.italic = italic
        self.underline = underline

        self.back = back_color(self.state)
        self.print_text = print_text(text,
                                     font_file_path,
                                     font_size,
                                     x, y, screen,
                                     text_color,
                                     back_color(self.state),
                                     bold, italic, underline)
        x, y = pygame.mouse.get_pos()
        self.mouse_pos = pygame.Rect(x, y, 1, 1)

    def handle_mouse_event(self, type):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move()
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down()
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up()
        return self

    def handle_mouse_move(self):
        if self.print_text.colliderect(self.mouse_pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'
        print_text(self.text,
                   self.font_file_path,
                   self.font_size,
                   self.x, self.y, self.screen,
                   self.text_color,
                   back_color(self.state),
                   self.bold, self.italic, self.underline)

    def handle_mouse_down(self):
        if self.print_text.colliderect(self.mouse_pos):
            self.state = 'pressed'
        print_text(self.text,
                   self.font_file_path,
                   self.font_size,
                   self.x, self.y, self.screen,
                   self.text_color,
                   back_color(self.state),
                   self.bold, self.italic, self.underline)

    def handle_mouse_up(self):
        if self.print_text.colliderect(self.mouse_pos):
            self.on_click()
            self.state = 'hover'
        print_text(self.text,
                   self.font_file_path,
                   self.font_size,
                   self.x, self.y, self.screen,
                   self.text_color,
                   back_color(self.state),
                   self.bold, self.italic, self.underline)
