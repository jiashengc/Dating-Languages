image bg hackathon_background = "qut-hackathon.png"

label hackathon_location:

    scene bg hackathon_background

    $ currentDay = day.getDay()

    jump hackathon_location_day

label hackathon_location_day:

    show javascript
    player "Hey JavaScript! It’s a few hours before the pitch, how’s your progress?"
    js "Going good! I was just done installing all the dependencies for the project!"
    player "That doesn’t sound too good?"
    js "Nah, with all these frameworks installed, I’ll get work done real quick!"
    player "Um, sure, do you need -"
    js "Oh look! Another new framework just came out! I’ve got to have that!"
    player "I don’t think that’s a good idea…"
    js "npm install nomongodb"
    js "npm info lifecycle send@0.32.2~install: send@0.32.2"
    js "npm info lifecycle depd@1.1.1~install: depd@1.1.1"
    js "npm info lifecycle harro@4.2.0~install: harro@4.2.0"
    js "npm info lifecycle nanisore@1.7.8~install nanisore@1.7.8"
    js "npm info lifecycle habina@1.0.0~-install habina@1.0.0"
    js "npm info lifecycle nanjiakoria@1.2.33~install nanjiakoria@.1.2.33"
    player "okay I'll just leave..."

    jump hackathon_location_end

label hackathon_location_end:

    show javascript

    "IT'S TIME FOR THE PITCHING TIME!"
    "LET'S HAVE JAVASCRIPT TO PITCH HER IDEA!"

    js "Thank you thank you! Here's my Hello World using lots of JavaScript frameworks!"

    show screen hello_world_two

label hackathon_location_end_two:

    "Clap-"
    js "Thank you thank you! I know I'm the best!"

    js "Thanks [mcName], you really are the greatest, would you like to come over my place? :)"

    jump room_location
