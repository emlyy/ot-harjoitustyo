from ui.game import Game
from ui.sprite_setter import SpriteSet
from ui.events import events
from ui.first_room import first_room
#from ui.ending_screen import EndingScreen

def main():
    game = Game()
    setter = SpriteSet()
    #end = EndingScreen()
    while game.start_screen is True:
        events(game)
    while game.running:
        if game.start is True:
            setter.sprites_setter(game)
            setter.groups_setter(game)
            first_room(game)
            game.start = False
        events(game)
        game.all_sprites.update()
        game.enemies.update()
        game.draw()
    #end.get_scores()
    #end.print_screen()


if __name__=="__main__":
    main()
  