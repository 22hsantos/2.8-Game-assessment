
label search_kanye:

    $ ka_route = True

    P "I should look for Kanye."
    P "She might still be lingering somewhere..."
    P "(I head over to the only place I know she might be.)"

    scene bg black

    stop music fadeout 1.0

    $ renpy.play("audio/stepping.mp3", channel="sfx1")

    #scene afternoon_library_bg

    P "(I slide open the door and...)"

    $ renpy.play("audio/sliding_door.mp3", channel="sfx1")

    #scene afternoon_hallway_bg

    P "..."
    P "She's not here..."
    P "(All the suspense died down in an instant, as I stood there alone.)"
    P "...Maybe she went home."
    P "I should go home too."
    P "(I turn around in defeat, when suddenly I hear rapid footsteps growing louder and louder.)"

    play music "BTS.mp3"
    
    show kanye sil at scale_sprite

    Ka "[name_input]-kun?"

    show kanye startled with dissolve

    Ka "What are you doing at school this late?"

    show kanye neutral

    P "(I sheepishly reply)"
    P "...I fell asleep."

    show kanye startled

    Ka "..."

    show kanye laugh

    Ka "Pfft, Bahaha!"
    Ka "I can't believe you fell asleep until this late, haha!"
    Ka "I hope you didn't drool on your desk too!!"

    P "(I just stood there in silent embarrassment, taking every ridicule she threw at me.)"

    show kanye smile

    Ka "Hahaha..."
    Ka "I haven't laughed that hard in a while."

    P "Are you done now?"

    Ka "..."
    Ka "Mhm."

    P "You can't say much..."
    P "Why are you still at school this late?"

    show kanye startled

    Ka "...!"

    show kanye hes

    Ka "..."
    Ka "I lost something important this morning."

    P "(Seeing her sudden change in emotion made me lose all annoyance I had towards her.)"
    P "Oh..."
    P "Uh, what was it?"

    P "(Kanye stands in silence, trying her best to answer my question)"
    P "(She quietly mumbles an answer, then darts her eyes to me.)"
    P "Um... what was that?"

    Ka "...A H*llo K*tty Plush keychain."

    P "(I freeze.)"
    P "H*llo K*tty? The cartoon character for kids?"

    show kanye angry

    Ka "It's not just for kids!"
    Ka "It's... um..."

    P "(I cut her off)"
    P "Hey, it's okay if you are a fan of things like these..."
    P "I think it's quite cute."

    show kanye blush

    Ka "...You don't think I'm being childish by liking things like these?"

    P "(I warmly smile at her.)"
    P "Of course not."
    P "In fact, I think that yellow dog one is cute—"

    show kanye excited

    Ka "P*mpompurin??"

    P "(Seeing her excited and nerdy expression fills my heart with a strange warmth.)"

    Ka "I know right?"
    Ka "His yellow fur looks so suuuper soft and—"

    menu:
        "Interrupt her":
            #jump interrupt_kanye
            pass

        "Let her yap":
            #jump let_her_yap
            pass

    show kanye neutral 2

    Ka "Anyway…"

    show kanye neutral

    Ka "Let’s head to the schoolyard."
    Ka "I think that was the last time I had it."

    scene bg black with fade

    P "(Kanye and I head to the yard, scanning for any sign of a plush keychain every step of the way.)"

    #scene schoolyard_bg with dissolve

    P "Was the school yard always this big…?"
    P "I thought a bright cat keychain would’ve been easy to spot."

    show kanye hes at scale_sprite

    Ka "What if someone stole it?"

    P "(Kanye drops her head down.)"
    P "There’s no way someone could’ve stolen such a precious item—"
    P "(Unexpectedly, a bright object in the corner of my eye catches my attention.)"
    P "...Is that it?"

    show kanye excited

    P "(Kanye swiftly turns her head towards the direction I was looking.)"
    Ka "That’s it!"

    hide kanye

    Ka "(I watch her bolt to the object and pick it up)"

    show kanye excited at scale_sprite

    Ka "[name_input]-kun, you found it!"

    P "(Her expression couldn’t be any brighter.)"
    P "(Though it was getting dark, her smile could’ve paralleled the sun.)"

    Ka "I can’t thank you enough, [name_input]-kun."

    P "...It’s no big deal."
    P "You can ask for my help anytime."

    scene bg black with fade

    P "(Kanye shot me another smile…"
    P "(This time, a whole lot warmer.)"
    P "(After exchanging our goodbyes, we both parted to our houses.)"

    #scene bedroom_bg with dissolve

    P "I didn’t expect a person like Kanye…"
    P "To be into such an out-of-character interest."
    P "You can’t judge a book by its cover, I guess."

    scene bg black with fade

    jump current