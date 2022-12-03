from sprites.ran import Ran
from sprites.background import Background
from sprites.texts import TextBox
from config import SPAWN_X, SPAWN_Y, RAN_IMAGE, BG_IMAGE, D_BOX, D_BOX_X, Y2, SCREEN_WIDTH, BOX_HEIGHT

def sprites_setter(game):
    game.player = Ran(game, SPAWN_X,SPAWN_Y, RAN_IMAGE)
    game.background = Background(0,0,BG_IMAGE)
    game.d_box = TextBox(game, (255,0,0), D_BOX, D_BOX, D_BOX_X, Y2)
    game.box.add(game.d_box)

    game.all_sprites.add(game.background,
    TextBox(game, (0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636),
    game.player)
