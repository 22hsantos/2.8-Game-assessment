# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#aligns sprite to centre and sizes up

init python:
    #allows to interact with the operating system
    import os
    #gets the player's name
    player_name = os.getlogin()

#aligns and resizes sprites
transform scale_sprite:
    zoom 2
    xalign 0.5
    yalign 1.0

#aligns bg to centre and sizes up
transform bg:
    zoom 3.0
    xalign 0.5
    yalign 0.5


define Ke = Character("Kei")
define K = Character("Kou")
define u = Character("[player_name]")

image kei default = "kei_default.png"
image bg default = "bg_default.jpg"

default book = False

# The game starts here.

label start:

    menu:
        "troubleshoot file creation":
            jump file_write
        "Play the story":
            jump story_start

# shortcut to troubleshoot errors without going through dialogue
label file_write:
    u "Hello."
    menu:
        "Return to menu":
            return
        "Write a file":

                python:

                    #absolute path to game directory
                    file_path = os.path.join(renpy.config.basedir, "game")
                    
                    #create and write to file
                    with open(file_path, "w") as file:
                        file.write("File created.")
                    
                    #check if the file exists
                    if os.path.exists(file_path):
                        print("File exists!!!")
                    else:
                        print("oh no")


label story_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg default at bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    K "My name is Shujin Kou."

    K "You will be playing the MVP of VEIL: BENEATH THE SURFACE."

    K "(I find a book on the ground)"

    K "(Should I…)"

    menu:
        "Pick it up":
            jump good_ending
        "Leave it alone":
            jump bad_ending

label good_ending:
    $ book = True
    show kei default at scale_sprite
    Ke "Hello!"
    if book:
        Ke "Oh! You've found my cookbook!" 
        Ke  "Thank you so much, [player_name]"
        u "Anytime."

    hide kei
    K "We lived happily ever after."
    # This ends the game.

    return

label bad_ending:
    K "I leave the book on the ground"
    K "I am alone for the rest of my life"
    return
