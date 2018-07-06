﻿label day4Night:

e "There is a loud thud."

menu:
    "...":
        pass

e "There's another loud thud. Then a few more."

menu:
    "Is Nema up to something again?":
        pass

call hall

e "You walk into the hallway."

e "Nema's already standing there."

show p n

menu:
    "Nema is that you?":
        pass

    "What's that sound?":
        pass
        
p n "No sir, this time it's not me."

e "Haruka emerges from her room."

show y m:
    linear 0 xalign 0.9 yalign 1.0

y m "Nema are you making those freakin' noises again? It's the middle of the night."

show p s

p s "N-no Haruka. I'll go check the radar."

e "The three of you walk into the navigation room."

call navRoom

play sound "sounds/DoorOpen2.mp3"

p n "Ok, let's see..."

e "After a moment Hei walks groggily into the room."

play sound "sounds/DoorClose2.mp3"

show r s:
    linear 0 xalign 0.1 yalign 1.0

r s "Hey guys, what's that sound?"

show y n

y n "Nemo's checkin'."

show r s

r s "Nibbler, what's going on?"

show p n

p n "One moment please..."

p s "Wait..."

p su "The ship we saw on the radar yesterday... it's on top of us."

show r su

r su "Wha-on top of us?!"

r su "Oh shit, oh god. Nope."

r su "Captain, do something!"

r su "Oh god, did they already capture us?"

menu:
    "Calm down.":
        pass

    "I don't know.":
        pass

r s "Oh god, oh no."

show y m

y m "I'm turning on the heavy external floods. Maybe we can light up whatever it is we're smackin' up against."

e "Haruka turns on the light, and you see a sea of blood and body parts floating around you."

y su "Oh my god..."

show p su

p su "Those... those.."

show y su

y su "They're people. Body parts."

y su "This is... blood?"

show r su

r su "..."

e "Hei runs out of the room into the bathroom."

hide r

menu:
    "Nema, what can we do?":
        pass

    "Haruka, what can we do?":
        pass

show p su

p su "W-we, u-uh- w-oh... w-ell we-"

e "There is a loud thud."

show y n

y n "Nema what's that."

show p su

p su "W-well, it's, a- it's-"

show y m

y m "Move."

y su "There's a ship here. It's moving up from below us... I think the blood is a trap."

y m "Captain, turn power to the shields, Nema, watch the radar for potential collision."

y m "HEI, WE NEED YOUR HELP."

show r su:
    linear 0 xalign 0.1 yalign 1.0

r su "I, but I can't..."

show y m #todo deal with hei being not in room

y m "GET YOUR ASS IN HERE."

show r s

r s "But..."

show y m

y m "DO YOU WANT TO GET THROUGH THIS? NOW."

show r s

r s "I'm here. OK. I'm alright."

r s "Jump on lasers. Hold your fire until I say."

show y n

y n "Captain, stay on the main controls. When I say, you need to jump into full boost."

y n "Nema, I really need you to watch for collisions, are you ok over there?"

show p s

p s "W-yeah, yes."

show y n

y n "Are you sure? You need to pay attention or we're dead."

show p n

p n "Yes, I'm alright, I'll be alright."

e "Haruka turns her attention to her computer."

e "She focuses for a long moment."

show y n

y n "OK, Captain, we can get a shot off on where the main ship shows on our radar, but I still advise that we get out of here immediately after. Our lack of visibility will give us huge issues if we don't. Do you want to fire a shot or just go?"

y m "What do you want to do?"

menu:
    "Fire whatever's necessary then get out of here.":
        pass

    "Just go, we shouldn't risk it.":
        pass

y n "OK, Hei, can you get a lock?"

show r s

r s "I think I have one."

show y m

y m "You need to know, there's no second chances."

show r s

r s "I'm pretty sure."

show y n

y n "God, Nema, are we clear?"

show p n

p n "..."

show y m

y m "NEMA."

show p n

p n "What? Yes. We're c-clear."

show y n

y n "Hei, if you're ready, fire on my mark. Captain, wait two seconds then get us the hell away from here."

y n "Everyone ready?"

y n "Three."

y n "Two."

y n "One."

y m "Hei now!"

show r su

r su "Right!"

#todo screen shake and stuff

e "There's a large flash of light and explosion."

show y su

y su "Captain!"

#todo one more option here
e "There is a timed prompt with two options. The easier of which will flahs you away. The other option leads to a bad end of everyone just dying here slowly."

e "The ship lurches forward and for a moment, you feel an intense force pushing you back."

menu:
    "We're going full speed.":
        pass

y h "Alright, then we should be goo-"

e "There is a loud crash."

show black
with fade

e "Everything is black."

return