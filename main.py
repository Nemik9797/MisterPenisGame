import sys
import pygame
import Functions.DisplayFunctions as display
import Constants.Colors as colors
import Functions.StandartFunctions as standartFunc

screen = display.displayInit()

import Constants.Fonts as fonts

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        screen = display.fullscreenMode(event, screen)
        screen.fill(colors.WHITE)
        text = fonts.STANDART_FONT.render('Hello', True, colors.BLACK, colors.WHITE)
        standartFunc.PrintText(text, 200, 200, screen)
        pygame.display.update()

