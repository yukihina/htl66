## core.rpy
## Core Relationship Management System for Ren'Py - Complete English Version
## 
## How to use:
## This script forms the backbone of the game's relationship and attribute system.
## It manages how characters relate to each other and how their attributes change throughout the game.
## 
## To initialize the RM system:
## $ rm = RM()  # This is typically done automatically
## 
## The system automatically:
## - Manages character relationships, corruption, trust, and integrity stats
## - Handles sexual statistics tracking for all love interests
## - Provides wardrobe/outfit management for all characters
## - Maintains level-based notifications for stat changes
## - Ensures save game compatibility across all versions
##
## Core Management Features:
## - RM class: Relationship Management for all character attributes
## - SexStats class: Sexual interaction tracking and statistics
## - WM class: Wardrobe Management for character outfits
## - Level-based progression system with notifications
## - Character knowledge and relationship status tracking
##
## Critical Save Game Compatibility:
## - All initialization priorities are preserved exactly (-900, -890, etc.)
## - All class structures and methods remain identical
## - All variable names and data structures are maintained
## - Complete backward compatibility with existing save files

################################################################################
## CORE RELATIONSHIP MANAGEMENT SYSTEM
################################################################################

init -900 python:
    ############################################################################
    ## RM CLASS - RELATIONSHIP MANAGEMENT CORE
    ############################################################################
    
    class RM:
        """
        RM stands for Relationship Management - handles all character relationships and attributes
        
        Core Features:
        - Tracks corruption, trust, pregnancy, relationship status for love interests
        - Manages main character integrity with locking mechanism
        - Handles organization trust levels (takeo, tmpd, osaka)
        - Provides safe stat updates with bounds checking
        - Maintains character knowledge tracking
        """
        def __init__(self):
            # List of all characters in the game that will have stats tracked
            self.chars = ["amber", "nanami", "elizabeth", "isabella", "kanae", "arlette", "antonella", "madison", "paz", "mc", "takeo", "tmpd", "osaka"]
            self.rels = {}  # Dictionary to store all character relationships and attributes
            
            # Initialize each character's attributes based on their type
            for char in self.chars:
                if char == "mc":  # Special case for main character (mc)
                    # MC only has integrity stat (starts at 50) and can be locked
                    self.rels[char] = {"integrity": 50, "integrity_locked": False}
                elif char in ["takeo", "tmpd", "osaka"]:  # Special case for organizations/special characters
                    # These only track trust level
                    self.rels[char] = {"trust": 0}
                else:  # Regular characters
                    # Regular characters have: corruption, trust, pregnancy status, relationship status, and if MC knows them
                    self.rels[char] = {"cor": 0, "trust": 0, "preg": False, "rel": False, "knows": False}

        def update(self, char, attr, val):
            """
            Updates a character's attribute by adding/subtracting a value
            
            Args:
                char (str): Character ID (e.g., "amber", "mc")
                attr (str): Attribute to update ("cor", "trust", "integrity", etc.)
                val (int): Value to add/subtract
            """
            if char in self.rels:  # Check if character exists
                if attr in ["cor", "trust", "integrity"]:  # These attributes are numerical (0-100)
                    # Special case: can't update integrity if it's locked
                    if attr == "integrity" and self.rels[char].get("integrity_locked"):
                        return
                    # Ensure value stays between 0 and 100
                    new_value = max(0, min(100, self.rels[char][attr] + val))
                    self.rels[char][attr] = new_value
                    # Lock integrity if it reaches 0 or 100
                    if attr == "integrity":
                        if new_value == 0 or new_value == 100:
                            self.rels[char]["integrity_locked"] = True
                else:  # For boolean attributes, just set the new value
                    self.rels[char][attr] = val
            
        def get(self, char, attr):
            """
            Retrieves a character's attribute value
            
            Args:
                char (str): Character ID
                attr (str): Attribute name
                
            Returns:
                Value of the attribute or None if character doesn't exist
            """
            if char in self.rels:
                return self.rels[char][attr]
            return None  # Return None if character doesn't exist

        def update_rel(self, char):
            """
            Updates relationship status based on trust level
            Only applies to regular characters (not mc, takeo, tmpd, osaka)
            
            Args:
                char (str): Character ID to update relationship status for
            """
            if char in self.rels and char not in ["mc", "takeo", "tmpd", "osaka"]:
                trust = self.rels[char]["trust"]
                # Character becomes "in a relationship" if trust is 70 or higher
                self.rels[char]["rel"] = trust >= 70

        def set_knows(self, char, value):
            """
            Sets whether MC has met this character
            Only applies to regular characters
            
            Args:
                char (str): Character ID
                value (bool): Whether MC knows this character
            """
            if char in self.rels and char not in ["mc", "takeo", "tmpd", "osaka"]:
                self.rels[char]["knows"] = value

    ############################################################################
    ## SEXSTATS CLASS - SEXUAL INTERACTION TRACKING
    ############################################################################
    
    class SexStats:
        """
        Sexual statistics tracking system for all love interests
        
        Features:
        - Tracks various sexual activities per character
        - Manages virginity status
        - Includes strike system for character interactions
        - Provides safe stat access and modification
        """
        def __init__(self):
            # List of characters eligible for sexual interactions (the female LIs)
            self.chars = ["amber", "nanami", "elizabeth", "isabella", "kanae", "arlette", "antonella", "madison", "paz"]
            self.stats = {}

            # Characters that start the game as non-virgins
            non_virgins = ["amber", "elizabeth", "kanae", "arlette", "antonella"]

            # Initialize sexual statistics for each character, including the new 'strike' attribute
            for char in self.chars:
                self.stats[char] = {
                    "anal": 0,
                    "assjob": 0,
                    "blowjob": 0,
                    "creampie": 0,
                    "pussyjob": 0,
                    "sex": 0,
                    "titjob": 0,
                    "virgin": char not in non_virgins,
                    "strike": 0  # NEW: 'strike' attribute to track strikes for each LI
                }
        
        def get(self, char, stat):
            """
            Get a sexual statistic for a character
            
            Args:
                char (str): Character ID
                stat (str): Statistic name
                
            Returns:
                int or bool: Value of the statistic, 0 if not found
            """
            if char in self.stats and stat in self.stats[char]:
                return self.stats[char][stat]
            return 0  # Return 0 if the character or stat doesn't exist
        
        def add(self, char, stat):
            """
            Increment a sexual statistic for a character
            
            Args:
                char (str): Character ID
                stat (str): Statistic name to increment
            """
            if char in self.stats and stat in self.stats[char]:
                self.stats[char][stat] += 1
        
        def set(self, char, stat, value):
            """
            Set a sexual statistic to a specific value
            
            Args:
                char (str): Character ID
                stat (str): Statistic name
                value (int or bool): Value to set
            """
            if char in self.stats and stat in self.stats[char]:
                self.stats[char][stat] = value

