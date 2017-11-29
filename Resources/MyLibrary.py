# MyLibrary.py

import pygame
from pygame.locals import *

screen = pygame.display.get_surface()

class MySprite(pygame.sprite.Sprite):
    """Loads the moveable character information"""

    def __init__(self):
        super().__init__()
        self.main_image = None
        self.columns = 0
        self.frame_num = 0
        self.init_x = 0
        self.init_y = 0
        self.width = 0
        self.height = 0

# X property
    def _getx(self):
        return self.rect.x
    def _setx(self, value):
        self.rect.x = value
    X = property(_getx, _setx)
    
# Y property
    def _gety(self):
        return self.rect.y
    def _sety(self, value):
        self.rect.y = value
    Y = property(_gety, _sety)

    def load(self, filename, width, height, init_x, init_y, columns):
        self.main_image = pygame.image.load(filename).convert_alpha()
        self.init_x = init_x
        self.init_y = init_y
        self.width = width
        self.height = height
        self.columns = columns
        self.rect = Rect(init_x, init_y, width, height)

    def update(self, current_column, direction): 

        current_X = current_column * 100
        current_Y = direction * 100
            
        rect = Rect(self.X, self.Y, 100, 100)
        self.rect1 = Rect(current_X, current_Y, 100, 100)
        self.image = self.main_image.subsurface(self.rect1)
        self.rect = rect

class MyWalls(pygame.sprite.Sprite):
    """Class for handling the walls and doors in the game"""
    
    def __init__(self):
        super().__init__()
        self.image = None
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        
# X property
    def _getx(self):
        return self.rect.x
    def _setx(self, value):
        self.rect.x = value
    X = property(_getx, _setx)
    
# Y property
    def _gety(self):
        return self.rect.y
    def _sety(self, value):
        self.rect.y = value
    Y = property(_gety, _sety)
        
    def load(self, filename, width, height, pos_x, pos_y):
        self.image = pygame.image.load(filename).convert_alpha()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = Rect(pos_x, pos_y, width, height)
        
    def update(self, pos_x, pos_y, width, height):
        self.rect = Rect(pos_x, pos_y, width, height)
     
# not working correctly at the moment
def column_check(current_column, columns):
    """loop for the sprite image to display"""
    index_x = 0
    if current_column == columns - 1:
        index_x = -1
    elif current_column == 1:
        index_x = 1
    return index_x
            
def wall_collisions(direction, sprite1, sprite2):
    """Handles collision detection between the player and the walls"""

    ouchie = pygame.sprite.spritecollideany(sprite1, sprite2)
    if ouchie is not None:
        if sprite1.rect.colliderect(ouchie.rect):
            if direction == 3:
                sprite1.rect.right = ouchie.rect.left
            elif direction == 1:
                sprite1.rect.top = ouchie.rect.bottom
            elif direction == 2:
                sprite1.rect.left = ouchie.rect.right
            elif direction == 0:
                sprite1.rect.bottom = ouchie.rect.top    
