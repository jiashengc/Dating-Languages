image bg kidney_background = "qut-kidney.png"

label kidney_location:

    scene bg kidney_background

    $ currentDay = day.getDay()

    jump kidney_location_day

label kidney_location_day:

    "It's [currentDay] today"

    jump location_end
