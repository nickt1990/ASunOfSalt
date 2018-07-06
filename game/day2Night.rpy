label day2Night:
    
e "Haruka walks out of the room"

menu:
    "Get ready - I should go change my clothes and check to see if I've recieved any emails from Hcue.":
        pass

e "Change clothes at dresser."

e "Go to computer to check email."

e "Email from Hcue appears:"

e "Captain Sentaku, Tonight at 0100 we will activate the Satori sensors in each of your crewmates rooms. Following is all the information you will need to know."

e "The sensors are located under the beds of each crewmate. In order to get a read on them, they must sleep in their bed, over their sensor."
   
e "The more time they spend, the more accurate it will be. At 8 hours, peak information accuracy will be achieved."
   
e "These instructions are intentionally left vague as to leave you to naturally testing the device in new ways giving us a wider range of information."

e "The crew is not to know about the sensors. We want natural readings and complete compliance. Do not strictly enforce the crewmates to stay in their room."
   
e "Rather they miss a night here and there than learn of the sensors and intentionally try to interfere with the experiment."

e "The message ends."

menu:
    "That's terrible!":
        pass

    "That's great!":
        pass

#play sound "sounds/KnockOnDoor.mp3" TODO

e "Sound effect plays, knock on dor"

show y h

y h "Ya comin' cap?"

menu:
    "On my way!":
        pass

e "You open the door to Haruka standing there in her PJ's"

menu:
    "Pajamas?":
        pass

    "What are you wearing?":
        pass

y n "Figured I'd dress comfortable, since it will be a long night and all."

menu:
    "Looks good!":
        pass

    "Looks unprofessional.":
        pass

y h "I'm cute. "

y n "..."

y h "Hey, this isn't my assignment, I'm the morale support, remember?"

e "She smiles."

y n "Lets get to it. Do you know what to do?"

menu:
    "No.":
        pass

y n "Sure. We have a one week compound engine so it'll be once a week somebody will be sitting here."

menu:
    "One week compund?":
        pass

y h "Right. It's why I'm here, remember? It's my own lil' contraption that builds on EnDrives. I call it the EhDrive. The little 'h' is for me. "

e "Haruka winks."

y n "The basics are the same, microwaves are pushed by a magnetron against a sort of cone-shaped thruster piece to cause propulsion. "

y n "The change comes in the form of that cone. While it still funnels the energy out of the cone, it also absorbs and stores the energy that is exchanged when the microwaves collide with the cone, and each other."
     
y n "The same material is around the entire ship causing the force of our movement and really anything else that affects us to store energy. This causes us to actually gain more energy then we are using. "

y n "This extra energy is stored throughout the week, and is slowly integrated into the engine over the course of the 7th night each week. That makes us faster, which generates more engery faster."
     
y n "It compounds upon itself exponentially."

y n "The thing tho, is that we have only idea how the ship, the engine, or anythign else will react to the energy levels we'll reach. "

y s "I built fail-safes and designed everything around massive amounts of energy and speed, y'know... we'll see. "

y h "Eventually if things goes peachy, we'll be moving faster than any known object in history. We'll be exherting more energy than Earth's sun at any given moment. We'll be a force of nature. Endless potential cap, right under your little feet!"

menu:
    "That sounds risky...":
        pass

    "That sounds amazing!":
        pass

y s "Well... yeah. S'posed to be. Hear me out cap."

y n "We'll be so far away after week two that there's no going back anyways. We came into this knowing we'd die out here. So why stop?"

menu:
    "This is bigger than us.":
        pass

y h "Exactly!"

y n "There's no knowing! We could discover something so beyond what we understand now that we push humanity ahead a thousand years. A million years! We need to take risks!"

menu:
    "Some risks, but this might be too much.":
        pass

y n "I understand your concern, but we could be talking about secrets of the universe type shit here. Existence, reality."

y h "The goddamn meaning of life! C'mon!"

menu:
    "Can the ship handle that kind of force?":
        pass

y m "Oh you, somebody was not listening. The stuff it's made out of is special. This ship isn't made of some sort of metal. It's a machine made to absorb and reuse energy from top to bottom. It can hold. For. Sure. "

y n "Besides, we'll be so far away, chances are if anything does happen it wont get back to the rest of humanity for decades."

y n "Look, we can think and try to explain things away all our lives and be no better for it. But imagine actually having real answers in our hands. We have the question of reality before us, and the key's in our hands."

y h "Consider it."

y n "Ya don't need to decide now. Just have an answer soon."

menu:
    "Fine.":
        pass

    "Don't get your hopes up.":
        pass

e "Haruka smiles."

y h "Whatever you say cap."

y n "At least admit that you're impressed with me though. Bet ya didn't expect me to be so freakin' smart."

menu:
    "No, I didn't. How'd that happen?":
        pass

    "I knew you were an engineer.":
        pass

y n "I appreciate the honesty."

y h "I just woke up one day smart. A miracle!"

e "haruka smirks."

y m "I worked my ass off, how do you think?"

y n "It's funny. It was all for some man. Professor Motakomi."

y n "I grew up in a poor family. We were on the top deck of my station."

