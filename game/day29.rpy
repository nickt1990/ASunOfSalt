label day29:

e ".{w= 0.15}.{w= 0.15}."

e "You wake up to a darkened room."

e "Your bedroom door opens."

e "Nema and Haruka are standing in the doorway hand-in-hand."

show y h

y h "Good morning sir."

show p h

p h "Yeah,{w= 0.15} g'morning."

menu:
    "What's gotten into you two?":
        pass

    "Good morning.":
        pass

p h "Hey,{w= 0.15} Haru,{w= 0.15} would you mind giving me and Captain a minute to talk privately?"

show y h

y h "Sure thing."

e "Haruka walks back out the door and disappears down the hall."

show p h

p h "You know,{w= 0.15} I was going to kill everyone on this ship a few weeks ago."

menu:
    "What?":
        pass

    "I know.":
#todo branch
        pass

p h "Yeah,{w= 0.15} we don't have to get into it."

p n "I more wanted to talk about why I didn't."

menu:
    "Why?":
        pass

p n "Well,{w= 0.15} to be honest,{w= 0.15} this was starting to feel a bit like home."

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
        pass

    "Happy with all of us?":
#todo branch
        pass

p h "Yeah."

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

p n "If you don't help yourself,{w= 0.15} then I don't think you can complain."

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

    "I'm going to tell them what you just said.":
#todo branch
        pass

p n "Me too."

p h "We'll see."

p h "You do what you have to Sir,{w= 0.15} and I'll do what I have to."

p n "That's what it's all about,{w= 0.15} isn't it?"

p n "Either work toward what you want,{w= 0.15} or give up and fade away."

show black

jump END
    
return