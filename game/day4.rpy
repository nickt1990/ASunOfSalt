label day4:

e "Conflicted and confused. Unsure of the future."

e "Feeling love, hurt, sad. "

e "Nobody is happy. Want to help. Feel alone."

e "The day starts with the typical alarm. You read your messages."

call hall

e "Walk into the hallway. All the doors are locked and things seem quiet."

e "You make your way into the kitchen."

call kitchen

e "Haruka is sitting at the table eating."

show y h

y h "Ay Cap. Care to join me?"

menu:
    "Sure.":
        pass

    "No thanks.":
        pass

y h "Good to have ya."

y n "It seems like morale has reached an impressive low on the fourth day."

y s "I don't get why it's so hard for people to just accept the way things are."

y n "We're not meant to control the world, y'know? "

y n "Things are how they are, ya can't fight that."

y s "Especially when it comes to people."

y n "It's best to just come to terms with the state of things and do you."

menu:
    "Sounds like you feel guilty.":
        pass

    "I agree.":
        pass

y s "I don't feel bad about what I said Cap, but I can't help but feel sorry for the guy."

y n "I'm not a machine."

y s "I did what I thought would be best for us both though, I was honest."

y h "No regrets."

e "Haruka smiled."

menu:
    "Plans for the day?":
        pass

y h "Oh, thinking I might jump into Nemas room and hurt her feelings. I'm trying to get through the whole crew by the end of the week."

e "Haruka smirked."

y n "Nah, I'm going to just do a full system checkup today."

y n "Do it when things are working fine, and they'll stay that way."

y n "That should take the whole day I figure. If not then I'll-"

e "Nema enters"

show p su:
    linear 0 xalign 0.9 yalign 1.0

p su "Captain, something strange is showing up on the radar."

show y su

y su "Strange? Like how?"

show p n

p n "Please, both of you come take a look."

e "You walk into the nav room."

p n "Do you see the yellow mass on the radar, toward the right side of the screen?"

show y su

y su "A ship? Way out here? "

show p n

p n "I checked, we're nowhere near any checkpoint or station. "

p n "It is possible we just happened upon a random traveller."

show y s

y s "Well, hardly."

show p s

p s "Yes, it's true. Most encounters this far are less innocent..."

p n "It has the highest probability of being Haneshowas."

show y su

y su "A what?"

show p n

p n "Those who chose to break from civilization after the government unification happened. They move between their base and the edges of our zoned-space to pick off travellers. This is a bit far out, but perhaps we're catching them on their way back to wherever they've set up operations."

show y n

y n "You mean Lurks."

show p n

p n "Lurks?"

show y n

y n "It's slang for all that mess that just came out of your mouth."

show p n

p n "Oh. Yes, Lurks."

menu:
    "How long until we encounter them?":
        pass

p n "It looks like we have approximately three days."

show y n

y n "Good, so we have time."

y n "We can prepare ourselves and fight them head on. No doubt we have more firepower than them, this ship is state of the art."

show p s

p s "F-...fight them?"

p n "Captain, not to be disrespectful to Haruka, but I suggest we avoid them entirely. With our few days, we can take a long course around and avoid any sort of conflict. There's a mass of debris and large objects between us and the ship that will most likely block any sort of scanner that they have from detecting us until we've already passed them. It's the safest option."

show y m

y m "But if we're heading toward wherever their home base is, who's to say they wont report our path back to the rest of their group and ambush us somewhere down the road?"

show p s

p s "..."

show y m

y m "We need to pound them now, show them that we're a force to be reckoned with, and scare them off us."

show p s

p s "Well..."

menu:
    "Yes Nema?":
        pass

    "You agree with Haruka?":
        pass

show p n

p n "That could also put a target on us, and notify them that we have things worth stealing, despite the risk."

p n "I still suggest manuvering around the object. Even if our path is reported to the rest of their forces, we'll become aware of any oncoming ambush with our long range scanners, and be able to outrun any vessel they have."

menu:
    "Nema, are you sure we'd be able to detect and outrun them?":
        pass

    "Haruka, are you sure we'd be able to fight them directly?":
        pass

p n "I'm fairly confident Captain."
     
p n "With Haruka's one-of-a-kind engine and a complete suite of state of the art technology backing it up, we should be able to vastly outpace even the most advanced crafts that exist within high-level stations."
     
p n "Let alone a... \"Lurk\""

menu:
    "Two prior options.":
        pass

    "OK, I've made a decision.":
        pass

menu:
    "We will outrun them.":
        pass

    "We will fight.":
        pass

