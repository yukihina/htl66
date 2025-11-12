## screen_ep_titles.rpy
## Episode Title System - Modular and Robust Version
##
## HOW IT WORKS:
## 1.  CENTRAL CONFIGURATION: Everything is managed from the 'episode_data' dictionary.
##     To add an episode, you only need to add a new entry.
##
## 2.  SIMPLE USAGE: To display a title screen, simply use:
##     call show_episode_title(1) # For episode 1
##     call show_episode_title(2) # For episode 2
##
## 3.  FAIL-SAFE TRANSITION: On click, a "controller" screen is used that:
##     a. Immediately stops the video.
##     b. Fades a black layer from transparent to opaque.
##     c. Once the screen is black, it cleans up and jumps to the episode.
##     This 100% prevents visual artifacts and black screens.

################################################################################
## 1. INITIALIZATION AND EPISODE CONFIGURATION
################################################################################

init python:
    # --------------------------------------------------------------------------
    # MODULARITY: THE EPISODE CONTROL CENTER
    # To add a new episode, you only need to add one line here.
    # The system will handle the rest.
    # --------------------------------------------------------------------------
    episode_data = {
        # Number: "Episode Title"
        1: "In the Realm of Past and Dreams",
        2: "A Glimmer in the Darkness",
        3: "Flirting with the Past",
        4: "Blossoming Innocence",
        5: "Beautiful Scars"
        # 6: "A New Beginning",  # <-- Example for episode 6
        # 7: "Shadows of Yesterday",   # <-- Example for episode 7
        # ... and so on for up to 20 or more.
    }

    # --------------------------------------------------------------------------
    # DYNAMIC ASSET CREATION
    # This loop automatically creates the video players for each
    # episode defined in 'episode_data'. You do not need to touch this.
    # --------------------------------------------------------------------------
    for ep_num in episode_data.keys():
        renpy.image(
            "ep{}_tbg_video".format(ep_num),
            Movie(
                channel="ep_bg", # A single channel to easily control it
                play="images/title/ep{}_title.webm".format(ep_num),
                loop=True
            )
        )

################################################################################
## 2. CORE LOGIC AND LABELS
################################################################################

# The main label to call any title screen.
# This is the only way you should call the title screens.
label show_episode_title(episode_number):
    # Hide UI elements we don't want to see
    window hide
    hide screen stats_button
    hide screen walkthrough_icon

    # Disable menus and rollback during the sequence
    $ store.quick_menu = False
    $ store.config.rollback_enabled = False

    # Prepare the scene and music
    scene eigengrau with dissolve
    $ store.playAudio(title_theme, "music", 1, True, 0.5, 0)

    # Show the main title screen, passing it the necessary data
    show screen episode_title_main(
        ep_num=episode_number,
        ep_name=episode_data.get(episode_number, "Unknown Episode"),
        target_label="ep{:02d}_start".format(episode_number)
    )

    # Pause the game and wait for the player to click
    $ renpy.ui.interact()

    # When the player clicks, control will return here.
    # The transition screen will handle hiding everything and jumping.
    return

################################################################################
## 3. SCREENS
################################################################################

# ------------------------------------------------------------------------------
# MAIN TITLE SCREEN
# Displays the background video, text, and interactive logo.
# ------------------------------------------------------------------------------
screen episode_title_main(ep_num, ep_name, target_label):
    modal True

    # Video Background - CORRECTED: Added xalign and yalign to center it.
    add "ep{}_tbg_video".format(ep_num) at episode_bg_transform xalign 0.5 yalign 0.5

    # Interactive Logo
    imagebutton:
        idle animated_glitch("title_logo2")
        hover animated_glitch("title_logo")
        ypos 367
        xpos 622
        # KEY ACTION: On click, it only shows the controller screen.
        # This is the only action, which makes it simple and robust.
        action Show("ep_title_transition_controller", target_label=target_label)
        hovered Show("vignette_overlay")
        unhovered Hide("vignette_overlay")

    # Title Texts
    text "episode {}".format(ep_num).upper() style "title_ep_num" xalign 0.5 ypos 238
    text ep_name.upper() style "title_ep_name" xalign 0.5 ypos 814

# ------------------------------------------------------------------------------
# TRANSITION CONTROLLER SCREEN (THE DEFINITIVE SOLUTION)
# This screen handles all transition logic to prevent errors.
# ------------------------------------------------------------------------------
screen ep_title_transition_controller(target_label):
    modal True
    zorder 200 # Ensures it is on top of everything

    # 1. On show, its FIRST action is to stop the video.
    on "show" action Stop("ep_bg")

    # 2. Displays a black background that fades in from 0% to 100% opacity.
    add "eigengrau" at fade_in(0.5)

    # 3. A timer waits for the fade animation to finish (0.5s).
    timer 0.5 action [
        # 4. Once the screen is black, it cleans everything up...
        Hide("episode_title_main"),
        Hide("vignette_overlay"),
        Hide("ep_title_transition_controller"),
        # 5. ...and finally, jumps to the correct destination.
        Jump(target_label)
    ]

# ------------------------------------------------------------------------------
# Vignette screen for the hover effect
# ------------------------------------------------------------------------------
screen vignette_overlay():
    add "vignette" xalign 0.5 yalign 0.5 at heartbeat(1,1.4,0.7), igm_appear_nowait


################################################################################
## 4. DYNAMIC TITLE LOGO IMAGES
################################################################################

image title_logo:
    "images/title/title_logo.webp"
    alpha 1.0

image title_logo2:
    "images/title/title_logo.webp"
    alpha 0.7
    linear 4 alpha 0.35
    pause 0.1
    linear 4 alpha 0.7
    pause 0.1
    repeat


################################################################################
## 5. QUICK ACCESS LABELS (OPTIONAL BUT RECOMMENDED)
################################################################################

# These labels are shortcuts for calling the system from your main script.
# It is cleaner than having `call show_episode_title(X)` throughout your code.

label ep01_title:
    call show_episode_title(1)
    return

label ep02_title:
    call show_episode_title(2)
    return

label ep03_title:
    call show_episode_title(3)
    return

label ep04_title:
    call show_episode_title(4)
    return

label ep05_title:
    call show_episode_title(5)
    return

# When you create episode 6, simply add:
# label ep06_title:
#     call show_episode_title(6)
#     return

################################################################################
## 6. STYLES AND TRANSFORMS (UNCHANGED)
################################################################################

init:
    transform fade_in(duration):
        alpha 0.0
        linear duration alpha 1.0

    transform episode_bg_transform:
        subpixel True
        zoom 1.25
        block:
            zoom 1.25
            linear 60 zoom 1.0
            pause 0.1
            linear 60 zoom 1.25
            pause 0.1
            repeat

    transform heartbeat(start_zoom, end_zoom, duration):
        zoom start_zoom
        linear duration zoom end_zoom
        linear duration zoom start_zoom
        repeat

style title_ep_num:
    kerning 0
    size 24
    font "fonts/quicksand.ttf"
    color "#bbc7b5"
    outlines [ (2, "#321414", 0, 0) ]

style title_ep_name:
    kerning 0
    size 26
    font "fonts/quicksand.ttf"
    color "#bbc7b5"
    outlines [ (2, "#321414", 0, 0) ]