import unittest
from main import CaveGame

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = CaveGame()
        self.game.sprites()
        
    
    def test_ran_spawns_correctly(self):
        self.assertEqual(self.game.player.rect.x , self.game.spawn_x)
        self.assertEqual(self.game.player.rect.y , self.game.spawn_y)

    def test_ran_moves_left(self):
        self.game.player.c_x -= self.game.player.speed
        x = self.game.player.rect.x
        self.game.player.update()
        self.assertEqual(self.game.player.rect.x, x - self.game.player.speed)
        
    def test_ran_moves_right(self):
        self.game.player.c_x += self.game.player.speed
        x = self.game.player.rect.x
        self.game.player.update()
        self.assertEqual(self.game.player.rect.x, x + self.game.player.speed)

    def test_ran_moves_up(self):
        self.game.player.c_y -= self.game.player.speed
        x = self.game.player.rect.y
        self.game.player.update()
        self.assertEqual(self.game.player.rect.y, x - self.game.player.speed)

    def test_ran_moves_down(self):
        self.game.player.c_y += self.game.player.speed
        x = self.game.player.rect.y
        self.game.player.update()
        self.assertEqual(self.game.player.rect.y, x + self.game.player.speed)
