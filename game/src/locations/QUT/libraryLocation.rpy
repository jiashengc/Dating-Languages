image bg library_background = "qut-library.png"

label library_location:

    scene bg library_background

    $ currentDay = day.getDay()

    jump library_location_day


label library_location_day:

    show javascript

    player "Hey JavaScript, are you finished yet? It's an hours before pitch time!"
    js "Just finished! Take a look. What do you think?"

    jump library_location_day_next

label library_location_day_next:

    js "Pretty cool huh?"
    player "..."

    jump location_end
