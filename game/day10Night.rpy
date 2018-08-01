label day10Night:

define harukaLove = True

show yb n

yb n ".{w=0.15}.{w=0.15}."

yb m "Wake up."

window hide
hide black
with fade

menu:
    "What are you wearing?":
        pass

yb su "Oh."

yb s "Uhm,{w=0.15} nothing."

yb n "Guys,{w=0.15} I mean,{w=0.15} people like this kind of thing, {w=0.15}right?"

yb s ".{w=0.15}.{w=0.15}."

yb h "What do you think?"

menu:
    "Cute.":
        yb h "You think?"
        yb s "It's weird isn't it."
        yb s "I look dumb.{w=0.15} I don't even know why I brought this outfit."
        yb s ".{w=0.15}.{w=0.15}."
        yb s "I'm going to change."
        yb h "Yeah."
        jump changeHaru10n
        pass

    "Uhm...":
        yb s "Oh.{w=0.15}.{w=0.15}."
        pass
        
    "Not a fan.":
        yb su "Seriously?"
        yb s "I see."
        yb n "B-.{w=0.15}.{w=0.15}."
        pass

yb h "Uhm.{w=0.15}.{w=0.15}."

menu:
    "What?":
        pass

    "Are you alright?":
        pass

yb s "If you want I could.{w=0.15}.{w=0.15}. change?"

yb s "Into something more comfortable,{w=0.15} I mean."

yb h "Not that this isn't comfortable."

yb h "I mean, just like, if you want I can change."

menu:
    "You should change.":
        pass

    "You're acting weird.":
        yb su "Weird?"
        yb n "Whatever, okay, I'll change."
        pass

yb su "O-{w=0.15}okay."

yb n "Of course,{w=0.15} right."

yb n "I'll change."

label changeHaru10n:

yb m "Close your eyes."

e "You close your eyes."

window hide
show black
with fade

yz n "Uhm.{w=0.15}.{w=0.15}."

yz s "A-{w=0.15}alright."

yz n "I mean,{w=0.15} you can open your eyes."

window hide
hide black
with fade

e "You open your eyes to see Haruka sitting beside you on the bed, stripped down to her underwear."

yz m "Don't stare!"

yz n "But.{w=0.15}.{w=0.15}.{w=0.15} do you think I look good?"

menu:
    "Yes.":
        jump nakedStay10n
        pass

    "You're making me uncomfortable.":
        yz su "Oh man."
        yz s "I'm so sorry Cap."
        yz s "I feel like an idiot."
        yz s "Look away."
        pass

label onClothesd10n:
##############################################
window hide
show black
with fade

e "You hear rustling."

e ".{w=0.15}.{w=0.15}."

yb s "Okay."

window hide
hide black
with fade

yb s "This is all I brought over{w=0.15}.{w=0.15}.{w=0.15}."

yb s ".{w=0.45}.{w=0.45}."

yb s "I'm sorry."

menu:
    "What is going on with you?":
        pass

yb s "Am I that bad at this?"

yb n "I thought a lot about what you said before."

yb s "I was jealous of Hei and Nema."

yb n "I've never taken the time to.{w=0.15}.{w=0.15}. ya'know.{w=0.15}.{w=0.15}. like somebody."

yb s "It seemed sort of like it could be nice, I don't know."

yb h "I've thought about it all of course."

yb s "Does that make it sound sad?"

yb n "Of course I have though."

yb n "Having somebody who you're just connected to."

yb h "Sharing stories, time, life."

yb n "You know.{w=0.15}.{w=0.15}. and.{w=0.15}.{w=0.15}. sex."

yb n "I always thought sex was more mental than physical."

yb h "Like the most honest way to tell somebody that you love them."

yb s "I'm naive."

yb s "Hei and Nema have shit all over that idea."

yb s "I just don't know a thing about anyone or anything but myself and this damn ship."

menu:
    "That's not true.":
        pass

    "You've built this all up too much.":
        pass

yb su "What?"

yb n "What do you mean?"

menu:
    "Sex and relationships can be what you want.":
        pass

    "Don't worry about anyone but you.":
	    yb n "Yeah.{w=0.35}.{w=0.35}."
		yb h "Yeah I guess so."
		jump notAsSweet
        pass

    "There's nothing to know, follow your instincts.":
        pass

yb su "C-{w=0.15}cap.{w=0.15}.{w=0.15}."

yb h "It means a lot to hear that."

label notAsSweet:

yb n "I've never tried to actually talk about this stuff before."

yb h "I thought I'd mess everything up,{w=0.15} or weird you out, {w=0.15}or seem like a little kid."

yb n "I know I sort of project a certain image.{w=0.15}.{w=0.15}."

yb s "I'm fine talking about it when I'm messing around,{w=0.15} but when it feels real like this.{w=0.15}.{w=0.15}."

menu:
    "Don't worry about that.":
        pass

    "Yeah, this was a surprise.":
        pass

yb n ".{w=0.15}.{w=0.15}."

yb su "Is.{w=0.15}.{w=0.15}. this alright?"

