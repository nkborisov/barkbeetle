__author__ = 'galactic'
from blocks import Platform
from pygame import *

class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("fire.png")
