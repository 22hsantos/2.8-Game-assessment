﻿# The script of the game goes in this file.

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

    import time, os, sys, ctypes

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
        try:
            os.remove(file_path)
            print("File deleted.")
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: You don'T have permission to delete this file.")

    #gets the player's name
    player_name = os.getlogin()

    #counts the number of Kei notes
    kei = 0

    #determines whether the player is stupid or not
    player_normal = False


#transitions
define dissolve = Dissolve(0.5)

#aligns and resizes sprites
transform scale_sprite:
    zoom 2
    xalign 0.5
    yalign 1.0

#zooms in bg, pans left to right
transform bg_pan:
    subpixel True
    zoom 1.5
    xalign 0.0
    linear 4.0 xalign 1.0

#aligns bg to centre and sizes up
transform bg:
    zoom 1.5
    xalign 0.5
    yalign 0.5

define Ke = Character("Zaigaku Kei")
define K = Character("Shujin Kou")
define u = Character("[player_name]")
define uk = Character("Unknown")
define Ka = Character("Takahashi Kagaku")
define coach = Character("Coach")
define T = Character("Sato Taiiku")

#Character Sprites
image kei default = "images/Kei/kei_default.png"

image ph = "images/PH_default.png"

#Kagaku Sprites
image kagaku neutral = "images/Kagaku/kagaku_neutral.png"
image kagaku sil = "images/Kagaku/kagaku_silhouette.png"
image kagaku angry = "images/Kagaku/kagaku_angry.png"
image kagaku excited = "images/Kagaku/kagaku_excited.png"
image kagaku startled = "images/Kagaku/kagaku_startled.png"
image kagaku neutral 2 = "images/Kagaku/kagaku_neutral2.png"

#Backgrounds
image bg hood = "images/backgrounds/bg_neighbourhood.jpeg"
image bg black = "images/backgrounds/bg_black.jpg"
image bg hallway = "images/backgrounds/bg_hallway.jpg"
image bg outside library = "images/backgrounds/bg_outside_library.jpg"
image bg library = "images/backgrounds/bg_library.jpg"
image bg cafeteria = 'images/backgrounds/bg_cafeteria.png'
image bg staircase = 'images/backgrounds/bg_staircase.jpg'
image bg rooftop = 'images/backgrounds/bg_rooftop.jpg'
image bg rooftop view = "images/backgrounds/bg_rooftop_view.jpg"
image bg afterschool = "images/backgrounds/bg_afterschool.png"
image bg gym = "images/backgrounds/bg_gym.png"


# The game starts here.



label start:

    stop music

    menu:
        "troubleshoot file creation":
            jump file_write
        "Play the story":
            jump story_start
        "Jump to checkpoint":
            jump checkpoint

#for easy label access
label checkpoint:

    u "Checkpoint reached"

    menu:

        "monday":
            jump monday_labels
        
        "tuesday":
            jump tuesday_labels
        "main menu":
            return

# shortcut to troubleshoot errors without going through dialogue
label file_write:
    u "Hello."

    if file_exists:
        u "Kei exists."
        $ os.remove(file_path)
        u "Kei does not exist."
    else:
        u "Kei does not exist."
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
                    u "I didn'T write a file."

                return

