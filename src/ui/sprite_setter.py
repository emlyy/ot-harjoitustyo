from sprites.ran import Ran
from sprites.background import Background
from sprites.texts import TextBox
from config import SPAWN_X, SPAWN_Y, RAN_IMAGE, BG_IMAGE, D_BOX, D_BOX_X, Y2, SCREEN_WIDTH, BOX_HEIGHT

class SpriteSet:
    def __init__(self):
        pass

    def sprites_setter(self, game):
        game.player = Ran(game, SPAWN_X,SPAWN_Y, RAN_IMAGE)
        game.background = Background(0,0,BG_IMAGE)
        game.d_box = TextBox((255,0,0), D_BOX, D_BOX, D_BOX_X, Y2)

    def groups_setter(self, game):
        game.all_sprites.add(game.background,
        TextBox((0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636),
        game.player)
        game.box.add(game.d_box)

    def clear_all_groups(self, game):
        game.all_sprites.empty()
        game.barriers.empty()
        game.enemies.empty()
        game.see_enemies.empty()
        game.box.empty()
