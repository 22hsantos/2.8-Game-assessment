
label search_kagaku:

    $ ka_route = True

    P "I should look for Kagaku."
    P "She might still be lingering somewhere..."
    P "(I head over to the only place I know she might be.)"

    scene bg black

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

    return