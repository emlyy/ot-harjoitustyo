from sprites.text_lines import *

class Actions:
    def __init__(self):
        self.counter = 0
        self.current_action = None

    def update_current(self, action):
        self.current_action = action

    def act(self, game):
        if self.current_action == "read_note":
            self.read_note(game)
        if self.current_action == "back":
            self.back(game)

    def back(self, game):
        game.update_text(game.current_text1, "")
        game.update_text(game.decision1, "")
        game.update_text(game.decision2, "")
        game.next = False
        game.can_move = True
        game.actions = False

    def read_note(self, game):
        if game.next is True:
            self.counter += 1
        if self.counter == 0:
            game.update_text(game.current_text1, NOTE_1)
            game.update_text(game.decision1, "")
            game.update_text(game.decision2, "")
        if self.counter == 1:
            game.update_text(game.current_text1, NOTE_2)
        if self.counter == 2:
            game.update_text(game.current_text1, DOTS)
        if self.counter == 3:
            game.update_text(game.current_text1, NOTE_3)
        if self.counter == 4:
            game.update_text(game.current_text1, NOTE_4)
        if self.counter == 5:
            game.update_text(game.current_text1, NOTE_END)
        if self.counter == 6:
            self.counter = 0
            self.back(game)
    