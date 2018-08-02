label day11Night:

define nemaBed = False
define nemaClothes = False
define nemaPoem = False

play sound "sounds/DoorClose2.ogg"

e "You enter to Nema standing in front of your computer."

show p h

p h "Hello sir."

e "You sit on the side of your bed."

menu:
    "Hey.":
        pass

    "Hello Nema.":
        pass

e "Nema smiles sweetly,{w=0.15} but her eyes are following you closely."

p s "I hope you're not bothered by the idea of sharing a room with me for tonight."

p s "I know that I'm not Haruka,{w=0.15} but I truly look forward to a chance to speak more with you,{w=0.15} Sir."

menu:
    "I'm looking forward to it too!":
        pass

    "Eh.{w=0.15}.{w=0.15}.{w=0.15}":
        pass

p h "That makes me very happy to hear,{w=0.15} Sir."

p n "Would you.{w=0.15}.{w=0.15}.{w=0.15}"

p s ".{w=0.15}.{w=0.15}.{w=0.15}"

p n "Would you mind if I sat with you on the bed?"

menu:
    "Of course.":
        pass

    "Not right now.":
        pass

e "Nema promptly stands up,{w=0.15} walks over,{w=0.15} and sits down neatly beside you with her hands in her lap."

e ".{w=0.15}.{w=0.15}.{w=0.15}"

e ".{w=0.35}.{w=0.23}.{w=0.35}"

e ".{w=0.45}.{w=0.45}.{w=0.45}"

p h "So,{w=0.15} sir. I ha-"

play sound "sounds/Knock.ogg"

e "There's a loud knocking on the door."

p su "I would have thought the life support systems in the hallway would be on low-power mode by now."

menu:
    "Answer the door." if harukaLove == True:
        pass
    "Answer the door." if harukaLove == False:
        e "Haruka's standing just outside the door."
        jump day11nBegin
        pass

play sound "sounds/DoorOpen2.ogg"

e "Haruka's standing outside of your room with a small package."

show y m

y m "Here."

e "She glares at Nema for a moment before handing you the package and starting to walk away."

label day11nBegin:

y m "I'm turning off the life support,{w=0.15} stay in your room."

play sound "sounds/DoorClose2.ogg"

hide y m

show p n

p su "What did she say?"

menu:
    "She dropped off a package..." if harukaLove == True:
        pass
    "Life support is off now." if harukaLove == False:
        p h "Oh good."
        p h "I'm glad we have Haruka to keep us in order."
        jump noSandwich
        pass

menu:
    "Check the package.":
        pass

e "You slowly open up the small box."

e "It's another plain ham sandwich."

p h "How nice of Haruka."

label noSandwich:

p n "She's always first to act in a time of need."

menu:
    "She's great.":
        p h "I had figured you'd feel that way,{w=0.15} Captain."
        pass

    "Not always.":
        p su "I'm sure you don't mean that."
        p n "She's always very quick to act."
        p h "I've noticed you've spent a bit of time together lately."
        pass

p n "You two have become close,{w=0.15} haven't you?"

menu:
    "We have.":
        p h "I'm glad."
        pass

    "Uhm.{w=0.15}.{w=0.15}.{w=0.15}":
        p h "It's okay, I understand."
        pass

e "Nema continues to stare forward for a moment in silence."

p h "I'd like to be close to both of you as well."

e "She has a smile on her face,{w=0.15} but she said this sort of sadly."

p n "I know I'm not always the most fun.{w=0.15}.{w=0.15}.{w=0.15}"

p h "But I think I'm making progress."

p n "Hei has helped with that a lot."

p n "He can be such a dork sometimes.{w=0.15}.{w=0.15}.{w=0.15} "

p h "But,{w=0.15} I like that."

menu:
    "Me too.":
        p h "I'm glad I'm not alone in that."
        pass

    "You're the only one.":
        p n "Well,{w=0.15} for me it would."
        pass

p n "I think it takes a little courage to be a dork."

p h "Don't you think so?"

menu:
    "Yeah it does.":
        pass

    "Not really.":
        p n "Well,{w=0.15} for me it would."
        pass

