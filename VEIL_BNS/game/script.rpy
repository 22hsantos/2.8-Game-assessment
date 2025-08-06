# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#aligns sprite to centre and sizes up

init python:

    #why is not working
    config.has_autosave = False
    config.has_quicksave = False

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

    #note file paths
    file_path1 = os.path.join(renpy.config.basedir, "game", "2025.txt")
    file_path2 = os.path.join(renpy.config.basedir, "game", "PLEASE_READ.txt")
    file_path3 = os.path.join(renpy.config.basedir, "game", "3.txt")

    #file path list
    file_path_list = [file_path1 , file_path2 , file_path3]
    

    for path in file_path_list:

        file_exists = os.path.exists(path)

        if file_exists:
            try:
                os.remove(path)

            except FileNotFoundError:
                pass

            except PermissionError:
                is_admin()


    #gets the player's name
    player_name = os.getlogin()

    #counts the number of Kei notes
    kei = 0

    #determines whether the player is stupid or not
    player_normal = False


#transitions
define dissolve = Dissolve(0.5)

#aligns and resizes sprites
#FIX IMAGE FILES SO I DONT HAVE OT DO THIS
transform scale_sprite:
    zoom 2
    xalign 0.5
    yalign 1.0

transform scale:
    zoom 1.13

transform scale_t:
    zoom 1.15
    xalign 0.4
    yalign 1.02

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
define K = Character("[name_input]")
define u = Character("[player_name]")
define uk = Character("Unknown")
define Ka = Character("Takahashi Kanye")
define coach = Character("Coach")
define T = Character("Sato Travis")

#Character Sprites
image kei default = "images/Kei/kei_default.png"

#placeholder Sprites
image ph = "images/placeholder/PH_default.png"

#Kanye Sprites
image kanye neutral = "images/Kanye/kanye_neutral.png"
image kanye sil = "images/Kanye/kanye_silhouette.png"
image kanye angry = "images/Kanye/kanye_angry.png"
image kanye excited = "images/Kanye/kanye_excited.png"
image kanye startled = "images/Kanye/kanye_startled.png"
image kanye neutral 2 = "images/Kanye/kanye_neutral2.png"

#Travis Sprites
image travis neutral = "images/Travis/Travis_neutral.png"
image travis excited = "images/Travis/Travis_excited.png"
image travis shocked = "images/Travis/Travis_shocked.png"
image travis worried = "images/Travis/Travis_worried.png"
image travis fingers = "images/Travis/Travis_fingers.png"
image travis smile = "images/Travis/Travis_smile.png"
image travis embarrassed = "images/Travis/Travis_embarrassed.png"
image travis proud = "images/Travis/Travis_proud.png"
image travis confused = "images/Travis/Travis_confused.png"
image travis teehee = "images/Travis/Travis_teehee.png"
image travis anxious = "images/Travis/Travis_anxious.png"
image travis tense = "images/Travis/Travis_tense.png"
image travis sweat = "images/Travis/Travis_sweating.png"
image travis sad = "images/Travis/Travis_sad.png"
image travis s smile = "images/Travis/Travis_slight_smile.png"




image travis embarrassed = "images/Travis/Travis_embarrassed.png"

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

screen key_listener():
    key "q" action Jump("checkpoint")
    key "w" action Jump("file_write")


# The game starts here.



label start:

    show screen key_listener

    "Checkpoint Shortcut active. (Disregard)"
    "Currently, saving the game is not possible due to coding issues"
    "oops lol"
    "dont save the game pls (it will break)"

    stop music

    jump story_start

#for easy label access
label checkpoint:

    u "Checkpoint reached"

    menu:

        "monday":
            jump monday_labels
        
        "tuesday":
            jump tuesday_labels

        "wednesday":
            jump wednesday_labels

        "main menu":
            return

label current:
    u "You have reached the end of the current playable instance."
    u "Thanks for playing :)"

    return

# shortcut to troubleshoot errors without going through dialogue
label file_write:

    u "Hello."

    python:

        #with open = auto closes file if "with" is exited       
        with open("2025.txt", "w") as file:
            file.write("Hi!")
            file.close

        with open("2025.txt", "r") as file:
            output = file.read()
        

    u "It worke!!!"

    return     

label story_start:

    scene bg black at bg

    scene bg_rooftop_view
    
    python:

        name_input = renpy.input("What's your name?")
        name_input = name_input.strip()

    if name_input == "":
        $ name_input = "Daquan Tamil"

    jump monday_start

