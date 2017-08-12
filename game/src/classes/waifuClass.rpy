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

        # adds items to ideal gift
        def addIdealGift(self, gift):
            self.ideal_gifts.append(gift)

        # adds items to received_gifts
        def receiveGift(self, gift):
            self.received_gifts.append(gift)
            self.affection += 10
            if gift in ideal_gifts:
                self.affection += 20

        # Asks question to user and displays possible responses
        def askQuestion(self, question):
            pass
            # TODO: add implementation



        # def answerIsCorrect(question, response):

