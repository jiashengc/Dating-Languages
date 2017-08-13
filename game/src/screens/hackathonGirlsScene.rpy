screen hackathon_girls:
    imagemap:
        ground "small-lake-town.png"
        hover "small-lake-town-selected.png"

        # Locations
        hotspot (195, 206, 110, 75) clicked Return(cp)

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
