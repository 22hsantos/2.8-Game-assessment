
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

    play music "LEASE.mp3"

    P "(I drowsily walk through my neighborhood, trying to keep myself awake every step of the way…)"
    "...!"

    if kei == 3:
        
        call meet_neighbour from _call_meet_neighbour


    else:  
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

    show kanye neutral at scale_sprite

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

    P "Hahaha… alright, alright."
    P "(We both make our way inside the entrance.)"

    scene bg hallway

    show kanye neutral at scale_sprite

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

    show kanye hes

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

    Ka "For being rude to me earlier, you bully."

    #run sfx
    $ renpy.play("audio/stepping.mp3", channel="sfx1")

    show kanye laugh

    hide kanye with easeoutleft

    P "(She swiftly runs off, giggling.)"

    P "H-hey!"
    P "Wait up!!"

    $ renpy.play("audio/stepping.mp3", channel="sfx1")

    P "(I hurry after Kanye, who was still laughing.)"

    scene bg black

    jump ka_thursday_midday

label ka_thursday_midday:

    $ renpy.music.set_volume(0.5, channel="sfx1")
    $ renpy.play("audio/bell.wav", channel="sfx1")
    $ renpy.music.set_volume(1, channel="sfx1")

    scene bg classroom

    #bgm

    P "Hmm…"
    P "I’m not that hungry—"

    stop music
    $ renpy.play("audio/sliding_door.mp3", channel="sfx1")
    show kanye neutral at scale_sprite

    Ka "Um, excuse me!"

    P "(All the students turn their head to Kanye’s sudden entrance.)"

    "Classmate 1" "Woah… It’s president Takashi-san…!"
    "Classmate 2" "I wonder why she’s here, she rarely visits classrooms…"

    Ka "Is [name_input] in this class?"

    P "(In an instant, everyone’s gaze turns to me.)"
    P "Ah… I’m here."

    Ka "Perfect, come with me."
    Ka "I have business to discuss with you."

    hide kanye neutral with easeoutleft

    $ renpy.music.set_volume(1.5, channel="sfx1")
    $ renpy.play("audio/stepping.mp3", channel="sfx1")

    P "(The room falls silent, my footsteps being the only sound there is.)"
    P "(However, I can hear glimpses of my classmates’ chatter as I pass by)"

    "Classmate 1" "What if he did something bad and got in trouble…?"
    "Classmate 2" "I didn’t know the new kid was such a delinquent…"

    scene bg black
    $ renpy.play("audio/stepping.mp3", channel="sfx1")
    pause 2.0
    scene bg hallway with dissolve
    show kanye neutral at scale_sprite

    P "Did… did I do something wrong?"

    show kanye smile

    Ka "Hm? What are you talking about?"

    P "Like, what made you call for me in such a formal manner?"

    show kanye emb

    Ka "Oh no, no!"
    Ka "You misunderstand me."

    show kanye smile

    Ka "I was just wondering if you’d like to join me for lunch?"

    P "..."
    P "(I couldn’t believe that she called me out in front of my whole class…)"
    P "(Because she wanted to invite me to lunch?)"
    P "Geez, why did you have to sound so scary?"

    show kanye neutral 2

    Ka "Well, I am still the Student Council President…"

    show kanye neutral

    Ka "And that means I have to keep up appearances."

    show kanye hes
    #show kanye sad

    Ka "I do apologise if it seemed that way though…"
    Ka "Sometimes, I cannot control my tone."

    P "No, it’s okay."
    P "I know you don’t mean it…"
    P "So, about lunch?"

    show kanye smile

    Ka "Yes, lunch!"
    Ka "We have to go to the rooftop."

    P "Huh? The rooftop—"

    scene bg black with fade

    #run sfx?

    play music "spirited.mp3"

    P "(Before I knew it, Kanye had already dragged me through several flights of stairs…)"

    scene bg staircase at bg with dissolve

    P "*Huff* H-hold up!!"
    P "(Kanye didn’t seem to acknowledge my cries of resistance…)"

    scene bg rooftop with dissolve

    pause 1.0

    Ka "So? How’s the view?"

    hide kanye

    scene bg rooftop view at bg_pan
    with dissolve
    pause

    if rooftop:
        P "..."
        P "(I gaze out at the view once again.)"
        P "I came here on my first day, too..."
        P "But its luster hasn't disappeared one bit."
        P "It's beautiful."

        pass

    else:
        #play music "calm3.mp3"

        P "Woah...!"
        P "What a view..."
        P "(I walk closer to the fence, looking down at the whole city.)"
        P "Everything looks so small from up here."
        Ka "I know, right?"
        P "(We both spend a moment enjoying watching people live their everyday lives.)"

        pass

    P  "(Suddenly, I notice Kagaku pulling a couple of boxes from her schoolbag.)"

    show kanye smile at scale_sprite

    Ka  "Let’s sit down and eat, shall we?" 

    if cafe > explore:

        P "Oh, I usually eat at the cafeteria..."
        P "So I actually don't have anything to eat right now."

        show kanye neutral

        Ka "Yeah, I noticed."

        P "?"

        Ka "I caught glimpses of you eating in the lunchroom for the past couple of days."
        
        pass

    else:

        P "Oh, I rarely eat lunch..."
        P "So I actually don’t have anything to eat right now."

        show kanye neutral

        Ka "Yeah, I noticed."
        P "?"

        Ka "I often saw you wandering around at lunchtime ever since you got here."

        pass

    Ka "So I thought I could make you a lunch."

    show kanye neutral

    P "(She gently unwraps an unexpectedly cute P*mpompurin bento box.)"
    P "Woah!"
    P "(She wasn’t joking about being into this stuff…)"
    P "(I open the pudding-patterned lid.)"
    P "..."
    P "This is so…"
    P "(I carefully examine the composition of the bento, admiring the fine details…)"
    P "(I was particularly impressed by the omelette that was in the shape of the iconic yellow dog.)"

    Ka "..."

    show kanye hes

    Ka "What are you waiting for?"

    show kanye neutral

    Ka "Dig in."

    show kanye eat

    P "(Kanye mercilessly rips apart her intricate creation.)"
    P "(I contemplated for a moment about if I should even destroy something so cute…)"
    P "(But the protests of my stomach left me no choice.)"
    P "Sorry, P*mpompurin…"

    hide kanye with dissolve

    P "(I reluctantly bring my chopsticks closer, and dig in.)"
    P "...!"
    P "This is delicious!"
    P "(I dart a look at Kanye, who was elated at my remark.)"

    show kanye blush at scale_sprite

    Ka "Thanks."

    show kanye emb

    P "No, thank you."

    scene bg black with fade

    $ renpy.music.set_volume(0.5, channel="sfx1")
    $ renpy.play("audio/bell.wav", channel="sfx1")
    $ renpy.music.set_volume(1, channel="sfx1")

    jump ka_thursday_noon

