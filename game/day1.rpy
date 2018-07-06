label day1:

$ seen_set = [ ]
$ save_name = "Introductions"

play music "music/Space.mp3" fadein 1.0

call beginningZoom from _call_beginningZoom

e "..."

play sound "sounds/DoorOpen2.mp3"

e "There's a sound from the hallway that sounds like a door opening."

e "The clock show's it's about 3AM."

e "You can faintly hear footsteps nearby."

menu:
    "Check it out.":
      pass
      
e "You stand and walk over to the entrance to your room."

call hall from _call_hall

play sound "sounds/DoorOpen2.mp3"

e "The door opens as you draw near."

e "There's a girl standing a few feet away in the hall."

show p su

p su "Oh! S-sorry captain... "

p su "I didn't mean to disturb you. Please excuse me, sir."

hide p su

e "The girl walks across the hall quickly."

play sound "sounds/DoorClose2.mp3"

e "She disappears into one of the doors across from you before you have a chance to speak."

e "Not a moment goes by before the door nearest to you slides open."

play sound "sounds/DoorOpen2.mp3"

e "A girl dressed in green walks out. She seems surprised to see you there."

play music "music/SpaceSunday.mp3" fadein 3.0

e "She stands closely in front of you."

show y h

y h "Hey there, Cap?"

menu:
    "Hello.":
      pass

    "Good morning?":
      pass

y h "Wasn't sure it was you."

y "Only saw you in pictures and stuff, you know."

y m "Pretty crazy they didn't even let us meet before sticking us on this thing and launching us off."

y m "I've been dying to talk to everybody, and they're just sitting in their rooms. "

y m "Buncha nerds."

y h "But, the big honcho finally shows his face!"

y "Baby steps. Right?"

menu:
    "It's... Haruka, right?":
        y h "That's right, you remembered. Consider me flattered."
        pass

    "Right.":
        y "Well, my name is Haruka."
        pass

y "You can just call me Haru though. "

y "I'm sure ya've read my file or something, so you already know I'm the engineer."

y "Little did you know, I'm also a terrible chef."

y h "And you thought you had me figured out, huh?"

y "You're allowed to be impressed. "

menu:
    "I'm speechless.":
      pass

    "Oh, great.":
      pass

y h "I know, I get it."

show y

y "Please try to hold it together for the sake of the crew though."

y h "We don't want them to know you're playing favorites already."

e "Haruka winks playfully."

show y

y "But hey, if you get on my good side, I'll make you a dry cake."

y "Would you like that?"

menu:
    "Oh... Uhm...":
        y h "Kidding."
        pass

    "Delightful.":
        y h "Alright, it's a date."
        pass
        
y "So... you can expect that from me."

y "But really? This mission is everything to me."

y "Four lives are being invested into my work. I get it. This is big."

y h "You can expect that I'll do my best. I'm not all doom and gloom, but I don't take any of this lightly."

y "And I expect the same from you."

menu:
    "You can count on me.":
        y h "Good."
        pass

    "I'll try.":
        y m "What? I hope you do more than try."
        pass

y "I made the ship, you gotta make the choices to keep it running."

y h "Right?"

menu:
    "Of course.":
      pass

y h "That's what I wanted to hear."

e "Haruka smiles."

show y

y "But... this is sort of heavy for introductions."

y "How about we have a drink? Celebrate our first night."

menu:
    "Sounds great!":
        y h "Alright, see you in the kitchen."
        pass

    "No thank you.":
        y h "Not taking no for an answer!"
        show y
        y "I'll see you in there."
        pass

hide y h

e "Haruka walks off."

menu:
    "Follow her into the kitchen.":
      pass
      
call kitchen from _call_kitchen

e "You enter the kitchen to see her standing by the counter."

show y

y h "Cap."

e "She nods her head."

y "Whatcha drinkin'?"

menu:
    "Same as you.":
        y "Comin' up."
        pass

    "None for me, thanks.":
        y "Alright, water it is."
        pass

y "So..."

y s "There's no way to really say this without being too forward..."

menu:
    "What is it?":
      pass

    "Then don't say it.":
        y h "Hah, that's not an option."
        show y
        y "Just wonderin'..."
        pass

y h "What kind of girls do ya like?"

menu:
    "What kind of girls?":
        y h "Yeah, what are you into?"
        pass

    "That's unprofessional.":
        y "We're gonna be stuck together for life."
        
        y h "I don't think it's weird to want to know, right?"
        
        menu:
            "I guess not...":
                pass
            "Well...":
                pass
                
        y h "So, what kind of girls?"
        pass

