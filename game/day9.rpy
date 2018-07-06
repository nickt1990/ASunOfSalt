label day9:

e "You've spent the morning monitoring system reports on your computer in silence."

e "Suddenly, there's a loud knocking on your door."

show r m

r m "Come out here COWARD."

menu:
    "What?":
        pass

    "Go away.":
        pass

r m "Face me like a man."

r m "I know you're in there, and you know why I'm here."

r n "Just come out here and we can get it over with."

menu:
    "Open your door.":
        pass

e "You walk over to the door."

e "As it slides open, you see Hei standing before you."

r h "Finally, there you are."

r n "Let's get to it, I'm gonna kick your ass."

menu:
    "Let's do it.":
        pass

    "What's your problem?":
        pass

r m "Soft and Moist Vegetables: 2 Turbo Vegetable Edition REMATCH."

r n "My room, 10 minutes."

r m "Warm your thumbs. {w=1.0}{size=-6}Bitch{/size}."

hide r m

play sound "sounds/DoorClose2.mp3"

e "Just as Hei walks away and into his room, Nema walks out of hers."

play sound "sounds/DoorOpen2.mp3"

show p h

p h "I wish you luck today in your trials Captain."

p n "May the best man win."

e "Nema bows."

p su "Don't forget to have some breakfast first though!"

e "Nema walks down the hallway toward the kitchen."

hide p su

menu:
    "Follow Nema into the kitchen.":
        call hall
        pass

e "You approach the open kitchen door to see Nema at the counter."

e "She's silently scrubbing at some dishes."

call kitchen

e "Haruka is eating quietly at the table."

show y n

y n "Hey Cap."

menu:
    "Morning.":
        pass

    "Morning grumpy.":
        pass

y s "I'm...{w=1.0} Sorry."

y s "..."

menu:
    "Don't worry about it.":
        pass

    "You haven't done anything to me.":
        pass

y s "Nah, I've been the worst. "

y s "I just feel so...{w=1.0} I don't know. "

y n "Would..."

y h " Would...{w=0.5} you be willing to meet up and talk over drinks tonight?"

y s "I have some things to say."

menu:
    "Of course.":
        pass

    "Somebody's getting a little dramatic.":
        pass

y n "Thank you."

hide y

e "Haruka makes her way out of the kitchen."

e "Nema's still absorbed in her work at the counter, so you quietly eat your food."

e "..."

e "Hei pops in."

show r h:
    linear 0 xalign 0.9 yalign 1.0

r h "Shakin' in your boots?"

r n "Look at the baby."

r h "He's terrified."
    
show r h:
    linear 0.5 xalign 0.5 yalign 1.0    

show p n:
    linear 0 xalign 0.9 yalign 1.0

p n "Hei you must always respect Captain."

show r m

r m "Nema I know,{w=0.5} I'm just-"

r m "we're doing-{w=0.5} it's a thing Nema,{w=0.5} just-"

show p n

p n "Hei, you must always respect your Captain."

show r m

r m "But I have to-{w=0.5} urrrrgh."

r n "{i}Captain.{/i}"

r s "{size=-6}I uhh.{/size}"

r n "Will meet you respectfully on the battlefield."

show p h

p h "Yes! "

e "Hei mouthes something obscene to you and then walked away."

hide r

e "Nema follows closely behind with a smile on her face."

hide p

menu:
    "I guess it's time to face the music.":
        call hall
        pass

    "I'm not done eating.":
        e "You take a few more minutes, then head out to meet Hei."
        call hall
        pass

e "You make your way to Hei's room."

call redRoom

show r m

r m "Ready to face the music?"

menu:
    "Sure.":
        pass

    "Nah.":
        pass

r h "First!"

r n "Let us reminisce."

r s "A week has passed."

r n "As men,{w=0.5} we have grown only stronger."

r h "As rivals,{w=0.5} we have grown more intense."

