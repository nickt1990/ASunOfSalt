label day2:
    
hide black

play music "music/MorningAlarm.mp3" fadein 2.0

e "You wake up to your computers alarm."

e "The room is lit up by the mail notification on your computer screen."

menu:
    "Check mail.":
        stop music fadeout 1
        pass

e "Once you pull yourself away from the computer, you hear a strange sound.{w=0.15}.{w=0.15}."

e "There's a faint sound of music coming from the hallway."

menu:
    "Check it out.":
        pass
        
call hall from _call_hall_16

play sound "sounds/DoorOpen2.mp3"

e "The music seems to be coming from the kitchen."

play sound "sounds/DoorOpen2.mp3"

menu:
    "Enter kitchen.":
        pass

call kitchen from _call_kitchen_4

e "You walk in to find Nema sitting at the table with a small music player."

e "She seems surprised to see you walk in, {w=0.15}and quickly turns off her music."

stop music fadeout 1

play music "music/Space.mp3" fadein 2.0

show p s

p s "C-captain I apologize if my music bothered you. I tried to keep it at a reasonable volume but I'll be sure to use headphones from now on sir."

menu:
    "It didn't bother me at all.":
        pass

    "What were you listening to?":
        pass

p s "Well, {w=0.15}I will be sure to continue being cautious."

p n "Anyways, {w=0.15}I was just heading back to my room."

p n "Have a good morning Captain."

menu:
    "Join me?":
        pass

    "Have a good morning, {w=0.15}Nema.":
        pass

p s "No, {w=0.15}I really should be back to work. Thank you though Captain."

play sound "sounds/DoorClose2.mp3"

hide p

e "Nema bows slightly and walks out of the room."

e "You pour yourself a bowl of cereal and sit at the table to eat."

menu:
    "Turn on radio":
        pass

    "Eat in silence.":#todo cut to asking about anime
        pass

e "The radio starts to quietly play the music that Nema had been listening to."

e "A moment goes by as you continue to eat, {w=0.15}and Haruka walks in."

show y h

y h "Morrrrnin'."

menu:
    "Good morning.":
        pass

    "Nod.":
        pass

y n "Listenin' to some tunes, {w=0.15}yeah?"

e "Nema creeps back into the picture, {w=0.15}just outside the room."

y n "This is that one band that was popular a few years ago right?"

y s "What was their name?"

menu:
    "Little Legs?":
        pass

    "Penguin Boys?":
        pass

y s "No..."

y n "Whatever."

y h "I was obsessed for a bit, {w=0.15}this is a major throwback."

menu:
    "They do sound great.":
        pass

    "They sound terrible...":
        pass

y n "Really?"

y s "Can't say they've held up for me."

y h "I'm glad you're happy though Cap."

e "Her voice is a little patronizing."

e "Nema blushes in the hallway and runs off."

y n "Anyways, {w=0.15}was just heading back to my room."

y h "Wanna come and watch some anime with me?"

menu:
    "Yes.":
        pass
    "No.":
        pass


y m "Fine, {w=0.15}I get it. Busy man."

hide y m

play sound "sounds/DoorOpen2.mp3"

e "Haruka walks over to her room."

e "You finish your food and walk out into the hallway."

call hall from _call_hall_17

play sound "sounds/DoorClose2.mp3"

e "YOU ARE NOW ABLE TO EXPLORE A LITTLE"

e "NAV ROOM CONTINUES MAIN STORYtodo"

e "HARUKAS ROOM" #todo make menu choice for rooms

call yellowRoom from _call_yellowRoom_1

show y hR

y h "Hey champ, {w=0.15}came to visit me after all?"

y n "Quite the rebel aren't ya?"

menu:
    "Yes. Yes I am.":
        pass

    "Just checking in.":
        pass

y h "Very impressive, {w=0.15}what a hero."

e "She smiles."

y n "Watch a little with me, {w=0.15}I need a break."

e "You sit and look at the screen with her."

y n "He's gonna get wrecked."

y n "Just wait.{w=0.15} Right here."

e "Somebody on the screen explodes."

y h "Boom!"

y h "God.{w=0.15} I love this show."

e "You and Haruka sit quietly, enthralled in the show on the television."

show black
with fade

e ".{w=0.35}.{w=0.35}."

hide black
with fade