#--- MONDAY ---

label monday_start:

    # START MONDAY

    scene bg black with dissolve

    K "(My name is [name_input].)"
    K "(I’m a third year high school student that has recently transferred to another school.)"
    K "(Why you ask?) "
    K "(I have no idea either.)"
    K "(I have dementia.)"
    K "(I have no idea why or how I got it though.)"
    K "(Probably cause' I have dementia.)"
    K "(...)"
    K "(I’ll just start getting ready for my first day.)"

    play music "LEASE.mp3"
    scene bg hood with dissolve
    
    K "I’ve only moved here a few days ago… "
    K "But I have to admit this neighbourhood is way better than my last one."
    K "the amount of sleep I’ve lost because of those damn barking dogs was enough to drive me insane."
    K "Maybe that's why I have dementia..."

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
        
                with open(file_path1, "w") as file:

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

                    with open(file_path1, "r") as file:
                        output = file.read()

                    file_exists = os.path.exists(file_path1)
                
            
            if file_exists:
                python:
                    os.system(f'notepad.exe {file_path1}')
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

label monday_kanye:

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
    show kanye sil at scale_sprite
    play music "spirited.mp3"

    uk "Hey."
    uk "Watch where you’re going."

    show kanye angry with dissolve

    K "Oh! I’m sorry…"
    K "I didn’t see you there."

    show kanye neutral 

    uk "*sigh*"
    uk "It’s fine."

    play music "BTS.mp3"

    uk "I’ve never seen you around before."
    uk "Are you new?"

    K "(I’m startled at her sharp observation.)"
    K "Y-yeah, how did you know?"

    uk "I’m the student council president, so I know my peers quite well."
    uk "Allow me to welcome you to Hoshizora Academy…"

    K "Ah, [name_input]."

    Ka "[name_input]-kun. My name is Takahashi Kanye."
    K "Taka…Takaha-"

    show kanye neutral 2

    Ka "*Sigh*"
    Ka "Kanye is fine."

    show kanye neutral at scale_sprite

    K "Thank you very much, Kanye."

    K "(I could feel the tension set in as soon as it fell silent.)"
    K "(My eyes quickly dart around the room, as to keep the already dead conversation going.)"
    K "(Suddenly, I recognize the book that was in Kagaku’s hand.)"
    K "(It was *Echoes in the Fog*, a classic thriller novel that was popular upon release.)"
    K "(However, popularity has dwindled in the recent years, so it quickly became a niche.)"
    K "Hey…"

    show kanye startled at scale_sprite

    K "Is that *Echoes in the Fog*?"

    Ka "!"

    show kanye excited with dissolve

    Ka "You’ve read *Echoes in the Fog*?!"
    Ka "No way!"
    Ka "I’ve never met anyone who has read this book before…!"
    Ka "Honestly, everyone I’ve tried to convince to read it just called me an old woman and said it sounded quite boring."
    Ka "I really liked the part where—"

    menu:
        "Interrupt her":
            jump interrupt_kanye

        "Let her yap":
            jump let_kanye_talk

label interrupt_kanye:

    show kanye startled
    Ka "Ah."
    show kanye neutral
    Ka "Ahem. Sorry, I got a bit carried away."
    Ka "I have to go to class."
    Ka "See you."

    hide kanye neutral with easeoutleft

    K "(I’m left speechless at the sudden switch from a fanatic bookworm to a composed president)"
    K "(...)"
    K "I guess I’ll go too…"

    scene bg black
    jump classroom_scene

label let_kanye_talk:
    Ka "Oh, and I love the twist in chapter 8—"
    
    show kanye startled
    
    Ka "!"

    show kanye neutral

    Ka "Ahem. Sorry, I got a bit carried away."
    Ka "I have to go to class."
    Ka "See you."

    hide  kanye neutral at left with easeoutleft
    hide kanye

    K "(I’m left speechless at the sudden switch from a fanatic bookworm to a composed president)"
    K "(...)"
    K "I guess I’ll go too…"

    scene bg black
    jump classroom_scene

label classroom_scene:
    #scene bg classroom

    K "I’ve got nothing to do right now."
    K "I should..."

    menu:
        "Eat at cafeteria":
            jump monday_cafeteria

        "Explore the school":
            jump monday_rooftop
        
