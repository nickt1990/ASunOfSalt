image splash = "SplashScreen.png"

label splashscreen:
    scene black 
    $ renpy.pause(1.5, hard=True)
    
    play sound "sounds/Splash.ogg"

    show splash with dissolve
    $ renpy.pause(1.5, hard=True)
    
    scene black with dissolve
    $ renpy.pause(0.4, hard=True)

    return