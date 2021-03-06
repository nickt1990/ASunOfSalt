﻿label day12:
    
stop music fadeout 2

e "You both sleep peacefully through the night."

window hide
hide black
with fade

play music "music/MorningAlarm.ogg" fadein 2.0
e "You wake up to the sound of your alarm."

menu:
    "Shut off alarm." if nemaBed == True:
        e "You reach over and shut the alarm off."
        e "Nema is still curled up beside you sleeping."
        pass
    "Shut off alarm." if nemaBed == False:
        e "You reach over and shut the alarm off."
        e "Nema is still asleep on the floor when you look over."
        pass

play music "music/Idle.ogg" fadein 3.0

menu:
    "Get out of bed.":
        pass

e "You move quietly out of the bed and to your computer."

window hide
show black 
with fade

menu:#computer
    "I'll read my emails.":
        label summariesD12:
        menu:
            "Haruka's summary.":
                call day12HaruS from _call_day12HaruS
                jump summariesD12
                pass
            "Hei's summary.":
                call day12HeiS from _call_day12HeiS
                jump summariesD12
                pass
            "Nema's summary.":
                call day12NemaS from _call_day12NemaS
                jump summariesD12
                pass
            "Email from Haruka" if harukaLove:
                e "There's an email from Haruka that came in last night."
                e "Cap,"
                e "I'm sorry for all the ham."
                e "I've just been eating them a lot and when I make them I figure I might as well make an extra in case you're hungry."
                e "They're good though, right?"
                e "-Haru"
                pass
            "I think I'm done.":
                jump day12Mid
                pass                
        pass

    "I don't feel like reading my emails.":
        jump day12Mid
        pass

label day12Mid:

play music "music/Pillows.ogg" fadein 2.0

window hide
hide black 
with fade

e "You notice Nema starting to move."

menu:
    "Good morning!" if nemaBed == True and nemaClothes == True:
        show p h
        p h "Good morning, sir."
        e "Nema sits up and scoots over and sits on the side of the bed."
        pass

    "Good morning!" if nemaBed == True and nemaClothes == False:
        show pz h
        pz h "Good morning, sir."
        window hide
        show black
        with fade
        hide pz h
        e "Nema stands up out of bed and begins to put her clothes on."
        show p h
        window hide
        hide black
        with fade
        e "Once dressed, she laid back down on the bed."
        pass

    "Good morning!" if nemaBed == False and nemaClothes == True:
        e "Nema gets out of her sleeping bag,{w=0.15} walks over to the side of your bed,{w=0.15} and sits down."
        pass

    "Good morning!" if nemaBed == False and nemaClothes == False:
        pz h "Good morning sir!"
        hide pz h
        show p h
        e "She quickly gathers her clothing and puts it back on."
        e "Then,{w=0.15} she walks over to the side of your bed and sits down."
        pass

show p h

p h "How did you sleep?"

e "Suddenly, the door opens."

play sound "sounds/DoorOpen2.ogg"

show y n:
    linear 0 xalign 0.9 yalign 1.0

y n "Hey."

menu:
    "Hey.":
        pass

    "Good morning.":
        pass

y h ".{w=0.15}.{w=0.15}."

y n "How was your night?"

menu:
    "Interesting.":
        pass

    "Good.":
        pass

y n "Ah,{w=0.15} I see.{w=0.15}.{w=0.15}."

show p h

p h "Good morning,{w=0.15} Haruka."

show y n

y n "Oh hey,{w=0.15} didn't notice you there."

show p h

p h "I just got up."

show y n

y n "Oh."

show p h

p h "Did you and Hei get along?"

show y h

y h "Surprisingly it wasn't so bad. "

y n "He gave me my space and was able to pretend to be a decent human for a little."

show p h

p h "Excellent!"

p h "I'm so glad to hear that."

p n "I was starting to worry you'd never become friends."

show y m

y m "Friends is pushing it."

y n "But he's not a complete loser."

show p su

p su "Where is he,{w=0.15} by the way?"

show y n

y n "Right, {w=0.15}he's still sleepin'."

show p h

p h "I see.{w=0.15}.{w=0.15}."

show y s

y s "So.{w=0.15}.{w=0.15}."

y n "Did you two get any sleeping done last night?"

menu:
    "That's all we did.":
        pass

    "Not much.":
        pass

y h "Oh, right."

y h "Of course."

y n "Cap,{w=0.15} almost forgot to mention."

y h "What a chivalrous one you are."

y n "Letting Nema sleep on the bed."

y n "Where did you sleep?"

menu:
    "We shared.":
        pass

    "On the floor." if nemaBed == False:
        p h "I brought a sleeping bag.{w=0.15} See?"
        e "She points to a sleeping bag on the floor."
        y m "Yeah, I bet you did."
        p su "Excuse me?"
        p n "Are you implying something, Haruka?"
        y m "I think you know exactly what I'm implying."
        p m "I'm sorry Haruka, but I don't feel I need to defend myself any further."
        jump nemaNoBed12
        pass

