﻿label day6:

menu:
    "Open your eyes.":
        pass

hide black

e "Nema is sitting in a chair beside you sleeping."

menu:
    "Nema?":
        pass

    "Hey.":
        pass

e "Nema snores loudly."

menu:
    "Nema.":
        pass

show p s

p s "Huh..."

p n "Captain?"

p su "Sir! Can you see?!"

menu:
    "Yes.":
        pass

    "No. I'm blind!":
        pass

p h "Oh, {w=0.15}I'm so happy! Thank goodness. "

p n "How do you feel?"

menu:
    "Great.":
        pass

    "Fine.":
        pass

p h "Excellent! "

p s "So then, {w=0.15}there is something I need to bring up to you, {w=0.15}sir."

menu:
    "Wow, {w=0.15}right to it.":
        pass

    "Go on.":
        pass

p s "I apologize for pushing this on you so s-soon after you getting back to health but..."

p n "Ever since the moment you started to rest yesterday, {w=0.15}Haruka and Hei have been arguing."

p s "I d-don't know what to do, {w=0.15}it starts up the second they see each other."

menu:
    "What are they arguing about?":
        pass

    "I'll talk to them.":
        pass

p n "Hei wants to make modifications to the ship."

p n "Haruka thinks he shouldn't, {w=0.15}she built the ship and he's not familiar with it enough to make worthwhile modifications."

p s "I... I can't understand a lot of what they say honestly, {w=0.15}it seems to be a very technical argument, {w=0.15}but that's the basic idea of it sir."

menu:
    "Ok.":
        pass

    "Thank you.":
        pass

play sound "sounds/DoorOpen2.mp3"

hide p

e "Leave the room. Haruka is on her heater."

show y h

y h "Cap! "

y n "Ya join the land of the living once again."

y h "I was worried, {w=0.15}I don't know what I would have done without ya Champ."

e "Haruka smiles."

menu:
    "Good to see you!":
        pass

    "What's this about you arguing with Hei?":
        pass

y h "Awww Cap. You mushball."

y n "But hey, {w=0.15}I've got a bit of an issue with... the other one."

menu:
    "Hei?":
        pass

    "Nema?":
        pass

y m "Yes."

y n "Hei."

y m "He's trying to dick up everything I've built with this ship."

y n "I'm OK with modifications, {w=0.15}sure."

y m "But he's trying to make huge changes, {w=0.15}and he has no actual idea what he's doing."

show r m:
    linear 0 xalign 0.9 yalign 1.0

r m "Not true!"

show y m

y m "Oh great, {w=0.15}here we go."

e "Nema walks out of your room."

show p s:
    linear 0 xalign 0.1 yalign 1.0

p s "Please, {w=0.15}don't argue again."

p s "The captain just got up, {w=0.15}he nee-"

show r m

r m "She's just being... a little hard to work with."

r su "Man, {w=0.15}I can improve the ship, {w=0.15}I know I can!"

r n "I realized how crap the weapons were when we got stuck in the blood junk the other day."

show y m

y m "Crap? You built them. It was your job from the beginning, {w=0.15}and now we're supposed to trust you to make changes on the go like this?"

show r n

r n "Well... Yeah? I built them, {w=0.15}so I know how to improve on them. "

r s "Do you want to fly out into the unknown with underpowered weapons?"

show y n

y n "Ya realize that because of the... unique qualities of our engine, {w=0.15}we can't slow down, {w=0.15}let alone stop this ship, {w=0.15}right?"

show r su

r su "What? I mean, {w=0.15}didn't we stop when that blood stuff surrounded us?"

show y n

y n "Nope, {w=0.15}I checked. It was sticking to us somehow."

show r n

r n "Well whatever, {w=0.15}that's what the suits are for."

r n "I can still get out there to make changes."

show y n

y n "You could, {w=0.15}but you wont."

y n "We'd have to put all weapons offline for how long?"

show r n

r n "Only two, {w=0.15}three days tops."

show y h

y h "Hah."

y n "And you wanna take energy from the engine? Right. Ok."

show r s

r s "Only the tiniest smallest amount."

show y m

y m "Any amount could screw up everything. How do you not get this?"

y n "It's just not worth the risk. "

y n "We can't mess with this. This engine is the reason we're even taking this trip. I'm not letting you screw it up."

show r m

r m "It's gonna get pretty screwed up if we get blown up by space blood or whatever."

r n "Surprise, {w=0.15}I didn't plan for that sort of thing, {w=0.15}and if it comes back we might be out of options."

show y h

y h "What are the chances that thing catches up? We'll be moving so fast."

show r n

r n "But we're already moving stupid fast and that thing stuck to us like nothing."

show p s

p s "H-he's right... You'd think that nothing would be ab-"

show y m

y m "Like you're one to talk, {w=0.15}you said we had time to go around that thing, {w=0.15}and your logic is the reason we didn't make a clean escape."

y m "Like hell I'm going to listen to your opinion on this."

menu:
    "Haruka you're being unfair.":
        pass

    "I'm sorry, {w=0.15}but I agree with Haruka.":
        pass

y n "Unfair? Cap, {w=0.15}sorry if I'm a bit riled up, {w=0.15}but I wanna survive and I don't trust Hei to come through in a pinch for shit."

y n "Our weapon can be our speed. "

y n "We just need to keep up with our weekly speed compounds and we'll be fine."

y n "Nothing will be able to touch us."

show r m

r m "I woulda thought that two days ago, {w=0.15}but it's not true man."

r s "We need more, {w=0.15}it's worth the risk of waiting, {w=0.15}please."

menu:
    "Sorry Hei, {w=0.15}but I think it's in our best interest to just build speed.":
        pass

    "Haruka, {w=0.15}I think we need a little extra insurance. You said yourself, {w=0.15}we're heading into the unknown.":
        pass