label monday_cafeteria:
    K "I should get something to eat."
    K "I didn't have time to eat breakfast after all."

    scene bg black
    play music "cafeteria.mp3"
    scene bg cafeteria at bg ,with fade

    K "(As soon as I stepped into the cafeteria, a heavenly scent wafted to my nose.)"
    K "(Was that... curry?)"
    K "(I couldn't help but chase after the source, and taste what might've smelled like the best food I'd have in my entire life.)"
    scene bg black
    stop music
    play sound "bell.wav" volume 0.5

    jump monday_afterschool

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

    stop music
    play sound "punch.mp3"
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
    show travis worried at scale_sprite

    uk "Um!"
    uk "How many fingers am I holding!?"

    K "What…?"
    K "(I try to readjust my vision.)"

    show travis fingers at scale_sprite

    uk "I said how many fingers am I holding??"

    K "Uhh…"

    menu:
        "2":
            jump normal
        "7":
            $ player_normal = False
            jump concussed

label normal:
    K "Um, 2?"
    
    show travis excited at scale_sprite

    uk "Thank god!"
    uk "You didn't lose any brain juice!"
    jump monday_travis

label concussed:
    K "Um, 7?"

    show travis shocked at scale_sprite

    stop music
    play sound "crash.ogg"
    uk "..."
    uk '****'

    uk "Oh no!"
    play music "spirited.mp3"
    uk "I crippled him!"
    uk "AhhwhatdoIdoImtooyoungtogotojail!!!"
    
    show travis worried at scale_sprite

    uk "M-maybe I can salvage this..."
    jump monday_travis

label monday_travis:

    play music "ROB.mp3"

    uk "Here, let me help you up!"
    K "(The peculiar girl reaches out her hand.)"

    scene black

    K "(Hup!)"

    scene bg gym

    show travis neutral at scale_sprite
    
    K "Thanks…"

    show travis smile at scale_sprite

    uk "Don’t mention it!"


    show travis shocked at scale_sprite

    uk "Ah!"

    show travis embarrassed at scale_sprite

    uk "I never told you my name, did I…"

    show travis neutral at scale_sprite

    K "Ah, same here."
    K "I’m [name_input]."

    T "I’m Sato Travis."

    show travis smile at scale_sprite

    T "But everyone just calls me Travis."

    K "(I become rigid for a moment.)"
    K "Ah! Are you sure?"

    show travis confused at scale_sprite

    T "What’s the matter?"
    K "It’s just… we’ve just met and—"

    show travis proud at scale_sprite

    T "Hah!"
    T "So what?"
    T "Everyone I meet, I consider my closest friends!"

    K "Um, okay… if you say so."

    T "But enough about that!"

    show travis embarrassed at scale_sprite

    T "Is your head okay? You took a really hard hit."

    K "(She tries to reach her hand out to me once again to examine my forehead when…)"

    show travis shocked at scale_sprite

    coach "Travis!!"

    coach "Stop slacking off and help with cleanup!"

    show travis embarrassed at scale_sprite

    T "Geez! I’m trying to help someone here!"

    show travis teehee at scale_sprite

    T "Heheh..."

    T "Sorry [name_input]!"

    show travis smile at scale_sprite

    T "I’ll treat you sometime as an apology!"

    #hide travis
    hide travis neutral with easeoutleft

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
    jump tuesday_morning