p h "I'm not the best at just relaxing and being myself."

p n "I don't know why,{w=0.15} it's just always been difficult."

p h "It makes him difficult to work with sometimes,{w=0.15} but he gets to speak his mind and be heard naturally."

p n "I feel like I have to work really hard to be heard."

p n "I want to work on it."

p h "I am working on it."

p n "I can feel myself getting better,{w=0.15} it's just taking a lot of time."

p s "Spending all that time with Hei helped I think,{w=0.15} but also,{w=0.15} it made me see how far I have to go."

p n "It feels like I'll never reach his level.{w=0.15}.{w=0.15}.{w=0.15}"

p n "Is it even possible?"

p s "Will I be stuck like this forever.{w=0.15}.{w=0.15}.{w=0.15}?"

p s ".{w=0.15}.{w=0.15}.{w=0.15}"

p h "I'm sorry,{w=0.15} I'm not complaining."

p n "After spending a whole day with Hei I'm just left with a lot to think about."

p h "And knowing we're locked up in here makes it easier to talk,{w=0.15} for some reason."

menu:
    "I kind of get that.":
        p h "Right? I'm glad."
        pass

    "Why?":
        pass

p n "It feels more personal,{w=0.15} more private."

p n "Like I can speak softer and not try as hard."

p n "Maybe like how Hei or Haruka always feel."

menu:
    "Maybe.":
        pass

    "Who knows.":
        pass

p h "Right."

e "Nema smiles at you,{w=0.15} then looks down at the floor."

#todo space shrimp effect (move effects across screen)
e "You sit in silence for a moment,{w=0.15} then there's a bright light out the window."

menu:
    "What's that?":
        pass

    "Are we in danger?":
        show p h
        e "Nema smiles at you."
        p n "I don't think so{w=0.15}.{w=0.15}.{w=0.15}."
        pass

p n "Hey.{w=0.15}.{w=0.15}.{w=0.15}"

p h "Space shrimp."

p n "Wow.{w=0.15}.{w=0.15}.{w=0.15}"

menu:
    "It's beautiful.":
        pass

    "Creepy.":
        p su "You think so?"
        pass

p n "I always loved when space shrimp would pass by my home."

p h "Down on earth they had things like rain and snow.{w=0.15}.{w=0.15}.{w=0.15}"

p n "Space shrimp kind of seemed like the closest we ever got to that."

p h "Something about that sort of atmosphere changing weather I always loved."

p n "It's romantic,{w=0.15} isn't it?"

menu:
    "Yeah.":
        p h "Agreed sir."
        pass

    "Not really. It's shrimp.":
        p h "I suppose you are right, sir."
        p n "But even still{w=0.15}.{w=0.15}.{w=0.15}."
        pass

p n "You know,{w=0.15} when I was young,{w=0.15} I'd play thunderstorm sounds every night."

p n "I couldn't sleep without it."

p h "My brains usually a little too active,{w=0.15} so the white noise effect really helped me calm down."

p n "But I think.{w=0.15}.{w=0.15}.{w=0.15} "

p s "Well."

p n "I'm talking too much,{w=0.15} aren't I?"

p s "I'm sorry sir,{w=0.15} I'm not sure what's gotten into me."

menu:
    "No,{w=0.15} I'm happy to listen!":
        pass
    "Don't worry about it.":
        pass

p h "Thank you sir."

p n "You've always been such a great listener."

p n "Me and Hei had a lot of fun.{w=0.15}.{w=0.15}.{w=0.15}"

e "Nema looks down and smiles sheepishly."

p n "So.{w=0.15}.{w=0.15}.{w=0.15}"

p n "If you're sure.{w=0.15}.{w=0.15}.{w=0.15}"

p h "I've always been a bit of a nerd when it comes to history."

p n "The old way of life on earth has always fascinated me."

p n "I'd collect candles and CDs and old pictures."

menu:
    "Candles?":
        p s "Yeah.{w=0.15}.{w=0.15}.{w=0.15}"
        pass

    "Old pictures?":
        p h "Yeah."
        p n "Just random pictures."
        p n "Not even people I knew."
        p h "I think that made it more interesting though."
        p h "Like having a tiny piece of somebody's life story."
        p n "That's how I felt at the time, anyways."
        p h "I really miss the candles more though, if I'm honest with you."
        pass

