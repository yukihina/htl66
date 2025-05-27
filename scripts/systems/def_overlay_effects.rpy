# Documentation for the Ren'Py Overlay Effects Script
# ---------------------------------------------------

# Purpose:
# This script defines various visual overlay effects that can be applied during gameplay
# to enhance the visual experience and create atmosphere.

# Main Components:
# 1. Fog Effect:
#    - Functions to show and hide a fog overlay.
# 2. Noise Effect:
#    - Functions to show and hide a noise overlay.

# Detailed Usage:
# 1. Showing Fog Effect:
#    label showFog(disFog, alpFog, transition=None):
#    - disFog: Dissolve time for fog transitions
#    - alpFog: Alpha (transparency) of the fog
#    - transition: Optional transition effect
#    Example: call showFog(1.0, 0.5)

# 2. Hiding Fog Effect:
#    label hideFog(transition=None):
#    - transition: Optional transition effect
#    Example: call hideFog(dissolve)

# 3. Showing Noise Effect:
#    label showNoise(disNoise, alpNoise, transition=None):
#    - disNoise: Dissolve time for noise transitions
#    - alpNoise: Alpha (transparency) of the noise
#    - transition: Optional transition effect
#    Example: call showNoise(0.5, 0.3)

# 4. Hiding Noise Effect:
#    label hideNoise(transition=None):
#    - transition: Optional transition effect
#    Example: call hideNoise(fade)

# Note: The noise effect is only available on PC versions of the game.

# Connections to Other Files:
# - These effects can be called from any script file in the game.
# - The overlay images (fog_00.png, noise_00.png, etc.) should be defined in visual_assets.rpy.

# Maintenance and Expansion:
# - To add new overlay effects, follow the pattern of existing effects.
# - Ensure new overlay images are properly placed in the game's image directory.
# - When updating, consider performance impact, especially for mobile devices.

# Note for Novices:
# - These effects are called using the 'call' statement in Ren'Py scripts.
# - The 'persistent.effectsOn' variable allows players to toggle effects on/off.
# - 'renpy.variant("pc")' checks if the game is running on a PC.

# Remember: Overuse of visual effects can be distracting or impact performance.
# Use judiciously to enhance the game's atmosphere at key moments.

init python:

    register_3d_layer('master', 'background', 'texture', 'middle', 'forward', 'transient', 'screens', 'overlay')

    ease_value = 30

    ################################
    ###### --- OVERLAY FX --- ######
    ################################
    
    # FOG LAYER----------------------------------------------------------------
label showFog(disFog, alpFog, transition=None):

    if persistent.effectsOn:

        $ dissolveFog = disFog
        $ alphaFog    = alpFog

        image imgFog:
            "fog_00" with Dissolve(dissolveFog)
            alpha alphaFog
            dissolveFog
            "fog_01" with Dissolve(dissolveFog)
            alpha alphaFog
            dissolveFog
            "fog_02" with Dissolve(dissolveFog)
            alpha alphaFog
            dissolveFog
            "fog_03" with Dissolve(dissolveFog)
            alpha alphaFog
            dissolveFog
            repeat

        if transition:
            show expression "imgFog" onlayer texture with transition
        else:
            show expression "imgFog" onlayer texture

    return

label hideFog(transition=None):

    if transition:
        hide expression "imgFog" onlayer texture with transition
    else:
        hide expression "imgFog" onlayer texture

    return



    # NOISE LAYER----------------------------------------------------------------
label showNoise(disNoise, alpNoise, transition=None):
    image imgNoise:
        "noise_00"
        alpha 0
        1.0
        repeat
    # if renpy.variant("pc"):

    #     if persistent.effectsOn:

    #         $ DissolveNoise = disNoise
    #         $ alphaNoise    = alpNoise

    #         image imgNoise:
    #             "noise_00" with Dissolve(DissolveNoise)
    #             alpha alphaNoise
    #             DissolveNoise
    #             "noise_01" with Dissolve(DissolveNoise)
    #             alpha alphaNoise
    #             DissolveNoise
    #             "noise_02" with Dissolve(DissolveNoise)
    #             alpha alphaNoise
    #             DissolveNoise
    #             "noise_03" with Dissolve(DissolveNoise)
    #             alpha alphaNoise
    #             DissolveNoise
    #             repeat

    #         if transition:
    #             show expression "imgNoise" onlayer texture with transition
    #         else:
    #             show expression "imgNoise" onlayer texture
                

    return

label hideNoise(transition=None):

    # if transition:
    #     hide expression "imgNoise" onlayer texture with transition
    # else:
    #     hide expression "imgNoise" onlayer texture


    return
