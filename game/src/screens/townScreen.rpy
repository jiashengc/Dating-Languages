screen town:
    imagemap:
        ground "small-lake-town.png"
        hover "small-lake-town-selected.png"

        # Locations
        hotspot (195, 206, 110, 75) clicked Jump ("park_location")
        hotspot (457, 443, 110, 75) clicked Jump ("cafe_location")
        hotspot (1010, 415, 110, 75) clicked Jump ("library_location")
        hotspot (895, 448, 110, 75) clicked Jump ("concert_location")

    fixed:
        $ currentDay = day.getDay()
        text "[currentDay]" xalign 0.95 yalign 0.05

    frame:
        xpadding 10
        ypadding 10
        xalign 0.95
        yalign 0.05

        vbox:
            $ currentDay = day.getDay()
            $ currentTime = day.getTime()
            text "[currentDay]"
            text "[currentTime]"