y su "Oh wow,{w=0.15} really?"

show p n

p n "Don't worry Haruka, {w=0.15}nothing took place."

p h "It was just nice to cuddle up to a warm body."

show y m

y m "I mean,{w=0.15} isn't that something?"

show p su

p su "W-{w=0.2}what?"

show y m

y m "I wouldn't cuddle up to you like that."

show p su

p su "Really?"

p n "I would to you."

show y m

y m "Well I wouldn't want you to."

show p s

p s "I'm sorry Haruka.{w=0.15}.{w=0.15}.{w=0.15} have I offended you somehow?"

show y m

y m "No, {w=0.15}I don't care what you do."

show p s

p s "Haruka, {w=0.15}I don't mean to sound obvious,{w=0.15} but Captain and I merely slept near one another."

label nemaNoBed12:

p h "My relationship with the captain has no bearing on yours, {w=0.15}you should have no worries."

show y m

y m "I'm not worried,{w=0.15} I'm just annoyed that you're doing your best to bang everyone on the ship."

show p su

p su "What do you mean?"

show y m

y m "You know exactly what I mean."

show p s

p s "Haruka,{w=0.15} I-"

show y n

y n "Nah,{w=0.15} you don't need to explain,{w=0.15} I'm sure I get it."

show p s

p s "Haruka,{w=0.15} people were meant to touch one another,{w=0.15} it's just another way of communicating."

show y m

y m "Well you don't have to communicate everything to everyone."

show p m

p m "I feel that you're purposely trying to provoke me,{w=0.15} Haruka."

show y n

y n "I'm not doing anything,{w=0.15} just making observations."

show p m

p m "No, {w=0.15}you're becoming emotional over something that didn't even happen."

p m "Even if the Captain and I did have sex, {w=0.15}I don't see what the issue would be."

show y h

y h "Ah there it is."

y n "Sex."

y m "I knew you understood me."

show p n

p n "Why does the idea bother you so much?"

show y m

y m "It doesn't bother me,{w=0.15} just let it go."

show p n

p n "Obviously it does Haruka."

p s "I'm not trying to hurt you."

p h "The Captain and I are just friends, {w=0.15}and I want to be friends with you too."

show y m

y m "Right,{w=0.15} like you're friends with Hei."

show p n

p n "I am friends with Hei."

show y h

y h "Yeah,{w=0.15} I remember."

show p m

p m "Haruka, {w=0.15}I'm sorry but I don't think that we're making any progress right now."

p m "Is the life support on?"

show y m

y m "Everything's back to normal."

show p n

p m "Then I'm going to leave."

p m "We can talk again later when you've calmed down."

hide p

e "Nema gets up and walks out the door."

play sound "sounds/DoorClose2.ogg"

show y n:
    linear 0.45 xalign 0.5 yalign 1.0

y n ".{w=0.15}.{w=0.15}."

e "Haruka stared blankly at the wall for a moment, {w=0.15}thinking."

y s "I'm sorry caps."

y s "I didn't mean to get so emotional."

y s "You know how I feel about Nema."

menu:
    "I do.":
        pass

    "That's no excuse.":
        y m "Ugh. {w=0.15}I know, {w=0.15}I know."
        pass

y s "You probably think I'm insane."

y s "But like I told you, {w=0.15}sex isn't some casual thing to me."

y s "I know I don't own you or anything,{w=0.15} I haven't even told.{w=0.15}.{w=0.15}. "

y n "Nevermind."

y n "Point is, {w=0.15}I was a jerk."

y m "Again."

menu:
    "We didn't have sex.":
        pass

    "We just shared a bed." if nemaBed:
        pass

    "It's none of your business what we did.":
        pass

y n "I know,{w=0.15} I know."

y s "It doesn't even matter."

y n ".{w=0.15}.{w=0.15}."

y n "I should apologize I guess."

menu:
    "Apologize.":
        $ nemaHarukaLove = True
        pass

    ".{w=0.15}.{w=0.15}.{w=0.15}":
        y h "Or maybe not?"
        pass

y n ".{w=0.15}.{w=0.15}."

y m "Hmph."

play sound "sounds/DoorOpen2.ogg"

hide y

e "Haruka walks out of the room."

play sound "sounds/DoorClose2.ogg"

e ".{w=0.15}.{w=0.15}."

e "You hear the sound of arguing coming from the hallway."

menu:
    "Check it out.":
        pass

play sound "sounds/DoorOpen2.ogg"

call hall from _call_hall_22

e "You open the door and enter the hallway."

play sound "sounds/DoorClose2.ogg"