r n "As friends,{w=0.5} we have grown closer."

r s "It's all been leading up to this."

r h "{b}THIS{/b} is the pinnacle of our existence as bros."

show p su:
    linear 0 xalign 0.9 yalign 1.0

p su "I wasn't aware you two had been spending time together."

show r s

r s "What? Well, I guess we haven't really."

menu:
    "At all.":
        pass

    "It's a spiritual thing. ":
        pass

show p n

p n "Then how is any of what you said true? "

show r s

r s ".{w=0.2}.{w=0.2}.{w=0.2}Nema{w=0.2}.{w=0.2}.{w=0.2}.{w=0.5} you gotta stop this."

e "Nema smiles at Hei."

show r s

r s "It ma-"

show p n

p n "Bu-"

show r su

r su "Oops.{w=0.2} What were you gonna say?"

show p su

p su "Oh no I'm so sorry,{w=0.2} continue."

show r n

r n "No if I keep goin' you wont ever say what you were gonna say."

r n "What was it?"

show p s

p s "Oh..."

p n "Nothing."

show r m

r m "Just tell me."

show p h

p h "Well I was going to say,{w=0.1} that you two should spend some time together."

show r m

r m "That's what we're doing right now Nema."

show p n

p n "Yes, but to form strong bonds you must spend time getting to know other people Hei.{w=0.2} That is how you make friends."

show r n

r n "Nema just let us play our game."

menu:
    "You guys have gotten close.":
        pass

    "I agree, we should spend some time together Hei.":
        pass

e "Nema immediately smiles."

show p h

p h "We're two peas in a pod, sir."

show r h

r h "Haha"

menu:
    "Are you two dating then?":
        pass

    "Good to hear.":
        pass

r n "Nah, we're just friends."

show p h

p h "Yep! Good friends."

menu:
    "When did that happen?":
        pass

p s "Well...{w=0.1} I g-guess it would have been... "

p s "It would have been that one ni-"

show r h

r h "C'mon, you know when."

r m "No more stalling!"

menu:
    "Alright, alright.":
        pass

r s "Wait is...{w=0.1} uhm..."

r n "Is Haruka gonna watch?"

menu:
    "I think Haruka needs a little time still.":
        pass

    "No.":
        pass

r s "Right.{w=0.1} Right, yeah, just wondering."

r h "Alright, you ready to start?"

menu:
    "Born ready.":
        pass

    "No.":
        pass

r h "Music to Buff Daddy's ears."

r h "What?"

show p h

p h "Go Buff Daddy!"

e "Nema smiles earnestly."

p h "Also, go Captain!"

e "Hei frowns."

show r n

r n "Alright,{w=0.1} let's do this."

r m "{b}ENGAGE.{/b}"

e "Cheesy music begins to play."

show p h

p h "Woo!"

show r h

r h "Ha! You picked Tomato?"

r m "Foolish you,{w=0.1} I KNEW you would pick tomato."

r n "Over the last several days I'd been monitoring you closely and matching your actions with a specific Veggie Fighter."

r h "You were all too easy to read I'm afraid!"

show p su

p su "Woah!"

show r n

show p h

r n "I'd been practicing with the Veggie that's able to beat Tomato with no problem..."

r h "Cucumber!"

p su "Of course!"

r h "That's right, I wont lose to you this time!"

menu:
    "Sure.":
        pass

    "You wont touch a leaf on my head, idiot!":
        pass

r n "Nema,{w=0.1} please."

r n "The introduction we've prepared."

e "Nema hops up to her feet."

show p n

p n "Ahem."

p h "Gentlemen! I want a fair fight!"

p s "But most of all, I want to see a fight...{w=0.1} with honor."

p h "Reach the limits of the battlefield,{w=0.1} and surpass them!"

p h "The time limit shall be set to infinite and the match will go on as long as it needs to!"

p n "Let this be a match that will go down..."

show r h

