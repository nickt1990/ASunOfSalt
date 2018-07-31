label day4:

play music "music/MorningAlarm.mp3" fadein 2.0

window hide
hide black
with fade

e "The day starts with the typical alarm."

e "You sit down at your computer."

window hide
show black 
with fade

label summariesD4:

menu:#computer
    "I'll read the summaries.":
        menu:
            "Haruka's summary.":
                call day4HaruS
                jump summariesD4
                pass
            "Hei's summary.":
                call day4HeiS
                jump summariesD4
                pass
            "Nema's summary.":
                call day4NemaS
                jump summariesD4
                pass
            "I think I'm done.":
                jump day4Start
                pass                
        pass

    "I'm going to respect their privacy.":
        jump day3Start
        pass

label day4Start:

window hide
hide black 
with fade

stop music fadeout 2.0

play music "music/Space.mp3" fadein 2.0

call hall from _call_hall_25

play sound "sounds/DoorOpen2.mp3"

e "Walk into the hallway. All the doors are locked and things seem quiet."

e "You make your way into the kitchen."

play sound "sounds/DoorOpen2.mp3"

call kitchen from _call_kitchen_7

e "Haruka is sitting at the table eating."

show y h

y h "Ay Cap.{w=0.25} Care to join me?"

menu:
    "Sure.":
        y h "Good to have ya."
        pass

    "No thanks.":
        y s "Aw c'mon, talk with me for a minute."
        y s "I need ya."
        pass

y n "It seems like morale has reached an impressive low on the fourth day."

y s "I don't get why it's so hard for people to just accept the way things are."

y n "We're not meant to control the world, {w=0.15}y'know? "

y n "Things are how they are, {w=0.15}ya can't fight that."

y s "Especially when it comes to people."

y n "It's best to just come to terms with the state of things and do you."

menu:
    "Sounds like you feel guilty.":
        pass

    "I agree.":
        y h "I knew you'd get it."
        y n "It's like{w=0.15}.{w=0.15}.{w=0.15}."
        y n "I don't feel bad about what I said, {w=0.15}I just can't help but feel sorry for the guy."
        pass

y n "I'm not a machine."

y s "I did what I thought would be best for us both though, {w=0.15}I was honest."

y h "No regrets."

e "Haruka smiled."

menu:
    "Plans for the day?":
        pass

y h "Oh, {w=0.15}thinking I might jump into Nemas room and hurt her feelings. I'm trying to get through the whole crew by the end of the week."

e "Haruka smirks."

y n "Nah, {w=0.15}I'm going to just do a full system checkup today."

y n "Do it when things are working fine, {w=0.15}and they'll stay that way."

y n "That should take the whole day I figure. If not then I'll-"

e "Nema enters"

show p su:
    linear 0 xalign 0.9 yalign 1.0

p su "Captain, {w=0.15}something strange is showing up on the radar."

show y su

y su "Strange? Like how?"

show p n

p n "Please, {w=0.15}both of you come take a look."

call navRoom
play sound "sounds/DoorOpen2.mp3"

e "You walk into the nav room."

p n "Do you see the yellow mass on the radar, {w=0.15}toward the right side of the screen?"

show y su

y su "A ship? Way out here? "

show p n

p n "I checked, {w=0.15}we're nowhere near any checkpoint or station. "

p n "It is possible we just happened upon a random traveller."

show y s

y s "Well, {w=0.15}hardly."

show p s

p s "Yes, {w=0.15}it's true. Most encounters this far are less innocent.{w=0.15}.{w=0.15}."

p n "It has the highest probability of being Haneshowas."

show y su

y su "A what?"

show p n

p n "Those who chose to break from civilization after the government unification happened.{w=0.15} They move between their base and the edges of our zoned-space to pick off travelers."

p n "This is a bit far out, {w=0.15}but perhaps we're catching them on their way back to wherever they've set up operations."

show y n

y n "You mean Lurks."

show p n

p n "Lurks?"

show y n

y n "It's slang for all that mess that just came out of your mouth."

show p n

p n "Oh. Yes, {w=0.15}Lurks."

menu:
    "How long until we encounter them?":
        pass

p n "It looks like we have approximately three days."

show y n

y n "Good, {w=0.15}so we have time."

