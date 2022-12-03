from sprites.note import Note
from sprites.enemy import Enemy
from sprites.barrier import Barrier
from config import NOTE_X, NOTE_Y, NOTE_IMAGE, BARRIERS_LIST, ENEMY_1_X, ENEMY_1_Y, ENEMY_IMAGE

def first_room(game):
    game.note = Note(game, NOTE_X, NOTE_Y, NOTE_IMAGE)
    game.enemy = Enemy(game, ENEMY_1_X, ENEMY_1_Y, ENEMY_IMAGE)
    game.all_sprites.add(game.note)
    game.enemies.add(game.enemy)

    for i in BARRIERS_LIST:
        game.barriers.add(Barrier(i[0],i[1],i[2],i[3]))