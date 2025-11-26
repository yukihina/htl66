################################################################################
## CORE RELATIONSHIP MANAGEMENT SYSTEM
################################################################################

init -900 python:
    ############################################################################
    ## CHARACTER PROGRESSION RATES
    ############################################################################
    # These multipliers are applied automatically to all stat changes
    # Different characters respond differently to player actions

    char_progression_rates = {
        "amber": {"trust": 1.0, "cor": 1.5},        # More easily corrupted
        "antonella": {"trust": 0.25, "cor": 1.0},   # Very hard to gain trust
        "arlette": {"trust": 1.5, "cor": 1.5},      # Responds strongly to both
        "elizabeth": {"trust": 2.0, "cor": 1.0},    # Gains trust quickly
        "isabella": {"trust": 1.0, "cor": 1.0},     # Balanced progression
        "kanae": {"trust": 0.5, "cor": 0.5},        # Slow progression both ways
        "madison": {"trust": 0.5, "cor": 2.0},      # Hard to trust, easily corrupted
        "nanami": {"trust": 3.0, "cor": 1.0},       # Very trusting, hard to corrupt
        "paz": {"trust": 1.0, "cor": 1.0}           # Balanced progression
    }

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
                    # Regular characters have: corruption, trust, pregnancy status, relationship status, if MC knows them, and emotional lock
                    self.rels[char] = {"cor": 0, "trust": 0, "preg": False, "rel": False, "knows": False, "emotionally_locked": False}

        def update(self, char, attr, val):
            """
            Updates a character's attribute by adding/subtracting a value
            Now includes:
            - Emotional lock check for characters with 3 strikes
            - Automatic progression rate multipliers

            Args:
                char (str): Character ID (e.g., "amber", "mc")
                attr (str): Attribute to update ("cor", "trust", "integrity", etc.)
                val (int or float): Base value to add/subtract (will be multiplied by character rate)
            """
            if char in self.rels:  # Check if character exists
                # EMOTIONAL LOCK SYSTEM: Check if character has 3 strikes (only for regular characters)
                if char not in ["mc", "takeo", "tmpd", "osaka"]:
                    strikes = ss.get(char, "strike")

                    # If character has 3 strikes, block any trust/corruption changes
                    if strikes >= 3 and attr in ["cor", "trust"]:
                        # Ensure emotionally_locked field exists (for old save compatibility)
                        if "emotionally_locked" not in self.rels[char]:
                            self.rels[char]["emotionally_locked"] = False

                        # Set emotional lock and return without updating stats
                        self.rels[char]["emotionally_locked"] = True
                        return  # Block the update - stats frozen at 0

                # AUTOMATIC PROGRESSION RATES: Apply character-specific multipliers
                if char in char_progression_rates and attr in ["cor", "trust"]:
                    # Get the rate for this character and attribute
                    rate = char_progression_rates[char].get(attr, 1.0)
                    # Multiply the base value by the rate and round to integer
                    val = round(val * rate)

                if attr in ["cor", "trust", "integrity"]:  # These attributes are numerical (0-100)
                    # Special case: can't update integrity if it's locked
                    if attr == "integrity" and self.rels[char].get("integrity_locked"):
                        return
                    # Ensure value stays between 0 and 100
                    new_value = max(0, min(100, self.rels[char][attr] + val))
                    self.rels[char][attr] = new_value
                    # MC Integrity auto-lock system
                    if attr == "integrity" and char == "mc":
                        # Lock if reaches 0 or 100 (pure paths)
                        if new_value == 0 or new_value == 100:
                            self.rels[char]["integrity_locked"] = True
                            lock_mc_alignment()
                        # Auto-lock at ep15+ if not already locked
                        elif hasattr(persistent, 'current_episode') and persistent.current_episode >= 15:
                            if not self.rels[char].get("integrity_locked"):
                                lock_mc_alignment()
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

        def migrate_old_saves(self):
            """
            Migrates old save files to include the new emotionally_locked field
            Automatically applies emotional lock to characters with 3 strikes
            Called automatically from after_load label
            """
            for char in self.chars:
                if char not in ["mc", "takeo", "tmpd", "osaka"]:
                    # If the emotionally_locked field doesn't exist, add it
                    if "emotionally_locked" not in self.rels[char]:
                        self.rels[char]["emotionally_locked"] = False

                        # Check if character already has 3 strikes in old save
                        strikes = ss.get(char, "strike")
                        if strikes >= 3:
                            # Apply emotional lock retroactively
                            self.rels[char]["cor"] = 0
                            self.rels[char]["trust"] = 0
                            self.rels[char]["emotionally_locked"] = True

        def migrate_to_ratio_system(self):
            """
            Migrates saves from pre-ratio system to new automatic ratio system
            Divides existing stat values by character rates to convert to base values
            Called automatically when loading old saves (save_system_version == 1)
            """
            for char in char_progression_rates:
                if char in self.rels:
                    # Divide existing values by their rates to get base values
                    trust_rate = char_progression_rates[char].get("trust", 1.0)
                    cor_rate = char_progression_rates[char].get("cor", 1.0)

                    old_trust = self.rels[char]["trust"]
                    old_cor = self.rels[char]["cor"]

                    # Convert to base values (rounded)
                    new_trust = round(old_trust / trust_rate) if trust_rate != 0 else old_trust
                    new_cor = round(old_cor / cor_rate) if cor_rate != 0 else old_cor

                    # Ensure values stay within bounds
                    self.rels[char]["trust"] = max(0, min(100, new_trust))
                    self.rels[char]["cor"] = max(0, min(100, new_cor))

        def check_emotional_lock(self, char):
            """
            Checks if a character has reached 3 strikes and applies emotional lock
            Resets corruption and trust to 0 when lock is applied

            Args:
                char (str): Character ID to check

            Returns:
                bool: True if lock was just applied (first time), False otherwise
            """
            if char in self.rels and char not in ["mc", "takeo", "tmpd", "osaka"]:
                strikes = ss.get(char, "strike")

                # Ensure emotionally_locked field exists (for old save compatibility)
                if "emotionally_locked" not in self.rels[char]:
                    self.rels[char]["emotionally_locked"] = False

                # If character has 3 strikes and is not already locked, apply lock
                if strikes >= 3 and not self.rels[char]["emotionally_locked"]:
                    self.rels[char]["cor"] = 0
                    self.rels[char]["trust"] = 0
                    self.rels[char]["emotionally_locked"] = True
                    return True  # Lock was just applied

            return False  # No lock applied

        def is_emotionally_locked(self, char):
            """
            Checks if a character is emotionally locked (has 3 strikes)

            Args:
                char (str): Character ID to check

            Returns:
                bool: True if character is emotionally locked, False otherwise
            """
            if char in self.rels and char not in ["mc", "takeo", "tmpd", "osaka"]:
                # Use .get() for compatibility with old saves
                return self.rels[char].get("emotionally_locked", False)
            return False

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
                    "footjob": 0,
                    "oral": 0,
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

    # MC Integrity levels - determines moral alignment
    integrity_levels = {
        0: (0, 30),    # Rogue: Antihero, ends justify means
        1: (31, 69),   # Neutral: Pragmatic, case by case
        2: (70, 100)   # Paragon: Hero, always does what's right
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

    ############################################################################
    ## MILESTONE DECISION SYSTEM - PATH LOCKING (Episode 6+)
    ############################################################################

    def lock_character_path(char, love_threshold=3, cor_threshold=3):
        """
        Checks milestone decision counters and locks a character's narrative path

        This is the core function for the Milestone Decision Model. It should be
        called at key story moments (typically end of Episode 6 or similar) to
        determine and permanently lock a character's relationship path.

        Args:
            char (str): Character ID (e.g., "amber", "nanami")
            love_threshold (int): Number of love choices needed to lock love path (default: 3)
            cor_threshold (int): Number of corruption choices needed to lock corruption path (default: 3)

        Returns:
            str: The locked path ("love", "corruption", or "neutral")

        Example usage:
            $ locked_path = lock_character_path("amber")
            # or with custom thresholds
            $ locked_path = lock_character_path("nanami", love_threshold=4, cor_threshold=4)
        """
        # Get the persistent path variable for this character
        path_var_name = f"{char}_path"

        # Check if path is already locked
        current_path = getattr(persistent, path_var_name, None)
        if current_path is not None:
            return current_path  # Already locked, return existing path

        # Get the milestone choice counters for this character
        love_choices = renpy.python.py_eval(f"{char}_love_choices")
        cor_choices = renpy.python.py_eval(f"{char}_cor_choices")

        # Determine which path to lock based on thresholds
        locked_path = "neutral"  # Default to neutral

        if love_choices >= love_threshold and cor_choices >= cor_threshold:
            # Both thresholds met - choose based on which has more choices
            if love_choices > cor_choices:
                locked_path = "love"
            elif cor_choices > love_choices:
                locked_path = "corruption"
            else:
                # Tie - use trust vs corruption stats as tiebreaker
                trust_val = rm.get(char, "trust")
                cor_val = rm.get(char, "cor")
                locked_path = "love" if trust_val >= cor_val else "corruption"
        elif love_choices >= love_threshold:
            locked_path = "love"
        elif cor_choices >= cor_threshold:
            locked_path = "corruption"
        # else: remains "neutral"

        # Lock the path by setting the persistent variable
        setattr(persistent, path_var_name, locked_path)

        return locked_path

    def get_character_path(char):
        """
        Gets the current locked path for a character

        Args:
            char (str): Character ID

        Returns:
            str or None: The locked path ("love", "corruption", "neutral") or None if unlocked
        """
        path_var_name = f"{char}_path"
        return getattr(persistent, path_var_name, None)

    def is_path_locked(char):
        """
        Checks if a character's path has been locked

        Args:
            char (str): Character ID

        Returns:
            bool: True if path is locked, False if still unlocked
        """
        return get_character_path(char) is not None

    def get_milestone_choices(char, choice_type):
        """
        Gets the current count of milestone choices for a character

        Args:
            char (str): Character ID
            choice_type (str): Either "love" or "cor"

        Returns:
            int: Number of milestone choices made
        """
        counter_name = f"{char}_{choice_type}_choices"
        return renpy.python.py_eval(counter_name)

    ############################################################################
    ## MC INTEGRITY ALIGNMENT SYSTEM
    ############################################################################

    def lock_mc_alignment():
        """
        Locks MC's moral alignment based on current integrity value.
        Should be called at the end of Episode 15.
        Can also be called earlier if integrity reaches 0 or 100 (pure paths).

        Returns:
            str: The locked alignment ("rogue", "neutral", or "paragon")

        Example usage:
            # At end of ep15
            $ alignment = lock_mc_alignment()

            # Or check manually
            if persistent.mc_alignment == "paragon":
                jump paragon_route
        """
        # Check if already locked
        if persistent.mc_alignment is not None:
            return persistent.mc_alignment

        # Get current integrity
        integrity = rm.get("mc", "integrity")

        # Determine alignment based on ranges
        if integrity <= 30:
            alignment = "rogue"
        elif integrity >= 70:
            alignment = "paragon"
        else:
            alignment = "neutral"

        # Lock the alignment
        persistent.mc_alignment = alignment
        rm.rels["mc"]["integrity_locked"] = True

        return alignment

    def get_mc_alignment():
        """
        Gets MC's current locked alignment.

        Returns:
            str or None: The locked alignment ("rogue", "neutral", "paragon") or None if unlocked
        """
        return getattr(persistent, 'mc_alignment', None)

    def is_alignment_locked():
        """
        Checks if MC's alignment has been locked.

        Returns:
            bool: True if alignment is locked, False otherwise
        """
        return persistent.mc_alignment is not None

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