show y m

y m "Seriously? We can blow them away and find some cool stuff."

y s "Your loss cap."

e "Nema smiles."

show p n

p n "I'll begin plotting a course around the threat, thank you sir."

menu:
    "Of course.":
        pass

    "It is what it is.":
        pass

show y n

y n "And I should get movin' too, see ya at dinner."

menu:
    "Good luck to you both!":
        pass

    "Work hard!":
        pass

y h "Thanks Cap."

show p h

p h "Yes, Captain!"

p n "Oh wait, sir?"

menu:
    "Yes?":
        pass

p s "I'm sorry to bother you, but... if at all possible, could you find time to go and speak to Hei today?"

p n "I had a hard time speaking with him last night, but I believe you could boost his morale."

menu:
    "Okay.":
        pass

menu:
    "Leave and talk to HEI.":
        pass

hide p

hide y

call hall
        
e "You walk up to Hei's door."

call redRoom

play sound "sounds/DoorOpen2.mp3"

menu:
    "Hei?":
        pass

    "Bud?":
        pass

show r n

r n "How are you feeling today?"

menu:
    "Great, how about you?":
        pass

    "Hi.":
        pass

r h "Hey, pretty grand. Can't keep me down man."

r s "You know, at first I was really down, but I realized that Haruka was right."

menu:
    "Really?":
        pass

    "In what way?":
        pass

r n "Yeah, she wants a strong man, and I haven't shown that to her. Why would she be interested?"

menu:
    "So what will you do?":
        pass

    "Good point.":
        pass

r h "Man up and get me a babe."

r n "I'm gonna work hard."

r n "What else? I'm gonna become a man she can look to when she's in need."

r n "When all is lost, and she needs a miracle, I'll be the first thing she thinks of."

r h "That kind of man."

menu:
    "How?":
        pass

r n "Easy, I already told you, I'm gonna work hard."

menu:
    "At what?":
        pass

r n "Oh... Well, I'll figure it out."

r h "You worry too much man, I don't get why she likes you."

menu:
    "That's a bit mean.":
        pass

    "Excuse me?":
        pass

r h "No offence, I think you're great, but you don't really say, or... do... much. It sounds like I'm being a dick, but for real."

r n "How can she like you when you haven't given her anything to like?"

menu:
    "You're friends with Nema.":
        pass

    "How could she not?":
        pass

r n "Well yeah, she's great."

menu:
    "She doesn't say much.":
        pass

r n "Well, no. I guess not. But she kind of communicates in a different way."

menu:
    "...":
        pass

r n "Like, I just get her. You know? I don't need to say a lot, and neither does she. We're buds."

menu:
    "...?":
        pass

r n "Whatever man, it's OK. I didn't mean to put you down, just thinkin' out loud."

menu:
    "OK.":
        pass

r n "So, I guess I should get to working on a plan. How to be a man..."

menu:
    "Whatever happened to your plan for dinner last night?":
        pass

    "Alright, good luck!":
        pass

r n "Plan for dinner last night?"

r su "What?"

menu:
    "You planned something to impress Haruka?":
        pass

    "Nevermind.":
        pass

r su "I did?"

menu:
    "You told me yesterday in the morning.":
        pass

    "Nevermind.":
        pass

r n "Me? For Haruka?"

menu:
    "Yes, you said it would blow my mind?":
        pass

    "Nevermind.":
        pass

r s "Blow your mind..."

menu:
    "You don't remember?":
        pass

    "Nevermind.":
        pass

r h "It sounds like something I'd remember doesn't it?"

menu:
    "Yes. But you don't?":
        pass

    "Nevermind.":
        pass

r n "Nah."

menu:
    "Good luck.":
        pass

r h "Thanks!"

hide r

call hall

e "Everyone's working on a task. How will you spend your day?"

menu:
    "Video games.":
        pass

    "Report writing.":
        pass
        
call blueRoom

e "Time passes..." #todo

show p n

p n "Excuse me, sir?"

p n "Dinner is ready, at your convenience sir."

menu:
    "Thank you Nema.":
        pass

    "Cool.":
        pass

e "Nema smiles."

p n "I'll tell the rest."

p n "Haruka and Hei said they'd just be a little bit, but... well... everything's all set up if you want to eat, sir. I'm going to wait, but there's no reason you should have to."

menu:
    "Sure!":
        pass

    "I'll wait.":
        pass

e "Nema sits down across the table from you."

menu:
    "This is good!":
        pass

    "Say nothing.":
        pass

p h "Thank you Captain."

