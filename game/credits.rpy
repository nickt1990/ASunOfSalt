label credits:
    $ persistent.credits = True
    $ _game_menu_screen = None
    $ _dismiss_pause = False
    $ _skipping = False
    $ _rollback = False
    image splash = Text("{size=90}Company Name", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theend
    with dissolve
    with Pause(credits_speed -4)
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    return

init python:
    credits = ('Direction/Writing/Programming/Music', 'Nick Bemiss'), ('Backgrounds', 'Dorktwerp'), ('Sprites and CG', 'Ballclown'), ('GUI', 'Cuddlywad'), ('Writing', 'Dorktwerp'), ('Writing', 'Fingerpookie'), ('Programming', 'Dorktwerp'), ('Music', 'Grumblemuck'), ('Music', 'Headwookum')
    credits_s = "{size=80}Game Title or Logo\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()