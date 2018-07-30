label day7:

window hide
hide black
with fade

e "You wake up abruptly."

play sound "sounds/Knock.mp3"

e "There is a knock on the door."

menu:
    "Answer the door.":
        pass

show p h

p h "Hello sir!"

menu:
    "Hello?":
        p h "Good morning!"
        pass

    "What's going on?":
        pass

p h "It's Peggy Day!"

menu:
    "Peggy day?":
        pass

    "Right, {w=0.15}Peggy day.":
        pass

p s "Sir.{w=0.15}.{w=0.15}. D-.{w=0.15}.{w=0.15}. do you not celebrate Peggy day?"

menu:
    "I don't know what it is.":
        pass

    "No. I hate Peggy day.":
        p su "What?!"
        pass

p h "Oh sir! My apologies! It's my favorite holiday!"

p h "It's celebrates the historic day in 2013 that scientists discovered our Peggy!"

menu:
    "Still don't know what Peggy is.":
        pass
    "Okay.":
        pass

p h "Peggy was the start to everything!"

p n "It just showed up, {w=0.15}and we assumed it was a moon to Saturn."

p s "You really don't know the story?"

p n "They thought it was just a moon to Saturn."

p n "But, {w=0.15}it was our first contact with Chalcogenium."

menu:
    "With what?":
        pass

p n "Sir.{w=0.15}.{w=0.15}. y-you aren't familiar? I suppose it's old technology now, {w=0.15}but still.{w=0.15}.{w=0.15}."

p n "It's the main reason we're able to survive out in space."

p n "It produces oxygen out of carbon dioxide. "

p n "At a rate over one-hundred times faster than any other known method. "

p n "In fact, {w=0.15}most of the interior of this ship is built out of it to supplement the engine."

menu:
    "How does it work?":
        pass

    "Oh, neat.":
        jump pastExp
        pass

p s "Oh.{w=0.15}.{w=0.15}. w-well, {w=0.15}Haruka would be able to explain better than me."

p n "B-but, {w=0.15}I know that we we owe our existence to it!"

p n "It directly led to us being able to build and sustain Station 001."

p n "If we hadn't had at least Station 001 built by the time of The Shred, {w=0.15}humans would most likely not have survived onward as a species."

p h "To me, {w=0.15}Peggy day is the start of a new history for the human race. "

p n "The day we started on our path from earthlings to something more."

label pastExp:

e "Hei walks out into the hallway."

play sound "sounds/DoorOpen2.mp3"

show r h:
    linear 0 xalign 0.9 yalign 1.0

r h "Hey dude, {w=0.15}Nema."

r n "Sup?"

show p h

p h "Hei, {w=0.15}good morning!"

p n "I was just telling our Captain about Peggy day. "

p n "He was completely unaware!"

show r s

r s "Peggy day?"

show p su

p su "W-.{w=0.15}.{w=0.15}. what? You as well?"

show r s

r s "I guess so..?"

show p h

p h "It's a national holiday!"

show r m

r m "If I didn't get a day off from the academy for it, {w=0.15}chances are it wasn't enough of a holiday for me to care."

show p m

p m "Unbelievable!"

p s "Then, {w=0.15}uhm, {w=0.15}well.{w=0.15}.{w=0.15}."

p n "C-captain, {w=0.15}would it be OK if I.{w=0.15}.{w=0.15}."

p s "Well, {w=0.15}I mean."

p s "Could we have a, {w=0.15}uhm.{w=0.15}.{w=0.15}."

menu:
    "What?":
        p n "What would you think of a Peggy day Celebration tonight? I'll set everything up on my own, {w=0.15}it will be no hassle sir, {w=0.15}I promise."
        pass

    "A celebration?":
        p h "Yes!"
        pass

p n "I can teach everyone more about the history of our greatest holiday, {w=0.15}and it will give everyone a much needed chance to relax a bit. I think it's a great opportunity, {w=0.15}but if you disagree I completely understand."

menu:
    "Sure.":
        pass

    "No, {w=0.15}we can't spare the time.":
        pass

p h "S-sir! Thank you so much! I'll set it all up sir, {w=0.15}no worries!"

p h "I even brought my board game on the mission in preparation!"

