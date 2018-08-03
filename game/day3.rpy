﻿#todo check all music is implemented
#todo add demon to later day

#todo ending idea
# ~DONE in d2n~ haruka mentions that motokami was world renown for his crossdimensional ideas 
# ~~ Nema is still nema at the end, it takes a human to trade places with their kind in order for them to move over to this world. Motokami gave them placeholder bodies but they aren't completely here, causing ripples in dimension -the demon
# ~~ Nema can be persuaded to stay if shes happy as things are with haruka
# ~~ Hei is also a being from other dimension
# ~~ plan was that you trade with hei, nema with haruka.
# ~~ everyone on the ship but you knows motokami
# ~~ ending revolves around if you're sacrificed to the other dimension or not so that hei and nema can come into our world as whole										  

label day3:

e ".{w=0.25}.{w=0.25}."

play music "music/MorningAlarm.ogg" fadein 3.0

window hide
hide black 
with fade

e "You wake up to see a notification on your computer screen."

play music "music/RelaxTalk.ogg" fadein 3.0

e "It appears that the Satori sensors are live."

window hide
show black 
with fade

menu:#computer
    "I should read the summaries.":
        label summariesD3:
        menu:
            "Haruka's summary.":
                call day3HaruS
                jump summariesD3
                pass
            "Hei's summary.":
                call day3HeiS
                jump summariesD3
                pass
            "Nema's summary.":
                call day3NemaS
                jump summariesD3
                pass
            "I think I'm done.":
                jump day3Start
                pass                
        pass

    "I'm going to respect their privacy.":
        jump day3Start
        pass

label day3Start:#DAY3START!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
window hide
hide black 
with fade

e "You decide to head out to see what the others are doing."

play sound "sounds/DoorOpen2.ogg"

call hall from _call_hall_29

e "You step out into the hallway.{w=0.15} Haruka is laying on the floor covered by a blanket.{w=0.15} Her eyes are closed."

menu:
    "Haruka?":
        pass

    "Are you a sleepwalker?":
        pass

show y h

y h "Oh, {w=0.15}hey Cap.{w=0.15} How you feeling after the late night?"

menu:
    "Excellent!":
        y h "There he is, {w=0.15}what a champ."
        pass

    "Terrible!":
        y h "Hah, boo hoo,{w=0.15} you'll live."
        pass

menu:
    "What are you doing?":
        pass

y n "Layin' on the heater."

y h "It feels good, {w=0.15}so warm."

y n "It's easy to just zone out and relax."

menu:
    "Thinking time?":
        y n "Yeah, {w=0.15}I s'pose."
        pass

    "In the hall?":
        y h "Sure, why not?"
        pass

play sound "sounds/DoorOpen2.ogg"

e "Hei walks out of his room."

play sound "sounds/DoorClose2.ogg"

show r h:
    linear 0 xalign 0.9

r h "Peeps."

show y n

y n "Loser."

show r s

r s "Why so hostile my pristine lemon cake?"

show y n

y n "No reason, {w=0.15}my garbage pile of a crewmate."

show r h

r h "Oooh. Sour like a lemon."

show y n

y n "You know it."

show r n

r n ".{w=0.15}.{w=0.15}."

r n "Yet."

e "Hei gazes at Haru."

r n "{size=-6}Sweet,{w=0.3} like a cake.{/size}"

show y m

y m "How are you our weapons expert?"

show r n

r n "I was the only one that applied."

show y m

y m "You're kidding."

show r h

r h "PSYCH."
     
r  "I'm the best, {w=0.15}put the rest of the applicants to SHAME! I'm smart as hell dude, {w=0.15}seriously."

show y n

y n "OK, {w=0.15}thank's for clearin' that up."

show r n

r n "You'll see. You'll be all over big daddy he-"

show y m

y m "Don't finish that sentence."

y m "I'll see you at breakfast. Go."

show r h

r h "But I'm just trying to get to know my brand new ship buds. "

menu:
    "Cool it.":
        r m "Fine fine, {w=0.15}geez, {w=0.15}I was just joshin' sir."
        e "Haruka shoots you a little smile as Hei walks away grumbling."
        hide r m
        pass

    "...":
        y m "Hei,{w=0.15} I said {b}STOP{/b}."
        r su "Woah hey,{w=0.15} alright."
        r s "I was just kidding,{w=0.15} geez."
        hide r s
        e "Hei turns and starts to walk away, mumbling to himself."
        pass