y n "We can prepare ourselves and fight them head on. No doubt we have more firepower than them, {w=0.15}this ship is state of the art."

show p s

p s "F-.{w=0.15}.{w=0.15}.fight them?"

p n "Captain, {w=0.15}not to be disrespectful to Haruka, {w=0.15}but I suggest we avoid them entirely."

p n "With our few days, {w=0.15}we can take a long course around and avoid any sort of conflict."

p n "There's a mass of debris and large objects between us and the ship that will most likely block any sort of scanner that they have from detecting us until we've already passed them."

p n "It's the safest option."

show y m

y m "But if we're heading toward wherever their home base is, {w=0.15}who's to say they wont report our path back to the rest of their group and ambush us somewhere down the road?"

show p s

p s ".{w=0.15}.{w=0.15}."

show y m

y m "We need to pound them now, {w=0.15}show them that we're a force to be reckoned with, {w=0.15}and scare them off us."

show p s

p s "Well.{w=0.15}.{w=0.15}."

menu:
    "Yes Nema?":
        pass

    "You agree with Haruka?":
        p s "I.{w=0.15}.{w=0.15}.{w=0.15} I'm not sure about that,{w=0.15} sir."
        pass

show p n

p n "That could also put a target on us, {w=0.15}and notify them that we have things worth stealing, {w=0.15}despite the risk."

p n "I still suggest maneuvering around the object.{w=0.25} Even if our path is reported to the rest of their forces, {w=0.15}we'll become aware of any oncoming ambush with our long range scanners, {w=0.15}and be able to outrun any vessel they have."

label menuSmall4:
menu:
    "Nema, {w=0.15}are you sure we'd be able to detect and outrun them?":
        p n "I{w=0.15}.{w=0.15}.{w=0.15}.{w=0.15} I'm fairly confident Captain."
        p n "With Haruka's one-of-a-kind engine and a complete suite of state of the art technology backing it up, {w=0.15}we should be able to vastly outpace even the most advanced crafts that exist within high-level stations."
        p n "Let alone a.{w=0.15}.{w=0.15}. \"Lurk\""
        p s "Fighting just seems like an unnecessary risk."
        pass

    "Haruka, {w=0.15}are you sure we'd be able to fight them directly?":
        y s "Not completely."
        y n "But we can't rely on our radars past those things."
        y n "They could be jamming us,{w=0.15} this could be a trap,{w=0.15} we have no idea what's up ahead."
        y n "I know my ship is fast enough to get past them, but I don't know if we're suited to deal with what we might find."
        y n "I'll say that we don't see the typical signs of radar jamming as far as I can tell,{w=0.15} though."
        y s "And,{w=0.15} the weapons that they have are an unknown."
        pass

p n "I'm fairly confident Captain."
     
p n "With Haruka's one-of-a-kind engine and a complete suite of state of the art technology backing it up, {w=0.15}we should be able to vastly outpace even the most advanced crafts that exist within high-level stations."
     
p n "Let alone a.{w=0.15}.{w=0.15}. \"Lurk\""

menu:
    "Two prior options.":
        jump menuSmall4
        pass

    "OK, {w=0.15}I've made a decision.":
        pass

menu:
    "We will outrun them.":
        pass

    "We will fight.":#todo ending
        pass

show y m

y m "Seriously?{w=0.15} We could blow them away and find some cool stuff."

y s "Your loss cap."

show p h
e "Nema smiles."

show p n

p n "I'll begin plotting a course around the threat, {w=0.15}thank you sir."

menu:
    "Of course.":
        pass

    "It is what it is.":
        pass

show y n

y n "And I should get movin' too, {w=0.15}see ya at dinner."

menu:
    "Good luck to you both!":
        pass

    "Work hard!":
        pass

y h "Thanks Cap."

show p h

p h "Yes, {w=0.15}Captain!"

p n "Oh wait, {w=0.15}sir?"

menu:
    "Yes?":
        pass

p s "I'm sorry to bother you, {w=0.15}but.{w=0.15}.{w=0.15}. if at all possible, {w=0.15}could you find time to go and speak to Hei today?"

p n "I had a hard time speaking with him last night, {w=0.15}but I believe you could boost his morale."

menu:
    "Okay.":
        pass

play sound "sounds/DoorClose2.mp3"

call hall from _call_hall_26

