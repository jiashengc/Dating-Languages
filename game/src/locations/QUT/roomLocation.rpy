image bg room_background = "anime-room.png"

image js sexy = Image("javascript-naked.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)

label room_location:

    scene bg room_background

    show javascript

    js "Thanks for everything till now..."
    js "I've got something special for you"
    js "I'll show you my secret source code"

    hide javascript
    show js sexy

    js ";)"

    "THE END"

    return