menu:
    "The top deck was bad?":
        pass

y h "Used to be, until they realized it sucks shit. You can fall out of buildings and you don't have the wider open spaces of the base. "

y s "Space is a luxury, and we did not have it."

y n "I shared a room with my seven brothers."

menu:
    "Seven in one room?":
        pass

    "All brothers?":
        pass

y n "Yeh, it sucked."

y m "Hated 'em all."

y h "But my oldest brother and I were close. Name was Jin. A true bro."

y n "We didn't have much money to do normal kid shit, so we'd go to the local library and read while my other brothers drank gasoline or whatever those idiots did."

y n "The library did this thing where they brought professors and scientists in to speak."

y n "Present their science garbage for all the 10 people who came to these things. Sort of a \"educate the poor children\" deal."

y n "At first I was blown away. The science talk made my lil' eyes bulge. Loved it."

y n "I started to have Jin take me to the library early mornings, late nights. I was like 13 and still needed help getting places, but he didn't mind."

y n "I'd read day and night. Pops didn't believe in school, but who needs school when you have the best teach in the skies?"

menu:
    "The best?":
        pass

    "You?":
        pass

y h "Me."

e "She smirked."

y n "So, gradually I started to understand enough that even I knew these speakers were full of shit. Only the shitbirds had the free time for children I guess."

y n "One time a dude was up there stammering around his own words. The man was incompetent, it made me furious, HE is educating the future of Station 6?  So I just walked up, told him that he was free to go, and started my own talk. He didn't even fight me on it."

y n "I must have been 16? I'm sure he was shocked. Maybe relieved that somebody set him free from his own bullshit."

menu:
    "You took his place?":
        pass

    "What was he talking about?":
        pass

y m "Yeah, screw that guy. These speeches were supposed to be educational. These guys were supposed to be examples for us kids."

y n "I looked around and saw the other kids just soaking in his complete bullshit, and it just pissed me off. He was poisoning kids who wanted to learn with his stupid existence."

y h "Anyways, from that point forward I would get there early and start giving my own lectures."

y n "When the guys who were supposed to be giving presentations showed up I'd just tell them that the schedule had changed and they were no longer needed."

y n "They were all losers. Nobody challenged me."

y s "Until one day. Shit. I will never forget."

y n "I was way into what I was saying already when man in a suit and tie- probably early 40's, walked up to me."

y n "He asked what I was doing. Said he was supposed to be giving a lecture today."

y h "I responded with the classic; \"screw off old man.\" They love that one."

y n "Without a moment of hesitation he slapped me across the face."

y n "\"Sit down.\""

y n "..."

y n "I did."

y n "I sat and listened. Professor Motakomi. It was the first time I'd ever heard of him, and he was amazing. "

y n "He made me feel small again. Like the little girl that I was supposed to be."

y h "The things he spoke, and the way he spoke about them... He was a genius. I was seeing stars cap, for real I was."

menu:
    "Did you get to speak to him?":
        pass

    "What did your brother do?":
        pass

y n "I did. It's crazy, the second he finished his lecture he walked right up to me and aske-"

#play sound "sounds/Alarm.mp3" todo

e "Alarm goes off."

y su "Shit."

y n "We haven't been watching the levels at all. "

e "Haruka adjusted some numbers on the computer screen."

menu:
    "Whats happening?":
        pass

    "Is it serious?":
        pass

y n "One of the converters was micalibrated. Tiny bit of energy was going to one side of the ship than the other."

y h "Coulda spent our entire lives flying in circles."

menu:
    "Miscalibrated by you?":
        pass

    "Great, no harm?":
        pass

y s "Apparently. I'm not perfect."

y h "There we go. S'all fine. The engine itself is doin' grand."

menu:
    "Good to hear.":
        pass

    "Safe enough?":
        pass

y h "Aw cap, ya chucklehead."

y h "Hey, nothings perfect. I'm not worried though, and that means you shouldn't be either."

y n "Still, let's focus on the engine. This first compound process is the big test."

menu:
    "Right. ":
        pass

play sound "sounds/DoorOpen2.mp3"

e "Nema walks in."

play sound "sounds/DoorClose2.mp3"

show p su:
    linear 0 xalign 0.9

p su "Captain, I heard the alarm. It everything alright?"

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

    "No thank you.":
        pass

p h "Oh, not at all Captain. I would be honored to help."

p n "Go ahead and get some rest."

menu:
    "Thanks.":
        pass

show y n

y n "I'll be heading to bed too."

show p s

p s "What?"

show y h

y h "Yeah I'm getting pretty tired. Good luck Nemo."

show p s

p s "Oh... OK, I'll do my best."

p s "Sleep well you two..."

call hall

play sound "sounds/DoorOpen2.mp3"

hide p

e "You walk into the hallway with Haruka close behind."

show y h

y h "Captain, was nice talkin to you tonight."

menu:
    "You mean talking at me?":
        pass

    "It was nice, wasn't it?":
        pass

y s "Maybe I said too much? "

y n "..."

y h "Nah. G'night Cap. "

hide y

menu:
    "Goodnight":
        pass
        
call blueRoom

return