e "She slowly falls on the bed, pulling you down with her."

e "Her head is resting on your shoulder,{w=0.15} the length of her body is sat warmly beside your own."

menu:
    "This is perfect.":
        pass

    "Sorry, let's keep some space.":
	    $ harukaLove = False
        yb su "Oh."
		yb n ".{w=0.25}.{w=0.25}."
		yb s "Oh."
		yb s "Gotcha."
		yb s "Well, I didn't bring anything else to sleep on, but I'll keep to my side of the bed."
		yb s ".{w=0.25}.{w=0.25}."
		yb s "I'm sorry to make this night weird for you."
		yb s "I thought I felt a connection,{w=0.25} but I guess that was just me."
		yb s "That's okay."
		hide yb s
		jump endDay10N
        pass

e "Haruka just smiles up at you, then closes her eyes and squeezes your arm."

window hide
show black
with fade

yb h "Thank you.{w=0.15}.{w=0.15}."

hide yb h

jump endDay10N

label nakedStay10n:
yz h "Oh.{w=0.15}.{w=0.15}."

yz n "Thank you."

yz m "Not that I changed because of that."

yz n "I just didn't know how you felt about the.{w=0.15}.{w=0.15}. uhm.{w=0.15}.{w=0.15}."

yz n "You know."

yz n "So, uh."

e "She scoots closer to you."

e "You can feel her warm skin against your arm."

e "She's making an effort to stay close, but you can feel her trembling."

yz h "I guess we're all locked in our rooms for a whole day, huh."

yz n "So I guess we should.{w=0.15}.{w=0.15}."

e "She leans toward your face, closes her eyes and pushes her lips out."

e "She's trembling violently, her face is scrunched up and uncomfortable looking."

menu:
    "Of course...":
        e "The second you get close she jumps back, shocked."
        pass

    "Why are you doing this all of a sudden?":
        yz su "Oh!{w=0.15} Uhm.{w=0.15}{w=0.15}.{w=0.15}."
        pass



yz su "S-{w=0.15}sorry!"

yz s "I'm sorry."

menu:
    "What is going on with you?":
        pass

yz s "Am I that bad at this?"

yz n "I thought a lot about what you said before."

yz s "I was jealous of Hei and Nema."

yz n "I've never taken the time to.{w=0.15}.{w=0.15}. ya'know.{w=0.15}.{w=0.15}. like somebody."

yz s "It seemed sort of like it could be nice, I don't know."

yz h "I've thought about it all of course."

yz s "Does that make it sound sad?"

yz n "Of course I have though."

yz n "Having somebody who you're just connected to."

yz h "Sharing stories, time, life."

yz n "You know.{w=0.15}.{w=0.15}. and.{w=0.15}.{w=0.15}. sex."

yz n "I always thought sex was more mental than physical."

yz h "Like the most honest way to tell somebody that you love them."

yz s "I'm naive."

yz s "Hei and Nema have shit all over that idea."

yz s "I just don't know a thing about anyone or anything but myself and this damn ship."

menu:
    "That's not true.":
        pass

    "You've built this all up too much.":
        pass

yz su "What?"

yz n "What do you mean?"

menu:
    "Sex and relationships can be what you want.":
        pass

    "Don't worry about anyone but you.":
        pass

    "There's nothing to know, follow your instincts.":
        pass

yz su "C-{w=0.15}cap.{w=0.15}.{w=0.15}."

yz h "It means a lot to hear that."

yz n "I've never tried to actually talk about this stuff before."

yz h "I thought I'd mess everything up,{w=0.15} or weird you out, {w=0.15}or seem like a little kid."

yz n "I know I sort of project a certain image.{w=0.15}.{w=0.15}."

yz s "I'm fine talking about it when I'm messing around,{w=0.15} but when it feels real like this.{w=0.15}.{w=0.15}."

menu:
    "Don't worry about that.":
        pass

    "Yeah, this was a surprise.":
        pass

yz n ".{w=0.15}.{w=0.15}."

yz su "Is.{w=0.15}.{w=0.15}. this alright?"

e "She slowly falls on the bed, pulling you down with her."

e "Her head is resting on your shoulder,{w=0.15} the length of her body is sat warmly beside your own."

menu:
    "This is perfect.":
        pass

    "Sorry, let's keep some space.":
        $ harukaLove = False
        yz su "Oh."
		yz n ".{w=0.25}.{w=0.25}."
		yz s "Oh."
		yz s "Gotcha."
		yz m "You just wanted a show."
		yz m "I get it."
		yz s "Well, I didn't bring anything else to sleep on, but I'll keep to my side of the bed."
		yz s ".{w=0.25}.{w=0.25}."
		yz s "Goodnight I guess."
		hide yz s
		jump endDay10N
        pass

e "Haruka just smiles up at you, then closes her eyes and squeezes your arm."

window hide
show black
with fade

yz h "Thank you.{w=0.15}.{w=0.15}."
hide yz h

label endDay10N:

window hide
show black
with fade

return