show y h

y h "Cap."

e "There's a hint of a smile on her face."

y n "I'm gonna use my newfound quiet for a bit of a nap."

y h "I'll see you at breakfast, {w=0.15}right Cappo?"

menu:
    "Of course.":
        pass

    "No.":
        pass

y n "See ya then."

hide y n

define heiD3 = True
define nemaD3 = True

label day3Menu:
call hall

menu:#MENU###################################################
    "Hei's Room" if heiD3:
        $ heiD3 = False
        jump heiRoomD3
        pass
    "Nema's Room" if nemaD3:
        $ nemaD3 = False
        jump nemaRoomD3
        pass
    "Kichen (Continues Story)":
        jump day3Kitchen
        pass

label heiRoomD3:
call redRoom from _call_redRoom_5

show r h

menu:
    "Morning.":
        pass

    "You're up early.":
        pass

show r h

r h "Heya Captain Crunk Incorporated."

r n "I actually have something I want your captain-{w=0.15}ly advice on."

menu:
    "What?":
        pass

r n "This is man to man right?"

r n "Just between us?"

menu:
    "Sure":
        r s "Alright.{w=0.15}.{w=0.15}.{w=0.15} so.{w=0.15}.{w=0.15}."
        pass

    "No promises.":
        r m "Fine."
        r n "Still.{w=0.15}.{w=0.15}."
        pass

r n "I've been having problems with one of the ship's ladies."

menu:
    "Haruka?":
        r h "How'd you guess?"
        e "There was heavy sarcasm in his voice."
        pass

    "Nema?":
        r m "You know it's not dude."
        r su "Haruka!"
        pass

r s "She's ridiculously mean to me for no real reason man."

r n "I try to keep things lighthearted but she snaps at me the second I come into sight."

r s "Does she really hate me as much as she acts like she does?"

r s "I know I can be a bit annoying but I just be kiddin'."

r n "She sees that right?"

menu:
    "No telling.":
        pass

    "I'm sure she does.":
        pass

r m "Well what the hell."

r s "I just don't get it man."

r n "You've barely said three words to her and she's all over ya."

r s "I crack these hilarious jokes and she doesn't even smile."

r s "Forget smiling, {w=0.15}she hates my jokes."

r s "And me."

r n "I don't get it."

menu:
    "She seems to like leadership.":
        r n "Yeah, {w=0.15}I can't disagree there."

        r s "But I mean"

        r n "I'm sort of a leader in a way."
        pass

    "She seems to hate laziness.":
        r su "Lazy?"
        r m "I don't have a lazy bone in my friggen body dude."
        pass

r n "I built every ounce of weapons technology on this ship."

r h "I was a professional yo-yo artist before I even hit 20."

menu:
    "...":
        pass

    "Artist?":
        pass

r n "I played piano in the section one-nine-six orchestra for three years, {w=0.15}I was youngest in the whole place!"

r m "I lead myself into that stuff."

r n "Well."

r s "My parents forced me into it. But I worked hard."

r s "Whatever.{w=0.15} She'll hate me forever and the rest of my life will be miserable."

r s "I am a cardboard box in the rain.{w=0.15} Melting like ice cream on a summer's evening."

r n "I was also the first person under 50 to be featured in my parents monthly poem compendium."

r n "It may not be seeable, {w=0.15}but I'm pretty boss when it comes to words and sentences in an artistic way."

menu:
    "I'm sold.":
        pass

    "You sure?":
        pass

r n "I have a lot to offer.{w=0.15} I do."

r s "Why doesn't she like me more?"

menu:
    "Maybe try to prove your worth?":
        r n "That's it.{w=0.15}.{w=0.15}.{w=0.15} She wants a go-getter."
        pass

    "Why's it so important?":
        r m "Shh,{w=0.15} shut up."
        r n "I got it."
        pass

r h "Thanks bud!{w=0.35} I need to get to work.{w=0.35} Dinner tonight, {w=0.15}prepare your mind to be blown."

e "His eyes have glazed over."

call hall from _call_hall_30

hide r

e "You walk back out into the hallway."

jump day3Menu

label nemaRoomD3:

call pinkRoom from _call_pinkRoom_2

