label day9Night:
    
call hall from _call_hall_50

e "Some time has passed, so you head out to the kitchen to meet Haruka."

show y h

call kitchen from _call_kitchen_14

play music "music/Spacetalk.ogg" fadein 3.0

y h "Heya Cap."

menu:
    "Hi.":
        pass

    "How are you?":
        pass

y s "I've never been good with this shit,{w=0.2} so I'm just going to say what's on my mind, {w=0.15}alright?"

menu:
    "Sure.":
        pass

    "Whatever.":
        pass

y s "I don't really lose my temper,{w=0.2} ever."

y s "I hate that I let myself go like that."

y n "I told you I expected great things out of you and that you could expect great things out of me."

y s "I don't think I've held up my end of things, {w=0.15}and I'm sorry."

menu:
    "It's not me you should be apologizing to.":
        pass

    "It's alright.":
        y s "Well,{w=0.2} still."
        y m "It's just that{w=0.2}.{w=0.2}.{w=0.2}."
        y n "Hei and Nema."
        y m "They just get under my skin."
        jump day9NightAlright
        pass

y n "Hei and Nema?"

y s "No."

y n "Sorry,{w=0.2} but I didn't promise 'em a damn thing."

menu:
    "That's not very professional.":
        pass

y n "I never claimed that I'd act professional."

y m "I can truly say that I just do not like either of them."

menu:
    "You don't mean that.":
        pass

y n "I'm not sorry for how I treated them.{w=0.2} I'm sorry that I promised you better than I'm giving you, {w=0.15}that's all."

label day9NightAlright:

y m "Why bother putting any effort into them if all they're gonna do is sit around screwing?"

menu:
    "Why does that bother you so much?":
        pass

    "They can do whatever they want, {w=0.15}this ship is their life now.":
        y m "Whatever."
        pass

y m "That's just not stuff I take lightly."

menu:
    "Why not?":
        pass

stop music fadeout 2

y s "You're not gonna let me off easy?"

y n ".{w=0.15}.{w=0.15}."

play music "music/PianoCave.ogg" fadein 2.0

y h "What do you want to drink."

menu:
    "Juice.":
        y h "Hope you like apple,{w=0.15} dork."
        pass

    "Something hard.":
        y h "Shots it is."
        pass

e "Haruka grabs you both drinks."

y n "You know what the chance is on average for a girl to get pregnant, {w=0.15}{w=0.2}even with birth control?"

menu:
    "Really low.":
        y n "Really goddamn low."
        pass

    "It's impossible.":
        y su "Nowadays?"
        y h "Almost."
        pass

y n "Like point zero eight percent."

y n "When I was growing up, {w=0.15}I was working with this scientist, {w=0.15}the one that taught me everything I know."

y n "I think I told you about him, {w=0.15}Dr. Motokami?"

y n "He knew the kind of place I was from."

y s "When we first met and I told him that I wanted to be an engineer he looked at me straight in the eyes and said no."

y s "That wont happen."

y n "I wanted to prove him wrong,{w=0.2} so I looked up how many engineers in the travel program came from my station."

y n "One hundred and thirty two."

y su "That's one-thousandth percent of the ninety-five thousand people who worked there."

y n "You'd think that would discourage a kid, {w=0.15}but it did the opposite."

y s "I stopped having fun."

y s "I stopped taking chances."

y n "I realized that I had to be the best I could, {w=0.15}and I couldn't afford to mess things up.{w=0.15} Every decision became a balancing act."

y n "Does this add or take away from my chances?"

y n "When I looked at guys, {w=0.15}I saw a negative point zero eight percent chance of getting off my shit station and into a real life."

y n "There are plenty of losers to pump out kids."

y n "I was going to send those stupid kids to the ends of the universe."

menu:
    "That's sad. ":
        y s "Maybe."
        pass

    "That makes sense. You can't tie yourself down.":
        y h "You think so?"
        y n "I'm not sure anymore."
        pass

y n "Maybe I'm wrong for thinking this way.{w=0.15}.{w=0.15}. Whatever."

y n "I got shit done,{w=0.2} yeah?"

menu:
    "Nema and Hei have accomplishments too.":
        pass

y s "I suppose,{w=0.2} they did make it this far.{w=0.15}.{w=0.15}."

y n "But I think for me, {w=0.15}this was the only way I could have done it."

y s "If I gave myself an inch into temptation, {w=0.15}I would have gone a mile."

y n "That's the kind of person I am."

menu:
    "That doesn't mean Nema and Hei are the same.":
        pass

y s "No.{w=0.2}.{w=0.2}."

y s "I guess it doesn't."

menu:
    "Maybe you've been unfair to them?":
        pass

y m "Ugh, {w=0.15}c'mon.{w=0.35} I didn't ask you here for this."

y s "I wanted to talk about us, {w=0.15}not them."

menu:
    "We're a group and I'm the captain.":
        pass

y s "Yeah yeah, {w=0.15}I get it."

y n ".{w=0.2}.{w=0.2}."

y s "I think I made a mistake."

menu:
    "Yeah, {w=0.15}you were rude as hell.":
        y s "No."
        pass

    "What do you mean?":
        pass

y s "I mean I threw my life away for this ship."

menu:
    "But it could be revolutionary.":
        pass

y n "It could be, {w=0.15}but then what?"

y m "The idiots back at the space station can fly farther faster?"

y m "So we can find more empty planets further away?"

y s "Why even bother exploring when we have dozens of safe sustainable places to live now, {w=0.15}y'know?"

menu:
    "You never know what you'll find out here.":
        y s "But.{w=0.15}.{w=0.15}."
        pass

    "I agree, {w=0.15}why not just be happy with what we have?":
        y n "Exactly."
        pass