y n "And that's it. What'd ya think?"

menu:
    "Awesome.":
        pass

    "Pretty dumb.":
        pass

y h "Agreed."

y n "Mako's just too damn sexy."

y h "What a badass."

y n "Ya think I could pull off her kind of look?"

y s "Hmm.{w=0.15}.{w=0.15}."

y s "I don't think I could."

y su "Could I?"

y s "No."

e "She looks troubled."

y h "Well, {w=0.15}I'll work on it."

y n "But, {w=0.15}I'm gonna take a little nap,{w=0.15} if ya don't mind."

y h "I'll talk to you in a bit Cap."

menu:
    "Exit the room.":
        hide y
        call hall from _call_hall_18
        pass

hide m2

e "NEMAS ROOM"

call pinkRoom from _call_pinkRoom

show p n

p n "Oh, {w=0.15}good afternoon Captain."

e "Nema smiles bashfully."

p h "Good timing, {w=0.15}I was just about to come looking for you."

menu:
    "Whats up?":
        pass

    "How can I help you, {w=0.15}Nema?":
        pass

p n "I just finished my report for my first day of findings. Would you mind going over it for me?"

menu:
    "Sure.":
        pass

    "No thanks.":
        pass

p h "Excellent!"

p n "It's sitting at the desk, {w=0.15}feel free to look it over."

hide p

e "Nema grabs a small notebook and lays down on her bed."

menu:
    "Pick up the paper on Nema's desk.":
        pass

e ".{w=0.15}.{w=0.15}."

e ".{w=0.15}.{w=0.15}.{w=0.15}."

e ".{w=0.15}.{w=0.15}.{w=0.15}{w=0.15}.."

e "The report basically just says \"no findings yet\" in an overly verbose way."

e "She's still absorbed in the notebook on her bed."

e "She doesn't appear to be paying attention."

e "One of the drawers is just barely open and you can make out some sort of object inside."

menu:
    "Don't snoop.":
        e "You decide to give her privacy."
        pass

    "Snoop it up!":
        pass

e "You take a moment to observe the room."

e "The room smells like a flower garden. Sort of earthy, {w=0.15}but pleasant."

e "She has pencils and books lined up on her desk. "

e "One of her drawers is slightly open."

menu:
    "Report looks great. Good job.":
        pass

    "What's with the alcohol in your desk?":
        pass

p n "Thank you sir. I do my best."

p n "Anyways sir, {w=0.15}I have a lot to attend to, {w=0.15}and I don't want to keep you."

p n "Please have a wonderful day Captain, {w=0.15}and feel free to inform me of any way I can be of help."

call hall from _call_hall_19

e "You walk out her door into the hallway."

hide p

menu:
    "HEI ROOMtodo":
        call redRoom from _call_redRoom_2
        pass

show r h

r h "Hey dude. Wanna play?"

e "Hei is sitting in front of an old gaming system on the floor."

e "He motions his hand to the second controller."

menu:
    "Sure.":
        e "You pick up the controller and start playing with him."
        pass

    "No, {w=0.15}just checking in.":
        pass

r n "I don't have the newest one, {w=0.15}but Soft and Moist Vegetables: 2 Turbo Vegetable Edition is the best anyways."

r h "Best games ever made, {w=0.15}if you ask me."

r n "Like, {w=0.15}yeah, {w=0.15}it's not a epic story with a huge budget and whatever."

r n "But you get to kick people in the face and I think it does that well."

menu:
    "You have tough standards.":
        pass

    "I do like face kicking.":
        pass

r h "I like what I like man."

r h "I used to play this all the time when I was a kid. My family had a maid, {w=0.15}and she would bring her kid over on the weekends."

r n "I totally kicked his ass every time."

r m "He didn't even stand a chance against the MANGLER."

r n "I could have probably played pro."

menu:
    "Pro, {w=0.15}huh?":
        pass

    "The Mangler. Right.":
        pass

r n "Yeah, {w=0.15}I barely even played by myself. I was just that good."

r su "I tell you it ju-"

r n "..."

r su "Did you just beat me?"

menu:
    "Yes.":
        pass

    "What does it look like?":
        pass

r n "Well... Shit."

e "He's stopped functioning. "

e "He no longer appears to be breathing."

e "He's probably joking, {w=0.15}but... it's getting weird."

