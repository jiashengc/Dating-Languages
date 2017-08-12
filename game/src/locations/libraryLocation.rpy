image bg library_background = "anime-library.png"

label library_location:

    scene bg library_background

    $ currentDay = day.getDay()

    jump library_location_day


label library_location_day:

    "It's [currentDay] today"

    jump location_end
