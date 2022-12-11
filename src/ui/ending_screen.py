import pygame
from scores import Data
from sprites.texts import TextBox

class EndingScreen:
    def __init__(self):
        self.scores = []
        self.data = Data()
        self.name = ""
        self.score = 0
        self.end_sprites = pygame.sprite.Group()
        self.end_sprites.add(TextBox((128,0,128), 400, 500, 280, 40))

    def add_latest(self, game):
        self.name = game.score.name
        self.score = game.score.count_total_score()
        self.data.add_scores(self.name, self.score)

    def get_scores(self):
        self.scores = []
        list = self.data.read_top_scores()
        for score in list:
            self.scores.append((score[0], score[1]))
        if len(self.scores) < 4:
            for num in range(4):
                self.scores.append(("empty",0000))

    def print_screen(self, game):
        game.screen.fill((0,0,0))
        self.end_sprites.draw(game.screen)
        game.text("Scoreboard:",game.font1,300,250)
        game.text("latest score:", game.font1, 300, 60)
        game.text(f"{self.name}  {self.score}", game.font1, 300, 110)
        y_cord = 300
        for score in self.scores[0:4]:
            game.text(f"{score[0]}  {score[1]}",game.font1,300,y_cord)
            y_cord += 50
        pygame.display.flip()
