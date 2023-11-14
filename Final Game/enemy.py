import pygame
import sys
import random
from projectiles import Projectile

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,width, height):
        super().__init__()
        self.radius = 15
        self.image = pygame.Surface((30,30))
        pygame.draw.circle(self.image, (255, 0, 0), (self.radius, self.radius), self.radius)
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect.width 
        self.rect.y = random.randint(self.radius, 600 - self.radius)
        self.speedx = random.randrange(1,4)
        self.width = width
        self.height = height
    
    #updates position of enemy
    def update(self):
        self.rect.x -= self.speedx
        
        #remove enemy sprite if exits the screen
        if self.rect.right < 0 or self.rect.top > self.height:
            self.kill()
    
    #Placeholder- enemy will shoot projectiles when implemented
    def shoot(self,all_projectiles):
        projectile = Projectile(self.rect.x, self.rect.y)
        all_projectiles.add(projectile)