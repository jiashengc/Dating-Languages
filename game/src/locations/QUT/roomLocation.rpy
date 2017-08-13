image bg room_background = "anime-room.png"

image js vhappy = Image("javascript-vhappy.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)
image js sexy = Image("javascript-naked.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)

label room_location:

    scene bg room_background

    show js vhappy

    js "Thanks for everything till now..."
    js "I've got something special for you"
    js "I'll show you my secret source code"

    show js sexy

    js ";)"

    "THE END"

    return