p h "Pumpkin scents were always my favorite."

p n "I had this one candle,{w=0.15} white pumpkin."

p h "I loved it to death."

p s "But.{w=0.15}.{w=0.15}.{w=0.15}"

p s "It must not have been popular,{w=0.15} because I only ever found one."

p n "It was my special event candle."

p n "I can remember each and every time I lit it."

menu:
    "Every single time?":
        pass

    "What was the last time?":
        jump lastCandle
        pass

p h "Yes sir!"

p n "I've only lit it six times so far."

p n "The first time was the first time I found it."

p n "To celebrate finding it."

p h "Second time was when I was accepted into Segment 3 higher studies."

p n "The next few times with my brothers.{w=0.15}.{w=0.15}.{w=0.15}"

label lastCandle:

p h "The last time was the night before I left for this mission."

menu:
    "A celebration?":
        pass

    "A goodbye?":
        pass

p n "Yes.{w=0.15}.{w=0.15}.{w=0.15} in a way."

p h "I just did everything I loved,{w=0.15} since I didn't know if I'd ever get the chance again."

menu:
    "Like what?":
        pass

p n "You'll think I'm strange."

menu:
    "It takes courage to be strange too.":
        p h "I suppose so."
        pass

    "No I wont.":
        p s "Okay{w=0.15}.{w=0.15}.{w=0.15}.{w=0.15} Well{w=0.15}.{w=0.15}.{w=0.15}."
        pass

p n "Well I turned to temperature down as far as I could."

p h "I love the cold."

p n "Then,{w=0.15} I lit my white pumpkin candle."

p n "Turned on my thunderstorm soundtrack."

p n "And.{w=0.15}.{w=0.15}.{w=0.15} wrote."

p h "Poems."

menu:
    "Poems?":
        pass

p n "Yes."

p h "I love writing poems."

menu:
    "Unexpected.":
        pass

    "That's interesting.":
        pass

p su "You think so?"

p n "I always thought it would seem cliche so I never told anybody."

p h "The quiet girl writes poems."

p n "But sometimes there's a reason behind some stereotypes."

p n "I have a hard time communicating sometimes,{w=0.15} but poems help me feel in control of that."

p h "It seems like a lot of people feel that way."

p n "So,{w=0.15} it doesn't make me unique."

p h "But it makes me feel understood a little bit."

menu:
    "Can I read one of your poems?":#todo read poem later
        $ nemaPoem = True
        pass

    "I see.":
        $ nemaPoem = False
        jump noPoem
        pass

p s "Oh.{w=0.15}.{w=0.15}.{w=0.15}"

p n "I don't have any with me right now."

p n "But.{w=0.15}.{w=0.15}.{w=0.15} yes."

p h "Yes,{w=0.15} I'll let you read some."

menu:
    "Do you not want me to see?":
        p h "I'm just a little nervous."
        p n "I've never shared them."
        pass

    "Alright.":
        p n "I've never shared them."
        p n "So I am a little nervous{w=0.15}.{w=0.15}.{w=0.15}."
        pass

p n "But.{w=0.15}.{w=0.15}.{w=0.15}"

p h "If I'm going to change,{w=0.15} I need to step out of my comfort zone,{w=0.15} right?"

menu:
    "Right. ":
        pass

    "Not really.":
        pass

label noPoem:

e "Nema smiles at you."

p n "So.{w=0.15}.{w=0.15}.{w=0.15}"

p h "If I'm honest Captain,{w=0.15} I'm feeling a little exhausted."

e "Nema stands up,{w=0.15} then pulls back the covers of your bed."

p n "Do you want to get to bed?"
#todo test branches
menu:
    "What? Come to bed?":
        pass

    "Sure.":
        $ nemaBed = True
        jump inBed
        pass

p su "Oh I'm sorry, I don't mean anything by it."

p n "There's nothing inherently sexual about physical contact or exposing skin as far as I'm concerned."

