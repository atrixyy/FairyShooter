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

    @abstractmethod
    def move(self):
        pass