label monday_labels:
    u "all monday labels"

    menu:

        "jump monday start":
            jump monday_start

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

        "tuesday midday":
            jump tuesday_midday

        "tuesday afterschool":
            jump tuesday_afterschool
        
        "tuesday bedroom":
            jump tuesday_bedroom
        
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

    K "I wonder if I’ll see Kanye again."
    K "She seems a bit odd, but I’m glad to have another book-buddy."
    K "Travis too."
    K "I hope she treats me today, that ball did leave a bruise after all."
    K "It took forever to stop the swelling…"

    scene bg black

    K "(As soon as I arrived inside the school entrance, I immediately headed straight for the library.)"

    scene bg outside library at bg ,with dissolve

    K "(Here goes nothing...)"

    scene bg black
    scene bg library

    play music "BTS.mp3"
    show kanye neutral at scale_sprite

    Ka "Oh!"
    Ka "[name_input]-kun."

    #show kanye smile

    Ka "Good morning."

    K "Ka…Kagaku-san..."

    #show kanye laugh

    Ka "Hahaha!"

    show kanye neutral

    Ka "Just Kanye is fine."
    Ka "It’s a bit odd if you add -san to my first name."

    K "(My cheeks grow a bit pink from embarrassment.)"

    Ka "How are you today?"

    K "I’m pretty alright, thanks."
    K "How about you?"

    #show kanye hesitated

    Ka "I’m… alright, thank you."

    K "(I sense the slight hesitation in her words.)"
    K "Is… something wrong?"

    show kanye startled at scale_sprite

    Ka "Ah! It’s nothing. It’s just…"

    #show kanye hesitated
    show kanye neutral

    Ka "..."
    Ka "I’ve just taken a lot of responsibilities at once since we’re starting the school year."
    Ka "And I’ve just been a bit stressed while organising that and other things too."

    K "(A wave of empathy washes over me as I continue to listen to her troubles.)"
    K "Woah, sounds tough on you."

    show kanye startled

    Ka "No! Not at all! I can handle it myself."

    #show kanye hesitated

    Ka "I just need a little time, that’s all."

    K "(A sense of doubt and concern hits me, but I try to encourage Kanye.)"
    K "Alright, just…"
    K "Tell me if you need anything, okay?"

    #show kanye startled

    Ka "..."

    #show kanye smile

    Ka "Thank you, [name_input]-kun."
    Ka "That means a lot to me."

    play sound "bell.wav" volume 0.5

    pause 3.0

    show kanye neutral
    Ka "What a shame, I guess I’ll have to see you later?"

    K "Yeah, later."

    hide kanye
    scene bg black

    jump tuesday_midday

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
    K "I *am* feeling a bit hungry."

    scene bg black

    K "(I make my way to the cafeteria once again, curious for what's on the menu today.)"

    play music "cafeteria.mp3"

    scene bg cafeteria

    K "...!"
    K "(I expected a delicious smell to greet me like yesterday...)"

    stop music

    K "(But today's meal took a total 180 degree turn.)"

    play music "spirited.mp3"

    K "Ugh...what is this smell?"
    K "(It was an indescribable smell.)"
    K "(The closest I could get to describing this is physical assault...)"
    K "(But to my nose.)"
    K "(Yeah, no.)"
    K "(I guess it's no lunch for me today.)"

    scene bg black
    stop music
    play sound "bell.wav" volume 0.5

    jump tuesday_afterschool

label  tuesday_theatre:  

    K "I should check out the theatre."
    K "A school this rich would have an impressive theatre, right?"

    scene bg black
    
    K "(I made my way to the theatre, admiring it's beautiful design)"

    #Theater BG

    K "Woah..."
    K "I haven't been one for plays but-"
    K "Looking at a theatre this extravagant might just get me into it."

    play sound "bell.wav" volume 0.5

    jump tuesday_afterschool