p s "I know that's not common thought though."

p h "I wouldn't blame you at all for feeling different, but{w=0.15}.{w=0.15}.{w=0.15}."

p n "Do you think that's weird?"

menu:
    "A little...":
        p s "I apologize sir."
        p n "I'm not suggesting we do anything sexual,{w=0.15} if that helps."
        pass

    "No!":
        p h "Good."
        p n "I'm happy you think the same."
        pass

p h "I just find it nice to sleep near another person."

p n "If it makes you uncomfortable,{w=0.15} I have no issues with sleeping on the floor though."

p h "I grabbed a sleeping bag just in case."

menu:
    "We can share.":
        p h "That sounds excellent to me,{w=0.15} sir."
        $ nemaBed = True
        pass

    "It might be best if we split up.":
        p h "No problem sir."
        e "Nema grabs a sleeping bag from the corner of the room and spreads it out on the floor."
        pass

label inBed:

e "She smiles,{w=0.15} then starts to lift her shirt over her head."

menu:
    "What are you doing?":
        pass

    "...":
        $ nemaClothes = False
        jump gettingNakedNema
        pass

p su "Oh!"

p n "My apologies again sir."

p h "I normally sleep in my underwear because I have a hard time getting comfortable in clothes."

p n "But I'd be okay staying dressed if you'd like."

menu:
    "No,{w=0.15} it's no trouble. ":
        pass

    "If you could,{w=0.15} please.":
        $ nemaClothes = True
        p su "Oh, okay."
        p h "Of course, I didn't mean to make you uncomfortable sir."
        p s "I suppose that was extremely inappropriate of me to even ask{w=0.15}.{w=0.15}.{w=0.15}."
        jump day11nEnd
        pass

p h "Are you sure sir?"

menu:
    "It was just surprising.":
        pass

    "Yes.":
        pass

p n "Alright,{w=0.15} as long as you're not bothered."

label gettingNakedNema:

e "She continues to pull her shirt up over her head and off her body."

e "Once her shirt's removed,{w=0.15} she pulls down her skirt and steps over it."

e "She starts to fold her clothes, paying no attention to you."

label day11nMenu:

menu:
    "Get into bed." if nemaBed == True and nemaClothes == True:
        e "You climb into bed."
        e "She slides into the bed next to you shortly after and pulls up the blankets."
        e "She sighs,{w=0.15} then pulls her body against yours."
        p s "I'm sorry for talking so much tonight Captain."
        p n ".{w=0.15}.{w=0.15}.{w=0.15}"
        p h "Thank you,{w=0.15} Sir."
        e "She squeezes you lightly,{w=0.15} and then falls asleep."
        hide p h
        pass
    "Get into bed." if nemaBed == True and nemaClothes == False:
        hide p n
        show pz n
        e "You climb into bed."
        e "She slides into the bed next to you and pulls up the blankets."
        e "She sighs,{w=0.15} then rolls onto her side."
        pz s "I'm sorry for talking so much tonight Captain."
        pz n ".{w=0.15}.{w=0.15}.{w=0.15}"
        pz n "And.{w=0.15}.{w=0.15}.{w=0.15}"
        pz h "Thank you,{w=0.15} Sir."
        e "She touches your side lightly,{w=0.15} and then falls asleep."
        hide pz h
        pass
    "Get into bed." if nemaBed == False and nemaClothes == True:
        e "As you climb into bed, you notice Nema sliding into her sleeping bag."
        e "She pulls it up to her chin and looks over at you with a smile."
        p h "Sleep well, sir."
        p h "I'm happy we were able to talk tonight."
        hide p h
        pass
    "Get into bed." if nemaBed == False and nemaClothes == False:
        e "As you climb into bed, you notice Nema sliding into her sleeping bag."
        e "She pulls it up to her chin and looks over at you with a smile."
        pz h "Sleep well, sir."
        pz h "I'm happy we were able to talk tonight."
        hide pz h
        pass

label day11nEnd:

e "After a few moments you drift off."

e ".{w=0.25}.{w=0.25}."

window hide
show black
with fade

#todo demon
d "Sleep well."

d "Our time draws near."

return