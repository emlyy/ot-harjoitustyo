from sprites.ran import Ran
from sprites.background import Background
from sprites.texts import TextBox
from sprites.door import Door
from sprites.item import Item
from sprites.enemy import Enemy
from sprites.barrier import Barrier
from text_lines import (YES, NO, NOTE_FOUND, CHEESE, EAT, DONT_EAT, RANS_MEMORY_BOOK,
READ, IGNORE, WATER_1, SWORD_FOUND, YES_SWORD)
from config import (SPAWN_X, SPAWN_Y, NOTE_X, NOTE_Y, NOTE_IMAGE,RAN_IMAGE,
BG_IMAGE, D_BOX, D_BOX_X, Y2, BARRIERS_LIST,DECORE_BARRIERS_2, DECORE_BARRIERS_3,
BARRIERS_LIST_2, BARRIERS_LIST_3, ENEMY_1_X, ENEMY_1_Y, ENEMY_2_X, ENEMY_2_Y,
ENEMY_3_X, ENEMY_3_Y, ENEMY_4_X, ENEMY_4_Y, ENEMY_IMAGE, BG_IMAGE_2, BG_IMAGE_3,
SCREEN_WIDTH, BOX_HEIGHT, CHEESE_X, CHEESE_Y, CHEESE_IMAGE, KING_IMAGE, DECORE_1,
DECORE_2, DECORE_3, DECORE_4, DECORE_5, INVIS, DECORE_2X, DECORE_2Y, DECORE_3X, DECORE_3Y)
class SpriteSet:
    """Sets all the needed sprites during game.

    """    
    def __init__(self):
        pass

    def sprites_setter(self, game):
        """The sprites needed through out the whole game.

        Args:
            game (Game Class): Connection to the game.
        """
        self.background = Background(0,0,BG_IMAGE)
        self.text_box = TextBox((0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636)
        game.player = Ran(game, SPAWN_X,SPAWN_Y, RAN_IMAGE)
        game.d_box = TextBox((255,0,0), D_BOX, D_BOX, D_BOX_X, Y2)
        game.box.add(game.d_box)
        game.door = (Door(self,game,1130,276))
        game.doors.add(game.door)

    def clear_all_groups(self, game):
        """Clears groups and sets player cordinates to spawn.

        """
        game.all_sprites.empty()
        game.barriers.empty()
        game.enemies.empty()
        game.see_enemies.empty()
        game.player.spawn()
        game.items.empty()

    def add_barriers(self,list, game):
        """Updates the barriers sprite group.

        Args:
            list (list): Of lists, where each list represents one
            barrier. The lists consist of integers ([1,2,3,4]) where
            1 is the width, 2 is height, 3 is the x cordinate and
            4 is the y cordinate of that barrier.
        """
        for i in list:
            game.barriers.add(Barrier(i[0],i[1],i[2],i[3]))

    def first_room(self, game):
        """Sprites needed specifically in room 1.

        """
        game.note = Item(game, NOTE_X, NOTE_Y,
        NOTE_IMAGE,"read_note", "back", NOTE_FOUND, YES, NO)
        game.enemy = Enemy(game, ENEMY_1_X, ENEMY_1_Y, ENEMY_IMAGE, "normal")
        water = Item(game, DECORE_2X, DECORE_2Y, INVIS,"water", "no water",WATER_1, YES, NO)

        game.all_sprites.add(water, self.background, self.text_box, game.player, game.note)
        game.enemies.add(game.enemy)
        self.add_barriers(BARRIERS_LIST,game)

    def second_room(self, game):
        """Sprites needed specifically in room 2.

        """
        game.room = 2
        self.clear_all_groups(game)

        game.cheese = Item(game, CHEESE_X, CHEESE_Y, CHEESE_IMAGE,
        "eat", "don't eat",CHEESE, EAT, DONT_EAT)
        memory_book = Item(game, DECORE_2X, DECORE_2Y, INVIS,
        "memory book", "back",RANS_MEMORY_BOOK, READ, IGNORE)
        sword = Item(game, DECORE_3X, DECORE_3Y, INVIS,
        "yes sword", "back",SWORD_FOUND, YES_SWORD, DONT_EAT)

        decore_1 = Background(500,20,DECORE_1)
        decore_2 = Background(590,100,DECORE_2)
        decore_3 = Background(520,425,DECORE_3)
        decore_4 = Background(810,440,DECORE_4)

        game.all_sprites.add(memory_book, sword,
        Background(0,0,BG_IMAGE_2), self.text_box, decore_1, decore_2,
        game.player, decore_3, game.cheese, decore_4)
        game.items.add(game.cheese)
        self.add_barriers(BARRIERS_LIST_2,game)
        self.add_barriers(DECORE_BARRIERS_2,game)

    def third_room(self, game):
        """Sprites needed specifically in room 3.

        """
        game.room = 3
        self.clear_all_groups(game)

        barrel_1 = Background(320,420,DECORE_5)
        barrel_2 = Background(300,460,DECORE_5)
        barrel_3 = Background(340,440,DECORE_5)
        crate_1 = Background(660,40,DECORE_3)
        crate_2 = Background(690,100,DECORE_3)

        game.all_sprites.add(Background(0,0,BG_IMAGE_3),self.text_box, crate_1, crate_2,
        game.player, barrel_1, barrel_3, barrel_2)
        game.enemies.add(Enemy(game,ENEMY_2_X,ENEMY_2_Y,ENEMY_IMAGE, "boss"),
        Enemy(game,ENEMY_3_X,ENEMY_3_Y,ENEMY_IMAGE,"boss"),
        Enemy(game,ENEMY_4_X,ENEMY_4_Y,KING_IMAGE,"boss"))
        game.see_enemies.add(Enemy(game,ENEMY_2_X,ENEMY_2_Y,ENEMY_IMAGE, "boss"),
        Enemy(game,ENEMY_3_X,ENEMY_3_Y,ENEMY_IMAGE,"boss"),
        Enemy(game,ENEMY_4_X,ENEMY_4_Y,KING_IMAGE,"boss"))
        self.add_barriers(BARRIERS_LIST_3,game)
        self.add_barriers(DECORE_BARRIERS_3,game)
