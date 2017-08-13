image bg kidney_background = "qut-kidney.png"

label kidney_location:

    scene bg kidney_background

    $ currentDay = day.getDay()

    jump kidney_location_day

label kidney_location_day:

    show javascript
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
    js "npm info using npm@1.4.0"
    js "npm info using node@v3.1.2"
    js "npm verb npm-session fd2646ea470e5443"
    js "npm http fetch GET 200 http://registry.npmjs.org/express 457ms"
    hide javascript

    jump library_location_day
