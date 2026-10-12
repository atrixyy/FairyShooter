#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractstaticmethod, abstractmethod

import pygame.image

from code.Const import ENTITY_SIZE, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

        if name in ENTITY_SIZE:
            size = ENTITY_SIZE[name]
            width = int(self.surf.get_width() * size)
            height = int(self.surf.get_height() * size)
            self.surf = pygame.transform.scale(self.surf, (width, height))

        self.rect = self.surf.get_rect(left=position[0], top=position[1])

        self.frames = [self.surf]

        if name in ['Player1', 'Enemy1', 'Enemy2']:
            self.frames = [
                pygame.image.load('./asset/' + name + '.png').convert_alpha(),
                pygame.image.load('./asset/' + name + '_1.png').convert_alpha(),
                pygame.image.load('./asset/' + name + '_2.png').convert_alpha()
            ]

        self.frame_index = 0
        self.animation_timer = 0

    def animate(self):
        if len(self.frames) > 1:
            self.animation_timer += 1

            if self.animation_timer >= 8:
                self.animation_timer = 0

                self.frame_index += 1

                if self.frame_index >= len(self.frames):
                    self.frame_index = 0

                self.surf = self.frames[self.frame_index]

                if self.name in ENTITY_SIZE:
                    self.surf = pygame.transform.scale(
                        self.surf,
                        (int(self.rect.width), int(self.rect.height))
                    )
    @abstractmethod
    def move(self):
        pass