menu:
    "How do you mean?":
        pass

    "This is a job, not a bar.":
        y h "Lighten up! C'mon."
        pass

y "We'll start simple. Ease you in. "

y "What kinda hair color do ya fancy?"

menu:
    "Brown?":
        pass

    "I like unnatural colors.":
        pass

y "Hm."

y "What about personality?"

menu:
    "Extrovert.":
        y h "Gee, I think you're all out of luck."
        y h "Don't know many girls like that."
        e "Haruka smiles."
        pass

    "Introvert.":
        y s "Oh? Huh..."
        pass

play sound "sounds/DoorOpen2.mp3"

show p su at left

p su "H-hello?"

show p su: 
    linear 0.5 xalign 0.1
    
show y h

play sound "sounds/DoorClose2.mp3"

y "Speak of the devil."

menu:
    "Hello.":
      pass

    "Who are you?":
      pass

show p su

p su "S-sir! I'm sorry to intrude, I'd hoped to maybe grab some water, but I didn't realize you would be up at this hour..."

y "Your name is Nemo right?"

p h "Hello Nichi Haruka. That's close, but my name is Nematsu Hi."

y "My name is Haru, and you then, will be Nema. Sound good?"

show p s

p s "Oh, o-of course, if that's what y-you'd like."

p s "Captain, you may f-feel free to refer to me as N-Nema as well."

e "Nema looks nervous."

p s "Anyways, I'm once again, s-so sorry to intrude on y-you."

y h "Damn, calm down Nemo, we're crewmates. Don't be so terrified."

show y

y "Sit down and have a drink with us."

y h "Loosen up, yeah?"

show p s

p s "Oh, s-sure..."

show y

y "That's the spirit, what a loose cannon."

menu:
    "It's OK Nema, take your time.":
        p h "T-thank you, Captain..."
        pass

    "You feeling alright Nema?":
        p s "I'm f-fine."
        pass

show p h

e "Nema smiles."

show y

show p

y "You know, we only need Mr. Weapons and we'll have our first crew meeting."

menu:
    "Somebody should get him.":
      pass

y "Just what I was thinking."

hide y

play sound "sounds/DoorOpen2.mp3"

e "Haruka leaves."

menu:
    "She's energetic, isn't she?":
      pass

show p

p "Y-yes sir, she is."

e "Nema smiles."

e "..."

e "A few moments pass in silence..."

show y


play sound "sounds/DoorClose2.mp3"

y "Said he'd be over in a minute."

y h "Seems like he'll be interesting."

y "Take that how ya'd like."

menu:
    "Interesting?":
      pass

    "Alright.":
      pass

y su "Yeah... I don't know if I should repeat what I saw."

show p su

p su "Oh my..."

show y

y "Yep."

y "But, while we wait, Nemo, tell us what you do?"

show p h

p h "Oh, uhm, absolutely."

p s "My n-name is... uh, Nematsu Hi. "

p "My role on this m-mission is as a scientific historian, so I'll be ta-"

show y su

y su "A scientific historian?"

show p

p "Well I will b-"

show y

y "That doesn't make sense. Scientist I understand, a historian I get... Well shit, actually no."

y m "Why would we need a historian at all?"

y "Oh hey Cap, we're in danger. Quick, who was the birthmother of Andrew Jackson?"

y h "Is that sorta what ya do?"

show p s

p s "Not quite Haruka, I'll be taking l-"

show y

y "Call me Haru."

show p s

p s "Oh, of course."

p "As I was saying, I'll b-"

show p su

play sound "sounds/DoorOpen2.mp3"

e "The door opens and the last crew member walks into the room."

show r h: 
    xalign 0.9

r h "Howdy!"

show p

menu:
    "Hey.":
      pass

    "Welcome, nice of you to join us.":
      pass

e "The last member of the crew nods at you."

r h "Ladies."

e "He nods again."

r "The name's Hei. Hei Babe. "

e "Hei winks seductively at Haru."

show p h

e "Nema smiles."

show y m

y m "Oh god. "

show r

r h "Seriously though, my name is Hei."

show p

show y

p "Nice to meet you Hei."

e "Hei nods."

show r

r "So..."

y "Yes, Mr. Babe?"

r "What have you guys been talking about?"

menu:
    "Nema was about to tell us something.":
        r h "Oh is that so? What's that?"
        pass

    "Nothing.":
        p s "O-oh..."
        y "Wasn't Nima saying something?"
        pass

p "I was just try-"

