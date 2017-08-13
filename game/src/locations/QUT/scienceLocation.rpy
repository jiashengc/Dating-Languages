image bg science_background = "qut-cube.png"

label science_location:

    scene bg science_background

    $ currentDay = day.getDay()

    jump science_location_day

label science_location_day:

    "It's [currentDay] today"

    jump location_end
