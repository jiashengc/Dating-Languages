screen qut:
    imagemap:
        ground "qut-map.png"
        hover "qut-map-hover.png"

        # Locations
        hotspot (825, 65, 150, 80) clicked Jump ("kidney_location")
        hotspot (315, 311, 90, 60) clicked Jump ("hackathon_location")
        hotspot (665, 256, 110, 125) clicked Jump ("library_location")
        hotspot (980, 220, 210, 220) clicked Jump ("science_location")
        hotspot (435, 585, 225, 90) clicked Jump ("computer_location")

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
