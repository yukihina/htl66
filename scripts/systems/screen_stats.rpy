# Documentation for the Ren'Py Character Statistics Screen System
# ---------------------------------------------------------------

# Purpose:
# This script implements screens to display and manage character statistics,
# allowing players to view detailed information about game characters.

# Main Components:
# 1. Style Definitions:
#    - Define visual styles for various elements of the stats screen.

# 2. character_positions Dictionary:
#    - Stores position information for character tabs.

# 3. Screens:
#    - stats_button: Button to open the stats screen.
#    - li_stats: Main stats screen showing character selection.
#    - li_stats_secondary: Displays detailed stats for a selected character.
#    - mc_stats: Specific screen for main character stats.

# Detailed Usage:
# 1. Showing the Stats Button:
#    show screen stats_button

# 2. Displaying Character Stats:
#    The li_stats screen is shown when the stats button is clicked.
#    Players can then select a character to view detailed stats.

# 3. Updating Character Info:
#    Character stats are pulled from the game's relationship management system (RM).

# Connections to Other Files:
# - Interacts closely with core.rpy for character data.
# - Uses character images defined in your image assets.
# - Relies on styles defined in gui.rpy and screens.rpy.

# Maintenance and Expansion:
# - When adding new characters, update the character_positions dictionary.
# - To add new stats, modify the li_stats_secondary screen and ensure the RM system tracks these stats.

# Note for Novices:
# - The 'selected_character' variable keeps track of which character's stats are being viewed.
# - The 'at' statement applies transforms for visual effects when showing screen elements.

# Remember: The stats screen provides valuable information to players about their 
# progress and relationships in the game. Ensure it's easy to navigate and understand.

style stats_name is text:
    kerning 0
    size 72
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"

style stats_age is text:
    kerning 0
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#ff9661"

style stats_weight is text:
    kerning 0
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#35d7ea"

style stats_height is text:
    kerning 0
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"

style stats_none is text:
    kerning 0
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#545454"

style stats_menu is text:
    kerning 0
    textalign 0.5
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#545454"

style stats_measure is text:
    kerning 0
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#eea835"

style stats_bio is text:
    xmaximum 365 
    kerning 0
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#b2b2b2"
    justify True

style stats_tab_text is text:
    kerning 0
    size 26
    hover_color "#ff9661"
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#545454"


define character_positions = {
    "mc": (205, 331),
    "amber": (180, 341),
    "antonella": (155, 351),
    "arlette": (174, 361),
    "elizabeth": (156, 371),
    "isabella": (168, 381),
    "kanae": (182, 391),
    "madison": (167, 401),
    "nanami": (172, 411),
    "paz": (198, 421),
}

default selected_character = None

screen stats_button():
    zorder 200
    imagebutton:
        xpos 1806
        ypos 55
        idle "gui/stats_off.png"
        hover "gui/stats_on.png"
        action Show("li_stats")

screen li_stats():
    modal True
    # -- CHAR MENU
    vbox:
        xpos 2
        for li_name in ["mc", "amber", "antonella", "arlette", "elizabeth", "isabella", "kanae", "madison", "nanami", "paz"]:
            $ xpos, ypos = character_positions.get(li_name, (0, 0)) 

            imagebutton at igm_appear:
                idle "gui/tab_" + li_name + "_off.png"
                hover "gui/tab_" + li_name + "_on.png"
                selected_idle "gui/tab_" + li_name + "_on.png"
                selected_hover "gui/tab_" + li_name + "_on.png"
                xpos xpos
                ypos ypos
                action [SetVariable("selected_character", li_name), Hide("li_stats_secondary"), Show("li_stats_secondary", li_name=li_name)]
                selected selected_character == li_name
                focus_mask None

    add "gui/popup_bg.png" xpos 236 ypos 84 at igm_appear_bg
    add animated_glitch("igm_logo") xpos 299 ypos 132 at igm_appear
    if not renpy.get_screen("li_stats_secondary"):
        text "Select the character whose stats you want to view \nfrom the menu on the left side of the screen." style "stats_menu"  xalign 0.5 yalign 0.5 at igm_appear

    imagebutton at igm_appear:
        xpos 1554
        ypos 138
        idle "gui/btn_close_on.png"
        hover "gui/btn_close_off.png"
        hover_offset (0, -2)
        action [Hide("li_stats"), Hide("li_stats_secondary")]
        style "igm_button"
        focus_mask None