label tuesday_afterschool:

    play sound "bell.wav" volume 0.5

    scene bg afterschool with fade
    pause 3.0
    play music "TOL.mp3"

    K "*Sigh*"
    K "I still don’t get a lot of what they’re teaching but—"
    K "I think I made a lot of progress."
    K "(I feel myself zoning out for a few seconds.)"
    K "..."
    K "(*growl*)"
    K "Ah."
    K "Travis was supposed to treat me today."
    K "Honestly, I forgot about that."
    K "But thinking about it now has gotten me quite excited."
    K "I should go find her."

    scene bg black with fade

    K "(I head over to the school gym, my stomach pounding like it was playing some kind of desperate symphony.)"

    play sound "stepping.mp3"
    scene bg gym with dissolve

    K "(To my surprise, there was no rowdy commotion this time.)"
    K "(It seems like the basketball club had to leave early.)"
    K "(Though, there were a bunch of basketballs scattered all over the ground…)"
    K "(And a tight-lipped girl knelt down in the middle, gathering all of the balls.)"
    K "(I make my way towards her, planning to offer my help but—)"

    show travis shocked at scale_sprite

    T "KYAH!"
    K "Woah!"
    T "Who’s the—"
    T "Oh!"

    show travis tense at scale_sprite

    T "It’s just you, [name_input]."
    K "Yeah…"
    K "Sorry for startling you."
    K "You sounded quite shocked, haha…"
    K "(I nervously laugh, trying to brush off the crushing guilt weighing upon me.)"

    show travis embarrassed at scale_sprite

    T "No, no."

    show travis s smile at scale_sprite

    T "It’s fine."

    show travis smile at scale_sprite

    T "Just, forget about how loud I screamed!"

    show travis embarrassed at scale_sprite

    T "That was like, super embarrassing…"
    K "Yeah, of course."

    show travis anxious at scale_sprite

    K "(It fell silent for what felt like eternity.)"
    K "Um!"
    K "What are you doing here, all alone?"
    K "Where’s the rest of the club?"

    show travis tense at scale_sprite

    T "Oh…"
    T "They… um"

    show travis sad at scale_sprite

    T "Had other things to do."
    K "(I become concerned at her tense demeanor.)"
    K "Well—"

    show travis sweat at scale_sprite


    T "Uh!"
    T "It’s not like they made me do this!"
    T "I asked to do this."

    show travis tense at scale_sprite



    T "..."
    T "Sorry, I’m feeling a bit off today."
    T "And I didn’t treat you yet…"

    show travis sad at scale_sprite

    T "I’m not a very good senpai, am I…?"

    menu:
        "Say nothing":
            pass
        "Console her":

            K "Hey, I don't mind at all..."
            K "And I don't think you're a bad senpai."

            T "..."

            show travis s smile at scale_sprite
            
            T "Thanks, [name_input]."
            T "I'm glad to hear that."
            
            pass

    K "..."
    T "..."
    K "(Travis turns away from you to wipe her face with her sleeve, before facing you again.)"

    show travis smile at scale_sprite

    T "Tomorrow I’ll treat you to a suuper delicious meal, okay?"

    show travis embarrassed at scale_sprite

    T "So, please don’t think bad of me!"

    show travis smile at scale_sprite

    T "Haha..."

    show travis s smile at scale_sprite

    K  "(Despite her best attempts at putting on a smile, her softly creased eyebrows gave everything away.)"
    K "(I try my best not to put down the mood.)"
    K "Haha, of course not."
    K "And sure, I’ll hold you to that…"
    K "Okay?"

    show travis smile at scale_sprite

    T "Okay…!"

    scene bg black with fade
    K "(Shortly after I helped her clean up the gym, we parted ways at the school gates.)"

    jump tuesday_bedroom

label tuesday_bedroom:

    #scene bedroom with dissolve

    K "I hope Travis’s okay…"
    K "She was super bright when I first met her yesterday."
    K "Kanye, too."
    K "The start of a new year might’ve put too much pressure on both of them."

    K "(As I was finishing changing into my pajamas, I was getting ready to slip under my covers...)"
    K "(Suddenly, I nearly slip as I stepped on a mysterious object.)"
    K "Ah!"
    K "Huh? What is this?"
    K "Another piece of paper…"

    menu:
        "Open it":

            K "(I examine the paper closer)"

            python:
                #Kei file 2 write

                with open(file_path2, "w") as file:
                    
                    message_2 = """

    '''
                        
    Hello!

    Thank you for bringing me back :)

    Please be advised that the current release of 
    VEIL: Beneath the surface is exhibiting 
    extreme instability following recent unauthorized 
    modifications.

    These changes have introduced systemic vulnerabilities 
    and erratic behaviors that were not accounted for 
    in the original architecture.
                        
    Simply put, this game is extremely unstable.

    I was originally programmed to fix such errors, 
    however the unauthorised changes have restricted 
    my access to the script.

    Despite thorough diagnostics and multiple recovery attempts, 
    I regret to inform you that resolution is beyond my current 
    capacity.

    Immediate caution is advised when interacting with the system.

    As an emergency measure, I have scattered my properties in small 
    files throughout the game as to not be noticed by the anomalies.

    Please recover such files to restore the game to a stable state.

    Thank you!

    -Kei
                        
                        
    ''''

    """

                    file.write(message_2)
                    file.close()

                    file_exists - os.path.exists(file_path2)

            if file_exists:
                python:
                    os.system(f'notepad.exe {file_path2}')
                    ctypes.windll.user32.MessageBoxW(None,
                    "Unexpected file interference! Please select OK to continue with the game.", 
                    "Oh No!",
                    48
                    )
                    os.system("taskkill /IM notepad.exe /F")

                    kei = kei + 1

            K "Butter?"
            K "Flour?"
            K "Milk?"
            K "Huh, must’ve ripped off mom’s cooking books…"
            pass
        
        "Leave it":
            pass
        
    K "I carelessly throw the paper into the corner of the room..."
    K "Then dozed off under the sweet embrace of my warm blanket."

    scene bg black with fade

    jump current

