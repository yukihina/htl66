## py_core_infochar.rpy
## Character Information Management System for Ren'Py - Complete English Version
## 
## How to use:
## This script manages character information and relationships in the game.
## It provides a flexible system for defining character attributes and
## dynamically updating character descriptions based on game state.
## 
## To access character information:
## amber.name          # Returns character name
## amber.age           # Returns character age
## amber.info          # Returns dynamic description with relationship terms
## 
## The system automatically:
## - Applies relationship term replacements based on patched/unpatched state
## - Updates character descriptions with current game variables
## - Manages both love interest and main character information
## - Provides centralized character data for consistency across the game
##
## Character Management Features:
## - Dynamic relationship term replacement system
## - Centralized character information storage
## - Support for both love interests and main character
## - Automatic text replacement for family/relationship terms
## - Extensible character attribute system
## - Age and information update functions
##
## Relationship System:
## - Patched mode: Uses family relationship terms
## - Unpatched mode: Uses landlord/tenant and friend terms
## - Dynamic text replacement throughout character descriptions
## - Support for custom relationship terminology
## - Main character name integration

################################################################################
## INITIALIZATION
################################################################################

init python:
    ############################################################################
    ## RELATIONSHIP TERM CONFIGURATION
    ############################################################################
    
    # Dynamic relationship term replacements based on game patch state
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

    ############################################################################
    ## CHARACTER CLASS DEFINITIONS
    ############################################################################

    class LoveInterest:
        """
        Character class for love interest characters with full attribute support
        """
        def __init__(self, name, age, height, weight, measurements, info):
            self.name = name
            self.age = age
            self.height = height
            self.weight = weight
            self.measurements = measurements
            self._info = info

        @property
        def info(self):
            """
            Get character information with dynamic relationship term replacement
            
            Returns:
                str: Character description with current relationship terms applied
            """
            info = self._info
            
            # Apply relationship term replacements
            for code, replacement in replacements.items():
                info = info.replace("[" + code + "]", replacement)
            
            # Apply main character name replacement
            info = info.replace("[mc_name]", mc_name)
            
            return info

        @info.setter
        def info(self, value):
            """Set new character information"""
            self._info = value

        def update_info(self, new_info):
            """
            Add new information to existing character description
            
            Args:
                new_info (str): Additional information to append
            """
            self._info += "\n" + new_info

        def set_age(self, new_age):
            """
            Update character age
            
            Args:
                new_age (int): New age value
            """
            self.age = new_age
        
        def set_measurements(self, new_measurements):
            """
            Update character measurements
            
            Args:
                new_measurements (str): New measurements string
            """
            self.measurements = new_measurements
        
        def get_full_profile(self):
            """
            Get complete character profile as formatted string
            
            Returns:
                str: Full character profile with all attributes
            """
            profile = f"Name: {self.name}\n"
            profile += f"Age: {self.age}\n"
            profile += f"Height: {self.height}\n"
            profile += f"Weight: {self.weight}\n"
            profile += f"Measurements: {self.measurements}\n\n"
            profile += self.info
            return profile
        
    class MainCharacter:
        """
        Character class for the main character with essential attributes
        """
        def __init__(self, age, height, weight, info):
            self.age = age
            self.height = height
            self.weight = weight
            self._info = info

        @property
        def info(self):
            """
            Get main character information with dynamic term replacement
            
            Returns:
                str: Character description with current relationship terms applied
            """
            info = self._info
            
            # Apply relationship term replacements
            for code, replacement in replacements.items():
                info = info.replace("[" + code + "]", replacement)
            
            # Apply main character name replacement
            info = info.replace("[mc_name]", mc_name)
            
            return info

        @info.setter
        def info(self, value):
            """Set new main character information"""
            self._info = value

        def set_age(self, new_age):
            """
            Update main character age
            
            Args:
                new_age (int): New age value
            """
            self.age = new_age
        
        def update_info(self, new_info):
            """
            Add new information to existing character description
            
            Args:
                new_info (str): Additional information to append
            """
            self._info += "\n" + new_info
        
        def get_full_profile(self):
            """
            Get complete main character profile as formatted string
            
            Returns:
                str: Full character profile with all attributes
            """
            profile = f"Age: {self.age}\n"
            profile += f"Height: {self.height}\n"
            profile += f"Weight: {self.weight}\n\n"
            profile += self.info
            return profile

    ############################################################################
    ## CHARACTER INSTANCES
    ############################################################################

    # Love Interest Characters
    amber = LoveInterest(
        "Amber", 37, "1.77 m", "79.6 kg", "b 99 - w 66 - h 106",
        "A rebellious streaming girl who transformed herself from her mother's beauty expectations into something entirely her own. Tattooed and fierce, she uses provocative behavior as both shield and weapon while harboring deep fears of abandonment beneath her aggressive exterior."
    )
    
    nanami = LoveInterest(
        "Nanami", 18, "1.48 m", "48.1 kg", "b 90 - w 57 - h 86",
        "A gentle, anxious girl from Tokyo's margins who finds confidence only through her manipulative best friend Madison. Despite her kind heart and protective instincts, severe social anxiety and low self-esteem make her vulnerable to those who claim to care."
    )
    
    elizabeth = LoveInterest(
        "Elizabeth", 59, "1.73 m", "69.5 kg", "b 97 - w 64 - h 103",
        "Once Milan's rising star and Tokyo's \"European Rose,\" now a fading beauty drowning in pills and wine. The former supermodel clings to past glory while willfully ignoring her husband's dark secrets, projecting lost dreams onto her children."
    )
    
    isabella = LoveInterest(
        "Isabella", 18, "1.45 m", "40.1 kg", "b 74 - w 56 - h 80",
        "A young cosplayer whose cheerful anime enthusiasm masks sophisticated intelligence and strategic awareness. Abandoned by her mother, she maintains possessive devotion to her father while observing family dynamics with unsettling perceptiveness that belies her innocent facade."
    )
    
    kanae = LoveInterest(
        "Kanae", 43, "1.61 m", "55.1 kg", "b 87 - w 57 - h 87",
        "A forensic doctor who approaches life with clinical detachment, viewing relationships as functional exchanges rather than emotional connections. Her alien-like pragmatism and unwavering professionalism mask whatever maternal instincts she might possess toward her anxious daughter."
    )
    
    arlette = LoveInterest(
        "Arlette", 24, "1.70 m", "67.1 kg", "b 95 - w 64 - h 98",
        "A French expatriate whose Parisian elegance conceals a woman on the run. Former hostess with a compassionate heart and strong moral compass, she's fleeing dangerous yakuza connections while carrying the weight of past relationships and lost innocence."
    )
    
    antonella = LoveInterest(
        "Antonella", 39, "1.60 m", "58.8 kg", "b 87 - w 60 - h 93",
        "A enigmatic woman with piercing blue eyes and a complicated past that intersects with dangerous worlds. Beautiful yet haunted, she moves through life carrying secrets that could change everything, while struggling with losses that have fundamentally altered who she once was."
    )
    
    madison = LoveInterest(
        "Madison", 18, "1.68 m", "52.8 kg", "b 87 - w 61 - h 84",
        "A young aspiring model whose strategic mind rivals seasoned manipulators. Behind her cute facade lurks dangerous unpredictability, using her intelligence to control those around her while harboring secret feelings that complicate her calculated existence."
    )
    
    paz = LoveInterest(
        "Paz", 37, "1.62 m", "70 kg", "b 94 - w 62 - h 103",
        "A half-Japanese officer carrying her sister's unsolved murder like a wound that won't heal. Her pursuit of justice often requires moral flexibility, balancing professional duty with personal vengeance while navigating identity struggles in a system that sees her as perpetually foreign."
    )

    # Main Character
    mc = MainCharacter(
        39, "1.85 m", "85 kg",
        "A Tokyo detective caught between family dysfunction and professional duty. Haunted by complex relationships with former partners and struggling to protect his daughter, he navigates a world where personal connections and criminal investigations dangerously intertwine."
    )

    ############################################################################
    ## CHARACTER MANAGEMENT FUNCTIONS
    ############################################################################

    def update_li_info(li_name, new_info):
        """
        Update love interest character information
        
        Args:
            li_name (str): Name of the character variable (e.g., "amber", "nanami")
            new_info (str): New information to add to character description
        """
        li = globals()[li_name]
        li.update_info(new_info)

    def get_character_by_name(character_name):
        """
        Get character object by character name
        
        Args:
            character_name (str): Display name of the character
            
        Returns:
            LoveInterest or MainCharacter: Character object or None if not found
        """
        character_map = {
            "Amber": amber,
            "Nanami": nanami,
            "Elizabeth": elizabeth,
            "Isabella": isabella,
            "Kanae": kanae,
            "Arlette": arlette,
            "Antonella": antonella,
            "Madison": madison,
            "Paz": paz,
            mc_name: mc
        }
        return character_map.get(character_name)

    def get_all_love_interests():
        """
        Get list of all love interest characters
        
        Returns:
            list: List of all LoveInterest objects
        """
        return [amber, nanami, elizabeth, isabella, kanae, arlette, antonella, madison, paz]

    def get_character_ages():
        """
        Get dictionary of all character ages
        
        Returns:
            dict: Dictionary mapping character names to ages
        """
        ages = {}
        for li in get_all_love_interests():
            ages[li.name] = li.age
        ages[mc_name] = mc.age
        return ages

    def update_relationship_terms(new_replacements):
        """
        Update relationship term replacements
        
        Args:
            new_replacements (dict): New replacement dictionary
        """
        global replacements
        replacements.update(new_replacements)

    def get_character_summary(character_name):
        """
        Get a brief summary of a character
        
        Args:
            character_name (str): Display name of the character
            
        Returns:
            str: Brief character summary or error message
        """
        character = get_character_by_name(character_name)
        if character:
            if hasattr(character, 'measurements'):
                return f"{character.name}, {character.age} years old. {character.height}, {character.weight}."
            else:
                return f"{character_name}, {character.age} years old. {character.height}, {character.weight}."
        return f"Character '{character_name}' not found."

    def set_all_character_ages(age_dict):
        """
        Set ages for multiple characters at once
        
        Args:
            age_dict (dict): Dictionary mapping character names to new ages
        """
        for char_name, new_age in age_dict.items():
            character = get_character_by_name(char_name)
            if character:
                character.set_age(new_age)

    def validate_character_data():
        """
        Validate all character data for consistency
        
        Returns:
            list: List of validation errors (empty if all valid)
        """
        errors = []
        
        for li in get_all_love_interests():
            if not li.name:
                errors.append(f"Love interest missing name")
            if li.age < 0:
                errors.append(f"{li.name}: Invalid age ({li.age})")
            if not li.height or not li.weight:
                errors.append(f"{li.name}: Missing physical attributes")
        
        if mc.age < 0:
            errors.append(f"Main character: Invalid age ({mc.age})")
        
        return errors

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this character information system in your game:
## 
## 1. Accessing character information:
##    $ character_name = amber.name
##    $ character_age = amber.age
##    $ character_description = amber.info  # Includes dynamic replacements
##
## 2. The system will automatically:
##    - Apply relationship term replacements based on patched state
##    - Replace [mc_name] with the current main character name
##    - Provide consistent character information across the game
##    - Handle both love interests and main character data
##
## 3. Updating character information:
##    $ amber.update_info("She recently started learning to paint.")
##    $ amber.set_age(38)
##    $ update_li_info("nanami", "She's becoming more confident each day.")
##
## 4. Character queries and management:
##    $ character = get_character_by_name("Amber")
##    $ all_ages = get_character_ages()
##    $ summary = get_character_summary("Isabella")
##    $ errors = validate_character_data()
##
## 5. Relationship term management:
##    # The system automatically handles patched/unpatched terminology
##    # Characters use [mo_r_low], [da_r], [fm_r_low] etc. in descriptions
##    # These are replaced with appropriate terms based on game state
##
## 6. Character profile display:
##    $ full_profile = amber.get_full_profile()
##    # Returns formatted string with all character attributes
##
## Example character information usage:
## label character_profile_screen:
##     "Character: [amber.name]"
##     "Age: [amber.age]"
##     "Height: [amber.height]"
##     "Description: [amber.info]"
##
## label character_interaction:
##     amber "I've been thinking about my [mo_r_low] lately."
##     # This will display as "mom" or "landlady" based on patch state
##     
##     mc "Tell me more about your [fm_r_low]."
##     # This will display as "family" or "household" based on patch state
##
## Character data organization:
## - Each love interest has: name, age, height, weight, measurements, info
## - Main character has: age, height, weight, info
## - All characters support dynamic information updates
## - Relationship terms are automatically replaced in info text
##
## Relationship term placeholders:
## - [mo_full_r_low] = mother/landlady
## - [si_full_r_low] = sister/close friend
## - [br_full_r_low] = brother/close friend
## - [mo_r_low] = mom/landlady
## - [da_r_low] = dad/landlord
## - [dau_r_low] = daughter/young lady
## - [niec_r_low] = niece/younger friend
## - [fm_r_low] = family/household
## - [so_r_low] = son/young man
## - [da_r] = Dad/Landlord
## - [mc_name] = current main character name
##
## Best practices:
## - Use placeholder terms in character descriptions for automatic replacement
## - Update character information as the story progresses
## - Validate character data periodically to catch inconsistencies
## - Use the get_character_by_name() function for dynamic character access
## - Keep character descriptions concise but informative
##
## Performance considerations:
## - Character information is loaded once at game start
## - Dynamic replacements are computed each time info is accessed
## - Use update functions for permanent character changes
## - Character validation should be used sparingly in production
##
## Troubleshooting:
## - If replacements don't work: Check that placeholder terms are properly formatted [term]
## - If character not found: Verify character name spelling matches exactly
## - If info doesn't update: Ensure you're using update_info() or setting _info directly
## - If ages are wrong: Check that set_age() is being called with valid integers