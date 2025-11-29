# Documentation for the Ren'Py Transitions Definition Script
# ----------------------------------------------------------

# Purpose:
# This script defines various transition effects used throughout the game to
# smoothly move between scenes, emphasize moments, or create visual interest.
# 
# MODIFICATION: All transitions now automatically exclude the 'notifications' layer
# to prevent notifications from disappearing during scene transitions.

# Main Components:
# 1. Fade Transitions
# 2. Time Passage Transitions
# 3. Scene Transitions
# 4. Thought and Focus Transitions
# 5. Special Effect Transitions
# 6. Directional Wipes
# 7. Miscellaneous Transitions

# Detailed Usage:
# 1. Fade Transitions:
#    - normalfade: Standard fade for changing POV/camera
#    - flash: Quick white flash effect
#    - blink: Simulates blinking effect
#    Example: scene new_background with normalfade

# 2. Time Passage Transitions:
#    - circlewipe: Indicates time passing
#    - mangaffw: Fast forward effect
#    Example: scene later_that_day with circlewipe

# 3. Scene Transitions:
#    - smoke: Transition to a new character in the same scene
#    - rose: For introducing an episode
#    Example: scene new_character_entry with smoke

# 4. Thought and Focus Transitions:
#    - clouds: For entering/exiting imagination sequences
#    - mangalines: To focus on something specific
#    Example: show mc_thinking with clouds

# 5. Special Effect Transitions:
#    - ripple: Water-like ripple effect
#    - shatter: Glass shattering effect
#    Example: scene dramatic_reveal with shatter

# 6. Directional Wipes:
#    - cwside: Side wipe transition
#    - vertcolor: Vertical color wipe
#    Example: scene next_area with cwside

# 7. Miscellaneous Transitions:
#    - paint: Paint-like transition effect
#    - wet: Water droplet effect
#    Example: scene rainy_day with wet

# Connections to Other Files:
# - These transitions can be used in any script file where scene changes occur.
# - The image files for these transitions (like circlewipe-cw.webp) should be in the game's image directory.

# Maintenance and Expansion:
# - To add new transitions, define them following the existing pattern.
# - Ensure all referenced image files exist in the correct directory.
# - Test new transitions on various devices to ensure compatibility and performance.

# Note for Novices:
# - Transitions are used with 'with' statements after scene, show, or hide commands.
# - The 'ImageDissolve' function uses an image to control the dissolve pattern.
# - Transition duration is typically set in seconds (e.g., 1.0 for one second).

# Remember: While transitions can enhance visual storytelling, overuse can slow down
# the game's pacing. Use them thoughtfully to support the narrative.

