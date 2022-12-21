import pygame
from sprites.texts import TextBox
from sprites.background import Background

class StartingScreen:
    """Performs the starting screen.

    Attributes:
        input: A string, the name that the user inputs.
        max_ch: Integer representing the maximum characters the input name
            is allowed to be.
        start_sprites: The sprite group for the sprites needed during the
            starting screen.
    """    
    def __init__(self):
        self.input_text = ""
        self.max_ch = 10
        self.start_sprites = pygame.sprite.Group()
        self.start_sprites.add(TextBox((128,0,128), 400, 525, 730, 180))
        self.start_sprites.add(TextBox((128,0,128), 570, 60, 40, 180))
        self.start_sprites.add(TextBox((128,0,128), 570, 60, 40, 240))
        self.start_sprites.add(TextBox((128,0,128), 570, 60, 40, 300))
        self.start_sprites.add(Background(780, 200, "src/images/controls.png"))
        self.start_sprites.add(Background(780, 420, "src/images/controls-2.png"))
        self.start_sprites.add(Background(780, 520, "src/images/controls-3.png"))
        self.start_sprites.add(Background(780, 620, "src/images/controls-5.png"))
        self.start_sprites.add(Background(40, 510, "src/images/gremking_big.png"))
        self.start_sprites.add(Background(310, 400, "src/images/textbubble.png"))

    def events(self,game):
        """Checks for user input events.

        """        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game.running = True
                    game.score.set_name(self.input_text)
                    break

                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    if len(self.input_text) < self.max_ch:
                        self.input_text += event.unicode

    def screen(self, game):
        """Draws and updates the screen.

        """        
        game.screen.fill((0,0,0))
        self.start_sprites.draw(game.screen)
        game.text("DUNGEON OF MEMORIES",game.font1,30,30)

        game.text("esc - restart game", game.font2, 850, 560)
        game.text("toggle text option", game.font2, 850, 470)
        game.text("select", game.font2, 1010, 630)

        game.text("start typing to input name", game.font2, 60, 200)
        game.text("press ENTER to start game", game.font2, 60, 320)
        game.text("name (max 10 charcters): " + self.input_text, game.font2, 60, 260)
        game.screen.blit(game.font2.render("Welcome!!!",True,(0,0,0)),(350, 420))
        game.screen.blit(game.font2.render("I hope you enjoy",True,(0,0,0)),(350, 460))
        game.screen.blit(game.font2.render("the adventure :]",True,(0,0,0)),(350, 500))
        pygame.display.update()