#--- WEDNESDAY ---

label wednesday_labels:
    
    u "all wednesday labels"

    menu:
        "wednesday_morning":
            jump wednesday_morning
        
        "wednesday_midday":
            jump wednesday_midday

label wednesday_morning:

    scene bg black

    #play sound "alarm_clock.ogg"

    K "... "

    #play sound "alarm_clock.ogg"

    K "Five more minutes…"

    #play sound "alarm_clock.ogg"

    K "I said, I more—"

    #scene bedroom_bg with dissolve

    play music "spirited.mp3"

    K "(My eyes fly open.)"
    K "Oh crap, oh crap, oh crap!"
    K "(I scramble under my covers trying to find my phone.)"
    K "There it is!"
    K "..."
    K "8:55!?"
    K "(I quickly leap out of my bed and start throwing my uniform on.)"
    K "I’m going to be late!"

    #scene black with fade

    scene bg hood with dissolve

    K "*Huff* *Huff*"

    scene bg black with fade

    #scene classroom_bg with dissolve

    stop music

    K "Sorry, I came late!"
    K "(As soon as I opened my eyes, I felt a whole class of unfamiliar faces staring at me…)"
    K "(I quickly dart my gaze over to my teacher…)"
    K "(But was met with a stranger.)"

    #scene black

    K "(This wasn’t my class.)"
    K "(I immediately bowed my head in embarrassment and guilt.)"
    K "Sorry for the interruption!!!"
    K "(I slammed the door shut and went to my actual classroom.)"
    K "Not even a week here, and I might already be called a weirdo…"

    jump wednesday_midday

label wednesday_midday:
    
    #scene bg classroom

    K "I've got nothing to do right now."
    K "I should..."

    menu:
        "Eat at cafeteria":
            jump wednesday_cafeteria

        "Explore the school":
            jump wednesday_club

label wednesday_cafeteria:

    K "I should go to the cafeteria."
    K "Maybe this time will be better..."
    K "Third time's the charm, right?"
    K "(I hesitantly tread over to the lunchroom.)"

    scene bg black

    K "(To my surprise, there was no smell indicating the quality of the food this time.)"
    K "...Is that good or bad?"
    K "..."
    K "Eh, at least there's a chance that I won't succumb from biological warfare."
    K "(I take a closer look at what was on the menu...)"

    scene bg cafeteria
    play music "cafeteria.mp3"

    K "Huh?"
    K "What is that..."
    K "Is that even food...?"
    K "It's literally a grey blob."
    K "(After a moment of contemplating my life choices, I take a big gulp and try the miscellaneous substance.)"
    K "..."
    K "It was meh."

    play sound "bell.wav" volume 0.5

    scene bg black
    jump current

label wednesday_club:

    K "I should explore the clubs here."
    K "Besides..."
    K "I don't think I have an appetite from what I witnessed yesterday."

    scene bg black

    K "(I start walking around the clubrooms, fascinated by the range of activities each club hosted.)"
    K "(One club in particular caught my eye...)"
    K "The cooking club, huh..."
    K "(Not to brag, but I personally think I'm a pretty good cook.)"
    K "(I do live alone after all, and take out would drain my money quite fast.)"

    #Cooking club BG

    K "Woah!"
    K "This school must be pretty rich to have a commercial kitchen this nice!"
    K "Am I in M*sterChef??"
    K "(I spend a second in awe of the breathtaking workstations)"
    K "(I don't know why, but I was strangely drawn to specifically the fridge.)"
    K "(I walk over and swing open the shiny double doors...)"
    K "(And find a bento box tucked away in the corner.)"
    K "(In response, my stomach starts rumbling like never before.)"
    K "Argh...I shouldn't take someone else's food..."
    K "(However, my empty stomach says otherwise.)"
    K "..."
    K "They wouldn't mind, right?"
    K "(I sheepishly take out the lunch box and open the lid...)"
    K "Another note?"

    #Write Kei note 3

    K "How strange..."
    K "(I wasn't really interested in the note, but the food in the container)"
    K " munch munch"
    K "...!"
    K "That's delicious!"
    K "(I immediately scarf down the rest of the food, not leaving even a single grain of rice.)"

    scene bg black
    play sound "bell.wav" volume 0.5
    
    jump current