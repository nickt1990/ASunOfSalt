﻿label day2Night:
    
e "Haruka walks out of the room"

call hall

e "You follow shortly behind."

call blueRoom

e "Then, head back to your room to change clothes and get prepared for the night."

e "Go to computer to check email."

window hide
show black
with fade

e "Email from HQ appears:"

e "Captain, {w=0.15}Tonight at 0100 we will activate the Satori sensors in each of your crewmates rooms. Following is all the information you will need to know."

e "The sensors are located under the beds of each crewmate. In order to get a read on them, {w=0.15}they must sleep in their bed, {w=0.15}over their sensor."
   
e "The more time they spend, {w=0.15}the more accurate it will be. At 8 hours, {w=0.15}peak information accuracy will be achieved."
   
e "These instructions are intentionally left vague as to leave you to naturally testing the device in new ways giving us a wider range of information."

e "The crew is not to know about the sensors. We want natural readings and complete compliance. Do not strictly enforce the crewmates to stay in their room."
   
e "Rather they miss a night here and there than learn of the sensors and intentionally try to interfere with the experiment."

e "The message ends."

window hide
hide black
with fade

menu:
    "That's terrible!":#todo: what happens here?
        pass

    "That's great!":
        pass

play sound "sounds/Knock.mp3"

show y h

y h "Ya comin' Cap?"

menu:
    "On my way!":
        pass

e "You open the door to Haruka standing there in her PJ's"
#todo this page should all be pj haruka
menu:
    "Pajamas?":
        pass

    "What are you wearing?":
        pass

y n "Figured I'd dress comfortable, {w=0.15}since it will be a long night and all."

menu:
    "Looks good!":#todo: does this conversation happen way later as well?
        y h "I'm cute. "
        pass

    "Looks unprofessional.":#todo: need text for this branch
        pass


y n "..."

y h "Hey, {w=0.15}this isn't my assignment, {w=0.15}I'm the morale support, {w=0.15}remember?"

e "She smiles."

y n "Lets get to it. Do you know what to do?"

menu:
    "No.":
        pass

y n "Sure. We have a one week compound engine so it'll be once a week somebody will be sitting here."

menu:
    "One week compound?":
        pass

y h "Right. It's why I'm here, {w=0.15}remember? It's my own lil' contraption that builds on EnDrives. I call it the EhDrive. The little 'h' is for me. "

e "Haruka winks."

y n "The basics are the same, {w=0.15}microwaves are pushed by a magnetron against a sort of cone-shaped thruster piece to cause propulsion. "

y n "The change comes in the form of that cone. While it still funnels the energy out of the cone, {w=0.15}it also absorbs and stores the energy that is exchanged when the microwaves collide with the cone, {w=0.15}and each other."
     
y n "The same material is around the entire ship causing the force of our movement and really anything else that affects us to store energy. This causes us to actually gain more energy then we are using. "

y n "This extra energy is stored throughout the week, {w=0.15}and is slowly integrated into the engine over the course of the 7th night each week. That makes us faster, {w=0.15}which generates more energy faster."
     
y n "It compounds upon itself exponentially."

y n "The thing tho, {w=0.15}is that we have only idea how the ship, {w=0.15}the engine, {w=0.15}or anything else will react to the energy levels we'll reach. "

y s "I built fail-safes and designed everything around massive amounts of energy and speed, {w=0.15}y'know... we'll see. "

y h "Eventually if things go peachy, {w=0.15}we'll be moving faster than any known object in history. We'll be exerting more energy than Earth's sun at any given moment. We'll be a force of nature. Endless potential Cap, {w=0.15}right under your little feet!"

menu:
    "That sounds risky...":
        y s "Well.{w=0.15}.{w=0.15}. yeah. S'posed to be.{w=0.15} Hear me out Cap."
        pass

    "That sounds amazing!":
        y h "I was hoping you'd think so!"
        pass

y n "We'll be so far away after week two that there's no going back anyways.{w=0.25} We came into this knowing we'd die out here. So why stop?"

menu:
    "This is much bigger than us.":
        pass

y h "Exactly!"

y n "There's no knowing!{w=0.15} We could discover something so beyond what we understand now that we push humanity ahead a thousand years. A million years! We need to take risks!"

