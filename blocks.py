__author__ = 'galactic'
from pygame import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#663300"
pltImage = image.load("platform_texture.png")

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pltImage
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    def setXY(self, x, y):

        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pltImage
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        return