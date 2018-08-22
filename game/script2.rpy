init:
    # Set up the size of the screen, and the window title.
    #$ config.screen_width = 800
    #$ config.screen_height = 600
    $ config.window_title = "TPC"
        
    
# The start label marks the place where the main menu jumps to to
# begin the actual game.

label start:
    define randomeSceneNum = 0

#####CHARACTER STATS#################################################
    define com = 0
    define int = 0
    define phy = 0
    define hap = 0
    define lov = 0
	define mod = 10

###################################
#####0 = (+com)conversation
#####1 = (+int)study
#####2 = (+phy)exercise
#####3 = (+art)art
#####4 = (-str)shop
#####5 = (-str)play
	define typeOfActivity = 0
###################################
#####0 = bad
#####1 = fine
#####2 = great
    define typeOfMood = 0

python:
    if mod < 10
        typeOfMood = 0
    if mod < 29
        typeOfMood = 1
    if mod > 30
        typeOfMood = 2

#####################################################################

    $ renpy.clear_game_runtime()        

    show bg space:
        xalign 1
        #linear 1 xalign 0

    # Store the current version of Ren'Py into a variable, so we can
    # interpolate it into the next line.
    $ version = renpy.version()
	
	## todo, a and b parameters will be based on x,y,z (typeOfEvent,typeOfActivity,Mood)
	## find way to make this more reusable.
	## Special scenes use different call
	## this is for if normal call
	## typeofmood = 1, study, between 1-100
	## typeofmood = 2, study, between 2-200
	## typeofmood = 3, study, between 3-300
	##etc
    randomeSceneNum = renpy.random.randint(0, 50)
    
	
    
    label END:

    #$ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)
    #"Your playtime is %(minutes)d minutes and %(seconds)d seconds."
    
    call credits from _call_credits
       
    #$ renpy.full_restart()

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
    $ style.button.activate_sound = 'sounds/Option.ogg'
    $ style.imagemap.activate_sound = 'sounds/Option.ogg'
    $ library.enter_sound = 'sounds/OpenMenu.ogg'
    $ library.exit_sound = 'sounds/CloseMenu.ogg'
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