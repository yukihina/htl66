## screen_ep_titles.rpy
## Episode Title System for Ren'Py - Complete English Version
## 
## How to use:
## This script manages the creation and display of episode title screens in a
## Ren'Py visual novel. It provides a dynamic and efficient way to handle
## multiple episode titles with minimal code repetition.
## 
## To display an episode title, the game should jump to the corresponding label:
## jump ep01_title
## 
## The system automatically:
## - Creates background images for each episode dynamically
## - Handles audio transitions and UI state management
## - Provides interactive title screens with hover effects
## - Manages scene transitions and rollback settings
##
## Episode Structure:
## - Each episode has a number, title, and background image
## - Title screens feature animated backgrounds and interactive logos
## - Clicking the logo advances to the episode start
## - Hover effects add visual feedback and immersion
##
## Adding New Episodes:
## 1. Add a new entry to the episode_data dictionary
## 2. Create a new background image named "ep{number}_title.avif"
## 3. Add a new label following the pattern of existing labels
## 4. The system automatically creates the necessary dynamic images

################################################################################
## INITIALIZATION
################################################################################

init python:
    ############################################################################
    ## EPISODE DATA CONFIGURATION
    ############################################################################
    
    episode_data = {
        1: "In the Realm of Past and Dreams",
        2: "A Glimmer in the Darkness",
        3: "Flirting with the Past",
        4: "Blossoming Innocence",
        5: "Beautiful Scars"
        # Add more episode titles here as needed
    }

    ############################################################################
    ## DYNAMIC IMAGE CREATION
    ############################################################################
    
    # Dynamically create episode background images based on episode_data
    for ep_num in episode_data.keys():
        renpy.image("ep{}_tbg".format(ep_num), 
                    Transform("title/ep{}_title.avif".format(ep_num),
                              subpixel=True,
                              zoom=1))

    ############################################################################
    ## EPISODE TITLE HELPER FUNCTIONS
    ############################################################################
    
    def show_episode_title(ep_num):
        """
        Centralized function for displaying episode title screens
        Handles UI state, audio, and screen transitions
        """
        # Hide UI elements that shouldn't appear during title screens
        renpy.hide_screen("stats_button")
        renpy.hide_screen("walkthrough_icon")
        
        # Disable quick menu and rollback during title sequence
        store.quick_menu = False
        store.config.rollback_enabled = False
        
        # Set up scene with fade transition
        renpy.scene()
        renpy.show("eigengrau")
        renpy.transition(smoke)
        
        # Play title theme music
        store.playAudio(title_theme, "music", 1, True, 0.5, 0)
        
        # Show the title screen with episode data
        renpy.show_screen("title", ep_num, episode_data[ep_num], "ep{:02d}_start".format(ep_num))
        renpy.pause()
    
    def get_episode_title(ep_num):
        """Get episode title by number"""
        return episode_data.get(ep_num, "Unknown Episode")
    
    def get_total_episodes():
        """Get total number of available episodes"""
        return len(episode_data)
    
    def episode_exists(ep_num):
        """Check if an episode exists"""
        return ep_num in episode_data

################################################################################
## DYNAMIC TITLE LOGO IMAGES
################################################################################

## Static title logo
image title_logo:
    "title/title_logo.webp"
    alpha 1.0

## Animated title logo with breathing effect
image title_logo2:
    "title/title_logo.webp"
    alpha 0.7
    linear 4 alpha 0.35
    pause 0.1
    linear 4 alpha 0.7
    pause 0.1
    repeat

################################################################################
## TRANSFORMS AND ANIMATIONS
################################################################################

init:
    ## ATL transform for episode background animation
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

    ## Breathing animation for vignette overlay
    transform heartbeat(start_zoom, end_zoom, duration):
        zoom start_zoom
        linear duration zoom end_zoom
        linear duration zoom start_zoom
        repeat

################################################################################
## EPISODE TITLE SCREENS
################################################################################

## Vignette overlay screen for immersive hover effect
screen vignette_overlay():
    add "vignette" xalign 0.5 yalign 0.5 at heartbeat(1,1.4,0.7), igm_appear_nowait