e "Nema is laying on the floor."

menu:
    "Nema?":
        pass

show p s

p sl "Nema."

e "There is drool all over her face.{w=0.15}.{w=0.15}. and the floor. {w=0.15}There's an empty glass bottle in her hand."

menu:
    "Shake her.":
        pass

show p s

e "Her eyes shoot open."

e "She looks like a scared owl."

show p sl

e "Her mouth opens, {w=0.15}then her eyes slowly close."

e "She slowly curls up and closes her eyes."

hide p

jump day3Menu

label day3Kitchen:
        
call kitchen from _call_kitchen_8

play sound "sounds/DoorOpen2.ogg"

e "You walk into the kitchen just ahead of Haruka and Hei."

play sound "sounds/DoorClose2.ogg"

show r su

r su "No Nema?"

menu:
    "We're going to let her catch up on a bit of rest.":
        pass

r n "Oh, {w=0.15}well I'm tired to so I'll catch you guys la-"

show y m:
    linear 0 xalign 0.9

y m "No."

show r su

r su "This trip sucks."

show y m

y m "This isn't a trip, {w=0.15}this is your job."

show r s

r s "Still sucks."

menu:
    "I agree, {w=0.15}boring.":
        r n "See? {w=0.25}Even our {size=-6}{i}suspiciously quiet{/i}{/size} captain thinks so."
        show y m

        y m "Maybe if you both did your jobs then you wouldn't be so bored, {w=0.15}yeah?"
        pass

    "I disagree, {w=0.15}this has been great.":
        y m "I'm sure time goes by a bit faster when you don't just lay around all day."
        r m "Hey, I do my job just fine."
        pass

menu:
    "Speaking of jobs, {w=0.15}what's the agenda for you two today?":
        pass

show r h

r h "Shouldn't you be telling us that?"

show y n

y n "Have you ever served on a ship?"

y n "We're not children and crews aren't run that way anymore.{w=0.15} You can figure out how to be productive. Do your best to keep us alive so the rest of us can work on our research."

show r n

r n "Fine. Today I'll be doing my BEST to keep us alive so the re-"

show y m

y m "Unbelievable."

show r n

r n "I'm not sure what you expected."

menu:
    "What are you doing Haruka?":
        pass

show y n

y n "I'm gonna start testin' on the training pod that was sent with us."

menu:
    "What?":
        pass

y h "Yup, {w=0.15}military grade."

y n "It's gonna be somethin' special. "

menu:
    "But what is it?":
        y h "I'll let that be a lil' surprise for everyone."
        pass

    "It sounds special.":
        pass

#todo setup for ending with testing vr


e "She smirks."

show r n

r n "Is it sexy?"

show y m

y m "What?"

show r n

r n "Like, {w=0.15}is it sexy. Is it cool."

show y n

y n "Hei, {w=0.15}why do you make it so hard to be around you?"

show r m

r m "Whatever."

show r n

e "Everyone eats quietly for a little bit."

e ".{w=0.15}.{w=0.15}."

r h "Bossman, {w=0.15}can you fetch a bottle of soy sauce from the fridge?"

menu:
    "Can you fetch it yourself?":
        r n "Sorry, {w=0.15}may you fetch it for me?"
        pass

    "No problem.":
        y m "Wait."
        pass

show y m

y m "Get it yourself,{w=0.15} jackoff."

show r n

r n "You know."

r s "That hurts a little bit."

r n "I'm not tr-"

show y n

y n "Ugh. I'll get it."

show r su

r su "Uh, {w=0.15}no that's fine."

r su "I'll get it!"

r su "Don't worry about it!"

show y n

y n "I'm already up, {w=0.15}you can continue to be la-"

play sound "sounds/Ketchup.ogg"

#todo low priority new ketchup sound
e "Ketchup squirts out of the fridge when Haru tries to open it."

y su "Is this.{w=0.15}.{w=0.15}.{w=0.15} Ketchup?"

show r s

stop music fadeout 2

r s "Yeah.{w=0.15}.{w=0.15}.{w=0.15} pretty funny right?"

play music "music/BadSituation.ogg" fadein 3.0

show y m

e "Haruka grabs a knife from the counter."

r su "Haruka c'mon, {w=0.15}it wasn't even meant for you! "

e "She turns around and looks at Hei for a moment."

