## screen_extras.rpy
## Core extras menu - This file contains the main navigation and rarely changes

## Define hover animations for the extras buttons
transform extras_button_hover:
    on hover:
        easein 0.2 xoffset 5 yoffset -5
    on idle:
        easeout 0.2 xoffset 0 yoffset 0

## Extras Menu Screen - Main hub for all extras content
screen extras():
    tag menu

    use game_menu(_("Extras"), scroll="viewport"):
        style_prefix "extras"

    if main_menu:
        add "gui/mmtitle_extras.png" ypos 151 xpos 1358 at igm_appear_fg
    else:
        null
    
    ## Main menu content
    vbox:
        spacing 50
        xalign 0.5
        yalign 0.5
        
        hbox:
            spacing 100
            xalign 0.5
            
            ## Replay Gallery Button
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
            
            ## Memories Button
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
            
            ## Music Player Button
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

## Common styles for all extras screens
style extras_button_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    hover_color "#27dc95"

style extras_wip_text:
    kerning 0
    size 30
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"