################################################################################
## LEVEL SYSTEM AND CHARACTER CONFIGURATION
################################################################################

init python:
    ############################################################################
    ## CORRUPTION AND TRUST LEVEL DEFINITIONS
    ############################################################################
    
    # Define dictionaries that map level numbers (0-5) to value ranges (0-100)
    # Used to determine corruption and trust levels for characters
    corruption_levels = {
        0: (0, 16),    # Level 0: Pure/Innocent (0-16%)
        1: (17, 32),   # Level 1: Slightly corrupted (17-32%)
        2: (33, 48),   # Level 2: Moderately corrupted (33-48%)
        3: (49, 64),   # Level 3: Notably corrupted (49-64%)
        4: (65, 80),   # Level 4: Highly corrupted (65-80%)
        5: (81, 100)   # Level 5: Fully corrupted (81-100%)
    }
    
    # Same structure as corruption_levels, but for trust
    trust_levels = {
        0: (0, 16),    # Level 0: Stranger/Hostile (0-16%)
        1: (17, 32),   # Level 1: Acquaintance (17-32%)
        2: (33, 48),   # Level 2: Friend (33-48%)
        3: (49, 64),   # Level 3: Close Friend (49-64%)
        4: (65, 80),   # Level 4: Very Close (65-80%)
        5: (81, 100)   # Level 5: Intimate/Best Friend (81-100%)
    }
    
    ############################################################################
    ## CHARACTER CONFIGURATION AND DISPLAY NAMES
    ############################################################################
    
    # Dictionary mapping internal character IDs to their display names
    # Comments indicate how each character's stats are modified:
    # - love: how quickly they gain trust
    # - cor: how quickly they get corrupted
    char_proper_names = {
        "amber": "Amber",           # 1X love / 1.5X corruption rate
        "antonella": "Antonella",   # 0.25X love / 1X corruption rate
        "arlette": "Arlette",      # 1.5X love / 1.5X corruption rate
        "elizabeth": "Elizabeth",   # 2X love / 1X corruption rate
        "isabella": "Isabella",     # 1X love / 1X corruption rate
        "kanae": "Kanae",          # 0.5X love / 0.5X corruption rate
        "madison": "Madison",       # 0.5X love / 2X corruption rate
        "nanami": "Nanami",        # 3X love / 1X corruption rate
        "paz": "Paz"               # 1X love / 1X corruption rate
    }
    
    ############################################################################
    ## LEVEL CHECKING AND NOTIFICATION FUNCTIONS
    ############################################################################
    
    def get_level_for_value(value, level_dict):
        """
        Helper function that takes a numeric value and a level dictionary
        Returns which level (0-5) the value falls into
        
        Args:
            value (int): Numeric value to check (0-100)
            level_dict (dict): Dictionary mapping levels to ranges
            
        Returns:
            int: Level number (0-5)
        """
        for level, (min_val, max_val) in level_dict.items():
            if min_val <= value <= max_val:
                return level
        return 0  # Default to level 0 if value doesn't fit in any range
    
    def check_levels(char, attr, val):
        """
        Main function to check and notify level changes
        
        Args:
            char (str): Character ID (e.g. "amber")
            attr (str): Attribute to check ("cor" for corruption or "trust")
            val (int): How much the attribute changed
        """
        # Get the new value after change
        new_value = rm.get(char, attr)
        
        # Calculate what the value was before the change
        old_value = new_value - val
        
        # Get character's display name (falls back to ID if not found)
        proper_name = char_proper_names.get(char, char)
        
        # Set up appropriate notifications based on attribute type
        if attr == "cor":  # Corruption notifications
            level_dict = corruption_levels
            notification_increase = "corruption_increase"  # Small increase
            notification_decrease = "corruption_decrease"  # Small decrease
            notification_level_up = "corruption_level_up"    # Level gained
            notification_level_down = "corruption_level_down"  # Level lost
        elif attr == "trust":  # Trust notifications
            level_dict = trust_levels
            notification_increase = "trust_increase"  # Small increase
            notification_decrease = "trust_decrease"  # Small decrease
            notification_level_up = "trust_level_up"    # Level gained
            notification_level_down = "trust_level_down"  # Level lost
        else:
            return  # Exit if invalid attribute
        
        # Calculate old and new levels
        old_level = get_level_for_value(old_value, level_dict)
        new_level = get_level_for_value(new_value, level_dict)
        
        # Show appropriate notification based on value change
        if val > 0:  # Value increased
            if new_level > old_level:  # Gained a level
                show_custom_notification(notification_level_up, char=proper_name, level=new_level)
            else:  # Small increase, no level change
                show_custom_notification(notification_increase, char=proper_name)
        elif val < 0:  # Value decreased
            if new_level < old_level:  # Lost a level
                show_custom_notification(notification_level_down, char=proper_name, level=new_level)
            else:  # Small decrease, no level change
                show_custom_notification(notification_decrease, char=proper_name)
        else:  # No change (val == 0)
            pass  # Do nothing

