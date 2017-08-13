image bg concert_background = "anime-concert.png"

label concert_location:

    scene bg concert_background

    $ currentDay = day.getDay()

    jump concert_location_day

label concert_location_day:

   "It's [currentDay] today"

   jump location_end
