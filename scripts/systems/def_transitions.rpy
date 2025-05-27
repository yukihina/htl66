# Documentation for the Ren'Py Transitions Definition Script
# ----------------------------------------------------------

# Purpose:
# This script defines various transition effects used throughout the game to
# smoothly move between scenes, emphasize moments, or create visual interest.

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
    # Common fades
    define normalfade = Fade(0.5, 0, 0.5, color="#16161d")  # Change perspective POV / camera
    define flash = Fade(.05, 0.0, .25, color="#F5F5FA")
    define blink = Fade(.35, 0.7, .5, color="#16161d")
    define blinkfast = Fade(.05, 0.0, .25, color="#16161d")

    # Slow fades
    define slowfade = Fade(1.5, 0, 1, color="#16161d")
    define slowfade2 = Fade(0, 0, 1.5, color="#16161d")
    define slowflash = Fade(1.5, 0, 1, color="#F5F5FA")

    # Time passage transitions
    define circlewipe = ImageDissolve("images/wipes/circlewipe-cw.webp", 1.0, ramplen=128)  # Time passes
    define ccirclewipe = ImageDissolve("images/wipes/circlewipe-ccw.webp", 1.0, ramplen=128)  # Time passes
    define mangaffw = ImageDissolve("images/wipes/mangaffw.webp", 1.7, ramplen=120)  # Fast forward (1) same scene
    define bubbles = ImageDissolve("images/wipes/bokeh_nb.webp", 1.5, ramplen=256, reverse=True)  # Fast forward (2) same scene
    define mangamove = ImageDissolve("images/wipes/mangamove.webp", 1.0, ramplen=64)  # Fast forward (3) same scene

    # Scene transitions
    define smoke = ImageDissolve("images/wipes/smoke.webp", 1.0, reverse=True, ramplen=64)  # Same scene but other character
    define lines = ImageDissolve("images/wipes/9.webp", 4.0, ramplen=128)  # End of a scene, focus on something sexy (1)
    define rose = ImageDissolve("images/wipes/rose.webp", 4.0, ramplen=128)  # Intro of an episode

    # Thought and focus transitions
    define clouds = ImageDissolve("images/wipes/bites.webp", 3.0, ramplen=128)  # Thinking, imagine (get back to reality)
    define clouds_inverse = ImageDissolve("images/wipes/bites.webp", 2.0, ramplen=128, reverse=True)  # Thinking, imagine
    define mangalines = ImageDissolve("images/wipes/mangalines.webp", 1.0, ramplen=64)  # Focus on something sexy (1)

    # Special effect transitions
    define bokeh = ImageDissolve("images/wipes/bokeh_bn.webp", 3.0, ramplen=128)
    define bokeh2 = ImageDissolve("images/wipes/bokeh_bn.webp", 3.0, ramplen=128, reverse=True)
    define ripple = ImageDissolve("images/wipes/ripple.webp", 4.0, reverse=True, ramplen=256)
    define watercolor = ImageDissolve("images/wipes/watercolor.webp", 3, reverse=True, ramplen=256)
    define shatter = ImageDissolve("images/wipes/shatter.webp", 1.0, ramplen=8)
    define shot = ImageDissolve("images/wipes/shot.webp", 1.0, ramplen=8)

    # Directional wipes
    define cwside = ImageDissolve("images/wipes/cw-side.webp", 1.0, 8)
    define cwtop = ImageDissolve("images/wipes/cw-top.webp", 1.0, 8)
    define vertcolor = ImageDissolve("images/wipes/17.webp", 2.0, ramplen=128)
    define horicolor = ImageDissolve("images/wipes/18.webp", 2.0, ramplen=128)
    define vertcolor2 = ImageDissolve("images/wipes/17.webp", 4.0)
    define horicolor2 = ImageDissolve("images/wipes/18.webp", 4.0)
    define oblique = ImageDissolve("images/wipes/24.webp", 2.0, ramplen=256)
    define oblique_r = ImageDissolve("images/wipes/24.webp", 2.0, ramplen=256)

    # Miscellaneous transitions
    define paint = ImageDissolve("images/wipes/12.webp", 1.0, 8)
    define blockinside = ImageDissolve("images/wipes/22.webp", 1.0, 8)
    define centrifug = ImageDissolve("images/wipes/23.webp", 1.0, 8)
    define line80 = ImageDissolve("images/wipes/27.webp", 4.0, reverse=True, ramplen=128)
    define dots = ImageDissolve("images/wipes/dots.webp", 1.0, ramplen=128)
    define wet = ImageDissolve("images/wipes/wet.webp", 1.0, 8)


