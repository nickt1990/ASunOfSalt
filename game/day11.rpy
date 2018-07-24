label day11:

window hide
hide black
with fade

e "You wake up slowly and realize the body beside you is now gone."

#todo haru act different if last night is different
    
e "Haruka is out of sight."

e ".{w=0.15}.{w=0.15}."

e "She doesn't seem to be in the room."

e "Then,{w=0.15} you notice that there's a sandwich sitting on your bedside table.{w=0.15}.{w=0.15}."

menu:
    "Check it out.":
        pass

e "It's a plain ham sandwich with one bite taken out of it."

e ".{w=0.15}.{w=0.15}.{w=0.15}There's a note on it."

e "The note reads \"You can have the rest.\""

menu:
    "\"That's sweet?\"":
        pass

    "\"That's sweet.\"":
        pass

e "There's some sound coming from the hallway."

menu:
    "Check it out.":
        pass
        
call hall from _call_hall_10

play sound "sounds/DoorOpen2.mp3"

show y n

y n "Hey."

play sound "sounds/DoorClose2.mp3"

e "Haruka's sitting on the floor by the heater, covered in a blanket from her neck down."

menu:
    "Are the systems back up?":
        y n "For now. "
        y n "I turned them on for the morning so we could meet with the others."
        pass

    "How'd you sleep?":
        y h "Good."
        e "Haruka looks down for a moment, as if thinking."
        y n "I turned the systems back on so we could meet up with everyone.{w=0.15} Just so you know."
        pass


y s ".{w=0.15}.{w=0.15}."

y n "Want to sit?"

menu:
    "Sure.":
        e "You sit down next to her."
        e "The warm air from the heater shoots up the back of your shirt."
        y n "Blanket?"
        menu:
            "Of course.":
                e "You wrap yourself up with the blanket and she pulls in closely to you."
                e "Her skin is so warm from the heat,{w=0.15} it's almost hot."
                y s "Hey,{w=0.15} Cap.{w=0.15}.{w=0.15}."
                pass
        pass

    "No thanks.":
        y s "Oh, sorry."
        y n "I didn't mean anything by it."
        y s "I just wanted to say.{w=0.15}.{w=0.15}."
        pass



y n "I'm sorry about last night."

y s "I know I'm kind of awkward when it comes to stuff like that."

y n "I just wanted to let you kn-"

play sound "sounds/DoorOpen2.mp3"

show r h:
    linear 0.0 xalign 0.1 yalign 1.0

r h "Morning Chumps."

r n "Have a cozy night?"

e "Hei winks at Haruka."

show y m

y m "God."

y n "The day hasn't even started yet and you're at it already."

show r su

r su "Woah."

r n "Apparently not such a hot night."

show y n

y n ".{w=0.15}.{w=0.15}."

show r h

r h "Well, {w=0.15}our night was HOT."

show y m

y m "Disgusting."

show r n

r n "H{w=0.25}-O{w=0.25}-"

show p m:
    linear 0.0 xalign 0.9 yalign 1.0

p m "Hei, please."

p m "Do not patronize them."

show r n

r n "Whatevs."

r h "Just letting her know what she's missing out on."

show y su

y su "Do you even hear this Nema?"

y m "You're doing an excellent job walking back any progress I thought you'd made."

y m "I don't know why I'm surprised."

show p h

p h "Don't worry Haruka,{w=0.15} it was a really fun sleepover."

p n "Not quite what I'd always imagined they'd be like as a kid,{w=0.15} but{w=0.15}.{w=0.15}.{w=0.15}."

p h "Fun."

show y n

y n "Dear god."

show r n

r n "So onto what we all really care about."

r h "We switchin' roomies?"

show y s

y s "W-what?"

show p h

p h "Oh sure, I'd be alright with that."

p n "That could be interesting."

show y s

y s "Well, we don't have to switch."

y n "I mean, it would probably be easier to just stay with how things are, right?"

show r su

r su "Maybe somebody had a better time than we thought, huh Nebo?"

show p su

p su "You think so?"

p n "Did you have a nice night with Captain Haruka?"

p h "We can stay in the same rooms again, I had a lot of fun with Hei."

show y su

y su "Oh, well."

y h "Yeah, I mean-"

show r h

r h "Nope!"

r h "Gotta switch!"

r n "Dude."

e "Hei looks you in the eyes,{w=0.15} hopeful."

r n "You stay with Nema,{w=0.15} I'm with Haruka,{w=0.15} good?"

r n "Good."

show y su

y su "Woah woah,{w=0.15} what?"

y n "Did I mishear that?"

y m "What in the world makes ya think I'd be even half alright with that?"

show r n

r n "Because I want another chance."

show y h

y h "I couldn't give less of a shit about what you want."

show r s

r s "Please Haruka, {w=0.15}I know I've been a dick."

r n "But have you ever thought that maybe it's because you've never given me a real shot?"

r n "Have we ever had a one on one conversation before?"

r s "Even one?"

show y s

y s "Well,{w=0.15} not really.{w=0.15}.{w=0.15}."

show p h

p h "I think it's a great idea."

p n "We can make effective use of our time with limited power to build our strength as a team."

show r n

r n "We have no strength as a team Haruka."

r s "Is that what you want?"

show y m

y m "Ugh.{w=0.15}.{w=0.15}."

y s "But.{w=0.15}.{w=0.15}."

e "Haruka looks at you with a defeated look."

y s ".{w=0.15}.{w=0.15}."

y n "What do ya think Cap?"

menu:
    "Let's just stick with the same roommates.":
        r s "No!"
        pass

    "Let's switch.":
        pass

show r s

r s "Please?"

r n "I'm trying to make right."

r n "I don't want to be stuck in this weird hostile environment forever."

r s "Give me a chance dude."

show y s

y s "Fine."

y m "I'll do it."

menu:
    "Are you sure?":
        pass

    "Alright.":
        pass

y m "Yeah,{w=0.15} whatever."

show r h

r h "Haruka!"

r h "Thank you!"

r h "I promise, come tomorrow, you'll see this hunk in a new light."

show y h

y m "Let's not get ahead of ourselves."

show p h

p h "I'm happy you are willing to give Hei a chance Haruka."

p h "He spoke a lot about getting a second chance with you last night,{w=0.15} I think he'll really give it his all."

show y m

y m "Skeptical,{w=0.15} but whatever."

show r h

r h "It's about time to get back to our rooms, right?"

show y s

y s "Ugh.{w=0.15}.{w=0.15}."

show p h

p h "Have a wonderful night you two."

p h "I look forward to getting to spend some time with you as well, Sir."

show y s

y s ".{w=0.15}.{w=0.15}."

play sound "sounds/DoorOpen2.mp3"

hide p

e "Nema turns and heads off to your room."

show r h

r h "Haru baby,{w=0.15} I'll be in my room."

r h "Come on in whenever you're ready."

play sound "sounds/DoorOpen2.mp3"

hide r

e "Hei jogs off to his room."

show y n

y n "Well.{w=0.15}.{w=0.15}."

y s ".{w=0.15}.{w=0.15}."

y s "I have to go turn on energy conservation."

e "Haruka looks down at the ground sadly."

y s ".{w=0.15}.{w=0.15}."

y s "Better get back to your room."

hide y

play sound "sounds/DoorOpen2.mp3"

e "Haruka walks off toward the navigation room."

play sound "sounds/DoorClose2.mp3"

call blueRoom from _call_blueRoom_5

e "You turn the other way and walk into your room."


return