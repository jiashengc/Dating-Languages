image bg park_background = "anime-park.png"

label park_location:

    scene bg park_background

    $ currentDay = day.getDay()

    jump park_location_day


label park_location_day:

    "It's [currentDay] today"

    jump location_end