p h "I thought I might miss celebrating this year, {w=0.15}thank you so much!"

p h "I'll get started right away! We can start the celebration at dinnertime, {w=0.15}until then, {w=0.15}please allow me to take hold of the kitchen!"

show r su

r su "Uh, {w=0.15}wow. I've never seen you so excited for something."

show p n

p n "Oh, {w=0.15}uhm.{w=0.15}.{w=0.15}."

show r h

r h "I like it."

e "Nema smiled."

show p h

p h "I'll see you both tonight!"

p h "Thank you again Captain!"

e "Nema runs off into her room."

hide p

show r su:
    linear 0.5 xalign 0.5 yalign 1.0

r su "Huh. "

r s "I hope this party doesn't turn out to just be a lecture."

show y h:
    linear 0 xalign 0.9 yalign 1.0

y h "What party?"

show r s

r s "Oh, {w=0.15}h-hey."

show y n

y n "Hey, {w=0.15}what party?"

menu:
    "We're having a Peggy day celebration tonight.":
        pass

    "Some party Nema's throwing.":
        pass

y h "Oh, {w=0.15}Peggy day? Hell yeah."

y n "It's been a shit couple of days, {w=0.15}that sounds nice."

menu:
    "I'm surprised you think so.":
        y su "Oh?"

        y s "Yeah I guess I've been a bit rough lately, {w=0.15}sorry."

        show r h

        r h "No problem my dude! I totally understand."

        show y n

        y n "Yep."
        pass

    "I agree!":
        pass

show r h

r h "You wanna go grab some breakfast?"

show y n

y n "Nah, {w=0.15}I was just poppin' out to see what the commotion was about."

y n "I'm gonna hole up in my room so I can get a bit of work done to make up for the party tonight."

y h "See ya Dump, {w=0.15}later Cap."

show r s

r s "Dump?"

r n "Are you calling me Dump?"

show y h

y h "Eh."

e "Haruka shrugs and starts to walk away."

y n "Wait."

y s "Is Nema putting this party on?"

menu:
    "Yeah.":
        pass

y m "This is just gonna be an hour of freaking lectures isn't it."

y s "Ugh."

hide y

play sound "sounds/DoorOpen2.mp3"

e "Haruka disappears into her room."

play sound "sounds/DoorClose2.mp3"

show r s

r s "I guess I should go do work or whatever too."

r h "You should drop by later for some games though."

r n "Later man."

play sound "sounds/DoorClose2.mp3"

hide r

e "You have some free time.{w=0.15}.{w=0.15}."

define day7Hei = True

define day7Haru = True

label day7FreeTime:
    
call hall from _call_hall_33

if day7Hei or day7Haru:
    menu:
        "Haruka's Room" if day7Haru:
            $ day7Haru = False
            call yellowRoom from _call_yellowRoom_4
            jump day7HarukaRoom
            pass
        "Hei's Room" if day7Hei:
            $ day7Hei = False
            call redRoom from _call_redRoom_7
            jump day7HeiRoom
            pass
else:
    call blueRoom from _call_blueRoom_14
    jump partyTime

label day7HarukaRoom:

show y n

y n "Oh hey Cap, {w=0.15}what's up?"

menu:
    "Just checking on progress.":
        y h "Always on top of things, {w=0.15}nice."
        pass

    "Just saying hi.":
        y h "Hi."
        y s "But, well."
        pass

y n "I've got tons to do before tonight if I want some free time."

y s "So,{w=0.15} gotta focus, {w=0.15}sorry Cap."

hide y

jump day7FreeTime

label day7HeiRoom:

show r h

r h "Hey!"

r m "What do you think you're doin?"

menu:
    "You said to drop by for games.":
        pass

    "Checking in.":
        pass

r m "You're trying to spy on my strategy."

r m "I haven't forgotten about our rematch."

r h "Two more days."

menu:
    "Rematch?":
        pass

    "Oh yeah.":
        pass

r h "Damn right. {w=0.15}I'm gonna beat you this time."

r m "Now GET OUT."

hide r

jump day7FreeTime

label partyTime:

call blueRoom

e "Seems like everyone is busy."

e "You spend some time checking your computer."

label summariesD7:

