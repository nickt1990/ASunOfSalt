label day8:

play sound "sounds/Knock.mp3"

e "There's a knock at your door."

window hide
hide black
with fade

menu:
    "Hello?":
        pass

    ".{w=0.15}.{w=0.15}.":
        pass

play sound "sounds/DoorOpen2.mp3"

show p s

p s "Captain, {w=0.15}may I speak with you?"

menu:
    "Sure.":
        p s "Sir I just wanted to apologize for last night."
        pass

    "About last night?":
        p s "Yes.{w=0.15}.{w=0.15}."
        pass



p s "Hei told me how I was acting and I.{w=0.15}.{w=0.15}.{w=0.15} There's just no excuse sir."

p s "I apologize."

menu:
    "No worries.":
        p s "B-.{w=0.15}.{w=0.15}."
        pass

    "Try to not do that again. You know how Haruka gets.":
        pass

p n "Of course sir."

p s "I've made breakfast in the kitchen if you're interested sir.{w=0.15} We'll be waiting."

hide p

e "Nema leaves."

menu:
    "Get up and move to kitchen.":
        pass

play sound "sounds/DoorClose2.mp3"

call kitchen from _call_kitchen_2

e "Nema and Hei are standing at the counter joking."

e "Haru is at the table."

show y h:
    linear 0 xalign 0.1 yalign 1.0

y h "Hey Cap!"

show r h:
    linear 0 xalign 0.5 yalign 1.0
    
show p h:
    linear 0 xalign 0.9 yalign 1.0

r h "Mornin' dude."

r h "Ready to fill that tummy."

e "Nema giggles."

menu:
    "Oh yeah.":
        pass

    "Uh.":
        pass

r n "Well.{w=0.15} I think we should do something about that, {w=0.15}don't you?"

show p h

p h "Hehe, {w=0.15}oh, {w=0.15}most definitely! "

show r n

r n "But.{w=0.15}.{w=0.15}."

show p su

p su "But what?!"

show r n

r n "You thinking what I'm thinking?"

show p s

p s "Oh. {w=0.15}Uhm."

p n "I hope that you're thinking pancak-"

show r h

r h "PANCAKES!"

e "Both of them laugh."

show y s

y s "They've been like this all morning."

y m "Kill me."

show r n

r n "Here you are, {w=0.15}the \"kill me\" deluxe for the lady."

show p h

p h "Hehe."

show r n

r n "And the tummy filler for.{w=0.15}.{w=0.15}. "

r s "Who had the tummy filler?"

show p h

p h "The captain did!"

show r h

r h "Right, {w=0.15}the captain! Tummy filler for sir Capitol."

menu:
    "Thank you?":
        pass

    ".{w=0.15}.{w=0.15}.":
        pass

e "Hei and Nema share a plate."

r n "So Mr. Boss, {w=0.15}what's the plan for today?"

show y n

y n "Actually, {w=0.15}today I'm going to be giving you all a briefing on how to compound the engine."

y s "I should have did it from the start, {w=0.15}but better late than never I guess."

show p h

p h "That sounds great Haruka, {w=0.15}I can't wait."

show r s

r s "Seriously?{w=0.15} That sounds like the worst."

show p h

p h "Oh Hei."

e "Nema smiles."

show y m

y m "Dear god."

show r su

r su "What."

show y m

y m "It's sickening.{w=0.15} Just being near you."

y s "Just get on with it already and bang, {w=0.15}we can wait."

show p h

p h "Hehe"

show r h

r h "Too late?"

show y su

y su "Woah, {w=0.15}what?"

y n "Are you serious?"

e "Hei smiles sheepishly."

y m "Hei she was drunk, {w=0.15}you disgu-"

show r h

r h "No, {w=0.15}this morning."

show y su

y su "This morning?"

y m "Nema.{w=0.15}.{w=0.15}.{w=0.15} what the hell."

show p su

p su "W-{w=0.15}what?"

show y m

y m "Do you have absolutely no self-respect?"

show p su

p su "Self re-{w=0.15}.{w=0.15}.{w=0.15}. what?"

show y m

y m "It's great to know you two can't do {i}ANYTHING{/i} on your own other than screw this loser."

y m "We're doomed. {w=0.15}This mission was DOA.{w=0.25} What am I even doing trying so hard."

show r su

r su "Uh, {w=0.15}what?"

show p su

p su "H-haruka.{w=0.15}.{w=0.15}.{w=0.15} it's not a big deal, {w=0.15}we were just having fun."

