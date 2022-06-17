import pygame
from pygame.sprite import *
from utils.standart_functions import print_text
from constants import Constant


@property
def back_color(self):
    return dict(normal=Constant.color.main_menu_background,
                hover=Constant.color.light_blue,
                pressed=Constant.color.light_green)[self.state]


class Sprite_Mouse_Location(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)
        print(self.rect)


class Button:
    def __init__(self,
                 x, y,
                 w, h,
                 text,
                 font_file_path, font_size,
                 screen,
                 textColor, backgroundColor,
                 bold, italic, underline,
                 on_click=lambda x: None,
                 padding=0):
        # super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click

        self.text = print_text(text,
                               font_file_path,
                               font_size,
                               x, y, screen,
                               textColor,
                               backgroundColor,
                               bold, italic, underline)
        x, y = pygame.mouse.get_pos()
        self.mouse_pos = pygame.Rect(x, y, 1, 1)

        '''TextObject(x + padding,
                               y + padding, lambda: text,
                               c.button_text_color,
                               c.font_name,
                               c.font_size)'''

    def handle_mouse_event(self, type):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move()
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down()
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up()

    def handle_mouse_move(self):
        if self.text.colliderect(self.mouse_pos):
            if self.state != 'pressed':
                #self.background_color = Constant.color.light_blue
                self.state = 'hover'
                #print(self.background_color)
        else:
            self.state = 'normal'

    def handle_mouse_down(self):
        if self.text.colliderect(self.mouse_pos):
            self.state = 'pressed'
            self.background_color = Constant.color.light_green

    def handle_mouse_up(self):
        if self.text.colliderect(self.mouse_pos):
            self.on_click(self)
            self.state = 'hover'
