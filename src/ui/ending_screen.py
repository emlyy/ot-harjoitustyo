import pygame
from repository.scores import Data
from sprites.texts import TextBox

class EndingScreen:
    """Draws the ending screen.

    Attributes:
        scores: a list of all the names and their scores, as tuples.
        name: name of the user.
        score: score the user got.
        end_sprites: a sprite group for all the sprites to be drawn on
            the ending screen.
    """
    def __init__(self):
        self.scores = []
        self.data = Data()
        self.name = ""
        self.score = 0
        self.end_sprites = pygame.sprite.Group()
        self.end_sprites.add(TextBox((128,0,128), 414, 500, 380, 40))

    def add_latest(self, game):
        """Adds the user's score into the database.
        """
        self.name = game.score.name
        self.score = game.score.count_total_score()
        self.data.add_scores(self.name, self.score)

    def get_scores(self):
        """Makes a list of the scores.
        Fills the list so that there are atleast four tuples.
        """
        self.scores = []
        list = self.data.read_top_scores()
        for score in list:
            self.scores.append((score[0], score[1]))
        if len(self.scores) < 4:
            for num in range(4):
                self.scores.append(("empty",0000))

    def print_screen(self, game):
        """Draws everything.
        """
        game.screen.fill((0,0,0))
        self.end_sprites.draw(game.screen)
        game.text("Scoreboard:",game.font1,414,250)
        game.text("Latest Score:", game.font1, 414, 60)
        game.text(f"{self.name}  {self.score}", game.font1, 414, 110)
        y_cord = 300
        for score in self.scores[0:4]:
            game.text(f"{score[0]}  {score[1]}",game.font1,414,y_cord)
            y_cord += 50
        game.screen.blit(game.font2.render("Thank you for playing!!! Hope you liked my game :]",
        True,(128,0,128)),(280, 700))
        game.screen.blit(game.font2.render("- emlyy",True,(128,0,128)),(330, 750))
        pygame.display.flip()