## Main episode title screen
screen title(ep_num, ep_name, ep_label):
    modal True
    
    ## Animated background image
    add "ep{}_tbg".format(ep_num) at episode_bg_transform xalign 0.5 yalign 0.5
    
    ## Interactive title logo
    imagebutton:
        idle animated_glitch("title_logo2")
        hover animated_glitch("title_logo")
        ypos 367
        xpos 622
        action [Hide("title"), Hide("vignette_overlay"), Jump(ep_label)]
        hovered Show("vignette_overlay")
        unhovered Hide("vignette_overlay")
    
    ## Episode number text
    text "episode {}".format(ep_num).upper() style "title_ep_num" xalign 0.5 ypos 238
    
    ## Episode title text
    text ep_name.upper() style "title_ep_name" xalign 0.5 ypos 814

################################################################################
## EPISODE TITLE LABELS
################################################################################

## Episode 1 Title Screen
label ep01_title:
    $ show_episode_title(1)

## Episode 2 Title Screen
label ep02_title:
    $ show_episode_title(2)

## Episode 3 Title Screen
label ep03_title:
    $ show_episode_title(3)

## Episode 4 Title Screen
label ep04_title:
    $ show_episode_title(4)

## Episode 5 Title Screen
label ep05_title:
    $ show_episode_title(5)

################################################################################
## EPISODE TITLE STYLES
################################################################################

## Episode number text style
style title_ep_num:
    kerning 0
    size 24
    font "fonts/quicksand.ttf"
    color "#bbc7b5"
    outlines [ (2, "#321414", 0, 0) ]

## Episode title text style
style title_ep_name:
    kerning 0
    size 26
    font "fonts/quicksand.ttf"
    color "#bbc7b5"
    outlines [ (2, "#321414", 0, 0) ]

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this episode title system in your game:
## 
## 1. Episode titles are displayed by jumping to their corresponding labels:
##    jump ep01_title
##    jump ep02_title
##    etc.
##
## 2. The system automatically:
##    - Hides UI elements during title sequence
##    - Disables quick menu and rollback
##    - Plays title theme music
##    - Transitions to episode start when logo is clicked
##    - Manages scene transitions and effects
##
## 3. To add new episodes:
##    - Add new entry to episode_data dictionary
##    - Create background image: title/ep{number}_title.avif
##    - Add new label: label ep0X_title: $ show_episode_title(X)
##    - The system handles dynamic image creation automatically
##
## 4. Required assets:
##    - Episode background images in title/ directory
##    - Title logo images (title_logo.webp)
##    - Vignette overlay image
##    - Transition effects (smoke, eigengrau)
##    - Font files (quicksand.ttf)
##
## 5. Required functions (should exist in your game):
##    - playAudio() for music management
##    - animated_glitch() for logo animation
##    - smoke transition effect
##    - igm_appear_nowait transform
##
## Example usage in episode flow:
## label start:
##     # Game introduction
##     jump ep01_title
##
## label ep01_start:
##     # Episode 1 content starts here
##     "Welcome to Episode 1!"
##     # ... episode content ...
##     jump ep02_title
##
## label ep02_start:
##     # Episode 2 content starts here
##     "Welcome to Episode 2!"
##     # ... episode content ...
##
## File structure:
## title/
##   ├── ep1_title.avif
##   ├── ep2_title.avif
##   ├── ep3_title.avif
##   ├── ep4_title.avif
##   ├── ep5_title.avif
##   └── title_logo.webp
##
## Customization options:
## - Modify episode_bg_transform for different background animations
## - Adjust title styles for different fonts/colors
## - Change logo positioning and hover effects
## - Add additional UI elements to the title screen
## - Implement different transition effects
##
## Performance considerations:
## - Dynamic image creation happens at init time
## - Background animations use ATL for efficiency
## - Transitions are optimized for smooth gameplay
## - Memory usage scales with number of episodes
##
## Maintenance notes:
## - Keep episode_data dictionary updated with new episodes
## - Ensure background images follow naming convention
## - Test title sequences after adding new episodes
## - Verify audio transitions work correctly
## - Check that episode start labels exist before referencing them