label day12:
    
e "You both sleep peacefully through the night."

hide black
    
e "Nema is still cuddled up beside you sleeping when you wake up."

menu:
    "Get out of bed.":
        pass

    "Stay in bed.":
        pass

e "You move quietly out of the bed and to your computer."

e "There's a instant message from Haruka telling you sleep well."

e "No other messages."

show p h

p h "Good morning, Sir."

hide p h

e "Nema stands up out of bed and begins to put her clothes on."

e "Once dressed, she laid back down on the bed."

show p h

p h "How did you sleep?"

e "Suddenly, the door opens."

play sound "sounds/DoorOpen2.mp3"

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

    "On the floor.":
        p su "What?"
        p n "No,{w=0.15} we shared the bed.{w=0.2} Of course."
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

p h "My relationship with him has no bearing on yours, {w=0.15}you should have no worries."

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

p n "Is the life support on?"

show y m

y m "Everything's back to normal."

show p n

p n "Then I'm going to leave."

p n "We can talk again later when you've calmed down."

hide p

e "Nema gets up and walks out the door."

play sound "sounds/DoorClose2.mp3"

show y n

y n "..."

e "Haruka stared blankly at the wall for a moment, {w=0.15}thinking."

y s "I'm sorry caps."

y s "I didn't mean to get so emotional."

y n "You know how I feel about Nema."

menu:
    "I do.":
        pass

    "That's no excuse.":
        y m "Ugh. {w=0.15}I know, {w=0.15}I know."
        pass

y s "You probably think I'm insane."

y n "But like I told you, {w=0.15}sex isn't some casual thing to me."

y s "I know I don't own you or anything,{w=0.15} I haven't even told.{w=0.15}.{w=0.15}. "

y n "Nevermind."

y n "Point is, {w=0.15}I was a jerk."

y m "Again."

menu:
    "We didn't have sex.":
        pass

    "We just shared a bed.":
        pass

y n "I know,{w=0.15} I know."

y s "It doesn't even matter."

y n ".{w=0.15}.{w=0.15}."

y n "I should apologize I guess."

y h "Or maybe not?"

y n ".{w=0.15}.{w=0.15}."

y m "Hmph."

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka walks out of the room."

play sound "sounds/DoorClose2.mp3"

e ".{w=0.15}.{w=0.15}."

e "You hear the sound of arguing coming from the hallway."

menu:
    "Check it out.":
        pass

play sound "sounds/DoorOpen2.mp3"

call hall from _call_hall_22

e "You open the door and enter the hallway."

play sound "sounds/DoorClose2.mp3"

e "Hei and Haruka are standing in the middle of the hallway yelling at one another."

y m "Why would I EVER do that?"

show r s

r s "C'mon, {w=0.15}you said it yourself that I wasn't too bad, what could it hurt?"

show y m:
    linear 0 xalign 0.9 yalign 1.0

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

y h "You're a real dirtbag roller-coaster,{w=0.15} you know that?"

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka abruptly turns and enters her room."

show r m

r m "Man, I thought I finally had her."

menu:
    "Too bad.":
        pass

    "Next time.":
        pass

r m "You're damn right,{w=0.15} too bad."

r h "But hey!"

r n "How did your night go?"

r h "Did you.{w=0.15}.{w=0.15}.{w=0.15}?"

menu:
    "...?":
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
    "That's pretty rude.":
        pass

    "No.":
        pass

r su "Oh, {w=0.15}right."

r s "Sorry, {w=0.15}I didn't mean it that way."

r h "Well I did,{w=0.15} but.{w=0.15}.{w=0.15}."

r n "I meant it in a bros kinda way,{w=0.15} right?"

menu:
    "No.":
        pass

    "Whatever.":
        pass

r s "Right."

r n "Well."

r n "Whatever man, {w=0.15}I got some games to play."

play sound "sounds/DoorOpen2.mp3"

e "Hei walks over and opens his door,{w=0.15} then..."

show p su:
    linear 0 xalign 0.9 yalign 1.0

play sound "sounds/DoorOpen2.mp3"

p su "Wait!"

e "Nema steps out of her room."

show r su

r su "Huh?"

show p n

p n "Hei{w=0.15}.{w=0.15}.{w=0.15}."

show r n

r n "Oh hey, {w=0.15}wanna play?"

show p h

p h "Well,{w=0.15} yes.{w=0.25} I do."

show r h

r h "Noice.{w=0.25} C'mon."

show p s

p s "Wait, {w=0.15}first,{w=0.15} I want to talk for a second."

p s "Talking with Captain last night got me thinking..."

p n "About all the things I miss from home."

p s ".{w=0.15}.{w=0.15}."

p h "My brothers."

p n "About the people I respect here on this ship..."

p h "About the person I want to be."

p n "I don't want to hold myself back anymore."

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

play sound "sounds/DoorClose2.mp3"

hide p

e "Nema turned and walked back into her room."

show r n

r n "..."

r s "Ugh."

play sound "sounds/DoorClose2.mp3"

hide r

e "Hei walks back into his room as well."

menu:
    "Head back to your room":
        call blueRoom from _call_blueRoom_9
        pass

e "You stay in your room for the rest of the day working."

e "You don't hear anyone else leave their rooms for the rest of the night."

show black

return