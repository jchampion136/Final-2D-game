import pygame
from projectiles import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self,screen,width,height,all_projectiles,all_sprites):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.image = pygame.Surface((30,30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (0,315)
        self.speed = 2
        self.is_jumping = False
        self.momentum = 0
        self.projectiles = all_projectiles
        self.sprites = all_sprites
        self.lives = 3
        self.gravity = 0.25
        
    #Player's movements
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key[pygame.K_SPACE]:
            self.shoot()
        if not self.is_jumping and key[pygame.K_UP]:
            self.is_jumping = True
            self.momentum = -6 
    
        self.momentum += self.gravity 
        self.rect.y += self.momentum 
        
        if self.rect.y >= 350:
            self.is_jumping = False
            self.rect.y = 350
            
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    # Keeps player from walking off left side of screen and applies collision with enemies
    def collision_det(self, enemy_group):
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(self.width, self.rect.right)
        collisions = pygame.sprite.spritecollide(self, enemy_group, True)
        for collide in collisions:
            self.lives -= 1
        if self.lives <= 0:
            self.kill()
    
    #Shoot projectiles
    def shoot(self):
        new_projectile = Projectile(self.rect.right, self.rect.centery)
        self.projectiles.add(new_projectile)
        self.sprites.add(new_projectile)
        
        

