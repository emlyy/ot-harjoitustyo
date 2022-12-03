from ui.game import Game
from ui.sprite_setter import sprites_setter
from ui.events import events
from ui.first_room import first_room

def main():
    game = Game()
    while game.start_screen is True:
        events(game)
    while game.running:
        if game.start is True:
            sprites_setter(game)
            first_room(game)
            game.start = False
        events(game)
        game.all_sprites.update()
        game.enemies.update()
        game.draw()


if __name__=="__main__":
    main()
  