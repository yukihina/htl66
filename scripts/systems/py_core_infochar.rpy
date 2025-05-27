# Documentation for the Ren'Py Character Information Management Script
# --------------------------------------------------------------------

# Purpose:
# This script manages character information and relationships in the game.
# It provides a flexible system for defining character attributes and
# dynamically updating character descriptions based on game state.

# Main Components:
# 1. Relationship Term Replacements:
#    - Defines how relationship terms change based on game state (patched/unpatched).
# 2. LoveInterest Class:
#    - Manages information for love interest characters.
# 3. MainCharacter Class:
#    - Manages information for the main character.
# 4. Character Instances:
#    - Creates instances for all major characters in the game.

# Detailed Usage:
# 1. Defining Characters:
#    amber = LoveInterest("Amber", 37, "1.77 m", "79.6 kg", "b 99 - w 66 - h 106", "Character description...")
#    mc = MainCharacter(39, "1.85 m", "85 kg", "MC description...")

# 2. Accessing Character Info:
#    amber.name  # Returns "Amber"
#    amber.age   # Returns 37
#    amber.info  # Returns the full description with dynamic replacements

# 3. Updating Character Info:
#    amber.update_info("New information about Amber.")
#    mc.set_age(40)

# 4. Using Dynamic Descriptions:
#    The 'info' property of characters will automatically update based on the
#    current game state and relationship terms.

# Connections to Other Files:
# - This script is closely tied to core.rpy, which manages character relationships.
# - Character information defined here is used throughout the game's dialogue and story scripts.

# Maintenance and Expansion:
# - When adding new characters, create new LoveInterest or MainCharacter instances.
# - To add new dynamic terms, update the 'replacements' dictionary.
# - Ensure that character descriptions use placeholders (e.g., [mo_r_low]) for dynamic content.

# Note for Novices:
# - The @property decorator in Python allows methods to be accessed like attributes.
# - The replacement system allows for dynamic text that changes based on game state.
# - Character information is centralized here, making it easier to maintain consistency across the game.

# Remember: Keep character descriptions and attributes up-to-date as the story progresses.
# This central management system helps maintain consistency in character portrayals throughout the game.