r h "In history!"

r m "Fight!"

show black

e ".{w=0.2}.{w=0.2}."

e ".{w=0.2}.{w=0.2}."

hide black #todo

r ".{w=0.3}.{w=0.3}."

r su "Y-you beat me..."

menu:
    "Yep.":
        pass

r s "I didn't even touch you."

show p s

p s "No..."

show r s

r s "But...{w=0.1} You were Tomato..."

r s "I had it all planned..."

r s "I...{w=0.1} Wha..."

show p s

p s "After all that practice,{w=0.1} I understand why you're upset Hei."

show r s

r s "Y-yeah...{w=0.1} well..."

r n "I guess I technically didn't \"practice\"."

menu:
    "You didn't practice?":
        pass

r n "I had so much to do."

menu:
    "Like... what?":
        pass

r m "Dunno, stop grilling me man."

show p s

p s "You seemed so serious about this Hei. "

p s "You didn't practice at all?"

show r su

r su "I wanted to!"

menu:
    "You have no work ethic. Shameful.":
        pass

    "Well, there's always next time!":
        pass

r m "I dedicate myself to what I {b}CARE{/b} about!"

r m "Sorry I can't just throw myself into boring garbage like you and angry woman across the hall."

show p s

p s "But Hei,{w=0.15} you really seemed to care about winning.{w=0.2} You've talked about it quite frequently this last week."

show r s

r s "Well I guess I didn't care that much."

r n "It's just a game."

menu:
    "Sore loser.":
        pass

    "Right, it was fun!":
        pass

r m "You wish, weiner head."

show p h

p h "Hei!{w=0.15} That's our Captain!"

show r s

r s "Whatever, sorry I don't have time to waste on a stupid video game."

play sound "sounds/DoorOpen2.mp3"

e "The door opens and haruka walks through"

show y n:
    linear 0.5 xalign 0.1 yalign 1.0

y n "Since when have you not had time to waste?"

show r s

r s "..."

show y n

y n "Somebody has to take engine duty tonight."

show r n

r n "I'll do it."

show y n

y n "You? "

show r n

r n "Yeah, I've been looking forward to it."

show y n

y n "Hah."

hide y

e "Haruka walks out."

menu:
    "I'm surprised.":
        pass

    "You don't want to actually do it, do you?":
        pass

show r h

r h "Well maybe there's more to me than you thought."

show p h

p h "I'm impressed too Hei,{w=0.15} will you alright on your own?{w=0.15} Did you read over the notes again?"

show r su

r su "Bu-wait."

r s "I was kind of hoping that maybe you...{w=0.15} would..."

show p su

p su "I would...?"

menu:
    "You want her to keep you company?":
        pass

    "You want her to do all the work?":
        pass

show r h

r h "Yes! "

show p s

p s "Oh...{w=0.15} w-well,{w=0.15} I did have some work I planned to get done tonight,{w=0.15} but I can help you out if you truly want me to."

show r h

r h "C'mon dude, it'll be fun."

show p s

p s "S-{w=0.1}sure,{w=0.15} I suppose it couldn't hurt."

p n "..."

p s "C-captain?{w=0.15} Would you like to join us?"

menu:
    "I have plans with Haruka tonight.":
        r su "Oh...{w=0.15} with Haruka?"
        r s "Right.{w=0.15} Ok."
        pass

    "I have work to do.":
        r n "Lame."
        pass

show r su

r s "Well, it's getting pretty late."

r n "I'm gonna get ready for the long night."

r n "G'night dude."

hide r

hide p

call hall

play sound "sounds/DoorClose2.mp3"

e "You step out into the hallway."

menu:
    "Visit Haruka.":
        e "You walk up to Haruka's door but it wont open."
        e "She must be busy."
        e "You head back to your room."
        pass

    "Go to your room and wait.":
        pass

call blueRoom

e "There's a notification on your computer."

e "You check your email."

return