show y su

y su "Having fun?{w=0.15} You're sick."

y m "If you don't value your body nobody else will, {w=0.15}I just- I just can't believe it."

show r su

r su "Woah, {w=0.15}where's this comin' from? Lay off her man."

show y m

y m "Oh fuck you, {w=0.15}you've never thought of another person in your life, {w=0.15}don't pretend like ya have her best interest in mind."

show r su

r su "Captain?"

menu:
    "Haruka lay off a little bit.":
        pass

    "She can say what she wants.":
        pass

show y n

y n "Whatever, {w=0.15}I'm done. "

y m "Thanks for the pancakes."

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka walks out of the room."

show p s

p s ".{w=0.15}.{w=0.15}."

show r s

r s ".{w=0.15}.{w=0.15}."

e "She pops her head back in the door."

show y m:
    linear 0 xalign -0.1 yalign 1.0

y m "And we're still having our goddamn meeting later. "

play sound "sounds/DoorClose2.mp3"

hide y

e "Nema and Hei sit in silence as the door closes again and Haruka disappears."

show r m

r m "Shit, {w=0.15}what was her problem."

menu:
    "Jealous.":
        r su "Jealous?"

        r su "You think so?"

        r n "I am a pretty buff daddy.{w=0.15}.{w=0.15}."

        show p su

        p su "Buff daddy?"

        show r h

        r h "Yeah babe, {w=0.15}it's slang for cool guy."

        show p h

        p h "Buff daddy.{w=0.15}.{w=0.15}."

        e "Nema smiles."
        pass

    "Stressed.":
        r s "Yeah,{w=0.15} I guess she does always seem busy."
        pass

show r s

r s "I should probably go talk to Haruka, {w=0.15}huh Heli-Capter?"

menu:
    "Yes.":
        r n "Alright, {w=0.15}I'll give it a shot."
        pass

    "No.":
        r h "Going to anyways!"
        pass

r h "Wish me luck!"

show p h

p h "Good luck."

e "They smile warmly at one another."

e "Hei leaves"

hide r

p s "I hope.{w=0.15}.{w=0.15}. {w} I hope he sorts things out."

menu:
    "Why?":
        p n "Why?{w=0.15} I want us all to be happy. "
        pass

    "Me too.":
        p h "Exactly."
        pass

p n "This is our life now."

menu:
    "Don't you like Hei?":
        pass

p n "Oh, {w=0.15}yes.{w=0.25} He's a great friend."

p h "That's why I want him and Haruka to get along."

p s "When they fight, {w=0.15}they make their feelings a public thing."

p s "It brings the mood of everyone down, {w=0.15}I feel."

menu:
    "That's true.":
        pass

    "That's putting it lightly.":
        pass

p n "That's the kind of people they are."

p h "I bet they could make good friends."

menu:
    "Maybe.":
        pass

    "I doubt that.":
        pass

p h "No, {w=0.15}I'm sure of it."

p n "They're both so passionate. "

p n "How could things not work out?"

menu:
    "That seems to be working against them.":
        p h "For now."

        p n "I believe that will change."
        pass

    "I guess.":
        pass

e "Hei enters."

play sound "sounds/DoorClose2.mp3"

show r s

r s "It didn't work."

show p s

p s "I'm sorry Hei.{w=0.15}.{w=0.15}."

show r h

r h "It's cool, {w=0.15}I didn't expect much."

menu:
    "What did you say?":
        pass

show p su

p su "Yeah, {w=0.15}what did you say to her?"

show r n

r n "Just the truth."

r s "I said to her, {w=0.15}I said, {w=0.15}\"Haruka.{w=0.15}.{w=0.15}.\""

r n "\"I know you're worried darlin'{w=0.15}.{w=0.15}.{w=0.15}.\""

r s "\"And I know you're hungry{w=0.15}.{w=0.15}.{w=0.15}.\""

show p s

p s "Oh Hei.{w=0.15}.{w=0.15}."

show r n

r n "\"But don't worry{w=0.15}.{w=0.15}.{w=0.15}.\""

r n "\"This meal feeds two.\""

menu:
    "And that didn't work?":
        pass

    "At least you.{w=0.15}.{w=0.15}.{w=0.15} tried?":
        pass

r h "Weird, {w=0.15}right?"

r n "I'm not totally convinced she heard me,{w=0.15} but whatever.{w=0.15} She'll get over it."

r h "Anyways I'm gonna go play some games until dinner, {w=0.15}you wanna come Nebs?"