init:
    ################################################################################
    ## LAYER EXCLUSION HELPER FUNCTION
    ################################################################################
    
    # Helper function to create transitions that exclude the notifications layer
    # This ensures notifications never disappear during transitions
    python:
        def create_layer_transition(transition_func, exclude_layers=None):
            """
            Creates a transition that applies to all layers except excluded ones
            
            Args:
                transition_func: The transition to apply (e.g., Fade(1.5, 0, 1, color="#16161d"))
                exclude_layers: List of layers to exclude (defaults to ['notifications'])
            
            Returns:
                Dictionary mapping layers to transitions
            """
            if exclude_layers is None:
                exclude_layers = ['notifications']
            
            # Get all layers from config.layers
            all_layers = config.layers if hasattr(config, 'layers') else ['master', 'transient', 'screens', 'overlay']
            
            # Create transition dict for all layers except excluded ones
            transition_dict = {}
            for layer in all_layers:
                if layer not in exclude_layers:
                    transition_dict[layer] = transition_func
            
            return transition_dict
    
    ################################################################################
    ## FADE TRANSITIONS (Modified to exclude notifications layer)
    ################################################################################
    
    # Standard fade transitions - now exclude notifications layer automatically
    define normalfade = create_layer_transition(Fade(0.5, 0, 0.5, color="#16161d"))  # Change perspective POV / camera
    define flash = create_layer_transition(Fade(.05, 0.0, .25, color="#F5F5FA"))
    define blink = create_layer_transition(Fade(.35, 0.7, .5, color="#16161d"))
    define blinkfast = create_layer_transition(Fade(.05, 0.0, .25, color="#16161d"))

    # Slow fade transitions - now exclude notifications layer automatically
    define slowfade = create_layer_transition(Fade(1.5, 0, 1, color="#16161d"))
    define slowfade2 = create_layer_transition(Fade(0, 0, 1.5, color="#16161d"))
    define slowflash = create_layer_transition(Fade(1.5, 0, 1, color="#F5F5FA"))

    ################################################################################
    ## IMAGE DISSOLVE TRANSITIONS (Modified to exclude notifications layer)
    ################################################################################
    
    # Time passage transitions - now exclude notifications layer automatically
    define circlewipe = create_layer_transition(ImageDissolve("images/wipes/circlewipe-cw.webp", 1.0, ramplen=128))  # Time passes
    define ccirclewipe = create_layer_transition(ImageDissolve("images/wipes/circlewipe-ccw.webp", 1.0, ramplen=128))  # Time passes
    define mangaffw = create_layer_transition(ImageDissolve("images/wipes/mangaffw.webp", 1.7, ramplen=120))  # Fast forward (1) same scene
    define bubbles = create_layer_transition(ImageDissolve("images/wipes/bokeh_nb.webp", 1.5, ramplen=256, reverse=True))  # Fast forward (2) same scene
    define mangamove = create_layer_transition(ImageDissolve("images/wipes/mangamove.webp", 1.0, ramplen=64))  # Fast forward (3) same scene

    # Scene transitions - now exclude notifications layer automatically
    define smoke = create_layer_transition(ImageDissolve("images/wipes/smoke.webp", 1.0, reverse=True, ramplen=64))  # Same scene but other character
    define lines = create_layer_transition(ImageDissolve("images/wipes/9.webp", 4.0, ramplen=128))  # End of a scene, focus on something sexy (1)
    define rose = create_layer_transition(ImageDissolve("images/wipes/rose.webp", 4.0, ramplen=128))  # Intro of an episode

    # Thought and focus transitions - now exclude notifications layer automatically
    define clouds = create_layer_transition(ImageDissolve("images/wipes/bites.webp", 3.0, ramplen=128))  # Thinking, imagine (get back to reality)
    define clouds_inverse = create_layer_transition(ImageDissolve("images/wipes/bites.webp", 2.0, ramplen=128, reverse=True))  # Thinking, imagine
    define mangalines = create_layer_transition(ImageDissolve("images/wipes/mangalines.webp", 1.0, ramplen=64))  # Focus on something sexy (1)

    # Special effect transitions - now exclude notifications layer automatically
    define bokeh = create_layer_transition(ImageDissolve("images/wipes/bokeh_bn.webp", 3.0, ramplen=128))
    define bokeh2 = create_layer_transition(ImageDissolve("images/wipes/bokeh_bn.webp", 3.0, ramplen=128, reverse=True))
    define ripple = create_layer_transition(ImageDissolve("images/wipes/ripple.webp", 4.0, reverse=True, ramplen=256))
    define watercolor = create_layer_transition(ImageDissolve("images/wipes/watercolor.webp", 3, reverse=True, ramplen=256))
    define shatter = create_layer_transition(ImageDissolve("images/wipes/shatter.webp", 1.0, ramplen=8))
    define shot = create_layer_transition(ImageDissolve("images/wipes/shot.webp", 2.0, reverse=True, ramplen=128))

    # Directional wipes - now exclude notifications layer automatically
    define cwside = create_layer_transition(ImageDissolve("images/wipes/cw-side.webp", 1.0, 8))
    define cwtop = create_layer_transition(ImageDissolve("images/wipes/cw-top.webp", 1.0, 8))
    define vertcolor = create_layer_transition(ImageDissolve("images/wipes/17.webp", 2.0, ramplen=128))
    define horicolor = create_layer_transition(ImageDissolve("images/wipes/18.webp", 2.0, ramplen=128))
    define vertcolor2 = create_layer_transition(ImageDissolve("images/wipes/17.webp", 4.0))
    define horicolor2 = create_layer_transition(ImageDissolve("images/wipes/18.webp", 4.0))
    define oblique = create_layer_transition(ImageDissolve("images/wipes/24.webp", 2.0, ramplen=256))
    define oblique_r = create_layer_transition(ImageDissolve("images/wipes/24.webp", 2.0, ramplen=256))

    # Miscellaneous transitions - now exclude notifications layer automatically
    define paint = create_layer_transition(ImageDissolve("images/wipes/12.webp", 1.0, 8))
    define blockinside = create_layer_transition(ImageDissolve("images/wipes/22.webp", 1.0, 8))
    define centrifug = create_layer_transition(ImageDissolve("images/wipes/23.webp", 1.0, 8))
    define line80 = create_layer_transition(ImageDissolve("images/wipes/27.webp", 4.0, reverse=True, ramplen=128))
    define dots = create_layer_transition(ImageDissolve("images/wipes/dots.webp", 1.0, ramplen=128))
    define wet = create_layer_transition(ImageDissolve("images/wipes/wet.webp", 1.0, 8))

    ################################################################################
    ## ATL-COMPATIBLE SIMPLE TRANSITIONS
    ################################################################################
    
    # Simple versions of transitions for use in ATL contexts (image animations)
    # ATL cannot use layer dictionary transitions, only simple transitions
    
    # Directional wipe simple transitions
    define horicolor2_simple = ImageDissolve("images/wipes/18.webp", 4.0)
    define vertcolor2_simple = ImageDissolve("images/wipes/17.webp", 4.0)
    define horicolor_simple = ImageDissolve("images/wipes/18.webp", 2.0, ramplen=128)
    define vertcolor_simple = ImageDissolve("images/wipes/17.webp", 2.0, ramplen=128)
    
    # Scene transition simple versions
    define mangamove_simple = ImageDissolve("images/wipes/mangamove.webp", 1.0, ramplen=64)
    define smoke_simple = ImageDissolve("images/wipes/smoke.webp", 1.0, reverse=True, ramplen=64)
    define bubbles_simple = ImageDissolve("images/wipes/bokeh_nb.webp", 1.5, ramplen=256, reverse=True)
    define watercolor_simple = ImageDissolve("images/wipes/watercolor.webp", 3, reverse=True, ramplen=256)
    define cwside_simple = ImageDissolve("images/wipes/cw-side.webp", 1.0, 8)
    
    # Thought and focus simple transitions
    define clouds_simple = ImageDissolve("images/wipes/bites.webp", 3.0, ramplen=128)
    define clouds_inverse_simple = ImageDissolve("images/wipes/bites.webp", 2.0, ramplen=128, reverse=True)
    
    # Fade simple transitions
    define normalfade_simple = Fade(0.5, 0, 0.5, color="#16161d")
    define slowfade_simple = Fade(1.5, 0, 1, color="#16161d")
    define flash_simple = Fade(.05, 0.0, .25, color="#F5F5FA")
    define blink_simple = Fade(.35, 0.7, .5, color="#16161d")
    
    # Basic dissolve simple transitions
    define dissolve_simple = Dissolve(0.5)
    define dissolve_slow = Dissolve(1.0)
    define dissolve_fast = Dissolve(0.25)

    ################################################################################
    ## INTEGRATION NOTES
    ################################################################################
    
    ## WHAT CHANGED:
    ## - All transitions now use create_layer_transition() helper function
    ## - This automatically excludes the 'notifications' layer from all transitions
    ## - Your existing code works exactly the same: scene bg with slowfade
    ## - Notifications will never disappear during any transition
    ## - Added ATL-compatible simple transitions for image animations
    ##
    ## HOW IT WORKS:
    ## - create_layer_transition() converts simple transitions to layer dictionaries
    ## - Each transition applies to all layers EXCEPT 'notifications'
    ## - The notifications layer remains completely unaffected by scene transitions
    ## - Simple transitions (*_simple) can be used in ATL contexts
    ##
    ## BENEFITS:
    ## - No need to change any existing script files
    ## - All transitions automatically preserve notifications
    ## - Clean separation of concerns
    ## - Future transitions automatically inherit notification immunity
    ## - ATL animations work without errors
    ##
    ## USAGE (unchanged):
    ## scene new_background with slowfade    # Notifications stay visible!
    ## show character with normalfade        # Notifications stay visible!
    ## hide overlay with circlewipe          # Notifications stay visible!
    ##
    ## ATL USAGE (use simple versions):
    ## image animated_bg:
    ##     "bg1.jpg" with horicolor2_simple
    ##     pause 2.0
    ##     "bg2.jpg" with vertcolor2_simple
    ##     pause 2.0
    ##     repeat