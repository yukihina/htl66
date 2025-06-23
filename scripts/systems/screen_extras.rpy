## screen_extras.rpy
## Extras Menu System - Complete English Version
## 
## How to use:
## The extras menu serves as the main hub for all additional content in the game.
## It provides navigation to replay gallery, memories, music player, and other bonus content.
## 
## To open the extras menu from anywhere in your game:
## textbutton "Extras" action ShowMenu("extras")
## 
## The extras menu features:
## - Animated button hover effects
## - Clean, organized navigation layout
## - Easy integration with other menu systems
## - Responsive design that works from main menu or in-game
##
## Navigation Structure:
## - Replay Gallery: Access to scene replay system
## - Memories: Photo gallery and memory collection
## - Music Player: Character-based music player with slideshow
##
## Adding New Extras:
## 1. Add new imagebutton with idle/hover states
## 2. Add corresponding text label
## 3. Wrap in vbox with proper spacing and animation
## 4. Ensure target screen/menu exists before linking

################################################################################
## INITIALIZATION
################################################################################

init python:
    ############################################################################
    ## EXTRAS MENU CONFIGURATION
    ############################################################################
    
    # Define available extras sections
    extras_sections = {
        "replay_gallery": {
            "title": "REPLAY GALLERY",
            "idle_image": "gui/replay_gallery_idle.png",
            "hover_image": "gui/replay_gallery_hover.png",
            "action": "ShowMenu('replay_gallery')",
            "enabled": True
        },
        "memories": {
            "title": "MEMORIES",
            "idle_image": "gui/memories_idle.png",
            "hover_image": "gui/memories_hover.png",
            "action": "ShowMenu('memories_gallery')",
            "enabled": True
        },
        "music_player": {
            "title": "MUSIC PLAYER",
            "idle_image": "gui/music_player_idle.png",
            "hover_image": "gui/music_player_hover.png",
            "action": "ShowMenu('music_player')",
            "enabled": True
        }
    }
    
    ############################################################################
    ## EXTRAS HELPER FUNCTIONS
    ############################################################################
    
    def get_enabled_extras():
        """Get list of enabled extras sections"""
        return [(key, data) for key, data in extras_sections.items() if data["enabled"]]
    
    def check_extras_availability():
        """Check if extras content is available (for future use)"""
        # This can be expanded to check for unlocked content, DLC, etc.
        return True

################################################################################
## TRANSFORMS AND ANIMATIONS
################################################################################

init:
    ## Hover animations for the extras buttons
    transform extras_button_hover:
        on hover:
            easein 0.2 xoffset 5 yoffset -5
        on idle:
            easeout 0.2 xoffset 0 yoffset 0

    ## Fade-in animation for extras content
    transform extras_fade_in:
        alpha 0.0
        ease 0.5 alpha 1.0

################################################################################
## EXTRAS MENU SCREEN
################################################################################

## Main Extras Menu Screen - Navigation hub for all extras content
screen extras():
    tag menu

    use game_menu(_("Extras"), scroll="viewport"):
        style_prefix "extras"

    ## Main menu title image (only shown when accessed from main menu)
    if main_menu:
        add "gui/mmtitle_extras.png" ypos 151 xpos 1358 at igm_appear_fg
    else:
        null
    
    ## Main menu content container
    vbox:
        spacing 50
        xalign 0.5
        yalign 0.5
        
        ## Horizontal layout for extras buttons
        hbox:
            spacing 100
            xalign 0.5
            
            ## Replay Gallery Section
            vbox at igm_appear_fg:
                spacing 10
                imagebutton:
                    idle "gui/replay_gallery_idle.png"
                    hover "gui/replay_gallery_hover.png"
                    action ShowMenu("replay_gallery")
                    style "igm_button"
                    focus_mask True
                    at extras_button_hover
                text _("REPLAY GALLERY") xalign 0.5 style "extras_button_text"
            
            ## Memories Section
            vbox at igm_appear_fg:
                spacing 10
                imagebutton:
                    idle "gui/memories_idle.png"
                    hover "gui/memories_hover.png"
                    action ShowMenu("memories_gallery")
                    style "igm_button"
                    focus_mask True
                    at extras_button_hover
                text _("MEMORIES") xalign 0.5 style "extras_button_text"
            
            ## Music Player Section
            vbox at igm_appear_fg:
                spacing 10
                imagebutton:
                    idle "gui/music_player_idle.png"
                    hover "gui/music_player_hover.png"
                    action ShowMenu("music_player")
                    style "igm_button"
                    focus_mask True
                    at extras_button_hover
                text _("MUSIC PLAYER") xalign 0.5 style "extras_button_text"