y s "Why strive for something better when what you have is good enough?"

y s "I'm definitely not happier than the millions of stupid people who wake up every day and piss their lives away."

y s "I worked myself to death and the only benefit that could possibly come from it will be for all those stupid people back home who are already fine."

menu:
    "What's so bad about that?":
        pass

y m "God,{w=0.2} nothing,{w=0.2} I know, {w=0.15}that's how life goes."

y s "You pass on what you've accomplished.{w=0.2} I get it."

y s "I just feel like a life that was sacrificed to give comfortable idiots another vacation option though."

y s "I never got a chance to.{w=0.1}.{w=0.1}.{w=0.15} I don't know.{w=0.2} Relax."

menu:
    "Why not now?":
        pass

y s "It's too late now."

y n "No offense,{w=0.15} but we're floating in our coffin.{w=0.15} Our lives are over."

menu:
    "No better time to relax than now.":
        pass

    "Then why does it matter? Do what you want.":
        pass

y s "Well I-"

y s ".{w=0.15}.{w=0.15}."

y n "Yeah."

y n "Maybe I should do what I want."

y n "Maybe I sh-"

show tWhite
with hpunch

$ renpy.pause(0.1)

hide tWhite

play music "music/Alarm.ogg" fadein 1.0

e "The ship shakes.{w=0.15} An alarm goes off."

y su "W-{w=0.15}what?"

y su "Oh wai-{w=0.15}Quick! {w=0.15}To the nav room!"

call hall from _call_hall_51

play sound "sounds/DoorOpen2.ogg"

e "You both run into the hall."

e "Hei jumps out of the navigation room into the hall wearing a dress."

show rz su:
    linear 0 xalign 0.9 yalign 1.0

rz su "Guys! Something went wrong!"

menu:
    "What happened?!":
        pass

    "What are you wearing!":
        rz m "Nevermind that!"
        pass

rz su "The engine went way off balance!"

show y su

y su "What do you mean way off?!"

show rz s

rz s "It's just not.{w=0.15}.{w=0.15}.{w=0.15} right?"

rz n "It's off where it's supposed to be."

rz s "The.{w=0.15}.{w=0.15}.{w=0.15} uh.{w=0.15}.{w=0.15}."

show y m

y m "Get out of my way!"

hide rz

call navRoom from _call_navRoom_4

y su "Nema what's going on?!"

show p su:
    linear 0 xalign 0.9 yalign 1.0

p su "I'm so sorry Haruka! "

p su "We j-{w=0.1}just looked away for a minute!{w=0.15} I swear!"

p s "I d-{w=0.15}didn't m-mean t-"

show y m

y m "{i}There's no time for this{/i},{w=0.2} we're dead Nema."

y s "The transfer rate is too high."

y ".{w=0.15}.{w=0.15}."

y su "Oh God.{w=0.15}.{w=0.15}."

y m "Get out of my way!"

stop music fadeout 2

e "Haruka types some commands into the computer."

y s "I set it to restructure but it should take a few minutes."

play music "music/Space.ogg" fadein 1.0

y n "Cap, {w=0.15}can ya watch this screen and let me know if anything gets out of place?"

menu:
    "Sure.":
        pass

    "Nah.":
        pass

y n "I'm adjusting the transfer rate to control the stability."

y s "Just tell me if-"

play music "music/Darker.ogg" fadein 2.0

show rz su:
    linear 0 xalign 0.1 yalign 1.0

rz su "Shit!"

rz su "It's back!"

show p n

p n "What's back Hei?"

show rz su

rz su "The red!{w=0.15} The blood!"

rz su "Look!{w=0.15} I can see it moving towards us! "

show y m

y m "Goddammit why now!"

y n "It looks like it's moving slow.{w=0.15} We have time to do something."

y n "So,{w=0.15} we compound.{w=0.15} Let's take a chance.{w=0.15} The engine can take it."

show rz su

rz su "That could kill us!"

show y n

y n "What do you think that red shit's going to do?{w=0.15} It's followed us this far and we're going insanely fast as it is. We need to move."

show rz s

rz s "I say we just wait it out.{w=0.15} See what happens."

rz s "Have our guns ready."

y s "But you never made changes. {w=0.25}Besides,{w=0.15} I don't think we can rely on weapons for this sort of thing."

show p s

p s "Can the engine h-{w=0.1}handle the compounding process right now, {w=0.15}Haruka?"

show y n

y n "I don't know, {w=0.15}{w=0.15}but what else can we do?"

show p s

p s "R-{w=0.15}right.{w=0.15}.{w=0.15}."

show y m

y m "Cap,{w=0.15} it's up to you, {w=0.15}{w=0.1}but you have to pick {b}now{/b}."

menu:
    "Compound!":
        jump compound9
        pass

    "We're going to wait it out.":
        pass

r m "Roger, guns ready!"

p m "On radar!"

y m "I'm preparing compound just in case."

e "The red ooze just continues to move closer to you."

p su "What do we do sir?"

y su "I think we need to go!"

r su "Yeah,{w=0.15} I'm with that idea now."

r su "Go{w=0.15} go{w=0.15} go!"

y su "Finishing preperations.{w=0.15}.{w=0.15}."

label compound9:

y s "Alright,{w=0.15} done."

y n "I put transfer to as high as I can,{w=0.15} it should take hold in a few seconds."

y s "Brace yourselves kids,{w=0.15} this might be it."

show rz s

stop music fadeout 1

r s "I'm not ready to d-"

play sound "sounds/Boost.ogg"

window hide
show black
with vpunch

return