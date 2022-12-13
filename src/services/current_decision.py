class CurrentDecision:
    """The decisions that are currently on going.

    Attributes:
        cord_y2: A boolean that tells if user has selected the
            option above.
        cord_y3: A boolean that tells if user has selected the
            option below. Cord_y indicates the small red box's
            cordinate.
        action1: string. One of the actions that can be chosen.
        action2: string. The other action.
    """
    def __init__(self):
        self.cord_y2 = False
        self.cord_y3 = False
        self.action1 = None
        self.action2 = None

    def update(self, cord_y):
        """When called updates which option was chosen.

        Args:
            cord_y (str): Indicates which text option the red box is on.
        """
        if cord_y == "cord_y2":
            self.cord_y2 = True
        if cord_y == "cord_y3":
            self.cord_y3 = True

    def update_actions(self, action_1, action_2):
        self.action1 = action_1
        self.action2 = action_2

    def __str__(self):
        """
        Returns:
            str: A string indicating which action is chosen to be executed next.
        """
        if self.cord_y2 is True:
            self.cord_y2 = False
            return self.action1
        if self.cord_y3 is True:
            self.cord_y3 = False
            return self.action2
        return None
