import pygame
from config import Y2, Y3
from .restart import restart

def events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
            pygame.quit()

        if game.start_screen is True:
            game.starting_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.start_screen = False
                    game.running = True
                    break
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                restart(game)

            if game.decisions is True:
                if event.key == pygame.K_DOWN:
                    game.d_box.update_rect(Y3)
                if event.key == pygame.K_UP:
                    game.d_box.update_rect(Y2)

            if event.key == pygame.K_SPACE:
                if game.decisions is True:
                    if game.d_box.rect.y == Y2:
                        game.text_decisions.update("cord_y2")
                    if game.d_box.rect.y == Y3:
                        game.text_decisions.update("cord_y3")
                    action = str(game.text_decisions)
                    game.text_actions.update_current(action)
                    game.text_actions.act(game)
                    game.decisions = False
                    game.actions = True
                else:
                    if game.actions is True:
                        game.next = True
                        game.text_actions.act(game)
                        game.next = False
