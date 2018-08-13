﻿label day9:

window hide
hide black
with fade

play music "music/MorningAlarm.ogg" fadein 2.0

e "You wake up to your alarm."

e "After getting up and about, you notice you have mail notifications on your computer."

window hide
show black
with fade

menu:#computer
    "Read mail.":
        label summariesD9:
        menu:
            "Haruka's summary.":
                call day9HaruS from _call_day9HaruS
                jump summariesD9
                pass
            "Hei's summary.":
                call day9HeiS from _call_day9HeiS
                jump summariesD9
                pass
            "Nema's summary.":
                call day9NemaS from _call_day9NemaS
                jump summariesD9
                pass
            "I think I'm done.":
                jump day9Start
                pass                
        pass

    "Not today.":
        jump day9Start
        pass

label day9Start:

window hide
hide black
with fade

stop music fadeout 3.0

play sound "sounds/Knock.ogg"

e "Suddenly, {w=0.15}there's a loud knocking on your door."

play music "music/EasternCowboy.ogg" fadein 2.0

r m "Come out here {b}COWARD.{/b}"

menu:
    "What?":
        pass

    "Go away.":
        pass

r m "Face me like a man."

r m "I know you're in there, {w=0.15}and you know why I'm here."

r n "Just come out here and we can get it over with."

menu:
    "Open your door.":
        pass

e "You walk over to the door."

e "As it slides open, {w=0.15}you see Hei standing before you."

show r m

r h "Finally, {w=0.15}there you are."

r n "Let's get to it, {w=0.15}I'm gonna kick your ass."

menu:
    "Let's do it.":
        pass

    "What?":
        pass

r m "Soft and Moist Vegetables:{w=0.15} 2 Turbo Vegetable Edition{w=0.15} {b}R{w=0.15}E{w=0.15}M{w=0.15}A{w=0.15}T{w=0.15}C{w=0.15}H{/b}."

r n "My room, {w=0.15}10 minutes."

r m "Warm your thumbs. {w=1.0}{size=-6}Bitch{/size}."

hide r m

play sound "sounds/DoorClose2.ogg"

e "Just as Hei walks away and into his room, {w=0.15}Nema walks out of hers."

play sound "sounds/DoorOpen2.ogg"

show p h

p h "I wish you luck today in your trials Captain."

p n "May the best man win."

e "Nema bows."

p h "Don't forget to have some breakfast first though!"

stop music fadeout 2

e "Nema walks down the hallway toward the kitchen."

hide p su

menu:
    "Follow Nema to the kitchen.":
        call hall from _call_hall_12
        pass

play sound "sounds/DoorOpen2.ogg"

play music "music/SpaceSunday.ogg" fadein 2.0

e "You approach the open kitchen door to see Nema at the counter."

e "She's silently scrubbing at some dishes."

call kitchen from _call_kitchen_3

e "Haruka is eating quietly at the table."

show y n

y n "Hey Cap."

menu:
    "Morning.":
        y s "So,{w=0.15} I just wanted to say.{w=0.15}.{w=0.15}."
        pass

    "Morning grumpy.":
        y h "Yeah yeah."
        pass

y s "I'm.{w=0.15}.{w=0.15}.{w=0.5} Sorry."

y s ".{w=0.15}.{w=0.15}."

menu:
    "Don't worry about it.":
        pass

    "You haven't done anything to me.":
        pass

y s "Nah, {w=0.15}I've been the worst. "

y s "I just feel so.{w=0.15}.{w=0.15}.{w=0.3} I don't know. "

y n "Would.{w=0.15}.{w=0.15}."

y h " Would ya be willing to meet up and talk over drinks tonight?"

y s "I have some things to say."

menu:
    "Of course.":
        y n "Thank you."
        pass

    "Somebody's getting a little dramatic.":
        y m "Hey,{w=0.15} c'mon,{w=0.15} I'm trying here."
        y s "I'll see ya later Cap."
        pass

hide y

play sound "sounds/DoorClose2.ogg"

e "Haruka makes her way out of the kitchen."

e "Nema's still absorbed in her work at the counter, {w=0.15}so you quietly eat your food."

e ".{w=0.15}.{w=0.15}."

play sound "sounds/DoorOpen2.ogg"

e "Hei pops in."

show r h:
    linear 0 xalign 0.9 yalign 1.0

r h "Shakin' in your boots?"

r n "Look at the baby."

r h "He's {i}terrified.{/i}"
    
show r h:
    linear 0.5 xalign 0.5 yalign 1.0    

show p n:
    linear 0 xalign 0.9 yalign 1.0

p n "Hei you must always respect Captain."

show r m

r m "Nema I know,{w=0.5} I'm just-"

r s "we're doing-{w=0.5} it's a thing Nema,{w=0.5} just-"

show p n

p n "Hei, {w=0.15}you must always respect your Captain."

show r m

r m "But I have to-{w=0.25} urrrrgh."

r s "{i}Captain.{/i}"

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
        call hall from _call_hall_13
        pass

    "I'm not done eating.":
        e "You take a few more minutes, {w=0.15}then head out to meet Hei."
        call hall from _call_hall_14
        pass

