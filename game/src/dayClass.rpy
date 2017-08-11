init python:
    class Day:
        def __init__(self):
            self.days = [
                'Monday',   #0
                'Tuesday',  #1
                'Wednesday',#2
                'Thursday', #3
                'Friday',   #4
                'Saturday', #5
                'Sunday'    #6
                ]
            self.time = [
                'Morning',  #0
                'Afternoon',#1
                'Evening'   #2
                ]
            self.currentDay = 0
            self.currentTime = 0

        def getDay(self):
            return self.days[self.currentDay]

        def addDay(self):
            if (self.currentDay == 6):
                self.currentDay = 0
            else:
                self.currentDay += 1

        def getTime(self):
            return self.time[self.currentTime]

        def addTime(self):
            if (self.currentTime == 2):
                self.currentTime = 0
                self.addDay()
            else:
                self.currentTime += 1
