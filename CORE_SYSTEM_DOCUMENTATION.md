# Core System Documentation

**Version:** 1.0
**Language:** English
**Last Updated:** November 2024

---

## Table of Contents

1. [Introduction](#introduction)
2. [System Overview](#system-overview)
3. [Relationship Management (RM)](#relationship-management-rm)
4. [Sexual Statistics (SexStats)](#sexual-statistics-sexstats)
5. [Wardrobe Management (WM)](#wardrobe-management-wm)
6. [Level System](#level-system)
7. [Milestone Decision System](#milestone-decision-system)
8. [Practical Examples](#practical-examples)
9. [Character Reference](#character-reference)
10. [Troubleshooting](#troubleshooting)

---

## Introduction

The **Core System** is the heart of the game's character progression and relationship tracking. It manages everything from how characters feel about you, what they're wearing, their corruption levels, and which story paths they'll follow.

Think of it as the game's memory - it remembers every choice you make, every interaction you have, and uses that information to shape the story as you play.

### What Does It Do?

- **Tracks Relationships**: Remembers how much each character trusts you or how corrupted they've become
- **Manages Statistics**: Keeps count of intimate moments and interactions
- **Handles Outfits**: Controls which clothes characters wear and when they unlock new outfits
- **Determines Story Paths**: Locks characters into specific storylines based on your choices
- **Shows Progress**: Displays notifications when your relationship reaches new milestones

---

## System Overview

The Core System consists of five main components:

### 1. **RM (Relationship Management)**
Controls character attributes like corruption, trust, integrity, and relationship status.

### 2. **SexStats**
Tracks intimate interactions and virginity status for all love interests.

### 3. **WM (Wardrobe Manager)**
Manages character outfits, unlocking, and switching between them.

### 4. **Level System**
Converts numerical stats (0-100) into levels (0-5) and shows notifications.

### 5. **Milestone Decision System**
Locks characters into story paths based on your cumulative choices.

---

## Relationship Management (RM)

The RM system tracks how characters relate to you and each other.

### Character Types

The system manages three types of characters:

#### **Love Interests** (Regular Characters)
- **Characters**: Amber, Nanami, Elizabeth, Isabella, Kanae, Arlette, Antonella, Madison, Paz
- **Attributes**:
  - `cor` (Corruption): How corrupted the character has become (0-100)
  - `trust` (Trust): How much they trust you (0-100)
  - `preg` (Pregnancy): Whether the character is pregnant (True/False)
  - `rel` (Relationship): Whether you're in a relationship (True/False)
  - `knows` (Knowledge): Whether you've met this character (True/False)
  - `emotionally_locked` (Emotional Lock): Whether the character has shut you out (True/False)

#### **Main Character (MC)**
- **Attributes**:
  - `integrity`: Your moral compass (0-100)
  - `integrity_locked`: Whether integrity can still change (True/False)

#### **Organizations**
- **Characters**: Takeo, TMPD, Osaka
- **Attributes**:
  - `trust`: How much the organization trusts you (0-100)

### How to Use RM

#### Updating Character Stats

To change a character's stats, use the `update` function with **base values**:

```renpy
# Base values - system applies character rates automatically
$ rm.update("amber", "cor", 3)       # Base 3 → 3 × 1.5 = 5 corruption (Amber's 1.5x cor rate)
$ rm.update("nanami", "trust", 2)    # Base 2 → 2 × 3.0 = 6 trust (Nanami's 3x trust rate)
$ rm.update("mc", "integrity", -2)   # Base -2 = -2 integrity (no rate for MC)
$ rm.update("takeo", "trust", 5)     # Base 5 = 5 trust (organizations have no rates)
```

**Parameters:**
- **Character ID**: The character's name (lowercase)
- **Attribute**: What you want to change ("cor", "trust", "integrity")
- **Value**: Base value to add (positive) or subtract (negative) - **system automatically applies character rates**

**Important Rules:**
- ✅ **Use base values (1, 2, 3, 5, 10)** - the system multiplies by character rates automatically
- ✅ Stats automatically stay between 0 and 100
- ✅ MC's integrity locks when it reaches 0 or 100
- ✅ You can't change a character's stats if they're emotionally locked
- ✅ **Each call only updates ONE attribute** - to update multiple attributes, make multiple calls
- ✅ **Values are automatically rounded** to integers (no decimals)

#### Updating Multiple Attributes

To update both corruption and trust (or any combination), make **separate calls** using **base values**:

```renpy
# Update both corruption and trust with same base value
$ rm.update("amber", "cor", 2)    # Base 2 → 2 × 1.5 = 3 corruption
$ rm.update("amber", "trust", 2)  # Base 2 → 2 × 1.0 = 2 trust

# Update both with different base values
$ rm.update("amber", "cor", 3)    # Base 3 → 3 × 1.5 = 5 corruption
$ rm.update("amber", "trust", -2) # Base -2 → -2 × 1.0 = -2 trust

# Common pattern: choice that increases one and decreases the other
menu:
    "Be gentle with her":
        $ rm.update("amber", "trust", 3)   # Base 3 → 3 × 1.0 = 3 trust
        $ rm.update("amber", "cor", -1)    # Base -1 → -1 × 1.5 = -2 corruption
        $ check_levels("amber", "trust", 3)
        $ check_levels("amber", "cor", -1)

    "Be forceful":
        $ rm.update("amber", "cor", 3)     # Base 3 → 3 × 1.5 = 5 corruption
        $ rm.update("amber", "trust", -2)  # Base -2 → -2 × 1.0 = -2 trust
        $ check_levels("amber", "cor", 3)
        $ check_levels("amber", "trust", -2)
```

**Note:** There is no syntax like `rm.update("amber", "cor" and "trust", 2)`. You must make individual calls for each attribute. Always use base values - the system handles rate multiplication automatically.

#### Getting Character Information

To check a character's current stats:

```renpy
$ amber_corruption = rm.get("amber", "cor")
$ nanami_trust = rm.get("nanami", "trust")
$ mc_integrity = rm.get("mc", "integrity")
$ in_relationship = rm.get("isabella", "rel")
$ is_pregnant = rm.get("kanae", "preg")
```

#### Managing Relationships

Update relationship status based on trust level:

```renpy
$ rm.update_rel("amber")  # If trust >= 70, sets rel to True
```

**Rule:** A character becomes your girlfriend when trust reaches 70 or higher.

#### Tracking Character Knowledge

Mark whether you've met a character:

```renpy
$ rm.set_knows("amber", True)   # You've met Amber
$ rm.set_knows("paz", False)    # You haven't met Paz yet
```

### The Emotional Lock System

When a character receives **3 strikes** (tracked separately in SexStats), they become emotionally locked:

**What Happens:**
- Their corruption and trust drop to 0
- You can't change their corruption or trust anymore
- The character has emotionally shut you out
- This represents a permanent consequence for poor choices

**Checking Emotional Lock:**

```renpy
$ is_locked = rm.is_emotionally_locked("amber")
if is_locked:
    "Amber won't talk to you anymore."
```

---

## Sexual Statistics (SexStats)

The SexStats system tracks intimate interactions with all love interests.

### Tracked Activities

For each love interest, the system tracks:

- `anal` - Anal sex encounters
- `assjob` - Assjob encounters
- `blowjob` - Oral sex encounters
- `creampie` - Creampie finishes
- `pussyjob` - Pussyjob encounters
- `sex` - Vaginal sex encounters
- `titjob` - Titjob encounters
- `virgin` - Virginity status (True/False)
- `strike` - Number of strikes (0-3)

### Starting Virginity Status

**Virgins at Start:**
- Nanami
- Isabella
- Madison
- Paz

**Non-Virgins at Start:**
- Amber
- Elizabeth
- Kanae
- Arlette
- Antonella

### How to Use SexStats

#### Incrementing Counters

When an intimate scene occurs:

```renpy
$ ss.add("amber", "blowjob")    # Add 1 to Amber's blowjob count
$ ss.add("nanami", "sex")       # Add 1 to Nanami's sex count
$ ss.add("isabella", "creampie") # Add 1 to Isabella's creampie count
```

#### Changing Virginity Status

When a character loses their virginity:

```renpy
$ ss.set("nanami", "virgin", False)  # Nanami is no longer a virgin
```

#### Managing Strikes

Add strikes for bad choices:

```renpy
$ current_strikes = ss.get("amber", "strike")
$ ss.set("amber", "strike", current_strikes + 1)
```

**Important:** When a character reaches 3 strikes, they become emotionally locked automatically.

#### Checking Statistics

Get current statistics:

```renpy
$ bj_count = ss.get("amber", "blowjob")
$ is_virgin = ss.get("nanami", "virgin")
$ strike_count = ss.get("isabella", "strike")

if bj_count > 5:
    "Amber has extensive experience now."

if is_virgin:
    "Nanami has never had sex before."

if strike_count >= 2:
    "Isabella is very upset with you. One more strike and she's done."
```

---

## Wardrobe Management (WM)

The WM system handles character outfits and clothing changes.

### Available Outfits Per Character

Each character has a different number of outfits:

| Character  | Max Outfits |
|-----------|-------------|
| Amber     | 6           |
| Nanami    | 9           |
| Elizabeth | 4           |
| Isabella  | 7           |
| Kanae     | 5           |
| Arlette   | 8           |
| Antonella | 4           |
| Madison   | 5           |
| Paz       | 6           |

**Note:** Outfit IDs start at 0 (default outfit is always ID 0).

### How to Use WM

#### Unlocking Outfits

To unlock a new outfit:

```renpy
$ wm.unlock("nanami", 3)     # Unlock outfit 3 for Nanami
$ wm.unlock("amber", 2)      # Unlock outfit 2 for Amber
```

**Rules:**
- Outfit 0 is always unlocked (default outfit)
- You can only unlock outfits that exist (within max range)
- Unlocking an outfit doesn't automatically equip it

#### Checking If Outfit Is Unlocked

```renpy
$ is_unlocked = wm.is_unlocked("nanami", 3)
if is_unlocked:
    "Nanami's special outfit is available!"
```

#### Changing Current Outfit

To set which outfit a character wears:

```renpy
$ wm.set("nanami", 2)   # Set Nanami's outfit to ID 2
```

**Rule:** You can only set outfits that have been unlocked.

#### Getting Current Outfit

Check which outfit is currently equipped:

```renpy
$ current = wm.get_current("nanami")
"Nanami is wearing outfit [current]."
```

#### Cycling Through Outfits

Move to next or previous unlocked outfit:

```renpy
$ wm.next_outfit("amber")    # Switch to next unlocked outfit
$ wm.prev_outfit("amber")    # Switch to previous unlocked outfit
```

**Behavior:** Cycles through unlocked outfits in order (wraps around at the end).

#### Getting All Unlocked Outfits

Get a list of all unlocked outfits:

```renpy
$ unlocked_list = wm.get_all_unlocked("nanami")
# Returns: [0, 2, 3, 5] (example)
```

### Practical Outfit Example

```renpy
label amber_date:
    # Unlock special date outfit
    $ wm.unlock("amber", 3)

    # Set it as current
    $ wm.set("amber", 3)

    # Show Amber in the new outfit
    show amber happy at center

    amber "Do you like my new dress?"
```

---

## Level System

The Level System converts raw numerical stats (0-100) into levels (0-5) for easier understanding and gating content.

### Level Ranges

Both corruption and trust use the same level ranges:

| Level | Range    | Description (Trust)      | Description (Corruption) |
|-------|----------|--------------------------|--------------------------|
| 0     | 0-16     | Stranger/Hostile         | Pure/Innocent            |
| 1     | 17-32    | Acquaintance             | Slightly Corrupted       |
| 2     | 33-48    | Friend                   | Moderately Corrupted     |
| 3     | 49-64    | Close Friend             | Notably Corrupted        |
| 4     | 65-80    | Very Close               | Highly Corrupted         |
| 5     | 81-100   | Intimate/Best Friend     | Fully Corrupted          |

### Getting a Character's Level

To check what level a character's stat is at:

```renpy
$ amber_trust_level = get_level_for_value(rm.get("amber", "trust"), trust_levels)
$ nanami_cor_level = get_level_for_value(rm.get("nanami", "cor"), corruption_levels)

if amber_trust_level >= 3:
    "Amber trusts you deeply."

if nanami_cor_level >= 2:
    "Nanami is becoming more open to your influence."
```

### Level Notifications

The system automatically shows notifications when levels change:

**Types of Notifications:**
- **Small Increase/Decrease**: When stats change but level stays the same
- **Level Up**: When a character gains a level
- **Level Down**: When a character loses a level

To trigger notifications after updating stats:

```renpy
$ rm.update("amber", "cor", 15)
$ check_levels("amber", "cor", 15)  # Shows notification

$ rm.update("nanami", "trust", 20)
$ check_levels("nanami", "trust", 20)  # Shows notification
```

**Important:** Always call `check_levels()` after `rm.update()` to show proper notifications.

### Using Levels to Gate Content

You can require specific levels to unlock dialogue choices:

```renpy
menu:
    "Casual conversation":
        jump .casual

    "Ask about her feelings" if get_level_for_value(rm.get("amber", "trust"), trust_levels) >= 2:
        # Only available if Amber's trust is Level 2 or higher
        jump .feelings

    "Make a bold move" if get_level_for_value(rm.get("amber", "cor"), corruption_levels) >= 3:
        # Only available if Amber's corruption is Level 3 or higher
        jump .bold
```

---

## Milestone Decision System

The Milestone Decision System is a two-phase progression system that locks characters into specific story paths.

### How It Works

#### **Phase 1: Foundation (Episodes 1-5)**

**Goal:** Build up stats and levels

- You make choices that increase corruption or trust
- Stats accumulate (0-100)
- Stats determine levels (0-5)
- Levels act as "keys" that unlock future choices

**Example:**
```renpy
menu:
    "Compliment her":
        $ rm.update("amber", "trust", 10)
        $ check_levels("amber", "trust", 10)

    "Tease her":
        $ rm.update("amber", "cor", 10)
        $ check_levels("amber", "cor", 10)
```

#### **Phase 2: Consolidation (Episode 6+)**

**Goal:** Make milestone decisions that determine final paths

- Certain special choices are "Milestone Decisions"
- These choices require specific levels to unlock
- Making these choices increments counters
- Reaching threshold (default 3) locks the path permanently

**Example:**
```renpy
menu:
    "Neutral choice":
        # Always available, doesn't count as milestone
        jump .neutral

    "I truly care about you." if get_level_for_value(rm.get("amber", "trust"), trust_levels) >= 2:
        # LOVE Milestone Decision - requires Trust Level 2+
        $ amber_love_choices += 1
        $ rm.update("amber", "trust", 15)
        $ check_levels("amber", "trust", 15)
        jump .love_path

    "You look better when flustered." if get_level_for_value(rm.get("amber", "cor"), corruption_levels) >= 2:
        # CORRUPTION Milestone Decision - requires Corruption Level 2+
        $ amber_cor_choices += 1
        $ rm.update("amber", "cor", 15)
        $ check_levels("amber", "cor", 15)
        jump .corruption_path
```

### Locking Paths

At a dramatic story moment (usually end of Episode 6), lock the path:

```renpy
label lock_paths_ep06_end:
    # Lock Amber's path based on milestone choices
    $ amber_path = lock_character_path("amber", love_threshold=3, cor_threshold=3)

    if persistent.amber_path == "love":
        "You've committed to a loving relationship with Amber."
    elif persistent.amber_path == "corruption":
        "You've chosen to corrupt Amber completely."
    else:
        "Your relationship with Amber remains undefined."
```

**Parameters:**
- `char`: Character ID
- `love_threshold`: Milestone love choices needed (default: 3)
- `cor_threshold`: Milestone corruption choices needed (default: 3)

**Returns:** `"love"`, `"corruption"`, or `"neutral"`

### Path Determination Logic

The system determines paths as follows:

1. **Both thresholds met**: Choose the path with more milestone choices
   - If tied: Use trust vs corruption stats as tiebreaker
2. **Only love threshold met**: Lock to "love"
3. **Only corruption threshold met**: Lock to "corruption"
4. **Neither threshold met**: Lock to "neutral"

### Using Locked Paths

In episodes 7+, branch based on locked paths:

```renpy
label amber_scene_ep07:
    if persistent.amber_path == "love":
        jump .love_route
    elif persistent.amber_path == "corruption":
        jump .corruption_route
    else:
        jump .neutral_route
```

### Helper Functions

#### Check Current Path
```renpy
$ current_path = get_character_path("amber")
# Returns: "love", "corruption", "neutral", or None (if not locked)
```

#### Check If Path Is Locked
```renpy
$ locked = is_path_locked("amber")
# Returns: True or False
```

#### Get Milestone Choice Count
```renpy
$ love_count = get_milestone_choices("amber", "love")
$ cor_count = get_milestone_choices("amber", "cor")
```

### Combining Paths and Stats

Even after locking paths, you can use stats for nuance:

```renpy
label amber_corruption_route:
    if rm.get("amber", "trust") >= 70:
        # High trust + corruption = willing submission
        amber "I've prepared everything for you, Master."
    else:
        # Low trust + corruption = reluctant submission
        amber "It's... ready."
        "She looks away nervously."
```

---

## Practical Examples

### Example 1: Basic Date Scene

```renpy
label amber_date_night:
    # Check if we've met Amber
    if not rm.get("amber", "knows"):
        $ rm.set_knows("amber", True)
        "You've just met Amber for the first time."

    # Increase trust from the date
    $ rm.update("amber", "trust", 15)
    $ check_levels("amber", "trust", 15)

    # Unlock and set a nice dress
    $ wm.unlock("amber", 2)
    $ wm.set("amber", 2)

    show amber happy at center

    amber "This has been wonderful."

    # Update relationship status
    $ rm.update_rel("amber")

    if rm.get("amber", "rel"):
        "Amber is now your girlfriend!"
```

### Example 2: Corruption Scene

```renpy
label corrupt_isabella:
    # Check corruption level first
    $ isabella_cor = get_level_for_value(rm.get("isabella", "cor"), corruption_levels)

    if isabella_cor < 2:
        "Isabella isn't corrupted enough for this."
        return

    # Scene proceeds
    menu:
        "Push her further":
            $ rm.update("isabella", "cor", 20)
            $ check_levels("isabella", "cor", 20)

            # Track the encounter
            $ ss.add("isabella", "sex")

            # Check if she was a virgin
            if ss.get("isabella", "virgin"):
                $ ss.set("isabella", "virgin", False)
                "Isabella has given you her virginity."

        "Stop here":
            $ rm.update("isabella", "trust", 10)
            $ check_levels("isabella", "trust", 10)
```

### Example 3: Strike System

```renpy
label bad_choice_amber:
    menu:
        "Apologize":
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)

        "Double down":
            # This is a bad choice - add a strike
            $ current_strikes = ss.get("amber", "strike")
            $ ss.set("amber", "strike", current_strikes + 1)

            # Check if we hit 3 strikes
            $ just_locked = rm.check_emotional_lock("amber")

            if just_locked:
                amber "I can't believe you... We're done. Don't talk to me again."
                "Amber has emotionally shut you out."
                "Her corruption and trust have been reset to 0."
                "You can no longer pursue a relationship with her."
            elif current_strikes + 1 >= 2:
                amber "I'm getting really tired of this..."
                "Warning: Amber has [current_strikes + 1] strike(s)."
```

### Example 4: Dynamic Outfit Selection

```renpy
label amber_apartment:
    # Set outfit based on trust level
    $ trust_level = get_level_for_value(rm.get("amber", "trust"), trust_levels)

    if trust_level >= 4:
        # Very close - wear intimate outfit
        if wm.is_unlocked("amber", 4):
            $ wm.set("amber", 4)
    elif trust_level >= 2:
        # Friends - wear casual outfit
        if wm.is_unlocked("amber", 2):
            $ wm.set("amber", 2)
    else:
        # Not close - default outfit
        $ wm.set("amber", 0)

    show amber at center
```

### Example 5: Milestone Decision Scene

```renpy
label amber_critical_choice_ep06:
    # This is a key moment in Episode 6
    $ trust_level = get_level_for_value(rm.get("amber", "trust"), trust_levels)
    $ cor_level = get_level_for_value(rm.get("amber", "cor"), corruption_levels)

    amber "What do you really want from me?"

    menu:
        "I want us to be together.":
            # This is always available but doesn't count as milestone
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            jump .neutral_response

        "I care about you deeply." if trust_level >= 2:
            # LOVE MILESTONE - counts toward love path
            $ amber_love_choices += 1
            $ rm.update("amber", "trust", 20)
            $ check_levels("amber", "trust", 20)

            amber "I... I care about you too."
            jump .love_response

        "I want to own you completely." if cor_level >= 2:
            # CORRUPTION MILESTONE - counts toward corruption path
            $ amber_cor_choices += 1
            $ rm.update("amber", "cor", 20)
            $ check_levels("amber", "cor", 20)

            amber "I... I understand."
            "She looks at you with a mix of fear and excitement."
            jump .corruption_response
```

### Example 6: Path Locking at End of Episode 6

```renpy
label ep06_finale:
    # Lock all character paths
    $ amber_path = lock_character_path("amber")
    $ nanami_path = lock_character_path("nanami")
    $ isabella_path = lock_character_path("isabella")

    # Show results to player
    "Your choices have determined your relationships:"

    if persistent.amber_path == "love":
        "Amber: Love Path - You've built a genuine relationship."
    elif persistent.amber_path == "corruption":
        "Amber: Corruption Path - You've dominated her completely."
    else:
        "Amber: Neutral Path - Your relationship remains casual."

    # Continue for other characters...
```

### Example 7: Using Locked Paths in Episode 7+

```renpy
label amber_bedroom_ep07:
    # Branch based on locked path
    if persistent.amber_path == "love":
        jump .love_scene
    elif persistent.amber_path == "corruption":
        jump .corruption_scene
    else:
        jump .neutral_scene

label .love_scene:
    $ wm.set("amber", 3)  # Romantic outfit
    show amber loving at center

    amber "I've been waiting for you."

    # Use trust for additional nuance
    if rm.get("amber", "trust") >= 85:
        "She embraces you warmly."
    else:
        "She smiles shyly."

    # Scene continues...

label .corruption_scene:
    $ wm.set("amber", 5)  # Submissive outfit
    show amber submissive at center

    amber "What are your orders, Master?"

    # Use corruption for intensity
    if rm.get("amber", "cor") >= 85:
        "She kneels immediately."
    else:
        "She hesitates briefly before kneeling."

    # Scene continues...

label .neutral_scene:
    $ wm.set("amber", 0)  # Default outfit
    show amber neutral at center

    amber "Oh, hey. What's up?"

    # Casual interaction
```

---

## Character Reference

### All Characters

| Character  | Type          | Available Attributes                          |
|-----------|---------------|-----------------------------------------------|
| Amber     | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Nanami    | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Elizabeth | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Isabella  | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Kanae     | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Arlette   | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Antonella | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Madison   | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| Paz       | Love Interest | cor, trust, preg, rel, knows, emotionally_locked |
| MC        | Main Character| integrity, integrity_locked                   |
| Takeo     | Organization  | trust                                         |
| TMPD      | Organization  | trust                                         |
| Osaka     | Organization  | trust                                         |

### Automatic Character Progression Rates

**NEW SYSTEM (Version 2.0):** Character progression rates are now applied **automatically** to all stat changes. You only need to think about "base values" - the system multiplies them by character-specific rates for you.

Different characters respond differently to your actions:

| Character  | Trust Rate | Corruption Rate | Notes                           |
|-----------|------------|-----------------|----------------------------------|
| Amber     | 1x         | 1.5x            | More easily corrupted           |
| Antonella | 0.25x      | 1x              | Very hard to gain trust         |
| Arlette   | 1.5x       | 1.5x            | Responds strongly to both       |
| Elizabeth | 2x         | 1x              | Gains trust quickly             |
| Isabella  | 1x         | 1x              | Balanced progression            |
| Kanae     | 0.5x       | 0.5x            | Slow progression both ways      |
| Madison   | 0.5x       | 2x              | Hard to trust, easily corrupted |
| Nanami    | 3x         | 1x              | Very trusting, hard to corrupt  |
| Paz       | 1x         | 1x              | Balanced progression            |

**How It Works (Automatic):**
```renpy
# You write base values:
$ rm.update("nanami", "trust", 3)    # Base value: 3
$ rm.update("madison", "cor", 5)     # Base value: 5
$ rm.update("antonella", "trust", 8) # Base value: 8

# System automatically applies rates:
# Nanami gets: 3 × 3.0 = 9 trust (3x rate)
# Madison gets: 5 × 2.0 = 10 corruption (2x rate)
# Antonella gets: 8 × 0.25 = 2 trust (0.25x rate)
```

**Key Points:**
- ✅ **Always use base values** - the system handles multiplication automatically
- ✅ **Values are rounded** - no decimal stats (e.g., 2.5 becomes 3)
- ✅ **Works with negatives** - negative values are also multiplied by rates
- ✅ **No special syntax needed** - just use `rm.update()` as usual

### Standard Base Values Guide

Use these **base values** in your rm.update() calls. The system will automatically apply character-specific multipliers.

| Decision Type              | Trust Base | Corruption Base | Integrity Base | Example                          |
|----------------------------|------------|-----------------|----------------|----------------------------------|
| **Casual interaction**     | ±1         | ±1              | ±1             | Small talk, minor choices        |
| **Personal moment**        | ±2         | ±2              | ±2             | Sharing feelings, personal favor |
| **Important decision**     | ±3         | ±3              | ±3             | Significant moral choice         |
| **Critical story moment**  | ±5         | ±5              | ±5             | Major relationship turning point |
| **Milestone decision**     | ±10        | ±10             | N/A            | Episode 6+ path-defining choices |

**Examples in Practice:**

```renpy
# Casual: complimenting a character
$ rm.update("amber", "trust", 1)  # Base 1 × 1.0 = 1 trust

# Personal: comforting someone emotional
$ rm.update("nanami", "trust", 2)  # Base 2 × 3.0 = 6 trust

# Important: choosing to protect someone
$ rm.update("elizabeth", "trust", 3)  # Base 3 × 2.0 = 6 trust

# Critical: accepting intimate proposal
$ rm.update("madison", "cor", 5)  # Base 5 × 2.0 = 10 corruption
$ rm.update("mc", "integrity", -5)  # Base -5 = -5 integrity

# Milestone (Episode 6+): path-defining choice
$ rm.update("amber", "trust", 10)  # Base 10 × 1.0 = 10 trust
$ amber_love_choices += 1
```

**Negative Values:**

```renpy
# Rejecting someone
$ rm.update("amber", "trust", -2)  # Base -2 × 1.0 = -2 trust

# Disappointing Nanami
$ rm.update("nanami", "trust", -3)  # Base -3 × 3.0 = -9 trust

# Corruption reversal (rare)
$ rm.update("madison", "cor", -1)  # Base -1 × 2.0 = -2 corruption
```

**Why These Values?**

These base values create balanced progression across all 20 episodes:
- **Casual (±1)**: Small, incremental changes
- **Personal (±2)**: Noticeable impact
- **Important (±3)**: Significant relationship shift
- **Critical (±5)**: Major story moments
- **Milestone (±10)**: Path-defining decisions (ep6+)

With character rates, these translate to meaningful but not extreme changes. For example:
- Nanami gains 3-6 trust from personal moments (2 × 3.0)
- Madison struggles to gain trust (2 × 0.5 = 1) but corrupts easily (2 × 2.0 = 4)

### Sexual Statistics Reference

All love interests track these statistics:

| Statistic | Type    | Description                    |
|-----------|---------|--------------------------------|
| anal      | Integer | Number of anal sex encounters  |
| assjob    | Integer | Number of assjob encounters    |
| blowjob   | Integer | Number of oral sex encounters  |
| creampie  | Integer | Number of creampie finishes    |
| pussyjob  | Integer | Number of pussyjob encounters  |
| sex       | Integer | Number of vaginal sex encounters |
| titjob    | Integer | Number of titjob encounters    |
| virgin    | Boolean | Virginity status (True/False)  |
| strike    | Integer | Number of strikes (0-3)        |

### Wardrobe Reference

| Character  | Available Outfits |
|-----------|-------------------|
| Amber     | 0, 1, 2, 3, 4, 5  |
| Nanami    | 0, 1, 2, 3, 4, 5, 6, 7, 8 |
| Elizabeth | 0, 1, 2, 3        |
| Isabella  | 0, 1, 2, 3, 4, 5, 6 |
| Kanae     | 0, 1, 2, 3, 4     |
| Arlette   | 0, 1, 2, 3, 4, 5, 6, 7 |
| Antonella | 0, 1, 2, 3        |
| Madison   | 0, 1, 2, 3, 4     |
| Paz       | 0, 1, 2, 3, 4, 5  |

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Stats Don't Update

**Symptoms:** You call `rm.update()` but nothing changes

**Solutions:**
1. Check character name spelling (must be lowercase)
2. Verify attribute name is correct ("cor", "trust", "integrity")
3. Make sure character isn't emotionally locked
4. Check if MC's integrity is locked

**Example:**
```renpy
# Wrong
$ rm.update("Amber", "corruption", 10)  # Wrong: uppercase name, wrong attribute

# Correct
$ rm.update("amber", "cor", 10)
```

#### Issue: Notifications Don't Appear

**Symptoms:** Stats update but no notification shows

**Solution:** Always call `check_levels()` after `rm.update()`

**Example:**
```renpy
# Wrong
$ rm.update("amber", "trust", 15)  # No notification

# Correct
$ rm.update("amber", "trust", 15)
$ check_levels("amber", "trust", 15)  # Shows notification
```

#### Issue: Can't Change Outfit

**Symptoms:** `wm.set()` doesn't work

**Solutions:**
1. Make sure outfit is unlocked first
2. Check that outfit ID is valid for that character
3. Verify character name is correct

**Example:**
```renpy
# Wrong
$ wm.set("amber", 10)  # Amber only has 6 outfits (0-5)

# Correct
$ wm.unlock("amber", 3)  # Unlock first
$ wm.set("amber", 3)     # Then set
```

#### Issue: Character Is Emotionally Locked

**Symptoms:** Can't change corruption or trust for a character

**Solution:** Check if character has 3 strikes

**Example:**
```renpy
$ is_locked = rm.is_emotionally_locked("amber")
$ strikes = ss.get("amber", "strike")

if is_locked:
    "Amber has [strikes] strikes and is emotionally locked."
    "Her stats can no longer change."
```

#### Issue: Path Won't Lock

**Symptoms:** `lock_character_path()` returns "neutral" when you expected "love" or "corruption"

**Solutions:**
1. Check milestone choice counters
2. Verify you incremented the correct counters in dialogue
3. Make sure thresholds aren't set too high

**Example:**
```renpy
# Check current progress
$ love_count = get_milestone_choices("amber", "love")
$ cor_count = get_milestone_choices("amber", "cor")

"Amber has [love_count] love choices and [cor_count] corruption choices."
"Need 3 of either to lock path."
```

#### Issue: MC's Integrity Won't Change

**Symptoms:** Integrity is stuck

**Solution:** Check if integrity is locked (happens at 0 or 100)

**Example:**
```renpy
$ is_locked = rm.get("mc", "integrity_locked")
$ current_integrity = rm.get("mc", "integrity")

if is_locked:
    "Your integrity is locked at [current_integrity]."
    "This represents your final moral state."
```

### Best Practices

#### 1. Always Use check_levels()

```renpy
# Good practice
$ rm.update("amber", "trust", 15)
$ check_levels("amber", "trust", 15)
```

#### 2. Check Before Unlocking Content

```renpy
# Check levels before showing content
$ trust_level = get_level_for_value(rm.get("amber", "trust"), trust_levels)

if trust_level >= 3:
    # Show intimate scene
    jump .intimate_scene
else:
    # Not ready yet
    "Amber isn't comfortable with this yet."
    return
```

#### 3. Unlock Outfits Naturally

```renpy
# Unlock outfits as rewards or story progression
if rm.get("amber", "rel"):
    $ wm.unlock("amber", 3)
    "Amber has unlocked a special outfit for you!"
```

#### 4. Track Virginity Properly

```renpy
# Always check and update virginity status
if ss.get("nanami", "virgin"):
    "This is Nanami's first time."
    $ ss.set("nanami", "virgin", False)

$ ss.add("nanami", "sex")
```

#### 5. Use Milestone Decisions Strategically

```renpy
# Reserve milestone decisions for important choices
# Regular choices don't need to increment counters
menu:
    "Chat casually":
        # Regular choice - no counter
        $ rm.update("amber", "trust", 5)
        $ check_levels("amber", "trust", 5)

    "Confess your feelings" if trust_level >= 2:
        # Milestone decision - increment counter
        $ amber_love_choices += 1
        $ rm.update("amber", "trust", 20)
        $ check_levels("amber", "trust", 20)
```

---

## Summary

The Core System is designed to create a living, breathing relationship system that:

- **Remembers** every choice you make
- **Responds** with realistic character progression
- **Locks** characters into meaningful paths
- **Rewards** player investment with unlockable content
- **Punishes** poor choices with consequences

By understanding these systems, you can create compelling, dynamic stories that respond to player choices in meaningful ways.

### Quick Reference

```renpy
# Relationship Management
$ rm.update("char", "attr", value)
$ rm.get("char", "attr")
$ rm.update_rel("char")
$ rm.set_knows("char", True/False)

# Sexual Statistics
$ ss.add("char", "stat")
$ ss.get("char", "stat")
$ ss.set("char", "stat", value)

# Wardrobe Management
$ wm.unlock("char", outfit_id)
$ wm.set("char", outfit_id)
$ wm.get_current("char")
$ wm.next_outfit("char")

# Level System
$ level = get_level_for_value(rm.get("char", "attr"), level_dict)
$ check_levels("char", "attr", value)

# Milestone System
$ char_love_choices += 1
$ char_cor_choices += 1
$ path = lock_character_path("char")
$ path = get_character_path("char")
$ locked = is_path_locked("char")
```

---

**End of Documentation**