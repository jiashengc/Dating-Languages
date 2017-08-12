init python:
    class Waifu(ADVCharacter):
        """docstring for Waifu"""
        def __init__(self, name, textColour, birthday, favColour):
            super(Waifu, self).__init__(name, color=textColour)
            self.birthday = birthday
            self.favColour = favColour
            self.affection = 0

        def addAffection(self, amount):
            self.affection += amount;