play sound "sounds/DoorClose2.ogg"

call redRoom from _call_redRoom_1

e "You make your way to Hei's room."

show r m

stop music fadeout 2

r m "Ready to face the music?"

menu:
    "Sure.":
        pass

    "Nah.":
        pass

r h "First!"

play music "music/MelancholyPiano.ogg" fadein 2.0

r n "Let us reminisce."

r s "A week has passed."

r n "As men,{w=0.25} we have grown only stronger."

r h "As rivals,{w=0.25} we have grown more intense."

r n "As friends,{w=0.25} we have grown closer."

r s "It's all been leading up to this."

r h "{b}THIS{/b} is the pinnacle of our existence as bros."

show p su:
    linear 0 xalign 0.9 yalign 1.0

p su "I wasn't aware you two had been spending time together."

show r s

r s "What? Well, {w=0.15}I guess we haven't really."

menu:
    "At all.":
        pass

    "It's a spiritual thing. ":
        pass

show p n

p n "Then how is any of what you said true? "

show r s

r s ".{w=0.2}.{w=0.2}.{w=0.2}Nema{w=0.2}.{w=0.2}.{w=0.2}.{w=0.25} you gotta stop this."

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

p s "Oh.{w=0.15}.{w=0.15}."

p n "Nothing."

show r m

r m "Just tell me."

show p h

p h "Well I was going to say,{w=0.15} that you two should spend some time together."

show r m

r m "That's what we're doing right now Nema."

show p n

p n "Yes, {w=0.15}but to form strong bonds you must spend time getting to know other people Hei.{w=0.2} That is how you make friends."

show r n

r n "Nema just let us play our game."

menu:
    "You guys have gotten close.":
        pass

    "I agree, {w=0.15}we should spend some time together Hei.":
        r m "I'm very busy,{w=0.15} we'll see."
        p su "Busy with what?"
        r su "Uh.{w=0.15}.{w=0.15}."
        r h "Busy with you!"
        pass

e "Nema immediately smiles."

show p h

p h "We're two peas in a pod, {w=0.15}sir."

show r h

r h "Haha."

menu:
    "Are you two dating then?":
        r n "Nah, {w=0.15}we're just friends."
        pass

    "Good to hear.":
        r h "Isn't it?"
        r h "The beauty of a blossoming friendhip right before your eyes."
        pass

show p h

p h "Yep!{w=0.15} Good friends."

menu:
    "When did that happen?":
        pass

p s "Well.{w=0.15}.{w=0.15}.{w=0.1} I g-guess it would have been.{w=0.15}.{w=0.15}. "

p s "It would have been that one ni-"

show r h

r h "C'mon, {w=0.15}you know when."

r m "No more stalling!"

menu:
    "Alright, {w=0.15}alright.":
        pass

r s "Wait is.{w=0.15}.{w=0.15}.{w=0.15} uhm.{w=0.15}.{w=0.15}."

r n "Is Haruka gonna watch?"

menu:
    "I think Haruka needs a little time still.":
        pass

    "No.":
        pass
        
stop music fadeout 3

r s "Right.{w=0.1} Right, {w=0.15}yeah, {w=0.15}just wondering."

r h "Alright, {w=0.15}you ready to start?"

menu:
    "Born ready.":
        r h "Music to Buff Daddy's ears."
        pass

    "No.":
        r h "What?"
        r m "C'mon man."
        r m "Don't make Buff Daddy mad!"
        pass

play music "music/Space.ogg" fadein 2.0

show p h

p h "Go Buff Daddy!"

e "Nema smiles earnestly."

p h "Also, {w=0.15}go Captain!"

show r s

e "Hei frowns."

show r n

r n "Alright,{w=0.1} let's do this."

r m "I'll even play the original soundtrack for you this time."

r m "{b}ENGAGE.{/b}"

play music "music/Diddy.ogg" fadein 1.0

show p h

p h "Woo!"

show r h

r h "Ha!{w=0.15} You picked Tomato?"

r m "Foolish you,{w=0.1} I KNEW you would pick tomato."

r n "Over the last several days I'd been monitoring you closely and matching your actions with a specific Veggie Fighter."

r h "You were all too easy to read I'm afraid!"

show p su

p su "{i}Woah!{/i}"

show r n

show p h

r n "I'd been practicing with the Veggie that's able to beat Tomato with no problem.{w=0.15}.{w=0.15}."

r h "{i}Cucumber!{/i}"

p su "Of course!"

r h "That's right, {w=0.15}I wont lose to you this time!"

menu:
    "Sure.":
        pass

    "You wont touch a leaf on my head, {w=0.15}idiot!":
        pass

r n "Nema,{w=0.1} please."

r n "The introduction we've prepared."

e "Nema hops up to her feet."

show p n

p n "Ahem."

p h "Gentlemen! I want a fair fight!"

p s "But most of all, {w=0.15}I want to see a fight.{w=0.15}.{w=0.15}.{w=0.1} with honor."

p h "Reach the limits of the battlefield,{w=0.1} and surpass them!"

p h "The time limit shall be set to infinite and the match will go on as long as it needs to!"

