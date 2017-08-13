image bg library_background = "qut-library.png"

label library_location:

    scene bg library_background

    $ currentDay = day.getDay()

    jump library_location_day


label library_location_day:

    show javascript normal

    player "Hey JavaScript, are you finished yet? It's an hours before pitch time!"
    js "Just finished! Take a look. What do you think?"

    call screen hello_world

label library_location_day_next:

	voice "voices/js8"
    js "Pretty cool huh?"
    player "..."

    jump location_end
