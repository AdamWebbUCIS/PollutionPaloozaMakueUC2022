
from time import time
import pygame
import os 

class Player(pygame.sprite.Sprite): 
    def __init__(self, is_alive=True):
        super().__init__()
        self.is_alive = is_alive
        self.x_pos = 475
        self.y_pos = 375
        
        self.player_index = 0
        self.player_net = [
            pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 5.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 4.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 3.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 2.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 1.png')).convert_alpha()
        ]

        self.active_level = None

        self.image_index = 0
        self.images = [
            pygame.transform.scale(self.player_net[self.player_index], (250, 250)),
            pygame.transform.flip(pygame.transform.scale(self.player_net[self.player_index], (250, 250)), True, False)
        ]
        self.image = self.images[self.image_index]
        self.health = 100
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

    def extend_pole(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            if (self.player_index < 4):
                self.player_index += 1
                self.images = [
                    pygame.transform.scale(self.player_net[self.player_index], (250, 250)),
                    pygame.transform.flip(pygame.transform.scale(self.player_net[self.player_index], (250, 250)), True, False)
                ]

    def retract_pole(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            if (self.player_index > 0):
                self.player_index -= 1
                self.images = [
                    pygame.transform.scale(self.player_net[self.player_index], (250, 250)),
                    pygame.transform.flip(pygame.transform.scale(self.player_net[self.player_index], (250, 250)), True, False)
                ]
    
    def flip_image(self):
        self.image = self.images[self.image_index]

    def update(self):
        self.flip_image()
        self.extend_pole()
        self.retract_pole()

