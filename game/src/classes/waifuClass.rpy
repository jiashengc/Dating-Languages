init python:
    class Waifu(ADVCharacter):
        """docstring for Waifu"""
        def __init__(self, name, textColour, birthday, favColour, favDrink, favAnimal, hobby, occupation):
            super(Waifu, self).__init__(name, color=textColour)
            self.birthday = birthday
            self.favColour = favColour
            self.favAnimal = favAnimal
            self.favDrink = favDrink
            self.hobby = hobby
            self.occupation = occupation
            self.affection = 0
            
            self.playerKnows = {
                'birthday': False,
                'favColour': False,
                'favAnimal': False,
                'favDrink': False,
                'hobby': False,
                'occupation': False
            }

        def addAffection(self, amount):
            self.affection += amount;