# The script of the game goes in this file.

init python:
    pass

# Delcare images for the game
image bg town = "anime-town.jpg"

# The game starts here.

label start:

    # Initialize variables
    python:
        cp = Waifu("C++", "#004481")
        js = Waifu("JavaScript", "#f7df1e")
        day = Day()

    scene bg town
    show eileen happy

    jump choice

label choice:

    scene bg town
    show eileen happy

    "It's time to pick your favourite language!"

    cp.c "Pick me you bitc! Affection: [cp.affection]"

    js.c "I'm JavaScript ahjaajahajha! Affection: [js.affection]"

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
    call screen town

    $ day.addTime()

    jump choice

label choose_CP:

    $ dayName = day.getDay()
    $ timeName = day.getTime()
    cp.c "Woohoo you choose me!"

    js.c "Gue gue gue gue it's [dayName] and it's [timeName]"

    jump next_day

label choose_JS:
    $ dayName = day.getDay()
    $ timeName = day.getTime()
    js.c "Wooo it's [dayName] and it's [timeName]"

    cp.c "Okay"

    jump next_day

label end:
    # This ends the game.
    "Game Over!"

    return
