# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#aligns sprite to centre and sizes up

init python:

    #allows to interact with the operating system


    import time 
    import os
    import sys
    import ctypes

    def is_admin():


        try:
            return ctypes.windll.shell32.IsUserAnAdmin()

        except Exception:
            return False
            get_admin()
    

    #replace with VEIL_BNS.exe
    def get_admin():
        
        #absolute path to renpy
        renpy_path = os.path.abspath("renpy.exe")

        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, os.path.abspath("renpy.exe"), None, 1
        )
        sys.exit()#terminates the session

    #note file paths
    file_path1 = os.path.join(renpy.config.basedir, "game", "2025.txt")
    file_path2 = os.path.join(renpy.config.basedir, "game", "PLEASE_READ.txt")
    file_path3 = os.path.join(renpy.config.basedir, "game", "3.txt")

    #file path list
    file_path_list = [file_path1 , file_path2 , file_path3]
    
    #checks if each file exists
    for path in file_path_list:

        file_exists = os.path.exists(path)

        if file_exists:
            try:
                os.remove(path)

            except FileNotFoundError:
                pass


    is_admin()

    #why is not working
    config.has_autosave = False
    config.has_quicksave = False

    #gets the player's name
    player_name = os.getlogin()

    #counts the number of Kei notes
    kei = 0

    #determines whether the player is stupid or not
    player_normal = False

    #Default name for player
    name_input = "Daquan Tamil"


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
define P = Character("[name_input]")
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

    $ admin = is_admin()

    if admin:
        "Have admin perms"
    
    else:
        "No admin perms"
        
        $ is_admin()


    "Checkpoint Shortcut active."
    "Currently, saving the game is not possible due to coding issues"
    "oops lol"
    "dont save the game pls (it will break)"

    stop music


    $ renpy.call_in_new_context("file_write")

    jump file_write

    #jump story_start

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

    P "(My name is [name_input].)"
    P "(I’m a third year high school student that has recently transferred to another school.)"
    P "(Why you ask?) "
    P "(I have no idea either.)"
    P "(I have dementia.)"
    P "(I have no idea why or how I got it though.)"
    P "(Probably cause' I have dementia.)"
    P "(...)"
    P "(I’ll just start getting ready for my first day.)"

    play music "LEASE.mp3"
    scene bg hood with dissolve
    
    P "I’ve only moved here a few days ago… "
    P "But I have to admit this neighbourhood is way better than my last one."
    P "the amount of sleep I’ve lost because of those damn barking dogs was enough to drive me insane."
    P "Maybe that's why I have dementia..."

    play sound "stepping.mp3"

    P "(...)"

    stop sound
    scene bg black at bg
    stop music

    P "Wait…"
    P "(Did I forget my house keys??)"

    play music "spirited.mp3"

    P "(I frantically start searching through my uniform pockets, trying to find my keys.) "
    P "Argh, not in the right one… "
    P "(my expression tenses up as I found my right pocket empty.)"
    P "(Hopefully, luck is on my side and my missing house key was in my left pocket…)"
    P "C’mon, c’mon…!"
    P "(...)"

    stop music

    play sound "sad_trombone.mp3"
    P "(I left my house keys at home.)"
    P "(I let out a long disappointed sigh of defeat.)"
    P "(But oddly enough, there was a note I didn’t remember putting in my pocket...)"

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
                
                P "Huh, I can’t even read this… "
                P "It’s all random measurements."
                P "(I disregard the note and continue walking to my new school.)"

            else:
                P "What the heck..."   

                scene bg hood
                play music "LEASE.mp3"
                P "Huh, I can’t even read this… "
                P "It’s all random measurements."
                P "(I disregard the note and continue walking to my new school.)"

        "Leave it alone.":
            P "Ehh..."
            P "I can open it later."
            P "(I disregard the note and continue walking to my new school.)"
    

    jump monday_morning

label monday_morning:
    scene bg hallway with dissolve
    play music "sincememo.mp3"
    play sound "stepping.mp3"

    P "(I was admiring my surroundings while strolling through the hallway.)"
    P "(It was like everywhere I saw was masterpiece painted by renowned painters.)"
    P "(After a while, I found myself in front of a familiar feeling door.) "
    scene bg outside library at bg ,with dissolve
    P "Ah."
    P "This must be the library."
    P "(I was relieved to see a school library so similar to mine.)"
    P "(That even though I’m in a new place, I'd still have a place to run away and escape reality.)"
    P "(I gently slid open the door.)"

    scene bg black
    play sound "stepping.mp3"

