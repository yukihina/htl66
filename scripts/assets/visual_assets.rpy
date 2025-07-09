## visual_assets.rpy
## Visual Assets System - Complete English Version
## 
## This file contains all visual assets including animated backgrounds,
## menu widgets, character animations, and special effects used throughout
## the game. Features dynamic act-based content and animated elements.
## 
## Features:
## - Act-based main menu backgrounds
## - Animated menu widgets and effects
## - Character animations and special screens
## - Overlay effects (fog, noise, etc.)
## - Dynamic pause generation for smooth animations

################################################################################
## INITIALIZATION AND PERSISTENT DATA
################################################################################

init python:
    ############################################################################
    ## PERSISTENT ACT FLAGS SETUP
    ############################################################################
    
    # Initialize persistent act flags if they don't exist
    # These flags control which act's assets are displayed in menus
    if not hasattr(persistent, "act2_play"):
        persistent.act2_play = False
    if not hasattr(persistent, "act3_play"):
        persistent.act3_play = False
    if not hasattr(persistent, "act4_play"):
        persistent.act4_play = False
    if not hasattr(persistent, "act5_play"):
        persistent.act5_play = False

    import random

    ############################################################################
    ## ACT-BASED IMAGE COLLECTIONS
    ############################################################################
    
    # Act 1 - Default main menu backgrounds
    act1_images = [
        "mainmenubg/amb1.avif",
        "mainmenubg/amb2.avif",
        "mainmenubg/arlette.avif",
        "mainmenubg/arlette2.avif",
        "mainmenubg/eli1.avif",
        "mainmenubg/eli2.avif",
        "mainmenubg/isa1.avif",
        "mainmenubg/isa2.avif",
        "mainmenubg/kana1.avif",
        "mainmenubg/kana2.avif",
        "mainmenubg/mad1.avif",
        "mainmenubg/mad2.avif",
        "mainmenubg/nana1.avif",
        "mainmenubg/nana2.avif",
        "mainmenubg/paz1.avif",
        "mainmenubg/paz2.avif"
    ]

    # Act 2 - Expanded character backgrounds
    act2_images = [
        "mainmenubg/amb02_act2.avif",
        "mainmenubg/amb03_act2.avif",
        "mainmenubg/amb04_act2.avif",
        "mainmenubg/ant01_act2.avif",
        "mainmenubg/ant02_act2.avif",
        "mainmenubg/ant03_act2.avif",
        "mainmenubg/arl01_act2.avif",
        "mainmenubg/eli01_act2.avif",
        "mainmenubg/eli02_act2.avif",
        "mainmenubg/eli03_act2.avif",
        "mainmenubg/evi01_act2.avif",
        "mainmenubg/isa01_act2.avif",
        "mainmenubg/isa02_act2.avif",
        "mainmenubg/kan01_act2.avif",
        "mainmenubg/kan02_act2.avif",
        "mainmenubg/mad01_act2.avif",
        "mainmenubg/mad02_act2.avif",
        "mainmenubg/mic01_act2.avif",
        "mainmenubg/nan01_act2.avif",
        "mainmenubg/nan02_act2.avif",
        "mainmenubg/osa01_act2.avif",
        "mainmenubg/pa01_act2.avif",
        "mainmenubg/pa02_act2.avif",
        "mainmenubg/amb01_act2.avif"
    ]

    # Act 3 - Future content placeholders
    act3_images = [
        "mainmenubg/act3_image1.avif",
        "mainmenubg/act3_image2.avif",
        "mainmenubg/act3_image3.avif",
        "mainmenubg/act3_image4.avif"
        # Add more images as acts are developed
    ]

    # Act 4 - Future content placeholders
    act4_images = [
        "mainmenubg/act4_image1.avif",
        "mainmenubg/act4_image2.avif"
        # Add more images as acts are developed
    ]

    # Act 5 - Future content placeholders
    act5_images = [
        "mainmenubg/act5_image1.avif",
        "mainmenubg/act5_image2.avif"
        # Add more images as acts are developed
    ]

    ############################################################################
    ## IMAGE RANDOMIZATION
    ############################################################################
    
    # Shuffle all image lists for variety in menu backgrounds
    random.shuffle(act1_images)
    random.shuffle(act2_images)
    random.shuffle(act3_images)
    random.shuffle(act4_images)
    random.shuffle(act5_images)

    ############################################################################
    ## DYNAMIC IMAGE SELECTION SYSTEM
    ############################################################################
    
    def get_chosen_images():
        """
        Select appropriate image list based on highest unlocked act.
        Priority system: Act 5 > Act 4 > Act 3 > Act 2 > Act 1 (default)
        """
        if persistent.act5_play:
            return act5_images
        elif persistent.act4_play:
            return act4_images
        elif persistent.act3_play:
            return act3_images
        elif persistent.act2_play:
            return act2_images
        else:
            return act1_images

    # Get the current appropriate image set
    chosen_images = get_chosen_images()

    ############################################################################
    ## RANDOM PAUSE GENERATION FUNCTIONS
    ############################################################################
    
    def get_mmbg_pause():
        """Generate random pause for main menu background transitions"""
        return renpy.random.choice([30, 24, 18, 12])
    
    def get_mmrain_pause():
        """Generate random pause for rain/star effects"""
        return renpy.random.choice([2, 2.4, 3, 0.8, 1.5])
    
    def get_dim_pause():
        """Generate random pause for dim effects"""
        return renpy.random.choice([5, 8, 10, 13])
    
    def get_blink_pause():
        """Generate random pause for blink effects"""
        return renpy.random.choice([0.1, 0.2, 0.3, 0.4])
    
    def get_eyes_pause():
        """Generate random pause for eye animations"""
        return renpy.random.choice([2.5, 1.8, 2, 1.5])

