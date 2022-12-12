from ui.game import Game
from ui.sprite_setter import SpriteSet
from ui.events import events
from ui.starting_screen import StartingScreen
from ui.ending_screen import EndingScreen

def main():
    """The game loop.

    While running is True checks for user events, updates all the sprites
    and draws the screen. First while loop is for starting screen and third
    while loop for ending screen.
    """    
    game = Game()
    setter = SpriteSet()
    start = StartingScreen()
    end = EndingScreen()
    while game.running is False:
        start.events(game)
        start.screen(game)
    setter.sprites_setter(game)
    setter.groups_setter(game)
    setter.first_room(game)
    while game.running:
        events(game)
        game.all_sprites.update()
        game.enemies.update()
        game.doors.update()
        game.draw()
    end.add_latest(game)
    end.get_scores()
    while True:
        events(game)
        end.print_screen(game)


if __name__=="__main__":
    main()
  