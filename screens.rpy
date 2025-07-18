﻿################################################################################
## Initialization
################################################################################

init offset = -1

default save_name = ""

init python:
    def set_save_name(new_name):
        def quote(s):
            s = s.replace("{", "{{")
            s = s.replace("[", "[[")
            return s
        store.save_name = quote(new_name)
################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    yalign 0.0
    xalign 0.0



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                null width 400
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    ypos 50
    xpos 18
    yalign 1.0

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 460
    xsize gui.dialogue_width
    ypos 60
    outlines [(3, "#333232", 0,0)]
    line_leading 4

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"
    add "vignette" at igm_appear_bg
    add "gui/confirm_popup.png" at igm_appear xalign 0.5 yalign 0.5
    add "gui/exclamation_mark.png" at igm_appear_fg, heartbeat(0.95,1.05,1) xalign 0.5 ypos 303
    text "attention".upper() at igm_appear_fg2 ypos 199 xalign 0.5 style "confirm_txt"
    
    frame at igm_appear_fg2:
        xalign 0.5
        yalign 0.5
        vbox:
            text prompt.upper() style "input_prompt" xalign 0.5 ypos 110
            input id "input"  xalign 0.5 ypos 220

style input_prompt is default

style input_prompt:
    properties gui.text_properties("input_prompt")
    textalign 0.5
    layout "subtitle"
    font "fonts/UbuntuTitling-Bold.ttf"
    size 42
    color "#34323d"
    xmaximum 598

style input:
    outlines [(3, "#1f1f1fff", 0, 0)]
    color "#ffcc01"
    size 42
    xmaximum 598


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

default choice_hovered = False

screen choice(items):
    style_prefix "choice"
    frame:
        xysize (1.0, 1.0)
        vbox:
            for n, i in enumerate(items, 1):
                textbutton "[n]. [i.caption]":
                    action i.action
                    hovered SetVariable("choice_hovered", True)
                    unhovered SetVariable("choice_hovered", False)
                if n < 10:
                    key str(n) action i.action

    if not choice_hovered:
        add "achtung" at igm_appear_fg:
            align (0.1, 0.4)

    on "show" action SetVariable("choice_hovered", False)

style choice_vbox is vbox:
    xpos 200
    yalign 0.5
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is choicemn:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back").lower() action Rollback()
            textbutton _("History").lower() action ShowMenu('history')
            textbutton _("Skip").lower() action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto").lower() action Preference("auto-forward", "toggle")
            textbutton _("Save").lower() action ShowMenu('save')
            textbutton _("Q.Save").lower() action QuickSave()
            textbutton _("Q.Load").lower() action QuickLoad()
            textbutton _("Prefs").lower() action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    font "fonts/UbuntuTitling-Bold.ttf"
    size 18
    kerning -1
    idle_color "#3f3c389f"
    hover_color "#27dc94cc"
    idle_outlines [ (2, "#ffffff9f", 0, 0) ]
    hover_outlines [ (2, "#000000cc", 0, 0) ]



################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():


    vbox:
        xpos 235
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_play_off.png"
            hover "gui/mm_play_on.png"
            hover_foreground "gui/mm_b_start.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action Start()
            style "mmenu_btn"
            focus_mask None



#button - load
    vbox:
        xpos 435
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_load_off.png"
            hover "gui/mm_load_on.png"
            hover_foreground "gui/mm_b_load.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action ShowMenu("load")
            style "mmenu_btn"
            focus_mask None


#button - achievments
    vbox:
        xpos 635
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_achi_off.png"
            hover "gui/mm_achi_on.png"
            hover_foreground "gui/mm_b_achi.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action ShowMenu("achievements")
            style "mmenu_btn"
            focus_mask None

#button - preferences
    vbox:
        xpos 835
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_pref_off.png"
            hover "gui/mm_pref_on.png"
            hover_foreground "gui/mm_b_pref.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action ShowMenu("preferences")
            style "mmenu_btn"
            focus_mask None


#button - extras
    vbox:
        xpos 1035
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_extras_off.png"
            hover "gui/mm_extras_on.png"
            hover_foreground "gui/mm_b_extras.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action ShowMenu("extras")
            style "mmenu_btn"
            focus_mask None

#button - about
    vbox:
        xpos 1235
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_about_off.png"
            hover "gui/mm_about_on.png"
            hover_foreground "gui/mm_b_about.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action ShowMenu("about")
            style "mmenu_btn"
            focus_mask None

