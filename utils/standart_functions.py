def PrintText(text, fontName,
              x, y,
              screen,
              textColor, backgroundColor = None):
    fontText = fontName.render(text, True, textColor, backgroundColor)
    textRect = fontText.get_rect()
    textRect.center = (x, y)
    screen.blit(fontText, textRect)

