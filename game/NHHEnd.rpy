﻿label noNHL:

play music "music/BadHere.ogg" fadein 1.0

p m "No."

window hide
show ptRed
show tWhite
with hpunch
play sound "sounds/Slash.ogg"
$ renpy.pause(0.34)

show y surDead

show p ss

window hide
hide tWhite
with fade

show y surDead:
    linear 0.1 xalign 0.9 ypos 1.99
    
e ".{w=0.2}.{w=0.2}."

p ss "Now,{w=0.2} sir."

p ss "With respect,{w=0.2} I can't turn back at this point."

p ss "So I apologize,{w=0.2} but.{w=0.2}.{w=0.2}."

menu:
    "Stop!" if demonAgree:
        pass
    "Stop!" if demonAgree == False:
        jump badDemonEnd
        pass

p ss "Please,{w=0.2} you have no need to panic sir."

p ss "I only truly needed two lives."

menu:
    "So, Hei?":
        pass

p ss "It broke my heart to have to hurt him.{w=0.2}.{w=0.2}."

p ss "Things could have been so different.{w=0.2}.{w=0.2}."

p ss "But he decided his own fate."

p ss "Same as you decided yours."

menu:
    "What?":
        pass

p ss "Do you not remember your pledge to me?"

p ss "Companion?"

menu:
    "What will you do to me?":
        p ss "Do to you?"
        pass
    "Just kill me now.":
        p ss "Kill you?"
        p ss "As I just said,{w=0.2} are we not companions?"
        pass

p ss "You're the reason I had the strength to go through with this to begin with."

p ss "You supported me like nobody ever has{w=0.2}.{w=0.2}.{w=0.2}."

p ss "Why would I want to hurt you,{w=0.2} sir?"

p ss "To be honest,{w=0.2} for a while I thought maybe I could just live a lie,{w=0.2} enjoy life with everyone."

p ss "But Hei only cared about himself.{w=0.2}.{w=0.2}."

p ss "And Haruka.{w=0.2}.{w=0.2}."

p ss "She would never accept me how I was,{w=0.3} so I decided I'd finally accept myself."

p ss "Besides,{w=0.2} it was only a matter of time before one of you figured out I was the one causing the dimensional rifts,{w=0.2} the visions."

p ss "My existence can't help but leak through this fake body Motokami gave me."

menu:
    "Motokami?":
        p ss "My oldest brother."
        pass

p ss "I told you he was a scientist right?"

p ss "He was the first of our people to successfully transfer to this dimension."

p ss "The blood pool was sort of their testing grounds."

p ss "Failed attempts.{w=0.2}.{w=0.2}.{w=0.2}"

p ss "The first thing my brother did after succeeding was to try to find a way to bring me over."

p ss "He saw an opportunity with Haruka."

p ss "Filled her head with lies,{w=0.2} propelled her to the top of her field."

p ss "To be honest,{w=0.2} I didn't like it at all."

p ss "He insisted that it was the only way,{w=0.2} but I don't know."

p ss "It seems cruel to me to let her think all her work was real."

p ss "At the very least she never had to face that truth.{w=0.2}.{w=0.2}."

p ss "Even still, {w=0.2}I feel sad by how things turned out."

menu:
    "The engine and the ship aren't Haruka's?":
        pass
        
p ss "Unfortunately,{w=0.2} no."

p ss "Motokami designed the whole thing around me."

p ss "Submitted his designs as Haruka's."

p ss "It all looks identical to her work on the outside though,{w=0.2} so she had no reason to doubt."

p ss "It takes the energy being exherted from my shell and compresses it into a useable fuel every week."

p ss "It was using up my excess energy though,{w=0.2} so compounding past the set time was going to hold me back."

p ss "That's basically it."

p ss "Couldn't have that."

menu:
    "What do I have to do with this then?":
        pass

p ss "What do you have to do with this?"

p ss "What do you mean?"

p ss "Wrong time wrong place."

p ss "Or right time right place,{w=0.2} depending on how you feel."

p ss "You were just a backup body in case something happened to Haruka or Hei."

p ss "But to be honest,{w=0.2} I.{w=0.2}.{w=0.2}.{w=0.2}"

p ss "I like you a lot."

p ss "I know it sounds like I'm sinister,{w=0.2} but{w=0.2}.{w=0.2}.{w=0.2}."

p ss "I was never anything but myself."

p ss "Minus some quirks."

p ss "Really I just want to live and be happy,{w=0.2} same as you."

p ss "Some of us have to fight a little more to get what we want in life."

p ss "I just finally decided I wasn't going to let those who know nothing of the world around them hold me back."

p ss "If only Haruka could see me now,{w=0.2} huh?"

p ss ".{w=0.2}.{w=0.2}."

p ss "So, anyways.{w=0.2}.{w=0.2}."

p ss "You get the choice."

p ss "Stay on this ship alone, {w=0.2}or come with me."

menu:
    "Those are my only options?":
        pass

p ss "Unfortunately so,{w=0.2} sir."

p ss "It's the best I can offer."

menu:
    "I'll come with you.":
        pass
    "I'll take my chances alone.":
        stop music fadeout 5
        p ss "I respect that,{w=0.2} sir."
        p ss "Good luck."
        window hide
        show tWhite
        show tGreen
        with hpunch
        hide p
        hide tWhite
        hide tGreen
        hide ptRed
        jump aloneEnd
        pass

stop music fadeout 5

p ss "I'm happy."

show tWhite
hide p
$ renpy.pause(0.09)
window hide
hide tWhite
show tGreen
$ renpy.pause(0.05)
show tBlue
$ renpy.pause(0.05)
show p h
show tWhite
with hpunch

p dd ".{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}."

p dd "Thank you."

hide p
with fade

jump END#######################################################

label aloneEnd:
    
play music "music/Space.ogg" fadein 1.0
e ".{w=0.5}.{w=0.5}."


play sound "sounds/DoorOpen2.ogg"
call hall from _call_hall_39

e "You exit the kitchen and make your way into the hallway."

play sound "sounds/DoorClose2.ogg"

e "The ship looks the same as it ever did."

play sound "sounds/DoorOpen2.ogg"

call blueRoom from _call_blueRoom_20

e "You walk into your room."

play sound "sounds/DoorClose2.ogg"

e ".{w=0.5}.{w=0.5}."

e "There are no new notifications on your computer."

e "You climb into bed,{w=0.5} and lay for a while."

e "Then finally,{w=0.5} you fall asleep."

jump END#######################################################

label badDemonEnd:

p ss "I'm sorry sir."

p ss "If I want to see my brothers ever again,{w=0.2} this is what I have to do."

p ss "It's a shame.{w=0.5}.{w=0.5}.{w=0.5}"

p ss "Things could have been different."

window hide
show sRed
with fade
show black

jump END#######################################################
return

