image bg computer_background = "qut-s-block.png"

label computer_location:

    scene bg computer_background

    $ currentDay = day.getDay()

    jump computer_location_day

label computer_location_day:

    "It's [currentDay] today"

    jump location_end
