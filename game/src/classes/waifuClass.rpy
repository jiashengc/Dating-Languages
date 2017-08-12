init python:
    class Waifu:
        
        # standard instantiation, default fields
        def __init__(self, name, colour):
            
    class Waifu(ADVCharacter):
        """docstring for Waifu"""
        def __init__(self, name, textColour, birthday, favColour):
            super(Waifu, self).__init__(name, color=textColour)
            self.birthday = birthday
            self.favColour = favColour
            # Pretty self explanatory
            self.psycho = random.randint(0, 100)
            # Overall happiness 
            # 0 = depressed, 100 = ecstatic
            # 50 = fine/neutral
            self.happy = 50
            # Affection towards user
            self.affection = 0
            # Anger level towards user
            self.anger = 0
            
            self.ideal_gifts = []
            self.received_gifts= []
            

        # custom fields for instantiation
        def __init__(self, name, colour, anger, psycho, happy, affection):
            self.c = Character(name, color=colour)
            self.anger = anger
            self.psycho = psycho
            self.happy = happy
            self.affection = affection
            self.ideal_gifts = []
            self.received_gifts= []

            
        # adds affection level
        def addAffection(self, points):
            self.affection += points

        # decreases affection level 
        def subAffection(self, points):
            self.affection -= points

        # adds items to ideal gift
        def addIdealGift(self, gift):
            self.ideal_gifts.append(gift)

        # adds items to received_gifts
        def receiveGift(self, gift):
            self.received_gifts.append(gift)
            
            self.affection += 10
            
            if gift in ideal_gifts:
                self.affection += 20

        
