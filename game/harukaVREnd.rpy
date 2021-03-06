label HarukaEnd: #############################################
    
show y
y h "Hah, {w= 0.15}I knew you had a mind of your own."

y n "I appreciate your fight Nema,{w= 0.15} but I think you'll come around on the idea."

y h "We don't have to live the rest of our lives for some people we'll never meet."

y h "We can experience something new and look past the edge of th-"

show p da

play music "music/Unbelivable.ogg" fadein 1.0

e "Nema's eyes go dark."

show p he

$ renpy.pause(0.2)

show p he:
    linear 0.1 xalign 0.5 ypos 1.99

e "She starts to look a bit like Hei for a moment, then falls to the floor."

e "You reach down to check her pulse,{w= 0.15}but she's freezing cold."

hide p

show y:
    linear 0.5 xalign 0.5 yalign 1.0

y h "About time."

menu:
    "What?":
        pass

    "You did this?":
        pass

y n "I was worried we were gonna run out of time."


y h "The game normally ends around this point anyways."

menu:
    "Game?":
        pass

    "Ends?":
        pass

y h "Yeah,{w= 0.15} and none of the endings have really made any sense so far."

y n "Gotta admit,{w= 0.15} I still don't get it,{w= 0.15} but I don't mind this one."

y m "Wait."

y n "You do remember the other endings you've gotten,{w= 0.15} don't you?"

menu:
    "No.{w=0.15}.{w=0.15}.":
        pass

    "Yes.":
        e"Then you already get it,{w= 0.15} right?"
        jump unplugvr
        pass

y n "Ooooh,{w= 0.15} alright."

y h "That explains it then."

y n "I must have turned off prior memories."

menu:
    "Pior memories?":
        y su "Pior?{w= 0.15} You mean prior?"
        pass

    "What ate you saying?":
        y su "What ate I saying?"
        pass

y s "Oh geez,{w= 0.15} I think things are getting unstable."

y n "I don't think I've seen spelling errors before."

label unplugvr:
    
stop music fadeout 3

y n "Let's unplug you, {w= 0.15}yeah?"

window hide
show tWhite
with hpunch
show black
call blueRoom from _call_blueRoom_19
play music "music/RelaxTalk.ogg" fadein 5.0
$ renpy.pause(1)
hide black
window hide
hide tWhite
with fade

e "You're in your room."

menu:
    "What's happening?":
        pass

y n "Don't you remember?"

y n "You plugged into the training module I was working on."

menu:
    "How long have we been on this ship?":
        y n "Maybe three weeks?"
        pass

    "What's that?":
        y h "You don't remember seeing it?"
        y s "Did I forget to restore that memory?"
        y m "Hmm.{w= 0.15}.{w= 0.15}."
        y n "Anyways,{w= 0.15} you've been under for a good week or two."
        pass

y h "Yeah,{w= 0.15} turns out Nema and Hei were up to some weird shit."

y n "Nema melted or something a few days ago and Hei just disappeared."

menu:
    "Why?":
        pass

y h "Hei I'm not sure about."

y n "Actually.{w= 0.15}.{w= 0.15}. Nema I'm not sure about either."

y n "We started to do double compounds each week and she kinda lost it a bit."

y s "She mentioned something about swapping for our souls?"

y h "I think she just kinda lost it a bit."

y m "The whole thing was pretty upsetting,{w= 0.15} let me tell ya."

y s "It was a slow decline from there."

y n "But regardless of why,{w= 0.15} the fact remains."

y h "It's just you and me now."

menu:
    "You seem happy about that.":
        pass

y h "I am."

y n "I've decided to relax a bit."

y s "And,{w= 0.15} well.{w= 0.15}.{w= 0.15}."

y n ".{w= 0.15}.{w= 0.15}."

show y h

e "Haruka goes flush."

y h "I'm happy it's with you."

e "She smiles down at you."

y n "So.{w= 0.15}.{w= 0.15}."

y h "You want a drink?"

window hide
show black

$ renpy.pause(5)

jump END