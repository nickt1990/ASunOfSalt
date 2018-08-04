label day15:

window hide
hide black 
with fade

e "You wake up,{w= 0.15}but it's still the middle of the night."

e "You can hear a slight sound coming from the hallway."

e "You get out of bed and get dressed."

play sound "sounds/DoorOpen2.ogg"

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
        show p h
        p h "I agree sir."
        pass

    "Why the change of heart?":
        y su "Why?"
        y m "Doesn't matter, I'm helping her, aren't I?"
        pass

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

menu:
    "Is that okay with you, Nema?" if nemaHarukaLove:
        jump NHL
        pass
    
    "Is that okay with you, Nema?" if nemaHarukaLove == False:
        jump noNHL
        pass    
    
return