################################################################################
## MAIN MENU ANIMATED BACKGROUNDS
################################################################################

# Dynamic main menu background that cycles through act-appropriate images
image menubg:
    "[chosen_images[0]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[1]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[2]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[3]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[4]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[5]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[6]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[7]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[8]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[9]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[10]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[11]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[12]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[13]]" with vertcolor2
    pause get_mmbg_pause()
    "[chosen_images[14]]" with horicolor2
    pause get_mmbg_pause()
    "[chosen_images[15]]" with vertcolor2
    pause get_mmbg_pause()
    repeat

# Animated star/rain effect for menu backgrounds
image mmbg_rain:
    "mainmenubg/mmbg_star1.webp" with dissolve
    pause get_mmrain_pause()
    "mainmenubg/mmbg_star2.webp" with dissolve
    pause get_mmrain_pause()
    "mainmenubg/mmbg_star3.webp" with dissolve
    pause get_mmrain_pause()
    "mainmenubg/mmbg_star4.webp" with dissolve
    pause get_mmrain_pause()
    "mainmenubg/mmbg_star5.webp" with dissolve
    pause get_mmrain_pause()
    "mainmenubg/mmbg_star6.webp" with dissolve
    pause get_mmrain_pause()
    repeat

################################################################################
## MAIN MENU WIDGET ANIMATIONS
################################################################################

# Animated main menu logo
image mmbg_logo:
    "gui/logo.png"
    pause get_mmbg_pause()
    "gui/logo2.png"
    pause get_mmrain_pause()
    repeat

################################################################################
## IN-GAME MENU WIDGET ANIMATIONS
################################################################################

# In-game menu logo animation
image igm_logo:
    "gui/title_txt.png"
    pause get_mmbg_pause()
    "gui/title_lips.png"
    pause get_mmrain_pause()
    repeat

# Background dimming effect for in-game menus
image igm_dim:
    "gui/bg_dim01.png" with mangamove
    pause get_dim_pause()
    "gui/bg_dim02.png" with mangamove
    pause get_dim_pause()
    repeat

# Skip button animation
image skip_an:
    "gui/skip.png" with dissolve
    pause 0.125
    "gui/skip_2.png" with dissolve
    pause 0.125
    "gui/skip_3.png" with dissolve
    pause 0.125
    "gui/skip_4.png" with dissolve
    pause 0.125
    "gui/skip_5.png" with dissolve
    pause 0.125
    repeat

# Attention/notice icon with pulsing animation
image achtung:
    "gui/icon_notice.png"
    yalign 0.5
    block:
        easein 1.5 alpha 1.0
        pause 1
        easein 1.5 alpha 0.0
        repeat

################################################################################
## HELP SYSTEM ANIMATIONS
################################################################################

# Corruption meter animation for help system
image help_cor:
    zoom 0.6
    "gui/cor_0.png" with dissolve
    pause 2.5
    "gui/cor_1.png" with dissolve
    pause 2.5
    "gui/cor_2.png" with dissolve
    pause 2.5
    "gui/cor_3.png" with dissolve
    pause 2.5
    "gui/cor_4.png" with dissolve
    pause 2.5
    "gui/cor_5.png" with dissolve
    pause 2.5
    repeat

# Trust meter animation for help system
image help_trust:
    zoom 0.6
    "gui/love_0.png" with dissolve
    pause 2.5
    "gui/love_1.png" with dissolve
    pause 2.5
    "gui/love_2.png" with dissolve
    pause 2.5
    "gui/love_3.png" with dissolve
    pause 2.5
    "gui/love_4.png" with dissolve
    pause 2.5
    "gui/love_5.png" with dissolve
    pause 2.5
    repeat