r su "Haruka! I swear I would not have done it if I kn-"

show y m:
    linear .2 xalign 0.89

e "She begins to swiftly walk towards him."

r su "Haruka please, {w=0.15}I'm so sorry I'll clean it up, {w=0.15}I'll never bother you again I swear, {w=0.15}I do"

play sound "sounds/Slash.ogg"
show tRed
with hpunch
$ renpy.pause(0.09)
hide tRed

show r sub

e "The moment she reaches him she lashes her arm out and slices his throat."

r sub "Grgrlgl-{w=0.1}hargh H-g-"

hide r su

play sound "sounds/Thud.ogg"

e "He collapses to the floor."

show y m:
    linear .3 xalign 0.5

y m "I just couldn't do it, {w=0.15}sorry cap."

menu:
    "Holy shit.":
        pass

    "Oh It's cool":
        pass

y n "You know that was for the best. "

y s "He would have been a major annoyance for the rest of our lives."

y s "He would have driven me crazy."

y n "Maybe he did."

menu:
    "No, {w=0.15}this is not OK. ":
        pass

y s "Fine.{w=0.35} I knew what I was doing.{w=0.35} I took a chance. "

y n "I'm not a coward like you."

y s "{size=-6}Coward.{w=0.05}{/size}{nw}"

y c1 "{size=-1}Coward.{w=0.05}{/size}{nw}"

y c2 "{size=+12}Coward.{w=0.05}{/size}{nw}"

y c3 "{size=+27}{b}Coward.{w=0.05}{/b}{/size}{nw}"

hide y

window hide
show black

stop music fadeout 2

play music "music/Space.ogg" fadein 2.0

call hall

e "{w=0.15}.{w=0.15}.{w=0.15}."

show p su
p su "Captain."
hide p

window hide
hide black
with fade

menu:
    "Nema?":
        pass

    "What's going on?":
        pass

e "You find yourself in the hallway all of a sudden."

e "You just barely noticed Nema walking into her open room."

call pinkRoom

stop music fadeout 3

e "You follow just behind her through the door."

play music "music/Evil.ogg" fadein 2.0

show ptBlack

e "The atmosphere seems to change as you enter."

menu:
    "Nema?":
        pass

    "Hello?":
        pass

e "No response."

e "You notice her standing in the corner, facing away from you."

menu:
    "Approach her.":
        pass
        
e "You walk up behind her."

e "Your arm reaches out to touch her shoulder{w=0.35}.{w=0.35}.{w=0.35}."

play sound "sounds/CaptainScare.ogg"

show p ss

$ renpy.pause(0.45)

hide p

window hide
show black
hide ptBlack
e "Suddenly you're in complete darkness."

play sound "sounds/demonspeechd31.ogg"
d "Leviathan ov mine, {w=0.15}stir.{w=0.15}.{w=0.15}."

play sound "sounds/demonspeechd32.ogg"
d "My burning sea. {w=0.15}Rise."

play sound "sounds/demonspeechd33.ogg"
d "I arrive."

play sound "sounds/demonspeechd34.ogg"
d "Blow your horns, {w=0.15}devout.{w=0.15} Announce me."

play sound "sounds/demonspeechd35.ogg"
d "Piles of flesh. "

play sound "sounds/demonspeechd36.ogg"
d "Waves of nothing."

play sound "sounds/demonspeechd37.ogg"
d "Do I make you smile?"

menu:
    "Yes.":#todo endings
        play sound "sounds/demonspeechd38.ogg"
        d "A deal is struck."
        pass
    "No.":
        pass

play sound "sounds/demonspeechd39.ogg"
d "Companion."

play sound "sounds/demonspeechd310.ogg"
d "We shall burn together."

play sound "sounds/demonspeechd312.ogg"
d "We shall be of many skins."

play sound "sounds/demonspeechd313.ogg"
d "We live."

stop music fadeout 3.0

window hide
show black

call kitchen

e "You feel cold wind on your skin."

play music "music/Space.ogg" fadein 2.0
e "{w=0.35}.{w=0.35}.{w=0.35}."

window hide
hide black
with fade
hide ptBlack

e "You fall back into your chair at the dinner table."

show r s

show y m
show y m:
    linear 0 xalign 0.99 #todo she floats

r s "Haruka c'mon, {w=0.15}it wasn't even meant for you! "