label monday_kanye:

    P "(...)"

    P "(The Glass Atlas)"
    P "(Chronicles of a Vanished Kingdom)"
    P "(Where the Shadows Dream)"
    P "Woah…"
    P "This library has a great selection of books."
    P "(I couldn’t contain my excitement as I was indulging in my dearly missed paradise.)"
    P "I wonder if they have-"

    stop sound
    stop music
    play sound "bamboo.ogg"

    P "...!"

    play sound "crash.ogg"

    uk "Oof!"

    scene bg library
    show kanye sil at scale_sprite
    play music "spirited.mp3"

    uk "Hey."
    uk "Watch where you’re going."

    show kanye angry with dissolve

    P "Oh! I’m sorry…"
    P "I didn’t see you there."

    show kanye neutral 

    uk "*sigh*"
    uk "It’s fine."

    play music "BTS.mp3"

    uk "I’ve never seen you around before."
    uk "Are you new?"

    P "(I’m startled at her sharp observation.)"
    P "Y-yeah, how did you know?"

    uk "I’m the student council president, so I know my peers quite well."
    uk "Allow me to welcome you to Hoshizora Academy…"

    P "Ah, [name_input]."

    Ka "[name_input]-kun. My name is Takahashi Kanye."
    P "Taka…Takaha-"

    show kanye neutral 2

    Ka "*Sigh*"
    Ka "Kanye is fine."

    show kanye neutral at scale_sprite

    P "Thank you very much, Kanye."

    P "(I could feel the tension set in as soon as it fell silent.)"
    P "(My eyes quickly dart around the room, as to keep the already dead conversation going.)"
    P "(Suddenly, I recognize the book that was in Kagaku’s hand.)"
    P "(It was *Echoes in the Fog*, a classic thriller novel that was popular upon release.)"
    P "(However, popularity has dwindled in the recent years, so it quickly became a niche.)"
    P "Hey…"

    show kanye startled at scale_sprite

    P "Is that *Echoes in the Fog*?"

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

    P "(I’m left speechless at the sudden switch from a fanatic bookworm to a composed president)"
    P "(...)"
    P "I guess I’ll go too…"

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

    P "(I’m left speechless at the sudden switch from a fanatic bookworm to a composed president)"
    P "(...)"
    P "I guess I’ll go too…"

    scene bg black
    jump classroom_scene

label classroom_scene:
    #scene bg classroom

    P "I’ve got nothing to do right now."
    P "I should..."

    menu:
        "Eat at cafeteria":
            jump monday_cafeteria

        "Explore the school":
            jump monday_rooftop
        
label monday_cafeteria:
    P "I should get something to eat."
    P "I didn't have time to eat breakfast after all."

    scene bg black
    play music "cafeteria.mp3"
    scene bg cafeteria at bg ,with fade

    P "(As soon as I stepped into the cafeteria, a heavenly scent wafted to my nose.)"
    P "(Was that... curry?)"
    P "(I couldn't help but chase after the source, and taste what might've smelled like the best food I'd have in my entire life.)"
    scene bg black
    stop music
    play sound "bell.wav" volume 0.5

    jump monday_afterschool

label monday_rooftop:

    P "I wonder what the view up on the rooftop is like."

    scene bg black

    scene bg staircase at bg
    play sound "stepping.mp3"

    P "(I find myself stepping up what might've been the longest staircase of my entire life.)"
    P "*Huff* *Huff*"
    P "How big..."
    P "Is this..."
    P "Goddamn school...!?"

    scene bg black

    play sound "sliding_door.mp3"

    pause 1.5

    scene bg rooftop with dissolve
    
    play music "rooftop.mp3"

    P "Woah...!"
    P "What a view..."
    P "(I stepped closer to the fence, looking down the whole city.)"

    scene bg rooftop view at bg_pan
    with dissolve
    pause

    P "Everything looks so small from up here."
    
    scene bg black

    P "(I spend a moment enjoying watching people live their everyday life before going back to class.)"

    stop music
    play sound "bell.wav" volume 0.5

    jump monday_afterschool

