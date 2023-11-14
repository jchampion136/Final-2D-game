import pygame

class Background:
    def __init__(self,screen,width,height):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.parallax_images = []
        
        #create list of background layers and loads to screen
        for i in range(1,7):
            parallax_image = pygame.image.load(f"{i}.png").convert_alpha()
            parallax_image = pygame.transform.scale(parallax_image, ((width, height)))
            self.parallax_images.append(parallax_image)
            self.width = self.parallax_images[0].get_width()
    
    #Copies and draws layers on the screen
    def draw_bg(self,speed,scroll):
        for i in range(5):
            self.screen.blit(self.parallax_images[0], ((i * self.width - scroll * speed, 0)))
            self.screen.blit(self.parallax_images[1], ((i * self.width - scroll * speed, 0)))
            self.screen.blit(self.parallax_images[2], ((i * self.width - scroll * speed, 0)))
            self.screen.blit(self.parallax_images[3], ((i * self.width - scroll * speed, 0)))
            self.screen.blit(self.parallax_images[4], ((i * self.width - scroll * speed, 0)))
            self.screen.blit(self.parallax_images[5], ((i * self.width - scroll * speed, 0)))
        
            speed += 0.2