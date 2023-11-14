import sys
import pygame
from pygame.locals import*
from background import Background
from player import Player
from enemy import Enemy
from npc import NPC

pygame.init()
#declarations
screen_width = 800
screen_height = 432
FPS = 40
posx = 50
posy = 180
scroll = 0
speed = 1
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("The Wild Things")
background = Background(screen,screen_width,screen_height)
clock = pygame.time.Clock()
all_enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_projectiles = pygame.sprite.Group()
player = Player(screen, screen_width, screen_height,all_projectiles,all_sprites)
npc = NPC()
font = pygame.font.Font(None,36)

spawn_timer = 0
spawn_interval = 100

while True:
    #sets FPS
    clock.tick(FPS)
    
    #Draws Background
    background.draw_bg(speed,scroll)
    
    #Moves player character
    player.move()
    
    #Creates various text banners
    lives_text = font.render(f"Lives: {int(player.lives)}", True, (255,255,255))
    game_over_text = font.render(f"Game Over, You Lose! Press ESC to quit", True, (255,255,255))
    you_win_text = font.render(f"Congratulations, You Win! Press ESC to quit", True, (255,255,255))
    
    #applies player collision with enemies
    player.collision_det(all_enemies)
    
    #copies the life counter on the screen
    screen.blit(lives_text, (10,10))
    
    #apply game over message if player dies
    if player.lives <= 0:
        message = game_over_text
    
    #Apply "you win" message if player reaches npc
    if pygame.sprite.collide_rect(player,npc):
        message = you_win_text
    
    #displays the chosen message then update the screen
    if player.lives <= 0 or pygame.sprite.collide_rect(player,npc):
        screen.blit(message,(screen_width// 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    
    #Creates moving parallax effect
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 4
    if key[pygame.K_RIGHT] and scroll < 1500:
        scroll += 4
    
    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        enemy = Enemy(screen_width, screen_height)
        enemy.rect.x = screen_width
        enemy.rect.y = 345
        all_enemies.add(enemy)
        all_sprites.add(enemy)
        spawn_timer = 0  # Reset the timer after spawning an enemy
            
    
    #Ends program by pressing escape or closing the window
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
    for projectile in all_projectiles:
        projectile.kill_on_collision(all_enemies)
            
        projectile.update()
        screen.blit(projectile.image, projectile.rect)
    
    player.draw()
    all_enemies.update()
    all_enemies.draw(screen)
    pygame.display.update()
    
    #Displays Npc and updates screen
    screen.blit(npc.image, npc.rect)
    pygame.display.update()
    
        
