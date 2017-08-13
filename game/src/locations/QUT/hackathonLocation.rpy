image bg hackathon_background = "qut-hackathon.png"

label hackathon_location:

    scene bg hackathon_background

    $ currentDay = day.getDay()

    jump hackathon_location_day

label hackathon_location_day:

    "Hey welcome"

    call screen qut