label ka_thursday_noon:

    $ renpy.music.set_volume(0.5, channel="sfx1")
    $ renpy.play("audio/bell.wav", channel="sfx1")
    $ renpy.music.set_volume(1, channel="sfx1")

    scene bg noon classroom with fade

    P "(As I pick up my belongings and walk out of the classroom, I see a certain council president leaning on the wall across from me.)"

    show kanye smile at scale_sprite

    play music "BTS.mp3"

    Ka "[name_input]."

    show kanye neutral

    Ka "What took you so long?"
    
    Ka "I figured that you had slept in the classroom again, haha."

    P "(I playfully groan)"
    P "I only fell asleep once…!"

    show kanye laugh

    Ka "Ahaha!"

    show kanye smile

    Ka "You never know…"
    Ka "It could be one of many."

    show kanye neutral

    Ka "Anyway…"
    Ka "Shall we go to D*nki?"

    P "(I give her a warm smile.)"

    show kanye blush

    P "We shall."

    show kanye smile

    Ka "Pfft."

    scene bg black with fade

    P "(After walking a few blocks, we had arrived at the D*nquixote.)"

    show kanye excited at scale_sprite

    Ka "Ah!"
    Ka "[name_input]-kun!"
    Ka "I see the new releases!!"

    #scene store with fade

    P "(In the blink of an eye, Kanye grips onto my hand and drags me straight to the S*nrio store.)"

    Ka "Oh my goodness…"
    Ka "They’re all so adorable!!"
    Ka "[name_input]-kun, do you see how cute they are!?"

    P "(I was still trying to catch my breath from what felt like an Olympic sprint.)"
    P "(On the other hand, Kanye didn’t even look like she broke a sweat.)"
    P "*Huff* *Huff*"

    show kanye hes

    Ka "[name_input]-kun?"
    Ka "Are you alright?"

    P "Yeah, I’m fine…"
    P "*Huff* Just catching my breath."
    P "(As soon as my breathing slowed, I shot up to look at the plushies.)"
    P "Oh yeah, they’re quite cute."

    show kanye smile

    Ka "I know, right?"

    P "(Kanye takes a plush out of the mountain of merchandise on the shelf.)"

    show kanye excited

    Ka "Should I get this one?"
    Ka "Or this one??"

    show kanye emb

    Ka "Ugh, I can’t decide!"
    Ka "I’d love to take them all home!"

    P "(Kanye plops herself cross-legged on the floor.)"
    P "Um..."
    P "I guess I’ll let you have a think, then?"

    P "(At this point, Kanye had already tuned me out.)"
    P "(I watch her mumble to herself, analyzing the various plushies in front of her.)"
    P "Ookay."
    P "(Speechless, I wander off into a different aisle.)"

    hide kanye with dissolve

    P "(Gazing at all the shelves of cutesy hair accessories, nothing particularly catches my eye...)"
    P "(Until I come across a particular hair bow.)"
    P "Huh..."
    P "This must be the bow that H*llo K*tty wears."
    P "Kanye would be ecstatic if she saw this."
    P "I’d love to see the look on her face."
    P "..."
    P "..."

    P "(Without a word, I pick up the item and stealthily step to the front.)"

    #play sound "money.wav"

    P "(After the cashier hands me back a paper bag, I make my way back to Kanye.)"
    P "(To my surprise, she was still sitting on the floor, a different expression this time.)"

    show kanye hes at scale_sprite

    P "Picked something yet, Kanye?"

    Ka "No..."
    Ka "But I’m concerned about the size of these plushies."
    Ka "My mother would never let me bring one of these home."
    Ka "She thinks my interests are too childish for someone my age."

    P "(She perks her head down at the pitiful plush in her hands.)"
    P "Damn, that sucks..."

    P "(I carefully scan the piles on the shelf, and take a small one out of the corner.)"
    P "How about this one?"
    P "Your mom surely wouldn’t notice."

    #show kanye intrigued

    Ka "Yeah… my mother wouldn’t mind something small."

    show kanye smile

    P "(Kanye shoots me a childish grin.)"
    Ka "Thanks, [name_input]-kun."

    P "(I accompany Kanye as she buys the small fluffy companion...)"
    P "(Which oddly had its own charm due to its small size.)"

    #play sound "money.wav"

    #scene outside_afternoon with fade

    hide kanye with dissolve

    P "Ever since we left the store, Kanye hadn't taken her eyes off the toy for a second."
    P "(She clutched it tightly, as if it were the most precious thing in the world.)"

    Ka "..."

    P "(I was hesitant for a moment, but I finally decided muster up the courage to reach into my pocket.)"
    P "Hey, Kanye..."

    show kanye neutral at scale_sprite

    Ka "Yes?"

    P "I got you something."
    P "I saw it in the store and thought you might like it."
    P "She looks down at the small pink bow in my hand."

    pause 1.0
    show kanye startled

    Ka "!!!"

    Ka "This is..."
    Ka "For me?"

    P "Yeah."

    Ka "I… I don’t know what to say."

    show kanye blush

    Ka "Thank you so much, [name_input]-kun."
    Ka "I love it so much."

    show kanye smile

    "(Kanye fastens the bow onto her hair, beaming with joy.)"

    Ka "It looks so cute!"
    Ka "..."

    show kanye hes

    Ka "..."
    Ka "I wish I could wear this every day."

    P "Well..."
    P "What's stopping you?"

    Ka "I..."
    Ka "What would everyone think of me if they saw me wearing something like this?"    
    Ka "Something so childish would be inappropriate."
    Ka "I’m the Student Council President, after all..."

    P "(I gently cut her off.)"
    P "So?"
    P "Who cares what other people think?"
    P "Liking cute things doesn't make you any less mature."
    P "It's not like your interests take away from the fact that you're a dependable student council president."

    Ka "..."

    #slight smile

    Ka "You're right."
    Ka "I think I needed to hear that."

    show kanye smile

    Ka "...I'll make sure to wear this tomorrow."

    hide kanye with easeoutleft

    P "(We continue walking around the shopping district, chatting about random things...)"
    P "(When suddenly, I spot an oddly eye-catching bookstore in the corner of my eye.)"
    P "Hey, Kanye..."
    P "Do you want to check out that bookstore?"

    show kanye neutral at scale_sprite

    Ka "That one?"

    show kanye smile

    Ka "Sure!"

    hide kanye with easeoutleft

    #bookstore bg

    show kanye neutral at scale_sprite

    Ka "Actually, this is my favorite bookstore."
    Ka "I come here all the time."

    P "Oh yeah?"

    Ka "Yeah."
    Ka "Since I was a kid, I've always loved reading."
    Ka "I used to come here with my dad all the time, since it was close to our house."
    Ka "He would always buy me a new book whenever we came here."
    Ka "He thought it would keep me busy..."

    show kanye laugh

    Ka "But I'd always end up reading them all in one sitting!"

    show kanye neutral

    Ka "I got it from him, I guess."

    P "Yeah, I can see that."
    P "Actually..."

    if book == True:
        menu:
            "I have a book for you.":
                $ renpy.call_in_new_context("give_book")

            "What book do you recommend?":
                jump current
    else:
        menu:
            "What book do you recommend?":
                pass
    
    Ka "What do I recommend?"
    Ka "..."
    Ka "Personally, I like 'The very sleepy c*terpiller'"
    Ka "I know it's childish..."
    Ka "But my father always used to read it to me as a kid."
    Ka "It was one of my favourite moments with him..."

    show kanye hes

    Ka "Before I lost him..."
    Ka "I wonder what he would think if he saw me now."
    Ka "..."
    Ka "Sorry."
    
    show kanye neutral

    Ka "I didn't mean to bring the mood down."

    P "No."

    show kanye startled

    P "You don't have to apologise."
    P "I'm glad that you can open up to me about these things."
    P "And I'm really happy that you trust me enough..."

    menu:

        "Because..."

        "I really like you.":
            jump good_ending

        "I also see you as a close friend.":
            jump bad_ending

