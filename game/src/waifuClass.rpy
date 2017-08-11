init python:
    class Waifu:
        def __init__(self, name, colour):
            self.c = Character(name, color=colour)
            self.affection = 0

        def addAffection(self, points):
            self.affection += points