label monday_afterschool:
    play sound "bell.wav" volume 0.5
    scene bg afterschool with fade
    pause 3.0
    play music "TOL.mp3"

    P "*Yawn*"
    P "That class had me beat."
    P "How am I supposed to be on the same level as everyone else, anyway?"
    P "This is literally my first day here!"
    P "..."
    P "Whatever, I’m going home."

    scene bg black with dissolve
    play sound "stepping.mp3" volume 1.5

    P "(Hmm? What’s all that noise?)"
    P "(I look around, and find that the source of the commotion has been coming from the school gym.)"
    P "(Guess I might check it out, I guess.)"

    scene bg gym with fade

    P "(It seems that the basketball club had some activities today.)"
    P "(I stick around for a while, watching the players do their drills.)"
    P "(I blankly stare at a ball that came out of nowhere.)"
    P "(Hey, isn’t that ball coming straight towards my—)"

    stop music
    play sound "punch.mp3"
    scene bg black

    P "*Thud!*"
    P "(An inexplicable pain started radiating from my forehead.)"
    P "(I could feel all the blood rushing as the red mark started thumping non-stop.)"

    uk "Oh my gosh! Are you okay!?"

    P "(I open my eyes to find a girl standing right in front of me.)"

    uk "Ahh, what do I do??"
    P "Huh…"
    P "(I manage to open my eyes.)"

    scene bg gym with dissolve
    play music "spirited.mp3"
    show travis worried at scale_sprite

    uk "Um!"
    uk "How many fingers am I holding!?"

    P "What…?"
    P "(I try to readjust my vision.)"

    show travis fingers at scale_sprite

    uk "I said how many fingers am I holding??"

    P "Uhh…"

    menu:
        "2":
            jump normal
        "7":
            $ player_normal = False
            jump concussed

label normal:
    P "Um, 2?"
    
    show travis excited at scale_sprite

    uk "Thank god!"
    uk "You didn't lose any brain juice!"
    jump monday_travis

label concussed:
    P "Um, 7?"

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
    P "(The peculiar girl reaches out her hand.)"

    scene black

    P "(Hup!)"

    scene bg gym

    show travis neutral at scale_sprite
    
    P "Thanks…"

    show travis smile at scale_sprite

    uk "Don’t mention it!"


    show travis shocked at scale_sprite

    uk "Ah!"

    show travis embarrassed at scale_sprite

    uk "I never told you my name, did I…"

    show travis neutral at scale_sprite

    P "Ah, same here."
    P "I’m [name_input]."

    T "I’m Sato Travis."

    show travis smile at scale_sprite

    T "But everyone just calls me Travis."

    P "(I become rigid for a moment.)"
    P "Ah! Are you sure?"

    show travis confused at scale_sprite

    T "What’s the matter?"
    P "It’s just… we’ve just met and—"

    show travis proud at scale_sprite

    T "Hah!"
    T "So what?"
    T "Everyone I meet, I consider my closest friends!"

    P "Um, okay… if you say so."

    T "But enough about that!"

    show travis embarrassed at scale_sprite

    T "Is your head okay? You took a really hard hit."

    P "(She tries to reach her hand out to me once again to examine my forehead when…)"

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

    P "(And another one runs away…)"
    P "*sigh*"
    P "I think I’ve had enough exploring for my first day here."
    P "I’m gonna head home."

    scene bg black
    jump monday_bedroom

