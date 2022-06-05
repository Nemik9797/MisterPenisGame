import pygame


def print_text(
    text, font_file_path, font_size, x, y, screen, textColor, backgroundColor=None, bold=False, italic=False
):

    font = pygame.font.Font(font_file_path, font_size)
    font.bold = bold
    font.italic = italic
    font_text = font.render(text, True, textColor, backgroundColor)
    text_rect = font_text.get_rect()
    text_rect.center = (x, y)
    screen.blit(font_text, text_rect)