#button - help
    vbox:
        xpos 1435
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_help_off.png"
            hover "gui/mm_help_on.png"
            hover_foreground "gui/mm_b_help.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action ShowMenu("help")
            style "mmenu_btn"
            focus_mask None

#button - quit
    vbox:
        xpos 1635
        ypos 880
        spacing -134
        add "gui/mm_play_bg.png" at focus_pulse_menu xalign 0.5
        imagebutton:
            xalign 0.5
            idle "gui/mm_quit_off.png"
            hover "gui/mm_quit_on.png"
            hover_foreground "gui/mm_b_quit.png"
            hover_align (1.0, 0.0)
            hover_offset (10, -10)
            action Quit(confirm=not main_menu)
            style "mmenu_btn"
            focus_mask None


    # hbox:
    #     style_prefix "navigation"

    #     xalign 0.5
    #     yalign 0.92
    #     spacing gui.navigation_spacing

    #     if main_menu:
    #         textbutton _("Start") action Start() style "mmenu_btn" 
    #     else:
    #         textbutton _("History") action ShowMenu("history") style "mmenu_btn" 

    #     textbutton _("Load") action ShowMenu("load") style "mmenu_btn" 
    #     textbutton "Achievements" action ShowMenu("achievements") style "mmenu_btn" 
    #     textbutton _("Preferences") action ShowMenu("preferences") style "mmenu_btn" 

    #     if _in_replay:
    #         textbutton _("End Replay") action EndReplay(confirm=True) style "mmenu_btn" 
    #     elif not main_menu:
    #         textbutton _("Main Menu") action MainMenu() style "mmenu_btn" 

    #     textbutton "Extras" action ShowMenu("extras") style "mmenu_btn" 


    #     if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
    #         textbutton _("Help") action ShowMenu("help") style "mmenu_btn" 

    #     if renpy.variant("pc"):
    #         textbutton _("Quit") action Quit(confirm=not main_menu) style "mmenu_btn" 




## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

