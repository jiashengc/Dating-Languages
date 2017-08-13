image bg kidney_background = "qut-kidney.png"

label kidney_location:

    scene bg kidney_background

    $ currentDay = day.getDay()

    jump kidney_location_day

label kidney_location_day:

    show js
    player "Hey, JavaScript! I really liked your idea. Do you want to work together on it?"
    js "Yea! If you can come up with a name for our framework that’ll be great!"
    player "How about Broccoli.js?"
    js "Nah, Broccoli.js already exists."
    player "Salad.js? Tree.js?"
    js "I think GreenCauliflower.js will work."
    player "Great let’s publish it!"
    js "Okay. But wait, i need to install my dependencies"
    player "Sure thing. How long will it take?"
    js "not too long!"

    jump location_end