p n "Let this be a match that will go down.{w=0.15}.{w=0.15}."

show r h

r h "In history!"

r m "Fight!"

window hide
show black
with fade

e ".{w=0.2}.{w=0.2}."

stop music fadeout 3

e ".{w=0.2}.{w=0.2}."

window hide
hide black
with fade

r ".{w=0.3}.{w=0.3}."

play music "music/Space.ogg" fadein 2.0

r su "Y-you beat me.{w=0.15}.{w=0.15}."

menu:
    "Yep.":
        pass

r s "I didn't even touch you."

show p s

p s "No.{w=0.15}.{w=0.15}."

show r s

r s "But.{w=0.15}.{w=0.15}.{w=0.1} You were Tomato.{w=0.15}.{w=0.15}."

r s "I had it all planned.{w=0.15}.{w=0.15}."

r s "I.{w=0.15}.{w=0.15}.{w=0.1} Wha.{w=0.15}.{w=0.15}."

show p s

p s "After all that practice,{w=0.1} I understand why you're upset Hei."

show r s

r s "Y-yeah.{w=0.15}.{w=0.15}.{w=0.1} well.{w=0.15}.{w=0.15}."

r n "I guess I technically didn't \"practice\"."

menu:
    "You didn't practice?":
        pass

r n "I had so much to do."

menu:
    "Like.{w=0.15}.{w=0.15}. what?":
        pass

r m "Dunno, {w=0.15}stop grilling me man."

show p s

p s "You seemed so serious about this Hei. "

p s "You didn't practice at all?"

show r su

r su "I wanted to!"

menu:
    "Shameful.":
        pass

    "Well, {w=0.15}there's always next time!":
        r m "Whatever."
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
        r m "You wish, {w=0.15}wiener head."
        pass

    "Right, {w=0.15}it was fun!":
        r m "Whatever,{w=0.15} dickbrains."
        pass

show p h

p h "Hei!{w=0.1} That's our Captain!"

show r s

r s "Sorry I don't have time to waste on a stupid video game."

play sound "sounds/DoorOpen2.ogg"

e "The door opens and Haruka walks through"

show y n:
    linear 0 xalign 0.1 yalign 1.0

y n "Since when have you not had time to waste?"

show r s

r s ".{w=0.15}.{w=0.15}."

show y n

y n "Somebody has to take engine duty tonight."

show r n

r n "I'll do it."

show y n

y n "You? "

show r n

r n "Yeah, {w=0.15}I've been looking forward to it."

show y n

y n "Hah."

hide y

play sound "sounds/DoorClose2.ogg"

e "Haruka walks out."

menu:
    "I'm surprised.":
        pass

    "You don't want to actually do it, {w=0.15}do you?":
        pass

show r h

r h "Well maybe there's more to me than you thought."

show p h

p h "I'm impressed too Hei,{w=0.15} will you alright on your own?{w=0.15} Did you read over the notes again?"

show r su

r su "Bu-wait."

r s "I was kind of hoping that maybe you.{w=0.15}.{w=0.15}.{w=0.15} would.{w=0.15}.{w=0.15}."

show p su

p su "I would.{w=0.15}.{w=0.15}.?"

menu:
    "You want her to keep you company?":
        r h "Yes!"
        pass

    "You want her to do all the work?":
        r m "Absolutely not!"

        r h "Help would be nice though."
        pass

show p s

p s "Oh.{w=0.15}.{w=0.15}.{w=0.15} w-well,{w=0.15} I did have some work I planned to get done tonight,{w=0.15} but I can help you out if you truly want me to."

show r h

r h "C'mon dude, {w=0.15}it'll be fun."

show p s

p s "S-{w=0.1}sure,{w=0.15} I suppose it couldn't hurt."

p n ".{w=0.15}.{w=0.15}."

p s "C-captain?{w=0.15} Would you like to join us?"

menu:
    "I have plans with Haruka tonight.":
        r su "Oh.{w=0.15}.{w=0.15}. with Haruka?"
        r s "Right.{w=0.35} Okay."
        pass

    "I have work to do.":
        r n "Lame."
        pass

show r su

r s "Well, {w=0.15}it's getting pretty late."

r n "I'm gonna get ready for the long night."

r n "G'night dude."

hide r

hide p

call hall from _call_hall_15

play sound "sounds/DoorClose2.ogg"

e "You step out into the hallway."

menu:
    "Visit Haruka.":
        e "You walk up to Haruka's door but it wont open."
        e "She must be busy."
        e "You head back to your room."
        pass

    "Go to your room and wait.":
        pass

call blueRoom from _call_blueRoom_8

e "There's a notification on your computer."

window hide
show black
with fade

play music "music/Idle.ogg" fadein 2.0

menu:#computer
    "I'll read my mail.":
        label summariesD92:
        menu:
            "Junk mail.":
                call bMail8 from _call_bMail8
                jump summariesD92
                pass
            "I think I'm done.":
                jump day9End
                pass                
        pass

    "I don't want to read my mail.":
        jump day9End
        pass

label day9End:

play music "music/Space.ogg" fadein 2.0

window hide
hide black
with fade

return