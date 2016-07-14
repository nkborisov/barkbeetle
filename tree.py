__author__ = 'galactic'

from blocks import *

TREE_WIDTH = 32
TREE_HEIGHT = 32


class Tree(sprite.Sprite):
    def __init__(self, pf):

        sprite.Sprite.__init__(self)
        self.image = Surface((TREE_WIDTH, TREE_HEIGHT))
        self.image = image.load("spruce.png")
        r = pf.getRect()
        self.rect = Rect(r.x, r.y - PLATFORM_HEIGHT, TREE_WIDTH, TREE_HEIGHT)