default persistent.shown_version = ""

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background at truecenter, concentrate
    add "mmbg_rain"
    add animated_glitch("mmbg_logo") at neon_flicker xalign 0.025 yalign 0.026


    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    vbox: ##PATREON
            xpos 1785
            ypos 700
            imagebutton hover_offset (0, -5) idle "gui/patreon_off.png" hover "gui/patreon_on.png" style "mm_widget" action OpenURL("https://www.patreon.com/qori") focus_mask True
    vbox: ##SUBS
            xpos 1785
            ypos 560
            imagebutton hover_offset (0, -5) idle "gui/subs_off.png" hover "gui/subs_on.png" style "mm_widget" action OpenURL("https://subscribestar.adult/qori") focus_mask True
    vbox: ##BOOST
            xpos 1785
            ypos 420
            imagebutton hover_offset (0, -5) idle "gui/boost_off.png" hover "gui/boost_on.png" style "mm_widget" action OpenURL("https://boosty.to/qori") focus_mask True
    vbox: ##ITCH
            xpos 1785
            ypos 280
            imagebutton hover_offset (0, -5) idle "gui/itch_off.png" hover "gui/itch_on.png" style "mm_widget" action OpenURL("https://qorigaming.itch.io/hard-to-love") focus_mask True
    vbox: ##OPPAI
            xpos 1785
            ypos 140
            imagebutton hover_offset (0, -5) idle "gui/oppai_off.png" hover "gui/oppai_on.png" style "mm_widget" action OpenURL("https://www.oppaiman.com/app/Hard_to_Love_0.26") focus_mask True
    vbox: ##DISCORD
            xpos -6
            ypos 700
            imagebutton hover_offset (0, -5) idle "gui/disc_off.png" hover "gui/disc_on.png" style "mm_widget" action OpenURL("https://discord.gg/RnRtAFggRW") focus_mask True
                


    if persistent.shown_version != config.version:
        timer 0.1 action Show("confirm_first_time", message="This is a solo passion project.\n\nPlease note, this BETA version may have bugs, experience crashes, and undergo significant changes, including potential save data issues.", yes_action=[SetVariable("persistent.shown_version", config.version), Hide("confirm_first_time")])

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
        add "igm_dim" at igm_appear_bg
        add "mmbg_rain" at igm_appear_bg

    add "gui/popup_bg.png" xpos 236 ypos 84 at igm_appear_bg
    add animated_glitch("igm_logo") xpos 299 ypos 132 at igm_appear
    add "gui/line.png" ypos 792 xpos 331 at igm_appear
    if main_menu:
        imagebutton at igm_appear:
            xpos 332
            ypos 824
            idle "gui/return_off.png"
            hover "gui/return_on.png"
            action ShowMenu("main_menu")
            style "igm_button"
            focus_mask None
    else:
        imagebutton at igm_appear:
            xpos 1297
            ypos 824
            idle "gui/quit_off.png"
            hover "gui/quit_on.png"
            action Quit(confirm=not main_menu)
            style "igm_button"
            focus_mask None

    if main_menu:
        null
    else:
        imagebutton at igm_appear:
            xpos 837
            ypos 185
            idle "gui/tab_mm_off.png"
            hover "gui/tab_mm_on.png"
            action MainMenu()
            style "igm_button"
            focus_mask None
        imagebutton at igm_appear:
            xpos 1007
            ypos 185
            idle "gui/tab_load_off.png"
            hover "gui/tab_load_hover.png"
            selected_hover "gui/tab_load_on.png"
            selected_idle "gui/tab_load_on.png"
            action ShowMenu("load")
            style "igm_button"
            focus_mask None
        imagebutton at igm_appear:
            xpos 1140
            ypos 185
            idle "gui/tab_save_off.png"
            hover "gui/tab_save_hover.png"
            selected_hover "gui/tab_save_on.png"
            selected_idle "gui/tab_save_on.png"
            action ShowMenu('save')
            style "igm_button"
            focus_mask None
        imagebutton at igm_appear:
            xpos 1273
            ypos 185
            idle "gui/tab_pref_off.png"
            hover "gui/tab_pref_hover.png"
            selected_hover "gui/tab_pref_on.png"
            selected_idle "gui/tab_pref_on.png"
            action ShowMenu("preferences")
            style "igm_button"
            focus_mask None
        imagebutton at igm_appear:
            xpos 1406
            ypos 185
            idle "gui/tab_help_off.png"
            hover "gui/tab_help_hover.png"
            selected_hover "gui/tab_help_on.png"
            selected_idle "gui/tab_help_on.png"
            action ShowMenu("help")
            style "igm_button"
            focus_mask None

    if main_menu:
        null
    else:
        imagebutton at igm_appear:
            xpos 1554
            ypos 138
            idle "gui/btn_close_on.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action Return()
            style "igm_button"
            focus_mask None


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

    if main_menu:
        add "gui/mmtitle_about.png" ypos 151 xpos 1370 at igm_appear_fg
    else:
        null

    add "gui/yuk_bg.png" ypos 276 xpos 306 at igm_appear_fg
    add animated_glitch("yukana") xpos 308 ypos 278 at igm_appear_fg
    add "gui/about_me.png" ypos 285 xpos 637 at igm_appear_fg

    vbox:
        xsize 444
        xpos 1149
        ypos 435

        vbox:
            text _("Version [config.version!t]\n") at igm_appear_fg style "about_txt"

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n" at igm_appear_fg  style "about_txt"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") at igm_appear_fg style "about_txt"

style about_txt is text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#34323d"

style about_label is about_txt
style about_label_text is about_txt
style about_text is about_txt




## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load
screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))
    if main_menu:
        add "gui/mmtitle_load.png" ypos 151 xpos 1411 at igm_appear_fg
    else:
        null


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))


    frame:
        xsize 1920
        ysize 1080

        use game_menu(title)

        fixed:

            order_reverse True
            vbox:
                xsize 1250
                xpos 331
                ypos 270

                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"
                    xalign 0.5
                    yalign 0.5
                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        
                        button at igm_appear_fg:
                            if renpy.get_screen("save"):
                                action [SetVariable("save_name", ""), Show("save_name_slot", accept=FileSave(slot))]
                            else:
                                action FileLoad(slot)
                            xsize 353
                            ysize 245
                            
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                frame:
                                    xsize 345
                                    ysize 194
                                    xalign 0.5
                                    yalign 0.0
                                    add FileScreenshot(slot) at igm_appear_fg2:
                                        xsize 345
                                        ysize 194
                                        xalign 0.5
                                        yalign 0.5
                                    add "gui/rectangle_mask.png" at igm_appear_fg2:
                                        xsize 345
                                        ysize 194
                                        xalign 0.5
                                        yalign 0.5
                                null height 10
                                vbox:
                                    xalign 0.1
                                    yalign 0.5
                                    spacing 2
                                    yoffset -6
                                    hbox:
                                        spacing 10  # Adjust spacing as needed
                                        text FileTime(slot, format=_("{#file_time}%m/%d/%Y, %I%p"), empty=_("")) at igm_appear_fg:
                                            style "slot_time_text"
                                        text FileSaveName(slot) at igm_appear_fg:
                                            style "slot_name_text"
                            key "save_delete" action FileDelete(slot)

                ## Buttons to access other pages.
                vbox:
                    style_prefix "page"
                    xpos 407
                    ypos -13
                    hbox:
                        if config.has_sync:
                            if CurrentScreenName() == "save":
                                textbutton _("Upload Sync") at igm_appear_fg:
                                    action UploadSync()
                                    xalign 0.1
                                    style "page_button"
                            else:
                                textbutton _("Download Sync") at igm_appear_fg:
                                    action DownloadSync()
                                    xalign 0.1
                                    style "page_button"
                        null width 40
                        xalign 0.5
                        spacing gui.page_spacing
                        textbutton _("<") action FilePagePrevious() at igm_appear_fg
                        if config.has_autosave:
                            textbutton _("{#auto_page}A") action FilePage("auto") at igm_appear_fg
                        if config.has_quicksave:
                            textbutton _("{#quick_page}Q") action FilePage("quick") at igm_appear_fg
                        for page in range(1, 10):
                            textbutton "[page]" action FilePage(page) at igm_appear_fg
                        textbutton _(">") action FilePageNext() at igm_appear_fg

