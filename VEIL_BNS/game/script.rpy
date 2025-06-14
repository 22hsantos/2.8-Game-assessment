# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#aligns sprite to centre and sizes up

init python:
    #allows to interact with the operating system
    """
    ctypes - allows interaction with windows system fn
    sys - allows access to system-related fn e.g exiting the program
    os - allows access to file handling and directories
    """

    import subprocess, time, os, sys, ctypes

    def is_admin():

        """
        ctypes.windll - gives acces to windows system libraries
        shell32 (Shell32.dll) - system library that manages shell functions
        IsUserAnAdmin()  = built in fn inside Shell32.dll that returns True or False
        """
        print("hi")
        return ctypes.windll.shell32.IsUserAnAdmin()
    
        if not is_admin():
            """

            ShellExecuteW(...) - restarts RenPy with admin privileges
            "runas" - Tells windows ask for permission (pop up window)
            sys.executable - restarts Python instance with admin privileges
            os.path.abspath("renpy.exe") - makes sure that renpy starts from the correct location
            sys.exit() - 
            """
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.abspath("renpy.exe"), None, 1)
            sys.exit()#terminates the session

    #absolute path to game directory
    file_path = os.path.join(renpy.config.basedir, "game", "book.txt")
                    
    #check if the file exists
    file_exists = os.path.exists(file_path)

    #removes file
    if file_exists:
        os.remove(file_path)

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

    if file_exists:
        u "Book exists."
        $ os.remove(file_path)
    else:
        u "Book does not exist."
        u "yipeee"
        
    menu:
        "Return to menu":
            return
        "Write a file":

                python:
                    
                    #create and write to file
                    with open(file_path, "w") as file:
                        file.write("File created.")
                        file.close()

                    #check if the file exists
                    file_exists = os.path.exists(file_path)

                if file_exists:
                    python:
                        subprocess.Popen(['notepad.exe', file_path])
                        ctypes.windll.user32.MessageBoxW(None,
                        "Unexpected file interference! Please close interfering file before continuing.", 
                        "Oh No!",
                        48
                        )
                        os.system("taskkill /IM notepad.exe /F")
                    u "I wrote a file."
                else:
                    u "I didn't write a file."

                return

label story_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg default at bg

    scene bg black at bg
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "LEASE.mp3"

    K "(My name is Shujin Kou)"

    K "(I’m a third year high school student that has recently transferred to another school"

    K "(Why you ask?) "

    K "(Because my mom felt like it.)"

    K "(Yeah.)"

    K "(It’s whatever, I’ll just start getting ready for my first day.)"

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
