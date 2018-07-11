init:
    # Set up the size of the screen, and the window title.
    #$ config.screen_width = 800
    #$ config.screen_height = 600
    $ config.window_title = "ASoS"
    
    transform midright:
        xpos 0.6
    transform midleft:
        xpos 0.05
        
    
# The start label marks the place where the main menu jumps to to
# begin the actual game.

label start:

    stop music fadeout 2.0
    
    $ renpy.clear_game_runtime()        

    show bg space:
        xalign 1
        #linear 1 xalign 0
    
    show shipFull at truecenter:
        zoom .10
        parallel:
            xalign .5
            linear 1.5 xalign .507
            linear 1 xalign .495
            linear 1 xalign .5
            repeat
        parallel:
            yalign 0.55
            linear 1 yalign 0.51
            linear 1 yalign 0.495
            linear 1 yalign 0.55            
            repeat


    # Store the current version of Ren'Py into a variable, so we can
    # interpolate it into the next line.
    $ version = renpy.version()
    
    call dayOneCard from _call_dayOneCard
    call day1 from _call_day1
    
    call dayTwoCard from _call_dayTwoCard    
    call day2 from _call_day2
    call day2Night from _call_day2Night
    
    call dayThreeCard from _call_dayThreeCard
    call day3 from _call_day3
    
    call dayFourCard from _call_dayFourCard
    call day4 from _call_day4
    call day4Night from _call_day4Night
    
    call dayFiveCard from _call_dayFiveCard
    call day5 from _call_day5
    
    call daySixCard from _call_daySixCard
    call day6 from _call_day6
    call day6Night from _call_day6Night
    
    call daySevenCard from _call_daySevenCard
    call day7 from _call_day7
    
    call dayEightCard from _call_dayEightCard
    call day8 from _call_day8
    
    call dayNineCard from _call_dayNineCard
    call day9 from _call_day9    
    call day9Night from _call_day9Night
    
    call day10 from _call_day10
    
    call day10Night from _call_day10Night
    
    call day11 from _call_day11
    
    call day11Night from _call_day11Night
    
    call day12 from _call_day12
    
    call day13 from _call_day13
    
    call day14 from _call_day14
    
    call day15 from _call_day15
    
    
    #call endings

    $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    "Your playtime is %(minutes)d minutes and %(seconds)d seconds."
    
       
    $ renpy.full_restart()

init:

    # Change some styles, to add images in the background of
    # the menus and windows.
    $ style.mm_root_window.background = Image("mainmenu.jpg")
    $ style.gm_root_window.background = Image("gamemenu.jpg")
    $ style.window.background = Frame("frame.png", 25, 25)

    # Change the look of the slider.
    $ style.bar.left_gutter = 10
    $ style.bar.right_gutter = 12
    $ style.bar.left_bar = Frame("slider_full.png", 10, 0)
    $ style.bar.right_bar = Frame("slider_empty.png", 12, 0)
    $ style.bar.thumb = Image("slider_idle.png")
    $ style.bar.hover_thumb = Image("slider_hover.png")
    $ style.bar.thumb_shadow = Image("slider_shadow.png")
    $ style.bar.thumb_offset = -10

    # Change some styles involving the margins and padding of the
    # default window. (We need this, as we use a frame image that
    # includes a drop-shadow.)
    $ style.window.xmargin = 0
    $ style.window.ymargin = 0
    $ style.window.xpadding = 20
    $ style.window.top_padding = 5
    $ style.window.bottom_padding = 15

    # Interface sounds, just for the heck of it.
    #$ style.button.activate_sound = 'click.wav'
    #$ style.imagemap.activate_sound = 'click.wav'
    #$ library.enter_sound = 'click.wav'
    #$ library.exit_sound = 'click.wav'
    #$ library.sample_sound = "18005551212.wav"

    # Select the transitions that are used when entering and exiting
    # the game menu.
    $ library.enter_transition = fade
    $ library.exit_transition = fade

# The splashscreen is called, if it exists, before the main menu is
# shown the first time. It is not called if the game has restarted.

# We'll comment it out for now.
#
# label splashscreen:
#     scene black
#     show text "American Bishoujo Presents..." with dissolve
#     $ renpy.pause(1.0)
#     hide text with dissolve
#
#     return