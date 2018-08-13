label day13:
    
e ".{w=0.15}.{w=0.15}."

e ".{w=0.35}.{w=0.35}."
    
e "After two nights of sharing,{w=0.15} you have the room to yourself."

e "You wake up alone and slowly sit up."

hide ptBlack
window hide
hide black
with fade

e "Your computer screen flashes a notification symbol."

window hide
show black 
with fade

menu:#computer
    "Check mail.":
        label summariesD13:
        menu:
            "Haruka's summary.":
                call day13HaruS from _call_day13HaruS
                jump summariesD13
                pass
            "Hei's summary.":
                call day13HeiS from _call_day13HeiS
                jump summariesD13
                pass
            "Nema's summary.":
                call day13NemaS from _call_day13NemaS
                jump summariesD13
                pass
            "Junk mail.":
                call bMail9 from _call_bMail9
                jump summariesD13
                pass
            "I think I'm done.":
                jump day13Start
                pass                
        pass

    "Get breakfast.":
        jump day13Start
        pass

label day13Start:

window hide
hide black 
with fade

play sound "sounds/DoorOpen2.ogg"

call hall from _call_hall_3

e "You stand up and walk out into the hallway."

e "No sign of anyone."

e "As you walk closer to the kitchen you can hear the sound of somebody rustling through items in the fridge."

call kitchen from _call_kitchen_1

play music "music/ChillVib.ogg" fadein 1.0

e "The kitchen door is open, Haruka is sitting at the table and Hei is at the fridge,{w=0.15} looking around."

show r h

r h "Uhh,{w=0.15} so we have.{w=0.15}.{w=0.15}.{w=0.15} uhm.{w=0.15}.{w=0.15}."

r n "What do I know how to make.{w=0.15}.{w=0.15}."

r h "You want some cereal?"

show y m:
    linear 0 xalign 0.1 yalign 1.0

y m "You said you'd make breakfast."

y m "Not pour cereal."

show r s

r s "Yeaaaah,{w=0.15} I did didn't I."

r m "Hmm.{w=0.15}.{w=0.15}."

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

r n ".{w=0.15}.{w=0.15}."

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

hide r

show y n:
    linear 0.4 xalign 0.5 yalign 1.0

e "You and Haruka sit for a moment, {w=0.15}and then she looks up at you."



y n "You know, I haven't seen Nema since yesterday."

y h "Not that I'm complaining,{w=0.15} just sort of strange."

y n "She's usually the first up."

menu:
    "She had a rough day yesterday.":
        pass

    "I'm sure she's around.":
        pass

y n "What, you mean our argument?"

y m "Shoot,{w=0.15} that was nothing. "

y m "If that's seriously what it is,{w=0.15} I'm a lil' annoyed, ya know?"

y n "Yeah we argued,{w=0.15} but we kind of live together, get over it."

menu:
    "You were pretty rude to her.":
        y n "Well."

        y h "Yeah, {w=0.15}I was a little bit."
        pass

    "Right.":
        pass

y n "I just can't see eye to eye with her."

y n "I'm fine not being friends with her,{w=0.15} but I don't want her to come in-between.{w=0.25}.{w=0.25}."

y n "I don't want her to make life harder than it has to be."

show r s:
    linear 0 xalign 0.9 yalign 1.0

r s "I think she's sad because of me."

show y su

y su "You?"

y n "What did you do?"

show r s

r s "I don't know,{w=0.15} neglect her or something?"

show y n

y n "Well whatever,{w=0.15} go apologize."

show r n

r n "I'm proving myself here,{w=0.15} she'll come around."

r h "Food's ready anyway."

e "Hei sets two plates on the table,{w=0.15} each with two eggs on them."

e "Sunny side up."

show y n

y n ".{w=0.15}.{w=0.15}."

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

y h "But later tonight,{w=0.15} you got some time to go over some reports with me?"

menu:
    "Sure.":
        y h "Perfect."
        pass

    "No.":
        y h "Hah, good one."
        pass

y n "I'll come to your room later."

y n "Tomorrow's the engine compound and I want to make sure everything's in order after all the weird stuff that's been happening."

menu:
    "No problem.":
        pass

    "Whatever.":
        pass

e "Haruka smiles at you and continues to eat."

call hall from _call_hall_4

hide y
hide r

e "You finish your eggs and head out of the kitchen.{w=0.15}.{w=0.15}."

play sound "sounds/DoorOpen2.ogg"

call blueRoom from _call_blueRoom_1

e "Into your room."

play sound "sounds/DoorClose2.ogg"

e "You sit down at your computer to get some work done."

window hide
show black 
with fade

play music "music/Idle.ogg" fadein 1.0

menu:#computer
    "I'll see if I have any mail.":
        label summariesD132:
        menu:
            "Junk mail.":
                call bMail10 from _call_bMail10
                jump summariesD132
                pass
            "I think I'm done.":
                jump day13End
                pass                
        pass

    "I'll go over some numbers for a while.":
        jump day13End
        pass

label day13End:

window hide
hide black 
with fade

stop music fadeout 3

play sound "sounds/Knock.ogg"

e "Some time passes,{w=0.15} and you hear a knock on your door."

menu:
    "Open the door":
        pass

play sound "sounds/DoorOpen2.ogg"

show y h

play music "music/CalmNight.ogg" fadein 1.0

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

y n "So.{w=0.15}.{w=0.15}."

e "Haruka walks right up in front of you."

y n "I just wanted to say that,{w=0.15} uhm."

e "Her hands are fidgeting."

y h "Well."

menu:
    "Yes?":
        pass

    "You alright?":
        pass

y n "You know,{w=0.15} I can't actually remember."

y s "Whatever."

e "Haruka starts to walk out your door,{w=0.15} then turns around."

y n "Oh,{w=0.15} and.{w=0.15}.{w=0.15}."

y s ".{w=0.15}.{w=0.15}."

y h "Nevermind!"

y h "I have work to do,{w=0.15} talk to ya later."

play sound "sounds/DoorClose2.ogg"

hide y

stop music fadeout 2

e "Haruka walks out into the hall."

show black

play music "music/Space.ogg" fadein 1.0

e "You lay on your bed for a while, {w=0.15}and then drift off to sleep."


return