label good_ending:

    play musice "end.mp3"

    Ka "..."
    Ka "I..."

    show kanye neutral

    Ka "I don't know what to say."
    Ka "We've only met this week..."
    Ka "But..."
    Ka "I can't deny that I also have an interest in you."

    show kanye smile

    Ka "Thank you so much, [name_input]-kun."
    Ka "Thank you for giving me the courage to do the things I couldn't before."
    Ka "And express myself without being ashamed."
    Ka "Thank you..."

    hide kanye

    "Good Ending."

    return

label bad_ending:
    
    show kanye hes

    Ka "...Oh."
    Ka "Is that so."

    if kei == 3:

        stop music

        Ka "Is it because of her?"
        Ka "she always manages to slip her way back in."
        Ka "Like some kind of cockroach."
        Ka "I think she spread her disgusting cockroach aura to you."
        
        hide kanye
        show blank at scale_sprite

        Ka "We need to clean you..."
        Ka "Now."

        $ persistent._clear()
        $ renpy.quit()

    else:
        Ka "I see."
        Ka "..."
        Ka "I just remembered I had an errand to run."
        Ka "I have to go."
        Ka "Sorry."

        hide kanye with easeoutleft

        "Bad end"

        return 



label give_book:

    stop music

    hide kanye
    show blank at scale_sprite

    pause 0.1

    show kanye startled at scale_sprite

    Ka "..."
    Ka "What"
    Ka "Did"
    Ka "You"
    Ka "Say"

    menu:
        "Repeat what you said":
            jump repeat_response

        "Say nothing":

            Ka "..."
            Ka "Okay."

            $ os.remove(file_path4)
            $ book == False

            #kanye runs off into the sunset with Elon Musk

            return

label repeat_response:  

    hide kanye
    show blank

    Ka "..."
    Ka "So she's still here."
    Ka "Looks like I didn't do a thorough enough cleaning."
    Ka "I guess I'll have to patch up again..."
    Ka "How annoying."
    Ka "Oh well."
    Ka "Goodbye, [name_input]-kun. "

    show kanye smile at scale_sprite   

    Ka "Please come back once I've fixed up this game, alright?"

    $ persistent._clear()
    $ renpy.quit()    