# Define the save_name_slot screen
screen save_name_slot(accept=NullAction()):
    modal True
    zorder 100  # Ensure this screen is on top of others

    # First, add the semi-transparent overlay
    add Solid("#000000") alpha 0.5

    # Then, add the frame containing the input and buttons
    frame:
        xsize 800
        ysize 400
        align (0.5, 0.5)  # Center the frame on the screen
        style_prefix "save_name"

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            add "gui/exclamation_mark_small.png":
                xalign 0.5
                yalign 0.5

            label _("Please name your save:") style "save_name_label"

            input:
                style "save_name_input"
                default store.save_name
                changed set_save_name
                length 40

            textbutton _("Save Game"):
                style "save_name_button"
                action [accept, Hide("save_name_slot")]

    key "game_menu" action Hide("save_name_slot")


# Define styles for the save_name_slot screen
style save_name_frame is frame:
    background "gui/rounded_frame.png"
    padding (20, 20)

style save_name_label is label:
    font "fonts/UbuntuTitling-Bold.ttf"
    size 28
    color "#FFFFFF"
    xalign 0.5

style save_name_input is input:
    font "fonts/UbuntuTitling-Bold.ttf"
    size 24
    color "#FFFFFF"
    background "#000000"
    padding (10, 10)
    xalign 0.5

style save_name_button is button:
    background "#555555"
    xalign 0.5

style save_name_button_text is button_text:
    font "fonts/UbuntuTitling-Bold.ttf"
    size 24
    color "#FFFFFF"
    xalign 0.5


# Existing styles
style page_label is gui_label

style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button

style slot_button_text is gui_button_text
style slot_time_text is text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#b2b2b2"
    hover_color "#eea835"

style slot_name_text is text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#b2b2b2"
    hover_color "#27dc95"

style page_label_text is text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    kerning 0
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    hover_color "#27dc95"

style slot_button:
    xalign 0.0

style slot_button_text:
    properties gui.text_properties("slot_button")

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu("Preferences"):
        frame:
            xsize 1920
            ysize 1080

    if main_menu:
        add "gui/mmtitle_pref.png" ypos 158 xpos 1214 at igm_appear_fg
    else:
        null

    hbox:
        add "gui/line.png" ypos 511 xpos 331 at igm_appear
    hbox:
        add "gui/line.png" ypos 651 xpos 331 at igm_appear

#PREF: AUDIO SECTION
    hbox: 
        xpos 347
        ypos 310
        add "gui/audio_title.png" at igm_appear_fg
        vbox:
            xpos 53
            ypos 10
            imagemap at igm_appear_fg:
                ground "gui/blue_bar_off.png"
                idle "gui/blue_bar_off.png"
                selected_hover "gui/blue_bar_on.png"
                selected_idle "gui/blue_bar_on.png"
                hotbar (0, 0, 600, 11) value Preference("sound volume")
                style "optstar"
            imagemap at igm_appear_fg:
                ypos 45
                ground "gui/orange_bar_off.png"
                idle "gui/orange_bar_off.png"
                selected_hover "gui/orange_bar_on.png"
                selected_idle "gui/orange_bar_on.png"
                hotbar (0, 0, 600, 11) value Preference("voice volume")
                style "optstar"
            imagemap at igm_appear_fg:
                ypos 90
                ground "gui/gray_bar_off.png"
                idle "gui/gray_bar_off.png"
                selected_hover "gui/gray_bar_on.png"
                selected_idle "gui/gray_bar_on.png"
                hotbar (0, 0, 600, 11) value Preference("music volume")
                style "optstar"

