label day15:
    
hide black 

e "You wake up,{w= 0.15}but it's still the middle of the night."

e "You can hear a slight sound coming from the hallway."

e "You get out of bed and get dressed."

play sound "sounds/DoorOpen2.mp3"

e "After that,{w= 0.15}you walk out into the hallway."

e "There are voices coming from the kitchen."

e "You walk in to see Haruka and Nema sitting at the table talking."

show p h

p h "Oh,{w= 0.15}good morning Captain."

show y h

y h "Hey."

menu:
    "What's going on?":
        pass

    "Everything alright?":
        pass

show p h

p h "Haruka came to me last night and apologized."

p n "She said she was happy I wanted to be more involved,{w= 0.15}and offered to help me get up to speed."

show y h

y h "Yeah,{w= 0.15}change of heart I guess."

menu:
    "That's great.":
        pass

    "Why the change of heart?":
        pass

show p h

p h "I agree sir."

p n "Do you want to sit in and listen as well?"

show y n

y n "Actually,{w= 0.15}before you answer,{w= 0.15}I'm gonna say you should just stay."

y n "We have something to talk about."

show p su

p su "Oh?"

p h "Alright,{w= 0.15}great."

menu:
    "What is it?":
        pass

show y s

y s "Well.{w= 0.15}.{w= 0.15}."

y n "Do you remember our discussion a week or so ago?"

y n "About continuing to compound after two weeks?"

y n "Did you ever come up with a decision?"

show p su

p su "Wait,{w= 0.15}what are you talking about?"

show y n

y n "We're talking about continuing to compound the ships energy after tomorrow."

y n "Continuing to gain speed beyond what we can even understand right now."

show p su

p su "Is that safe?"

show y n

y n "No way to know."

y n "That alright with you?"

show p n

p n ".{w= 0.15}.{w= 0.15}."

p n "I'm alright with whatever the Captain decides."

p n "My personal preference.{w= 0.15}.{w= 0.15}. is that we don't do it."

show y su

y su "What?"

y n "Why?"

show p n

p n "I'd like to stick to the mission parameters."

p n "I think it would be irresponsible to potentially throw away a resource that the stations are expecting to be here."

show y m

y m "A resource? We're dead to them."

y n "They're expecting a message or two from us with a little information,{w= 0.15}and that's it."

y n "Let's do this for.{w= 0.15}.{w= 0.15}."

y n ".{w= 0.15}.{w= 0.15}."

y h "For ourselves."

y n "Let's see something nobody else has."

show p s

p s "I have to argue against that idea Sir."

p n "Let's provide value for our friends and family back home."

show y m

y m "What if we don't have a family back home worth a damn?"

y m "What if we come up with nothing?"

show p n

p n "Then we take satisfaction knowing we were a stepping stone that helped the station get to the next mission that will help them."

show y m

y m "That's insane."

y n "Captain,{w= 0.15}what do you want to do?"

menu:
    "Compound.":
        #if haruka flag, call HarukaEnd
        pass

    "Stop and follow our original orders.":
        jump TwoWeeks
        pass

y h "Hah,{w= 0.15}I knew you had a mind of your own."

y n "I appreciate your fight Nema,{w= 0.15}but I think you'll come around on the idea."

y h "We don't have to live the rest of our lives for some people we'll never meet."

y h "We can experience something new and look past the edge of th-"

e "Haruka's eyes roll back."

e "She starts to gasp and choke."

y m "Gh-chh-ka."

y su "Geh-"

e "She falls to the floor and writhes violently for a moment,{w= 0.15}and then settles into a quiet gurgle as her body sits motionless."

menu:
    "Help her.":
        pass

    "Don't help her.":
        pass

show p n

p n "There's no need to help her,{w= 0.15}Sir."

e "Nema looks somehow different."

e "Her face is more menacing."

p n "She's made this all far more difficult than it needed to be from the start."

p h "You haven't made it all that easy on me either,{w= 0.15}to be frank,"

p n "But you know what? After listening to your encouragement and really thinking about it.{w= 0.15}.{w= 0.15}."

p h "I realized I have no reason to keep this facade up anymore."

p n "I've appreciated your companionship,{w= 0.15}and I hope I can continue to."

p n "Will you let me do that sir? "

p s "Or do you want to join Haruka?"

menu:
    "What are you talking about?":
        pass

    "Prepare to die.":
        pass

p n "I'm disappointed Sir. You really had no clue?"

p h "This mission is really about me."

menu:
    "How?":
        pass

p n "I designed the ship."

menu:
    "What about Haruka?":
        pass

p s "Well,{w= 0.15}unfortunately for her,{w= 0.15}none of her designs actually worked."

p h "She had no idea what she was talking about most of the time to be honest."

p n "As it turns out,{w= 0.15}you can't get a very good education from the slums."

p h "She did an adequate job as a stand-in though."

menu:
    "Stand in?":
        pass

p n "Well yeah,{w= 0.15}we couldn't have the focus on me."

p h "People might have dug a little too far and realized that I don't actually have a security number,{w= 0.15}or a hometown."

p n "People might have realized that I'm not a person."

p h "That would have been troubling."

p n "Luckily there are a few humans able to look beyond themselves and their species."

menu:
    "What do you mean?":
        pass