label monday_bedroom:

    P "(I hurried home before the sun set.)"

    #scene bg bedroom

    P "(While I was a bit overwhelmed with the events that happened today, I was glad I made two new friends.)"
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

    P "(My eyelids started lifting the moment the sun hit my eyes.)"

    #scene bg bedroom
    play music "ROB.mp3"

    P "Argh… Morning already?"
    P "(I groggily put on my uniform and gather my things.)"
    P "Okay, time to go to—"

    stop music

    P "(I suddenly put my hand over my right pocket.)"

    play music "ROB.mp3"

    P "*Sigh* Thank god I remembered this time…"
    P "I don’t want to ever climb in through the window again."
    P "Hopefully no one saw me, I’d die of embarrassment."
    P "Well, I’m off."

    play music "LEASE.mp3"
    scene bg hood with dissolve
    play sound "stepping.mp3"

    P "I wonder if I’ll see Kanye again."
    P "She seems a bit odd, but I’m glad to have another book-buddy."
    P "Travis too."
    P "I hope she treats me today, that ball did leave a bruise after all."
    P "It took forever to stop the swelling…"

    scene bg black

    P "(As soon as I arrived inside the school entrance, I immediately headed straight for the library.)"

    scene bg outside library at bg ,with dissolve

    P "(Here goes nothing...)"

    scene bg black
    scene bg library

    play music "BTS.mp3"
    show kanye neutral at scale_sprite

    Ka "Oh!"
    Ka "[name_input]-kun."

    #show kanye smile

    Ka "Good morning."

    P "Ka…Kagaku-san..."

    #show kanye laugh

    Ka "Hahaha!"

    show kanye neutral

    Ka "Just Kanye is fine."
    Ka "It’s a bit odd if you add -san to my first name."

    P "(My cheeks grow a bit pink from embarrassment.)"

    Ka "How are you today?"

    P "I’m pretty alright, thanks."
    P "How about you?"

    #show kanye hesitated

    Ka "I’m… alright, thank you."

    P "(I sense the slight hesitation in her words.)"
    P "Is… something wrong?"

    show kanye startled at scale_sprite

    Ka "Ah! It’s nothing. It’s just…"

    #show kanye hesitated
    show kanye neutral

    Ka "..."
    Ka "I’ve just taken a lot of responsibilities at once since we’re starting the school year."
    Ka "And I’ve just been a bit stressed while organising that and other things too."

    P "(A wave of empathy washes over me as I continue to listen to her troubles.)"
    P "Woah, sounds tough on you."

    show kanye startled

    Ka "No! Not at all! I can handle it myself."

    #show kanye hesitated

    Ka "I just need a little time, that’s all."

    P "(A sense of doubt and concern hits me, but I try to encourage Kanye.)"
    P "Alright, just…"
    P "Tell me if you need anything, okay?"

    #show kanye startled

    Ka "..."

    #show kanye smile

    Ka "Thank you, [name_input]-kun."
    Ka "That means a lot to me."

    play sound "bell.wav" volume 0.5

    pause 3.0

    show kanye neutral
    Ka "What a shame, I guess I’ll have to see you later?"

    P "Yeah, later."

    hide kanye
    scene bg black

    jump tuesday_midday

label tuesday_midday:
    play sound "bell.wav" volume 0.5

    #classroom bg

    P "I've got nothing to do right now."
    P "I should..."

    menu:
        
        "eat at the cafeteria":
            jump tuesday_cafeteria
        
        "Explore the school":
            jump tuesday_theatre
    
label tuesday_cafeteria:
    
    P "I should go to the cafeteria."
    P "I *am* feeling a bit hungry."

    scene bg black

    P "(I make my way to the cafeteria once again, curious for what's on the menu today.)"

    play music "cafeteria.mp3"

    scene bg cafeteria

    P "...!"
    P "(I expected a delicious smell to greet me like yesterday...)"

    stop music

    P "(But today's meal took a total 180 degree turn.)"

    play music "spirited.mp3"

    P "Ugh...what is this smell?"
    P "(It was an indescribable smell.)"
    P "(The closest I could get to describing this is physical assault...)"
    P "(But to my nose.)"
    P "(Yeah, no.)"
    P "(I guess it's no lunch for me today.)"

    scene bg black
    stop music
    play sound "bell.wav" volume 0.5

    jump tuesday_afterschool

label  tuesday_theatre:  

    P "I should check out the theatre."
    P "A school this rich would have an impressive theatre, right?"

    scene bg black
    
    P "(I made my way to the theatre, admiring it's beautiful design)"

    #Theater BG

    P "Woah..."
    P "I haven't been one for plays but-"
    P "Looking at a theatre this extravagant might just get me into it."

    play sound "bell.wav" volume 0.5

    jump tuesday_afterschool

