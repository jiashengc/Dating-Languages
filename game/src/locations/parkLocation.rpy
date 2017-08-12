image bg park_background = "anime-park.png"

label park_location:

    scene bg park_background

    $ currentDay = day.getDay()

    if day.currentDay == 1:
        jump park_location_tuesday
    elif day.currentDay == 2:
        jump park_location_wednesday
    elif day.currentDay == 3:
        jump park_location_thursday
    elif day.currentDay == 4:
        jump park_location_friday


label park_location_tuesday:

    "Woah it's [currentDay]"

    jump choice

label park_location_wednesday:

    "Wow it's [currentDay]"

    jump choice

label park_location_thursday:

    "Shit it's [currentDay]"

    jump choice

label park_location_friday:

    "TGIP it's [currentDay]"

    jump choice
