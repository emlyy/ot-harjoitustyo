import pygame
from sprites.ran import Ran
from sprites.background import Background


class CaveGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((1184, 980))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        
        self.background_color = (55,55,55)
        self.spawn_x = 20
        self.spawn_y = 290
        self.ran_image = "src/images/ran1.png"
        self.bg_image = "src/images/cave_tilesheet-1.png"
        
        # when starting the game or entering a new room
        self.start = True

        # for the game loop
        self.running = True
        
        pygame.init()
        

    def sprites(self):
        # for making the sprites when game starts, first room
        self.player = Ran(self.spawn_x,self.spawn_y, self.ran_image)
        self.bg = Background(0,0,self.bg_image)
        self.all_sprites.add(self.bg)
        self.all_sprites.add(self.player)
        


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
            
            # player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.c_x -= self.player.speed
                if event.key == pygame.K_d:
                    self.player.c_x += self.player.speed
                if event.key == pygame.K_s:
                    self.player.c_y += self.player.speed
                if event.key == pygame.K_w:
                    self.player.c_y -= self.player.speed
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.player.c_x = 0
                if event.key == pygame.K_d:
                    self.player.c_x = 0
                if event.key == pygame.K_s:
                    self.player.c_y = 0
                if event.key == pygame.K_w:
                    self.player.c_y = 0

        

    def draw(self):
        # draws everything on the screen
        self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        self.clock.tick(60)


    def main(self):
        while self.running:
            if self.start == True:
                self.sprites()
                self.start = False
            self.events()
            self.all_sprites.update()
            self.draw()

        

if __name__=="__main__":

    game = CaveGame()
    
    game.main()

    

    
        