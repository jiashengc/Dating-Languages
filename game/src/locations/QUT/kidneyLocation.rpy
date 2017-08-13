image bg kidney_background = "qut-kidney.png"

label kidney_location:

    scene bg kidney_background

    $ currentDay = day.getDay()

    jump kidney_location_day

label kidney_location_day:

    show javascript
    player "Hey, JavaScript! I really liked your idea. Do you want to work together on it?"
    voice "voices/kidney-01.ogg"
    js "Yea! If you can come up with a name for our framework that’ll be great!"
    player "How about Broccoli.js?"
    voice "voices/kidney-02.ogg"
    js "Nah, Broccoli.js already exists."
    player "Salad.js? Tree.js?"
    voice "voices/kidney-03.ogg"
    js "I think GreenCauliflower.js will work."
    player "Great let’s publish it!"
    voice "voices/kidney-04.ogg"
    js "Okay. But wait, I need to install my dependencies."
    player "Sure thing. How long will it take?"
    voice "voices/kidney-05.ogg"
    js "Not too long!"
    js "npm info using npm@1.4.0"
    js "npm info using node@v3.1.2"
    js "npm verb npm-session fd2646ea470e5443"
    js "npm http fetch GET 200 http://registry.npmjs.org/express 457ms"
    hide javascript

    jump library_location