e "Nema smiles shortly."

e "Time flashes forward and your food is gone."

p s "The others should be here soon..."

menu:
    "What exactly did they say?":
        pass

p n "Haruka just glanced at me when I told her food was ready. "

p s "That's not an uncommon response from her though..."

menu:
    "What about Hei?":
        pass

p n "He was playing a game and just said \"I know, I know.\""

p s "I took that as his way of saying he would come as soon as possible, but I suppose I assumed a bit much."

p n "..."

p n "Not a problem, I'll pack their meals away in the fridge."

menu:
    "Need help?":
        pass

    "OK.":
        pass

e "Nema ignores you for a second and moves to put the food away."

p s "C-captain... May I ask you a question?"

menu:
    "Yes.":
        pass

p n "W-"

e "Nema struggles to find words."

p n "No, nevermind. I figured it out."

p n "Thank you though. "

e "Nema smiled."

menu:
    "No, what was it?":
        pass

    "No problem.":
        pass

p n "I was going to ask what you..."

p s "What... Uhm......."

p n "What do you think about the ship we spotted on the radar?"

e "Nema blushed."

menu:
    "Worried.":
        pass

    "Not worried.":
        pass

p h "That's oddly a relief to me... Thank you."

p s "To be quite honest, I'm worried as well."

p n "These \"Lurks\" that we saw earlier, I've noticed something weird."

p n "The shape has changed. From a triangular mass to a large circle. It seems to be slowly spreading out."

menu:
    "What does that mean?":
        pass

    "Uh oh.":
        pass

p n "It most likely is just interference, but it makes me uneasy. If something is able to effect our view that much, does that mean our information is unreliable?"

menu:
    "Should extra steps be taken?":
        pass

p s "No, no. As I said, I think it's just a sort of interference. It just gave me momentary pause, I apologize Captain."

p n "I still firmly believe all that I said earlier this morning about the situation."

p n "I can't agree with hostility as our first action in meeting with this unknown ship."

e "Suddenly everything goes dark."

menu:
    "What happened?":
        pass

    "Quck, to the nav room!":
        pass

p su "I-I'm not sure! We-w-uhm..."

p n "What should we do?"

menu:
    "Head to nav room. ":
        pass

    "Hide.":
        pass

call navRoom

p n "Yes sir!"

menu:
    "What is it?":
        pass

p n "It looks like... a large asteroid just happened to pass beween us and the sun. "

p n "Everything else is full power, the autopilot AI is functioning normally, we should be in no danger."

menu:
    "How did we not notice this asteroid before?":
        pass

    "Good to hear!":
        pass

p n "I'm sorry sir, I actually did notice the asteroid before, but I failed to notice that it would have this effect on us. I apologize."

menu:
    "That's OK.":
        pass

    "Please keep an eye out for things like this.":
        pass

p n "It wont happen again sir."

play sound "sounds/DoorOpen2.mp3"

e "The door opens and Haruka walks in."

show y n:
    linear 0 xalign 0.9 yalign 1.0

y n "What's happenin'?"

show p n

p n "It seems to just be just a large asteroid blocking out the sunlight."

show y n

y n "Oh damn, well good. I thought we were about to launch into something serious."

y n "How long's this gonna go on for?"

show p n

p n "My closest estimation is thirteen hours."

show y n

y n "Thirteen hours? Wow..."

show p n

p n "Yes, the asteroid is travelling almost perfectly parallel to us."

show y h

y h "It's almost like we'll get to have our own personal night."

menu:
    "True.":
        pass

    "Troubling.":
        pass

y n "It's exciting. "

y h "A lil' taste of what things were like back on the blue rock, eh?"

e "Haruka smiles."

y n "Perfect timing too, I was thinking of grabbin' some food and hittin' the bed."

y n "Nems, there any food left?"

show p n

p n "Oh, yes. I saved a portion for you in the fridge."

show y h

y h "Thanks, it smells so good, I've been rushin' through my last bit of work so I could come get some."

show p su

p su "R-really?"

show y n

y n "Course. I'm stravin'."

show p h

p h "Oh, thank you Haruka!"

show y m

y m "Sure?"

y h "Well, I'm gonna go grab that, thanks."

hide y

show p h

p h "Well, of course!"

p h "I'm going to get to my room as well Captain, be sure to enjoy this personal night the best you can!"

menu:
    "OK.":
        pass

    "I'll do my best!":
        pass

p h "Good night!"

e "Nema smiles as she walks back to her room."

hide p

e "You decide to head to yours as well."

call blueRoom

return