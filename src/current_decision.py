class CurrentDecision:
    def __init__(self):
        self.cord_y2 = False
        self.cord_y3 = False
        self.action1 = None
        self.action2 = None

    def update(self, cord_y):
        if cord_y == "cord_y2":
            self.cord_y2 = True
        if cord_y == "cord_y3":
            self.cord_y3 = True

    def update_actions(self, action_1, action_2):
        self.action1 = action_1
        self.action2 = action_2

    def __str__(self):
        if self.cord_y2 is True:
            self.cord_y2 = False
            return self.action1
        if self.cord_y3 is True:
            self.cord_y3 = False
            return self.action2
        return None