show p h

p h "O-{w=0.15}of course I'd like to!"

e "Nema smiles again."

p n "I look forward to seeing you at the meeting Captain."

show r h

r h "Cya dude."

hide r

hide p

e "The two of them walk out of the room."

play sound "sounds/DoorClose2.mp3"

e "You have some free time."

define day8Hei = True

define day8Haru = True

label day8Free:
    
call hall from _call_hall_5

menu:
    "Haruka's Room" if day8Haru:
        $ day8Haru = False
        call yellowRoom from _call_yellowRoom
        pass
    "Hei's Room" if day8Hei:
        $ day8Hei = False        
        call redRoom from _call_redRoom
        e "In Hei's room, {w=0.15}he and Nema are just playing games."
        e "The don't acknowledge you."
        jump day8Free
    "Go back to your room" if day8Haru == False and day8Hei == False:
        call blueRoom from _call_blueRoom_2
        jump day8AfterFree

show y h

y h "Oh, {w=0.15}hey Cap."

y n "Whatsup?"

menu:
    "Came to check on you.":
        pass

    "Just saying hi.":
        pass

y n "Yeah I figured."

y m "I'm not apologizing."

y n "It's not my fault that I'm the only one here with standards."

y m "Seriously, {w=0.15}am I imagining it, {w=0.15}or am I the only one who gives a shit?"

menu:
    "They're adults, {w=0.15}they can do what they want.":
        pass

    "No, {w=0.15}the others are pretty lax.":
        pass

y s "Well duh. Thanks Captain, {w=0.15}gee."

y n "Of course they can."

y n "I just wish that they cared about quality in any part of their lives."

y m "Or having some semblance of respect for themselves, {w=0.15}or anyone around them."

menu:
    "Are you jealous?":
        pass

    "Is this really about self-respect?":
        pass

y n "Jealous of those idiots?"

y m "I thought I'd be surrounded by greats on this mission, {w=0.15}y'know?"

y m "I thought I'd be among people who worked hard and gave a shit like me, {w=0.15}so I wouldn't have to be the bad guy all the time."

y s "I'm sick of being the odd one out, {w=0.15}and I'm tired of always feeling like an asshole."

y m "I want everyone to be the best they can, {w=0.15}and I refuse to hide it."

y m "It's not fair that all it gets me is hated."

menu:
    "Maybe you can try being a bit more gentle?":
        pass

    "Don't hide how you feel, {w=0.15}I get it.":
        pass

y n "Cap I kind of want to be alone, {w=0.15}thanks."

y s "I know you mean well, {w=0.15}but.{w=0.15}.{w=0.15}. please?"

menu:
    "No problem.":
        pass

    "No.":
        pass

y s "Thank you."

hide y s

call hall from _call_hall_6

e "You walk out into the empty hallway."

jump day8Free

label day8AfterFree:

menu:
    "I guess I can get some work done now?":
        pass

call blueRoom
e "You go back to your room and get on the computer."

label summariesD8:

menu:#computer
    "I'll read the summaries.":
        menu:
            "Haruka's summary.":
                call day8HaruS
                jump summariesD8
                pass
            "Hei's summary.":
                call day8HeiS
                jump summariesD8
                pass
            "Nema's summary.":
                call day8NemaS
                jump summariesD8
                pass
            "I think I'm done.":
                jump day8Mid
                pass                
        pass

    "I'm going to respect their privacy.":
        jump day8Mid
        pass

label day8Mid:

e "Time has passed."

play sound "sounds/Knock.mp3"

e "There's a knock on your door."

play sound "sounds/DoorOpen2.mp3"

call hall from _call_hall_7

show y

y s "Time for the thing, {w=0.15}c'mon."

play sound "sounds/DoorClose2.mp3"

menu:
    "Yes ma'am.":
        pass
        
call navRoom from _call_navRoom_1

e "You head into into the navigation room together."

show y n:
    linear 0.5 xalign 0.1 yalign 1.0

show p n:
    linear 0 xalign 0.5 yalign 1.0

p n "Hello sir."

show r n:
    linear 0 xalign 0.9 yalign 1.0

r n "Yo."

menu:
    "Hello.":
        pass

    "Yo.":
        pass

show y s

y s "Alright, {w=0.15}I'm just going to get through this. "

y n "Everyone open up the MonEn.exe program on your station."

y n "Now look at the red bar. "

y n "That's the missing info.{w=0.15} Our sensors aren't perfect and this shows how imperfect."

y n "Now green bar. "