show y m:
    linear .2 xalign 0.94

e "She takes another step forward."

r s "Haruka!{w=0.15} I swear I would not have done it if I kn-"

show y m:
    linear .2 xalign 0.89

e "She takes a step forward."

menu:
    "Stop her.":
        y su "What are you doing?"
        e "You look at her hands."
        show y n
        e "She's not holding anything."
        pass

    "Let her go.":
        e "Now, standing right before Hei{w=0.15}.{w=0.15}.{w=0.15}."
        e "She sighs."
        show y n
        y n "Nope."
        pass

show r n

r n "I said I was sorry.{w=0.15}.{w=0.15}."

show y n

y n "I'm not interested. "

show r n

r n "But Haruka.{w=0.15}.{w=0.15}."

show y n

y n "I'm gonna go wash up. "

play sound "sounds/DoorOpen2.ogg"

hide y

e "Haruka leaves the room."

play sound "sounds/DoorClose2.ogg"

show r s

r s "She's not THAT mad right?"

menu:
    "You kidding?":
        pass

    "She'll cool down.":
        pass

r s "I know."

r n "Man.{w=0.15} I could use a beer.{w=0.15}.{w=0.15}.{w=0.15} Could you grab me one from the fridge?"

menu:
    "Absolutely not.":
        pass

r h ".{w=0.15}.{w=0.15}."        

r s "Today sucks.{w=0.15} I'm gonna go to sleep."

r s "See ya man."

play sound "sounds/DoorOpen2.ogg"

hide r

e "You finish eating then walk into the hallway."

call hall from _call_hall_32

define heiRoomD32 = True
define haruRoomD32 = True

label menuD32:
call hall
menu:
    "Hei's Room" if heiRoomD32:
        $ heiRoomD32 = False
        jump heiRoom3
    "Haruka's Room" if haruRoomD32:
        $ haruRoomD32 = False
        jump haruRoom3
    "Work (Continues Story)":
        jump workD3

label haruRoom3:
call yellowRoom from _call_yellowRoom_3

show y m

y m "Can you believe that idiot?"

y h "Cap, {w=0.15}I'm happy you're here."

y n "At least there's one other sane person on this damn ship."

y n "But.{w=0.15}.{w=0.15}."

y n "If you don't mind, {w=0.15}I need to get some work done."

y n "Sorry Cap."

y n "We'll talk later."

hide y n
jump menuD32

label heiRoom3:

call redRoom from _call_redRoom_6

show r s

r s "Dude I really fucked up."

r s "My goal has moved down from her liking me, {w=0.15}to her not hating me."

r s "I hate my life."

r s "Ughhh"

r n "Man I'll see you at dinner.{w=0.15} I need to mope around for a while."

hide r n

jump menuD32

label workD3:

call blueRoom

e "You go to your room and get some work done on the computer."

window hide
show black
with fade

e ".{w=0.35}.{w=0.35}.{w=0.35}"

window hide
hide black
with fade


call hall
play sound "sounds/DoorClose2.ogg"
e "After a while,{w=0.25} you decide to head to the kitchen for dinner."

call kitchen from _call_kitchen_9
play sound "sounds/DoorOpen2.ogg"
e "You enter the kitchen{w=0.15}.{w=0.15}.{w=0.15}."

e "Only Nema is here."

show p h

p h "Hello Captain!"

menu:
    "Nema, {w=0.15}how are you feeling?":
        p h "I'm feeling great, {w=0.15}thank you for your leniency today sir. "
        
        menu:
            "Of course.":
                pass

            "Good.":
                pass
        pass

    "Finally up?":
        p h "Yes sir,{w=0.15} I apologize."
        p n "I had to catch up on a little sleep."
        pass

e "Hei walks in"

show r h:
    linear 0 xalign .9

r h "Hey Chicklet.{w=0.35} Feeling better?"

e "Nema chuckles."

show p h

p h "Yes Hei, {w=0.15}thank you for your concern."

show r n

r n "No prob."

r h "So, {w=0.15}what we having for dinner?"

r n "You know, {w=0.15}I was sort of thinking that steak sounded good."

r n "Nema, {w=0.15}do you know how to mak-"

e "Haruka walks through the still open door."

play sound "sounds/DoorClose2.ogg"

show y n:
    linear 0 xalign .1

