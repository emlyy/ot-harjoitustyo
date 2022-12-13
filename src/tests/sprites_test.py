import unittest
from ui.game import Game
from ui.sprite_setter import SpriteSet
from sprites.ran import Ran
from sprites.item import Item
from sprites.enemy import Enemy
from sprites.barrier import Barrier
from sprites.door import Door
from config import BARRIERS_LIST

class TestSprites(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.setter = SpriteSet()
        self.game.player = Ran(self.game, 300, 300, "src/images/ran-1.png")
        self.game.note = Item(self.game, 500, 300, "src/images/star.png", "read_note", "back", "NOTE_FOUND", "YES", "NO")
        self.game.enemy = Enemy(self.game, 780, 270, "src/images/woodgrem-2.2.png", "normal")
        self.game.door = Door(self.setter,self.game,1130,276)
        self.game.doors.add(self.game.door)
        self.game.enemies.add(self.game.enemy)

    def test_cannot_move_when_note_found(self):
        self.game.player.rect.x = 500
        self.game.note.update()
        self.assertEqual(self.game.can_move, False)

    def test_cannot_move_through_barriers(self):
        for i in BARRIERS_LIST:
            self.game.barriers.add(Barrier(i[0],i[1],i[2],i[3]))
        self.game.player.rect.x = 21
        self.game.player.rect.y = 230
        self.game.player.c_x -= 3
        self.game.player.c_y += 3
        if self.game.can_move is True:
            self.game.player.rect.x += self.game.player.c_x
            self.game.player.collision("x")
            self.game.player.rect.y += self.game.player.c_y
            self.game.player.collision("y")
        self.assertEqual(self.game.player.rect.x, 20)
        self.assertEqual(self.game.player.rect.y, 230+3)

    def test_normal_enemy_collision(self):
        self.assertEqual(self.game.can_move, True)
        self.assertEqual(self.game.enemies.has(self.game.enemy), True)

        self.game.player.rect.x = 780
        self.game.player.rect.y = 275
        self.game.enemy.update()

        self.assertEqual(self.game.can_move, False)
        self.assertEqual(self.game.enemies.has(self.game.enemy), False)
        self.assertEqual(self.game.see_enemies.has(self.game.enemy), True)
    
    def test_boss_enemy_collision(self):
        self.game.enemies.empty()
        self.game.enemy = Enemy(self.game, 780, 270, "src/images/woodgrem-2.2.png", "boss")
        self.game.enemies.add(self.game.enemy)
        self.game.see_enemies.add(self.game.enemy)
        self.assertEqual(self.game.can_move, True)
        self.assertEqual(self.game.enemies.has(self.game.enemy), True)
        self.assertEqual(self.game.see_enemies.has(self.game.enemy), True)

        self.game.player.rect.x = 780
        self.game.player.rect.y = 275
        self.game.enemy.update()

        self.assertEqual(self.game.can_move, False)
        self.assertEqual(len(self.game.enemies), 0)
        self.assertEqual(self.game.see_enemies.has(self.game.enemy), True)

    def test_door_update_where(self):
        self.assertEqual(self.game.door.where, "second")
        self.game.door.update_where("third")
        self.assertEqual(self.game.door.where, "third")
    
    def test_door_works(self):
        self.assertEqual(self.game.room, 1)
        self.assertEqual(self.game.door.where, "second")
        self.game.player.rect.x = 1130
        self.game.player.rect.y = 276
        self.game.doors.update()
        self.assertEqual(self.game.door.where, "third")
        self.assertEqual(self.game.room, 2)