p h "Oh,{w= 0.15}it's a fun story."

p n "One of yours found a way to communicate with one of us."

p h "He's the one who's helped me hold this form for so long."

p n "He also took on a student,{w= 0.15}which I'm told was a big deal for him. "

p n "His first ever,{w= 0.15}a young girl from the slums."

p h "A nobody. I'd say it was random,{w= 0.15}but really he just thought she was cute."

p n "As good a reason as any I suppose."

p h "He filled her head with nonsense,{w= 0.15}and pushed her to the top."

p n "Nobody but him could dispute her supposedly revolutionary theories."

p n "He convinced them all she was a genius."

p n "That she was going to change the world."

p h "And that got us all the funding and time we needed."

menu:
    "Haruka?":
        pass

    "Nema?":
        pass

p m "Obvious."

p n "She had an expiration date on her head since the moment Motokami saw her."

p h "She fulfilled her purpose perfectly. Don't feel bad for her."

menu:
    "You killed her.":
        pass

    "What are you?":
        pass

p n "Yeah,{w= 0.15}but I gave her the courtesy of letting her think she might have made a difference in the world all the way to the end."

p h "She allowed us this opportunity,{w= 0.15}after all."

menu:
    "What are you?":
        pass

p h "Ah,{w= 0.15}the real question."

p n "But a name wouldn't tell you anything."

p n "I am.{w= 0.15}.{w= 0.15}."

p h "Not like you."

p n "Not a body like this."

p h "I'm something more.{w= 0.15}.{w= 0.15}. complex."

p n "I am the fuel for this ship."

p n "I am overflowing."

p h "I'm soon to be the end."

p n "But it's for the best."

p n "I promise."

menu:
    "Why kill Haruka now?":
        pass

p h "There's a question I can give you a real answer to!"

p n "This ship runs on my excess power."

p n "So you can see why this \"compounding\" has been an issue to me."

p h "I'm about ready to transfer over to this existence completely though,{w= 0.15}so I need to gather myself."

menu:
    "Gather yourself?":
        pass

p s "To be quite honest,{w= 0.15}I'm getting a little bored of talking about this."

p n "I'll give you one last question,{w= 0.15}and then we'll say goodbye."

p n "Is that your question or do you have another?"

menu:
    "I have a different one.":
        pass

    "That's my question.":
        pass

p n "I thought as much."

p h "Ask when you are ready,{w= 0.15}Sir."

menu:
    "Is Hei in on this?":
        pass

    "What's going to happen?":
        pass

menu:
    "Why am I here?":
        pass

    "What's your goal?":
        pass

menu:
    "Why do you seem so normal?":
        pass

p n "Hei? "

p s "I'm sorry that your last question was that one."

p n "Hei is.{w= 0.15}.{w= 0.15}. a friend."

p s "In a way."

p s "I'll admit that he disappointed me more than I could ever show.{w=0.15}.{w=0.15}."

p n "I can't offer you much more than that though."

p h "That's life sometimes though,{w= 0.15}isn't it?"

e "The light from the windows begins to turn a deep crimson."

e "You see the red liquid start to gather outside."

p n "Thank you for your help,{w= 0.15}Sir."

p h "It's been interesting spending some time with normal people."

p n "But I think I'm done here."

show black

jump END

label TwoWeeks: #END ---------------------------------------------------

p h "A wise choice,{w= 0.15}Captain."

show y s

y s "Mmm."

y s ".{w= 0.15}.{w= 0.15}."

y n "Not what I would have done,{w= 0.15}obviously."

y n "But.{w= 0.15}.{w= 0.15}."

y n "You know what?"

y n "I'm not upset."

y h "I meant it when I said I was sorry for how I've been acting,{w= 0.15}Nema."

y n "I'm going to back off a little and let you and Hei step up."

show p h

p h "Thank you Haruka."

p n "I think we'll really surprise you."

show y n

y n "I hope so,{w= 0.15}but if you don't.{w= 0.15}.{w= 0.15}."

y h "That's fine."

show e

e "Haruka and Nema look content."

show y n

y n "Cap,{w= 0.15}you can head back to bed after all."

y h "Let's give Nema a chance to shine here,{w= 0.15}yeah?"

y n "I'll talk to ya in the morning."

show p h

p h "Goodnight Captain."

menu:
    "G'night.":
        pass

hide y
hide p

play sound "sounds/DoorClose2.mp3"

e "You walk out of the room."

e "You hear the two girls talking quietly behind you as the door closes."

e "Quietly,{w= 0.15}you walk back into your room and lay on the bed."

e "After a few moments,{w= 0.15}you fall asleep."

e "About two weeks go by.{w= 0.15}.{w= 0.15}.."

jump day29

label HarukaEnd: #END ---------------------------------------------------
    
show y h
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
    "No...":
        pass

    "Yes.":
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

    "I guess.":
        pass

y h "I am."

y n "I've decided to relax a bit."

y s "And,{w= 0.15}uh.{w= 0.15}.{w= 0.15}."

y n ".{w= 0.15}.{w= 0.15}."

e "Haruka goes flush."

y h "There's nobody else I'd rather do it with."

e "She smiles down at you."

y n "So.{w= 0.15}.{w= 0.15}."

y h "You want a drink?"

show black

jump END
    
return