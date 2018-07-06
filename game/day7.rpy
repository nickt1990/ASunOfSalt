label day7:

e "There is a knock on the door."

menu:
    "Answer the door.":
        pass

show p h

p h "Hello sir!"

menu:
    "Hello?":
        pass

    "What's going on?":
        pass

p h "It's Peggy Day!"

menu:
    "Peggy day?":
        pass

    "Right, Peggy day.":
        pass

p s "Sir... D-... do you not celebrate Peggy day?"

menu:
    "I don't know what it is.":
        pass

    "No. I hate Peggy day.":
        pass

p h "Oh sir! My apologies! It's my favorite holiday!"

p h "It's celebrates the historic day in 2013 that scientists discovered our Peggy!"

menu:
    "Still don't know what Peggy is.":
        pass

p h "Peggy was the start to everything!"

p n "It just showed up, and we assumed it was a moon to Saturn."

p s "You really don't know the story?"

p n "They thought it was just a moon to Saturn."

p n "But, it was our first contact with Chalcogenium."

menu:
    "With what?":
        pass

p n "Sir... y-you aren't familiar? I suppose it's old technology now, but still..."

p n "It's the main reason we're able to survive out in space."

p n "It produces oxygen out of carbon dioxide. "

p n "At a rate over one-hundred times faster than any other known method. "

p n "In fact, most of the interior of this ship is built out of it to supplement the engine."

menu:
    "How does it work?":
        pass

    "Oh, neat.":
        pass

p s "Oh... w-well, Haruka would be able to explain better than me."

p n "B-but, I know that we we owe our existence to it!"

p n "It directly led to us being able to build and sustain Station 001."

p n "If we hadn't had at least Station 001 built by the time of The Shred, humans would most likely not have survived onward as a species."

p h "To me, Peggy day is the start of a new history for the human race. "

p n "The day we started on our path from earthlings to something more."

e "Hei walks out into the hallway."

play sound "sounds/DoorOpen2.mp3"

show r h:
    linear 0 xalign 0.9 yalign 1.0

r h "Hey dude, Nema."

r n "Sup?"

show p h

p h "Hei, good morning!"

p n "I was just telling our Captain about Peggy day. "

p n "He was completely unaware!"

show r s

r s "Peggy day?"

show p su

p su "W-... what? You as well?"

show r s

r s "I guess so..?"

show p h

p h "It's a national holiday!"

show r m

r m "If I didn't get a day off from the academy for it, chances are it wasn't enough of a holiday for me to care."

show p m

p m "Unbelievable!"

p s "Then, uhm, well..."

p n "C-captain, would it be OK if I..."

p s "Well, I mean."

p s "Could we have a, uhm..."

menu:
    "What is it?":
        pass

    "A celebration?":
        pass

p n "What would you think of a Peggy day Celebration tonight? I'll set everything up on my own, it will be no hassle sir, I promise."

p n "I can teach everyone more about the history of our greatest holiday, and it will give everyone a much needed chance to relax a bit. I think it's a great opportunity, but if you disagree I completely understand."

menu:
    "Sure.":
        pass

    "No, we can't spare the time.":
        pass

p h "S-sir! Thank you so much! I'll set it all up sir, no worries!"

p h "I even brought my board game on the mission in preperation!"

p h "I thought I might miss celebrating this year, thank you so much!"

p h "I'll get started right away! We can start the celebration at dinnertime, until then, please allow me to take hold of the kitchen!"

show r su

r su "Uh, wow. I've never seen you so excited for something."

show p n

p n "Oh, uhm..."

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

r s "Oh, h-hey."

show y n

y n "Hey, what party?"

menu:
    "We're having a Peggy day celebration tonight.":
        pass

    "Some party Nema's throwing.":
        pass

y h "Oh, Peggy day? Hell yeah."

y n "It's been a shit couple of days, that sounds nice."

menu:
    "I'm surprised you think so.":
        pass

    "I agree!":
        pass

y su "Oh?"

y s "Yeah I guess I've been a bit rough lately, sorry."

show r h

r h "No problem my dude! I totally understand."

show y n

y n "Yep."

show r h

r h "You wanna go grab some breakfast?"

show y n

y n "Nah, I was just poppin' out to see what the commotion was about."

y n "I'm gonna hole up in my room so I can get a bit of work done to make up for the party tonight."

y h "See ya Dump, later Cap."

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

e "You have some free time..."

define day7Hei = True

define day7Haru = True

label day7FreeTime:
    
