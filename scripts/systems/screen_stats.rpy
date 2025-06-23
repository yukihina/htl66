## screen_stats.rpy
## Character Statistics System - Complete English Version
## 
## How to use:
## To open the stats screen from anywhere in your game:
## show screen stats_button
## or
## action Show("li_stats")
## 
## The stats system displays character information including:
## - Character biography and physical stats
## - Sexual experience statistics
## - Relationship status (trust/corruption levels)
## - Character traits (pregnancy, virgin status, strikes)
## - Outfit navigation for unlocked costumes
##
## Character Selection:
## Players can select characters from the left side menu to view detailed stats
## The system supports both main character (MC) stats and love interest stats
## Unknown characters show placeholder information until discovered

################################################################################
## INITIALIZATION
################################################################################

init python:
    # Character Statistics State Management
    class StatsState:
        def __init__(self):
            self.selected_character = None
            self.selected_tab = "bio"
            self.icon_hover_description = ""
            self.icon_hover_xpos = 0
            self.icon_hover_ypos = 0
    
    # Create global stats state instance
    if not hasattr(store, 'stats_state'):
        stats_state = StatsState()
    
    ############################################################################
    ## CHARACTER POSITION CONFIGURATION
    ############################################################################
    
    # Character tab positions for the left side menu
    character_positions = {
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
    
    ############################################################################
    ## CHARACTER DATA HELPER FUNCTIONS
    ############################################################################
    
    def get_character_stats_data(li_name):
        """Get character statistics data from relationship management system"""
        if li_name == "mc":
            return {
                "trust": rm.get("mc", "integrity"),
                "corruption": 0,
                "knows": True,
                "pregnant": False,
                "is_virgin": False,
                "strike_count": 0
            }
        else:
            return {
                "trust": rm.get(li_name, "trust"),
                "corruption": rm.get(li_name, "cor"),
                "knows": rm.get(li_name, "knows"),
                "pregnant": rm.get(li_name, "preg"),
                "is_virgin": ss.get(li_name, "virgin"),
                "strike_count": ss.get(li_name, "strike")
            }
    
    def get_character_sex_stats(li_name):
        """Get character sexual experience statistics"""
        return [
            ("Anal", ss.get(li_name, "anal")),
            ("Assjob", ss.get(li_name, "assjob")),
            ("Blowjob", ss.get(li_name, "blowjob")),
            ("Creampie", ss.get(li_name, "creampie")),
            ("Pussyjob", ss.get(li_name, "pussyjob")),
            ("Sex", ss.get(li_name, "sex")),
            ("Titjob", ss.get(li_name, "titjob"))
        ]
    
    def get_corruption_level_image(corruption_value):
        """Get corruption level image based on corruption value"""
        if corruption_value <= 16:
            return "gui/cor_0.png"
        elif corruption_value <= 32:
            return "gui/cor_1.png"
        elif corruption_value <= 48:
            return "gui/cor_2.png"
        elif corruption_value <= 64:
            return "gui/cor_3.png"
        elif corruption_value <= 80:
            return "gui/cor_4.png"
        else:
            return "gui/cor_5.png"
    
    def get_trust_level_image(trust_value):
        """Get trust/love level image based on trust value"""
        if trust_value <= 16:
            return "gui/love_0.png"
        elif trust_value <= 32:
            return "gui/love_1.png"
        elif trust_value <= 48:
            return "gui/love_2.png"
        elif trust_value <= 64:
            return "gui/love_3.png"
        elif trust_value <= 80:
            return "gui/love_4.png"
        else:
            return "gui/love_5.png"
    
    def get_mc_integrity_image(integrity_value):
        """Get MC integrity alignment image based on integrity value"""
        if integrity_value == 0:
            return "gui/stats_mc_0.png"
        elif integrity_value <= 10:
            return "gui/stats_mc_10.png"
        elif integrity_value <= 20:
            return "gui/stats_mc_20.png"
        elif integrity_value <= 30:
            return "gui/stats_mc_30.png"
        elif integrity_value <= 40:
            return "gui/stats_mc_40.png"
        elif integrity_value <= 50:
            return "gui/stats_mc_50.png"
        elif integrity_value <= 60:
            return "gui/stats_mc_60.png"
        elif integrity_value <= 70:
            return "gui/stats_mc_70.png"
        elif integrity_value <= 80:
            return "gui/stats_mc_80.png"
        elif integrity_value <= 90:
            return "gui/stats_mc_90.png"
        else:
            return "gui/stats_mc_100.png"
    
    ############################################################################
    ## STRIKE SYSTEM HELPER FUNCTIONS
    ############################################################################
    
    def get_strike_icon_data(li_name, strike_count):
        """Get strike icon image and description based on strike count"""
        if strike_count == 0:
            return {
                "image": "gui/strike_0.png",
                "description": li_name + " has not been emotionally hurt yet. A relationship is still possible."
            }
        elif strike_count == 1:
            return {
                "image": "gui/strike_1.png",
                "description": li_name + " has been slightly hurt. Be careful with your choices."
            }
        elif strike_count == 2:
            return {
                "image": "gui/strike_2.png",
                "description": li_name + "'s heart has been significantly damaged. Your relationship is in jeopardy."
            }
        else:  # 3 or more
            return {
                "image": "gui/strike_3.png",
                "description": "You've completely broken " + li_name + "'s heart. A romantic path may no longer be possible."
            }
    
    def set_icon_hover(description, xpos, ypos):
        """Set hover tooltip for character trait icons"""
        stats_state.icon_hover_description = description
        stats_state.icon_hover_xpos = xpos
        stats_state.icon_hover_ypos = ypos
    
    def clear_icon_hover():
        """Clear hover tooltip"""
        stats_state.icon_hover_description = ""
    
    ############################################################################
    ## TAB MANAGEMENT FUNCTIONS
    ############################################################################
    
    def set_stats_tab(tab_name):
        """Set the currently selected stats tab"""
        stats_state.selected_tab = tab_name
    
    def set_selected_character(character_name):
        """Set the currently selected character and reset tab"""
        stats_state.selected_character = character_name
        stats_state.selected_tab = "bio"  # Reset to bio tab when changing character

################################################################################
## STATS BUTTON SCREEN
################################################################################

screen stats_button():
    zorder 200
    imagebutton:
        xpos 1806
        ypos 55
        idle "gui/stats_off.png"
        hover "gui/stats_on.png"
        action Show("li_stats")

################################################################################
## MAIN STATS SCREEN
################################################################################

screen li_stats():
    modal True
    
    ## Character selection menu on the left side
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
                action [
                    Function(set_selected_character, li_name),
                    Hide("li_stats_secondary"),
                    Show("li_stats_secondary", li_name=li_name)
                ]
                selected stats_state.selected_character == li_name
                focus_mask None
    
    ## Main background and logo
    add "gui/popup_bg.png" xpos 236 ypos 84 at igm_appear_bg
    add animated_glitch("igm_logo") xpos 299 ypos 132 at igm_appear
    
    ## Initial instructions when no character is selected
    if not renpy.get_screen("li_stats_secondary"):
        text "Select the character whose stats you want to view \nfrom the menu on the left side of the screen." style "stats_menu" xalign 0.5 yalign 0.5 at igm_appear
    
    ## Close button
    imagebutton at igm_appear:
        xpos 1554
        ypos 138
        idle "gui/btn_close_on.png"
        hover "gui/btn_close_off.png"
        hover_offset (0, -2)
        action [Hide("li_stats"), Hide("li_stats_secondary")]
        style "igm_button"
        focus_mask None

################################################################################
## SECONDARY STATS SCREEN (CHARACTER DETAILS)
################################################################################

screen li_stats_secondary(li_name=None):
    if li_name is None:
        pass
    elif li_name == "mc":
        use mc_stats
    else:
        ## Get character data
        python:
            li = globals()[li_name]
            char_data = get_character_stats_data(li_name)
            trust = char_data["trust"]
            corruption = char_data["corruption"]
            knows = char_data["knows"]
            pregnant = char_data["pregnant"]
            is_virgin = char_data["is_virgin"]
            strike_count = char_data["strike_count"]
        
        ## Character label background
        vbox:
            xpos 474
            ypos 294
            add "gui/label_li.png" at igm_appear_fg
        
        ## Tab navigation (Bio / Stats)
        hbox:
            xpos 494
            ypos 260
            spacing 30
            textbutton "Bio" text_style "stats_tab_text" at igm_appear_fg action Function(set_stats_tab, "bio")
            textbutton "Stats" text_style "stats_tab_text" at igm_appear_fg action Function(set_stats_tab, "sex_stats")
        
        ## Character name display
        vbox:
            xpos 304
            ypos 351
            if knows:
                text "[li.name.upper()]" at igm_appear_fg style "stats_name"
            else:
                text "???" at igm_appear_fg style "stats_name"
        
        ## Character image with outfit navigation
        vbox:
            xalign 0.6
            yalign 1.0
            if knows:
                ## Use the helper function to get the image based on the current outfit
                add get_character_outfit_pic(li_name) at igm_appear_fg yoffset -220 xoffset -71
                
                ## Only show outfit navigation if character has more than one outfit unlocked
                $ unlocked_outfits = wm.get_all_unlocked(li_name)
                if len(unlocked_outfits) > 1:
                    ## Outfit navigation buttons
                    hbox:
                        xalign 0.5
                        spacing 180
                        
                        ## Previous outfit button
                        imagebutton:
                            idle "gui/btn_prev_off.png"
                            hover "gui/btn_prev_on.png"
                            hover_offset (0, -2)
                            action Function(wm.prev_outfit, li_name)
                            at igm_appear_fg
                            focus_mask True
                        
                        ## Display current outfit number / total unlocked
                        $ current_outfit = wm.get_current(li_name)
                        $ current_index = unlocked_outfits.index(current_outfit) + 1
                        text "[current_index]/[len(unlocked_outfits)]" at igm_appear_fg style "stats_measure"
                        
                        ## Next outfit button
                        imagebutton:
                            idle "gui/btn_next_off.png"
                            hover "gui/btn_next_on.png"
                            hover_offset (0, -2)
                            action Function(wm.next_outfit, li_name)
                            at igm_appear_fg
                            focus_mask True
            else:
                add "gui/char_pic_null.webp" at igm_appear_fg yoffset -220 xoffset -71
        
        ## Character information display based on selected tab
        if stats_state.selected_tab == "bio":
            ## Biography tab content
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
            ## Sexual statistics tab content
            vbox:
                xpos 310
                ypos 444
                spacing 15
                if knows:
                    $ sex_data = get_character_sex_stats(li_name)
                    
                    hbox:
                        text "SEXUAL EXPERIENCE" at igm_appear_fg style "stats_age"
                    
                    null height 10
                    
                    ## Display sex statistics
                    for stat_name, stat_value in sex_data:
                        hbox at igm_appear_fg:
                            spacing 50
                            text stat_name style "stats_measure" min_width 150
                            text str(stat_value) style "stats_weight"
                else:
                    text "???" at igm_appear_fg style "stats_bio"
        
        ## Character trait icons (strikes, pregnancy, virgin status)
        hbox:
            ypos 322
            xpos 1329
            if knows:
                ## Strike status (Heart icon) - States 0-3
                $ strike_data = get_strike_icon_data(li.name, strike_count)
                $ strike_xpos = 1329
                $ strike_ypos = 322
                
                imagebutton:
                    idle strike_data["image"]
                    hover strike_data["image"]
                    at igm_appear_fg
                    action NullAction()
                    hovered Function(set_icon_hover, strike_data["description"], strike_xpos, strike_ypos)
                    unhovered Function(clear_icon_hover)
                    focus_mask True
                
                null width 32
                
                ## Pregnancy status
                $ preg_xpos = 1329 + 32 + 48  # Strike width + null width
                $ preg_ypos = 322
                
                if pregnant:
                    imagebutton:
                        idle "gui/preg_on.png"
                        hover "gui/preg_on.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered Function(set_icon_hover, li.name + " is pregnant.", preg_xpos, preg_ypos)
                        unhovered Function(clear_icon_hover)
                        focus_mask True
                else:
                    imagebutton:
                        idle "gui/preg_off.png"
                        hover "gui/preg_off.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered Function(set_icon_hover, li.name + " is not pregnant.", preg_xpos, preg_ypos)
                        unhovered Function(clear_icon_hover)
                        focus_mask True
                
                null width 32
                
                ## Virgin status
                $ virgin_xpos = 1329 + 32 + 48 + 32 + 48  # Strike + null + preg + null width
                $ virgin_ypos = 322
                
                if is_virgin:
                    imagebutton:
                        idle "gui/virgin_on.png"
                        hover "gui/virgin_on.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered Function(set_icon_hover, li.name + " is still a virgin.", virgin_xpos, virgin_ypos)
                        unhovered Function(clear_icon_hover)
                        focus_mask True
                else:
                    imagebutton:
                        idle "gui/virgin_off.png"
                        hover "gui/virgin_off.png"
                        at igm_appear_fg
                        action NullAction()
                        hovered Function(set_icon_hover, li.name + " is not a virgin.", virgin_xpos, virgin_ypos)
                        unhovered Function(clear_icon_hover)
                        focus_mask True
            else:
                null
        
        ## Character corruption and trust level displays
        vbox:
            xpos 1449
            ypos 475
            if knows:
                ## Corruption level
                add get_corruption_level_image(corruption) at igm_appear_fg
                
                null height 23
                
                ## Trust/Love level
                add get_trust_level_image(trust) at igm_appear_fg
            else:
                null
        
        ## Show hover tooltip as speech bubble over icon
        if stats_state.icon_hover_description != "":
            frame:
                ## Position the bubble above the icon with offset
                xpos stats_state.icon_hover_xpos - 75  # Center and adjust for width
                ypos stats_state.icon_hover_ypos - 85  # Position above the icon
                xmaximum 200
                
                text stats_state.icon_hover_description:
                    size 16
                    font "fonts/UbuntuTitling-Bold.ttf"
                    color "#545454"
                    text_align 0.5
                    xalign 0.5

################################################################################
## MAIN CHARACTER STATS SCREEN
################################################################################

screen mc_stats():
    ## Character label background
    vbox:
        xpos 474
        ypos 294
        add "gui/label_mc.png" at igm_appear_fg
    
    ## Character name display
    vbox:
        xpos 304
        ypos 351
        text "[mc_name.upper()]" at igm_appear_fg style "stats_name"
    
    ## Character alignment display based on integrity
    vbox:
        xpos 929
        yalign 0.5
        $ mc_integrity = rm.get("mc", "integrity")
        add get_mc_integrity_image(mc_integrity) at igm_appear_fg
    
    ## Character information display
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

################################################################################
## WALKTHROUGH INTEGRATION SCREEN
################################################################################

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

################################################################################
## STATS SCREEN STYLES
################################################################################

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

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this stats system in your game:
##
## 1. Display the stats button in your HUD:
##    show screen stats_button
##
## 2. Or open stats directly from any menu:
##    textbutton "Character Stats" action Show("li_stats")
##
## 3. The stats system will automatically:
##    - Display character selection menu on the left
##    - Show detailed character information when selected
##    - Switch between bio and sexual stats tabs
##    - Display character trait icons with hover tooltips
##    - Handle outfit navigation for characters with multiple outfits
##    - Show appropriate information based on character discovery status
##
## 4. Required character data systems:
##    - rm (Relationship Management): trust, corruption, knows, pregnancy
##    - ss (Sexual Statistics): virgin status, strikes, sexual experience
##    - wm (Wardrobe Management): outfit unlocking and navigation
##    - Character objects with: name, age, height, weight, measurements, info
##
## 5. Required assets:
##    - Character tab images: gui/tab_[character]_off.png, gui/tab_[character]_on.png
##    - UI elements: gui/popup_bg.png, gui/label_li.png, gui/label_mc.png
##    - Trait icons: gui/strike_[0-3].png, gui/preg_on/off.png, gui/virgin_on/off.png
##    - Level indicators: gui/cor_[0-5].png, gui/love_[0-5].png, gui/stats_mc_[level].png
##    - Navigation buttons: gui/btn_prev/next_off/on.png, gui/btn_close_on/off.png
##    - Character images via get_character_outfit_pic() function
##
## 6. Character data structure example:
##    define amber = Character("Amber")
##    amber.name = "Amber"
##    amber.age = "22"
##    amber.height = "5'6\""
##    amber.weight = "125 lbs"
##    amber.measurements = "34C-24-36"
##    amber.info = "Character biography text here..."
##
## 7. System dependencies:
##    - Must have relationship management (rm) system
##    - Must have sexual statistics (ss) system  
##    - Must have wardrobe management (wm) system
##    - Must have character discovery system
##    - Must have animated_glitch() function for logo
##    - Must have igm_appear/igm_appear_fg/igm_appear_bg transforms
##
## TROUBLESHOOTING:
## - If character images don't show: Ensure get_character_outfit_pic() function exists
## - If stats don't display: Check rm.get() and ss.get() function calls
## - If tabs don't work: Verify stats_state.selected_tab is being set correctly
## - If hover tooltips don't appear: Check icon_hover variables are being set
##
## Example implementation in your main menu or HUD:
## screen hud():
##     use stats_button  # This will show the stats button
##
## Or in an extras menu:
## screen extras():
##     textbutton "Character Stats" action Show("li_stats")
##     textbutton "Other Options" action NullAction()