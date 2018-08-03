label day4Night:

e "There is a loud thud."

menu:
    ".{w=0.15}.{w=0.15}.":
        pass

e "There's another loud thud.{w=0.25} Then a few more."

window hide
hide black
show tBlack

menu:
    "Is Nema up to something again?":
        pass

play sound "sounds/DoorOpen2.ogg"

call hall from _call_hall_2

e "You walk into the hallway."

e "Nema's already standing there."

show p n

menu:
    "Nema is that you?":
        p n "No sir, {w=0.15}this time it's not me."
        pass

    "What's that sound?":
        p s "I'm not sure, Captain."
        pass
        
e "Haruka emerges from her room."

show y m:
    linear 0 xalign 0.9 yalign 1.0

y m "Nema are you making those freakin' noises again? It's the middle of the night."

show p s

p s "N-no Haruka. {w=0.15}I'll go check the radar."

call navRoom from _call_navRoom
play sound "sounds/DoorOpen2.ogg"

e "The three of you walk into the navigation room."

p n "Ok, {w=0.15}let's see.{w=0.15}.{w=0.15}."

e "After a moment Hei walks groggily into the room."

play sound "sounds/DoorClose2.ogg"

show r s:
    linear 0 xalign 0.1 yalign 1.0

r s "Hey guys, {w=0.15}what's that sound?"

show y n

y n "Nemo's checkin'."

show r s

r s "Nibbler, {w=0.15}what's going on?"

show p n

p n "One moment please.{w=0.15}.{w=0.15}."

p s "Wait.{w=0.15}.{w=0.15}."

p su "The ship we saw on the radar yesterday.{w=0.15}.{w=0.15}. it's almost on top of us."

show r su

r su "Wha-on top of us?!"

r su "Oh no, {w=0.15}oh god."

r su "Captain, {w=0.15}do something!"

r su "Oh god, {w=0.15}did they already capture us?"

menu:
    "Calm down.":
        pass

    "I don't know.":
        pass

r s "Oh god, {w=0.15}oh no."

show y m

y m "I'm turning on the heavy external floods.{w=0.15} Maybe we can light up whatever it is we're smackin' up against."

window hide#todo test this transition
show ptRed
with fade

e "Haruka turns on the light, {w=0.15}and you see a sea of blood and body parts floating around you."

y su "Oh my god.{w=0.15}.{w=0.15}."

show p su

p su "Those.{w=0.15}.{w=0.15}. those{w=0.15}.{w=0.15}.{w=0.15}."

show y su

y su "They're people.{w=0.15} Body parts."

y su "This is.{w=0.15}.{w=0.15}. blood?"

show r su

r su ".{w=0.15}.{w=0.15}."

e "Hei runs out of the room into the bathroom."

hide r

menu:
    "Nema, {w=0.15}what can we do?":
        pass

    "Haruka, {w=0.15}what can we do?":
        y n "Nema's the one with the information right now."
        y n "What do we do Nema?"
        pass

show p su

p su "W-we, {w=0.15}u-uh- w-oh.{w=0.15}.{w=0.15}. w-ell we-"

e "There is a loud thud."

show y n

y n "Nema what's that."

show p su

p su "W-well, {w=0.15}it's, {w=0.15}a- it's-"

show y m

y m "Move."

y su "There's something else here.{w=0.15} It's moving up from below us.{w=0.15}.{w=0.15}.{w=0.15} I think the blood is a decoy."

y m "Captain, {w=0.15}turn power to the shields, {w=0.15}Nema, {w=0.15}watch the radar for potential collision."

y m "HEI, {w=0.15}WE NEED YOUR HELP."

show r su:
    linear 0 xalign 0.1 yalign 1.0

e "You can hear Hei through the doorway."

r su "I, {w=0.15}but I can't.{w=0.15}.{w=0.15}."

y m "GET YOUR ASS IN HERE."

e "Hei shuffles into the room."

show r s

r s "But.{w=0.15}.{w=0.15}."

show y m

y m "DO YOU WANT TO GET THROUGH THIS?{w=0.25} NOW."

show r s

r s "I'm here.{w=0.15} OK. {w=0.15}I'm alright."

y m "Jump on lasers. {w=0.15}Hold your fire until I say."

y m "We have no idea what exactly is there,{w=0.15} or where to shoot right now,{w=0.15} but we need to be prepared."

show y n

y n "Captain, {w=0.15}stay on the main controls.{w=0.25} When I say, {w=0.15}you need to jump into full boost."

y n "Nema, {w=0.15}I really need you to watch for collisions, {w=0.15}are you okay over there?"

show p s

p s "W-yeah, {w=0.15}yes."

show y n

y n "Are you sure? You need to pay attention or we're dead."

show p n

p n "Yes, {w=0.15}I'm alright, {w=0.15}I'll be alright."

e "Haruka turns her attention to her computer."

e "She focuses for a long moment."

show y n

y n "OK, {w=0.15}Captain, {w=0.15}we can get a shot off on where the main ship shows on our radar, {w=0.15}but I still advise that we get out of here immediately after.{w=0.15} Our lack of visibility will give us huge issues if we don't."

y n "Do you want to fire a shot or just go?"

#todo make both sides of this an ending
menu:#todo this leads to you potentially hitting "yourself" ~ ending - Blow them up and then in the end it's you? Set up a warp jump that's you traveling through time at some point. (Here?)
    "Fire whatever's necessary then get out of here.":
        pass

    "Just go, {w=0.15}we shouldn't risk it.":
        pass

y n "OK, {w=0.15}Hei, {w=0.15}can you get a lock?"

show r s

r s "I think I have one."

show y m

y m "You need to know, {w=0.15}there's no second chances."

show r s

r s "I'm pretty sure."

show y n

y n "God, {w=0.15}Nema, {w=0.15}are we clear?"

show p n

p n ".{w=0.15}.{w=0.15}."

show y m

y m "NEMA."

show p n

p n "What?{w=0.15} Yes.{w=0.25} We're c-{w=0.15}clear."

show y n

y n "Hei, {w=0.15}if you're ready, {w=0.15}fire on my mark.{w=0.15} Captain, {w=0.15}wait two seconds then engage the boost."

y n "Everyone ready?"

y n "Three."

y n "Two."

y n "One."

y m "Hei now!"


show r su

r su "Right!"

window hide
hide ptRed
show tWhite #todo test white and play thru this part
with hpunch

play sound "sounds/Explosion.ogg"

e "There's a large flash of light and explosion."

show y su

y su "Captain,{w=0.15} now!"

menu:
    "Engage.":
        pass

play sound "sounds/Boost.ogg"        

$ renpy.pause(0.09)
window hide
hide tWhite
show tGreen
$ renpy.pause(0.05)
show tBlue
$ renpy.pause(0.05)
show tWhite
with hpunch

e "The ship lurches forward and for a moment, {w=0.15}you feel an intense force pushing you back."

window hide
hide white
with fade

y h "Alright, {w=0.15}then we should be goo-"

play sound "sounds/Explosion2.ogg"

window hide
show black
with fade

e "There is a loud crash."

e "Everything goes completely dark."

return