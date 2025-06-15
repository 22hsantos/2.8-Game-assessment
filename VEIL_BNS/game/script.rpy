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
    file_path = os.path.join(renpy.config.basedir, "game", "2025.txt")
                    
    #check if the file exists
    file_exists = os.path.exists(file_path)

    #removes file
    if file_exists:
        os.remove(file_path)

    #gets the player's name
    player_name = os.getlogin()

    #dialogue sound effects



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

#Sound effects

#Character Sprites
image kei default = "images/Kei/kei_default.png"

#Backgrounds
image bg hood = "images/backgrounds/bg_neighbourhood.jpeg"
image bg black = "images/backgrounds/bg_black.jpg"


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
                        os.system(f'notepad.exe {file_path}')
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



    scene bg black at bg
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    # MONDAY MORNING
    K "(My name is Shujin Kou)"
    K "(I’m a third year high school student that has recently transferred to another school"
    K "(Why you ask?) "
    K "(Because my mom felt like it.)"
    K "(Yeah.)"
    K "(It’s whatever, I’ll just start getting ready for my first day.)"

    play music "LEASE.mp3"
    scene bg hood
    
    K "I’ve only moved here a few days ago… "
    K "But I have to admit this neighbourhood is way better than my last one."
    K "the amount of sleep I’ve lost because of those damn barking dogs was enough to drive me insane."

    play sound "stepping.mp3"

    K "(...)"

    stop sound
    scene bg black at bg
    stop music

    K "Wait…"
    K "(Did I forget my house keys??)"

    play music "spirited.mp3"

    K "(I frantically start searching through my uniform pockets, trying to find my keys.) "
    K "Argh, not in the right one… "
    K "(my expression tenses up as I found my right pocket empty.)"
    K "(Hopefully, luck is on my side and my missing house key was in my left pocket…)"
    K "C’mon, c’mon…!"
    K "(...)"

    stop music

    K "(I left my house keys at home.)"
    K "(I let out a long disappointed sigh of defeat.)"
    K "(But oddly enough, there was a note I didn’t remember putting in my pocket...)"
    
    python:
        #create and write to file
        with open(file_path, "w") as file:

            message_1 = r"""
            [code]
            I'm sorry, but an uncaught exception occurred.

            While running game code:
            File "game/script.rpy", line 189, in script
            Kei "Please help me"
            Exception: Sayer 'Kei' is not defined.

            -- Full Traceback ------------------------------------------------------------

            Full traceback:
              File "game/script.rpy", line 189, in script
                Kei "Please help me"
              File "C:\\Users\\YOU\\OneDrive\\renpy-8.3.7-sdk\\renpy\\ast.py", line 2586, in execute
                Say.execute(self)
              File "C:\\Users\\YOU\\OneDrive\\renpy-8.3.7-sdk\\renpy\\ast.py", line 583, in execute
                who = eval_who(self.who, self.who_fast)
              File "C:\\Users\\YOU\\OneDrive\\renpy-8.3.7-sdk\\renpy\\ast.py", line 472, in eval_who
                raise Exception("Sayer '%s' is not defined." % who)
            Exception: Sayer 'Kei' is not defined.
            Attempting to define 'Kei'
            Scanning game directory for 'Kei'
            'Kei' successfully defined.
            Please close this message once finished.

            Windows-10-10.0.26100 AMD64
            Ren'Py 8.3.7.25031702
            VEIL: Beneath The Surface 1.0
            XXX XXX 15 16:28:04 2025
            [/code]"""

            file.write(message_1)
            file.close()

    if file_exists:
        python:
            os.system(f'notepad.exe {file_path}')
            ctypes.windll.user32.MessageBoxW(None,
            "Unexpected file interference! Please select OK to continue with the game.", 
            "Oh No!",
            48
            )
            os.system("taskkill /IM notepad.exe /F")
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
