from config import SPAWN_X, SPAWN_Y
from ui.sprite_setter import SpriteSet
from ui.rooms import Rooms

def restart(game):
    SpriteSet().clear_all_groups(game)
    SpriteSet().groups_setter(game)

    game.can_move = True
    game.decisions = False
    game.next = False
    game.actions = False
    game.water = False
    game.weapon = False
    game.combat = False

    game.update_text(game.current_text1, "")
    game.update_text(game.decision1, "")
    game.update_text(game.decision2, "")
    game.text_actions.counter = 0

    game.player.rect.x = SPAWN_X
    game.player.rect.y = SPAWN_Y

    Rooms().first_room(game)