menu:#computer
    "I'll read the summaries.":
        label summariesD7:
        menu:
            "Haruka's summary.":
                call day7HaruS
                jump summariesD7
                pass
            "Hei's summary.":
                call day7HeiS
                jump summariesD7
                pass
            "Nema's summary.":
                call day7NemaS
                jump summariesD7
                pass
            "I think I'm done.":
                jump day7Mid
                pass                
        pass

    "I'm going to respect their privacy.":
        jump day7Mid
        pass

label day7Mid:

play sound "sounds/Knock.mp3"

e "There's a knock on your door."

play sound "sounds/DoorOpen2.mp3"

call hall from _call_hall_34

show y h

y h "Hey Cap! It's party time."

y n "Ya ready for a lifetime of lectures?"

show r h:
    linear 0 xalign 0.9 yalign 1.0

r h "Guys, {w=0.15}we can just pretend we fell asleep."

r n "Nema would be alright, {w=0.15}right?"

menu:
    "We're going, {w=0.15}she was excited.":
        pass

    "Yeah, {w=0.15}maybe she'd be fine without us.":
        y s "Nah, c'mon, we have to go."
        pass

r h "I know, {w=0.15}I know."

show y s

y s "Sleeping would probably be more exciting."

show r n

r n "You were right though, let's just throw her a bone."

play sound "sounds/DoorOpen2.mp3"

e "Haruka opens the door to the kitchen."

call kitchen from _call_kitchen_10

show y su

y su "What the-"

show p h:
    linear 0 xalign 0.1 yalign 1.0

p h "Hey!{w=0.15} G-{w=0.15}guys! "

p su "*hic*"

p h "Ya maaaaade it."

p h "Heh."

show r su

r su "Nema are you drunk?"

show p su

p su "What?! "

p m "{b}NOT ME.{/b}"

e "Nema leans in close."

p h "I might{w=0.45} be a little {w=0.25}drunk."

p m "Shhh."

show y h

y h "I take back everything I said.{w=0.15} This party's gonna be amazing."

show p h

p h "You're{w=0.15} am{w=0.1}azing!"

p n "And{w=0.15} so pretty, {w=0.15}and sm{w=0.15}art."

p n "You're so good at the.{w=0.15}.{w=0.15}. the leading."

p h "Even better{w=0.15} than{w=0.15} the captain."

p su "But"

p m "{b}DON'T{/b}"

p n "tell"

p h "him."

show y h

y h "Hahaha, {w=0.15}you gonna take that Cap?"

menu:
    "Nema show some respect.":

        pass

    "Somehow, {w=0.15}I'm not insulted.":
        pass

show p n

p n "Delightful."

show r su

r su "What?"

show p su

p su "What?"

p h "Come on, {w=0.15}sit sit sit!"

show r n

r n "Alright, {w=0.15}alright, {w=0.15}sitting."

e "Hei and Nema sit together,{w=0.15} Haru by you on the outside."

show p h

p h "Now party!"

show y n

y n "What?"

show p n

p n ".{w=0.15}.{w=0.15}."

show r n

r n "Uhh."

e "Nema looks directly into Hei's eyes."

show p n

p n "Now."

e "She put her hand on his."

p m "{size=-4}{i}Party.{/i}{/size}"

show r su

r su "Uhm, {w=0.15}well, {w=0.15}I, {w=0.15}uh.{w=0.15}.{w=0.15}."

show p h

p h "Pschhh.{w=0.15}.{w=0.15}.{w=0.15} Hehe."

show r h

r h "Oh, {w=0.15}that was a joke?"

menu:
    "Nema are you OK?":
        pass

    "Nema, {w=0.15}you're not OK.":
        pass

show p n

p n "I am O-{w=0.25}oaky{w=0.15}.{w=0.15}.{w=0.15}.{w=0.25} sir."

p n "Please."

p n "Do no{w=0.15}t worry."

show y h

y h "Convincing."

show r su

r su "So.{w=0.15}.{w=0.15}. what do we do here Nema?"

show p n

p n "How about a board game?"

p h "Please, {w=0.15}let's play a{w=0.15} board game."

show y h