#PREF: MUTE ALL SECTION
    hbox: 
        xpos 1300
        ypos 365
        add "gui/mute_title.png" at igm_appear_fg
        vbox:
            xpos 23
            ypos -13
            imagebutton at igm_appear:
                idle "gui/switch_off.png"
                hover "gui/switch_on.png"
                selected_hover "gui/switch_off.png"
                selected_idle "gui/switch_on.png"
                action Preference("all mute", "toggle")
                style "igm_button"
                focus_mask None

#PREF: TXT SPEED SECTION / FOWARD TIME
    hbox: 
        xpos 344
        ypos 548
        add "gui/txt_title.png" at igm_appear_fg
        vbox:
            xpos 40
            ypos -2
            imagemap at igm_appear_fg:
                ground "gui/bar_magenta_off.png"
                idle "gui/bar_magenta_off.png"
                selected_hover "gui/bar_magenta_on.png"
                selected_idle "gui/bar_magenta_on.png"
                hotbar (0, 0, 421, 21) value Preference("text speed")
                style "optstar"
            imagemap at igm_appear_fg:
                ypos 40
                ground "gui/bar_purple_off.png"
                idle "gui/bar_purple_off.png"
                selected_hover "gui/bar_purple_on.png"
                selected_idle "gui/bar_purple_on.png"
                hotbar (0, 0, 421, 21) value Preference("auto-forward time")
                style "optstar"

#PREF:  SKIP TXT SECTION
    hbox: 
        xpos 1222
        ypos 548
        add "gui/skip_title.png" at igm_appear_fg
        vbox:
            xpos 23
            ypos -13
            imagebutton at igm_appear:
                idle "gui/checkbox_square_off.png"
                hover "gui/checkbox_square_on.png"
                selected_hover "gui/checkbox_square_off.png"
                selected_idle "gui/checkbox_square_on.png"
                action Preference("skip", "toggle")
                style "igm_button"
                focus_mask None
            imagebutton at igm_appear:
                ypos 14
                idle "gui/checkbox_square_off.png"
                hover "gui/checkbox_square_on.png"
                selected_hover "gui/checkbox_square_off.png"
                selected_idle "gui/checkbox_square_on.png"
                action Preference("after choices", "toggle")
                style "igm_button"
                focus_mask None

#PREF: DISPLAY SECTION
    hbox:
        xpos 354
        ypos 677
        add "gui/display_window.png" at igm_appear_fg
        vbox:
            xpos 52
            ypos -6
            imagebutton at igm_appear:
                idle "gui/checkbox_square_off.png"
                hover "gui/checkbox_square_on.png"
                selected_hover "gui/checkbox_square_off.png"
                selected_idle "gui/checkbox_square_on.png"
                action Preference("display", "window")
                style "igm_button"
                focus_mask None
    hbox:
        xpos 354
        ypos 737
        add "gui/display_fullscreen.png" at igm_appear_fg
        vbox:
            ypos -8
            xpos 31
            imagebutton at igm_appear:
                idle "gui/checkbox_square_off.png"
                hover "gui/checkbox_square_on.png"
                selected_hover "gui/checkbox_square_off.png"
                selected_idle "gui/checkbox_square_on.png"
                action Preference("display", "fullscreen")
                style "igm_button"
                focus_mask None

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "mecha"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

    if main_menu:
        add "gui/mmtitle_help.png" ypos 150 xpos 1417 at igm_appear_fg
    else:
        null

    vbox:
        xsize 1250
        xpos 370
        ypos 270
        spacing 23

        hbox:
            xalign 0.61
            textbutton _("Game Mechanics") action SetScreenVariable("device", "mecha") style "help_link" at igm_appear_fg
            null width 60
            textbutton _("Game Icons") action SetScreenVariable("device", "gicons") style "help_link" at igm_appear_fg
            null width 60
            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard") style "help_link" at igm_appear_fg
            null width 60
            textbutton _("Mouse") action SetScreenVariable("device", "mouse") style "help_link" at igm_appear_fg

            if GamepadExists():
                null width 60
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad") style "help_link" at igm_appear_fg
                
        if device == "mecha":
            use gamemech_help
        elif device == "gicons":
            use gameicons_help
        elif device == "keyboard":
            use keyboard_help
        elif device == "mouse":
            use mouse_help
        elif device == "gamepad":
            use gamepad_help



