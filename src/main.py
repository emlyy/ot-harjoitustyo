from ui.game import Game
from ui.sprite_setter import SpriteSet
from ui.events import events
from ui.rooms import Rooms
from ui.starting_screen import StartingScreen
from ui.ending_screen import EndingScreen

def main():
    game = Game()
    setter = SpriteSet()
    start = StartingScreen()
    end = EndingScreen()
    while game.start_screen is True:
        start.events(game)
        start.screen(game)
    while game.running:
        if game.start is True:
            setter.sprites_setter(game)
            setter.groups_setter(game)
            Rooms().first_room(game)
            game.start = False
        events(game)
        game.all_sprites.update()
        game.enemies.update()
        game.door.update()
        game.draw()
    end.add_latest(game)
    end.get_scores()
    while True:
        events(game)
        end.print_screen(game)


if __name__=="__main__":
    main()
  