e "You walk out of the room into the hall."

hide p

hide y

play sound "sounds/DoorClose2.mp3"
        
e "You walk up to Hei's door."

call redRoom from _call_redRoom_4

play sound "sounds/DoorOpen2.mp3"

menu:
    "Hei?":
        pass

    "Bud?":
        pass

show r n

r n "How are you feeling today?"

menu:
    "Great, {w=0.15}how about you?":
        pass

    "Hi.":
        pass

r h "Hey, {w=0.15}pretty grand.{w=0.25} Can't keep me down man."

r s "You know, {w=0.15}at first I was really down, {w=0.15}but I realized that Haruka was right."

menu:
    "Really?":
        pass

    "In what way?":
        pass

r n "Yeah, {w=0.15}she wants a strong man, {w=0.15}and I haven't shown that to her.{w=0.15} Why would she be interested?"

menu:
    "So what will you do?":
        pass

    "Good point.":
        r h "I know."
        r h "I also know what I have to do."
        pass

r h "Man up and get me a babe."

r n "I'm gonna work hard."

r n "What else?{w=0.25} I'm gonna become a man she can look to when she's in need."

r n "When all is lost, {w=0.15}and she needs a miracle, {w=0.15}I'll be the first thing she thinks of."

r h "That kind of man."

menu:
    "How?":
        pass

r n "Easy, {w=0.15}I already told you, {w=0.15}I'm gonna work hard."

menu:
    "At what?":
        pass

r n "Oh.{w=0.15}.{w=0.15}. Well, {w=0.15}I'll figure it out."

r h "You worry too much man, {w=0.15}I don't get why she likes you."

menu:
    "Excuse me?":
        pass

    "What do you mean?":
        pass

r h "No offense, {w=0.15}I think you're great, {w=0.15}but you don't really say, {w=0.15}or.{w=0.15}.{w=0.15}. do.{w=0.15}.{w=0.15}. much. It sounds like I'm being a dick, {w=0.15}but for real."

r n "How can she like you when you haven't given her anything to like?"

menu:
    "You're friends with Nema.":
        pass

r n "Well yeah, {w=0.15}she's great."

menu:
    "She doesn't say much.":
        pass

r n "Well, {w=0.15}no. I guess not.{w=0.25} But she kind of communicates in a different way."

menu:
    ".{w=0.15}.{w=0.15}.":
        pass

r n "Like, {w=0.15}I just get her. You know? I don't need to say a lot, {w=0.15}and neither does she. We're buds."

menu:
    ".{w=0.15}.{w=0.15}.?":
        pass

r n "Whatever man, {w=0.15}it's OK. I didn't mean to put you down, {w=0.15}just thinkin' out loud."

menu:
    "OK.":
        pass

r n "So, {w=0.15}I guess I should get to working on a plan. How to be a man.{w=0.15}.{w=0.15}."

menu:
    "Whatever happened to your plan for dinner last night?":
        pass

    "Alright, {w=0.15}good luck!":
        pass

r n "Plan for dinner last night?"

r su "What?"

menu:
    "You planned something to impress Haruka?":
        pass

    "Nevermind.":
        jump neverminded
        pass

r su "I did?"

menu:
    "You told me yesterday in the morning.":
        pass

    "Nevermind.":
        jump neverminded
        pass

r n "Me?{w=0.15} For Haruka?"

menu:
    "Yes, {w=0.15}you said it would blow my mind?":
        pass

    "Nevermind.":
        jump neverminded
        pass

r s "Blow your mind.{w=0.15}.{w=0.15}."

menu:
    "You don't remember?":
        pass

    "Nevermind.":
        jump neverminded
        pass

r h "It sounds like something I'd remember doesn't it?"

menu:
    "Yes. But you don't?":
        pass

    "Nevermind.":
        jump neverminded
        pass

r n "Nah."

label neverminded:

r h "Whatever dude."

r h "She'll be mine this time tomorrow,{w=0.15} just you wait!"

label noNevermind:

menu:
    "Good luck.":
        pass
    "Good luck, I guess?":
        pass

r h "Thanks!"

hide r

call hall from _call_hall_27

play sound "sounds/DoorClose2.mp3"

e "Everyone's busy working on a task."
        
call blueRoom from _call_blueRoom_12