show y h

y h "Oh Cap, {w=0.15}you beatiful man."

y n "This is the right choice, {w=0.15}I promise."

show r m

r m "Fine, {w=0.15}if you say so sir."

show p s

p s "..."

show y n

y n "Well then, {w=0.15}I'm gonna go finish my work."

y n "I'll see you guys later."

play sound "sounds/DoorClose2.mp3"

e "Haruka walks into her room."

hide y

r m "I got stuff to do too."

e "Hei shuffles off to his room."

hide r

play sound "sounds/DoorClose2.mp3"

show p s

p s "..."

p s "I guess I'll get to work as well, {w=0.15}sir..."

e "Nema looks at you sadly, {w=0.15}then slowly walks off to her room."

hide p

e "Everyone's gone to their rooms."

e "Where would you like to go?"


define hei6 = True
define haru6 = True
define nema6 = True
    
label day6Menu:
    
menu:
    "Hei's Room" if hei6 == True:
        call redRoom from _call_redRoom_3
        $ hei6 = False
        jump day6Hei
        pass

    "Haruka's Room" if haru6 == True:
        call yellowRoom from _call_yellowRoom_2
        $ haru6 = False
        jump day6Haruka
        pass
        
    "Nema's Room" if nema6 == True:
        call pinkRoom from _call_pinkRoom_1
        $ nema6 = False
        jump day6Nema
        pass        
        
    "Go back to your room" if nema6 == False and haru6 == False:
        call blueRoom from _call_blueRoom_10
        jump preDinnerDay6             

label day6Hei:

e "Hei's door is locked."

e "You can't hear any sound coming from the room."

jump day6Menu#day6Hei

label day6Haruka:

e "Haruka talks briefly, {w=0.15}but is busy on her computer."

jump day6Menu#day6Haruak

label day6Nema:

p n "Hello Captain."

menu:
    "Hello.":
        pass

p n "..."

menu:
    "What is it?":
        pass

    "Are you upset?":
        pass

p n "I was just thinking about earlier."

p s "I don't necessarily agree with your decision..."

p n "But I'm not jealous of the fact that you are the one who had to make it."

p s "I know where I stood on the issue, {w=0.15}but I can't imagine making a choice there on the spot like that."

p n "How do you do it?"

menu:
    "You just follow your gut.":
        pass

    "Logic. You think it through.":
        pass

p s "Follow your gut..."

p n "I don't even know what that means sir."

p n "What do you do when your decision gets people killed?"

p s "Or when you make the wrong choice?"

menu:
    "Do your best to make things right.":
        pass

    "Just deal with it.":
        pass

p n "I believe I'd want to do my best to make things right, {w=0.15}but the fact would remain that I decided to take responsibility when I obviously wasn't ready. "

p n "It's hard to imagine that wouldn't end in a snowball effect."

p n "Failing, {w=0.15}acting responsibly and putting yourself in charge of the work to make things right, {w=0.15}failing, {w=0.15}putting yourself in charge of more again."

p n "Doesn't it make sense to just let natural leaders lead?"

menu:
    "Don't you want to improve?":
        pass

    "Yes, {w=0.15}I guess it does.":
        pass

p n "I can improve in other ways to compliment the leaders. Not everybody has to be a leader."

p s "Maybe..."

p n "I'm content just being support. I want to see us succeed."

menu:
    "Don't limit yourself. You can succeed on your own too.":
        pass

    "There needs to be a great crew behind every leader, {w=0.15}that's true.":
        pass

p h "No, {w=0.15}it's not limiting, {w=0.15}it's focusing."

p n "It makes sense..."

p h "I'm appreciative you took the time to talk over these petty personal problems with me sir."

p h "Thank you."

e "Nema turns to her work."

jump day6Menu #day6nema

label preDinnerDay6:

menu:
    "Check email":
        pass

e "After checking email you hear a knock on the door."

e "From the hallway you hear Hei's voice."

show r n

r n "Hey, {w=0.15}wanna grab some food?"

hide r n

menu:
    "Sure.":
        call hall from _call_hall_23
        pass

play sound "sounds/DoorOpen2.mp3"

e "You open your door and step into the hallway."

play sound "sounds/DoorClose2.mp3"

e "Hei is nowhere in sight, {w=0.15}but the kitchen door is open."

call kitchen from _call_kitchen_6

e "You enter the kitchen and see him sitting at the table."

show r m

r m "Man, {w=0.15}I'm going crazy."

r n "I wont hold your decision this morning against you, {w=0.15}do what you think is best."

r n "But damn, {w=0.15}why is Haruka such a dick sometimes?"

r n "She wants people to step up, {w=0.15}but when they do she just shuts them down."

r s "I don't know what to do man."

r s "There are no tricks up my sleeve."

r m "I'm just a man for god's sake."

menu:
    "Keep trying?":
        pass

    "Maybe it's not meant to be.":
        pass

r n "Keep trying?"

r s "But like... Why bother?"

r s "So Haruka can make my life miserable?"

r m "She's so hot, {w=0.15}I can't not be attracted to her."

r s "But..."

r s "I don't know."

r s "This sucks."

r s "I'm gonna finish in my room. "

r s "I'll see you tomorrow dude."

hide r

e "You sit in silence and eat your food."

e "After you finish, {w=0.15}you make your way back to your room."

play sound "sounds/DoorClose2.mp3"

call hall from _call_hall_24

e "The ship is silent."

play sound "sounds/DoorOpen2.mp3"

call blueRoom from _call_blueRoom_11

e "You lay down on your bed and slowly fall asleep."

e "The screen fades to black."

#TODO DAY 6 NIGHT SCENE

return