## Work In Progress Screen (for future extras)
screen extras_wip():
    tag menu
    
    use game_menu(_("Work In Progress"), scroll="viewport"):
        style_prefix "extras"
    
    frame:
        xalign 0.5
        yalign 0.5
        background None
        
        vbox:
            spacing 30
            xalign 0.5
            
            text _("COMING SOON") style "extras_wip_title" xalign 0.5
            text _("This feature is currently under development") style "extras_wip_text" xalign 0.5
            
            textbutton _("Return"):
                style "extras_return_button"
                action Return()

################################################################################
## EXTRAS STYLES
################################################################################

## Button text style for extras navigation
style extras_button_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    hover_color "#27dc95"

## Work in progress title style
style extras_wip_title:
    kerning 0
    size 36
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"
    outlines [(1, "#198c5f", 0, 0)]

## Work in progress text style
style extras_wip_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"

## Return button style for WIP screen
style extras_return_button:
    background "gui/button_idle.png"
    hover_background "gui/button_hover.png"
    xsize 200
    ysize 50

style extras_return_button_text:
    kerning 0
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    hover_color "#27dc95"
    xalign 0.5
    yalign 0.5

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this extras menu in your game:
## 
## 1. In your main menu or game menu, add a button like this:
##    textbutton "Extras" action ShowMenu("extras")
##
## 2. The extras menu will automatically:
##    - Display available sections with hover animations
##    - Navigate to specific content menus (replay, memories, music)
##    - Adapt its appearance based on context (main menu vs in-game)
##    - Use consistent styling throughout the interface
##
## 3. To add new extras sections:
##    - Add new entry to extras_sections dictionary
##    - Create corresponding idle/hover button images
##    - Add new vbox section in the extras screen
##    - Ensure target screen exists before linking
##
## 4. Required assets:
##    - Button images for each section (idle/hover states)
##    - Main menu title image (mmtitle_extras.png)
##    - Background and UI elements as needed
##
## 5. This extras system is designed to be:
##    - Easily expandable for future content
##    - Compatible with existing menu systems
##    - Visually consistent with the game's design
##
## Example main menu integration:
## screen main_menu():
##     tag menu
##     style_prefix "main_menu"
##     
##     vbox:
##         textbutton "Start Game" action Start()
##         textbutton "Load Game" action ShowMenu("load")
##         textbutton "Extras" action ShowMenu("extras")
##         textbutton "Settings" action ShowMenu("preferences")
##         textbutton "Quit" action Quit()
##
## Example in-game integration:
## screen game_menu_navigation():
##     vbox:
##         textbutton "Save" action ShowMenu("save")
##         textbutton "Load" action ShowMenu("load")
##         textbutton "Extras" action ShowMenu("extras")
##         textbutton "Settings" action ShowMenu("preferences")
##         textbutton "Return" action Return()
##
## Asset organization:
## gui/
##   ├── replay_gallery_idle.png
##   ├── replay_gallery_hover.png
##   ├── memories_idle.png
##   ├── memories_hover.png
##   ├── music_player_idle.png
##   ├── music_player_hover.png
##   └── mmtitle_extras.png
##
## Future expansion ideas:
## - Achievement gallery integration
## - Behind-the-scenes content
## - Character profiles and bios
## - Developer commentary
## - Concept art gallery
## - Statistics and progress tracking