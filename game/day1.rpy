﻿label day1:

window hide
show black

$ seen_set = [ ]
$ save_name = "Introductions"

play music "music/Space.ogg" fadein 1.0

call beginningZoom from _call_beginningZoom

$ renpy.pause(1.5, hard=True)

e ".{w=0.15}.{w=0.15}."

e "It's your first night as captain aboard an experimental ship."

e "Due to the unorthidox nature of the mission,{w=0.15} you were placed on the ship with little knowledge of your crew or your goal."

e "You were guided straight to your room,{w=0.15} and then sent off."

e "\"Instructions will come\" is what you were told."

e ".{w=0.15}.{w=0.15}."

e "It's been quiet for hours at this point."

e "But suddenly-"

play sound "sounds/DoorOpen2.ogg"

e "You hear a sound like a door opening from the hall."

e "The clock shows it's about 3AM."

e "You can faintly hear footsteps nearby."

menu:
    "Check it out.":
        window hide
        hide black
        with fade
        pass
      
e "You stand and walk over to the entrance to your room."

call hall from _call_hall

play sound "sounds/DoorOpen2.ogg"

e "The door opens as you draw near."

e "There's a girl standing a few feet away in the hall."

show pc su

pc su "Oh!{w=0.15} S-{w=0.15}sorry captain... "

pc su "I didn't mean to disturb you. {w=0.15}Please excuse me, sir."

hide pc su

e "The girl walks across the hall quickly."

play sound "sounds/DoorClose2.ogg"

e "She disappears into one of the doors across from you before you have a chance to speak."

e "Not a moment goes by before the door nearest to you slides open."

play sound "sounds/DoorOpen2.ogg"

e "A girl dressed in green walks out.{w=0.15} She seems surprised to see you there."

play music "music/SpaceSunday.ogg" fadein 3.0

e "She stands closely in front of you."

show y h

y h "Hey there, Cap?"

menu:
    "Hello.":
      pass

    "Good morning?":
      pass

y h "Wasn't sure it was you."

y "Only saw you in pictures and stuff,{w=0.15} you know."

y m "Pretty crazy they didn't even let us meet before sticking us on this thing and launching us off."

y m "I've been dying to talk to everybody,{w=0.15} and they're just sitting in their rooms. "

y m "Buncha nerds."

y h "But,{w=0.15} the big honcho finally shows his face!"

y "Baby steps. Right?"

menu:
    "It's... Haruka, right?":
        y h "That's right,{w=0.15} you remembered. Consider me flattered."
        pass

    "Right.":
        y "Well, {w=0.15}my name is Haruka."
        pass

y "I'm sure ya've read my file or something,{w=0.15} so you already know I'm the engineer."

y "Little did you know,{w=0.15} I can also juggle."

y h "And you thought you had me figured out,{w=0.15} huh?"

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

y "But hey,{w=0.15} if you get on my good side, I'll toss a few bowling pins for ya."

y "Would you like that?"

menu:
    "Oh... Uhm...":
        y h "Kidding."
        pass

    "Delightful.":
        y h "Alright,{w=0.15} it's a date."
        pass
        
y "So.{w=0.15}.{w=0.15}.{w=0.15} you can expect that from me."

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

y "I made the ship,{w=0.15} you gotta make the choices to keep it running."

y h "Right?"

menu:
    "Of course.":
      pass

y h "That's what I wanted to hear."

e "Haruka smiles."

show y

y "But.{w=0.15}.{w=0.15}.{w=0.15} this is sort of heavy for introductions."

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

play sound "sounds/DoorOpen2.ogg"

e "Haruka walks off."

menu:
    "Follow her into the kitchen.":
      pass
      
call kitchen from _call_kitchen

play sound "sounds/DoorClose2.ogg"

e "You enter the kitchen to see her standing by the counter."

show y

y h "Cap."

e "She nods her head."

y "What'cha drinkin'?"

menu:
    "Same as you.":
        y "Comin' up."
        pass

    "None for me, thanks.":
        y "Alright,{w=0.15} water it is."
        pass

y "So..."

y s "There's no way to really say this without being too forward..."

menu:
    "What is it?":
      pass

    "Then don't say it.":
        y h "Hah,{w=0.15} that's not an option."
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
        y h "Lighten up! {w=0.15}C'mon."
        pass

y "We'll start simple. Ease you in. "

y "What kinda hair color do ya fancy?"

menu:
    "Brown?":
        y h "Good choice!"
        pass
    "Blonde?":
        y n "Oh?"
        y s "Well I guess that's unfortunate for you."
        pass
    "Black?":
        pass
    "Red?":
        y su "Red?"
        y s "Well I guess that's unfortunate for you."
        pass
    "I like unnatural colors.":
        y m "Like pink?"
        pass

y n ".{w=0.25}.{w=0.25}."

y "Hm."

y "What about personality?"

menu:
    "Extrovert.":
        y h "Gee,{w=0.25} I think you're all out of luck."
        y h "Don't know many girls like that."
        e "Haruka smiles."
        pass

    "Introvert.":
        y s "Oh? Huh..."
        pass

