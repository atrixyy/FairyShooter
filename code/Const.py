#C
from typing import Literal

import pygame

C_PINK = (255, 174, 201)
C_WHITE= (255, 255, 255)
C_BLACK = (0, 0, 0)
C_GRAY = (128, 128, 128)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 200, 0)
C_BROWN = (185, 122, 87)
C_BLUE = (0, 162, 235)
C_RED = (200,0, 0)
C_CYAN = (0, 128, 128)



# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 2,
    'Level1Bg2' : 4,
    'Level1Bg3' : 8,
    'Level1Bg4' : 10,
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 4,
    'Level2Bg3': 6,
    'Level2Bg4': 8,
    'Level2Bg5': 10,
    'Level2Bg6': 12,
    'Level2Bg7': 14,
    'Player1' : 3,
    'Player1Shot' : 6,
    'Player2' : 3,
    'Player2Shot' : 6,
    'Enemy1' : 2,
    'Enemy1Shot' : 5,
    'Enemy2' : 1,
    'Enemy2Shot' : 5,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Level2Bg7': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 60,
    'Enemy2': 1,
    'Enemy2Shot': 50,
}


ENTITY_SIZE = {
    'Player1' : 0.5,
    'Player2' : 0.176,
    'Enemy1' : 0.5,
    'Enemy2' : 0.5,
    'Player1Shot' : 0.2,
    'Player2Shot' : 0.05,
    'Enemy1Shot' : 0.2,
    'Enemy2Shot' : 0.22,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level2Bg7': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1' : 20,
    'Player2' : 15,
    'Enemy1': 50,
    'Enemy2': 100,

}

#M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

#P
PLAYER_KEY_UP = {'Player2': pygame.K_UP,
                 'Player1': pygame.K_w}

PLAYER_KEY_DOWN = {'Player2': pygame.K_DOWN,
                   'Player1': pygame.K_s}

PLAYER_KEY_LEFT = {'Player2': pygame.K_LEFT,
                   'Player1': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player2': pygame.K_RIGHT,
                    'Player1': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player2': pygame.K_RCTRL,
                    'Player1': pygame.K_LCTRL}


# S
SPAWN_TIME = 3000


# T
TIMEOUT_LEVEL = 20500
TIMEOUT_STEP: int = 100

# W
WIN_WIDTH = 1600
WIN_HEIGHT = 900

#S again because of the WIN_WIDTH
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 100),
    'EnterName': (WIN_WIDTH / 2, 250),
    'Label': (WIN_WIDTH / 2, 330),
    'Name': (WIN_WIDTH / 2, 390),
    0: (WIN_WIDTH / 2, 450),
    1: (WIN_WIDTH / 2, 490),
    2: (WIN_WIDTH / 2, 530),
    3: (WIN_WIDTH / 2, 570),
    4: (WIN_WIDTH / 2, 610),
    5: (WIN_WIDTH / 2, 650),
    6: (WIN_WIDTH / 2, 690),
    7: (WIN_WIDTH / 2, 730),
    8: (WIN_WIDTH / 2, 770),
    9: (WIN_WIDTH / 2, 810),
}
