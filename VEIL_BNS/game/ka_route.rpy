
label search_kanye:

    $ ka_route = True

    P "I should look for Kanye."
    P "She might still be lingering somewhere..."
    P "(I head over to the only place I know she might be.)"

    scene bg black

    stop music fadeout 1.0

    $ renpy.play("audio/stepping.mp3", channel="sfx1")

    scene bg noon library with dissolve

    P "(I slide open the door and...)"

    $ renpy.play("audio/sliding_door.mp3", channel="sfx1")

    scene bg noon hallway with dissolve

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
            P "Uh, Kanye..."
            P "Shouldn't we be looking for your keychain?"

            show kanye emb

            Ka "Oh yeah..."

            show kanye smile

            Ka "Haha, I think I might've yapped on forever if you hadn't stopped me."
            pass

        "Let her yap":

            Ka "His laid-back personality is so relatable!"
            Ka "Honestly, it's because of pompompurin that I'm especially fond of caramel pudding."
            Ka "Although he's in the spotlight, it's important to mention his best friends...)"
            Ka "Muffin the hamster, Scone the mouse, and Custard the bird!"
            Ka "I'd say they are the most iconic group in the history of, well, anything!"

            P "(Kanye takes a moment to catch her breath after spending 10 minutes gushing about the cartoon dog.)"

            pass

    show kanye neutral 2

    Ka "Anyway…"

    show kanye neutral

    Ka "Let’s head to the schoolyard."
    Ka "I think that was the last time I had it."

    scene bg black with fade

    P "(Kanye and I head to the yard, scanning for any sign of a plush keychain every step of the way.)"

    scene bg schoolyard with dissolve

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

    hide kanye with easeoutleft

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

    scene bg bedroom with dissolve

    P "I didn’t expect a person like Kanye…"
    P "To be into such an out-of-character interest."
    P "You can’t judge a book by its cover, I guess."

    scene bg black with fade

    jump ka_thursday_morning

label ka_thursday_morning:

    scene bg black

    $ renpy.play("audio/clock.mp3", channel="sfx1")

    P "Ugh…"
    P "Time to get ready, I guess."
    P "(I cook myself a simple sunny side up egg for breakfast…)"
    P "(And prepare myself for another day.)"

    scene bg hood with dissolve

    P "(I drowsily walk through my neighborhood, trying to keep myself awake every step of the way…)"
    "...!"

    if kei == 3:
        
        call meet_neighbour


    else:
        pass

    P "What was that?"
    P "It's was like everything froze for a second…"
    P "(I take a minute to process the awkward sensation when my phone suddenly lights up.)"
    P "...!"
    P "It’s nearly 8:30!"
    P "I might not get the chance to see Kanye before class!"
    P "(I immediately pick up the pace and run to school as fast as I can.)"

    scene bg black

    #scene school_gates_bg
    
    P "(I unexpectedly see a familiar face at the school gates.)"

    play music "BTS.mp3"

    show kanye neutral 
    P "Kanye?"

    show kanye startled
    Ka "...!"
    Ka "[name_input]! You’re here!"

    show kanye smile
    Ka "What took you so long?"

    show kanye laugh

    Ka "Did you wake up late or something?"

    P "Ah, sorry..."
    P "I didn’t know you were waiting for me."

    show kanye smile

    Ka "Of course I was!"
    Ka "It’s no fun being in the library when you’ve already read every book…"

    show kanye emb

    Ka "...twice."

    P "Pfft…"
    P "(I try to hold myself back, but a few chuckles escape.)"

    show kanye blush
    Ka "!!!"

    show kanye angry

    Ka "Shuddup."
    Ka "You would’ve done the same thing if you saw our school’s surprisingly tiny selection."

    show kanye neutral

    P "Hahaha…alright, alright."
    P "(We both make our way inside the entrance.)"

    scene bg hallway

    Ka "...Hey, [name_input]-kun…"
    P "Yeah?"

    Ka "You’ve seen the D*nqi in the shopping district, right?"
    P "Ah, I haven’t had time to really explore the area."
    P "There’s a D*nqi here?"

    show kanye smile

    Ka "Yeah, not too far from the school."
    Ka "If you want, we can check it out together after school."

    P "Oh yeah, that sounds great."
    P "But what’s with the sudden topic?"

    show kanye startled

    Ka "Uh…"
    Ka "Well, the thing is…"

    show kanye emb

    Ka "There are some new limited edition H*llo K*tty plushies in D*nqi…"
    Ka "And I wanted to check it out."

    P "..."

    show kanye hes
    Ka "You’d still like to come with me, right?"

    P "..."
    P "Of course I do."

    show kanye smile

    stop music
    Ka "ahah…"

    play music "spirited.mp3"

    P "(Without warning, a sharp pain suddenly hits my shoulder.)"

    show kanye angry

    P "Ouch!"
    P "What was that for!?"

    Ka "For being rude to me, you bully."

    play sound "stepping.mp3"

    P "(She swiftly runs off, giggling.)"

    P "H-hey!"
    P "Wait up!!"

    play sound "stepping.mp3"

    P "(I hurry after Ka, who was still laughing.)"

    scene bg black

    return