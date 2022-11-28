from ui.game import Game
from ui.sprite_setter import sprites
from ui.events import events

def main():
    game = Game()
    while game.start_screen is True:
        events(game)
    while game.running:
        if game.start is True:
            sprites(game)
            game.start = False
        events(game)
        game.all_sprites.update()
        game.draw()


if __name__=="__main__":
    main()
  