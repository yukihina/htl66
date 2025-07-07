# Documentation for the Ren'Py Character Definition Script
# --------------------------------------------------------

# Purpose:
# This script defines all characters used in the game, including their visual and audio properties, 
# as well as relationship terms. It's crucial for dialogue presentation and character interactions.

# Main Components:
# 1. Helper Functions:
#    - ensure_opus(): Ensures audio files have the .opus extension.
#    - create_character(): Creates a standard speaking character.
#    - create_thinking_character(): Creates a character for internal thoughts.
#    - create_nvl_character(): Creates a character for NVL-mode dialogue.

# 2. Patching System:
#    - Determines if a patch has been applied, affecting certain character definitions.

# 3. Character Definitions:
#    - Defines main characters, secondary characters, and their variants (thinking, yelling, etc.).

# 4. Relationship Definitions:
#    - Defines relationship terms used in the game, with variations based on the patched status.

# Detailed Usage:
# 1. Creating Characters:
#    Characters are created using the helper functions. For example:
#    $ amb = create_character("Amber", "#FF3333", "#ffd3d3")
#    $ amb_t = create_thinking_character("Amber", "#FF3333", "#d19494")

# 2. Using Characters in Dialogue:
#    Once defined, characters can be used directly in the script:
#    amb "Hello, I'm Amber."
#    amb_t "What should I do next?"

# 3. NVL Characters:
#    For novel-style dialogue, use NVL characters:
#    amb_nvl "This is a long passage of text..."

# 4. Relationship Terms:
#    Access relationship terms using the defined variables:
#    "She's my [mo_r_low]."

# 5. Patched Content:
#    Some character definitions change based on the patch status:
#    if patched:
#        $ eli = Character("Mom", ...)
#    else:
#        $ eli = Character("Elizabeth", ...)

# Adding New Characters:
# To add a new character:
# 1. Use the appropriate create_*_character function in the define_characters function.
# 2. Add the character to the characters dictionary.
# 3. If needed, create thinking and NVL variants.

# Connections to Other Files:
# - This script is closely linked to core.rpy, which uses these character definitions for the relationship system.
# - The characters defined here are used throughout the game's script files for dialogue.
# - Style definitions in def_styles.rpy may affect how these characters' dialogue is displayed.

# Maintenance and Expansion:
# When updating this script:
# 1. Ensure consistency in naming conventions (e.g., character shorthand like 'amb' for Amber).
# 2. When adding new characters, follow the established patterns for main and secondary characters.
# 3. Update the patching system if new conditional character definitions are needed.
# 4. If adding new relationship terms, ensure they're added to both patched and non-patched dictionaries.

# Note for Novices:
# - Character objects in Ren'Py control how dialogue is displayed.
# - The `who_color` parameter sets the color of the character's name.
# - The `what_color` parameter sets the color of the character's dialogue.
# - NVL mode is used for novel-style text that fills the screen, as opposed to the default dialogue box.
# - The `patched` variable allows for different game versions or content variations.

# Remember: Changes to character definitions can have wide-reaching effects across your entire game script. 
# Always test thoroughly after making modifications!

init -1002 python:
    if not hasattr(renpy.persistent, "patch_applied"):
        renpy.persistent.patch_applied = False

    global patch_activated
    patch_activated = False


init -1001 python:
    patched = renpy.persistent.patch_applied

init -1000 python:
    def create_character(name, who_color, what_color, suffix='[dialogue_bubble]', yalign=0.0, yoffset=9, **kwargs):
        return Character(name, who_color=who_color, what_color=what_color, who_suffix=suffix, yalign=yalign, yoffset=yoffset, **kwargs)

    def create_thinking_character(name, who_color, what_color, yalign=0.0, yoffset=9):
        return Character(name, who_color=who_color, what_color=what_color, what_prefix='{fii}', what_suffix='{/fii}', who_suffix='[thinking_bubble]', yalign=yalign, yoffset=yoffset)

    def create_nvl_character(name, who_color, what_color, callback_name=None):
        if callback_name:
            callback = globals().get(callback_name)
        else:
            callback = None
        return Character(name, who_color=who_color, what_color=what_color, kind=nvl, callback=callback)