menu:
    "Some risks, {w=0.15}but this might be too much.":
        pass

y n "I understand your concern, {w=0.15}but we could be talking about secrets of the universe type shit here. Existence, {w=0.15}reality."

y h "The damn meaning of life!{w=0.15} C'mon!"

menu:
    "Can the ship handle that kind of force?":
        pass

y m "Oh you, {w=0.15}somebody was not listening.{w=0.25} The stuff it's made out of is special. This ship isn't made of some sort of metal. It's a machine made to absorb and reuse energy from top to bottom. It can hold. For. Sure. "

y n "Besides, {w=0.15}we'll be so far away, {w=0.15}chances are if anything does happen it wont get back to the rest of humanity for decades."

y n "Look, {w=0.15}we can think and try to explain things away all our lives and be no better for it.{w=0.25} But imagine actually having real answers in our hands. We have the question of reality before us, {w=0.15}and the key's in our hands."

y h "Consider it."

y n "Ya don't need to decide now. Just have an answer soon."

menu:
    "Fine.":
        pass

    "Don't get your hopes up.":
        e "Haruka smiles."

        y h "Whatever you say Cap."
        pass

y n "At least admit that you're impressed with me though.{w=0.25} Bet ya didn't expect me to be so freakin' smart."

menu:
    "No, {w=0.15}I didn't. How'd that happen?":
        y n "I appreciate the honesty."
        y h "I just woke up one day smart. A miracle!"
        e "Haruka smirks."
        y m "I worked my ass off, {w=0.15}how do you think?"
        pass

    "I knew you were an engineer.":
        y h "Far enough,{w=0.15} but it didn't happen on its own."
        y m "I worked my ass off"
        pass

y n "It's funny.{w=0.25} It was all for some man. Professor Motakomi."

y n "I grew up in a poor family.{w=0.25} We were on the top deck of my station."

menu:
    "The top deck was bad?":
        pass

y h "Yeah. {w=0.15}Used to be that the higher you were the classier, {w=0.15}until they realized it sucks up there. You can fall out of buildings and you don't have the wider open spaces of the base. "

y s "Space is a luxury, {w=0.15}and we did not have it."

y n "I shared a room with my seven brothers."

menu:
    "Seven in one room?":
        y n "Yeh, {w=0.15}it sucked."
        y m "Seven dudes and little ol' me? {w=0.15}Childhood was hard."
        pass

    "All brothers?":
        y n "Yeh, {w=0.15}it sucked."

        y m "Hated 'em all."
        pass

y h "But my oldest brother and I were close. Name was Jin. A true bro."

y n "We didn't have much money to do normal kid shit, {w=0.15}so we'd go to the local library and read while my other brothers drank gasoline or whatever those idiots did."

y n "The library did this thing where they brought professors and scientists in to speak."

y n "Present their science garbage for all the 10 people who came to these things. {w=0.15}Sort of an \"educate the poor children\" deal."

y n "At first I was blown away.{w=0.15} The science talk made my lil' eyes bulge.{w=0.15} Loved it."

y n "I started to have Jin take me to the library early mornings, {w=0.15}late nights. I was like 13 and still needed help getting places, {w=0.15}but he didn't mind."

y n "I'd read day and night. Pops didn't believe in school, {w=0.15}but who needs school when you have the best teach in the skies?"

menu:
    "The best?":
        pass

    "You?":
        pass

y h "Me."

e "She smirked."

y n "So, {w=0.15}gradually I started to understand enough that even I knew these speakers were full of shit. Only the shitbirds had the free time for children I guess."

y n "One time a dude was up there stammering around his own words. The man was incompetent, {w=0.15}it made me furious, {w=0.15}HE is educating the future of Station 6?  So I just walked up, {w=0.15}told him that he was free to go, {w=0.15}and started my own talk. He didn't even fight me on it."

y n "I must have been 16? I'm sure he was shocked. Maybe relieved that somebody set him free from his own bullshit."

menu:
    "You took his place?":
        y h "Yeah."
        pass

    "What was he talking about?":
        y m "Who cares?"
        pass

y m "Screw that guy.{w=0.25}These speeches were supposed to be educational. {w=0.15}These guys were supposed to be examples for us kids."

