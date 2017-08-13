screen hackathon_girls:
    imagemap:
        ground "qut-hackathon.png"
        hover "qut-hackathon-girls.png"

        # Locations
        hotspot (0, 328, 250, 500) clicked Return(c)
        hotspot (250, 330, 250, 500) clicked Return(java)

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