y h "Didn't see that one coming, {w=0.15}what with the board game being out and set up and the only thing you have appeared to actually set up with your entire day of preperation."

show r su

r su "No, {w=0.15}we're missing a piece on our side?"

show p su

p su "What? No, {w=0.15}I had them all{w=0.15} out."

p n "Did you move{w=0.15} it?"

p m "You {i}snake.{/i}"

show r h

r h "Hah, {w=0.15}nope, {w=0.15}sorry to say it was already gone."

show p n

p n "I like that."

p h "Hei you are{w=0.15} always honest and I.{w=0.35} Like.{w=0.35} That."

e "Nema puts her arm around Hei."

show r su

r su "Oh, {w=0.15}hi there."

show p h

p h "Hi.{w=0.15} Heh.{w=0.25} Heh."

show y h

y h "Nema please don't laugh like that."

show p n

p n "Oh.{w=0.15}.{w=0.15}."

p h "Heh."

show y n

y n "Alright, {w=0.15}come on. What do you normally do on Peggy day that you love so much?"

show p n

p n "Normally? "

p s "Well this is not{w=0.15} normally."

p s "Normally I'd be at home, {w=0.15}with my family."

show y n

y n "Right.{w=0.15} And?"

show p n

p n "And{w=0.15} we wou{w=0.15}ld play {w=0.15}games."

show y m

y m "Like?"

show p h

p h "My brothers{w=0.15}*hic*{w=0.15} always had some{w=0.15}thing new to play."

p n "They were{w=0.15} the fun ones."

p s "I am{w=0.15} not the fun one."

show y m

y m "Yes, {w=0.15}I've realized this."

show r s

r s "Come on Haruka."

show y n

y n "I'm trying Hei.{w=0.15} I'm trying so hard."

show r m

r m "You're not trying, {w=0.15}you're putting her down."

show y h

y h "Well she's making it hard to do anything else right now."

show r m

r m "That's not fair, {w=0.15}she's obviously not used to doing this sort of thing."

show y m

y m "Yes, {w=0.15}obviously.{w=0.15} That's what I was saying."

show p m

p m "That's what she was {i}saying.{/i}"

show r s

r s "I'm on your side, {w=0.15}Nema."

show p h

p h "Awww."

e "Nema smiles and gives Hei a hug."

p h "What{w=0.15} a sweetie-pie."

show r su

r su "Oh."

show y h

y h "Hahaha"

show r su

r su "Shut up.{w=0.25} Let me switch seats with you."

show y m

y m "Hell no."

show p h

p h "Haruka I'll{w=0.15} sit by{w=0.15} you!"

e "Nema let out a little wink."

show r s

r s "Cap I don't think I feel right sitting here right now."

show y m

y m "Hell no to that too.{w=0.15} I'm not sitting by you."

show r m

r m "Fine, {w=0.15}you know, {w=0.15}I don't even know why I care."

show p su

p su "Woah, {w=0.15}{b}grumps.{/b}"

show y m

y m "Seriously."

show r m

r m "No, {w=0.15}I don't even know how to be on your side Haruka, {w=0.15}why do you make it so hard?"

show y n

y n "Because I don't really like ya?"

menu:
    "Haruka be nice.":
        y h "I'm being nice. Nobody likes to be led on."
        pass

    ".{w=0.15}.{w=0.15}.":
        pass

y n "He has a right t'know how I feel."

show r m

r m "More like you wont even let me have a chance."

show p m

p m "Yeah, {w=0.15}ruude!"

show r m

r m "I'm done. {w=0.15}Nema's cuter anyways."

menu:
    "Is this a conversation to have while we're all here?":
        pass

    "Well then.":
        pass

show y h

y h "HAH.{w=0.15} Alright."

show p h

p h "Hei!"

p su "You.{w=0.15}.{w=0.15}.{w=0.25} {i}love{/i} me."

show r s

r s "Ha, {w=0.15}oh, {w=0.15}well.{w=0.15}.{w=0.15}."

r n "I like you Nema, {w=0.15}how about that."

show p s

p s "{size=-6}You love me.{/size}"

e "Nema stuck her tongue out at Haruka."

show y h

y h "Alright happy couple, {w=0.15}what are we doing?"

show p m