y n "That's the stability."

y n "You want that to be above 2c's. "

y n "That's give or take the missing information, {w=0.15}which could go either way."

y s "So you-{w=0.15} Hei."

y n ".{w=0.15}.{w=0.15}."

y m "{size=+4}HEI.{/size}"

show r su

r su "Oh, {w=0.15}yeah?"

show y m

y m "Are you paying attention?"

show r s

r s "Uh.{w=0.25} Yeah."

show y m

y m "Ya better be."

y n "Now finally, {w=0.15}the last bar is the transfer rate."

y n "You want this to mostly be stable, {w=0.15}between 2 and 4 C's."

y n "If anything goes out of range, {w=0.15}then you can type in the emergency code that applies and it will walk you through steps to remedy the problem, {w=0.15}or you can come get me."

y n "The codes are all in an email I sent you on our first or second day."

y n "Really as long as you know that, {w=0.15}you'll be fine in nine out of ten situations."

y n "The most important bar to watch is green."

show r n

r n "What's the green bar do?"

show y su

y su "What?"

show r n

r n "Actually what do all the bars stand for? {w=0.15}There's no words on this screen."

show y m

y m ".{w=0.15}.{w=0.15}."

y m "Hei."

y m "You have got to be the most incompetent person I have ever met."

show r h

r h "Hah, {w=0.15}well, {w=0.15}gee."

show y m

y m "No, {w=0.15}I mean it."

y m "I worked my ass off my entire life-"

show y s

y s "and threw my life away to go on this mission.{w=0.15}.{w=0.15}."

show r su

r su "Hey hold on I wa-"

show y m

y m "Was to get away from the sort of ignorant, {w=0.15}drunk, {w=0.15}filth that I grew up surrounded by."

y s "I thought I'd be among brilliant minds."

y s "I thought I wouldn't have to be the one babysitting for once."

y m "But here I am surrounded by the same filth."

show p su

p su "H-{w=0.15}haruka, {w=0.15}tha-{w=0.15}that's not fair.{w=0.15}.{w=0.15}."

p s "We're not p-"

show y m

y m "It's not fair, {w=0.15}NOTHING is."

y s "That's my point."

y m "I'm sick of working myself to death, {w=0.15}being the odd one out because I care about doing something with my life."

y s "I want a friend, {w=0.15}Nema."

y s "I want to relax for one day."

y m "I want to close my eyes and know that one other person out there has my back."

y s ".{w=0.15}.{w=0.15}."

y s "Not in this lifetime."

y m "What a goddamn joke this all turned out to be."

y m "I threw {b}EVERYTHING{/b} away for this."

y m "Screw this and fuck you."

play sound "sounds/DoorOpen2.mp3"

hide y

e "Haruka walks away."

show r su

r su "Geesh."

r n "Somebody's in a bad mood lately."

show p m

p m "Hei!{w=0.15} You should have paid attention!"

show r su

r su "I did, {w=0.15}I was just joshin'."

menu:
    "Probably a bad move.":
        pass

r m "Well duh, {w=0.15}I see that now dude."

r n "Still, {w=0.15}wasn't that sort of an overreaction? I mean c'mon."

show p s

p s "I cannot say I'd have responded the same, {w=0.15}but she has seemed to be a bit irritable lately."

show r n

r n "Should I go apologize?"

show p s

p s "I'm sorry Hei, {w=0.15}but I'm not sure that would help right now."

p n "Perhaps if Captain went to see her?"

menu:
    "Not a good idea.":
        r n "Well, {w=0.15}you know best man."
        pass

    "Alright.":
        p su "Uhm,{w=0.15} Hei."
        p n "Maybe give her some time."
        r su "You think so?"
        r s "I guess I can do that{w=0.15}.{w=0.15}.{w=0.15}."
        pass

show r n

r s "If we're done here though, {w=0.15}I think I'm gonna go snooze."

show p s

p s "Given the circumstances that might be the best thing for all of us."

menu:
    "Goodnight you two.":
        pass

p s "Goodnight Captain."

play sound "sounds/DoorClose2.mp3"

hide p

hide r

e "Hei and Nema walk off to their individual rooms."

call hall from _call_hall_8

play sound "sounds/DoorOpen2.mp3"

e "You make your way back to yours as well."

call blueRoom from _call_blueRoom_3

play sound "sounds/DoorClose2.mp3"

e "You lay down on your bed."

window hide
show black
with fade

e ".{w=0.15}.{w=0.15}.{w=0.15}"

return