init python:
    if patched:
        replacements = {
            "mo_full_r_low": "mother",
            "si_full_r_low": "sister",
            "br_full_r_low": "brother",
            "mo_r_low": "mom",
            "da_r_low": "dad",
            "dau_r_low": "daughter",
            "niec_r_low": "niece",
            "fm_r_low": "family",
            "so_r_low": "son",
            "da_r": "Dad",
        }
    else:
        replacements = {
            "mo_full_r_low": "landlady",
            "si_full_r_low": "close friend",
            "br_full_r_low": "close friend",
            "mo_r_low": "landlady",
            "da_r_low": "landlord",
            "dau_r_low": "young lady",
            "niec_r_low": "younger friend",
            "fm_r_low": "household",
            "so_r_low": "young man",
            "da_r": "Landlord",
        }


    class LoveInterest:
        def __init__(self, name, age, height, weight, measurements, info):
            self.name = name
            self.age = age
            self.height = height
            self.weight = weight
            self.measurements = measurements
            self._info = info

        @property
        def info(self):
            info = self._info
            for code, replacement in replacements.items():
                info = info.replace("[" + code + "]", replacement)
            info = info.replace("[mc_name]", mc_name)
            return info

        @info.setter
        def info(self, value):
            self._info = value

        def update_info(self, new_info):
            self._info += "\n" + new_info

        def set_age(self, new_age):
            self.age = new_age
        
    class MainCharacter:
        def __init__(self, age, height, weight, info):
            self.age = age
            self.height = height
            self.weight = weight
            self._info = info

        @property
        def info(self):
            info = self._info
            for code, replacement in replacements.items():
                info = info.replace("[" + code + "]", replacement)
            info = info.replace("[mc_name]", mc_name)
            return info

        @info.setter
        def info(self, value):
            self._info = value

        def set_age(self, new_age):
            self.age = new_age


    amber = LoveInterest("Amber", 37, "1.77 m", "79.6 kg", "b 99 - w 66 - h 106", "She's a misunderstood rebel who craves acceptance. Rejected by her [mo_full_r_low] and at odds with her [si_full_r_low], she finds solace in her [br_full_r_low]. Beneath her tough exterior, she yearns for love while hiding her most controversial feelings. Her turbulent path is lit by her unwavering loyalty and unexpected sweetness.")
    nanami = LoveInterest("Nanami", 18, "1.48 m", "48.1 kg", "b 90 - w 57 - h 86", "She's a sweet but anxious introvert who puts others first despite her self-doubt. Her bestie Madison looks out for her, but her [mo_r_low] Kanae is emotionally MIA. Nanami wants to be a psychologist to help people while learning to open up to her loved ones.")
    elizabeth = LoveInterest("Elizabeth", 59, "1.73 m", "69.5 kg", "b 97 - w 64 - h 103", "She's a former English model who gave up her career for her [fm_r_low], leaving her with regrets. She's still stunning, but beneath the surface, she's dealing with the emotional scars from her husband's abuse and the fallout from putting his career first. Struggling with low self-esteem and a protective love for her [so_r_low], she confronts her unfulfilled dreams.")
    isabella = LoveInterest("Isabella", 18, "1.45 m", "40.1 kg", "b 74 - w 56 - h 80", "She's a tough girl who loves books and cosplay. She puts on a cheerful face, but inside she's dealing with heavy stuff after her [mo_r_low] abandoned her. She's smart and feels things deeply, especially when it comes to her [da_r]. They have a loving but complicated relationship, and she gets possessive of him. Despite the betrayal, she keeps going with a guarded heart.")
    kanae = LoveInterest("Kanae", 43, "1.61 m", "55.1 kg", "b 87 - w 57 - h 87", "She's a forensic scientist who's all about facts over feelings, which makes relationships tricky. Underneath her cold exterior, she craves deep connections with others, especially her [dau_r_low] Nanami. Even though she's emotionally distant, it's clear she wants love and understanding.")
    arlette = LoveInterest("Arlette", 24, "1.70 m", "67.1 kg", "b 95 - w 64 - h 98", "She's a former French model turned charming hostess, creating moments of fake connection to get by. But beneath the surface, she's a loving soul trapped by debt and yearning for real affection. She's balancing two worlds - the glamour of her job and the raw emotions of her private life. She dreams of finding true love, breaking free from her debts, and caring for her ill grandma.")
    antonella = LoveInterest("Antonella", 39, "1.60 m", "58.8 kg", "b 87 - w 60 - h 93", "She's a half-Japanese, half-Italian woman, is haunted by a past of abuse and loss. She walks a labyrinth of deceit and danger, but holds onto her love for [mc_name] and Isabella. As she navigates lies and threats, she's driven by her feelings for them, hoping to find solace and redemption.")
    madison = LoveInterest("Madison", 18, "1.68 m", "52.8 kg", "b 87 - w 61 - h 84", "She's a sexy, clever girl who'll do anything to escape her messed-up [fm_r_low] and make it as a model. She's known for her sharp tongue and manipulative ways, but she has a softer side when it comes to her bestie Nanami and her [niec_r_low] Isabella. She uses her charm to navigate the drama at home while chasing her dreams.")
    paz = LoveInterest("Paz", 37, "1.62 m", "70 kg", "b 94 - w 62 - h 103", "She is a mixed Japanese-Mexican cop caught between her strong sense of duty and her loyalty to her friend [mc_name]. Her [fm_r_low]'s struggles have shaped her integrity, but she faces tough ethical dilemmas on the job. She's wrestling with her own conflicts while trying to do what's right in a messed-up justice system.")
    mc = MainCharacter(39, "1.85 m", "85 kg", "Haunted by a nightmarish past, [mc_name] is a detective bearing the scars of both a bullet and lost love. His life revolves around the relentless pursuit of his ex-girlfriend Antonella and repairing the fractured relationship with his [dau_r_low] Isabella. Beneath his sarcastic armor beats a deeply affectionate heart, driving him to mend broken bonds while vigilantly unraveling the mysteries of his own history and the crimes he investigates.")


    def update_li_info(li_name, new_info):
        li = globals()[li_name]
        li.update_info(new_info)

#b *** - w *** - h ***