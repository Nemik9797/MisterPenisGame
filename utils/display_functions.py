import pygame
from constants.display import Display


def displayInit():
    pygame.init()
    screen = pygame.display.set_mode(Display.default_size)
    return screen


def fullscreenMode(event, currentScreen):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            fullscreen = ~(Display.full_screen)
            size = pygame.display.list_modes()[0]
            screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
            # После двойного нажатия F11 восстановить исходный размер интерфейса
            if not fullscreen:
                size = Display.default_size
                new_screen = pygame.display.set_mode(size)
            else:
                new_screen = currentScreen
        else:
            new_screen = currentScreen
    else:
        new_screen = currentScreen
    return new_screen
