import pgzrun
import os
import random
from pgzhelper import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 1000
HEIGHT = 700
TITLE = 'GAME CENTER'


dino_background1 = Actor('dino_background', (2148,384))
dino_background2 = Actor('dino_background', (3150,384))
obstacle_list = ['box', 'wheels', 'dumpster']
obstacle = Actor(random.choice(obstacle_list), (1050, 580))

yellow_boy_run = Actor('dino_run_1', (250, 500))
yellow_boy_run.images = ['dino_run_2', 'dino_run_3', 'dino_run_4', 'dino_run_5', 'dino_run_6', 'dino_run_7', 'dino_run_8']
yellow_boy_run.fps = 10

yellow_boy_jump_up = Actor('dino_jump_1')
yellow_boy_jump_up.images = ['dino_jump_2', 'dino_jump_3', 'dino_jump_4']
yellow_boy_jump_up.fps = 5

yellow_boy_jump_down = Actor('dino_jump_4')
yellow_boy_jump_down.images = ['dino_jump_5', 'dino_jump_6', 'dino_jump_7', 'dino_jump_8']
yellow_boy_jump_down.fps = 5

dino_speed = 2.5
dino_jump = False

def update ():
        global dino_jump
    #background movement#
        dino_background1.x -= dino_speed
        dino_background2.x -= dino_speed
        if dino_background1.x == -1150:
            dino_background2.x = 3150
        if dino_background2.x == -1150:
            dino_background1.x = 3150

        #obstacle movement#
        if obstacle.x <= -100 :
            obstacle.image = random.choice(obstacle_list)
            obstacle.x = 1050
        else :
            obstacle.x -= dino_speed

        #character movement#
        if dino_jump :
            yellow_boy_run.y -= 5
            yellow_boy_jump_up.animate()
            yellow_boy_run.image = yellow_boy_jump_up.image
            if yellow_boy_run.y <= 210 :
                dino_jump = False
        elif not dino_jump  and yellow_boy_run.y != 500 :
            yellow_boy_jump_down.animate()
            yellow_boy_run.image = yellow_boy_jump_down.image
            if yellow_boy_run.y <= 500 :
                yellow_boy_run.y += 5
        else :
            yellow_boy_run.animate()
            yellow_boy_run.image = yellow_boy_run.image


def draw ():
    dino_background2.draw()
    dino_background1.draw()
    obstacle.draw()
    yellow_boy_run.draw()

def on_key_down(key):
    global dino_jump

    #dino jump#
    if key == keys.SPACE and yellow_boy_run.y >= 500 :
        dino_jump = True

pgzrun.go()