play sound "sounds/DoorOpen2.ogg"

show pc su at left

pc su "H-hello?"
    
show y h

play sound "sounds/DoorClose2.ogg"

y "Speak of the devil."

menu:
    "Hello.":
      pass

    "Who are you?":
      pass

show pc su

pc su "S-{w=0.15}sir! I'm sorry to intrude,{w=0.15} I'd hoped to maybe grab some water, {w=0.15}but I didn't realize you would be up at this hour..."

y "Your name is Nemo right?"

pc h "Hello Nichi Haruka.{w=0.15} That's close, {w=0.15}but my name is Nematsu Hi."

y "Call me Haruka,{w=0.15} and you then,{w=0.15} will be Nema.{w=0.35} Sound good?"

show pc s

pc s "Oh, o-{w=0.15}of course, {w=0.15}if that's what y-you'd like."

pc s "Captain,{w=0.15} you may f-{w=0.15}feel free to refer to me as N-Nema as well."

e "Nema looks nervous."

pc s "Anyways,{w=0.15} I'm once again, s-{w=0.15}so sorry to intrude on y-{w=0.15}you."

y h "Damn, {w=0.15}calm down Nemo, we're crewmates. Don't be so terrified."

show y

y "Sit down and have a drink with us."

y h "Loosen up, yeah?"

show pc s

pc s "Oh, s-{w=0.15}sure.{w=0.15}.{w=0.15}."

show y

y "That's the spirit, what a loose cannon."

menu:
    "It's okay Nema, take your time.":
        pc h "T-{w=0.15}thank you, Captain.{w=0.15}.{w=0.15}."
        pass

    "You feeling alright Nema?":
        pc s "I'm f-{w=0.15}fine."
        pass

show pc h

e "Nema smiles."

show y

show pc h

y "You know, {w=0.15}we only need Mr. Weapons and we'll have our first crew meeting."

menu:
    "Somebody should get him.":
      pass

y "Just what I was thinking."

hide y

play sound "sounds/DoorOpen2.ogg"

e "Haruka leaves."

menu:
    "She's energetic,{w=0.15} isn't she?":
      pass

show pc

pc "Y-{w=0.15}yes sir, {w=0.15}she is."

e "Nema smiles."

e ".{w=0.25}.{w=0.25}."

e "A few moments pass in silence..."

show y


play sound "sounds/DoorClose2.ogg"

y "Said he'd be over in a minute."

y h "Seems like he'll be interesting."

y "Take that how ya'd like."

menu:
    "Interesting?":
      pass

    "Alright.":
      pass

y su "Yeah... {w=0.15}I don't know if I should repeat what I saw."

show pc su

pc su "Oh my.{w=0.15}.{w=0.15}."

show y

y "Yep."

y "But,{w=0.15} while we wait,{w=0.15} Nemo, tell us what you do?"

show pc h

pc h "Oh, {w=0.15}uhm, {w=0.15}absolutely."

pc s "As I said, my n-{w=0.15}name is{w=0.15}.{w=0.15}.{w=0.15}.{w=0.15} {w=0.15}uh,{w=0.15} Nematsu Hi. "

pc "My role on this m-{w=0.15}mission is as a scientific historian, so I'll be ta-"

show y su

y su "A scientific historian?"

show pc

pc "Well I will b-"

show y

y "That doesn't make sense. Scientist I understand, a historian I get... Well shit, actually no."

y m "Why would we need a historian at all?"

y "Oh hey Cap,{w=0.15} we're in danger.{w=0.15} Quick, who was the birth-mother of Andrew Jackson?"

y h "Is that sorta what ya do?"

show pc s

pc s "Not quite Haruka,{w=0.15} I'll be taking l-"

show y

y "Call me Haru."

show pc s

pc s "Oh, of course."

pc "As I was saying,{w=0.15} I'll b-"

show pc su

play sound "sounds/DoorOpen2.ogg"

e "The door opens and the last crew member walks into the room."

show r h: 
    xalign 0.9

r h "Howdy!"

show pc

menu:
    "Hey.":
      pass

    "Welcome, nice of you to join us.":
      pass

e "The last member of the crew nods at you."

r h "Ladies."

e "He nods again."

r "The name's Hei.{w=0.15} Hei Babe. "

e "Hei winks seductively at Haru."

show pc h

e "Nema smiles."

show y m

y m "Oh god. "

show r

r h "Seriously though, my name is Hei."

show pc

show y

pc "Nice to meet you Hei."

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
        pc s "O-oh..."
        y "Wasn't Nima saying something?"
        pass

pc "I was just try-"

y "She was telling us about her job, {w=0.15}she's a librarian or something?"

e "Nema looks unbothered by the frequent interruptions."

r h "Oh, great.{w=0.15} What's your job Haru?"

y "I do whatever Cap needs."

e "She smiles at you."

r su "Oh really?{w=0.35} Cool, {w=0.15}like a second in command right?"

y h "Exactly like that."

show r

r "Do we have a third in command?"

show y

y "No."

show r h

