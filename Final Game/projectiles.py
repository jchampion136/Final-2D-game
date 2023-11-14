import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 5
        
    #updates projectile
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 800:
            self.kill() #removes projectile if it goes off screen
    
    #Kills enemies on collision wth projectiles
    def kill_on_collision(self, enemies_group):
        enemies_hit = pygame.sprite.spritecollide(self, enemies_group, True)
        
        #remove both the enemy and the projectile on collision
        for enemy in enemies_hit:
            self.kill()
            enemy.kill()