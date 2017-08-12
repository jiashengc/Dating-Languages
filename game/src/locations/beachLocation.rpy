image bg beach_background = "anime-beach.png"

label beach_location:

    scene bg beach_background

    $ currentDay = day.getDay()

    jump beach_location_day

label beach_location_day:

    "It's [currentDay] today"

    jump location_end
