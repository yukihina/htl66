# Documentation for the Ren'Py Episode Title Script
# -------------------------------------------------
# Purpose:
# This script manages the creation and display of episode title screens in a
# Ren'Py visual novel. It provides a dynamic and efficient way to handle
# multiple episode titles with minimal code repetition.

# Main Components:
# 1. episode_data Dictionary:
#    Stores episode numbers as keys and their titles as values.

# 2. Dynamic Image Creation:
#    Automatically creates background images for each episode based on the
#    episode_data dictionary.

# 3. episode_bg_transform:
#    Defines the animation for the episode background images.

# 4. title_logo and title_logo2:
#    Define the title logo images and their animations.

# 5. Styles (title_ep_num and title_ep_name):
#    Define the text styles for the episode number and name display.

# 6. vignette_overlay Screen:
#    Adds a vignette effect to the title screen.

# 7. title Screen:
#    Main screen for displaying the episode title.

# 8. show_episode_title Function:
#    Centralizes the logic for displaying an episode title screen.

# 9. Episode Title Labels:
#    One label per episode (ep01_title, ep02_title, etc.)

# Usage:
# The script automatically sets up episode title screens based on the episode_data dictionary.
# To display an episode title, the game should jump to the corresponding label:
# jump ep01_title

# Adding New Episodes:
# 1. Add a new entry to the episode_data dictionary.
# 2. Create a new background image named "ep{number}_title.png" in the "title/" directory.
# 3. Add a new label following the pattern of existing labels.

# Example for adding episode 5:
# In episode_data dictionary:
#     5: "The New Adventure Begins"
# 
# Create image file:
#     title/ep5_title.png
# 
# Add new label:
#     label ep05_title:
#         $ show_episode_title(5)

# Customization:
# - Modify the episode_bg_transform to change the background animation.
# - Adjust the styles (title_ep_num and title_ep_name) to change text appearance.
# - Modify the title screen to change the layout or add new elements.
# - Update the show_episode_title function if you need to change the behavior
#   of how episode titles are displayed.

# File Structure:
# - Episode background images should be in the "title/" directory.
# - Image files should be named "ep{number}_title.png".

# Performance Note:
# This script creates images dynamically at init, which may impact initial loading time
# for a large number of episodes. However, it ensures efficient memory usage and quick
# access during gameplay.

# Maintenance:
# When updating this script, ensure that:
# 1. New episodes are added to the episode_data dictionary.
# 2. Corresponding background images are added to the "title/" directory.
# 3. Any changes to the title screen layout or animation are reflected in the
#    title screen and episode_bg_transform.

# Dependencies:
# This script assumes the existence of certain functions and assets:
# - playAudio function for playing audio
# - smoke transition
# - eigengrau image or color
# - animated_glitch function for logo animation
# - heartbeat transform for vignette effect

# Remember: Ensure all referenced assets (images, fonts, etc.) exist in your project.
# This script only defines the episode title system, not the entire game structure or other screens.

init python:
    episode_data = {
        1: "In the Realm of Past and Dreams",
        2: "A Glimmer in the Darkness",
        3: "Flirting with the Past",
        4: "Blossoming Innocence",
        5: "Beautiful Scars"
        # Add more episode titles here as needed
    }

    # Dynamically create episode background images
    for ep_num in episode_data.keys():
        renpy.image("ep{}_tbg".format(ep_num), 
                    Transform("title/ep{}_title.avif".format(ep_num),
                              subpixel=True,
                              zoom=1))

# Define the ATL transform as specified
transform episode_bg_transform:
    subpixel True
    zoom 0.5
    block:
        zoom 0.5
        linear 60 zoom 1.0
        pause 0.1
        linear 60 zoom 0.5
        pause 0.1
        repeat

image title_logo:
    "title/title_logo.webp"
    alpha 1.0

image title_logo2:
    "title/title_logo.webp"
    alpha 0.7
    linear 4 alpha 0.35
    pause 0.1
    linear 4 alpha 0.7
    pause 0.1
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

screen vignette_overlay():
    add "vignette" xalign 0.5 yalign 0.5 at heartbeat(1,1.4,0.7), igm_appear_nowait

screen title(ep_num, ep_name, ep_label):
    modal True
    add "ep{}_tbg".format(ep_num) at episode_bg_transform xalign 0.5 yalign 0.5
    imagebutton:
        idle animated_glitch("title_logo2")
        hover animated_glitch("title_logo")
        ypos 367
        xpos 622
        action [Hide("title"), Hide("vignette_overlay"), Jump(ep_label)]
        hovered Show("vignette_overlay")
        unhovered Hide("vignette_overlay")
    text "episode {}".format(ep_num).upper() style "title_ep_num" xalign 0.5 ypos 238
    text ep_name.upper() style "title_ep_name" xalign 0.5 ypos 814

init python:
    def show_episode_title(ep_num):
        renpy.hide_screen("stats_button")
        renpy.hide_screen("walkthrough_icon")
        store.quick_menu = False
        store.config.rollback_enabled = False
        renpy.scene()
        renpy.show("eigengrau")
        renpy.transition(smoke)
        store.playAudio(title_theme, "music", 1, True, 0.5, 0)
        renpy.show_screen("title", ep_num, episode_data[ep_num], "ep{:02d}_start".format(ep_num))
        renpy.pause()

label ep01_title:
    $ show_episode_title(1)

label ep02_title:
    $ show_episode_title(2)

label ep03_title:
    $ show_episode_title(3)

label ep04_title:
    $ show_episode_title(4)

label ep05_title:
    $ show_episode_title(5)
