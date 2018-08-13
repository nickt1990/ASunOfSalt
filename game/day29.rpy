label day29:

e ".{w= 0.15}.{w= 0.15}."

window hide
hide black
with fade

play sound "sounds/DoorOpen2.ogg"

e "Your bedroom door opens."

e "Nema and Haruka are standing in the doorway hand-in-hand."

show y h:
    linear 0 xalign 0.4 yalign 1.0
show p h:
    linear 0 xalign 0.6 yalign 1.0

y h "Good morning sir."

p h "Yeah,{w= 0.15} g'morning."

menu:
    "Good morning.":
        pass

y h "Doin well Caps?"

menu:
    "Could be worse.":
        y h "Ever the optimist!"
        pass
    "No complaints.":
        y h "I hear ya."
        pass
    "Eh.":
        y m "Get that outta here man."
        y s "You can go hang out with Hei if that's how you wanna be."
        pass

e ".{w= 0.15}.{w= 0.15}."

y h "Well.{w= 0.15}.{w= 0.15}. as much as I'd love to stay and enjoy this wild conversation{w= 0.15} I just wanted to say hey."

y h "Nema said she had something to talk to you about."

p h "Thank you,{w= 0.15} Haru."

show y h

y h "Sure thing jelly bean."

e "Haruka leans over and kisses Nema on the cheek, then walks back out the door."

hide y

show p h:
    linear 0.3 xalign 0.5 yalign 1.0

p s "Captain.{w= 0.15}.{w= 0.15}."

p h "You know.{w= 0.15}.{w= 0.15}."

p s "I was going to kill everyone on this ship a few weeks ago."

menu:
    "What?":
        pass

p h "Yeah,{w= 0.15} we don't have to get into it."

p n "I more wanted to talk about why I didn't."

menu:
    "Why?":
        pass
    "What?":
        p h "No, why."
        pass

p n "To be honest,{w= 0.15} this was starting to feel a bit like home."

p h "As soon as Haruka and I actually sat down and talked with each other,{w= 0.15} I realized we were both feeling the same."

p s "Funny how two people hurting the same way can take it out in two entirely different ways,"

p n "I was far away from home,{w= 0.15} unable to talk to my family or anyone like me."

p n "Not sure what purpose my mission here would actually accomplish for everyone."

p s "Not sure if I wanted to accomplish anything for anyone."

p n "But Haruka and me got to talking and.{w= 0.15}.{w= 0.15}."

p h "Well."

p h "You only get one chance,{w= 0.15} and I want to spend mine here trying to be happy."

menu:
    "Happy with Haruka?":
        p h "Yeah."
        pass

    "Happy with all of us?":
        p h "Of course."
        p h "Surprisingly,{w= 0.15} Haruka's been a big part of what's going right lately."
        pass

p n "She has the confidence to push us forward,{w= 0.15} and I have the right kind of mind to keep our heads where they should be."

p h "At least that's how I see it."

p n "Just this morning we.{w= 0.15}.{w= 0.15}."

p s "Uhm.{w= 0.15}.{w= 0.15}."

p h "Well,{w= 0.15} we finally got on each others level."

menu:
    "What's that mean?":
        pass

p n "I think that should be fairly obvious."

p h "Hei wont be too happy about it,{w= 0.15} but to be honest.{w= 0.15}.{w= 0.15}."

p n "If you don't help yourself,{w= 0.15} you can't always expect a happy ending."

menu:
    "I guess.":
        pass

    "I agree.":
        pass

e "Nema smiles."

p n "Well anyways,{w= 0.15} that's it."

p h "I just felt like it was time to come clean since I've decided to stay with you all."

menu:
    "I'm glad you decided to stay.":
        pass

p n "Me too."

p h "You do what you have to sir,{w= 0.15} and I'll do what I have to."

p n "That's what it's all about,{w= 0.15} isn't it?"

p n "Either work toward what you want or live unfulfilled."

p h "You don't need to make a dramatic turnaround,{w= 0.15} or have a shocking revelation."

p h "You just need to try to change,{w= 0.15} just a little."

p s ".{w= 0.15}.{w= 0.15}."

p h "Yes,{w=0.15} that's what I think."

show black

e ".{w= 0.35}.{w= 0.35}."

jump END
    
return