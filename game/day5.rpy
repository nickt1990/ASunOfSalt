label day5:

#todo make everything dark
e "Everything is dark..."

e "But you hear sound coming from nearby."

show y n

y n "Cap?"

y n "Cap you ok?"

menu:
    "What happened?":
        pass

    "Is everyone alright?":
        pass

y s "We clipped a space rock at high speed."

y n "Luckily shields were up, so there was no damage to the ship as far as I know. We managed ta lose track of the ship as well."

menu:
    "And what about everyone else?":
        pass

y h "Yep, everyone's OK."

y s "You got the worst of it, lucky you."

menu:
    "Are we still behind the asteroid?":
        pass

    "Why are we sitting in the dark?":
        pass

show r su

r su "The dark?"

show p su

p su "Oh no..."

show y su

y su "Cap, can you see me?"

y s "How many fingers am I holding up?"

menu:
    "No, I can't see.":
        pass

    "Three?":
        y "Wait can you see or not?"
        
        r "He said three."
        
        y "I know he said three idiot, but that sounded like a question."
        
        p "Captain, was that a guess?"
        pass

y m "Goddammit. "

y n "Nema, you had the medical training right."

show p su

p su "I did, Haruka."

show y n

y n "Take a look, can ya?"

show p s

p s "A-absolutely, yes, a-alright, one moment please."

e "There's a slight rustling sound."

e "You catch a light fragrance, it's faint, but it almost smells like a garden."

menu:
    "Nema, you smell nice.":
        pass

    "...":
        pass

p su "T-thank you, sir..."

p n "..."

p su "Oh! Right..."

p n "O-one moment sir, please just hold still."

e "Soft skin touches your face."

e "Fingertips."

e "They're gentle and quick. "

show r h

r h "Cap bap, if you're blind forever, I will take your place as the alpha."

show y h

y h "Right, we need a captain who reacts to danger hurling his face into a toilet."

show r s

r s "Well. I wasn't scared, I had to go, I wasn't going to let that little surprise change my schedule."

show y m

y m "No. That's not true."

show r s

r s "It's not true, but it wasn't very nice to make fun of me for it."

show p n

p n "OK, lean back sir."

e "You feel Nema move very closely to you."

e "Her warm breath just barely reaches your forhead."

p n "I see..."

show y su

y su "How's it look?"

show r h

r h "Yeah, how are the ol' balls?"

show p h

p h "It looks like there's minimal damage. If he takes two toreg pills he'll be alright in a day with luck."

show y n

y n "Good, get on it."

show p n

p n "Of course, let me grab them, one moment."

show y m

y m "What the hell, how does that even happen."

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

p n "Yes, now we just have to wait."

show y n

y n "Alright, and you will wait with Cap."

y m "After all you WERE the one that told us it was OK to drive directly into a huge rock."

show p s

p s "I-I know..."

p s "Captain, I'm so very sorry."

p n "I'll never be able to make it up to you, I know, but I- b- I, please know that it was a mistake."

p n "C-captain I... I..."

menu:
    "It's OK Nema.":
        pass

    "It was a risk, I should have known better.":
        pass

p su "Sir..."

p s "I will gladly watch the Captain. Of course."

show y m

y m "Well... good? You don't really have a choice, but, right."

y n "Hei and me are gonna take a look around to make sure everything's OK."

show r s

r s "But I'm sore from the crash..."

show y n

y n "Unless you want to be dead from something else, you're helping."

show r n

r n "Whatever, I guess I'll give this place my best peek."

show y s

y s "Then do it. Please?"

show r h

r h "Hei Babe is on the case, madam."

show y n

y n "Be back soon Cap."

show r h

r h "Don't die on us bro."

e "You sound a slapping sound."

r s "Ouch, rude."

play sound "sounds/DoorOpen2.mp3"

e "You hear Hei and Haruka walk out the door."

play sound "sounds/DoorClose2.mp3"

e "There is silence for a while."

show p s

p s "..."

p s "C-captain, I just want to say again that I'm sorry."

p n "I panicked, I didn't even register what I was seeing or doing."

p s "I p-put your life in danger. I'm weak, I panicked."

menu:
    "You did the best you could.":
        pass

    "I know you're capable of better, Nema.":
        pass

p m "But my best isn't good enough!"

p s "Haruka was amazing. She took charge, she kept calm."

p n "She can be a little abrupt sometimes, but she is a leader."

p s "I'm not a leader captain. "

p s "I have difficulty even standing up straight when I'm startled."

p n "Even Hei fought through his anxiety and was able to perform his tasks."

p n "He acts like a goof, but he came through when we needed it."

p s "What good am I if I only serve to take up space?"

p s "I'm the weak link in our crew, I know I am."

p s "I've known since the first day, Haruka knew too."

p s "She's the type of person who thrives off of excellence, and I think it worries her that she might have to put her life in the hands of a sub-par person like me."

p s "I want to get stronger captain, but what do I do?"

p n "You can't practice traumatic events."

p n "You just have to be the kind of person who can step up and take charge, who doesn't care if they step on another's toes, or gets in anothers face."

p s "I'm not that person and I never will be."

p s "..."

menu:
    "You can be.":
        pass

    "Not with that attitude, no.":
        pass

p su "Me? I can be?"

p s "I mean no disrespect sir, but how could I ever be that?"

menu:
    "Push yourself. ":
        pass

    "Think differently.":
        pass

p s "I have been pushing myself."

p s "I do every day, sir."

p s "Just being around others, trying to communicate, that takes a toll on me."

p s "I just don't know how to push myself into being a dependable person when I struggle to just exist."

p s "And I can't stop being me. I'm weak, captain."

p n "..."

p s "I'm sorry for wasting your time with my self-pity sir. "

p n "You really should be getting some rest, after all."

menu:
    "OK.":
        pass

    "I don't mind.":
        pass

p h "Good."

p n "Here sir, take this medicine. You should get drowsy fairly quickly."

e "Nema puts a pill in your hand."

menu:
    "Swallow the pill.":
        pass
        
call blueRoom

e "You hear Nema set down beside you."

e "A moment passes, and you drift off to sleep."


d "Rip."


d "Shred."


d "Piece by piece."


d "You'll burn at my hands, and dance at my feet."


d "We shall be one, and you shall be nothing."


d "Nothing but a limb of mine."


d "A hand to grasp your soul."


d "All of nothing."

hide r

hide y

hide p


return