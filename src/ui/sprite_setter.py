import pygame
from sprites.ran import Ran
from sprites.background import Background
from sprites.barrier import Barrier
from sprites.texts import TextBox
from sprites.note import Note
from config import SPAWN_X, SPAWN_Y, RAN_IMAGE, BG_IMAGE, NOTE_X, NOTE_Y, NOTE_IMAGE, D_BOX, D_BOX_X, Y2, SCREEN_WIDTH, BOX_HEIGHT, BARRIERS_LIST

def sprites(game):
    game.player = Ran(game, SPAWN_X,SPAWN_Y, RAN_IMAGE)
    game.background = Background(0,0,BG_IMAGE)
    game.note = Note(game, NOTE_X, NOTE_Y, NOTE_IMAGE)
    game.d_box = TextBox(game, (255,0,0), D_BOX, D_BOX, D_BOX_X, Y2)
    game.box.add(game.d_box)
    game.all_sprites.add(game.background)
    game.all_sprites.add(TextBox(game, (0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636))
    game.all_sprites.add(TextBox(game, (0,0,0), SCREEN_WIDTH, BOX_HEIGHT, 0, 636))
    game.all_sprites.add(game.note)
    game.all_sprites.add(game.player)

    for i in BARRIERS_LIST:
        game.barriers.add(Barrier(i[0],i[1],i[2],i[3]))