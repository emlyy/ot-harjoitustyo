import pygame

class CurrentDecision:
    def __init__(self):
        self.y2 = False
        self.y3 = False

    def update(self, y):
        if y == "y2":
            self.y2 = True
        if y == "y3":
            self.y3 = True

    def update_actions(self, n, m):
        self.action1 = n
        self.action2 = m

    def __str__(self):
        if self.y2 == True:
            self.y2 = False
            return self.action1
        if self.y3 == True:
            self.y3 = False
            return self.action2
            