p m "We're going to{w=0.15} sit here and argue."

show y n

y n "Already done, {w=0.15}next?"

show r n

r n "What did you and your brothers do?"

show p h

p h "My brothers{w=0.15} would set up a bo{w=0.15}ard game, {w=0.15}or Mahjong in the living room, {w=0.15}and we'd all sit down and just play and talk and eat and laugh."

p n "That's{w=0.15} what we will{w=0.15} do."

show y n

y n "I'd play some Mahjong, {w=0.15}do you have a set?"

show p n

p n "In{w=0.15} my room."

show y h

y h "Alright great."

y s ".{w=0.15}.{w=0.15}."

y n "So.{w=0.15}.{w=0.15}."

show p n

p n "Yes?"

show y h

y h "Go get it?"

show p m

p m "No."

show y n

y n "Oh. Great."

y s "I think I'm going to bed."

show r su

r su "Wait. {w=0.15}Why can't we use it Nema?"

show p h

p h "Hei!"

e "Nema smiles and nuzzles up to him."

show r h

r h "Ahaha, {w=0.15}easy."

show p n

p n "Because {w=0.15}it's my brothers set and I never asked{w=0.15} if I could{w=0.15} use it."

show r n

r n "Then why do you have it?"

show p n

p n "I got it when they{w=0.15} died."

show y n

y n "So you don't really have to ask to use it then, {w=0.15}do you?"

show p s

p s "It's not for playing.{w=0.25} I haven't{w=0.15} asked."

show y m

y m "Alright then I'm going to bed. "

menu:
    "Nema, {w=0.15}there's no way we could \"ask them\"?":
        pass

    "Let's just use the set anyways.":
        pass

show r n

r n "Yeah, {w=0.15}what if we try to talk to them?"

show p su

p su "B-but, {w=0.15}I.{w=0.15}.{w=0.15}. we can't{w=0.15} anymore."

show y m

y m "Are you guys talking about communicating with spirits? Really?"

show r n

r n "Yes.{w=0.25} Do you want to try Nema."

show p m

p m "Wha-{w=0.15}.{w=0.15}.{w=0.15}. N-{w=0.15}no!"

show r su

r su "Huh?"

show p s

p s "No, {w=0.15}no no no."

menu:
    "Why not?":
        pass

    "Alright.":
        pass

p s "They'll get{w=0.15} mad.{w=0.15} N-{w=0.15}no."

e "Nema starts to tear up."

show r su

r su "Woah hey, {w=0.15}c'mon you, {w=0.15}stop.{w=0.15}.{w=0.15}. that."

r s "Uhm."

e "Hei looks at you with fear in his eyes."

menu:
    "Nod.":
        pass

    "Look back with fear.":
        pass

r su "Uhhh.{w=0.15}.{w=0.15}."

e "Hei wraps his arm around Nema."

r n "It's OK. I'm sure they don't hate you."

show p s

p s "No, {w=0.15}they do, {w=0.15}I know."

show r n

r n "Right. {w=0.25}We won't do that then."

show p s

p s "They hate{w=0.15} me, {w=0.15}no."

p s "I don't want to{w=0.15} play anymore."

show y m

y m "Alright, {w=0.15}it's official, {w=0.15}I'm out of here.{w=0.15} I have a ton of work to do and this is ridiculous."

menu:
    "Alright.":
        pass

    "You sure?":
        pass

y n "G'night Cap."

hide y

e "Haruka walks out."

play sound "sounds/DoorOpen2.mp3"

e "Nema continues to sniffle into Hei's shoulder."

show r h

r h "I guess I can take care of her, {w=0.15}you can go on."

menu:
    "Okay.":
        pass

    "I'll help.":
        pass

r n "See you in the morning."

menu:
    "Good luck.":
        pass
        
hide r

hide p
        
play sound "sounds/DoorClose2.mp3"        
    
call hall from _call_hall_35

e "You pass by Haruka in the hall."

show y m

y m "{i}Geesh.{/i}"

play sound "sounds/DoorClose2.mp3"

hide y

window hide
show black
with fade

e "Her door closes and you head into your room and go to bed."

e ".{w=0.15}.{w=0.15}."

call blueRoom from _call_blueRoom_15

return