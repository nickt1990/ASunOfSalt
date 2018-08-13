label NHL:

show p n

p n ".{w= 0.15}.{w= 0.15}."

p n "I'm alright with whatever the captain decides."

p n "My personal preference.{w= 0.15}.{w= 0.15}. is that we don't do it."

show y su

y su "What?"

y n "Why?"

show p n

p n "I'd like to stick to the mission parameters."

p n "I think it would be irresponsible to potentially throw away a resource that the stations are expecting to be here."

show y m

y m "A resource? We're dead to them."

y n "They're expecting a message or two from us with a little information,{w= 0.15} and that's it."

y n "Let's do this for.{w= 0.15}.{w= 0.15}."

y n ".{w= 0.15}.{w= 0.15}."

y h "For ourselves."

y n "Let's see something nobody else has."

show p s

p s "I have to argue against that idea sir."

p n "Let's provide value for our friends and family back home."

show y m

y m "What if we don't have a family back home worth a damn?"

y m "What if we come up with nothing?"

show p n

p n "Then we take satisfaction knowing we were a stepping stone that helped the station get to the next mission that will help them."

show y m

y m "That's insane."

y n "Captain,{w= 0.15}what do you want to do?"

menu:
    "Compound.":
        jump HarukaEnd
        pass

    "Stop and follow our original orders.":
        jump TwoWeeks
        pass

label TwoWeeks: #END ---------------------------------------------------

p h "A wise choice,{w= 0.15} captain."

show y s

y s "Mmm."

y s ".{w= 0.15}.{w= 0.15}."

y n "Not what I would have done,{w= 0.15} obviously."

y n "But.{w= 0.15}.{w= 0.15}."

y n "You know what?"

y n "It's cool."

y h "I meant it when I said I was sorry for how I've been acting,{w= 0.15}Nema."

y n "I'm going to back off a little and let you and Hei step up."

show p h

p h "Thank you Haruka."

p n "I think we'll really surprise you."

show y n

y n "I hope so,{w= 0.15} but if you don't.{w= 0.15}.{w= 0.15}."

y h "That's fine."

e "Haruka and Nema look content."

show y n

y n "Cap,{w= 0.15} you can head back to bed after all."

y h "Let's give Nema a chance to shine here,{w= 0.15} yeah?"

y n "I'll talk to ya in the morning."

show p h

p h "Goodnight Captain."

menu:
    "G'night.":
        pass

call hall from _call_hall_43

hide y
hide p

play sound "sounds/DoorClose2.ogg"

e "You walk out of the room."

e "You hear the two girls talking quietly behind you as the door closes."

call blueRoom from _call_blueRoom_21

e "You walk back into your room and lay on the bed."

window hide
show black
with fade

e "After a few moments,{w= 0.15} you fall asleep."

stop music fadeout 1

e ".{w= 0.15}.{w= 0.15}."

play music "music/Space.ogg" fadein 1.0

e "Two weeks later."

jump day29