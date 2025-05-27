# Documentation for the Ren'Py Core Relationship Management Script
# ----------------------------------------------------------------

# Purpose:
# This script forms the backbone of the game's relationship and attribute system. It manages how characters relate to each other and how their attributes change throughout the game.

# Main Components:
# 1. RM (Relationship Management) Class:
#    - Initializes and manages character data for all characters in the game.
#    - Provides methods to update and retrieve character attributes.
#    - Handles special cases like the main character's integrity and organization-specific trust.

# 2. Attribute Levels:
#    - Defines dictionaries for corruption_levels and trust_levels.
#    - These dictionaries map numerical ranges to level categories (0-5).

# 3. check_levels() Function:
#    - Monitors changes in corruption and trust levels for all characters.
#    - Triggers notification screens when levels change.

# 4. Notification Screens:
#    - corruption_notification: Displays when a character's corruption level changes.
#    - trust_notification: Displays when a character's trust level changes.

# Detailed Usage:
# 1. Initializing the RM system:
#    At the start of your game, create an instance of RM:
#    $ rm = RM()

# 2. Updating character attributes:
#    Use rm.update() to change character attributes. For example:
#    $ rm.update("amber", "cor", 10)  # Increases Amber's corruption by 10
#    $ rm.update("takeo", "trust", -5)  # Decreases Takeo's trust by 5
#    $ rm.update("mc", "integrity", 15)  # Increases MC's integrity by 15

# 3. Retrieving character data:
#    Use rm.get() to access character attributes. For example:
#    $ amber_corruption = rm.get("amber", "cor")
#    $ isabella_relationship = rm.get("isabella", "rel")

# 4. Updating relationships:
#    After changing trust levels, call rm.update_rel() to update relationship status:
#    $ rm.update_rel("nanami")

# 5. Setting character knowledge:
#    Use rm.set_knows() to indicate that the MC has met a character:
#    $ rm.set_knows("amber", True)

# 6. Checking levels:
#    Call check_levels() periodically (e.g., after significant events) to update and display notifications:
#    $ check_levels()

# 7. Using in conditional statements:
#    You can use rm.get() in your script for conditional branching:
#    if rm.get("amber", "cor") > 50:
#        "Amber's behavior has become noticeably more corrupt."
#    if rm.get("nanami", "rel"):
#        "Nanami and MC are in a relationship."

# Adding New Characters:
# To add a new character to the system:
# 1. Add the character's name to the self.chars list in the RM class __init__ method.
# 2. If the character needs special attributes, add appropriate logic in the __init__ method.

# Connections to Other Files:
# - This script is closely connected to def_chars.rpy, which defines the character objects.
# - The notification screens defined here are used in screens.rpy for display.
# - The RM instance created here is used throughout the game script for managing character relationships and attributes.

# Maintenance and Expansion:
# When updating or expanding this script:
# 1. Ensure any new attributes are properly initialized in the RM class.
# 2. Update the check_levels() function if new attributes need to be monitored.
# 3. Modify notification screens if you want to display additional information.
# 4. If adding new methods to RM, document them thoroughly and update this documentation.

# Note for Novices:
# This script uses Ren'Py's Python support. If you're new to Python:
# - The 'class' keyword defines a new type of object (RM in this case).
# - Methods like update() and get() are functions that belong to the RM class.
# - The 'self' parameter in these methods refers to the instance of RM you're working with.
# - Dictionaries (like self.rels) are used to store key-value pairs, allowing quick access to character data.

# Remember: This system is central to your game's mechanics. Always test thoroughly after making changes!