# Integrity meter animation for help system
image help_integrity:
    zoom 0.7
    "gui/stats_mc_0.png" with dissolve
    pause 3.5
    "gui/stats_mc_20.png" with dissolve
    pause 2
    "gui/stats_mc_50.png" with dissolve
    pause 2
    "gui/stats_mc_80.png" with dissolve
    pause 2
    "gui/stats_mc_100.png" with dissolve
    pause 3.5
    repeat

# Virginity status animation for help system
image help_virg:
    zoom 0.7
    "gui/virgin_on.png" with dissolve
    pause 4
    "gui/virgin_off.png" with dissolve
    repeat

# Relationship strikes animation for help system
image help_rel:
    zoom 0.7
    "gui/strike_0.png" with dissolve
    pause 4
    "gui/strike_1.png" with dissolve
    pause 4
    "gui/strike_2.png" with dissolve
    pause 4
    "gui/strike_3.png" with dissolve
    repeat

# Pregnancy status animation for help system
image help_preg:
    zoom 0.7
    "gui/preg_on.png" with dissolve
    pause 4
    "gui/preg_off.png" with dissolve
    pause 4
    repeat

# Camera button states animation (version 1)
image help_camera1:
    "gui/button/cam_active.png" with dissolve
    pause 4
    "gui/button/cam_active_hover.png" with dissolve
    pause 1
    "gui/button/cam_off.png" with dissolve
    pause 8
    "gui/button/cam_hover.png" with dissolve
    pause 1
    repeat

# Camera button states animation (version 2)
image help_camera2:
    "gui/button/cam_off.png" with dissolve
    pause 5
    "gui/button/cam_hover.png" with dissolve
    pause 1
    "gui/button/cam_active.png" with dissolve
    pause 7
    "gui/button/cam_active_hover.png" with dissolve
    pause 1
    repeat

# Stats display toggle animation
image help_stats:
    "gui/stats_off.png" with dissolve
    pause 4.5
    "gui/stats_on.png" with dissolve
    pause 4.5
    repeat

# Assistant feature animation
image help_assist:
    "gui/assist_off.png" with dissolve
    pause 2.5
    "gui/assist_on.png" with dissolve
    pause 1
    "gui/assist_active.png" with dissolve
    pause 4
    "gui/assist_active_hover.png" with dissolve
    pause 1
    repeat

# Dialogue type indicator animation
image help_talk:
    xalign 0.5
    yalign 0.5
    "dialogue" with dissolve
    pause 5
    "monologue" with dissolve
    pause 5
    repeat

################################################################################
## CHARACTER ANIMATIONS
################################################################################

# Yukana character animation
image yukana:
    "gui/yuk_5.png" with horicolor2
    pause get_mmbg_pause()
    "gui/yuk_6.png" with vertcolor2
    pause get_mmbg_pause()
    repeat

# Heart animation with rotation and scaling
image heart:
    "gui/button/heart.png"
    subpixel True
    xpos -40
    ypos -10
    parallel:
        easein 0.5 rotate 6.5
        pause 0.5
        easein 0.5 rotate -6.5
        pause 0.5
        repeat
    parallel:
        easein 0.25 zoom 1.21
        pause 0.25
        easeout 0.25 zoom 1
        pause 0.25
        repeat
    block:
        easein 1.5 ypos -20
        easein 1.5 ypos -10
        repeat

################################################################################
## DIALOGUE STATE ICONS
################################################################################

# Thinking state icon with subtle animation
image thinking:
    "gui/thinking.png"
    subpixel True
    yanchor 0.65
    xoffset -15
    parallel:
        easein 0.5 rotate 1 
        pause 0.5
        easein 0.5 rotate -1 
        pause 0.5
        repeat
    parallel:
        easein 0.25 zoom 1.01 
        pause 0.25
        easeout 0.25 zoom 1 
        pause 0.25
    repeat

# Dialogue state icon with subtle animation
image dialogue:
    "gui/dialogue.png"
    subpixel True
    yanchor 0.75
    xoffset -30
    parallel:
        easein 0.5 rotate 1 
        pause 0.5
        easein 0.5 rotate -1 
        pause 0.5
        repeat
    parallel:
        easein 0.25 zoom 1.01 
        pause 0.25
        easeout 0.25 zoom 1 
        pause 0.25
    repeat

# Monologue state icon with subtle animation
image monologue:
    "gui/monologue.png"
    subpixel True
    yanchor 0.69
    xoffset -25
    parallel:
        easein 0.5 rotate 1 
        pause 0.5
        easein 0.5 rotate -1 
        pause 0.5
        repeat
    parallel:
        easein 0.25 zoom 1.01 
        pause 0.25
        easeout 0.25 zoom 1 
        pause 0.25
    repeat

