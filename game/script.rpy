# The script of the game goes in this file.
image bg hackathon_start_background = "qut-hackathon.png"

init python:
    mcName = ""
    girlsMet = 0

    config.tts_voice = "en-us+f4"

define player = DynamicCharacter("mcName")


# Delcare images for the game
image bg town = "anime-town.jpg"
image bg hackathon = "qut-hackathon.png"
image java normal = Image("java normal.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)
image c normal = Image("C.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)
image javascript normal = Image("JavaScript.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)
image python normal = Image("Python.png", xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=1.0)


# The game starts here.

label start:

    # Initialize variables
    python:
        #cp = Waifu("C++", "#004481", "20 March, 1970", "Blue", "Coke", "Gnu", "Memes", "Princess")
        #js = Waifu("JavaScript", "#f7df1e", "7 December, 1990", "White", "Coke", "Gnu", "Memes", "Princess")
        #py = Waifu("Python", "#35709f", "20 February 1991", "Yellow")
        #ph = Waifu("PHP", "#7486bd", "8 June 1995", "Green")
        #jv = Waifu("java", "#e52c2a", "23 May 1995", "Red")
        cp = Character("C++", color="#004481")
        java = Character("Java", color="#e52c2a")
        js = Character("JavaScript", color="#f7df1e")
        py = Character("Python", color="#35709f")
        c = Character("C", color="#004481")
        day = Day()

    #Name the main character
    #jump nameMC

    jump hackathon_girls

label nameMC(girl, girl_img):
    show image girl_img

    scene bg hackathon_start_background

    girl "Hi! I haven't met you before, what's your name?"
    $ mcName = renpy.input("What is your name?", length=16)

    if mcName == "":
        "Please enter a name"
        call nameMC(girl, girl_img)
    $ mcName = mcName.rstrip().title()
    
    hide girl_img
    return

label hackathon_girls:
    call screen hackathon_girls

    $ _name = _return.name

    scene bg hackathon_start_background

    if girlsMet == 0:
        call nameMC(_return, "[_name].png")

    if _name == "C":
        if girlsMet != 0:
            player "Hi, I’m [mcName]. What’s your name?"
        c "Hello, peasant. My name is C%s.U#(v|f`Lu.0U\6T."
        c "Excuse me. I meant my name is C."
        player "Okay. What do you want to work on for the hackathon?"
        c "I think I’ll be making a new operating system."
        player "Ambitious."
        "I accidentally dropped my iPhone."
        player "Oh, sorry. Could you pick that up for me?"
        c "I don’t do garbage collection."

    elif _name == "JavaScript":
        if girlsMet != 0:
            player "Hi, I’m [mcName]. What’s your name?"
        js "Hey I’m JavaScript! Nice to meet you!"
        player "Are you related to Java by any chance?"
        js "Are pineapples related to apples?"
        player "Oh, okay. So what do you plan to build in this hackathon?"
        js "Yea, so let me pitch to you."
        js "Did you know that broccoli prices affects us at a global scale?"
        js "Every year people buy broccoli at high prices wasting nearly 1 million dollars a year."
        js "So how about we build a platform using Angular, Vue, Mongo, Node, Socket.io, React, Express, Ember, Meteor, jQuery, d3, lodash, Underscore, Backbone, Knockout to track the prices of broccoli."
        player "Sounds like you’ve got everything planned."
        js "Yea! I’ll also be making my own framework during the hack, I promise it’ll be great!"
        player "Yea, sure. I’ll be looking forward to it then."

    elif _name == "Python":
        if girlsMet != 0:
            player "Hi, I’m [mcName]. What’s your name?"
        py "Hey! I’m Python3. You can just call me Python."
        player "3? Do you have a couple older siblings or something?"
        py "Yeah nobody cares about them. I'm the favourite child."
        player "Wow. Well, what kind of stuff do you like to work on in your free time?"
        py "I like doing maths! I enjoy machine learning as well. Not at the same time though. I can’t multitask."
        player "Seems interesting. Are you planning on doing that for the hackathon?"
        py "Actually, I want to make a dating sim… where the characters are programmers."
        player "Sounds like fun! Good luck!"


        pass
    # elif _name == "PHP":
    #     pass
    elif _name == "Java":
        show java    
        if girlsMet != 0:
            player "Hi, I'm [mcName]. What's your name?"
        voice "voices/java1.ogg"    
        java "Good evening. I'm Java."
        player "I really like your glasses."
        voice "voices/java2.ogg"
        java "Why thank you. I need them because I can't see sharp."
        player "What are you working on this weekend?"
        voice "voices/java3.ogg"
        java "I'm going to be implementing a port of Minecraft onto Android."
        player "Oh, that sounds-"
        voice "voices/java4.ogg"
        java "And after that I'll be creating a modification that allows enterprises to flourish."
        voice "voices/java5.ogg"
        java "by implementing a payroll and human resource managment solution to synergise our business operations."
        player "Uh, that... sounds good. Could I get your number and chat to you about it."
        voice "voices/java6.ogg"
        java "org.character.java:21: phoneNumber has private access in JavaCharacter"
        player "I'll talk to you later."
        hide java 
    else:
        "Something has went wrong, you shouldn't see this"
        jump hackathon_girls

    $ girlsMet += 1

    if girlsMet != 5:
        jump hackathon_girls
    else:
        "Now you've met everyone."
        jump next_time


label next_time:
    $ day.addTime()
    call screen qut

label next_day:
    jump hackathon_location


# label choice:

#     scene bg town
#     show eileen happy

#     "It's time to pick your favourite language!"

#     cp "Pick me you bitc! Affection: [cp.affection]"


#     js "I'm JavaScript ahjaajahajha! Affection: [js.affection]"

#     call test("Hello")

#     menu:
#         "Choose C++":
#             $ cp.addAffection(1)
#             $ js.addAffection(-1)
#             jump choose_CP

#         "Choose JavaScript":
#             $ cp.addAffection(-1)
#             $ js.addAffection(1)
#             jump choose_JS

#         "Choose to stop choosing":
#             jump end


# label test(words):
#     cp "[words]"


# label next_day:
#     call screen town

# label choose_CP:

#     $ dayName = day.getDay()
#     $ timeName = day.getTime()
#     cp "Woohoo you choose me!"

#     if cp.playerKnows["birthday"]:
#         menu:
#             cp "Do you remember when my birthday is?"
#             "Yes":
#                 jump cp_correct_birthday
#             "No":
#                 jump cp_wrong_birthday
#             "No":
#                 jump cp_wrong_birthday
#             "No":
#                 jump cp_wrong_birthday
#     else:
#         cp "My birthday is [cp.birthday]"
#         $ cp.playerKnows["birthday"] = True

#     js "Gue gue gue gue it's [dayName] and it's [timeName]"

#     jump next_day

# label choose_JS:
#     $ dayName = day.getDay()
#     $ timeName = day.getTime()
#     js "Wooo it's [dayName] and it's [timeName]"

#     cp "Okay"

#     jump next_day

# label cp_correct_birthday:
#     cp "Yes, that is correct"
#     jump next_day

# label cp_wrong_birthday:
#     cp "No, Baka! >:("
#     jump next_day

label location_end:
    $ prevDay = day.getDay()
    $ day.addTime()

    if (prevDay == day.getDay()):
        call screen qut
    else:
        jump room_location

label end:
    # This ends the game.
    "Game Over!"

    return