e "Hei and Haruka are standing in the middle of the hallway yelling at one another."
                                                                                     
show y m

y m "Why would I EVER do that?"

show r s:
    linear 0 xalign 0.9 yalign 1.0

r s "C'mon, {w=0.15}you said it yourself that I wasn't too bad,{w=0.15} what could it hurt?"

show y m

y m "No,{w=0.15} absolutely not."

y m "It wasn't bad for one night, {w=0.15}that doesn't mean I'm jumping to move in."

show r h

r h "You'll come around,{w=0.15} my flower."

show y m

y m "Ugh."

y n "Not ever."

y n "Never."

show r n

r n "Is this because of that thing with Nema?"

show y su

y su "What?"

show r h

r h "We're just friends,{w=0.15} you know that."

r n "You're my real sunshine."

show y h

y h "You're a real dirtbag,{w=0.15} you know that?"

play sound "sounds/DoorOpen2.ogg"

hide y

e "Haruka abruptly turns and walks to her room."

show r m:
    linear 0.4 xalign 0.5 yalign 1.0

r m "Man, I thought I finally had her."

menu:
    "Too bad.":
        pass

    "Next time.":
        pass

show r s

e "Hei just looks at you and frowns."

r h "But hey!"

r n "How did your night go?"

r h "Did you.{w=0.15}.{w=0.15}.{w=0.15}?"

menu:
    ".{w=0.15}.{w=0.15}.?":
        pass

    "What?":
        pass

r n "What?"

r h "You know."

r h "Did ya{w=0.15}.{w=0.15}.{w=0.15}. "

r h "You know?"

menu:
    "No?":
        pass

    "No.":
        pass

r h "Take a ride on the Nema express?"

menu:
    "Are you serious?":
        r s "Um.{w=0.25} No?"
        pass

    "No.":
        r su "Oh, {w=0.15}right."
        pass

r s "Sorry, {w=0.15}I didn't mean it that way."

r h "Well I did,{w=0.15} but.{w=0.15}.{w=0.15}."

r n "I meant it in a bros kinda way,{w=0.15} right?"

menu:
    "No.":
        r s "Right."
        pass

    "Show your crewmate some respect.":
        r m "Sheesh."
        pass

    "Whatever.":
        r s "Fine."
        pass

r n "Well."

r n "Whatever man, {w=0.15}I got some games to play."

play sound "sounds/DoorOpen2.ogg"

e "Hei walks over and opens his door,{w=0.15} then.{w=0.15}.{w=0.15}."

show p su:
    linear 0 xalign 0.9 yalign 1.0

play sound "sounds/DoorOpen2.ogg"

p su "Wait!"

e "Nema steps out of her room."

show r su

r su "Huh?"

show p n

p n "Hei{w=0.15}.{w=0.15}.{w=0.15}."

show r n

r n "Oh hey, {w=0.15}wanna play some games?"

show p h

p h "Well,{w=0.15} yes.{w=0.25} I do."

show r h

r h "Noice.{w=0.25} C'mon."

show p s

p s "Wait, {w=0.15}first,{w=0.15} I want to talk for a second."

p s "Talking with Captain last night got me thinking.{w=0.15}.{w=0.15}."

p n "About all the things I miss from home."

p s ".{w=0.15}.{w=0.15}."

p h "My brothers."

p n "About the people I respect here on this ship.{w=0.15}.{w=0.15}."

p h "About the person I want to be."

p n "I don't want to hold myself back anymore."

p h "I think I can make this a place I want to live."

p n "I just want to follow how I feel."

p h "And I feel like.{w=0.15}.{w=0.15}."

p n "I love you."

show r su

r su "W-{w=0.15}what?"

show p h

p h ".{w=0.15}.{w=0.15}."

show r n

r n ".{w=0.15}.{w=0.15}."

r s ".{w=0.15}.{w=0.15}."

show p s

r s "I'm sorry,{w=0.15} Nems, I thought we.{w=0.15}.{w=0.15}."

r s "Aren't we friends?"

show p s

p s "Yes.{w=0.15}.{w=0.15}."

show r n

r n "Isn't that enough?"

r h "We're good friends,{w=0.15} right?"

show p s

p s ".{w=0.15}.{w=0.15}."

p s "I suppose it is."

play sound "sounds/DoorClose2.ogg"

hide p

e "Nema turned and walked back into her room."

show r n

r n ".{w=0.15}.{w=0.15}."

r s "Ugh."

play sound "sounds/DoorClose2.ogg"

hide r

e "Hei walks back into his room as well."

menu:
    "Head back to your room":
        call blueRoom from _call_blueRoom_9
        pass

e "You stay in your room for the rest of the day working."

stop music fadeout 2

e "You don't hear anyone leave their rooms for the rest of the night."

play music "music/Space.ogg" fadein 1.0

window hide
show black
with fade

return