r h "Can I be third in command?"

show y

y "I don't see why not."

pc s "So I'm f-{w=0.15}fourth in line.{w=0.15}.{w=0.15}."

e "Hei smiles"

show r h

r h "Don't worry, {w=0.15}I'll save the worst jobs for you Nema."

e "Nema smiles."

show pc h

pc s "T-{w=0.15}there actually is no second in command.{w=0.15}.{w=0.15}.{w=0.15} is there?"

menu:
    "No. ":
      pass

    "Absolutely not.":
      pass
      
show pc h

e "Nema looks relieved."

show y

y "Hey Cap,{w=0.15} speaking of being in command,{w=0.15} I just remembered something. {w=0.35}Someone needs ta pull an all nighter tomorrow to monitor the engine through the first milestone. "

y "Who do ya want on that?"

show r su

r su "Wait,{w=0.15} are you talking about like, work?"

e "Hei groans."

e "Nema waits quietly."

define harukaNight2 = True

menu:
    "I do it this time.":
        $ harukaNight2 = False
        y h "Sure thing cap."
        pass

    "Haruka, you seem to understand it best.":
        y "No problem!"
        y s "But,{w=0.15} actually.{w=0.15}.{w=0.15}."
        show y
        y "Would you mind staying up with me just this once?"
        y h "Since you're the captain and all,{w=0.15} you should probably know the process, right?"
        menu:
            "Makes sense":
                y h "Great!"
                pass
        pass

show y h

show r h

r h "Awesome."

show pc s

pc s "I wouldn't have minded doing it."

show y

y "But now you don't have to. {w=0.15}Everyone wins."

show r

r "Seriously,{w=0.15} get some sleep and enjoy it."

show pc s

pc s "Right.{w=0.15}.{w=0.15}. "

e "Nema looks warily at you."

show r h

r h "Think of it this way, now you can be rested the next morning, and help cover for the captain while he makes up for his long night."

e "Nema nods, she seems satisfied."

e "There is a moment of silence."

show y

y "Well...{w=0.15} I'm going to bed."

show r

r "Ditto, see you snaggle babies in the morning.{w=0.15} Just wanted to pop in and say hey."

play sound "sounds/DoorOpen2.ogg"

hide r

pc su ".{w=0.15}.{w=0.15}."

pc "Snaggle babies.{w=0.25}.{w=0.25}.{w=0.25}."

y "Later."

hide y

show pc s:
    linear 0.4 xalign 0.5

play sound "sounds/DoorClose2.ogg"

pc s "Oh, {w=0.15}Okay."

pc "I guess it is pretty late,{w=0.15} isn't it?"

e "Nema seems hesitant to leave."

menu:
    "Hang back for a moment.":
      pass

    "Goodnight.":
        jump day1End
        pass

pc su "Not tired sir?"

menu:
    "I wanted to talk to you.":
      pass

pc h "Of course, what's on your mind?"

menu:
    "What were you saying earlier about your job here?":
      pass

pc h "Oh, yes."

pc "I'm the scientific historian for our journey. "

pc "It's not a core role to the mission, but I will provide quite a lot of value to our home station by charting out new space, and conducting various experiments. "

pc "It's my task to take any information with an ounce of value,{w=0.15} and get that information back to our station."

menu:
    "Sounds valuable to me!":
        pc "Thank you sir."
        pass
    "I see.":
        pass

e "Nema nods slightly and bows"

menu:
    "What do you think about the crew?":
      pass

pc "I... look forward to getting to know them."

pc "I'm a little apprehensive about..."

pc "No,{w=0.15} I'm excited to see what comes of our close proximity."

pc "It will be an interesting experience to say the least."

pc h "I hope to create valuable relationships here."

e "She blushes."

menu:
    "Me too.":
        pc "I'm happy to hear that sir."
        pass

    "Well, we'll see how things go.":
        pc "Yes, surely we will."
        pass
e ".{w=0.15}.{w=0.15}."      

show pc

pc "Well.{w=0.15}.{w=0.15}."

pc "I think I'm going to begin preparing for sleep as well."

pc h "I look forward to working together,{w=0.15} Sir."

menu:
    "It will be interesting.":
        show pc
        pc "I believe it will sir."
        pass
    "Me too.":
        pass

show pc

pc "Well..."

label day1End:

pc "Goodnight,{w=0.15} Captain."

stop music fadeout 5

play sound "sounds/DoorOpen2.ogg"

hide pc

e "Nema walks out into the hallway."

menu:
    "Might as well head to bed as well.":
        pass
        
play music "music/Space.ogg" fadein 2.0

call hall from _call_hall_1

play sound "sounds/DoorClose2.ogg"

e "You walk out into the hallway and see all of the doors shut."

e "The ship is silent."

play sound "sounds/DoorOpen2.ogg"

call blueRoom from _call_blueRoom

e "You enter your room and head straight for your bed."

play sound "sounds/DoorClose2.ogg"

e "As soon as you lay your head down on the pillow, you feel yourself dozing off."

window hide

show black
with fade

e "..."

window hide

return