y "She was telling us about her job, she's a librarian or something?"

e "Nema looks unbothered by the frequent interruptions."

r h "Oh, great. What's your job Haru?"

y "I do whatever Cap needs."

e "She smiles at you."

r su "Oh really cool, like a second in command right?"

y h "Exactly like that."

show r

r "Do we have a third in command?"

show y

y "No."

show r h

r h "Can I be third in command?"

show y

y "I don't see why not."

p s "So I'm f-fourth in line..."

e "Hei smiles"

show r h

r h "Don't worry, I'll save the worst jobs for you Nema."

e "Nema smiles."

show p h

p s "T-there actually is no second in command... is there?"

menu:
    "No. ":
      pass

    "Absolutely not.":
      pass
      
show p h

e "Nema looks relieved."

show y

y "Hey Cap, speaking of being in command, I just remembered something. Someone needs ta pull an all nighter tomorrow to monitor the engine through the first milestone. "

y "Who do ya want on that?"

show r su

r su "Wait, are you talking about like, work?"

e "Hei groans."

e "Nema waits quietly."

menu:
    "I do it this time.":
        y h "Sure thing cap."
        pass

    "Haruka, you seem to understand it best.":
        y "No problem!"
        y s "But, actually..."
        show y
        y "Would you mind staying up with me just this once?"
        y h "Since you're the captain and all, you should probably know the process, right?"
        menu:
            "Makes sense":
                y h "Great!"
                pass
        pass

show y h

show r h

r h "Awesome."

show p s

p s "I wouldn't have minded doing it."

show y

y "But now you don't have to. Everyone wins."

show r

r "Seriously, get some sleep and enjoy it."

show p s

p s "Right... "

e "Nema looks warily at you."

show r h

r h "Think of it this way, now you can be rested the next morning, and help cover for the captain while he makes up for his long night."

e "Nema nods, she seems satisfied."

e "There is a moment of silence"

show y

y "Well... I'm going to bed."

show r

r "Ditto, see you snaggle babies in the morning. Just wanted to say hi."

play sound "sounds/DoorOpen2.mp3"

hide r

p "Snaggle babies...."

y "Later."

hide y

show p s:
    linear .5 xalign 0.5

play sound "sounds/DoorClose2.mp3"

p s "Oh, Okay."

p "I guess it is pretty late, isn't it?"

e "Nema seems hesitant to leave."

menu:
    "Hang back for a moment.":
      pass

    "Goodnight.":
        jump day1End
        pass

p su "Not tired Sir?"

menu:
    "I wanted to talk to you.":
      pass

p h "Of course, what's on your mind?"

menu:
    "What were you saying earlier about your job here?":
      pass

p h "Oh, yes."

p "I'm the scientific historian for our journey. "

p "It's not a core role to the mission, but I will provide quite a lot of value to our home station by charting out new space, and conducting various experiments. "

p "It's my task to take any information with an ounce of value, and get that information back to our station."

menu:
    "Sounds valuable to me!":
        p "Thank you sir."
        pass
    "I see.":
        pass

e "Nema nods slightly and bows"

menu:
    "What do you think about the crew?":
      pass

p "I... look forward to getting to know them."

p "I'm a little aprehensive about..."

p "No, I'm excited to see what comes of our close proximity."

p "It will be an interesting experience to say the least."

p h "I hope to create valuable relationships here."

e "She blushes."

menu:
    "Me too.":
        p "I'm happy to hear that sir."
        pass

    "Well, we'll see how things go.":
        p "Yes, surely we will."
        pass
e "..."      

show p

p "Well..."

p "I think I'm going to begin preparing for sleep as well."

p h "I look forward to working together, Sir."

menu:
    "It will be interesting.":
        show p
        p "I believe it will sir."
        pass
    "Me too.":
        pass

show p

p "Well..."

label day1End:

p "Goodnight, Captain."

stop music fadeout 5

play sound "sounds/DoorOpen2.mp3"

hide p

e "Nema walks out into the hallway."

play sound "sounds/DoorClose2.mp3"


menu:
    "Might as well head to bed as well.":
        pass
        
play music "music/Space.mp3" fadein 2.0

call hall from _call_hall_1

e "You walk out into the hallway and see all of the doors shut."

e "The ship is silent."

play sound "sounds/DoorOpen2.mp3"

call blueRoom from _call_blueRoom

e "You enter your room and head straight for your bed."

play sound "sounds/DoorClose2.mp3"

e "As soon as you lay your head down on the pillow, you feel yourself dozing off."

show black
with fade

e "..."


return