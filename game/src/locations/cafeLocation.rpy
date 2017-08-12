image bg cafe_background = "anime-cafe.png"

label cafe_location:

    scene bg park

    $ currentDay = day.getDay()

    if day.currentDay == 1:
        jump park_locatio

    call screen town
