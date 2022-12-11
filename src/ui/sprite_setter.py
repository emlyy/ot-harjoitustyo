from sprites.ran import Ran
from sprites.background import Background
from sprites.texts import TextBox
from sprites.door import Door
from sprites.note import Note
from sprites.enemy import Enemy
from sprites.barrier import Barrier
from config import SPAWN_X, SPAWN_Y, NOTE_X, NOTE_Y, NOTE_IMAGE,RAN_IMAGE, BG_IMAGE, D_BOX, D_BOX_X, Y2, BARRIERS_LIST, BARRIERS_LIST_2, BARRIERS_LIST_3, ENEMY_1_X, ENEMY_1_Y, ENEMY_IMAGE, BG_IMAGE_2, BG_IMAGE_3, SCREEN_WIDTH, BOX_HEIGHT
class SpriteSet:
    def __init__(self):
        pass

    def sprites_setter(self, game):
        game.player = Ran(game, SPAWN_X,SPAWN_Y, RAN_IMAGE)
        game.background = Background(0,0,BG_IMAGE)
        game.d_box = TextBox((255,0,0), D_BOX, D_BOX, D_BOX_X, Y2)
        game.box.add(game.d_box)
        game.door = (Door(game,1130,276))
        game.doors.add(game.door)

    def groups_setter(self, game):
        game.all_sprites.add(game.background,
        TextBox((0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636),
        game.player)

    def clear_all_groups(self, game):
        game.all_sprites.empty()
        game.barriers.empty()
        game.enemies.empty()
        game.see_enemies.empty()
        game.player.spawn()

    def add_barriers(self,list, game):
        for i in list:
            game.barriers.add(Barrier(i[0],i[1],i[2],i[3]))

    def first_room(self, game):
        game.note = Note(game, NOTE_X, NOTE_Y, NOTE_IMAGE)
        game.enemy = Enemy(game, ENEMY_1_X, ENEMY_1_Y, ENEMY_IMAGE)
        game.all_sprites.add(game.note)
        game.enemies.add(game.enemy)

        self.add_barriers(BARRIERS_LIST,game)

    def second_room(self, game):
        game.second_room = False
        self.clear_all_groups(game)
        game.all_sprites.add(Background(0,0,BG_IMAGE_2),
        TextBox((0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636),
        game.player)
        self.add_barriers(BARRIERS_LIST_2,game)

    def third_room(self, game):
        game.third_room = False
        self.clear_all_groups(game)
        game.all_sprites.add(Background(0,0,BG_IMAGE_3),
        TextBox((0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636),
        game.player)
        self.add_barriers(BARRIERS_LIST_3,game)