# Define a default variable for the selected tab
default selected_tab = "bio"
# Variables for storing hover text and position
default icon_hover_description = ""
default icon_hover_xpos = 0
default icon_hover_ypos = 0

screen li_stats_secondary(li_name=None):
    if li_name is None:
        pass
    elif li_name == "mc":
        use mc_stats
    else:
        python:
            li = globals()[li_name]
            trust = rm.get(li_name, "trust")
            corruption = rm.get(li_name, "cor")
            knows = rm.get(li_name, "knows")
            pregnant = rm.get(li_name, "preg")

        # -- CHAR LABEL
        vbox:
            xpos 474
            ypos 294
            add "gui/label_li.png" at igm_appear_fg

        # -- SUBMENU TABS
        hbox:
            xpos 494
            ypos 260
            spacing 30
            textbutton "Bio" text_style "stats_tab_text" at igm_appear_fg action [SetVariable("selected_tab", "bio")]
            textbutton "Stats" text_style "stats_tab_text" at igm_appear_fg action [SetVariable("selected_tab", "sex_stats")]

        # -- CHAR NAME
        vbox:
            xpos 304
            ypos 351
            if knows:
                text "[li.name.upper()]" at igm_appear_fg style "stats_name"
            else:
                text "???" at igm_appear_fg style "stats_name"

        # -- CHAR PIC
        vbox:
            xalign 0.6
            yalign 1.0
            if knows:
                # Use the helper function to get the image based on the current outfit
                add get_character_outfit_pic(li_name) at igm_appear_fg yoffset -220 xoffset -71
                
                # Only show outfit navigation if character has more than one outfit unlocked
                $ unlocked_outfits = wm.get_all_unlocked(li_name)
                if len(unlocked_outfits) > 1:
                    # Outfit navigation buttons
                    hbox:
                        xalign 0.5
                        spacing 180
                        
                        # Previous outfit button
                        imagebutton:
                            idle "gui/btn_prev_off.png"  # Create these navigation button images
                            hover "gui/btn_prev_on.png"
                            hover_offset (0, -2)
                            action Function(wm.prev_outfit, li_name)
                            at igm_appear_fg
                            focus_mask True
                        
                        # Display current outfit number / total unlocked
                        $ current_outfit = wm.get_current(li_name)
                        $ current_index = unlocked_outfits.index(current_outfit) + 1
                        text "[current_index]/[len(unlocked_outfits)]" at igm_appear_fg style "stats_measure"
                        
                        # Next outfit button
                        imagebutton:
                            idle "gui/btn_next_off.png"  # Create these navigation button images
                            hover "gui/btn_next_on.png"
                            hover_offset (0, -2)
                            action Function(wm.next_outfit, li_name)
                            at igm_appear_fg
                            focus_mask True
            else:
                add "gui/char_pic_null.webp" at igm_appear_fg yoffset -220 xoffset -71

        # -- CHAR INFO (Based on selected tab)
        if selected_tab == "bio":
            # -- BIO TAB CONTENT
            vbox:
                xpos 310
                ypos 444
                if knows:
                    text "[li.age] YEARS OLD" at igm_appear_fg style "stats_age"
                    null height 10
                    hbox:
                        text "[li.height.upper()]" at igm_appear_fg style "stats_height"
                        null width 8
                        text "&" at igm_appear_fg style "stats_none"
                        null width 8
                        text "[li.weight.upper()]" at igm_appear_fg style "stats_weight"
                    null height 10
                    text "[li.measurements.upper()]" at igm_appear_fg style "stats_measure"
                    null height 10
                    text "[li.info]" at igm_appear_fg style "stats_bio"
                else:
                    text "???" at igm_appear_fg style "stats_age"
                    null height 10
                    text "???" at igm_appear_fg style "stats_height"
                    null width 8
                    text "???" at igm_appear_fg style "stats_none"
                    null width 8
                    text "???" at igm_appear_fg style "stats_weight"
                    null height 10
                    text "???" at igm_appear_fg style "stats_measure"
                    null height 10
                    text "???" at igm_appear_fg style "stats_bio"
        else:
            # -- SEX STATS TAB CONTENT
            vbox:
                xpos 310
                ypos 444
                spacing 15
                if knows:
                    python:
                        sex_data = [
                            ("Anal", ss.get(li_name, "anal")),
                            ("Assjob", ss.get(li_name, "assjob")),
                            ("Blowjob", ss.get(li_name, "blowjob")),
                            ("Creampie", ss.get(li_name, "creampie")),
                            ("Pussyjob", ss.get(li_name, "pussyjob")),
                            ("Sex", ss.get(li_name, "sex")),
                            ("Titjob", ss.get(li_name, "titjob"))
                        ]
                    
                    hbox:
                        text "SEXUAL EXPERIENCE" at igm_appear_fg style "stats_age"
                    
                    null height 10
                    
                    # Fixed display of sex stats
                    for stat_name, stat_value in sex_data:
                        hbox at igm_appear_fg:
                            spacing 50
                            text stat_name style "stats_measure" min_width 150
                            text str(stat_value) style "stats_weight"
                else:
                    text "???" at igm_appear_fg style "stats_bio"

        # -- CHAR TRAITS (with updated xpos)
        hbox:
            ypos 322
            xpos 1329
            if knows:
                # Strikes (Heart icon) - States 0-3
                $ strike_count = ss.get(li_name, "strike") if li_name != "mc" else 0
                $ strike_xpos = 1329
                $ strike_ypos = 322
                
                if strike_count == 0:
                    imagebutton:
                        idle "gui/strike_0.png"
                        hover "gui/strike_0.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + " has not been emotionally hurt yet. A relationship is still possible."), 
                                 SetVariable("icon_hover_xpos", strike_xpos), 
                                 SetVariable("icon_hover_ypos", strike_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                elif strike_count == 1:
                    imagebutton:
                        idle "gui/strike_1.png"
                        hover "gui/strike_1.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + " has been slightly hurt. Be careful with your choices."),
                                 SetVariable("icon_hover_xpos", strike_xpos), 
                                 SetVariable("icon_hover_ypos", strike_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                elif strike_count == 2:
                    imagebutton:
                        idle "gui/strike_2.png"
                        hover "gui/strike_2.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + "'s heart has been significantly damaged. Your relationship is in jeopardy."),
                                 SetVariable("icon_hover_xpos", strike_xpos), 
                                 SetVariable("icon_hover_ypos", strike_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                else:  # 3 or more
                    imagebutton:
                        idle "gui/strike_3.png"
                        hover "gui/strike_3.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", "You've completely broken " + li.name + "'s heart. A romantic path may no longer be possible."),
                                 SetVariable("icon_hover_xpos", strike_xpos), 
                                 SetVariable("icon_hover_ypos", strike_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                
                null width 32
                
                # Pregnancy status
                $ preg_xpos = 1329 + 32 + 48  # Strike width + null width
                $ preg_ypos = 322
                
                if pregnant:
                    imagebutton:
                        idle "gui/preg_on.png"
                        hover "gui/preg_on.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + " is pregnant."),
                                 SetVariable("icon_hover_xpos", preg_xpos), 
                                 SetVariable("icon_hover_ypos", preg_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                else:
                    imagebutton:
                        idle "gui/preg_off.png"
                        hover "gui/preg_off.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + " is not pregnant."),
                                 SetVariable("icon_hover_xpos", preg_xpos), 
                                 SetVariable("icon_hover_ypos", preg_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                
                null width 32
                
                # Virgin status
                $ virgin_xpos = 1329 + 32 + 48 + 32 + 48  # Strike + null + preg + null width
                $ virgin_ypos = 322
                
                $ is_virgin = ss.get(li_name, "virgin") if li_name != "mc" else False
                if is_virgin:
                    imagebutton:
                        idle "gui/virgin_on.png"
                        hover "gui/virgin_on.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + " is still a virgin."),
                                 SetVariable("icon_hover_xpos", virgin_xpos), 
                                 SetVariable("icon_hover_ypos", virgin_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
                else:
                    imagebutton:
                        idle "gui/virgin_off.png"
                        hover "gui/virgin_off.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered [SetVariable("icon_hover_description", li.name + " is not a virgin."),
                                 SetVariable("icon_hover_xpos", virgin_xpos), 
                                 SetVariable("icon_hover_ypos", virgin_ypos)]
                        unhovered SetVariable("icon_hover_description", "")
                        focus_mask True
            else:
                null

        # -- CHAR CORRUPTION / LOVE
        vbox:
            xpos 1449
            ypos 475
            if knows:
                if corruption >= 0 and corruption <= 16:
                    add "gui/cor_0.png" at igm_appear_fg
                elif corruption >= 17 and corruption <= 32:
                    add "gui/cor_1.png" at igm_appear_fg
                elif corruption >= 33 and corruption <= 48:
                    add "gui/cor_2.png" at igm_appear_fg
                elif corruption >= 49 and corruption <= 64:
                    add "gui/cor_3.png" at igm_appear_fg
                elif corruption >= 65 and corruption <= 80:
                    add "gui/cor_4.png" at igm_appear_fg
                elif corruption >= 81 and corruption <= 100:
                    add "gui/cor_5.png" at igm_appear_fg
                
                null height 23
                
                if trust >= 0 and trust <= 16:
                    add "gui/love_0.png" at igm_appear_fg
                elif trust >= 17 and trust <= 32:
                    add "gui/love_1.png" at igm_appear_fg
                elif trust >= 33 and trust <= 48:
                    add "gui/love_2.png" at igm_appear_fg
                elif trust >= 49 and trust <= 64:
                    add "gui/love_3.png" at igm_appear_fg
                elif trust >= 65 and trust <= 80:
                    add "gui/love_4.png" at igm_appear_fg
                elif trust >= 81 and trust <= 100:
                    add "gui/love_5.png" at igm_appear_fg
            else:
                null
        
        # Show hover text as speech bubble over icon
        if icon_hover_description != "":
            frame:
                # Position the bubble above the icon with offset
                xpos icon_hover_xpos - 75  # Center and adjust for width
                ypos icon_hover_ypos - 85  # Position above the icon
                xmaximum 200
                
                text icon_hover_description:
                    size 16
                    font "fonts/UbuntuTitling-Bold.ttf"
                    color "#545454"  # Black text for bubble
                    text_align 0.5
                    xalign 0.5



screen mc_stats():    
# -- CHAR LABEL
    vbox:
        xpos 474
        ypos 294
        add "gui/label_mc.png" at igm_appear_fg

# -- CHAR NAME
    vbox:
        xpos 304
        ypos 351
        text "[mc_name.upper()]" at igm_appear_fg style "stats_name"

# -- CHAR ALIGNMENT
    vbox:
        xpos 929
        #ypos 627
        yalign 0.5
        if rm.get("mc", "integrity") == 0:
            add "gui/stats_mc_0.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 10:
            add "gui/stats_mc_10.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 20:
            add "gui/stats_mc_20.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 30:
            add "gui/stats_mc_30.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 40:
            add "gui/stats_mc_40.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 50:
            add "gui/stats_mc_50.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 60:
            add "gui/stats_mc_60.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 70:
            add "gui/stats_mc_70.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 80:
            add "gui/stats_mc_80.png" at igm_appear_fg
        elif rm.get("mc", "integrity") <= 90:
            add "gui/stats_mc_90.png" at igm_appear_fg
        else:
            add "gui/stats_mc_100.png" at igm_appear_fg

# -- CHAR INFO
    vbox:
        xpos 310
        ypos 444
        text "[mc.age] YEARS OLD" at igm_appear_fg style "stats_age"
        null height 10
        hbox:
            text "[mc.height.upper()]" at igm_appear_fg style "stats_height"
            null width 8
            text "&" at igm_appear_fg style "stats_none"
            null width 8
            text "[mc.weight.upper()]" at igm_appear_fg style "stats_weight"
        null height 10
        text "[mc.info]" at igm_appear_fg style "stats_bio"


screen walkthrough_icon():
    zorder 200
    if walkthrough_enabled:
        imagebutton:
            xpos 1806
            ypos 150
            idle "gui/assist_active.png"
            hover "gui/assist_active_hover.png"
            sensitive renpy.loadable("wt_core.rpyc")
            action If(renpy.loadable("wt_core.rpyc"), Show("walkthrough_options"))
    else:
        imagebutton:
            xpos 1806
            ypos 150
            idle "gui/assist_off.png"
            hover "gui/assist_on.png"
            sensitive renpy.loadable("wt_core.rpyc")
            action If(renpy.loadable("wt_core.rpyc"), Show("walkthrough_options"))
