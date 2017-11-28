#based on "spritesheet1 group - WORKING.py"
#moves in all directions and stops at screen edge. loop reset not in class
#collides with, and stops at, walls

import sys, os, pygame
from Resources.MyLibrary import wall_collisions
from Resources.MyLibrary import MySprite, MyWalls
from pygame.locals import *

#Position variables
new_x = 0
new_y = 0
vel_x = 100
init_x = 100
init_y = 300

#Key variables
key_right = False
key_left = False
key_up = False
key_down = False

#Frame variables
columns = 7
current_column = 0
direction = 0
index_x = 1

#Image & variables
image_width = 700
image_height = 400
screen_width = 1000
screen_height = 600

pygame.init()
pygame.key.set_repeat()
screen = pygame.display.set_mode((screen_width, screen_height))
grid1 = pygame.image.load(os.path.join("images", "1000x600Grid.bmp")).convert_alpha()

#Groups
player_grp = pygame.sprite.Group()
walls_grp = pygame.sprite.Group()

#Sprites
warrior1 = MySprite()
soldier = os.path.join("images", "warrior.png")
warrior1.load(soldier, image_width, image_height, 0, 0, columns)
player_grp.add(warrior1)

wall1 = MyWalls()
wall2 = MyWalls()
wall_img1 = os.path.join("images", "wall4.png")
wall1.load(wall_img1, 100, 100, 300, 200)
wall2.load(wall_img1, 100, 100, 400, 300)
walls_grp.add(wall1)
walls_grp.add(wall2)

#Starting position
warrior1.X = init_x
warrior1.Y = init_y

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_RIGHT:
                key_right = True
            elif event.key == pygame.K_LEFT:
                key_left = True
            elif event.key == pygame.K_UP:
                key_up = True
            elif event.key == pygame.K_DOWN:
                key_down = True

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if key_right:
        if warrior1.X >= 900:
            warrior1.X = 900
        else:
            warrior1.X += vel_x
        if current_column == columns - 1:
            index_x = - 1
        elif current_column == 1:
            index_x = 1
        current_column += index_x
        direction = 3
        key_right = False
    if key_up:
        if warrior1.Y <= 0:
            warrior1.Y = 0
        else:
            warrior1.Y += -vel_x
        if current_column == columns - 1:
            index_x = - 1
        elif current_column == 1:
            index_x = 1
        current_column += index_x
        direction = 1
        key_up = False
    if key_left:
        if warrior1.X <= 0:
            warrior1.X = 0
        else:
            warrior1.X += -vel_x
        if current_column == columns - 1:
            index_x = - 1
        elif current_column == 1:
            index_x = 1
        current_column += index_x
        direction = 2
        key_left = False
    if key_down:
        if warrior1.Y >= screen_height - vel_x:
            warrior1.Y = screen_height - vel_x
        else:
            warrior1.Y += vel_x
        if current_column == columns - 1:
            index_x = -1
        elif current_column == 1:
            index_x = 1
        current_column += index_x
        direction = 0
        key_down = False

    screen.blit(grid1, (0, 0))

    walls_grp.draw(screen)
    player_grp.update(current_column, direction)
    a2 = wall_collisions(direction, warrior1, walls_grp)
    player_grp.draw(screen)

    pygame.display.update()