y n "Cap."

menu:
    "Hello.":
        pass

    "Ay":
        pass

e "Haruka glares at Hei."

show p h

p h "Good evening Haruka, {w=0.15}how has your day been?"

show y n

y n "My day's been interesting."

show p su

p su "Why is that? Some excitement this morning or perh-"

show y n

y n "Hei, {w=0.15}why has my day been interesting?"

show r n

r n "W-{w=0.15}well.{w=0.15}.{w=0.15}."

r h "Today you worked on a new training device, {w=0.15}and we're all just so excited b-"

e "Haruka's glare intensified. "

r s "Uh, {w=0.15}h-{w=0.15}heh.{w=0.35} Sorry.{w=0.35} Again."

show y n

y n "Don't do that again."

show r n

r n "Never!"

show y n

y n "Alright.{w=0.15}.{w=0.15}.{w=0.15} Forgiven."

show r su

r su "Wait, {w=0.15}really?"

show y n

y n "I'm stuck with ya, {w=0.15}aren't I?"
     
y n "Why not."

show r h

r h "Thanks babe, {w=0.15}I rea-"

show y n

y n "Stop while you're ahead."

show p h

p h "Hah."

p n "Oh.{w=0.15}.{w=0.15}.{w=0.15} so uhm.{w=0.15}.{w=0.15}.{w=0.15} should I make food?"

show y su

y su "You can cook?"

show p n

p n "Well.{w=0.15}.{w=0.15}.{w=0.15} y-yes.{w=0.15} I thought I mentioned that yesterday, {w=0.15}my apologies. My parents were bo-"

show y h

y h "Great! Lookin' forward to it."

show p n

p n "Oh! It will be great, {w=0.15}I promise! You'll love it!"

show y n

y n "Alright."

show p su

p su "Y-.{w=0.15}.{w=0.15}.{w=0.15}."

e "Nema looks nervous."

p n "Uhm.{w=0.15}.{w=0.15}."

show r n

r n "What's up Nems?"

show p s

p s "Well.{w=0.15}.{w=0.15}.{w=0.15} How would you guys like to play a game today after dinner?"

show r h

r h "Hell yeah! What kind of game?"

r n "Maybe a fighting game? "

r n "I can bring out my Game Slab X."

show y n

y n "If we're going to play a game, {w=0.15}how about we play somethin' that's you know."

y n "Not that."

show r s

r s "Man, {w=0.15}you really know how to hurt a guy."

show p n

p n "Well I was thinking"

show y n

y n "Yeah?"

show p n

p n "Maybe we could play a game to get to know each other better?"

show y n

y n "Twenty questions then."

show p h

p h "Sure! Yes, {w=0.15}that sounds fine, {w=0.15}thank you Haruka."

show r m

r m "You can't even win 20 questions."

menu:
    "You're right.":
        pass

    "You win by learning about each other!":
        pass

r m "Bah!"

show y n

y n "Eloquent. "

show r n

r n "Fine, {w=0.15}whatever. What's your favorite color?"

show y n

y n "Ugh."

y n "We'll eat and then we can think about the game."

show r n

r n "Speaking of eating, {w=0.15}is food ready Nibbles?"

show p h

p h "Nibbles!"

e "Nema smiles."

p n "It is. I'll prepare the plates shortly."

show r h

r h "Damn straaaaaight."

e "Nema doles out the plates."

show y n

y n "Thanks Nematsu."

show r h

r h "Yeah thanks."

menu:
    "Thank you!":
        p h "It was my pleasure everybody!"
        pass

    "Let's eat!":
        pass

show p h

show r h

r h "This food is dope."

show y n

y n "It is pretty good, {w=0.15}nice job."

show p h

p h "R-Really!?{w=0.15} Thank you so much!"

p n "What do you think Captain?"

menu:
    "It's delicious!":
        pass

    "It's not bad.":
        pass

p su "Captain thank you! "

e "Eat in silence."

show r s

r s "Nemo, {w=0.15}ya haven't touched your food. Feelin' alright?"

show p h

p h "Yes! {w=0.15}I'm just so excited!"

show y n

y n "What?"

show p h

p h "You all like my food. "

e "She smiles."

show r h

r h "Awww"

r n "That's adorable."

show y n

y n "C'mon, {w=0.15}just eat up so we can play."

