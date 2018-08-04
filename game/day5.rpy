label day5:

e "You hear sound coming from nearby."

show y n

y n "Cap?"

y n "Cap you okay?"

menu:
    "What happened?":
        pass

y s "We clipped a space rock at high speed."

y n "Luckily shields were up, {w=0.15}so no damage to the ship as far as I know.{w=0.25}"

y n "We managed to lose track of whatever else was there too."

menu:
    "Is everyone alright?":
        pass

y h "Yep, {w=0.15}everyone's fine."

y s "You got the worst of it, {w=0.15}lucky you."

menu:
    "Are we still with the asteroid?":
        p su "What do you mean sir?"
        
        p s "Wait.{w=0.15}.{w=0.15}."
        pass

    "Why are we sitting in the dark?":
        show r su
        r su "The dark?"
        pass

show p su

p su "Oh no.{w=0.15}.{w=0.15}."

show y su

y su "Cap, {w=0.15}can you see me?"

y s "How many fingers am I holding up?"

menu:
    "No, {w=0.15}I can't see.":
        pass

    "Three?":
        y "Wait can you see or not?"
        
        r "He said three."
        
        y "I know he said three idiot, {w=0.15}but that sounded like a question."
        
        p "Captain, {w=0.15}was that a guess?"
        pass

y m "Goddammit. "

y n "Nema, {w=0.15}you had the medical training right."

show p su

p su "I did, {w=0.15}Haruka."

show y n

y n "Take a look, {w=0.15}can ya?"

show p s

p s "A-absolutely, {w=0.15}yes, {w=0.15}a-alright, {w=0.15}one moment please."

e "There's a slight rustling sound."

e "You catch a light fragrance, {w=0.15}it's faint, {w=0.15}but it almost smells like a garden."

menu:
    "Nema, {w=0.15}you smell nice.":
        p su "T-thank you, {w=0.15}sir.{w=0.15}.{w=0.15}."

        p n ".{w=0.15}.{w=0.15}."

        p su "Oh! Right.{w=0.15}.{w=0.15}."
        pass

    ".{w=0.15}.{w=0.15}.":
        pass

p n "O-one moment sir, {w=0.15}please hold still."

e "Soft skin touches your face."

e "Fingertips."

e "They're gentle and quick."

show r h

r h "Cap my boy, {w=0.15}if you're blind forever, {w=0.15}I will take your place as the alpha."

show y h

y h "Right, {w=0.15}we need a captain who reacts to danger hurling his face into a toilet."

show r s

r s "Well. I wasn't scared, {w=0.15}I had to go, {w=0.15}I wasn't going to let that little surprise change my schedule."

show y m

y m "No. That's not true."

show r s

r s "It's not true, {w=0.15}but it wasn't very nice to make fun of me for it."

show p n

p n "OK, {w=0.15}lean back sir."

e "You feel Nema move very closely to you."

e "Her warm breath just barely reaches your forehead."

p n "I see.{w=0.15}.{w=0.15}."

show y su

y su "How's it look?"

show r h

r h "Yeah, {w=0.15}how are the ol' balls?"

show p h

p h "It looks like there's minimal damage. If he takes two toreg pills he'll be alright in a day with luck."

show y n

y n "Good, {w=0.15}get on it."

show p n

p n "Of course, {w=0.15}let me grab them, {w=0.15}one moment."

show y m

y m "This is strange."

y m "I mean, what the hell, {w=0.15}how does that even happen."

y s "You look totally fine Cap."

y n "Weird."

show p n

p n "Please hold out your hand sir."

e "Two small pills are placed in your hand."

menu:
    "Swallow pills.":
        pass

show y n

y n "All good?"

show p n

p n "Yes, {w=0.15}now we just have to wait."

show y n

y n "Alright, {w=0.15}and you will wait with Cap."

y m "After all you WERE the one that told us it was fine to drive directly into a huge rock."

show p s

p s "I-I know.{w=0.15}.{w=0.15}."

p s "Captain, {w=0.15}I'm so very sorry."

p n "I'll never be able to make it up to you, {w=0.15}I know, {w=0.15}but.{w=0.15}.{w=0.15}.{w=0.15} please know that it was a mistake."

p n "C-{w=0.15}captain I.{w=0.15}.{w=0.15}. I.{w=0.15}.{w=0.15}."

menu:
    "It's alright Nema.":
        pass

    "It was a risk, {w=0.15}I should have known better.":
        pass

p su "Sir.{w=0.15}.{w=0.15}."

p s "I will gladly watch the Captain.{w=0.35} Of course."

show y m

y m "Well.{w=0.15}.{w=0.15}. good? You don't really have a choice, {w=0.15}but, {w=0.15}right."

