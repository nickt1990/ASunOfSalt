init:
    # Character pictures.
    image p neu = "Nema/PNakedNeutral.png"
    image p hap = "Nema/PNakedHappy.png"
    image p ang = "Nema/PNakedAngry.png"
    image p sad = "Nema/PNakedSad.png"
    image p sur = "Nema/PNakedSurprised.png"
    image p:
        "Nema/PLeatherNeutral.png"
        pause 7
        "Nema/PLeatherNeutral2.png"
        pause 0.1
        repeat
    image p n:
        "Nema/PLeatherNeutral.png"
        pause 7
        "Nema/PLeatherNeutral2.png"
        pause 0.1
        repeat        
    image p s:
        "Nema/PLeatherSad.png"
        pause 7 #10.5
        "Nema/PLeatherSad2.png"
        pause 0.1
        repeat
    image p su:
        "Nema/PLeatherSurprised.png"
        pause 7 #10.5
        "Nema/PLeatherSurprised2.png"
        pause 0.1
        repeat
    image p m:
        "Nema/PLeatherAngry.png"
        pause 7 #10.5
        "Nema/PLeatherAngry2.png"
        pause 0.1
        repeat
    image p h:
        "Nema/PLeatherHappy.png"
        pause 7
        "Nema/PLeatherHappy2.png"
        pause 0.1
        repeat        

    image y neu = "Haruka/YNakedNeutral.png"
    image y hap = "Haruka/YNakedHappy.png"
    image y ang = "Haruka/YNakedAngry.png"
    image y sad = "Haruka/YNakedSad.png"
    image y sur = "Haruka/YNakedSurprised.png"
    image y:
        "Haruka/YGreenNeutral.png"
        pause 7.7 
        "Haruka/YGreenNeutral2.png"
        pause 0.1
        repeat
    image y n:
        "Haruka/YGreenNeutral.png"
        pause 7.7 
        "Haruka/YGreenNeutral2.png"
        pause 0.1
        repeat        
    image y m:
        "Haruka/YGreenAngry.png"
        pause 7.7
        "Haruka/YGreenAngry2.png"
        pause 0.1
        repeat       
    image y s:
        "Haruka/YGreenSad.png"
        pause 7.7 
        "Haruka/YGreenSad2.png"
        pause 0.1
        repeat
    image y su:
        "Haruka/YGreenSurprised.png"
        pause 7.7 
        "Haruka/YGreenSurprised2.png"
        pause 0.1
        repeat
    image y h:
        "Haruka/YGreenHappy.png"
        pause 7.7 
        "Haruka/YGreenHappy2.png"
        pause 0.1
        repeat        

    image r neu = "Hei/RNakedNeutral.png"
    image r hap = "Hei/RNakedHappy.png"
    image r ang = "Hei/RNakedAngry.png"
    image r sad = "Hei/RNakedSad.png"
    image r sur = "Hei/RNakedSurprised.png"
    image r:
        "Hei/RCasualNeutral.png"
        pause 8.3
        "Hei/RCasualNeutral2.png"
        pause 0.1
        repeat
    image r n:
        "Hei/RCasualNeutral.png"
        pause 8.3
        "Hei/RCasualNeutral2.png"
        pause 0.1
        repeat        
    image r m:
        "Hei/RCasualAngry.png"
        pause 8.3
        "Hei/RCasualAngry2.png"
        pause 0.1
        repeat
    image r s:
        "Hei/RCasualSad.png"
        pause 8.3
        "Hei/RCasualSad2.png"
        pause 0.1
        repeat
    image r su:
        "Hei/RCasualSurprised.png"
        pause 8.3
        "Hei/RCasualSurprised2.png"
        pause 0.1
        repeat
    image r h:
        "Hei/RCasualHappy.png"
        pause 8.3
        "Hei/RCasualHappy2.png"
        pause 0.1
        repeat        

    # A character object. This object lets us have the character say
    # dialogue without us having to repeatedly type their name. It also
    # lets us change the color of their name.
    
    $ e = Character('Eileen', color=(200, 255, 200, 255))

    $ p = Character('Nema', image="p", color=(255, 100, 255, 255), ctc="ctc_blink", ctc_position="nestled")
    $ y = Character('Haruka', image="y", color=(240, 240, 0, 255), ctc="ctc_blink", ctc_position="nestled")
    $ r = Character('Hei', image="r", color=(0, 0, 255, 255), ctc="ctc_blink", ctc_position="nestled")
    $ m = Character('Player', color=(150,255,150,255))
    $ d = Character('Demon', color=(255, 0, 0, 255))
    $ ma = Character('Marsh', color=(150,150,150,255))
    $ e = Character(what_color="#ffffff", window_background="gui/narrator.png")
    
    image ctc_blink:
        "ctc01.png"
        linear 0.5 alpha 1.0
        "ctc03.png"
        linear 0.5 alpha 0.3
        repeat
        
   