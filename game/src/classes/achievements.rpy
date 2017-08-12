init python:

   # Step 1. Create the gallery object.
   g = Gallery()

   # Step 2. Add buttons and images to the gallery.

   # A button that contains an image that automatically unlocks.
   g.button(“ACHIEVEMENT_NAME”)
   g.condition(“persistent.ACHIEVEMENT_NAME”)
   
   g.button(“ACHIEVEMENT_NAME”)
   g.condition(“persistent.ACHIEVEMENT_NAME”)

screen achievements:

   # Ensure this replaces the main menu.
   tag menu

   # The background.
   add “BACKGROUND”

   # A grid of buttons.
   grid 3 1:

       xfill True
       yfill True

       # Call make_button to show a particular button.
       add g.make_button(“ACHIEVEMENT_NAME”, “ACHIEVEMENT_NAME”, xalign=0.5, yalign=0.5)
       add g.make_button(“ACHIEVEMENT_NAME”, “ACHIEVEMENT_NAME”, xalign=0.5, yalign=0.5)
       textbutton “Return” action Return() xalign 0.5 yalign 0.5