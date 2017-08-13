image bg cafe_background = "anime-cafe.png"

label cafe_location:

    scene bg cafe_background

    $ currentDay = day.getDay()

    jump cafe_location_day

label cafe_location_day:

    "It's [currentDay] today"

    jump location_end
