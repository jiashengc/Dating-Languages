# The script of the game goes in this file.

init python:
    pass

# Delcare images for the game
image bg town = "anime-town.jpg"

# The game starts here.

label start:

    # Initialize variables
    python:
        py = Waifu("Python", "#35709f", "20 February 1991", "Yellow")
        ph = Waifu("PHP", "#7486bd", "8 June 1995", "Green")
        cp = Waifu("C", "#004481", "20 March, 1970", "Blue")
        js = Waifu("JavaScript", "#f7df1e", "7 December, 1990", "White")
        jv = Waifu("java", "#e52c2a", "23 May 1995", "Red")
        day = Day()

    scene bg town
    show eileen happy

    jump choice

label choice:

    scene bg town
    show eileen happy

    "It's time to pick your favourite language!"

    cp "Pick me you bitc! Affection: [cp.affection]"

    js "I'm JavaScript ahjaajahajha! Affection: [js.affection]"

    menu:
        "Choose C++":
            $ cp.addAffection(1)
            $ js.addAffection(-1)
            jump choose_CP

        "Choose JavaScript":
            $ cp.addAffection(-1)
            $ js.addAffection(1)
            jump choose_JS

        "Choose to stop choosing":
            jump end

label next_day:
    $ day.addTime()

    call screen town

    jump choice

label choose_CP:

    $ dayName = day.getDay()
    $ timeName = day.getTime()
    cp "Woohoo you choose me!"

    js "Gue gue gue gue it's [dayName] and it's [timeName]"

    jump next_day

label choose_JS:
    $ dayName = day.getDay()
    $ timeName = day.getTime()
    js "Wooo it's [dayName] and it's [timeName]"

    cp "Okay"

    jump next_day

label end:
    # This ends the game.
    "Game Over!"

    return