show p n

p n "I'll save it for later, {w=0.15}I'm ready!"

menu:
    "Let's start!":
        pass

show y n

y n "Ok.{w=0.15} Here are the rules."

y n "We go clockwise, {w=0.15}so it'll go me, {w=0.15}Hei, {w=0.15}Nema, {w=0.15}then Caps."

show r n

r n "We're starting with you? I want to start."

show y m

y m "No."

y n "So on your turn, {w=0.15}the other 3 each get to ask you a question, {w=0.15}and you pick one to answer."

show r n

r n "Whoever gets their question picked the most wins."

show y n

y n "No."

y n "And we just do that around the circle. We can call five times around good."

show p h

p h "Haruka, {w=0.15}I've never played the game this way. It sounds interesting."

show y n

y n "Sure. It's how I've always played it."

show r n

r n "So"

show y m

y m "So ask away, {w=0.15}idiot."

show r n

r n "Ok, {w=0.15}uhhhhh."

r n "What age did you have your first kiss?"

show y n

y n "What is this, {w=0.15}middle school?"

show r s

r s "Hey, {w=0.15}don't make fun of my question.{w=0.25 This was your stupid idea for a game."

show y n

y n "Whatever.{w=0.25 Nema what do you have?"

show p n

p n "Haruka, {w=0.15}what is one thing you are very proud of?"

show y n

y n "Alright, {w=0.15}Cap?"

menu:
    "What age did you have your first kiss?":
        pass

    "What is one thing you're very ashamed of?":
        pass

y n "Tryin' to block me in, {w=0.15}eh?"

y h "Well, {w=0.15}I'll pick something I'm proud of."

y n "This ship."

y n "Being here."

y n "I worked my ass off my entire life."

y n "I've never not had to struggle, {w=0.15}y'know?"

r n "Classic from rags to riches. The princess of the stars, {w=0.15}they call her."

y m "It's amazing that you can turn my pride into shame with one sentence."

show r n

r n "Eh."

show y n

y n "Alright, {w=0.15}next. "

show p n

p n "Uhmmm Hei, {w=0.15}it's your turn."

show r h

r h "Nice. Alright, {w=0.15}what do ya got for papa?"

show p h

e "Nema chuckles."

show p n

p n "Hei, {w=0.15}what is your crowning achievement?"

menu:
    "Have you always been bad at video games?":
        pass

    "What is your ideal woman?":
        jump heiNoRealQ        
        pass

show r n

r n "Ask a real question goddamn it."

menu:
    "No.":
        pass

    "What is your ideal woman?":
        jump heiNoRealQ
        pass

r m "I'm going to SMASH you at that rematch. "

r h "You dick."

label heiNoRealQ:

show y n

y n "Why do you try so hard to annoy me?"

show r h

r h "Haruka, {w=0.15}honey, {w=0.15}I never tried to do anything but love you."

r n "Alright, {w=0.15}your turn Captain."

show p h
e "Nema laughs."

show y n

y n "That was your answer?"

show r n

r n "Straight from my heart."

show y n

y n "Fine, {w=0.15}Cap, {w=0.15}you can go."

show r s

r s "Haruka"

menu:
    "Let's do it!":
        pass

show y n

y n "Who is your favorite crewmate?"

show r n

r n "Ohhh, {w=0.15}I like that. Same."

r n "Nema, {w=0.15}pick the same one"

show p s

p s "B-but I'd much rather know his greatest accomplishment to be quite honest."

show y n

y n "What's with you and your hokey questions? You're supposed to dig out their darkest secrets, {w=0.15}not help them write a resume."

show p s

p s "I don't want to make anyone uncomfortable."

show y h

y h "Life is pain. "

y n "Her question is the same.{w=0.15} Answer."

menu:
    "Haruka":
        pass

    "Nema":
        y su "Seriously?"
        p su "Me?"
        p n ".{w=0.15}.{w=0.15}."
        p h "Thank you captain."
        y m "I don't buy it."
        e "Haruka rolls her eyes."
        jump harukaNextTurn
        pass

y h "Shucks Cap, {w=0.15}I knew the answer, {w=0.15}but to hear it makes me smile. What a smooth operator."

show p h

p h "No surprise, {w=0.15}Haruka is very charismatic and strong. "

e "Nema smiles."

show r m

