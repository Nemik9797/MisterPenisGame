import pygame

from constants.display import Display


class ScreenTools:
    def __init__(self):
        self.fullscreen_mode = Display.fullscreen
        self.screen = self.display_init()

    def display_init(self):
        pygame.init()
        if self.fullscreen_mode:
            screen = pygame.display.set_mode(Display.default_size, pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode(Display.default_size)
        return screen

    def switch_fullscreen(self):
        if self.fullscreen_mode:
            size = Display.default_size
            new_screen = pygame.display.set_mode(size)
        else:
            size = pygame.display.list_modes()[0]
            new_screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.fullscreen_mode = ~self.fullscreen_mode
        return new_screen

    def event_apply(self, event, screen):
        new_screen = screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                new_screen = self.switch_fullscreen()
        return new_screen
