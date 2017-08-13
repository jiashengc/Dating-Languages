screen hackathon_girls:
    imagemap:
        ground "qut-hackathon-girls.png"
        hover "qut-hackathon-girls-hover.png"

        # Locations
        hotspot (0, 230, 347, 490) clicked Return(c)
        hotspot (347, 230, 272, 490) clicked Return(py)
        hotspot (619, 230, 401, 490) clicked Return(js)
        hotspot (1021, 230, 249, 490) clicked Return(java)

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