label story_start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    scene bg black at bg
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    # START MONDAY
    K "(My name is Shujin Kou.)"
    K "(I’m a third year high school student that has recently transferred to another school.)"
    K "(Why you ask?) "
    K "(Because my mom felt like it.)"
    K "(Yeah.)"
    K "(It’s whatever, I’ll just start getting ready for my first day.)"

    play music "LEASE.mp3"
    scene bg hood with dissolve
    
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

    play sound "sad_trombone.mp3"
    K "(I left my house keys at home.)"
    K "(I let out a long disappointed sigh of defeat.)"
    K "(But oddly enough, there was a note I didn’t remember putting in my pocket...)"

    menu:
        "Open it":
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
                    YOU MAY CLOSE THIS MESSAGE.

                    Windows-10-10.0.26100 AMD64
                    Ren'Py 8.3.7.25031702
                    VEIL: Beneath The Surface 1.0
                    XXX XXX 15 16:28:04 2025
                    [/code]"""

                    file.write(message_1)
                    file.close()

                    file_exists = os.path.exists(file_path)
                
            
            if file_exists:
                python:
                    os.system(f'notepad.exe {file_path}')
                    ctypes.windll.user32.MessageBoxW(None,
                    "Unexpected file interference! Please select OK to continue with the game.", 
                    "Oh No!",
                    48
                    )
                    os.system("taskkill /IM notepad.exe /F")

                    kei = kei + 1
                
                K "Huh, I can’t even read this… "
                K "It’s all random measurements."
                K "(I disregard the note and continue walking to my new school.)"

            else:
                K "What the heck..."   

                scene bg hood
                play music "LEASE.mp3"
                K "Huh, I can’t even read this… "
                K "It’s all random measurements."
                K "(I disregard the note and continue walking to my new school.)"

        "Leave it alone.":
            K "Ehh..."
            K "I can open it later."
            K "(I disregard the note and continue walking to my new school.)"
    

    jump monday_morning

#--- MONDAY ---
label monday_morning:
    scene bg hallway with dissolve
    play music "sincememo.mp3"
    play sound "stepping.mp3"

    K "(I was admiring my surroundings while strolling through the hallway.)"
    K "(It was like everywhere I saw was masterpiece painted by renowned painters.)"
    K "(After a while, I found myself in front of a familiar feeling door.) "
    scene bg outside library at bg ,with dissolve
    K "Ah."
    K "This must be the library."
    K "(I was relieved to see a school library so similar to mine.)"
    K "(That even though I’m in a new place, I'd still have a place to run away and escape reality.)"
    K "(I gently slid open the door.)"

    scene bg black
    play sound "stepping.mp3"

label monday_kagaku:

    K "(...)"

    K "(The Glass Atlas)"
    K "(Chronicles of a Vanished Kingdom)"
    K "(Where the Shadows Dream)"
    K "Woah…"
    K "This library has a great selection of books."
    K "(I couldn’t contain my excitement as I was indulging in my dearly missed paradise.)"
    K "I wonder if they have-"

    stop sound
    stop music
    play sound "bamboo.ogg"

    K "...!"

    play sound "crash.ogg"

    uk "Oof!"

    scene bg library
    show kagaku sil at scale_sprite
    play music "spirited.mp3"

    uk "Hey."
    uk "Watch where you’re going."

    show kagaku angry with dissolve

    K "Oh! I’m sorry…"
    K "I didn’t see you there."

    show kagaku neutral 

    uk "*sigh*"
    uk "It’s fine."

    play music "BTS.mp3"

    uk "I’ve never seen you around before."
    uk "Are you new?"

    K "(I’m startled at her sharp observation.)"
    K "Y-yeah, how did you know?"

    uk "I’m the student council president, so I know my peers quite well."
    uk "Allow me to welcome you to Hoshizora Academy…"

    K "Ah, Shujin Kou."

    Ka "Shujin-kun. My name is Takahashi Kagaku."
    K "Taka…Takaha-"

    show kagaku neutral 2

    Ka "*Sigh*"
    Ka "Kagaku is fine."

    show kagaku neutral

    K "Thank you very much, Kagaku."

    K "(I could feel the tension set in as soon as it fell silent)"
    K "(My eyes quickly dart around the room, as to keep the already dead conversation going.)"
    K "(Suddenly, I recognize the book that was in Kagaku’s hand.)"
    K "(It was *Echoes in the Fog*, a classic thriller novel that was popular upon release.)"
    K "(However, popularity has dwindled in the recent years, so it quickly became a niche.)"
    K "Hey…"

    show kagaku startled at scale_sprite

    K "Is that *Echoes in the Fog*?"

    Ka "!"

    show kagaku excited with dissolve

    Ka "You’ve read *Echoes in the Fog*?!"
    Ka "No way!"
    Ka "I’ve never met anyone who has read this book before…!"
    Ka "Honestly, everyone I’ve tried to convince to read it just called me an old woman and said it sounded quite boring."
    Ka "I really liked the part where—"

    menu:
        "Interrupt her":
            jump interrupt_kagaku

        "Let her yap":
            jump let_kagaku_talk

label interrupt_kagaku:
    show kagaku startled
    Ka "Ah."
    show kagaku neutral
    Ka "Ahem. Sorry, I got a bit carried away."
    Ka "I have to go to class."
    Ka "See you."

    hide kagaku neutral with easeoutleft

    K "(I’m left speechless at the sudden switch from a fanatic bookworm to a composed president)"
    K "(...)"
    K "I guess I’ll go too…"

    scene bg black
    jump classroom_scene

label let_kagaku_talk:
    Ka "Oh, and I love the twist in chapter 8—"
    
    show kagaku startled
    
    Ka "!"

    show kagaku neutral

    Ka "Ahem. Sorry, I got a bit carried away."
    Ka "I have to go to class."
    Ka "See you."

    hide  kagaku neutral at left with easeoutleft
    hide kagaku

    K "(I’m left speechless at the sudden switch from a fanatic bookworm to a composed president)"
    K "(...)"
    K "I guess I’ll go too…"

    scene bg black
    jump classroom_scene

label classroom_scene:
    #scene bg classroom

    K "I’ve got nothing to do right now."
    K "I should…"

    menu:
        "Eat at cafeteria":
            jump monday_cafeteria

        "Explore the school (rooftop)":
            jump monday_rooftop
        
label monday_cafeteria:
    K "I should get something to eat."
    K "I didn'T have time to eat breakfast after all."
    scene bg black
    play music "cafeteria.mp3"
    scene bg cafeteria at bg ,with fade

    K "(As soon as I stepped into the cafeteria, a heavenly scent wafted to my nose.)"
    K "(Was that... curry?)"
    K "(I couldn'T help but chase after the source, and taste what might've smelled like the best food I'd have in my entire life.)"
    scene bg black
    stop music
    play sound "bell.wav" volume 0.5

    jump checkpoint

label monday_rooftop:

    K "I wonder what the view up on the rooftop is like."

    scene bg black

    scene bg staircase at bg
    play sound "stepping.mp3"

    K "(I find myself stepping up what might've been the longest staircase of my entire life.)"
    K "*Huff* *Huff*"
    K "How big..."
    K "Is this..."
    K "Goddamn school...!?"

    scene bg black

    play sound "sliding_door.mp3"

    pause 1.5

    scene bg rooftop with dissolve
    
    play music "rooftop.mp3"

    K "Woah...!"
    K "What a view..."
    K "(I stepped closer to the fence, looking down the whole city.)"

    scene bg rooftop view at bg_pan
    with dissolve
    pause

    K "Everything looks so small from up here."
    
    scene bg black

    K "(I spend a moment enjoying watching people live their everyday life before going back to class.)"

    stop music
    play sound "bell.wav" volume 0.5

    jump monday_afterschool

label monday_afterschool:
    play sound "bell.wav" volume 0.5
    scene bg afterschool with fade
    pause 3.0
    play music "TOL.mp3"

    K "*Yawn*"
    K "That class had me beat."
    K "How am I supposed to be on the same level as everyone else, anyway?"
    K "This is literally my first day here!"
    K "..."
    K "Whatever, I’m going home."

    scene bg black with dissolve
    play sound "stepping.mp3" volume 1.5

    K "(Hmm? What’s all that noise?)"
    K "(I look around, and find that the source of the commotion has been coming from the school gym.)"
    K "(Guess I might check it out, I guess.)"

    scene bg gym with fade

    K "(It seems that the basketball club had some activities today.)"
    K "(I stick around for a while, watching the players do their drills.)"
    K "(I blankly stare at a ball that came out of nowhere.)"
    K "(Hey, isn’t that ball coming straight towards my—)"

    #replace sfx
    stop music
    play sound "bamboo.ogg"
    scene bg black

    K "*Thud!*"
    K "(An inexplicable pain started radiating from my forehead.)"
    K "(I could feel all the blood rushing as the red mark started thumping non-stop.)"

    uk "Oh my gosh! Are you okay!?"

    K "(I open my eyes to find a girl standing right in front of me.)"

    uk "Ahh, what do I do??"
    K "Huh…"
    K "(I manage to open my eyes.)"

    scene bg gym with dissolve
    play music "spirited.mp3"
    show ph

    uk "Um!"
    uk "How many fingers am I holding!?"

    K "What…?"
    K "(I try to readjust my vision.)"

    #show taiiku_fingers

    uk "I said how many fingers am I holding??"

    K "Uhh…"

    menu:
        "3":
            jump normal
        "7":
            $ player_normal = False
            jump concussed

label normal:
    K "Um, 3?"
    #Excited Taiiku sprite
    uk "Thank god!"
    uk "You didn'T lose any brain juice!"
    jump monday_taiiku

label concussed:
    K "Um, 7?"
    stop music
    play sound "crash.ogg"
    uk "..."
    uk '****'
    #shocked Taiiku sprite
    uk "Oh no!"
    play music "spirited.mp3"
    uk "I broke him!"
    uk "AhhwhatdoIdoImtooyoungtogotojail!!!"
    #worried taiiku
    uk "M-maybe I can salvage this..."
    jump monday_taiiku

label monday_taiiku:

    play music "ROB.mp3"

    uk "Here, let me help you up!"
    K "(The peculiar girl reaches out her hand.)"

    scene black

    K "(Hup!)"

    scene bg gym

    show ph
    
    K "Thanks…"

    uk "Don’t mention it!"
    uk "Ah!"
    uk "I never told you my name, did I…"

    K "Ah, same here."
    K "I’m Shujin Kou."

    T "I’m Sato Taiiku."
    T "But everyone just calls me Taiiku."

    K "(I become rigid for a moment.)"
    K "Ah! Are you sure?"

    T "What’s the matter?"
    K "It’s just… we’ve just met and—"

    #show taiiku_proud

    T "Hah!"
    T "So what?"
    T "Everyone I meet, I consider my closest friends!"

    K "Um, okay… if you say so."

    T "But enough about that!"

    #show taiiku_embarrassed

    T "Is your head okay? You took a really hard hit."

    K "(She tries to reach her hand out to me once to examine my forehead when…)"

    coach "Taiiku!!"

    #show taiiku_shocked

    coach "Stop slacking off and help with cleanup!"

    #show taiiku_pouty

    T "Geez! I’m trying to help someone here!"

    #show taiiku_embarrassed

    T "Sorry Kou!"
    T "I’ll treat you sometime as an apology!"

    #hide taiiku
    hide ph with easeoutleft

    K "(And another one runs away…)"
    K "*sigh*"
    K "I think I’ve had enough exploring for my first day here."
    K "I’m gonna head home."

    scene bg black
    jump monday_bedroom

label monday_bedroom:

    K "(I hurried home before the sun set.)"

    #scene bg bedroom

    K "(While I was a bit overwhelmed with the events that happened today, I was glad I made two new friends.)"
    jump checkpoint

label monday_labels:
    u "all monday labels"

    menu:

        "jump story start":
            jump story_start

        "monday morning":
            jump monday_morning

        "monday midday classroom":
            jump classroom_scene
        
        "monday afterschool":
            jump monday_afterschool
        
        "return to checkpoint":
            jump checkpoint


#--- TUESDAY ---

label tuesday_labels:
    u "all tuesday labels"

    menu:
        "tuesday_morning":
            jump tuesday_morning
        
        "go back":
            jump checkpoint

label tuesday_morning:

    scene bg black

    K "(My eyelids started lifting the moment the sun hit my eyes.)"

    #scene bg bedroom
    play music "ROB.mp3"

    K "Argh… Morning already?"
    K "(I groggily put on my uniform and gather my things.)"
    K "Okay, time to go to—"

    stop music

    K "(I suddenly put my hand over my right pocket.)"

    play music "ROB.mp3"

    K "*Sigh* Thank god I remembered this time…"
    K "I don’t want to ever climb in through the window again."
    K "Hopefully no one saw me, I’d die of embarrassment."
    K "Well, I’m off."

    play music "LEASE.mp3"
    scene bg hood with dissolve
    play sound "stepping.mp3"

    K "I wonder if I’ll see Kagaku again."
    K "She seems a bit odd, but I’m glad to have another book-buddy."
    K "Taiiku too."
    K "I hope she treats me today, that ball did leave a bruise after all."
    K "It took forever to stop the swelling…"

    scene bg black

    K "(As soon as I arrived inside the school entrance, I immediately headed straight for the library.)"

    scene bg outside library at bg ,with dissolve

    K "(Here goes nothing...)"

    scene bg black
    scene bg library

    show kagaku neutral at scale_sprite

    Ka "Oh!"
    Ka "Shujin-kun."

    #show kagaku smile

    Ka "Good morning."

    K "Ka…Kagaku-san..."

    #show kagaku laugh

    Ka "Hahaha!"

    #show kagaku neutral

    Ka "Just Kagaku is fine."
    Ka "It’s a bit odd if you add -san to my first name."

    K "(My cheeks grow a bit pink from embarrassment.)"

    Ka "How are you today?"

    K "I’m pretty alright, thanks."
    K "How about you?"

    #show kagaku hesitated

    Ka "I’m… alright, thank you."

    K "(I sense the slight hesitation in her words.)"
    K "Is… something wrong?"

    show kagaku startled at scale_sprite

    Ka "Ah! It’s nothing. It’s just…"

    #show kagaku hesitated
    show kagaku neutral

    Ka "..."
    Ka "I’ve just taken a lot of responsibilities at once since we’re starting the school year."
    Ka "And I’ve just been a bit stressed while organising that and other things too."

    K "(A wave of empathy washes over me as I continue to listen to her troubles.)"
    K "Woah, sounds tough on you."

    show kagaku startled

    Ka "No! Not at all! I can handle it myself."

    #show kagaku hesitated

    Ka "I just need a little time, that’s all."

    K "(A sense of doubt and concern hits me, but I try to encourage Kagaku.)"
    K "Alright, just…"
    K "Tell me if you need anything, okay?"

    #show kagaku startled

    Ka "..."

    #show kagaku smile

    Ka "Thank you, Shujin-kun."
    Ka "That means a lot to me."

    play sound "bell.wav" volume 0.5

    pause 3.0

    show kagaku neutral
    Ka "What a shame, I guess I’ll have to see you later?"

    K "Yeah, later."

    hide kagaku
    scene bg black

    jump checkpoint

label tuesday_midday:
    play sound "bell.wav" volume 0.5

    #classroom bg

    K "I've got nothing to do right now."
    K "I should..."

    menu:
        
        "eat at the cafeteria":
            jump tuesday_cafeteria
        
        "Explore the school":
            jump tuesday_theatre
    
    
label tuesday_cafeteria:
    
    K "I should go to the cafeteria."
    K "I am feeling a bit hungry"

    scene bg black

    K "(I make my way to the cafeteria once again, curious for what's on the menu today.)"

    play music "cafeteria.mp3"

    scene bg cafeteria

    K "...!"
    K "(I expected a delicious smell to greet me like yesterday...)"

    stop music

    K "(But today's meal took a total 180 degree turn)"

    play music "spirited.mp3"

    K "Ugh...what is this smell?"
    K "(It was an indescribable smell.)"
    K "(The closest I could get to describing this is physical assault...)"
    K "(But to my nose.)"
    K "(Yeah, no.)"
    K "(I guess it's no lunch for me today.)"

    scene bg black
    play sound "bell.wav" volume 0.5

    jump checkpoint
