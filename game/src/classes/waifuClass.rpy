init python:
    class Waifu:
        def __init__(self, name, colour):
            self.c = Character(name, color=colour)
            self.anger = 0
            self.psycho = 0
            # "Depressed"  happy =0
            # "Fine" happy=50
            # "Ecstatic" happy=100
            self.happy = 0
            self.affection = 0

        def __init__(self, name, colour, anger, psycho, happy, affection):
            
        def addAffection(self, points):
            self.affection += points