label tuesday_afterschool:

    play sound "bell.wav" volume 0.5

    scene bg afterschool with fade
    pause 3.0
    play music "TOL.mp3"

    P "*Sigh*"
    P "I still don’t get a lot of what they’re teaching but—"
    P "I think I made a lot of progress."
    P "(I feel myself zoning out for a few seconds.)"
    P "..."
    P "(*growl*)"
    P "Ah."
    P "Travis was supposed to treat me today."
    P "Honestly, I forgot about that."
    P "But thinking about it now has gotten me quite excited."
    P "I should go find her."

    scene bg black with fade

    P "(I head over to the school gym, my stomach pounding like it was playing some kind of desperate symphony.)"

    play sound "stepping.mp3"
    scene bg gym with dissolve

    P "(To my surprise, there was no rowdy commotion this time.)"
    P "(It seems like the basketball club had to leave early.)"
    P "(Though, there were a bunch of basketballs scattered all over the ground…)"
    P "(And a tight-lipped girl knelt down in the middle, gathering all of the balls.)"
    P "(I make my way towards her, planning to offer my help but—)"

    show travis shocked at scale_sprite

    T "KYAH!"
    P "Woah!"
    T "Who’s the—"
    T "Oh!"

    show travis tense at scale_sprite

    T "It’s just you, [name_input]."
    P "Yeah…"
    P "Sorry for startling you."
    P "You sounded quite shocked, haha…"
    P "(I nervously laugh, trying to brush off the crushing guilt weighing upon me.)"

    show travis embarrassed at scale_sprite

    T "No, no."

    show travis s smile at scale_sprite

    T "It’s fine."

    show travis smile at scale_sprite

    T "Just, forget about how loud I screamed!"

    show travis embarrassed at scale_sprite

    T "That was like, super embarrassing…"
    P "Yeah, of course."

    show travis anxious at scale_sprite

    P "(It fell silent for what felt like eternity.)"
    P "Um!"
    P "What are you doing here, all alone?"
    P "Where’s the rest of the club?"

    show travis tense at scale_sprite

    T "Oh…"
    T "They… um"

    show travis sad at scale_sprite

    T "Had other things to do."
    P "(I become concerned at her tense demeanor.)"
    P "Well—"

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

            P "Hey, I don't mind at all..."
            P "And I don't think you're a bad senpai."

            T "..."

            show travis s smile at scale_sprite
            
            T "Thanks, [name_input]."
            T "I'm glad to hear that."
            
            pass

    P "..."
    T "..."
    P "(Travis turns away from you to wipe her face with her sleeve, before facing you again.)"

    show travis smile at scale_sprite

    T "Tomorrow I’ll treat you to a suuper delicious meal, okay?"

    show travis embarrassed at scale_sprite

    T "So, please don’t think bad of me!"

    show travis smile at scale_sprite

    T "Haha..."

    show travis s smile at scale_sprite

    P  "(Despite her best attempts at putting on a smile, her softly creased eyebrows gave everything away.)"
    P "(I try my best not to put down the mood.)"
    P "Haha, of course not."
    P "And sure, I’ll hold you to that…"
    P "Okay?"

    show travis smile at scale_sprite

    T "Okay…!"

    scene bg black with fade
    P "(Shortly after I helped her clean up the gym, we parted ways at the school gates.)"

    jump tuesday_bedroom

label tuesday_bedroom:

    #scene bedroom with dissolve

    P "I hope Travis’s okay…"
    P "She was super bright when I first met her yesterday."
    P "Kanye, too."
    P "The start of a new year might’ve put too much pressure on both of them."

    P "(As I was finishing changing into my pajamas, I was getting ready to slip under my covers...)"
    P "(Suddenly, I nearly slip as I stepped on a mysterious object.)"
    P "Ah!"
    P "Huh? What is this?"
    P "Another piece of paper…"

    menu:
        "Open it":

            P "(I examine the paper closer)"

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

                    file_exists = os.path.exists(file_path2)

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

            P "Butter?"
            P "Flour?"
            P "Milk?"
            P "Huh, must’ve ripped off mom’s cooking books…"
            pass
        
        "Leave it":
            pass
        
    P "I carelessly throw the paper into the corner of the room..."
    P "Then dozed off under the sweet embrace of my warm blanket."

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

    P "... "

    #play sound "alarm_clock.ogg"

    P "Five more minutes…"

    #play sound "alarm_clock.ogg"

    P "I said, I more—"

    #scene bedroom_bg with dissolve

    play music "spirited.mp3"

    P "(My eyes fly open.)"
    P "Oh crap, oh crap, oh crap!"
    P "(I scramble under my covers trying to find my phone.)"
    P "There it is!"
    P "..."
    P "8:55!?"
    P "(I quickly leap out of my bed and start throwing my uniform on.)"
    P "I’m going to be late!"

    #scene black with fade

    scene bg hood with dissolve

    P "*Huff* *Huff*"

    scene bg black with fade

    #scene classroom_bg with dissolve

    stop music

    P "Sorry, I came late!"
    P "(As soon as I opened my eyes, I felt a whole class of unfamiliar faces staring at me…)"
    P "(I quickly dart my gaze over to my teacher…)"
    P "(But was met with a stranger.)"

    #scene black

    P "(This wasn’t my class.)"
    P "(I immediately bowed my head in embarrassment and guilt.)"
    P "Sorry for the interruption!!!"
    P "(I slammed the door shut and went to my actual classroom.)"
    P "Not even a week here, and I might already be called a weirdo…"

    jump wednesday_midday

