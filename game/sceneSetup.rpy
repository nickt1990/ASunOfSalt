init:
    # Declare the images that are used in the program.
    # Backgrounds.
    image bg space = "large empty.png"
    image bg rroom =   "e1.png"
    image bg broom =   "e1.png"
    image bg kitchen = "e1.png"
    image bg proom =   "e1.png"
    image bg yroom =   "e1.png"
    image bg bathroom ="e1.png"
    image bg nroom =   "e1.png"
    image bg hall =    "e1.png"
    image bg shipFull = "ship_full.png"
    image shipFull = "ship_full.png"
    image black = Solid((0, 0, 0, 255))#r,b,g,alpha
    image tRed = Solid((255, 0, 0, 100))
    
# ~~~SETTING UP BG SHIP MOVEMENTS~~~
label beginningZoom:
    show shipFull:
        linear 1 zoom 1.3 xalign .369 yalign .020
    return

label blueRoom:
    show shipFull:
        parallel:
            linear 1 xalign .369
        parallel:
            linear 1 yalign .020
    return
    
label redRoom:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .059
        parallel:
            linear 1 yalign .020       
    return
    
label pinkRoom:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .059
        parallel:
            linear 1 yalign .915      
    return
    
label yellowRoom:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .369
        parallel:
            linear 1 yalign .915       
    return
    
label kitchen:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .669
        parallel:
            linear 1 yalign .020      
    return
    
label bathroom:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .685
        parallel:
            linear 1 yalign .915      
    return
    
label navRoom:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .98
        parallel:
            linear 1 yalign .5      
    return
    
label hall:
    show shipFull:
        linear .5     
        parallel:
            linear 1 xalign .5
        parallel:
            linear 1 yalign .48      
    return
