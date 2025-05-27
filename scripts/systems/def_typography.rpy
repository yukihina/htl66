# Documentation for the Ren'Py Typography Definition Script
# ---------------------------------------------------------

# Purpose:
# This script defines custom text tags that can be used to apply special
# typographic styles to text within the game's dialogue and UI.

# Main Components:
# Custom text tags for various font styles and text effects.

# Detailed Usage:
# 1. Fairy Text Tag:
#    - Tag: {fa}
#    - Effect: Changes text to Fairymuffinroundpop font
#    Example: "This is {fa}fairy-like{/fa} text."

# 2. Fibra Bold Tag:
#    - Tag: {fib}
#    - Effect: Changes text to FibraOneUltraBoldIt font
#    Example: "This is {fib}bold fibra{/fib} text."

# 3. Fibra Italic Tag:
#    - Tag: {fii}
#    - Effect: Changes text to FibraOneRegularIt font
#    Example: "This is {fii}italic fibra{/fii} text."

# 4. Mr. Brown Tag:
#    - Tag: {vo}
#    - Effect: Changes text to mrbrown font
#    Example: "This is in {vo}Mr. Brown{/vo} style."

# 5. Market Alt Tag:
#    - Tag: {mka}
#    - Effect: Applies specific size, kerning, and font (Omnes) to text
#    Example: "This is {mka}market alternative{/mka} style."

# 6. Market Bold Tag:
#    - Tag: {mkb}
#    - Effect: Changes text to MarketBold font
#    Example: "This is {mkb}market bold{/mkb} text."

# 7. Antonella Theme Tag:
#    - Tag: {ath}
#    - Effect: Changes text color to a specific shade (fadadd)
#    Example: "This is in {ath}Antonella's theme color{/ath}."

# 8. Antonella Bold Tag:
#    - Tag: {abo}
#    - Effect: Applies bold, large, colored text for Antonella's dialogue
#    Example: "{abo}Antonella speaks boldly{/abo}"

# Connections to Other Files:
# - These tags can be used in any dialogue or UI text throughout the game's script files.
# - The fonts referenced should be defined and included in the game's font directory.

# Maintenance and Expansion:
# - To add new text tags, follow the pattern of existing tag definitions.
# - Ensure all referenced fonts are included in the game's files.
# - When adding new tags, consider their impact on text readability and overall design consistency.

# Note for Novices:
# - Custom text tags are used within quotation marks in dialogue or UI text.
# - Tags must be closed with a corresponding closing tag (e.g., {fa}text{/fa}).
# - The 'config.custom_text_tags' dictionary is used to register these custom tags with Ren'Py.

# Remember: While custom typography can enhance visual appeal, overuse can lead to 
# readability issues. Use these tags judiciously to highlight important text or 
# create specific moods without overwhelming the player.

    ################################
    ###### --- TYPOGRAPHY --- ######
    ################################
init python:

    def fairy_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"font=/fonts/Fairymuffinroundpop-1GG5e.ttf"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["fa"] = fairy_tag

    def fibra_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"font=/fonts/FibraOneUltraBoldIt.otf"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["fib"] = fibra_tag

    def fibraitalic_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"font=/fonts/FibraOneRegularIt.otf"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["fii"] = fibraitalic_tag

    def mbrown_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"font=/fonts/mrbrown.otf"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["vo"] = mbrown_tag

    def marketalt_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"space=12"),
                (renpy.TEXT_TAG, u"k=2"),
                (renpy.TEXT_TAG, u"size=38"),
                (renpy.TEXT_TAG, u"font=/fonts/omnes.otf"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
                (renpy.TEXT_TAG, u"/size"),
                (renpy.TEXT_TAG, u"/k"),
                (renpy.TEXT_TAG, u"space=12"),
            ]

    config.custom_text_tags["mka"] = marketalt_tag

    def marketb_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"font=/fonts/MarketBold.otf"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/font"),
            ]

    config.custom_text_tags["mkb"] = marketb_tag

    def antoth_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"color=#fadadd"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/color"),
            ]

    config.custom_text_tags["ath"] = antoth_tag

    def antobold_tag(tag, argument, contents):
            return [
                (renpy.TEXT_TAG, u"color=#b76e79"),
                (renpy.TEXT_TAG, u"size=70"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
                (renpy.TEXT_TAG, u"/color"),
            ]

    config.custom_text_tags["abo"] = antobold_tag