screen keyboard_help():
    viewport:
        xsize 1250
        ymaximum 440
        mousewheel True
        scrollbars "vertical" at igm_appear_fg

        
        grid 2 12:
            xalign 0.1
            spacing 30
            
            text _("Enter") style "help_lbl" at igm_appear_fg 
            text _("Advances dialogue and activates the interface.") style "help_txt" at igm_appear_fg 

            text _("Space") style "help_lbl" at igm_appear_fg 
            text _("Advances dialogue without selecting choices.") style "help_txt" at igm_appear_fg 

            text _("Arrow Keys") style "help_lbl" at igm_appear_fg 
            text _("Navigate the interface.") style "help_txt" at igm_appear_fg 

            text _("Escape") style "help_lbl" at igm_appear_fg 
            text _("Accesses the game menu.") style "help_txt" at igm_appear_fg 

            text _("Ctrl") style "help_lbl" at igm_appear_fg 
            text _("Skips dialogue while held down.") style "help_txt" at igm_appear_fg 

            text _("Tab") style "help_lbl" at igm_appear_fg 
            text _("Toggles dialogue skipping.") style "help_txt" at igm_appear_fg 

            text _("Page Up") style "help_lbl" at igm_appear_fg 
            text _("Rolls back to earlier dialogue.") style "help_txt" at igm_appear_fg 

            text _("Page Down") style "help_lbl" at igm_appear_fg 
            text _("Rolls forward to later dialogue.") style "help_txt" at igm_appear_fg 

            text "H" style "help_lbl" at igm_appear_fg 
            text _("Hides the user interface.") style "help_txt" at igm_appear_fg 

            text "S" style "help_lbl" at igm_appear_fg 
            text _("Takes a screenshot.") style "help_txt" at igm_appear_fg 

            text "V" style "help_lbl" at igm_appear_fg 
            text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.") style "help_txt" at igm_appear_fg 

            text "Shift+A" style "help_lbl" at igm_appear_fg 
            text _("Opens the accessibility menu.") style "help_txt" at igm_appear_fg


screen mouse_help():
    viewport:
        xsize 1250
        ymaximum 300
        #mousewheel True
        #scrollbars "vertical"
        
        grid 2 5:
            xalign 0.1
            spacing 30

            text _("Left Click") style "help_lbl" at igm_appear_fg
            text _("Advances dialogue and activates the interface.") style "help_txt" at igm_appear_fg 

            text _("Middle Click") style "help_lbl" at igm_appear_fg
            text _("Hides the user interface.") style "help_txt" at igm_appear_fg 

            text _("Right Click") style "help_lbl" at igm_appear_fg
            text _("Accesses the game menu.") style "help_txt" at igm_appear_fg 

            text _("Mouse Wheel Up") style "help_lbl" at igm_appear_fg
            text _("Rolls back to earlier dialogue.") style "help_txt" at igm_appear_fg 

            text _("Mouse Wheel Down") style "help_lbl" at igm_appear_fg
            text _("Rolls forward to later dialogue.") style "help_txt" at igm_appear_fg 


screen gamepad_help():
    viewport:
        xsize 1250
        ymaximum 440
        
        grid 2 7:
            xalign 0.1
            spacing 25

            text _("Right Trigger\nA/Bottom Button") style "help_lbl" at igm_appear_fg yalign 0.5
            text _("Advances dialogue and activates the interface.") style "help_txt" at igm_appear_fg

            text _("Left Trigger\nLeft Shoulder") style "help_lbl" at igm_appear_fg yalign 0.5
            text _("Rolls back to earlier dialogue.") style "help_txt" at igm_appear_fg

            text _("Right Shoulder") style "help_lbl" at igm_appear_fg yalign 0.5
            text _("Rolls forward to later dialogue.") style "help_txt" at igm_appear_fg

            text _("D-Pad, Sticks") style "help_lbl" at igm_appear_fg yalign 0.5
            text _("Navigate the interface.") style "help_txt" at igm_appear_fg

            text _("Start, Guide, B/Right Button") style "help_lbl" at igm_appear_fg yalign 0.5
            text _("Accesses the game menu.") style "help_txt" at igm_appear_fg

            text _("Y/Top Button") style "help_lbl" at igm_appear_fg yalign 0.5
            text _("Hides the user interface.") style "help_txt" at igm_appear_fg

            textbutton _("Calibrate") style "help_link2" action GamepadCalibrate() at igm_appear_fg