# Screaming state icon with subtle animation
image screaming:
    "gui/scream.png"
    subpixel True
    yanchor 0.65
    xoffset -7
    parallel:
        easein 0.5 rotate 1 
        pause 0.5
        easein 0.5 rotate -1 
        pause 0.5
        repeat
    parallel:
        easein 0.25 zoom 1.01 
        pause 0.25
        easeout 0.25 zoom 1 
        pause 0.25
    repeat

################################################################################
## BASIC COLOR AND EFFECT IMAGES
################################################################################

# Basic solid color backgrounds
image black = Solid("#000000")
image white = Solid("#F5F5FA")
image eigengrau = Solid("#16161D")

# Overlay effects
image vignette = "common/blacktrans.webp"

################################################################################
## OVERLAY EFFECTS
################################################################################

# Fog overlay effects
image fog_00 = "images/overlay/fog_00.webp"
image fog_01 = "images/overlay/fog_01.webp"
image fog_02 = "images/overlay/fog_02.webp"
image fog_03 = "images/overlay/fog_03.webp"

# Noise overlay effects
image noise_00 = "images/overlay/noise00.webp"
image noise_01 = "images/overlay/noise01.webp"
image noise_02 = "images/overlay/noise02.webp"
image noise_03 = "images/overlay/noise03.webp"

################################################################################
## LOGO AND BRANDING ELEMENTS
################################################################################

# New logo elements for branding
image nl_bg = "gui/new_logo_qori00.webp"
image nl_lo = "gui/new_logo_qori01.webp"
image nl_jp = "gui/new_logo_qori02.webp"
image nl_qo = "gui/new_logo_qori04.webp"
image nl_ga = "gui/new_logo_qori05.webp"

################################################################################
## VIDEO ELEMENTS
################################################################################

# Animated sakura movie with alpha mask
image sakura_movie = Movie(play="images/common/sakura.webm", mask="images/common/sakura_alpha.webm", loop=True)

################################################################################
## ACT ENDING SEQUENCES
################################################################################

# Act I ending background
image act1_ending_bg = "act1_end"

# Act I ending text elements
image the_end_text = Text("THE END", style="the_end_style")
image of_text = Text("of", style="of_style") 
image act_one_text = Text("ACT I", style="act_one_style")
image thank_you_text = Text("Thank you for playing", style="thank_you_style")
image save_reminder_text = Text("(You should save here)", style="save_reminder_style")

################################################################################
## SPECIAL SCREENS
################################################################################

# Forced pause screen for dramatic moments
screen forced_pause():
    modal True
    key "dismiss" action Return()

# Player death POV screen
screen mcpov_dying:
    add "vignette" xpos 0 ypos 0 at pov_die

################################################################################
## COMMENTED OUT ASSETS
################################################################################

# These assets are commented out but preserved for potential future use:

# Star animation (alternative version)
# image star:
#     "gui/button/star.png"
#     subpixel True
#     xpos 43
#     ypos -40
#     block:
#         easein 1.5 ypos -60
#         easein 1.5 ypos -40
#         repeat

# Yes button animation
# image yesb:
#     "gui/button/yesbutton.png"
#     subpixel True
#     xpos 30
#     ypos -47
#     block:
#         easein 1.5 ypos -67 alpha 0.9
#         easein 1.5 ypos -47 alpha 0
#         repeat

# No button animation
# image nob:
#     "gui/button/nobutton.png"
#     subpixel True
#     xpos 30
#     ypos -47
#     block:
#         easein 1.5 ypos -67 alpha 0.9
#         easein 1.5 ypos -47 alpha 0
#         repeat

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to use visual assets in your game:
##
## 1. Act-based backgrounds:
##    - Set persistent.act2_play = True to unlock Act 2 backgrounds
##    - The system automatically uses the highest unlocked act's images
##
## 2. Animated elements:
##    show heart at right
##    show thinking at left
##    
## 3. Help system animations:
##    show help_cor at center
##    pause 10
##    hide help_cor
##
## 4. Overlay effects:
##    show fog_01 zorder 100 with dissolve
##    show noise_02 zorder 101 with dissolve
##
## 5. Dialogue state indicators:
##    show dialogue at right
##    "Character is speaking normally."
##    show monologue at right  
##    "Character is thinking internally."
##
## 6. Adding new acts:
##    - Create act[X]_images list with new background files
##    - Add persistent.act[X]_play flag
##    - Update get_chosen_images() function
##
## 7. Custom animations:
##    - Use the pause generation functions for varied timing
##    - Follow the parallel/block structure for complex animations
##    - Always use subpixel True for smooth movement
##
## 8. Performance considerations:
##    - Large image lists are shuffled only once at startup
##    - Use appropriate zorder values to layer effects properly
##    - Consider file sizes when adding new video elements