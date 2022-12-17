from random import randint
from text_lines import (PUNCH_1, PUNCH_1A, PUNCH_1B,
PUNCH_2A, PUNCH_2B, ROCK_1, ROCK_1A, ROCK_1B, ROCK_2A, ROCK_2B,
EAT_LIST, LEAVE_IT, NOTE_LIST, WHICH_ITEM, NO_WEAPON, WEAPON_1,
WEAPON_2, TALK_L, SWORD, WATER, NO_ITEM, WATER_LIST, WATER_NO,
RANS_MEMORY_BOOK_2)

class Actions:
    """Current action that's taking place.

    Updates the three texts that can be seen during different actions
    such as during combat, reading a sign etc.

    Attributes:
        counter: An integer count of which text comes next. Grows every time
        user presses space.
        current_action: str of the action that is currently going.
        rng: An integer, either 1 or 0, indicating what we roll
            as our deciding path.
        teleport: A boolean indicating if player should be moved
            after no item action
    """
    def __init__(self):
        self.counter = 0
        self.current_action = None
        self.rng = 0
        self.teleport = False

    def update_current(self, action):
        self.current_action = action

    def roll_rng(self):
        self.rng = randint(0,1)

    def act(self, game):
        """Checks which room is running and divides action calls accordingly.
        """
        if self.current_action == "back" or self.current_action is None:
            self.back(game)
        elif game.room == 1:
            self.first_room_actions(game)
        elif game.room == 2:
            self.second_room_actions(game)
        elif game.room == 3:
            self.third_room_actions(game)

    def first_room_actions(self, game):
        """first room actions

        """
        if self.current_action == "read_note":
            self.lines(game, NOTE_LIST)
        if self.current_action == "throw_rock":
            self.combat(game, ROCK_1, ROCK_1A, ROCK_1B, ROCK_2A, ROCK_2B)
        if self.current_action == "punch":
            self.combat(game, PUNCH_1, PUNCH_1A, PUNCH_1B, PUNCH_2A, PUNCH_2B)
        if self.current_action == "water":
            game.water = True
            self.lines(game, WATER_LIST)
        if self.current_action == "no water":
            self.lines(game, WATER_NO)

    def second_room_actions(self, game):
        """second room actions for items

        """
        if self.current_action == "eat":
            self.lines(game, EAT_LIST)
            game.items.remove(game.cheese)
        if self.current_action == "don't eat":
            self.lines(game, LEAVE_IT)
        if self.current_action == "yes sword":
            game.weapon = True
            game.score.add_to_score(25)
            self.back(game)
        if self.current_action == "memory book":
            self.lines(game, RANS_MEMORY_BOOK_2)

    def third_room_actions(self,game):
        """calls for actions when room 3 is running.

        If the user has picked up an item it will change the options they
        see on screen.
        """
        if self.current_action == "item":
            if game.water is True:
                if game.weapon is True:
                    self.found(game, "water bucket", "sword", WHICH_ITEM, WEAPON_2, WEAPON_1)
                else:
                    self.found(game,"water bucket", "no item", WHICH_ITEM, WEAPON_2, NO_WEAPON)
            else:
                if game.weapon is True:
                    self.found(game, "no item", "sword", WHICH_ITEM, NO_WEAPON, WEAPON_1)
                else:
                    self.update_current("no item")
                    self.lines(game, NO_ITEM)
        if self.current_action == "talk":
            self.lines(game, TALK_L)
        if self.current_action == "sword":
            self.boss_fight(game,SWORD)
        if self.current_action == "water bucket":
            self.boss_fight(game, WATER)
        if self.current_action == "no item":
            self.lines(game, NO_ITEM)
            self.teleport = True

    def back(self, game):
        """Lets user continue playing.

        Transitions from current action to overworld play.
        """
        game.update_text(game.current_text1, "")
        game.update_text(game.decision1, "")
        game.update_text(game.decision2, "")
        game.next = False
        game.can_move = True
        game.actions = False
        if self.teleport is True:
            self.teleport = False
            game.player.rect.x = 600
            game.player.rect.y = 150

    def found(self, game, action_1, action_2, question, decision_1, decision_2):
        """Decision making action.

        Updates the texts that user will see during decision making. Puts forth
        the decisions event.

        Args:
            action_1 (str): One of the two str that are for option for current decision.
            action_2 (str): The other option.
            question (str): Intro for what player has stumbled upon.
            decision_1 (str): Option one for user.
            decision_2 (str): Option two for user.
        """
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
        """Normal combat action.

        Args:
            intro (str): Introduction text.
            one_a (str): First text if rng has rolled 0.
            one_b (str): First text if rng has rolled 1.
            two_a (str): Second text if rng has rolled 0.
            two_b (str): Second text if rng has rolled 1.
            Only one text at a time. Changes when space is pressed.
        """
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
            game.see_enemies.empty()
            game.score.add_to_score(100)
            self.back(game)

    def lines(self, game, lines):
        """Performs actions that don't depend on rng.

        Args:
            lines (list): A list of the texts in order to be shown on screen.
        """
        if game.next is True:
            self.counter += 1
        if self.counter == len(lines):
            self.counter = 0
            if self.current_action != "no water":
                game.score.add_knowledge_points(1)
                game.score.add_to_score(50)
                game.see_enemies.empty()
            self.back(game)
        else:
            if self.counter == 0:
                self.intro(game, lines[0])
            else:
                game.update_text(game.current_text1, lines[self.counter])

    def boss_fight(self, game, lines):
        """Special combat in room 3.

        Args:
            lines (list): A list of the possible strings.
        """
        if game.next is True:
            self.counter += 1
        if self.counter == 0:
            self.intro(game,"")
            self.rng_paths(game, lines[0], lines[2])
        if self.counter == 1:
            self.rng_paths(game, lines[1], lines[3])
        if self.counter == 2:
            game.update_text(game.current_text1, lines[4])
        if self.counter == 3:
            self.counter = 0
            game.see_enemies.empty()
            game.score.add_to_score(100)
            game.score.add_knowledge_points(1)
            self.back(game)