e "You head to your room to try and get some things done."

window hide
show black
with fade

e "{w=0.25}.{w=0.35}.{w=0.45}."

play sound "sounds/DoorOpen2.mp3"

e "There's a knock on your door."

window hide
hide black
with fade

show p n

p n "Excuse me, {w=0.15}sir?"

p n "Dinner is ready, {w=0.15}at your convenience sir."

menu:
    "Thank you Nema.":
        pass

    "Okay.":
        pass

e "Nema smiles."

p n "I'll tell the rest."

p n "Haruka and Hei said they'd just be a little bit.{w=0.25} I'd like to suggest that we wait for them,{w=0.15} if that's alright with you Captain?"

define eatD4 = False

menu:
    "Of course.":
        e "Nema sits down across the table from you."
        jump nemaWaitD4
        pass

    "I'm hungry now.":
        pass

e "Nema sits down across the table from you."

e "You dig into the food, finishing it quickly."

e "It's got a great flavor to it."

menu:
    "This was great!":
        p h "I'm glad you think so, sir!"
        pass
    "Thanks.":
        p h "Of course, I'm happy to contribute."
        pass
    "...":
        pass

label nemaWaitD4:
e "Nema smiles shortly."

window hide
show black
with fade
e ".{w=0.15}.{w=0.15}."
e ".{w=0.35}.{w=0.35}."
window hide
hide black
with fade

p s "The others should be here soon.{w=0.15}.{w=0.15}."

menu:
    "What exactly did they say?":
        pass

p n "Haruka just glanced at me when I told her food was ready. "

p s "That's not an uncommon response from her though.{w=0.15}.{w=0.15}."

menu:
    "What about Hei?":
        pass

p n "He was playing a game and just said \"I know, {w=0.15}I know.\""

p s "I took that as his way of saying he would come as soon as possible, {w=0.15}but I suppose I assumed a bit much."

p n ".{w=0.15}.{w=0.15}."

p n "Not a problem, {w=0.15}I'll pack their meals away in the fridge."

menu:
    "Need help?":
        pass

    "OK.":
        pass

e "Nema ignores you for a second and moves to put the food away."

p s "C-captain.{w=0.15}.{w=0.15}. May I ask you a question?"

menu:
    "Yes.":
        pass

p n "W-"

e "Nema struggles to find words."

p n "No, {w=0.15}nevermind.{w=0.25} I figured it out."

p n "Thank you though. "

e "Nema smiled."

menu:
    "No, {w=0.15}what was it?":
        pass

    "No problem.":
        jump dontListenNemaD4
        pass

p n "I was going to ask what you.{w=0.15}.{w=0.15}."

p s "What.{w=0.15}.{w=0.15}.{w=0.15} Uhm.{w=0.15}.{w=0.15}.{w=0.15}.{w=0.15}.{w=0.15}.{w=0.15}."

p n "What do you think about the ship we spotted on the radar?"

e "Nema blushed."

menu:
    "Worried.":
        p h "That's oddly a relief to me.{w=0.15}.{w=0.15}.{w=0.15} Thank you."
        p s "To be quite honest, {w=0.15}I'm worried as well."
        pass

    "Not worried.":
        p su "Oh.{w=0.15}.{w=0.15}."
        p n "Wow,{w=0.15} I suppose that's one of many reasons that you are the captain."
        p s "I can't help but feel worried, {w=0.15}even a little panicked."
        p n "But we have to go on,{w=0.15} right?"
        pass

p n "These \"Lurks\" that we saw earlier, {w=0.15}I've noticed something weird."

p n "The shape has changed. From a triangular mass to a large circle. It seems to be slowly spreading out."

menu:
    "What does that mean?":
        pass

    "Uh oh.":
        pass

p n "It most likely is just interference, {w=0.15}but it makes me uneasy. If something is able to affect our view that much, {w=0.15}does that mean our information is unreliable?"

menu:
    "Should extra steps be taken?":
        pass

p s "No, {w=0.15}no. As I said, {w=0.15}I think it's just a sort of interference. It just gave me momentary pause, {w=0.15}I apologize Captain."

p n "I still firmly believe all that I said earlier this morning about the situation."

p n "I can't agree with hostility as our first action in meeting with this unknown ship."

label dontListenNemaD4:

