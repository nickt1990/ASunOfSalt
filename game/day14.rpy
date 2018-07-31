label day14:
    
e ".{w=0.15}.{w=0.15}."

hide black
    
e "You're woken up by some sort of sound coming from the hallway."

e "It sounds like.{w=0.15}.{w=0.15}.{w=0.15} music?"
    
menu:
    "Check it out.":
        pass

e "You walk over to the doorway."

call hall from _call_hall_28

play sound "sounds/DoorOpen2.mp3"

e "As you walk out into the hallway, {w=0.15}you see Nema sitting on the ground across the hall."

e "Music is coming from a small,{w=0.15} old boom-box."

e "On the ground next to the boom-box,{w=0.15} Nema is laying down, writing in a black notebook."

show p h

p h "Good morning Captain."

e "She sits up as soon as she sees you."

p h "How are you Sir?"

menu:
    "Good.":
        p h "I'm happy to hear it sir!"
        pass

    "Are you feeling alright?":
        p h "Of course!"
        pass

p n "By the way, {w=0.15}while I have you here."

p n "I just wanted to let you know that I'll be taking over for Hei on his engine monitoring duty tonight."

menu:
    "Why?":
        pass

    "Did he talk you into that?":
        p h "Hah, {w= 0.15}no sir."
        pass

p h "I want to understand things better."

p n "I was thinking I'd monitor the levels and find averages."

p n "Maybe we can automate the process somehow."

play sound "sounds/DoorOpen2.mp3"

show y n:
    linear 0 xalign 0.9 yalign 1.0

y n "That wouldn't work."

show p su

p su "Oh!"

p h "Hey Haruka."

show y m

y m "We didn't automate the monitoring of the engine because we're operating with untested hardware."

y n "There's no way for us to actually know what levels to expect,{w= 0.15}or what things going wrong will look like."

show p n

p n "Are we sure about that?"

p n "Have we done extensi-"

show y m

y m "Just leave it alone Nema,{w= 0.15}alright?"

show p s

p s ".{w=0.15}.{w=0.15}."

p n ".{w=0.15}.{w=0.15}."

p m "No."

show y su

y su "What?"

show p n

p n "I'm going to take Hei's shift, {w=0.15}I'm going to monitor the engine,{w=0.15} and I'm going to see what conclusion I come to."

show y m

y m "No,{w=0.25} you're not."

y m "Hei is taking his shift,{w=0.15} and you will let him."

show p m

p m "I'm sorry Haruka,{w=0.15} but you have absolutely no authority over me."

p m "I'm doing what I said I would."

show y m

y m "Where is this coming from?"

y m "Who are you all of a sudden?"

y m "I just sai-"

show p m

p m "I'll talk to you later Captain."

play sound "sounds/DoorClose2.mp3"

hide p

e "Nema grabs her things then turns around and walks into her room."

show y m

y m "Hey!"

e "Haruka stomps after Nema and begins to knock on her door."

y m "What's your deal?!"

y m "Get out here and talk to me!"

show p m

play sound "sounds/DoorOpen2.mp3"

e "Nema pops her head out of her doo."

p m "I've been trying to talk to you for two weeks and I haven't made any progress."

p m "You say you're sick of always being in control? "

p m "Here's your chance,{w=0.15} sit back."

hide p

play sound "sounds/DoorClose2.mp3"

e "Nema turned up the music in her room."

show y su

y su "Unbelievable."

play sound "sounds/DoorOpen2.mp3"

e "Hei walks out of his room."

show r su

r su "What's goin' on out here?"

show y m

y m "Nema's totally lost it."

show r su

r su "What?"

show y m

y m "She wants to take your shift tonight for some maintenance stuff that I already know wont work."

show r n

r n "Oh.{w=0.15}.{w=0.15}."

r n "So why's that a problem?"

show y m

y m "Just because neither of you know how to actually contribute doesn't mean you should start doing whatever comes to mind."

y m "I have a plan in place, {w=0.15}you have to come to me with this stuff."

show r m

r m "Woah dude, {w=0.15}what?"

r m "Why am I getting chewed out here all of a sudden?"

r m "You're the one that said you wanted us to take some initiative."

r m "That's what Nema's doing."

show y m

y m "Right,{w= 0.15}and what are you doing?"

y m "Why am I even talking to you."

show r m

r m "Hey,{w= 0.15}that's not fair."

r m "Have you ever thought maybe that you're the problem?"

r m "Maybe Nema and I want to try and do more,{w= 0.15}but you always just shut us down?"

r m "If you actually wanted us to step up,{w= 0.15}you've give us a chance."

show y m

y m "Please,{w= 0.15}you don't wait for somebody else to give you a chance."

y m "You take it,{w= 0.15}or you don't do anything."

show r m

r m "Whatever,{w= 0.15}you just want to feel all high and mighty and tell us what to do and feel like the one smart person among idiots."

r m "Screw this,{w= 0.15}figure it out on your own."

r m "And more power to Nema,{w= 0.15}good for her finally standing up for herself."

e "Hei looks towards you."

r m "Good luck with her dude."

play sound "sounds/DoorClose2.mp3"

e "Then he turns and storms off back into his room."

show y m

y m "Great,{w= 0.15}so it's take your frustrations out on Haruka day."

y m "I don't deserve this,{w= 0.15}I've kept this ship afloat this entire time."

y m "I work day and night for a stupid cause I don't even care about anymore."

y m "And I'm the bad guy here."

menu:
    "Well, you are kind of shutting them down.":
        pass

    "Everyone's stressed out, just calm down.":
        pass

y m "Seriously?"

y m "You don't think it's possible for them to do anything without me guiding them along and allowing it?"

y m "I'm not their mother man,{w= 0.15}they need to figure out their own shit."

y m "I'll see you later,{w= 0.15}I can't do this right now."

hide y

e "Everyone has gone back to their rooms."

call blueRoom

e "You head back into your room and check your mail."

label summariesD14:

window hide
show black 
with fade

menu:#computer
    "I'll read the summaries.":
        menu:
            "Haruka's summary.":
                call day14HaruS
                jump summariesD14
                pass
            "Hei's summary.":
                call day14HeiS
                jump summariesD14
                pass
            "Nema's summary.":
                call day14NemaS
                jump summariesD14
                pass
            "I think I'm done.":
                jump day14Mid
                pass                
        pass

    "I'm going to respect their privacy.":
        jump day14Mid
        pass

label day14Mid:

e "You spend the rest of the evening working and end up falling asleep early."

e ".{w=0.15}.{w=0.15}."

return