label wednesday_midday:
    
    #scene bg classroom

    P "I've got nothing to do right now."
    P "I should..."

    menu:
        "Eat at cafeteria":
            jump wednesday_cafeteria

        "Explore the school":
            jump wednesday_club

label wednesday_cafeteria:

    P "I should go to the cafeteria."
    P "Maybe this time will be better..."
    P "Third time's the charm, right?"
    P "(I hesitantly tread over to the lunchroom.)"

    scene bg black

    P "(To my surprise, there was no smell indicating the quality of the food this time.)"
    P "...Is that good or bad?"
    P "..."
    P "Eh, at least there's a chance that I won't succumb from biological warfare."
    P "(I take a closer look at what was on the menu...)"

    scene bg cafeteria
    play music "cafeteria.mp3"

    P "Huh?"
    P "What is that..."
    P "Is that even food...?"
    P "It's literally a grey blob."
    P "(After a moment of contemplating my life choices, I take a big gulp and try the miscellaneous substance.)"
    P "..."
    P "It was meh."

    play sound "bell.wav" volume 0.5

    scene bg black
    jump current

label wednesday_club:

    P "I should explore the clubs here."
    P "Besides..."
    P "I don't think I have an appetite from what I witnessed yesterday."

    scene bg black

    P "(I start walking around the clubrooms, fascinated by the range of activities each club hosted.)"
    P "(One club in particular caught my eye...)"
    P "The cooking club, huh..."
    P "(Not to brag, but I personally think I'm a pretty good cook.)"
    P "(I do live alone after all, and take out would drain my money quite fast.)"

    #Cooking club BG

    P "Woah!"
    P "This school must be pretty rich to have a commercial kitchen this nice!"
    P "Am I in M*sterChef??"
    P "(I spend a second in awe of the breathtaking workstations.)"
    P "(I don't know why, but I was strangely drawn to specifically the fridge.)"
    P "(I walk over and swing open the shiny double doors...)"
    P "(And find a bento box tucked away in the corner.)"
    P "(In response, my stomach starts rumbling like never before.)"
    P "Argh...I shouldn't take someone else's food..."
    P "(However, my empty stomach says otherwise.)"
    P "..."
    P "They wouldn't mind, right?"
    P "(I sheepishly take out the lunch box and open the lid...)"
    P "What the hell"
    P "Another note?"

    menu:
        "Open it":

            P "(I examine the paper closer)"

            python:

                #Kei file 3
                with open(file_path3, "w") as file:
                    
                    message_3 ="""
                    
                    Thank you again for allowing me to repair VEIL: Beneath The Surface.
                    I am deeply regretful that you had to experience the game in such a
                    unfinished state.
                    I prepared this lunch as a an apology and a sign of my gratitude.
                    I hope you like it :)
                    
                    -Kei
                    
                    """

                    file.write(message_3)
                    file.close

                    file_exists = os.path.exists(file_path3)
                
            if file_exists:
                python:
                    os.system(f'notepad.exe {file_path3}')
                    ctypes.windll.user32.MessageBoxW(None,
                    "Unexpected file interference! Please select OK to continue with the game.", 
                    "Oh No!",
                    48
                    )
                    os.system("taskkill /IM notepad.exe /F")

                    kei = kei + 1


    P "How strange..."
    P "(I wasn't really interested in the note, but the food in the container)"
    P " munch munch"
    P "...!"
    P "That's delicious!"
    P "(I immediately scarf down the rest of the food, not leaving even a single grain of rice.)"

    scene bg black
    play sound "bell.wav" volume 0.5
    
    jump current