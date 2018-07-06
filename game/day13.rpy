label day13:
    
e "You have the room to yourself."

menu:
    "Check mail":
        pass

    "Get breakfast":
        pass

e "Checking mail."

play sound "sounds/DoorOpen2.mp3"

e "You stand up and walk out into the hallway."

e "No sign of anyone."

e "As you walk closer to the kitchen you can hear the sound of somebody rustling through items in the fride."

e "The kitchen door is open, Haruka is sitting at the table and Hei is at the fridle,{w=0.15} looking around."

show r h

r h "Uhh, so we have...{w=0.15} uhm..."

r n "What do I know how to make..."

r h "You want some cereal?"

show y m:
    linear 0 xalign 0.9 yalign 1.0

y m "You said you'd make breakfast."

y m "Not pour cereal."

show r s

r s "Yeaaaah, I did didn't I."

r m "Hmm..."

show y su

y su "Oh!"

y h "Hey Cap!"

e "Haruka smiles and waves you over."

y h "C'mon, sit,{w=0.15} Hei's making us breakfast."

show r s

r s "Breakfast for three people now, right."

e "Haruka moves in close to you and speaks in a hushed tone."

show y n

y n "We chatted earlier this morning and he said he wanted to try and do better."

y h "I doubt anything will change,{w=0.15} but if I can get at least one breakfast out of it then whatever."

show r m

r m "Did I hear you doubting me over there?"

show y n

y n "Yes."

show r n

r n "..."

e "Hei goes back to cooking."

show y h

y h "It's been great so far. "

show r h

r h "You think so?"

show y m

y m "It's been five minutes bud,{w=0.15} my expectations are still low."

show r s

r s "Fine."

e "Hei turns away from you two and focuses on cooking."

e "You and Haruka sit for a moment, {w=0.15}and then she looks up at you."

show y n

y n "You know, I haven't seen Nema since yesterday."

y h "Not that I'm complaining,{w=0.15} just sort of strange."

y n "She's usually the first up."

menu:
    "She had a rough day yesterday.":
        pass

    "I'm sure she's around.":
        pass

y n "What, you mean our argument?"

y m "Shit, that was nothing. "

y m "If that's seriously what it is,{w=0.15} I'm a lil' annoyed, ya know?"

y n "Yeah we argued,{w=0.15} but we kind of live together, get over it."

menu:
    "You were pretty rude to her.":
        pass

    "Right.":
        pass

y n "Well."

y h "Yeah, {w=0.15}I was a little bit."

y n "I just can't see eye to eye with her."

y n "I'm fine not being friends with her,{w=0.15} but I don't want her to come inbetween..."

y n "I don't want her to make life harder than it has to be."

show r s

r s "I think she's sad because of me."

show y su

y su "You?"

y n "What did you do?"

show r s

r s "I don't know,{w=0.15} neglecting her or something?"

show y n

y n "Well whatever,{w=0.15} go apologize."

show r n

r n "I'm proving myself here,{w=0.15} she'll come around."

r h "Food's ready by the way."

e "Hei sets two plates on the table, each with two eggs on them."

e "Sunny side up."

show y n

y n "..."

y h "Better than I expected."

y n "Thank you."

show r h

r h "Really?"

r n "See?{w=0.15} I'm not so bad."

show y n

y n "If that's true then ya don't have to keep saying it."

show r n

r n "Fair enough."

show y n

y n "Anyways, {w=0.15}Cap."

y n "After we eat, {w=0.15}I'm going to catch Hei up on the systems."

y n "But later tonight,{w=0.15} you got some time to go over some reports with me?"

menu:
    "Sure.":
        pass

    "No.":
        pass

y h "Perfect."

y n "I'll come to your room later."

y n "Tomorrow's the engine compound and I want to make sure everythings in order after all the weird stuff that's been happening."

menu:
    "No problem.":
        pass

    "Whatever.":
        pass

e "Haruka smiles at you and continues to eat."

e "You finish your eggs and head out of the kitchen.{w=0.15}.{w=0.15}."

hide y
hide r

play sound "sounds/DoorOpen2.mp3"

e "And into your room,{w=0.15} to get some work done on your computer."

play sound "sounds/DoorClose2.mp3"

e "Some time passes,{w=0.15} and you hear a knock on your door."

menu:
    "Open the door":
        pass

play sound "sounds/DoorOpen2.mp3"

y h "Heya Cap!"

menu:
    "Good evening.":
        pass

y n "How's it goin'?"

y h "Pretty quiet day, {w=0.15}huh?"

menu:
    "Yeah.":
        pass

    "I guess.":
        pass

y n "So..."

e "Haruka walks right up in front of you."

y n "I just wanted to say that,{w=0.15} uhm."

e "Her hands are figeting."

y h "Well."

menu:
    "Yes?":
        pass

    "You alright?":
        pass

y n "You know,{w=0.15} I can't actually remember."

y h "Whatever."

e "Haruka starts to walk out your door,{w=0.15} then turns around."

y n "Oh,{w=0.15} and..."

y s ".{w=0.15}.{w=0.15}."

y h "Nevermind!"

y h "I have work to do,{w=0.15} talk to ya later."

play sound "sounds/DoorClose2.mp3"

hide y

e "Haruka walks out into the hall."

e "You lay on your bed for a while, {w=0.15}and then drift off to sleep."


return