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
                    # Regular characters have: corruption, trust, pregnancy status, relationship status, if MC knows them, and emotional lock
                    self.rels[char] = {"cor": 0, "trust": 0, "preg": False, "rel": False, "knows": False, "emotionally_locked": False}

        def update(self, char, attr, val):
            """
            Updates a character's attribute by adding/subtracting a value
            Includes emotional lock check (3 strikes) and path lock system (milestone decisions)

            Args:
                char (str): Character ID (e.g., "amber", "mc")
                attr (str): Attribute to update ("cor", "trust", "integrity", etc.)
                val (int): Value to add/subtract
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

                # PATH LOCK SYSTEM: Auto-check and apply path locks for love interests
                if char not in ["mc", "takeo", "tmpd", "osaka"] and attr in ["cor", "trust"]:
                    # Auto-check if path should be locked (similar to strike auto-lock)
                    locked_path = self.check_and_lock_path(char)

                    if locked_path == "love":
                        # Love path locked: block corruption, double trust
                        if attr == "cor":
                            return  # Block corruption gains
                        elif attr == "trust":
                            val = val * 2  # Double trust gains
                    elif locked_path == "corruption":
                        # Corruption path locked: block trust, double corruption
                        if attr == "trust":
                            return  # Block trust gains
                        elif attr == "cor":
                            val = val * 2  # Double corruption gains
                    # If neutral or None (not locked yet), no blocking, no doubling

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

        def check_and_lock_path(self, char, love_threshold=3, cor_threshold=3):
            """
            Auto-checks milestone counters and locks path if threshold reached
            Similar to emotional lock system - called automatically during rm.update()

            Args:
                char (str): Character ID
                love_threshold (int): Milestone love choices needed to lock (default: 3)
                cor_threshold (int): Milestone corruption choices needed to lock (default: 3)

            Returns:
                str or None: Current locked path ("love", "corruption", "neutral") or None if not locked yet
            """
            path_var_name = f"{char}_path"

            # Check if already locked in persistent
            current_path = getattr(persistent, path_var_name, None)
            if current_path is not None:
                return current_path  # Already locked, return existing path

            # Get milestone choice counters
            try:
                love_choices = renpy.python.py_eval(f"{char}_love_choices")
                cor_choices = renpy.python.py_eval(f"{char}_cor_choices")
            except:
                return None  # Counters don't exist yet

            # Check if threshold reached for auto-lock
            locked_path = None

            if love_choices >= love_threshold and cor_choices >= cor_threshold:
                # Both thresholds met - choose based on which has more choices
                if love_choices > cor_choices:
                    locked_path = "love"
                elif cor_choices > love_choices:
                    locked_path = "corruption"
                else:
                    # Tie - use trust vs corruption stats as tiebreaker
                    trust_val = self.get(char, "trust")
                    cor_val = self.get(char, "cor")
                    locked_path = "love" if trust_val >= cor_val else "corruption"
            elif love_choices >= love_threshold:
                locked_path = "love"
            elif cor_choices >= cor_threshold:
                locked_path = "corruption"
            # else: threshold not reached yet, return None

            # If threshold reached, lock it permanently in persistent
            if locked_path is not None:
                setattr(persistent, path_var_name, locked_path)

                # Show notification that path has been locked
                # Similar to strike notifications
                if locked_path == "love":
                    show_custom_notification("path_lock_love", char=char_proper_names.get(char, char))
                elif locked_path == "corruption":
                    show_custom_notification("path_lock_corruption", char=char_proper_names.get(char, char))

            return locked_path

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

    ############################################################################
    ## MILESTONE DECISION SYSTEM - PATH LOCKING (Episode 6+)
    ############################################################################

    def lock_character_path(char, love_threshold=3, cor_threshold=3):
        """
        DEPRECATED: Path locking now happens automatically via rm.update()

        This function is kept for backwards compatibility, but is no longer needed.
        Path locking now works like the strike system - it auto-locks when thresholds
        are reached during any rm.update() call.

        The auto-lock system:
        - Checks milestone counters every time rm.update() is called
        - Locks path when love_choices >= 3 OR cor_choices >= 3
        - Once locked, blocks opposite stat and doubles locked stat
        - Works automatically across episodes (ep06, ep07, ep08...)

        You can still call this function to manually check/force a lock, but it's not required.

        Args:
            char (str): Character ID (e.g., "amber", "nanami")
            love_threshold (int): Number of love choices needed to lock love path (default: 3)
            cor_threshold (int): Number of corruption choices needed to lock corruption path (default: 3)

        Returns:
            str: The locked path ("love", "corruption", "neutral", or None if not locked yet)

        Example usage:
            $ locked_path = lock_character_path("amber")  # Check current path
            $ locked_path = get_character_path("amber")   # Better: use this instead
        """
        # Just call the auto-lock function that's already integrated in rm.update()
        return rm.check_and_lock_path(char, love_threshold, cor_threshold)

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