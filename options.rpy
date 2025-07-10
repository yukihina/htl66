## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Hard to Love")
define config.layers = ['master', 'background', 'texture', 'middle', 'forward', 'transient', 'screens', 'overlay', 'states', 'notifications']

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.25"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HardtoLove"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/hard-to-love.opus"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.6)
define config.window_hide_transition = Dissolve(.6)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15



## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "HardtoLove-1710312783"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    # ------------------------------------------------------------------------------
    # ARCHIVE DEFINITIONS 
    # ------------------------------------------------------------------------------
    # Define archives that will be created (all using "all" distribution)
    build.archive("scripts", "all")      # Base scripts go to scripts.rpa
    build.archive("wt", "all")           # DLC scripts (walkthrough) go to wt.rpa 
    build.archive("patch", "all")        # Patch script goes to patch.rpa
    build.archive("fonts", "all")        # Fonts go to fonts.rpa

    build.archive("audio_sfx", "all")    # SFX goes to audio_sfx.rpa
    build.archive("audio_music", "all")  # Music goes to audio_music.rpa

    build.archive("gui", "all")          # GUI goes to gui.rpa

    build.archive("images_ep1", "all")
    build.archive("images_ep2", "all")
    build.archive("images_ep3", "all")
    build.archive("images_ep4", "all")
    build.archive("images_ep5", "all")

    build.archive("images_achiev", "all")   # achievements, sms, title
    build.archive("images_common", "all")   # mainmenubg, overlay, wipes, common

    # ------------------------------------------------------------------------------
    # IGNORE / EXCLUDE FILES
    # ------------------------------------------------------------------------------
    # Files that won't be included in any distribution
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.md', None)
    build.classify('**.ini', None)
    build.classify('**.rst', None)
    build.classify('**.log', None)
    build.classify('**.txt', None)
    build.classify('**.rpyx', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/cache/**', None)
    build.classify('game/scripts/deprecated/**', None)
    build.classify('**.json', None)
    build.classify('**.gitignore', None)
    build.classify('**.gitattributes', None)
    build.classify('.git/**', None)
    build.classify('.vscode/**', None)

    # Exclude source .rpy files
    build.classify('**.rpy', None)

    # ------------------------------------------------------------------------------
    # CLASSIFY FILES INTO DISTRIBUTIONS
    # ------------------------------------------------------------------------------
    # Note: Order matters! More specific patterns should come first

    # Special scripts - must be before general scripts classification
    build.classify("game/wt_*.rpyc", "wt")
    build.classify("game/patch.rpyc", "patch")

    # Base scripts
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.py", "scripts")
    build.classify("game/**.rpym", "scripts")

    # Fonts
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")

    # Audio - SFX
    build.classify("game/audio/**.ogg", "audio_sfx")
    build.classify("game/audio/**.mp3", "audio_sfx")
    build.classify("game/audio/**.wav", "audio_sfx")
    build.classify("game/audio/**.opus", "audio_sfx")

    build.classify("game/sfx/**.ogg", "audio_sfx")
    build.classify("game/sfx/**.mp3", "audio_sfx")
    build.classify("game/sfx/**.wav", "audio_sfx")
    build.classify("game/sfx/**.opus", "audio_sfx")

    # Audio - Music
    build.classify("game/music/**.ogg", "audio_music")
    build.classify("game/music/**.mp3", "audio_music")
    build.classify("game/music/**.wav", "audio_music")
    build.classify("game/music/**.opus", "audio_music")

    # GUI
    build.classify("game/gui/**", "gui")

    # Episode Images
    build.classify("game/images/ep1/**", "images_ep1")
    build.classify("game/images/ep2/**", "images_ep2")
    build.classify("game/images/ep3/**", "images_ep3")
    build.classify("game/images/ep4/**", "images_ep4")
    build.classify("game/images/ep5/**", "images_ep5")

    # Achievement/SMS/Title Images
    build.classify("game/images/achievements/**", "images_achiev")
    build.classify("game/images/sms/**", "images_achiev")
    build.classify("game/images/title/**", "images_achiev")

    # Common Images
    build.classify("game/images/mainmenubg/**", "images_common")
    build.classify("game/images/overlay/**", "images_common")
    build.classify("game/images/wipes/**", "images_common")
    build.classify("game/images/common/**", "images_common")
    build.classify("game/images/memories/**", "images_common")

    # ------------------------------------------------------------------------------
    # FALLBACK CLASSIFICATION
    # ------------------------------------------------------------------------------
    # Any unmatched files will go to scripts.rpa
    build.classify("game/**", "scripts")