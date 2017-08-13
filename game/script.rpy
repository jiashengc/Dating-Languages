# The script of the game goes in this file.

init python:
    mcName = ""
    girlsMet = 0

define player = DynamicCharacter("mcName")


# Delcare images for the game
image bg town = "anime-town.jpg"

# The game starts here.

label start:

    # Initialize variables
    python:
        cp = Waifu("C++", "#004481", "20 March, 1970", "Blue", "Coke", "Gnu", "Memes", "Princess")
        #js = Waifu("JavaScript", "#f7df1e", "7 December, 1990", "White", "Coke", "Gnu", "Memes", "Princess")
        #py = Waifu("Python", "#35709f", "20 February 1991", "Yellow")
        #ph = Waifu("PHP", "#7486bd", "8 June 1995", "Green")
        #jv = Waifu("java", "#e52c2a", "23 May 1995", "Red")
        day = Day()

    #Name the main character
    #jump nameMC

    jump hackathon_girls

label nameMC(girl, girl_img):
    show image girl_img

    girl "Hi! I haven't met you before, what's your name?"
    $ mcName = renpy.input("What is your name?", length=16)

    if mcName == "":
        "Please enter a name"
        jump nameMC
    $ mcName = mcName.rstrip().title()

    girl "Nice to meet you, [mcName]"
    hide girl_img
    return

label hackathon_girls:
    cp "Your count: [girlsMet]"

    call screen hackathon_girls

    $ _name = _return.name

    if girlsMet == 0:
        call nameMC(_return, "[_name].png")

    if _name == "C++":
        if girlsMet != 0:
            cp "Hey, you're [mcName], right?"
        cp "Memes :^)"
    elif _name == "JavaScript":
        pass
    elif _name == "Python":
        pass
    elif _name == "PHP":
        pass
    elif _name == "Java":
        pass
    else:
        "Something has went wrong"
        jump hackathon_girls

    $ girlsMet += 1

    if girlsMet != 5:
        jump hackathon_girls
    else:
        "Now you've met everyone."
        jump next_time


label next_time:
    $ day.addTime()
    call screen qut


label next_day:
    jump hackathon_location


label location_end:
    $ prevDay = day.getDay()
    $ day.addTime()

    if (prevDay == day.getDay()):
        call screen qut
    else:
        jump room_location

label end:
    # This ends the game.
    "Game Over!"

    return
