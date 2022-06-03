
def PrintText(text, x, y, screen):
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


