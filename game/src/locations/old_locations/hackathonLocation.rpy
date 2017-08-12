image bg hackathon_background = "anime-hackathon.png"

label hackathon_location:

    scene bg hackathon_background

    $ currentDay = day.getDay()

    jump hackathon_location_day

label hackathon_location_day:

    "Hey welcome"
