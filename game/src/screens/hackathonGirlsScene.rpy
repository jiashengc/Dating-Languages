screen hackathon_girls:
    imagemap:
        ground "qut-hackathon.png"
        hover "qut-hackathon-girls.png"

        # Locations
        hotspot (0, 230, 360, 500) clicked Return(c)
        hotspot (360, 230, 300, 500) clicked Return(java)

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