init -999 python:
    def define_characters(patched):
        characters = {}

        characters["amb"] = create_character("Amber", "#FF3333", "#ffd3d3")
        characters["amb_t"] = create_thinking_character("Amber", "#FF3333", "#d19494")
        characters["amb_y"] = create_character("Amber", "#FF3333", "#ffd3d3", '[screaming_bubble]')
        characters["amb_nvl"] = create_nvl_character("Amber", "#FF3333", "#ffd3d3", callback_name="Phone_ReceiveSound")

        characters["anto"] = create_character("Antonella", "#556B2F", "#E8F0E0")
        characters["anto_t"] = create_thinking_character("Antonella", "#556B2F", "#D8E0D0")
        characters["anto_y"] = create_character("Antonella", "#556B2F", "#E8F0E0", '[screaming_bubble]')
        characters["anto_nvl"] = create_nvl_character("Antonella", "#556B2F", "#E8F0E0", callback_name="Phone_ReceiveSound")

        characters["mad"] = create_character("Madison", "#2E8B57", "#E8F5E9")
        characters["mad_t"] = create_thinking_character("Madison", "#2E8B57", "#C8E6C9")
        characters["mad_y"] = create_character("Madison", "#2E8B57", "#E8F5E9", '[screaming_bubble]')
        characters["mad_nvl"] = create_nvl_character("Madison", "#2E8B57", "#E8F5E9", callback_name="Phone_ReceiveSound")

        characters["arl"] = create_character("Arlette", "#dfc577", "#e5dab8")
        characters["arl_t"] = create_thinking_character("Arlette", "#dfc577", "#b1a88d")
        characters["arl_nvl"] = create_nvl_character("Arlette", "#dfc577", "#e5dab8", callback_name="Phone_ReceiveSound")

        characters["isa"] = create_character("Isabella", "#00CED1", "#E0F5F5")
        characters["isa_t"] = create_thinking_character("Isabella", "#00CED1", "#D0EBEB")
        characters["isa_y"] = create_character("Isabella", "#00CED1", "#E0F5F5", '[screaming_bubble]')
        characters["isa_nvl"] = create_nvl_character("Isabella", "#00CED1", "#E0F5F5")

        characters["kan"] = create_character("Kanae", "#33ffff", "#b2ffff")
        characters["kan_nvl"] = create_nvl_character("Kanae", "#33ffff", "#b2ffff", callback_name="Phone_ReceiveSound")

        characters["mc_t"] = create_thinking_character("[mc_name]", "#4169E1", "#DBC071")
        characters["mc_s"] = create_character("[mc_name]", "#4169E1", "#E6C87A", '[monologue_bubble]')
        characters["mc_y"] = create_character("[mc_name]", "#4169E1", "#E6C87A", '[screaming_bubble]')
        characters["mc_nvl"] = create_nvl_character("[mc_name]", "#4169E1", "#E6C87A", callback_name="Phone_SendSound")

        characters["nana"] = create_character("Nanami", "#9B59D0", "#F2E6FF")
        characters["nana_t"] = create_thinking_character("Nanami", "#9B59D0", "#E6D6F5")
        characters["nana_y"] = create_character("Nanami", "#9B59D0", "#F2E6FF", '[screaming_bubble]')
        characters["nana_nvl"] = create_nvl_character("Nanami", "#9B59D0", "#F2E6FF", callback_name="Phone_ReceiveSound")

        characters["pa_s"] = create_character("Paz", "#DA70D6", "#F4E6F4")
        characters["pa_t"] = create_thinking_character("Paz", "#DA70D6", "#E6D6E6")
        characters["paz_nvl"] = create_nvl_character("Paz", "#DA70D6", "#F4E6F4", callback_name="Phone_ReceiveSound")

        if patched:
            characters["eli"] = Character("Mom", who_color="#CC6699", what_color="#F6E6F0", who_suffix='[dialogue_bubble]', yalign=1)
            characters["eli_y"] = Character("Mom", who_color="#CC6699", what_color="#F6E6F0", who_suffix='[screaming_bubble]', yalign=1)
            characters["mic"] = Character("Dad", who_color="#BDB6B1", what_color="#BFB7B4", who_suffix='[dialogue_bubble]', yalign=1)
            characters["eli_nvl"] = create_nvl_character("Mom", "#CC6699", "#F6E6F0", callback_name="Phone_ReceiveSound")
        else:
            characters["eli"] = Character("Elizabeth", who_color="#CC6699", what_color="#F6E6F0", who_suffix='[dialogue_bubble]', yalign=1)
            characters["eli_y"] = Character("Elizabeth", who_color="#CC6699", what_color="#F6E6F0", who_suffix='[screaming_bubble]', yalign=1)
            characters["mic"] = Character("Michael", who_color="#BDB6B1", what_color="#BFB7B4", who_suffix='[dialogue_bubble]', yalign=1)
            characters["eli_nvl"] = create_nvl_character("Elizabeth", "#CC6699", "#F6E6F0", callback_name="Phone_ReceiveSound")

        characters["aoi"] = create_character("Aoi", "#ad594c", "#e5baac")
        characters["aya"] = create_character("Aya", "#56494b", "#b3a1a3")
        characters["hid"] = create_character("Hideo", "#a2b1d0", "#dae2f2")
        characters["kit"] = create_character("Kitsune", "#00A86B", "#00CC99")
        characters["rin"] = create_character("Rina", "#d18376", "#ffd4cc")
        characters["shi"] = create_character("Shigeo", "#C5C5ED", "#E6E6FA")
        characters["tak"] = create_character("Takeo", "#6d6c6c", "#b4b4b4")
        characters["yas"] = create_character("Yakuza Shatei", "#837c5e", "#aaaaa8")
        characters["yaw"] = create_character("Yakuza Wakagashira", "#8bf5f0", "#98bdbb")
        characters["hir"] = create_character("Hiroshi", "#FFA500", "#FFF2E6")
        characters["ed"] = create_character("Echo Dot", "#00A4E4", "#B3E5FC")
        characters["surg"] = create_character("The Surgeon", "#58aeda", "#7fa5b5")

        return characters


    def define_relationships(patched):
        if patched:
            return {
                "mo_r": "Mom", "mo_r_low": "mom", "mo_full_r": "Mother", "mo_full_r_low": "mother",
                "da_r": "Dad", "da_r_low": "dad", "da_full_r": "Father", "da_full_r_low": "father",
                "br_r": "Bro", "br_r_low": "bro", "br_full_r": "Brother", "br_full_r_low": "brother",
                "si_r": "Sis", "si_r_low": "sis", "si_full_r": "Sister", "si_full_r_low": "sister",
                "gra_r": "Grandma", "gra_r_low": "grandma", "gra_full_r": "Grandmother", "gra_full_r_low": "grandmother",
                "grf_r": "Grandfather", "grf_r_low": "grandfather", "grf_short_r": "Grandpa", "grf_short_r_low": "grandpa",
                "dau_r": "Daughter", "dau_r_low": "daughter",
                "so_r": "Son", "so_r_low": "son",
                "chi_r": "children", "sib_r": "sibling",
                "aun_r": "Aunt", "aun_r_low": "aunt", "au_r": "Auntie", "au_r_low": "auntie",
                "fm_r": "Family", "fm_r_low": "family",
                "unc_r": "Uncle", "unc_r_low": "uncle",
                "neph_r": "Nephew", "neph_r_low": "nephew",
                "niec_r": "Niece", "niec_r_low": "niece",
                "cou_r": "Cousin", "cou_r_low": "cousin",
                "gran_r": "Granddaughter", "gran_r_low": "granddaughter",
                "gson_r": "Grandson", "gson_r_low": "grandson",
                "half_sib_r": "Half-sibling", "half_sib_r_low": "half-sibling",
                "stp_sib_r": "Sibling", "stp_sib_r_low": "sibling",
                "stp_mo_r": "Stepmother", "stp_mo_r_low": "stepmother",
                "stp_fa_r": "Stepfather", "stp_fa_r_low": "stepfather",
                "inlaw_r": "In-law", "inlaw_r_low": "in-law",
                "daddy_r": "Daddy", "daddy_r_low": "daddy",
                "d_daddy_r": "D-daddy", "d_daddy_r_low": "d-daddy",
                "mommy_r": "Mommy", "mommy_r_low": "mommy",
                "sis_r": "Sis", "sis_r_low": "sis",
                "bro_r": "Bro", "bro_r_low": "bro",
                "cous_r": "Cousin", "cous_r_low": "cousin",
                "granny_r": "Granny", "granny_r_low": "granny", 
                "grampy_r": "Grampy", "grampy_r_low": "grampy",
                "half_sis_r": "Half-sister", "half_sis_r_low": "half-sister",
                "half_bro_r": "Half-brother", "half_bro_r_low": "half-brother",
                "step_sis_r": "Step-sister", "step_sis_r_low": "step-sister",
                "step_bro_r": "Step-brother", "step_bro_r_low": "step-brother",
                "sis_inlaw_r": "Sister-in-law", "sis_inlaw_r_low": "sister-in-law",
                "bro_inlaw_r": "Brother-in-law", "bro_inlaw_r_low": "brother-in-law"
            }
        else:
            return {
                "mo_r": "Landlady", "mo_r_low": "landlady", "mo_full_r": "Landlady", "mo_full_r_low": "landlady",
                "da_r": "Landlord", "da_r_low": "landlord", "da_full_r": "Landlord", "da_full_r_low": "landlord",
                "br_r": "Friend", "br_r_low": "friend", "br_full_r": "Close Friend", "br_full_r_low": "close friend",
                "si_r": "Friend", "si_r_low": "friend", "si_full_r": "Close Friend", "si_full_r_low": "close friend",
                "gra_r": "Elderly Lady", "gra_r_low": "elderly lady", "gra_full_r": "Elderly Lady", "gra_full_r_low": "elderly lady",
                "grf_r": "Elderly Gentleman", "grf_r_low": "elderly gentleman", "grf_short_r": "Elderly Gentleman", "grf_short_r_low": "elderly gentleman",
                "dau_r": "Young Lady", "dau_r_low": "young lady",
                "so_r": "Young Man", "so_r_low": "young man",
                "chi_r": "young people", "sib_r": "friend",
                "aun_r": "Older Friend", "aun_r_low": "older friend", "au_r": "Older Friend", "au_r_low": "older friend",
                "fm_r": "Household", "fm_r_low": "household",
                "unc_r": "Older Friend", "unc_r_low": "older friend",
                "neph_r": "Younger Friend", "neph_r_low": "younger friend",
                "niec_r": "Younger Friend", "niec_r_low": "younger friend",
                "cou_r": "Friend", "cou_r_low": "friend",
                "gran_r": "Young Lady", "gran_r_low": "young lady",
                "gson_r": "Young Man", "gson_r_low": "young man",
                "half_sib_r": "Close Friend", "half_sib_r_low": "close friend",
                "stp_sib_r": "Friend", "stp_sib_r_low": "friend",
                "stp_mo_r": "Older Lady", "stp_mo_r_low": "older lady",
                "stp_fa_r": "Older Gentleman", "stp_fa_r_low": "older gentleman",
                "inlaw_r": "In-law", "inlaw_r_low": "in-law",
                "daddy_r": "Older Gentleman", "daddy_r_low": "older gentleman",
                "d_daddy_r": "O-older G-gentleman", "d_daddy_r_low": "o-older g-gentleman",
                "mommy_r": "Older Lady", "mommy_r_low": "older lady",
                "sis_r": "Friend", "sis_r_low": "friend",
                "bro_r": "Friend", "bro_r_low": "friend",
                "cous_r": "Friend", "cous_r_low": "friend",
                "granny_r": "Elderly Lady", "granny_r_low": "elderly lady",
                "grampy_r": "Elderly Gentleman", "grampy_r_low": "elderly gentleman",
                "half_sis_r": "Close Friend", "half_sis_r_low": "close friend", 
                "half_bro_r": "Close Friend", "half_bro_r_low": "close friend",
                "step_sis_r": "Friend", "step_sis_r_low": "friend",
                "step_bro_r": "Friend", "step_bro_r_low": "friend",
                "sis_inlaw_r": "In-law", "sis_inlaw_r_low": "in-law",
                "bro_inlaw_r": "In-law", "bro_inlaw_r_low": "in-law"
            }

init -998 python:
    characters = define_characters(patched)
    globals().update(characters)

    relationships = define_relationships(patched)
    globals().update(relationships)

    if not patched:
        import re

        replace_dict = {
            "mama": "landlady",
            "momma": "landlady",
            "moms": "landladies",
            "daddies": "landlords",
            "daughters": "young ladies",
            "mommy": "older lady",
            "aunty": "older friend",
            "families": "households",
            "incest": "affection",
            "siblings": "friends",
            "incestuous": "affectionate"
        }

        def game_text_mod(text):
            rc = re.compile('\\b|\\b'.join(map(re.escape, replace_dict)), re.I)
            def translate(match):
                key = match.group(0).lower()
                suffix = "'s" if "'s" in key else ""
                key = key[:-2] if suffix else key
                value = replace_dict[key]
                if match.group(0).isupper():
                    value = value.upper()
                elif match.group(0).istitle():
                    value = value.title()
                return value + suffix
            return rc.sub(translate, text)

        config.say_menu_text_filter = game_text_mod