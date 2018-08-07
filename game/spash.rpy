image splash = "large empty.png"

label splashscreen:
    scene black 
    with Pause(1.5)
    
    play sound "sounds/DoorOpen.ogg"

    show splash with dissolve
    with Pause(1.5)
    
    scene black with dissolve
    with Pause(0.5)

    return