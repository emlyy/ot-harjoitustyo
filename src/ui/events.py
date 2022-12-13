import pygame
from config import Y2, Y3
from services.restart import restart

def events(game):
    """Checks user input events.

    Always checks if user presses quit. While running checks always
    if esc key is pressed to see if user wants to restart the game.
    When decisions is True checks if user moves the red box (d_box)
    that indicates which decision is chosen. Also checks if space
    is pressed which selects the current decision.
    When actions is True checks if space is pressed which indicates
    that the next text should be displayed.
    """    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
            pygame.quit()

        if game.running is True:

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