#todo everything would not go dark in a spaceship
e "Suddenly, {w=0.15} everything goes dark."

p su "W-what's happening?!"

menu:
    "What do we do?":
        pass

p su "I-I'm not sure!{w=0.25} We-w-uhm.{w=0.15}.{w=0.15}."

p n "I don't know!"

menu:
    "Head to nav room. ":
        pass

    "Hide.":#todo end
        pass

play sound "sounds/DoorOpen2.mp3"

call navRoom from _call_navRoom_3

p n "Yes sir!"

menu:
    "What is it?":
        pass

#todo "Passed between us and the sun" Didn't we leave Earth and it's solar system, which includes the sun, behind? I thought we are testing some device for getting around fast. Maybe I misread something along the line.
p n "It looks like.{w=0.15}.{w=0.15}.{w=0.15}"

p n "We're getting some sort of interference from a large asteroid that's floating alongside us."

#todo this ties in with end, nema gathering power
p su "I'm not sure I've ever heard of an asteroid causing this sort of interference, but it seems clear that that's the source."

p n "Everything else is full power, {w=0.15}the autopilot AI is functioning normally, {w=0.15}we should be in no danger."

menu:
    "How did we not notice this asteroid before?":
        p n "I'm sorry sir, {w=0.15}I actually did notice the asteroid before, {w=0.15}but I failed to think it could have this affect."
        menu:
            "That's OK.":
                pass

            "Please keep an eye out for things like this.":
                p n "It wont happen again sir."
                pass
        pass

    "Good to hear!":
        pass

play sound "sounds/DoorOpen2.mp3"

e "The door opens and Haruka walks in."

show y n:
    linear 0 xalign 0.9 yalign 1.0

y n "What's happenin'?"

y n "The lights went out but everything seems fine."

show p n

p n "It seems to just be just a large asteroid interfering with our lights."

y su "Just our lights?"

y m "Hmmm.{w=0.15}.{w=0.15}."

y n "I suppose that sort of makes sense?"

y n "The lights are on their own circuits, but still.{w=0.15}.{w=0.15}."

show y n

y n "Anyways,{w=0.15} I thought we might be about to launch into something serious,{w=0.15} so I guess I'm thankful."

y n "How long's this gonna go on for?"

show p n

p n "My closest estimation is thirteen hours."

show y n

y n "Thirteen hours? Wow.{w=0.15}.{w=0.15}."

show p n

p n "Yes, {w=0.15}the asteroid is traveling almost perfectly parallel to us at a surprisingly close speed to our own."

show y h

y h "It's almost like we'll get to have our own personal night."

menu:
    "True.":
        pass

    "Troubling.":
        pass

y n "It's exciting. "

y h "A lil' taste of what things were like back on the blue rock, {w=0.15}eh?"

e "Haruka smiles."

y n "Perfect timing too, {w=0.15}I was thinking of grabbin' some food and hittin' the bed."

y n "Nems, {w=0.15}there any food left?"

show p n

p n "Oh, {w=0.15}yes. I saved a portion for you in the fridge."

show y h

y h "Thanks, {w=0.15}it smells so good, {w=0.15}I've been rushin' through my last bit of work so I could come get some."

show p su

p su "R-{w=0.15}really?"

show y n

y n "Course.{w=0.15} I'm starvin'."

show p h

p h "Oh, {w=0.15}thank you Haruka!"

show y m

y m "Sure?"

y h "Well, {w=0.15}I'm gonna go grab that, {w=0.15}thanks."

hide y

show p h

p h "Well, {w=0.15}of course!"

p h "I'm going to get to my room as well Captain, {w=0.15}be sure to enjoy this personal night the best you can!"

menu:
    "OK.":
        pass

    "I'll do my best!":
        pass

p h "Good night!"

play sound "sounds/DoorClose2.mp3"

call hall
e "You follow Nema out into the hallway."

hide p

e "She smiles at you as she walks into her room down the hall."

call blueRoom from _call_blueRoom_13
play sound "sounds/DoorOpen2.mp3"

e "You make your way to your own room."

play sound "sounds/DoorClose2.mp3"

e "You walk in,{w=0.15} and lay on your bed."

e ".{w=0.15}.{w=0.15}."

e "After some time, you drift off to sleep."

window hide
show black
with fade

return