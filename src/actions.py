from random import randint
from sprites.text_lines import *

class Actions:
    def __init__(self):
        self.counter = 0
        self.current_action = None
        self.rng = 0
        self.enemy = None

    def update_current(self, action):
        self.current_action = action

    def roll_rng(self):
        self.rng = randint(0,1)

    def act(self, game):
        if self.current_action == "read_note":
            self.read_note(game, NOTE_LIST)
        if self.current_action == "back" or self.current_action is None:
            self.back(game)
        if self.current_action == "throw_rock":
            self.combat(game, ROCK_1, ROCK_1A, ROCK_1B, ROCK_2A, ROCK_2B)
        if self.current_action == "punch":
            self.combat(game, PUNCH_1, PUNCH_1A, PUNCH_1B, PUNCH_2A, PUNCH_2B)

    def back(self, game):
        game.update_text(game.current_text1, "")
        game.update_text(game.decision1, "")
        game.update_text(game.decision2, "")
        game.next = False
        game.can_move = True
        game.actions = False

    def found(self, game, action_1, action_2, question, decision_1, decision_2):
        game.can_move = False
        game.decisions = True
        game.text_decisions.update_actions(action_1, action_2)
        game.update_text(game.current_text1, question)
        game.update_text(game.decision1, decision_1)
        game.update_text(game.decision2, decision_2)

    def intro(self, game, intro):
        game.update_text(game.current_text1, intro)
        game.update_text(game.decision1, "")
        game.update_text(game.decision2, "")
        self.roll_rng()

    def rng_paths(self, game, text1, text2):
        if self.rng == 0:
            game.update_text(game.current_text1, text1)
            game.score.add_to_score(50)
        else:
            game.update_text(game.current_text1, text2)
            game.score.add_to_score(20)

    def combat(self, game, intro, one_a, one_b, two_a, two_b):
        if game.next is True:
            self.counter += 1
        if self.counter == 0:
            self.intro(game, intro)
        if self.counter == 1:
            self.rng_paths(game, one_a, one_b)
        if self.counter == 2:
            self.rng_paths(game, two_a, two_b)
        if self.counter == 3:
            self.counter = 0
            game.combat = False
            game.see_enemies.empty()
            game.score.add_to_score(100)
            self.back(game)

    def read_note(self, game, notes):
        if game.next is True:
            self.counter += 1
        if self.counter == 6:
            self.counter = 0
            game.score.add_knowledge_points(1)
            game.score.add_to_score(50)
            self.back(game)
        else:
            if self.counter == 0:
                self.intro(game, notes[0])
            else:
                game.update_text(game.current_text1, notes[self.counter])
