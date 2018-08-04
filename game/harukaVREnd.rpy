label HarukaEnd: #############################################
    
show y
y h "Hah,{w= 0.15}I knew you had a mind of your own."

y n "I appreciate your fight Nema,{w= 0.15}but I think you'll come around on the idea."

y h "We don't have to live the rest of our lives for some people we'll never meet."

y h "We can experience something new and look past the edge of th-"

e "Nema falls on the floor,{w= 0.15}limp."

e "You reach down to check her pulse,{w= 0.15}but when you bend down you see where her eyes were,{w= 0.15}there are only empty sockets."

y h "About time."

menu:
    "What?":
        pass

    "You did this?":
        pass

y n "I was worried we were gonna run out of time."

#todo go back and foreshadow this
y h "The game normally ends around this point anyways."

menu:
    "Game?":
        pass

    "Ends?":
        pass

y h "Yeah,{w= 0.15}and none of the endings really made any sense."

y n "Gotta admit,{w= 0.15}I still don't get it,{w= 0.15}but I don't mind this one."

y m "Wait."

y n "You do remember the other endings you've gotten,{w= 0.15}don't you?"

menu:
    "No.{w=0.15}.{w=0.15}.":
        pass

    "Yes.":
#todo branch
        pass

y n "Ooooh,{w= 0.15}alright."

y h "That explains it then."

y n "I must have turned off prior memories."

menu:
    "Prior memories?":
        pass

    "What do you mean?":
        pass

y s "Oh geez,{w= 0.15}I think things are getting unstable."

y n "I don't think I've seen spelling errors before."

y n "Let's unplug you,{w= 0.15}yeah?"

e "The screen flickers."

e "You're in your room."

menu:
    "What's happening?":
        pass

y n "Don't you remember?"

y n "You plugged into the training module I was working on."

menu:
    "How long have we been on this ship?":
        pass

    "What's that?":
#todo branch
        pass

y n "Maybe three weeks?"

y h "Yeah,{w= 0.15}turns out Nema and Hei were up to some weird shit."

y n "Nema melted or something a few days ago and Hei just disappeared."

menu:
    "Why?":
        pass

y h "Hei I'm not sure about."

y n "Actually.{w= 0.15}.{w= 0.15}. Nema I'm not sure about either."

y n "We started to do double compounds each week and she kinda lost it a bit."

y s "It was a slow decline from there."

y n "But regardless of why,{w= 0.15}the fact remains."

y h "It's just you and me now."

menu:
    "You seem happy about that.":
        pass

y h "I am."

y n "I've decided to relax a bit."

y s "And,{w= 0.15}uh.{w= 0.15}.{w= 0.15}."

y n ".{w= 0.15}.{w= 0.15}."

show y h

e "Haruka goes flush."

y h "I'm happy it's with you."

e "She smiles down at you."

y n "So.{w= 0.15}.{w= 0.15}."

y h "You want a drink?"

window hide
show black

jump END