call hall

if day7Hei or day7Haru:
    menu:
        "Haruka's Room" if day7Haru:
            $ day7Haru = False
            call yellowRoom
            jump day7HarukaRoom
            pass
        "Hei's Room" if day7Hei:
            $ day7Hei = False
            call redRoom
            jump day7HeiRoom
            pass
else:
    call blueRoom
    jump partyTime

label day7HarukaRoom:

show y n

y n "Oh hey Cap, what's up?"

menu:
    "Just checking on progress.":
        pass

    "Just saying hi.":
        pass

y h "Always on top of things, nice."

y n "I got tons to do before tonight if I want some free time though."

y s "Gotta focus, sorry Cap."

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

r h "Damn right. I'm gonna beat you this time."

r m "Now GET OUT."

hide r

jump day7FreeTime

label partyTime:

e "Seems like everyone is busy."

e "Check your computer in order to work on your own project."

e "Check computer, time skips."

e "There's a knock on your door."

play sound "sounds/DoorOpen2.mp3"

call hall

show y h

y h "Hey Cap! It's party time."

y n "Ya ready for a lifetime of lectures?"

show r h:
    linear 0 xalign 0.9 yalign 1.0

r h "Guys, we can just pretend we fell asleep."

r n "Nema would be alright, right?"

menu:
    "We're going, she was excited.":
        pass

    "Yeah, maybe she'd be fine without us.":
        pass

r h "I know, I know."

show y s

y s "Sleeping would probably be more exciting."

show r n

r n "Let's just throw her a bone, c'mon."

e "Haruka opens the door to the kitchen."

play sound "sounds/DoorOpen2.mp3"

call kitchen

show y su

y su "What the-"

show p h:
    linear 0 xalign 0.1 yalign 1.0

p h "Hey! G-guys! "

p su "*hic*"

p h "Ya maaaaade it."

p h "Heh."

show r su

r su "Nema are you drunk?"

show p su

p su "What?! "

p m "NOT ME."

e "Nema leans in close."

p h "I might be a little drunk."

p m "Shhh."

show y h

y h "I take back everything I said. This party's gonna be amazing."

show p h

p h "You're amazing!"

p n "And so pretty, and smart."

p n "You're so good at the... the leading."

p h "Even better than the captian."

p su "But"

p m "DON'T"

p n "tell"

p h "him."

show y h

y h "Hahaha, you gonna take that Cap?"

menu:
    "Nema show some respect.":
        pass

    "Somehow, I'm not insulted.":
        pass

show p n

p n "Delightful."

show r su

r su "What?"

show p su

p su "What?"

p h "Come on, sit sit sit!"

show r n

r n "Alright, alright, sitting."

e "Hei and nema sit together. Haru by you on the outside."

show p h

p h "Now party!"

show y n

y n "What?"

show p n

p n "..."

show r n

r n "Uhh."

e "Nema looks directly into Hei's eyes."

show p n

p n "Now."

e "She put her hand on his."

p m "Party."

show r su

r su "Uhm, well, I, uh..."

show p h

p h "Pschhh... Hehe."

show r h

r h "Oh, that was a joke?"

menu:
    "Nema are you OK?":
        pass

    "Nema, you're not OK.":
        pass

show p n

p n "I am OK sir."

p n "Please."

p n "Do not worry."

show y h

y h "Convincing."

show r su

r su "So... what do we do here Nema?"

show p n

p n "How about a board game?"

p h "Please, let's play a board game."

show y h

y h "Didn't see that one coming, what with the board game being out and set up and the only thing you have appeared to actually set up with your entire day of preperation."

show r su

r su "No, we're missing a piece on our side?"

show p su

p su "What? No, I had them all out."

p n "Did you move it?"

p m "You snake."

show r h

r h "Hah, nope, sorry to say it was already gone."

show p n

p n "I like that."

p h "Hei you're always honest and I. Like. That."

e "Nema puts her arm around Hei."

show r su

r su "Oh, hi there."

show p h

p h "Hi. Heh. Heh."

show y h

y h "Nema please don't laugh like that."

show p n

p n "Oh..."

p h "Heh."

show y n

y n "Alright, come on. What do you normally do on Peggy day that you love so much?"

show p n

p n "Normally? "

p s "Well this is not normally."

p s "Normally I'd be at home, with my family."

show y n

y n "Right. And?"

show p n

p n "And we would play games."

show y m

y m "Like?"

show p h

p h "My brothers always had something new to play."

p n "They were the fun ones."