y n "Hei and me are gonna take a look around to make sure everything's okay."

show r s

r s "But I'm sore from the crash.{w=0.15}.{w=0.15}."

show y n

y n "Unless you want to be dead from something else, {w=0.15}you're helping."

show r n

r n "Whatever, {w=0.15}I guess I'll give this place my best peek."

show y s

y s "Then do it. Please?"

show r h

r h "Hei Babe is on the case, {w=0.15}madam."

show y n

y n "Be back soon Cap."

show r h

r h "Don't die on us bro."

play sound "sounds/Slap.ogg"

e "You hear a slapping sound."

r s "Ouch, {w=0.15}rude."

play sound "sounds/DoorOpen2.ogg"

hide r
hide y

e "You hear Hei and Haruka walk out the door."

play sound "sounds/DoorClose2.ogg"

e "There is silence for a while."

show p s

play music "music/MelancholyPiano.ogg" fadein 3.0

p s ".{w=0.15}.{w=0.15}."

p s "C-captain, {w=0.15}I just want to say again that I'm sorry."

p n "I panicked, {w=0.15}I didn't even register what I was seeing or doing."

p s "I p-{w=0.15}put your life in danger by being so weak."

menu:
    "You did the best you could.":
        p m "But my best isn't good enough!"
        pass

    "I know you're capable of better, {w=0.15}Nema.":
        p s "I know sir, I apologize.{w=0.15}.{w=0.15}."
        p s "The more time that passes the more I realize I'm just not meant for this life."
        pass

p s "Haruka was amazing. She took charge, {w=0.15}she kept calm."

p n "She can be a little abrupt sometimes, {w=0.15}but she is a leader."

p s "I'm not a leader,{w=0.15} Captain. "

p s "I have difficulty even standing up straight when I'm startled."

p n "Even Hei fought through his anxiety and was able to perform his tasks."

p n "He acts like a goof, {w=0.15}but he came through when we needed it."

p s "What good am I if I only serve to take up space?"

p s "I'm the weak link in our crew, {w=0.15}I know I am."

p s "I've known since the first day, {w=0.15}Haruka knew too."

p s "She's the type of person who thrives off of excellence, {w=0.15}and I think it worries her that she might have to put her life in the hands of a sub-par person like me."

p s "I want to get stronger Captain, {w=0.15}but what do I do?"

p n "You can't practice traumatic events."

p n "You just have to be the kind of person who can step up and take charge, {w=0.15}who doesn't care if they step on another's toes, {w=0.15}or gets in another's face."

p s "I'm not that person,{w=0.15} and I never will be."

p s ".{w=0.15}.{w=0.15}."

menu:
    "You can be.":
        p su "Me? {w=0.15}I can be?"
        pass

    "Not with that attitude, {w=0.15}no.":
        p s "My attitude?"
        p s "Even still.{w=0.15}.{w=0.15}."
        pass

p s "I mean no disrespect sir, {w=0.15}but how could I ever be that?"

menu:
    "Push yourself. ":
        p s "I have been pushing myself."
        pass

    "Think differently.":
        p s "I try."
        pass



p s "I do every day, {w=0.15}sir."

p s "Just being around others, {w=0.15}trying to communicate, {w=0.15}that takes a toll on me."

p s "I just don't know how to push myself into being a dependable person when I struggle to just exist."

p s "And I can't stop being me. I'm weak, {w=0.15}captain."

p n ".{w=0.15}.{w=0.15}."

p s "I'm sorry for wasting your time with my self-pity sir. "

p n "You really should be getting some rest, {w=0.15}after all."

menu:
    "Okay.":
        p h "Good."
        pass

    "I don't mind.":
        p s "I have to insist."
        pass

p n "Here sir, {w=0.15}take this medicine. {w=0.15}You should get drowsy fairly quickly."

e "Nema puts another pill in your hand."

menu:
    "Swallow the pill.":
        pass
        
call blueRoom from _call_blueRoom_6

e "You hear Nema sit down beside you."

hide p

stop music fadeout 3

e "A moment passes, {w=0.15}and you drift off to sleep."

play music "music/Evil.ogg" fadein 2.0

window hide
show tRed

#todo demon

d "Rip."


d "Shred."


d "Piece by piece."


d "You'll burn at my hands, {w=0.15}and dance at my feet."


d "We shall be one, {w=0.15}and you shall be nothing."


d "Nothing but a limb of mine."


d "A hand to grasp your soul."

stop music fadeout 2.0

d "All of nothing."

window hide
hide tRed
show black
with fade

play music "music/Space.ogg" fadein 2.0

e ".{w=0.35}.{w=0.35}.{w=0.35}.{w=0.35}"

return