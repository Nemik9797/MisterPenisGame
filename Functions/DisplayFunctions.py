import pygame
import Constants.DisplayVariables as consts

def displayInit():
    pygame.init()
    screen = pygame.display.set_mode(consts.DEFAULT_SIZE)
    return screen

def fullscreenMode(event, currentScreen):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            consts.FULLSCREEN = not consts.FULLSCREEN
            size = pygame.display.list_modes()[0]
            screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
            # После двойного нажатия F11 восстановить исходный размер интерфейса
            if consts.FULLSCREEN == False:
                size = consts.DEFAULT_SIZE
                screen = pygame.display.set_mode(size)
            else:
                screen = currentScreen
        else:
            screen = currentScreen
    else:
        screen = currentScreen
    return screen