r m "Eh."

e "Haruka glares."

r h "Haha, {w=0.15}you know I joke babe. "

show y n

label harukaNextTurn:
    
y n "Whatever, {w=0.15}back to me. "

show r n

r n "What's your ideal woman? Or man."

show y n

y n "Idiot. Anybody that isn't you."

show r s

r s "Hey, {w=0.15}if you're choosing mine you have to be serious."

show y n

y n "Hmph, {w=0.15}Nema?"

show p n

p n "Oh, {w=0.15}well"

p s "Not hokey right? Uhm"

p n "Could I ask why do you seem to dislike Hei so much?"

show y h

y h "You can, {w=0.15}that's the point of the game."

y n "Cap?"

menu:
    "Same as Nema":
        pass

    "Same as Hei":
        pass

y n "You know what, {w=0.15}why don't I answer 'em all at once?"

y n "The ideal man for me is strong."

y n "Not because I need to be taken care of."

y n "Strong mind, {w=0.15}strong opinions, {w=0.15}strong will. Someone to stand beside me."

y h "I want somebody who puts effort into their life, {w=0.15}y'know?"

y h "Somebody who understands that you need to work hard, {w=0.15}and take control, {w=0.15}or else you're throwing your time away. "

y n "Looks don't matter so much to me. Strength does."

show r n

r n "So what about the other part? About me?"

show y h

y h "I already answered it."

y n "I like strong people, {w=0.15}and you are not one of those."

y m "You're soft, {w=0.15}you bend under the slightest amount of pressure, {w=0.15}ya have no convictions, {w=0.15}you're the place that time goes to die."

show r s

r s "Hey, {w=0.15}that's not true."

show y n

y n "Then prove me wrong. If you were that kind of person I'd see it, {w=0.15}but I don't."

show r n

r n "I have a lot to offer, {w=0.15}I-"

show y n

y n "Well show me. I don't see it."

show r s

r s "That's well"

show y n

y n "That's what I thought."

y m "Do your own thing, {w=0.15}I don't care."

y n "But don't try to force your friendship on me, {w=0.15}please."

y n "I'm not trying to hurt you, {w=0.15}but I wont slow down."

y n "I need to do what I'm passionate about, {w=0.15}and I want to be around passionate people."

y n "When I look at you, {w=0.15}I see a weaker me, {w=0.15}and that puts me on edge."

y su "I don't mean to be so rude to you, {w=0.15}but something about you brings that out in me. I'm sorry, {w=0.15}but that's how it is."

show r s

r s "Oh Ok."

r s "I think I'm done with this game.{w=0.15} Can you let me out Nema."

show p n

p n "Yes, {w=0.15}of course"

show r s

r s "Goodnight."

play sound "sounds/DoorOpen2.ogg"

e "Hei opens the door and walks out of the room."

hide r

show y n

y n "Well, {w=0.15}looks like the game is over."

show p s

p s "Yes, {w=0.15}it does."

p s ""

p s "I'm going to go check on Hei."

p n "Goodnight. It's been nice getting a chance to know you both more."

e "Nema walks out after Hei."

play sound "sounds/DoorClose2.ogg"

hide p

show y n:
    linear 0.5 xalign .5
    
show y s

e "There's a moment of silence between you and Haruka."

y n "You think I was too harsh?"

menu:
    "It's better to be direct.":
        y n "I agree."
        pass

    "You could have been more sensitive.":
        y s "I dunno Cap."
        pass

y n "I honestly don't think he's a bad guy."

y n "I know it doesn't look that way, {w=0.15}but it's true."

y n "But I'd rather he knew exactly how I feel instead of leading him on and hurting him every day."

y s "It didn't feel good to say that, {w=0.15}I know I look like a jerk"

y n "But I think it was the best thing to do."

y h "And I'm happy you agree."

y n "Anyways, {w=0.15}I'm going to take a shower and get to bed."

y s "This has been a shitty night. "

play sound "sounds/DoorOpen2.ogg"

hide y

e "Haruka walks out and goes to bed."

call hall

e "You follow shortly after into the hallway.{w=0.15}.{w=0.15}."

call blueRoom

e "And then turn into your room."

window hide
show black
with fade

e "You fall onto your bed and drift off to sleep."

e ".{w=0.15}.{w=0.15}.{w=0.15}"

return