menu:
    "I think... I'm gonna go.":
        pass

    "Wanna play again?":
        pass

r m "NO! REMAAAAATCH."

e "He slapped you in the face and frowned."

r m "Les go, {w=0.15}bitch."

e "Not being left much of a choice, {w=0.15}you play another round with him."

e "..."

e "..."

e "..."

r su "You won... again."

r n "Did you used to have this game?"

menu:
    "Soft and Moist Vegetables: 2 Turbo Vegetable Edition? No.":
        pass

    "Uh, {w=0.15}sure. ":
        pass

r m "Psh, {w=0.15}right. You probably used to play this all the time."

r m "Nerd."

e "..."

e "..."

e "He looks sad."

e "You turn to leave."

r s "Wait."

e "He walks up behind you."

r s "I have to tell you something sir."

r s "I..."

r s "I never beat my maids son in the game."

r s "I never even won a match against another person."

r n "I've been practicing since we got on this ship, {w=0.15}it's been at least 20 hours of nothing but intense training. I really tried."

menu:
    "This is all you've been doing?":
        pass
    "...":
        pass

r s "I thought I could reinvent my image. This was to be my big debut."

r s "I'm... sorry."

e "You see tears well up in his eyes. "

menu:
    "Rematch. One week from today.":
        pass

    "*Blow raspberry*":
        pass

e "He looks surprised for a second."

r n ".{w=0.15}.{w=0.15}."

r h "Bring your big boy pants."

r m "'Cuz I'm gonna F**K YOU UP!"

r h "YEEEEEEHAW!"

r n "Get out."

e "He goes back to the game."

hide r

e "You make your way back out into the hallway."

call hall from _call_hall_20

menu:
    "NAV ROOM":
        call navRoom from _call_navRoom_2
        pass

e "Everyone shows up right behind you."

menu:
    "What's going on?":
        pass

    "Ah, {w=0.15}just in time for the meeting.":
        pass

show y n

y n "You called a meeting remember?"

menu:
    "Yes.":
        pass

y h "No you didn't, {w=0.15}ass. I grabbed everyone."

show p n:
    linear 0 xalign 0.1

p n "Captain, {w=0.15}Haruka expressed an interest in setting a sort of schedule."

show r m:
    linear 0 xalign 0.9 yalign 1.0

r m "I don't see why we need one. We'll be fine. "

show y n

y n "What have you done so far Mr. Babe?"

show r n

r n "I've been productive."

show y m

y m "No. Ya haven't."

show r s

e "Hei frowns."

y h "They say a schedule is the best way to ensure productivity."

y n "So what do you have for us? Ideas?"

menu:
    "Yes.":
        pass

    "What do you think?":
        pass

y h "Great lets hear it!"

e "You did not plan for this."

y s "...You don't have a clue do you?"

y h "Fine. Points for trying. "

y n "Anyone else?"

show r su

r su "What?"

e "Hei obviously had not been listening."

e "Nema was fidgeting with her hands."

show p s

p s "Well, {w=0.15}we c-could... maybe..."

show y m

y m "Ugh."

y n "Well, {w=0.15}I don't want to babysit you all, {w=0.15}but I sort of assumed you guys would be a little more excited to get stuff done."

y n "Maybe we don't need to have a strict schedule, {w=0.15}but there should be some sort of periodic progress update."

y n "We need some way of knowing things are getting done, {w=0.15}that's part of a Captains job, {w=0.15}right?"

e "She looks accusingly at you."

menu:
    "You're not children. ":
        pass

    "Do what you want.":
        pass

y n "Fair enough, {w=0.15}I think we can trust each other to do what we need to, {w=0.15}right?"

y n "Any concerns?"

show r s

r s "Do I have to get up early."

show y m

y m "Seriously? Only if you want."

y m "Idiot."

e "Hei smiles."

menu:
    "Say nothing.":
        pass

    "Good work Haruka.":
        pass

y n "Cap, {w=0.15}I'd use any time you have today to get comfortable with the ship and your new equipment."

y n "I want you to be comfortable with the basic functions of the ship in case I'm not available for some reason."

show p h

p h "Haruka, {w=0.15}th-"

show y n

y n "What."

show p s

p s "Thank you for your hard work. "