p s "I am not the fun one."

show y m

y m "Yes, I've realized this."

show r s

r s "Come on Haruka."

show y n

y n "I'm trying Hei. I'm trying so hard."

show r m

r m "You're not trying, you're putting her down."

show y h

y h "Well she's making it hard to do anything else right now."

show r m

r m "That's not fair, she's obviously not used to doing this sort of thing."

show y m

y m "Yes, obviously. That's what I was saying."

show p m

p m "That's what she was saying."

show r s

r s "I'm on your side, Nema."

show p h

p h "Awww. "

e "Nema smiles and gives Hei a hug."

p h "What a sweetie-pie."

show r su

r su "Oh."

show y h

y h "Hahaha"

show r su

r su "Shut up. Let me switch seats with you."

show y m

y m "Hell no."

show p h

p h "Haruka I'll sit by you!"

e "Nema let out a little wink."

show r s

r s "Cap I don't think I feel right sitting here right now."

show y m

y m "Hell no to that too. I'm not sitting by you."

show r m

r m "Fine, you know, I don't even know why I care."

show p su

p su "Woah, grumps."

show y m

y m "Seriously."

show r m

r m "No, I don't even know how to be on your side Haruka, why do you make it so hard?"

show y n

y n "Because I don't really like ya?"

menu:
    "Haruka be nice.":
        pass

    "...":
        pass

y h "I'm being nice. Nobody likes to be led on."

y n "He has a right ta know how I feel."

show r m

r m "More like you wont even let me have a chance."

show p m

p m "Yeah, ruude!"

show r m

r m "I'm done. Nema's cuter anyways."

menu:
    "Is this a conversation to have while we're all here?":
        pass

    "Well then.":
        pass

show y h

y h "HAH. Alright."

show p h

p h "Hei!"

p su "You... love me."

show r s

r s "Ha, oh, well..."

r n "I like you Nema, how about that."

show p s

p s "You love me. "

e "Nema stuck her tongue out at Haruka."

show y h

y h "Alright happy couple, what are we doing?"

show p m

p m "We're going to sit here and argue."

show y n

y n "Already done, next?"

show r n

r n "What did you and your brothers do?"

show p h

p h "My brothers would set up a board game, or Mahjong in the living room, and we'd all sit down and just play and talk and eat and laugh."

p n "That's what we will do."

show y n

y n "I'd play some Mahjong, do you have a set?"

show p n

p n "In my room."

show y h

y h "Alright great."

y s "..."

y n "So..."

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

r su "Wait. Why can't we use it Nema?"

show p h

p h "Hei!"

e "Nema smiles and nuzzles up to him."

show r h

r h "Ahaha, easy."

show p n

p n "Because it's my brothers set and I never asked if I could use it."

show r n

r n "Then why do you have it?"

show p n

p n "I got it when they died."

show y n

y n "So you don't really have to ask to use it then, do you?"

show p s

p s "It's not for playing. I haven't asked."

show y m

y m "Alright then I'm going to bed. "

menu:
    "Nema, there's no way we could \"ask them\"?":
        pass

    "Let's just use the set anyways.":
        pass

show r n

r n "Yeah, what if we try to talk to them?"

show p su

p su "B-but, I... we can't anymore."

show y m

y m "Are you guys talking about communicating with spirits? Really?"

show r n

r n "Yes. Do you want to try Nema."

show p m

p m "Wha-... N-no!"

show r su

r su "Huh?"

show p s

p s "No, no no no."

menu:
    "Why not?":
        pass

    "Alright.":
        pass

p s "They'll get mad. N-no."

e "Nema starts to tear up."

show r su

r su "Woah hey, c'mon you, stop... that."

r s "Uhm."

e "Hei looks at you with fear in his eyes."

menu:
    "Nod.":
        pass

    "Look back with fear.":
        pass

r su "Uhhh..."

e "Hei wraps his arm around Nema."

r n "It's OK. I'm sure they don't hate you."

show p s

p s "No, they do, I know."

show r n

r n "Right. We won't do that then."

show p s

p s "They hate me, no."

p s "I don't want to play anymore."

show y m

y m "Alright, it's official, I'm out of here. I have a ton of work to do and this is ridiculous."

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

r h "I guess I can take care of her, you can go on."

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
    
call hall

e "You pass by Haruka in the hall."

show y m

y m "Geesh."

play sound "sounds/DoorClose2.mp3"

hide y

e "Her door closes and you head into your room."

call blueRoom


return