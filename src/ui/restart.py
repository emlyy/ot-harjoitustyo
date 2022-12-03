from config import SPAWN_X, SPAWN_Y, SCREEN_WIDTH, BOX_HEIGHT, BARRIERS_LIST
from sprites.texts import TextBox
from sprites.barrier import Barrier

def restart(game):
    game.all_sprites.empty()
    game.barriers.empty()
    game.enemies.empty()
    game.see_enemies.empty()

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

    game.all_sprites.add(game.background,
    TextBox(game, (0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636),
    game.player, game.note)
    game.enemies.add(game.enemy)

    for i in BARRIERS_LIST:
        game.barriers.add(Barrier(i[0],i[1],i[2],i[3]))
