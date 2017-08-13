# The script of the game goes in this file.

init python:
    mcName = ""
    girlsMet = 0

    config.tts_voice = "en-us+f4"

define player = DynamicCharacter("mcName")


# Delcare images for the game
image bg town = "anime-town.jpg"
image bg hackathon = "qut-hackathon.png"
image java normal = "java normal.png"

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
        js = Character("Javascript", color="##f7df1e")
        
        day = Day()

    #Name the main character
    #jump nameMC

    jump hackathon_girls

label nameMC(girl, girl_img):
    show image girl_img

    girl "Hi! I haven't met you before, what's your name?"
    $ mcName = renpy.input("What is your name?", length=16)

    if mcName == "":
        "Please enter a name"
        call nameMC(girl, girl_img)
    $ mcName = mcName.rstrip().title()
    
    girl "Nice to meet you, [mcName]"
    hide girl_img
    return

label hackathon_girls:
    cp "Your count: [girlsMet]"

    call screen hackathon_girls

    $ _name = _return.name
        
    if girlsMet == 0:
        call nameMC(_return, "[_name].png")

    if _name == "C++":
        if girlsMet != 0:
            cp "Hey, you're [mcName], right?"
        cp "Memes :^)"
    elif _name == "JavaScript":
        pass
    elif _name == "Python":
        if girlsMet != 0:
            js "Hi! You must be [mcName], it's nice to meet you!"

        pass
    elif _name == "PHP":
        pass
    elif _name == "Java":
        show java happy
        if girlsMet != 0:
            java "Good evening. I'm Java. You must be [mcName]."
        player "Hi! I really like your glasses."
        java "Why thank you. I need them because I can't see sharp."
        player "What are you working on this weekend?"
        java "I'm going to be implementing a port of Minecraft onto Android."
        player "Oh, that soun-"
        java "And after that I'll be creating a modification that allows enterprises to flourish"
        java "by implementing a payroll and human resource managment solution to synergise our business operations"
        player "Uh, that... sounds good. Could I get your number and chat to you about it."
        java "org.character.java:21: phoneNumber has private access in JavaCharacter"
        player "I'll talk to you later."
        hide java happy
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

# label location_end:
#     $ prevDay = day.getDay()
#     $ day.addTime()

#     if (prevDay == day.getDay()):
#         call screen town
#     else:
#         jump room_location

label end:
    # This ends the game.
    "Game Over!"

    return
