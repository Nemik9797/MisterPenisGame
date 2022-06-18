import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, screen_location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = screen_location


class Colorkey_image(pygame.sprite.Sprite):
    def __init__(self, image_file, screen_location, colorkey):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image.set_colorkey(colorkey)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = screen_location