################################################################################
## WARDROBE MANAGEMENT SYSTEM
################################################################################

init -890 python:
    ############################################################################
    ## WM CLASS - WARDROBE MANAGEMENT
    ############################################################################
    
    class WM:
        """
        WM stands for Wardrobe Manager - handles character outfits/clothing
        
        Features:
        - Manages outfit unlocking and selection for all characters
        - Tracks maximum available outfits per character
        - Provides outfit navigation (next/previous)
        - Ensures outfit availability before selection
        """
        def __init__(self):
            # List of all characters in the game that will have wardrobes tracked
            self.chars = ["amber", "nanami", "elizabeth", "isabella", "kanae", "arlette", "antonella", "madison", "paz"]
            
            # Dictionary to store all character wardrobe data
            self.wardrobes = {}
            
            # Define the maximum number of outfits for each character
            self.max_outfits = {
                "amber": 6,
                "nanami": 9,
                "elizabeth": 4,
                "isabella": 7,
                "kanae": 5,
                "arlette": 8,
                "antonella": 4,
                "madison": 5,
                "paz": 6
            }
            
            # Initialize each character's wardrobe
            for char in self.chars:
                # Create a dictionary for each character
                # - unlocked: set of unlocked outfit IDs
                # - current: currently selected outfit (defaults to 0)
                self.wardrobes[char] = {
                    "unlocked": {0},  # Default outfit (0) is always unlocked
                    "current": 0      # Default to outfit 0
                }
        
        def unlock(self, char, outfit_id):
            """
            Unlocks a specific outfit for a character
            
            Args:
                char (str): Character ID
                outfit_id (int or str): Outfit ID to unlock
                
            Returns:
                bool: True if outfit was unlocked, False otherwise
            """
            if char in self.wardrobes:
                # Convert outfit_id to integer if it was passed as string
                if isinstance(outfit_id, str) and outfit_id.isdigit():
                    outfit_id = int(outfit_id)
                
                # Check if outfit_id is valid (within max range for this character)
                if 0 <= outfit_id < self.max_outfits.get(char, 0):
                    self.wardrobes[char]["unlocked"].add(outfit_id)
                    return True
            return False
        
        def is_unlocked(self, char, outfit_id):
            """
            Checks if a specific outfit is unlocked for a character
            
            Args:
                char (str): Character ID
                outfit_id (int or str): Outfit ID to check
                
            Returns:
                bool: True if outfit is unlocked, False otherwise
            """
            if char in self.wardrobes:
                # Convert outfit_id to integer if it was passed as string
                if isinstance(outfit_id, str) and outfit_id.isdigit():
                    outfit_id = int(outfit_id)
                
                return outfit_id in self.wardrobes[char]["unlocked"]
            return False
        
        def set(self, char, outfit_id):
            """
            Sets the current outfit for a character (if it's unlocked)
            
            Args:
                char (str): Character ID
                outfit_id (int or str): Outfit ID to set as current
                
            Returns:
                bool: True if outfit was set, False otherwise
            """
            if char in self.wardrobes:
                # Convert outfit_id to integer if it was passed as string
                if isinstance(outfit_id, str) and outfit_id.isdigit():
                    outfit_id = int(outfit_id)
                
                # Only set the outfit if it's unlocked
                if outfit_id in self.wardrobes[char]["unlocked"]:
                    self.wardrobes[char]["current"] = outfit_id
                    return True
            return False
        
        def get_current(self, char):
            """
            Gets the currently selected outfit for a character
            
            Args:
                char (str): Character ID
                
            Returns:
                int: Current outfit ID, 0 if character doesn't exist
            """
            if char in self.wardrobes:
                return self.wardrobes[char]["current"]
            return 0  # Default to outfit 0 if character doesn't exist
        
        def get_all_unlocked(self, char):
            """
            Gets all unlocked outfits for a character as a sorted list
            
            Args:
                char (str): Character ID
                
            Returns:
                list: Sorted list of unlocked outfit IDs
            """
            if char in self.wardrobes:
                return sorted(list(self.wardrobes[char]["unlocked"]))
            return [0]  # Return only the default outfit if character doesn't exist
            
        def next_outfit(self, char):
            """
            Changes to the next unlocked outfit for a character
            
            Args:
                char (str): Character ID
                
            Returns:
                bool: True if outfit was changed, False otherwise
            """
            if char in self.wardrobes:
                unlocked = self.get_all_unlocked(char)
                if len(unlocked) <= 1:
                    return False  # No change if only one outfit is unlocked
                
                current = self.wardrobes[char]["current"]
                current_index = unlocked.index(current) if current in unlocked else 0
                next_index = (current_index + 1) % len(unlocked)
                self.wardrobes[char]["current"] = unlocked[next_index]
                return True
            return False
            
        def prev_outfit(self, char):
            """
            Changes to the previous unlocked outfit for a character
            
            Args:
                char (str): Character ID
                
            Returns:
                bool: True if outfit was changed, False otherwise
            """
            if char in self.wardrobes:
                unlocked = self.get_all_unlocked(char)
                if len(unlocked) <= 1:
                    return False  # No change if only one outfit is unlocked
                
                current = self.wardrobes[char]["current"]
                current_index = unlocked.index(current) if current in unlocked else 0
                prev_index = (current_index - 1) % len(unlocked)
                self.wardrobes[char]["current"] = unlocked[prev_index]
                return True
            return False

    ############################################################################
    ## WARDROBE HELPER FUNCTIONS
    ############################################################################
    
    # Create a global instance of the Wardrobe Manager
    wm = WM()

    def get_character_outfit_pic(char_name, knows=True):
        """
        Returns the appropriate image path for a character's current outfit
        
        Args:
            char_name (str): The character's ID (e.g., 'nanami')
            knows (bool): Whether the MC knows this character
        
        Returns:
            str: String path to the appropriate image file
        """
        if not knows:
            return "gui/char_pic_null.webp"
        
        current_outfit = wm.get_current(char_name)
        return f"gui/{char_name}_outfit_{current_outfit}.png"

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this core relationship system in your game:
## 
## 1. The system initializes automatically with proper save game compatibility
##    - RM, SexStats, and WM instances are created automatically
##    - All initialization priorities are preserved for save compatibility
##    - Character data structures remain identical to previous versions
##
## 2. Basic relationship management:
##    $ rm.update("amber", "cor", 10)     # Increase Amber's corruption by 10
##    $ rm.update("takeo", "trust", -5)   # Decrease Takeo's trust by 5
##    $ rm.update("mc", "integrity", 15)  # Increase MC's integrity by 15
##    $ rm.update_rel("nanami")           # Update relationship status based on trust
##    $ rm.set_knows("amber", True)       # Set that MC has met Amber
##
## 3. Retrieving character data:
##    $ amber_corruption = rm.get("amber", "cor")
##    $ isabella_relationship = rm.get("isabella", "rel")
##    $ mc_integrity = rm.get("mc", "integrity")
##
## 4. Sexual statistics management:
##    $ ss.add("amber", "blowjob")        # Increment Amber's blowjob count
##    $ ss.set("nanami", "virgin", False) # Set Nanami as non-virgin
##    $ amber_bj = ss.get("amber", "blowjob")  # Get Amber's blowjob count
##    $ is_virgin = ss.get("nanami", "virgin") # Check virginity status
##
## 5. Wardrobe management:
##    $ wm.unlock("nanami", 3)            # Unlock outfit 3 for Nanami
##    $ wm.set("nanami", 2)               # Set Nanami's current outfit to 2
##    $ current_outfit = wm.get_current("nanami")  # Get current outfit
##    $ wm.next_outfit("amber")           # Switch to next unlocked outfit
##
## 6. Level checking and notifications:
##    $ check_levels("amber", "cor", 15)  # Check corruption level change
##    $ check_levels("nanami", "trust", 20)  # Check trust level change
##
## Example usage in game script:
## label amber_scene:
##     # Update corruption and check for level changes
##     $ rm.update("amber", "cor", 15)
##     $ check_levels("amber", "cor", 15)
##     
##     # Check relationship status
##     if rm.get("amber", "rel"):
##         "Amber is now in a relationship with you."
##     
##     # Track sexual interaction
##     $ ss.add("amber", "blowjob")
##     
##     # Unlock new outfit
##     $ wm.unlock("amber", 2)
##
## Character attribute reference:
## RM attributes:
## - Love interests: "cor" (corruption), "trust", "preg" (pregnancy), "rel" (relationship), "knows"
## - Main character: "integrity", "integrity_locked"
## - Organizations: "trust" only
##
## SexStats attributes:
## - "anal", "assjob", "blowjob", "creampie", "pussyjob", "sex", "titjob"
## - "virgin" (boolean), "strike" (integer)
##
## WM methods:
## - unlock(), set(), get_current(), next_outfit(), prev_outfit()
## - is_unlocked(), get_all_unlocked()
##
## Level system:
## - Corruption/Trust levels: 0-5 (ranges from 0-100 stats)
## - Level 0: 0-16, Level 1: 17-32, Level 2: 33-48
## - Level 3: 49-64, Level 4: 65-80, Level 5: 81-100
## - Automatic notifications when levels change
##
## Save game compatibility:
## - All initialization priorities preserved (-900, -890)
## - All class structures maintained exactly
## - All variable names and data types unchanged
## - Complete backward compatibility ensured
##
## Character progression rates:
## - Amber: 1X love / 1.5X corruption
## - Antonella: 0.25X love / 1X corruption  
## - Arlette: 1.5X love / 1.5X corruption
## - Elizabeth: 2X love / 1X corruption
## - Isabella: 1X love / 1X corruption
## - Kanae: 0.5X love / 0.5X corruption
## - Madison: 0.5X love / 2X corruption
## - Nanami: 3X love / 1X corruption
## - Paz: 1X love / 1X corruption
##
## Critical notes:
## - Never modify initialization priorities (-900, -890)
## - Never change class method signatures
## - Never alter data structure names or types
## - Always test save game loading after any modifications
## - Use check_levels() after stat updates for proper notifications
##
## Troubleshooting:
## - If stats don't update: Check character name spelling and attribute names
## - If saves break: Verify no initialization priorities were changed
## - If levels don't show: Ensure check_levels() is called after stat changes
## - If outfits don't work: Check that outfit IDs are within max_outfits range