init -900 python:
    class RM:  # RM stands for Relationship Management - handles all character relationships and attributes
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
            # Updates a character's attribute by adding/subtracting a value
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
            # Retrieves a character's attribute value
            if char in self.rels:
                return self.rels[char][attr]
            return None  # Return None if character doesn't exist

        def update_rel(self, char):
            # Updates relationship status based on trust level
            # Only applies to regular characters (not mc, takeo, tmpd, osaka)
            if char in self.rels and char not in ["mc", "takeo", "tmpd", "osaka"]:
                trust = self.rels[char]["trust"]
                # Character becomes "in a relationship" if trust is 70 or higher
                self.rels[char]["rel"] = trust >= 70

        def set_knows(self, char, value):
            # Sets whether MC has met this character
            # Only applies to regular characters
            if char in self.rels and char not in ["mc", "takeo", "tmpd", "osaka"]:
                self.rels[char]["knows"] = value

    class SexStats:
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
            if char in self.stats and stat in self.stats[char]:
                return self.stats[char][stat]
            return 0  # Return 0 if the character or stat doesn't exist
        
        def add(self, char, stat):
            if char in self.stats and stat in self.stats[char]:
                self.stats[char][stat] += 1
        
        def set(self, char, stat, value):
            if char in self.stats and stat in self.stats[char]:
                self.stats[char][stat] = value



#  add+1
#$ ss.add("amber", "blowjob")
# $ ss.set("nanami", "virgin", False)
# $ ss.set("paz", "virgin", True)

# get value
#$ amber_bj = ss.get("amber", "blowjob")
# $ is_virgin = ss.get("nanami", "virgin")

# specific value
#$ ss.set("amber", "sex", 5)

# Define dictionaries that map level numbers (0-5) to value ranges (0-100)
# Used to determine corruption and trust levels for characters
init python:
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
    
    # Helper function that takes a numeric value and a level dictionary
    # Returns which level (0-5) the value falls into
    def get_level_for_value(value, level_dict):
        for level, (min_val, max_val) in level_dict.items():
            if min_val <= value <= max_val:
                return level
        return 0  # Default to level 0 if value doesn't fit in any range
    
    # Main function to check and notify level changes
    # Parameters:
    # - char: character ID (e.g. "amber")
    # - attr: attribute to check ("cor" for corruption or "trust")
    # - val: how much the attribute changed
    def check_levels(char, attr, val):
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


init -890 python:
    class WM:  # WM stands for Wardrobe Manager - handles character outfits/clothing
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
            """Unlocks a specific outfit for a character"""
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
            """Checks if a specific outfit is unlocked for a character"""
            if char in self.wardrobes:
                # Convert outfit_id to integer if it was passed as string
                if isinstance(outfit_id, str) and outfit_id.isdigit():
                    outfit_id = int(outfit_id)
                
                return outfit_id in self.wardrobes[char]["unlocked"]
            return False
        
        def set(self, char, outfit_id):
            """Sets the current outfit for a character (if it's unlocked)"""
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
            """Gets the currently selected outfit for a character"""
            if char in self.wardrobes:
                return self.wardrobes[char]["current"]
            return 0  # Default to outfit 0 if character doesn't exist
        
        def get_all_unlocked(self, char):
            """Gets all unlocked outfits for a character as a sorted list"""
            if char in self.wardrobes:
                return sorted(list(self.wardrobes[char]["unlocked"]))
            return [0]  # Return only the default outfit if character doesn't exist
            
        def next_outfit(self, char):
            """Changes to the next unlocked outfit for a character"""
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
            """Changes to the previous unlocked outfit for a character"""
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

    # Create a global instance of the Wardrobe Manager
    wm = WM()

    # Helper function for screen to get the appropriate image path
    def get_character_outfit_pic(char_name, knows=True):
        """
        Returns the appropriate image path for a character's current outfit
        
        Parameters:
        - char_name: The character's ID (e.g., 'nanami')
        - knows: Whether the MC knows this character
        
        Returns:
        - String path to the appropriate image file
        """
        if not knows:
            return "gui/char_pic_null.webp"
        
        current_outfit = wm.get_current(char_name)
        return f"gui/{char_name}_outfit_{current_outfit}.png"