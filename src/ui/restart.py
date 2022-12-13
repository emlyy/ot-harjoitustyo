from ui.sprite_setter import SpriteSet

def restart(game):
    """Resets the game.
    """
    SpriteSet().clear_all_groups(game)
    SpriteSet().groups_setter(game)

    game.can_move = True
    game.decisions = False
    game.next = False
    game.actions = False
    game.water = False
    game.weapon = False
    game.room = 1

    game.update_text(game.current_text1, "")
    game.update_text(game.decision1, "")
    game.update_text(game.decision2, "")
    game.text_actions.counter = 0

    game.score.reset_scores()
    game.door.update_where("second")

    SpriteSet().first_room(game)
