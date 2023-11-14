import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))  
        self.rect = self.image.get_rect()
       
        #starting location for npc
        self.rect.x = 750  
        self.rect.y = 345  