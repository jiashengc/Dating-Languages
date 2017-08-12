image bg centre_background = "anime-town-centre.png"

label centre_location:

    scene bg centre_background

    $ currentDay = day.getDay()

    jump centre_location_day

label centre_location_day:

    "It's [currentDay] today"

    jump location_end