e "Haruka looked blankly at Nema for a brief moment then turned back to you."

show y n

y n "Alright, {w=0.15}well how do you guys feel about getting some food in us? I'll cook?"

show r h

r h "Yes mumsy."

e "There is silence."

r n "..."

show y n

y n "What is wrong with you?"

show p y

show r h

e "Hei chuckles and Nema smiles."

show r h

r h "Let's go, {w=0.15}I'm starving."

call hall from _call_hall_21

e "Everyone moves into the kitchen."

play sound "sounds/DoorOpen2.mp3"

call kitchen from _call_kitchen_5

r n "What are we having Haru?"

show y h

y h "Ramen.{w=0.15} My specialty."

show p n

p n "My mother used to run a ramen stand when I was a kid."

show y n

y n "Cool. "

show p h

p h "Yes. I am told my ramen is quite good."

show y n

y n "Oh. Cool."

e "It's mostly silent while Haruka cooks."

y h "So who wants the first dish?"

menu:
    "Give it to me.":
        pass

    "Give it to Nema.":
        pass

y n "Sure thing boss."

menu:
    "It's great!":
        y h "I know!"
        pass
    "Stay silent":
        y h "good, right?"
        y n "I know it is. You don't have to say a word."
        y h "Just enjoy."
        pass

e "Haruka is beaming with confidence."

y n "Alright. The rest of you get your own."

e "Everyone grabs their food and sits down to the table."

show r s

r s "Man, {w=0.15}I'm tired."

show y n

y n "Tired from what. You haven't done a single today."

show r s

r s "Why do you try so hard to hurt me?"

e "Haruka rolls her eyes."

r n "I'm looking forward to a nice sleep."

r n "How about you Captain?"

e "Hei sticks his tongue out."

menu:
    "Are you volunteering Hei?":
        pass

e "Nema chuckles."

e "Hei slowly withdraws his tongue."

show y n

y n "Hei you're pathetic."

show r h

r h "Oh c'mon. I know you think I'm charming."

show y n

y n "Not even close."

show r h

r h "You think I'm charming."

e "Hei smiles. Haruka sighs. Nema giggles."

show p h

p h "I think you're plenty charming Hei."

e "Nema gives a sweet smile."

show y m

y m "God, {w=0.15}please."

show r n

r n "Loved by all, {w=0.15}sought after by many, {w=0.15}tamed by none."

show y m

y m "You sound like a damn car commercial."

y n "What gives you this huge ego? "

y n "Are you secretly not a huge waste of space?"

show r n

r n "Yes. Secretly, {w=0.15}I am a great use of space."

e "Nema chuckles."

show p h

p h "High value to volume ratio."

show r h

r h "Precisely. I'm the bargain of the century ergonomically."

show y n

y n "Ergonomic. You sure that's the word you want?"

show r h

r h "That's what it says, {w=0.15}right on the box."

r n "Premium label baby."

show y m

y m "Alright. I thought you were tired?"

show r su

r su "You know... I am."

r n "I think I'll have myself a snooze."

r h "Captain! Good luck my fearless Captain."

menu:
    "Thanks!":
        r n "Hei smiles"
        pass
    "Your turn next time.":
        r n "Hei's eyes get wide. He walks away."
        pass

e "Hei walks out into the hallway."

hide r

e "for a moment there is silence."

show p s

p s "Haruka, {w=0.15}do you plan on staying up for a while?"

show y n

y n "Actually, {w=0.15}I thought I might help Cap pass the time tonight."

menu:
    "What do you mean?":
        y n "I'm gonna stay up with you."
        pass
    "You want to stay up?":
        pass

y h "It'll be fun! "

show p s

p s "Oh. I see, {w=0.15}nice. Ok."

p s "Then I guess I'll just retreat to my room for the night."

p n "U-unless... you'd like another pair of hands to help?"

show y n

y n "I think we got it, {w=0.15}right Cap?"

menu:
    "Yeah, {w=0.15}we're good.":
        pass

show p n

p n "Yes sir... I'll gladly take the shift next week, {w=0.15}if that would help?"

hide p n

e "Nema walks out of the room and heads to bed."

show y n

y n "So, {w=0.15}take an hour and meet in the nav room, {w=0.15}yeah?"

menu:
    "Sounds good":
        pass

y h "Right-o"

hide y h

return