screen gamemech_help():
    viewport:
        xsize 1250
        ysize 440
        mousewheel True
        scrollbars "vertical" at igm_appear_fg
        
        vbox:
            xalign 0.1
            spacing 30
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_cor" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("Corruption levels dictate how naughty your Love Interests will be. \nEvery 16 points unlocks a new level of corruption, allowing naughtier actions and sexier outfits. \nHigher levels mean they'll let loose and indulge their desires. Lower levels keep things tamer.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_trust" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("This shows how much your Love Interests care for and trust the Main Character. \nEarn 16 points to level up, changing their behavior and unlocking possible relationships. \nHigh love and trust are essential for the best endings.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_rel" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("This tells you if your Main Character is dating a Love Interest. \nIf they break up, the story might give chances to reconnect and rekindle the romance.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_preg" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("Pregnancy can become part of your story based on the choices you make. \nIt's up to you whether to pursue this path.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_integrity" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("Integrity heavily influences the game's endings, reflecting your moral and ethical choices outside of romance. \nYou start neutral, but making ethical choices promotes justice lawfully. \nUnethical choices may lead to a vigilante path, shaping your story's morality.") style "help_txt" at igm_appear_fg

screen gameicons_help():
    viewport:
        xsize 1250
        ysize 440
        mousewheel True
        scrollbars "vertical" at igm_appear_fg
        
        vbox:
            xalign 0.1
            spacing 30
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "achtung" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("When you see this icon, the game is paused and needs your attention. \nChoose an option from the menu in the middle-left part of the screen (except on phone interactions) to continue.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    hbox:
                        xalign 0.5 yalign 0.5
                        spacing 10
                        add "help_camera1" at igm_appear_fg 
                        add "help_camera2" at igm_appear_fg
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("You may see two or more circles above your Main Character's name. \nEach circle is a different camera angle for the same scene. Click on the circles to switch between views. \nThe active camera angle has a green circle.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_stats" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("Click this icon to see the stats of your Love Interests and Main Character.\nAs you improve these stats, you'll unlock better visual rewards for each Love Interest.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_assist" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("This icon is for my supporters only.\nClick it to get hints for making better decisions with certain characters. A green circle in the top-left means it's active. \nTo activate, click the icon and select the characters you want help with. To deactivate, deselect the chosen characters.") style "help_txt" at igm_appear_fg
        
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "help_talk" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("This icon means your character or the current character is speaking or having a conversation.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "screaming" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("When you see this icon, your character or the current character is yelling or speaking loudly.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    add "thinking" at igm_appear_fg xalign 0.5 yalign 0.5
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("This icon means you're reading the thoughts of your character or the current character.\nAs the player, you see these inner dialogues, but other characters in the game don't.") style "help_txt" at igm_appear_fg
            
            hbox:
                spacing 40
                
                frame:
                    xsize 360
                    xalign 0.5
                    yalign 0.5
                    hbox:
                        xalign 0.5 yalign 0.5
                        spacing 10
                        add "gui/phone_sms.png" at igm_appear_fg, phone_sms_icon xalign 0.5 yalign 0.5 zoom 0.6
                hbox:
                    xsize 650
                    yalign 0.5
                    text _("When this icon appears, you've received a message on your phone. It's up to you to reply or not.") style "help_txt" at igm_appear_fg
            
style help_txt is text:
    xalign 0.0
    yalign 0.5
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#a59f96"

style help_lbl is text:
    xalign 0.0
    yalign 0.5
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#2a3957"

style help_link is button:
    xalign 0.0

style help_link_text is text:
    size 30
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#27dc95"
    hover_color "#c9f9d7"

style help_link2 is button:
    xalign 0.0

style help_link2_text is text:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#eea835"
    hover_color "#ffe999"



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm


screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"
    add "vignette" at igm_appear_bg
    add "gui/confirm_popup.png" at igm_appear xalign 0.5 yalign 0.5
    add "gui/exclamation_mark.png" at igm_appear_fg, heartbeat(0.95,1.05,1) xalign 0.5 ypos 303
    text "confirm".upper() at igm_appear_fg2 ypos 199 xalign 0.5 style "confirm_txt"
    
    frame at igm_appear_fg2:
        xalign 0.5
        yalign 0.5
        vbox:
            null height 250
            if len(message.split()) > 8:
                label _(message).upper():
                    style "confirm_prompt2"
                    xalign 0.5
            else:
                label _(message).upper():
                    style "confirm_prompt"
                    xalign 0.5
                

            hbox:
                xalign 0.5
                ypos 92
                spacing 34
                imagebutton:
                    xalign 0.5
                    idle "gui/cancel_off.png"
                    hover "gui/cancel_on.png"
                    hover_foreground "gui/cancel_on.png"
                    action no_action
                    #style "mmenu_btn"
                    focus_mask None
                imagebutton:
                    xalign 0.5
                    idle "gui/ok_off.png"
                    hover "gui/ok_on.png"
                    hover_foreground "gui/ok_on.png"
                    action yes_action
                    #style "mmenu_btn"
                    focus_mask None




    ## Right-click and escape answer "no".
    key "game_menu" action no_action

screen confirm_first_time(message, yes_action):
    modal True
    zorder 200

    style_prefix "confirm"
    add "vignette" at igm_appear_bg
    add "gui/confirm2_popup.png" at igm_appear xalign 0.5 yalign 0.5
    add "gui/lock.png" at igm_appear_fg, heartbeat(0.95,1.05,1) xalign 0.5 ypos 303
    text "warning".upper() at igm_appear_fg2 ypos 199 xalign 0.5 style "confirm_txt"
    
    frame at igm_appear_fg2:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            null height 350
            if len(message.split()) > 8:
                label _(message):
                    style "confirm_prompt4"
                    xalign 0.1
            else:
                label _(message):
                    style "confirm_prompt3"
                    xalign 0.1
            null height 3
            text "yukana".upper() style "confirm_prompt5_text" xalign 1.0

            hbox:
                xalign 0.5
                ypos 42
                imagebutton:
                    xalign 0.5
                    idle "gui/ok_off.png"
                    hover "gui/ok_on.png"
                    hover_foreground "gui/ok_on.png"
                    action yes_action
                    #style "mmenu_btn"
                    focus_mask None

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_prompt2 is gui_prompt
style confirm_prompt2_text is gui_prompt_text
style confirm_prompt3 is gui_prompt
style confirm_prompt3_text is gui_prompt_text
style confirm_prompt4 is gui_prompt
style confirm_prompt4_text is gui_prompt_text
style confirm_prompt5 is gui_prompt
style confirm_prompt5_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_txt is text:
    kerning 0
    size 54
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#fff"

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    font "fonts/UbuntuTitling-Bold.ttf"
    size 42
    color "#a59f96"
    xmaximum 570
    ymaximum 137

style confirm_prompt2_text:
    textalign 0.5
    layout "subtitle"
    font "fonts/UbuntuTitling-Bold.ttf"
    size 28
    color "#a59f96"
    xmaximum 570
    ymaximum 137

style confirm_prompt3_text:
    textalign 0
    layout "subtitle"
    font "fonts/UbuntuTitling-Bold.ttf"
    size 42
    color "#a59f96"
    xmaximum 570
    ymaximum 137

style confirm_prompt4_text:
    textalign 0
    layout "subtitle"
    font "fonts/UbuntuTitling-Bold.ttf"
    size 24
    color "#a59f96"
    xmaximum 570
    ymaximum 137

style confirm_prompt5_text:
    textalign 0.9
    
    font "fonts/UbuntuTitling-Bold.ttf"
    size 26
    color "#ff5d5d"
    xmaximum 570
    ymaximum 137

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")



## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            yalign 0.5
            xoffset -18
            spacing 4

            text _("Skipping").lower()

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    ysize 64
    xsize 222
    background Frame("skip_an", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    kerning 0
    yalign 0.5
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [ (2, "#797979", 0, 0) ]
    color "#f3f2f2"

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"
    size 16
    yalign 0.0


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    kerning 0
    yalign 0.5
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [ (2, "#797979", 0, 0) ]
    color "#f3f2f2"



## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    #### ADD THIS TO MAKE THE PHONE WORK!! :) ###
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
    ####
    ## Indent the rest of the screen
        window:
            style "nvl_window"

            has vbox:
                spacing gui.nvl_spacing

            ## Displays dialogue in either a vpgrid or the vbox.
            if gui.nvl_height:

                vpgrid:
                    cols 1
                    yinitial 1.0

                    use nvl_dialogue(dialogue)

            else:

                use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True, as it is above.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign
    

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [ (2, "#313131", 0, 0) ]

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
