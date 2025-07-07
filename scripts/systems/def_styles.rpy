# Documentation for the Ren'Py Style Definition Script
# ----------------------------------------------------

# Purpose:
# This script defines the visual styles used throughout the game interface. It controls 
# the appearance of text, buttons, menus, and other UI elements, ensuring a consistent look and feel.

# Main Components:
# 1. Text Styles:
#    - Defines font, size, color, and other properties for various text elements.

# 2. Button Styles:
#    - Sets the appearance and behavior of different types of buttons.

# 3. Choice Menu Styles:
#    - Determines the look of choice menus presented to the player.

# 4. Dialogue and Name Box Styles:
#    - Controls the appearance of character names and dialogue boxes.

# 5. User Interface Element Styles:
#    - Defines styles for various UI components like scrollbars, sliders, and frames.

# Detailed Usage:
# 1. Text Styling:
#    - General text properties:
#      define gui.text_size = 30
#      define gui.text_color = '#E5E5E5'
#    - These affect all default text in the game.

# 2. Button Styling:
#    - Different button types have their own styles:
#      style mm_widget is button:
#          activate_sound sfx_scup
#          hover_sound sfx_spop
#    - This defines sounds for main menu widget buttons.

# 3. Choice Menu Styling:
#    - Styles for player choices:
#      style choicemn is button:
#          xalign 1.0
#          activate_sound sfx_magic
#    - This sets the alignment and sound for choice menu buttons.

# 4. Character Name Styling:
#    define gui.name_text_font = "fonts/newzenbold2.ttf"
#    define gui.name_text_size = 36
#    - These define the font and size for character names in dialogue.

# 5. Custom Text Tags:
#    - The script defines custom text tags like {fa} for fairy text, {fib} for Fibra font, etc.
#    - These can be used in dialogue to change text appearance mid-sentence.

# Adding New Styles:
# To add a new style:
# 1. Use the 'style' keyword followed by the style name.
# 2. Define properties within the style block.
# Example:
# style new_button_style is button:
#     xalign 0.5
#     yalign 0.5
#     background "new_button_bg.png"

# Connections to Other Files:
# - This script affects the visual presentation of characters defined in def_chars.rpy.
# - The styles defined here are used in screens.rpy for various game screens.
# - Sound effects referenced in button styles should be defined in sound_assets.rpy.

# Maintenance and Expansion:
# When updating this script:
# 1. Ensure new styles are consistent with the existing visual theme.
# 2. When modifying existing styles, check how changes affect all screens and dialogue.
# 3. If adding new fonts, make sure they are included in the game's files.
# 4. Test on different screen sizes to ensure responsive design.

# Note for Novices:
# - Styles in Ren'Py cascade, meaning a style can inherit properties from another style.
# - The 'is' keyword is used for style inheritance.
# - Properties like 'xalign' and 'yalign' control positioning (0.0 is left/top, 1.0 is right/bottom).
# - Color can be specified in hexadecimal (#RRGGBB) or as named colors.

# Remember: Changes to styles can dramatically affect the game's look. Always preview changes 
# in various contexts to ensure they work well throughout the game!

init:    
    ################################
    ###### ----- TXTBOX ----- ######
    ################################

    define gui.text_size = 30
    define gui.text_line_spacing = 0
    define gui.text_font = "fonts/omnes.otf"
    define gui.text_color = '#E5E5E5'
    define gui.text_kerning = 1


    ################################
    ###### --- MENU BTNS ---- ######
    ################################

    style mm_widget is button:
        activate_sound sfx_scup
        hover_sound sfx_spop

    style igm_button is button:
        activate_sound sfx_magic
        hover_sound sfx_cute_igbutton   

    style mmenu_btn is button:
        xalign 1.0
        activate_sound sfx_magic
        hover_sound sfx_blip


    style mmenu_btn_text is text:
        kerning -1
        xcenter 0.5
        size 30
        hover_color "#ef9fec"
        font "fonts/UbuntuTitling-Bold.ttf"
        outlines [ (3, "#321414", 0, 0) ]
        color "#f3f2f2"

    ################################
    ###### ---- CHAR NAME --- ######
    ################################

    define gui.name_text_font = "fonts/newzenbold2.ttf"
    define gui.name_text_size = 36
    define gui.name_text_kerning = 0
    define gui.name_text_outlines = [(3, "#1f1f1fff", 0,0)]
    
    ################################
    ###### ----- CHOICES ---- ######
    ################################

    image greencrcl:
        "gui/green_circle.png"
        yalign 0.5
        xalign 1.0
        block:
            easein 1.5 alpha 1.0
            easein 1.5 alpha 0.0
            repeat

    style choicemn is button:
        xalign 1.0
        activate_sound sfx_magic
        hover_sound sfx_blip
        hover_foreground "greencrcl"

    define gui.choice_button_text_font = "fonts/UbuntuTitling-Bold.ttf"
    define gui.choice_button_text_size = 28
    define gui.choice_button_text_kerning = -1
    define gui.choice_button_text_idle_color = "#3f3c38"
    define gui.choice_button_text_hover_color = "#27dc95"
    define gui.choice_button_text_idle_outlines = [ (2, "#ffffffff", 0, 0) ]
    define gui.choice_button_text_hover_outlines = [ (2, "#000000ff", 0, 0) ]
    define gui.choice_button.hover_background = "gui/green_circle.png"


    define gui.choice_button_borders = Borders(20, 20, 20, 20, 10, -5, 10, -5)
    define gui.choice_button_tile = False
    define gui.choice_button_text_xalign = 0.0

    style choice_button2_text is choice_button_text
    style choice_button3_text is choice_button_text
    style choice_button4_text is choice_button_text
    style choice_button5_text is choice_button_text
    style choice_button6_text is choice_button_text


    ################################
    ###### ---- BUBBLES ----- ######
    ################################
    define thinking_bubble = "{image=thinking}"
    define monologue_bubble = "{image=monologue}"
    define dialogue_bubble = "{image=dialogue}"
    define screaming_bubble = "{image=screaming}"

    ################################
    ###### -- TITLES - ######
    ################################
    style title_screen_jp:
        size 150
        outlines [ (4, "#535353", 0, 0) ]
        font "fonts/wd7.otf"
        color "#F5F5F5"
        xalign 0.5
        yalign 0.9
        xanchor center
        yanchor center

    style title_screen:
        size 150
        outlines [ (4, "#535353", 0, 0) ]
        font "fonts/omnes.otf"
        color "#F5F5F5"
        xalign 0.5
        yalign 0.9
        xanchor center
        yanchor center

    style minutes:
        size 150
        outlines [ (4, "#535353", 0, 0) ]
        font "fonts/quicksand.ttf"
        color "#F5F5F5"
        text_align 0.5
        xalign 0.5
        yalign 0.9

    style location:
        size 50
        outlines [ (4, "#535353", 0, 0) ]
        font "fonts/omnes.otf"
        color "#F5F5F5"
        xalign 0.85
        yalign 0.8

    style title_screen_number:
        size 800
        kerning -1
        outlines [ (2, "#535353", 0, 0) ]
        font "fonts/omnes.otf"
        color "#a9a9a9a9"
        xalign 0.5
        yalign 0.6
        xanchor center
        yanchor center