y n "I looked around and saw the other kids just soaking in his complete bullshit, {w=0.15}and it just pissed me off. He was poisoning kids who wanted to learn with his stupid existence."

y h "Anyways, {w=0.15}from that point forward I would get there early and start giving my own lectures."

y n "When the guys who were supposed to be giving presentations showed up I'd just tell them that the schedule had changed and they were no longer needed."

y n "They were all losers. Nobody challenged me."

y s "Until one day. Shit. I will never forget."

y n "I was way into what I was saying already when man in a suit and tie- probably early 40's, {w=0.15}walked up to me."

y n "He asked what I was doing. Said he was supposed to be giving a lecture today."

y h "I responded with the classic; \"screw off old man.\" They love that one."

y n "Without a moment of hesitation he slapped me across the face."

y n "\"Sit down.\""

y n ".{w=0.15}.{w=0.15}."

y n "I did."

y n "I sat and listened. Professor Motakomi. It was the first time I'd ever heard of him, {w=0.15}and he was amazing. "

y n "He made me feel small again. Like the little girl that I was supposed to be."

y h "The things he spoke, {w=0.15}and the way he spoke about them... He was a genius. I was seeing stars Cap, {w=0.15}for real I was."

menu:
    "Did you get to speak to him?":
        pass

    "What did your brother do?":
        #todo branch
        pass

y n "I did.{w=0.15} He taught me everything I know."
     
y h "It's crazy, {w=0.15}the second he finished his lecture he walked right up to me and aske-"

play music "music/Alarm.mp3" fadein 2.0

e "Alarm goes off."

y su "Shit."

y n "We haven't been watching the levels at all. "

e "Haruka adjusted some numbers on the computer screen."

menu:
    "Whats happening?":
        pass

    "Is it serious?":
        pass

y n "One of the converters was miscalibrated. A tiny bit more energy was going to one side of the ship than the other."

y h "Coulda spent our entire lives flying in circles."

menu:
    "Mis-calibrated by you?":
        y s "Apparently.{w=0.15} I'm not perfect."
        pass

    "Great, {w=0.15}no harm?":
        y h "Doesn't look like it!"
        pass



y h "S'all fine now.{w=0.15} The engine itself is doin' grand."

menu:
    "Good to hear.":
        y h "Yep!"
        pass

    "Safe enough?":
        y h "Hey, {w=0.15}nothings perfect.{w=0.15} I'm not worried though, {w=0.15}and that means you shouldn't be either."
        pass

y n "Still, {w=0.15}let's focus on the engine. This first compound process is the big test."

menu:
    "Right. ":
        pass

play sound "sounds/DoorOpen2.mp3"

e "Nema walks in."

play sound "sounds/DoorClose2.mp3"

show p su:
    linear 0 xalign 0.9

p su "Captain, {w=0.15}I heard the alarm. It everything alright?"

menu:
    "Yeah.":
        pass

    "False alarm.":
        pass

p n "I see."

p s "W-would you like to take a break Captain? I wouldn't mind taking over your shift for a while."

menu:
    "I'll take a break.":
        pass

    "No thank you.":#todo branch
        pass

p h "Oh, {w=0.15}not at all Captain. I would be honored to help."

p n "Go ahead and get some rest."

menu:
    "Thanks.":
        pass

show y n

y n "I'll be heading to bed too."

show p s

p s "What?"

show y h

y h "Yeah I'm getting pretty tired.{w=0.15} Good luck Nemo."

show p s

p s "Oh.{w=0.15}.{w=0.15}. OK, {w=0.15}I'll do my best."

p s "Sleep well you two.{w=0.15}.{w=0.15}."

call hall from _call_hall_9

play sound "sounds/DoorOpen2.mp3"

hide p

e "You walk into the hallway with Haruka close behind."

show y h

y h "Captain, {w=0.15}was nice talkin' to you tonight."

menu:
    "You mean talking at me?":
        pass

    "It was nice, {w=0.15}wasn't it?":#todo branch
        pass

y s "Maybe I said too much? "

y n ".{w=0.15}.{w=0.15}."

y h "Nah. G'night Cap. "

hide y

menu:
    "Goodnight":
        pass
        
call blueRoom from _call_blueRoom_4

return