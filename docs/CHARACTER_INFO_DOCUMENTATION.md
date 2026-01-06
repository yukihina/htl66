# Character Information System Documentation

**Version:** 1.0
**Language:** English
**Last Updated:** November 2024

---

## Table of Contents

1. [Introduction](#introduction)
2. [System Overview](#system-overview)
3. [Character Data Structure](#character-data-structure)
4. [Relationship Term System](#relationship-term-system)
5. [Accessing Character Information](#accessing-character-information)
6. [Updating Character Data](#updating-character-data)
7. [Available Characters](#available-characters)
8. [Practical Examples](#practical-examples)
9. [Helper Functions](#helper-functions)
10. [Troubleshooting](#troubleshooting)

---

## Introduction

The **Character Information System** manages all character data in your game, including names, ages, physical attributes, and biographical information. It also handles dynamic text replacement for family/relationship terms based on whether your game is patched or unpatched.

### What Does It Do?

- **Stores Character Data**: Centralizes all character information
- **Dynamic Text Replacement**: Changes family terms based on patch status
- **Easy Access**: Simple syntax to get character information
- **Update Functions**: Modify character data as the story progresses
- **Profile Generation**: Create formatted character profiles

---

## System Overview

### Two Character Types

1. **Love Interests** (Main characters you can romance)
   - Have full attributes: name, age, height, weight, measurements, info
   - Example: Amber, Nanami, Elizabeth

2. **Main Character** (The protagonist)
   - Has: age, height, weight, info
   - Name is stored separately as `mc_name`

### Patched vs Unpatched

The system automatically changes relationship terms:

**Patched Mode** (family terms):
- Mother, sister, brother, family, etc.

**Unpatched Mode** (non-family terms):
- Landlady, close friend, household, etc.

This allows your game to work in different regions/platforms with content restrictions.

---

## Character Data Structure

### Love Interest Attributes

Every love interest character has these attributes:

| Attribute     | Type   | Example          | Description                    |
|---------------|--------|------------------|--------------------------------|
| name          | String | "Amber"          | Character's display name       |
| age           | Number | 37               | Character's age in years       |
| height        | String | "1.77 m"         | Character's height             |
| weight        | String | "79.6 kg"        | Character's weight             |
| measurements  | String | "b 99 - w 66..." | Body measurements              |
| info          | String | "A rebellious..." | Character biography            |

### Main Character Attributes

The main character (mc) has:

| Attribute | Type   | Example       | Description              |
|-----------|--------|---------------|--------------------------|
| age       | Number | 39            | MC's age in years        |
| height    | String | "1.85 m"      | MC's height              |
| weight    | String | "85 kg"       | MC's weight              |
| info      | String | "A Tokyo..." | MC's biography           |

**Note:** MC's name is stored in the `mc_name` variable, not in the character object.

---

## Relationship Term System

### How It Works

You use placeholder codes in character descriptions, and the system automatically replaces them with appropriate terms based on patch status.

### Available Placeholders

| Code              | Patched          | Unpatched        | Usage Example           |
|-------------------|------------------|------------------|-------------------------|
| [mo_full_r_low]   | mother           | landlady         | "My [mo_full_r_low]"   |
| [si_full_r_low]   | sister           | close friend     | "My [si_full_r_low]"   |
| [br_full_r_low]   | brother          | close friend     | "My [br_full_r_low]"   |
| [mo_r_low]        | mom              | landlady         | "My [mo_r_low]"        |
| [da_r_low]        | dad              | landlord         | "My [da_r_low]"        |
| [dau_r_low]       | daughter         | young lady       | "His [dau_r_low]"      |
| [niec_r_low]      | niece            | younger friend   | "My [niec_r_low]"      |
| [fm_r_low]        | family           | household        | "Our [fm_r_low]"       |
| [so_r_low]        | son              | young man        | "Their [so_r_low]"     |
| [da_r]            | Dad              | Landlord         | "[da_r] is home"       |
| [mc_name]         | (Player's name)  | (Player's name)  | "[mc_name] arrived"    |

### Example Usage

**In Character Info:**
```python
amber.info = "She lives with her [mo_r_low] and worries about [fm_r_low] expectations."
```

**What Players See:**

**Patched:**
> "She lives with her mom and worries about family expectations."

**Unpatched:**
> "She lives with her landlady and worries about household expectations."

---

## Accessing Character Information

### Getting Basic Information

To get a character's data:

```renpy
# Get character name
$ character_name = amber.name  # Returns: "Amber"

# Get character age
$ character_age = amber.age  # Returns: 37

# Get character height
$ character_height = amber.height  # Returns: "1.77 m"

# Get character weight
$ character_weight = amber.weight  # Returns: "79.6 kg"

# Get measurements
$ measurements = amber.measurements  # Returns: "b 99 - w 66 - h 106"
```

### Getting Character Biography

```renpy
# Get character info with automatic term replacement
$ bio = amber.info

# Display in dialogue
"[amber.info]"

# Use in text box
text "[amber.info]"
```

**Important:** When you access `.info`, placeholders are automatically replaced with appropriate terms.

### Displaying Character Data

```renpy
label show_amber_profile:
    "Name: [amber.name]"
    "Age: [amber.age]"
    "Height: [amber.height]"
    "Weight: [amber.weight]"
    "Measurements: [amber.measurements]"
    ""
    "[amber.info]"
```

---

## Updating Character Data

### Updating Age

```renpy
# Update character age
$ amber.set_age(38)

# Or update directly
$ amber.age = 38
```

### Updating Information

```renpy
# Add new information to bio
$ amber.update_info("She recently started learning to paint.")

# Replace entire bio
$ amber.info = "A completely new description here."
```

### Updating Measurements

```renpy
$ amber.set_measurements("b 100 - w 65 - h 107")
```

### Getting Full Profile

```renpy
# Get formatted profile with all data
$ full_profile = amber.get_full_profile()

# Display it
"[full_profile]"
```

**Output:**
```
Name: Amber
Age: 37
Height: 1.77 m
Weight: 79.6 kg
Measurements: b 99 - w 66 - h 106

A rebellious streaming girl who transformed herself...
```

---

## Available Characters

### Love Interests

#### Amber
```renpy
amber.name          # "Amber"
amber.age           # 37
amber.height        # "1.77 m"
amber.weight        # "79.6 kg"
amber.measurements  # "b 99 - w 66 - h 106"
amber.info          # Biography with dynamic terms
```

#### Nanami
```renpy
nanami.name         # "Nanami"
nanami.age          # 18
nanami.height       # "1.48 m"
nanami.weight       # "48.1 kg"
nanami.measurements # "b 90 - w 57 - h 86"
nanami.info         # Biography with dynamic terms
```

#### Elizabeth
```renpy
elizabeth.name          # "Elizabeth"
elizabeth.age           # 59
elizabeth.height        # "1.73 m"
elizabeth.weight        # "69.5 kg"
elizabeth.measurements  # "b 97 - w 64 - h 103"
elizabeth.info          # Biography with dynamic terms
```

#### Isabella
```renpy
isabella.name         # "Isabella"
isabella.age          # 18
isabella.height       # "1.45 m"
isabella.weight       # "40.1 kg"
isabella.measurements # "b 74 - w 56 - h 80"
isabella.info         # Biography with dynamic terms
```

#### Kanae
```renpy
kanae.name          # "Kanae"
kanae.age           # 43
kanae.height        # "1.61 m"
kanae.weight        # "55.1 kg"
kanae.measurements  # "b 87 - w 57 - h 87"
kanae.info          # Biography with dynamic terms
```

#### Arlette
```renpy
arlette.name          # "Arlette"
arlette.age           # 24
arlette.height        # "1.70 m"
arlette.weight        # "67.1 kg"
arlette.measurements  # "b 95 - w 64 - h 98"
arlette.info          # Biography with dynamic terms
```

#### Antonella
```renpy
antonella.name          # "Antonella"
antonella.age           # 39
antonella.height        # "1.60 m"
antonella.weight        # "58.8 kg"
antonella.measurements  # "b 87 - w 60 - h 93"
antonella.info          # Biography with dynamic terms
```

#### Madison
```renpy
madison.name          # "Madison"
madison.age           # 18
madison.height        # "1.68 m"
madison.weight        # "52.8 kg"
madison.measurements  # "b 87 - w 61 - h 84"
madison.info          # Biography with dynamic terms
```

#### Paz
```renpy
paz.name          # "Paz"
paz.age           # 37
paz.height        # "1.62 m"
paz.weight        # "70 kg"
paz.measurements  # "b 94 - w 62 - h 103"
paz.info          # Biography with dynamic terms
```

### Main Character

```renpy
mc.age      # 39
mc.height   # "1.85 m"
mc.weight   # "85 kg"
mc.info     # Biography with dynamic terms
mc_name     # Player's name (stored separately)
```

---

## Practical Examples

### Example 1: Character Profile Screen

```renpy
label show_character_profile:
    menu:
        "Whose profile do you want to see?"

        "Amber":
            jump show_amber

        "Nanami":
            jump show_nanami

        "Back":
            return

label show_amber:
    # Display Amber's profile
    "CHARACTER PROFILE"
    ""
    "Name: [amber.name]"
    "Age: [amber.age] years old"
    "Height: [amber.height]"
    "Weight: [amber.weight]"
    "Measurements: [amber.measurements]"
    ""
    "[amber.info]"
    ""
    "Press any key to continue..."
    return
```

### Example 2: Dynamic Dialogue

```renpy
label family_discussion:
    amber "I was talking to my [mo_r_low] yesterday."

    mc "How is your [mo_r_low] doing?"

    amber "She's good. The whole [fm_r_low] is planning a dinner this weekend."

    mc "Sounds nice. Will your [si_full_r_low] be there too?"

    amber "Yeah, everyone's coming!"
```

**Patched Version Shows:**
> "I was talking to my mom yesterday."
> "How is your mom doing?"
> "The whole family is planning..."
> "Will your sister be there too?"

**Unpatched Version Shows:**
> "I was talking to my landlady yesterday."
> "How is your landlady doing?"
> "The whole household is planning..."
> "Will your close friend be there too?"

### Example 3: Updating Character Info

```renpy
label story_progression:
    "A year has passed..."

    # Update ages
    $ amber.set_age(38)
    $ nanami.set_age(19)
    $ mc.age = 40

    # Add new information
    $ amber.update_info("She's now a successful content creator with millions of followers.")
    $ nanami.update_info("She's gained confidence and no longer relies on Madison.")

    "Things have changed..."
```

### Example 4: Conditional Information

```renpy
label reveal_background:
    if trust_level >= 5:
        # High trust - reveal detailed info
        amber "[amber.info]"
        amber "And there's more you should know..."
        $ amber.update_info("She has a complicated past with the yakuza that still haunts her.")

    else:
        # Low trust - basic info only
        amber "I'd rather not talk about my past right now."
```

### Example 5: Using Helper Functions

```renpy
label character_comparison:
    # Get character by name
    $ char = get_character_by_name("Amber")

    if char:
        "Found character: [char.name]"
        "Age: [char.age]"

    # Get all ages
    $ ages = get_character_ages()

    "Character ages:"
    for name, age in ages.items():
        "[name]: [age] years old"

    # Get summary
    $ summary = get_character_summary("Nanami")
    "[summary]"
```

### Example 6: Batch Updates

```renpy
label time_skip:
    "Five years later..."

    # Update multiple ages at once
    $ age_updates = {
        "Amber": 42,
        "Nanami": 23,
        "Isabella": 23,
        "Madison": 23
    }

    $ set_all_character_ages(age_updates)

    "Everyone has grown and changed..."
```

---

## Helper Functions

### get_character_by_name()

Get a character object by their display name:

```renpy
$ char = get_character_by_name("Amber")

if char:
    "Found: [char.name]"
    "Age: [char.age]"
else:
    "Character not found"
```

**Parameters:**
- `character_name` (string): The display name of the character

**Returns:**
- Character object or None if not found

### get_all_love_interests()

Get a list of all love interest characters:

```renpy
$ all_lis = get_all_love_interests()

for li in all_lis:
    "[li.name] - Age [li.age]"
```

**Returns:**
- List of all LoveInterest objects

### get_character_ages()

Get ages of all characters as a dictionary:

```renpy
$ ages = get_character_ages()

for name, age in ages.items():
    "[name]: [age]"
```

**Returns:**
- Dictionary: `{"Amber": 37, "Nanami": 18, ...}`

### get_character_summary()

Get a brief summary of a character:

```renpy
$ summary = get_character_summary("Isabella")
"[summary]"
```

**Output Example:**
> "Isabella, 18 years old. 1.45 m, 40.1 kg."

**Parameters:**
- `character_name` (string): Display name of character

**Returns:**
- String summary or error message

### set_all_character_ages()

Update multiple character ages at once:

```renpy
$ age_dict = {
    "Amber": 40,
    "Nanami": 20,
    "Isabella": 20
}

$ set_all_character_ages(age_dict)
```

**Parameters:**
- `age_dict` (dictionary): Maps character names to new ages

### update_li_info()

Update a love interest's information by variable name:

```renpy
$ update_li_info("amber", "She now runs her own streaming studio.")
```

**Parameters:**
- `li_name` (string): Variable name (lowercase, e.g., "amber")
- `new_info` (string): Information to add to biography

### validate_character_data()

Check all character data for errors:

```renpy
$ errors = validate_character_data()

if errors:
    "Found errors in character data:"
    for error in errors:
        "[error]"
else:
    "All character data is valid!"
```

**Returns:**
- List of error messages (empty list if all valid)

**Checks:**
- Names are not empty
- Ages are not negative
- Physical attributes are present

---

## Troubleshooting

### Common Issues

#### Issue: Placeholders Not Replaced

**Symptoms:** You see `[mo_r_low]` in text instead of "mom" or "landlady"

**Solutions:**
1. Use `.info` property, not `._info`:
   ```renpy
   # Correct
   $ bio = amber.info

   # Wrong
   $ bio = amber._info
   ```

2. Make sure placeholder is in square brackets:
   ```renpy
   # Correct
   "My [mo_r_low] is home"

   # Wrong
   "My mo_r_low is home"
   ```

#### Issue: Character Not Found

**Symptoms:** `get_character_by_name()` returns None

**Solutions:**
1. Check name spelling (case-sensitive):
   ```renpy
   # Correct
   $ char = get_character_by_name("Amber")

   # Wrong
   $ char = get_character_by_name("amber")
   $ char = get_character_by_name("AMBER")
   ```

2. Make sure character exists in the system

#### Issue: Age Updates Don't Work

**Symptoms:** Age doesn't change when you update it

**Solutions:**
1. Use `set_age()` method:
   ```renpy
   # Correct
   $ amber.set_age(38)

   # Also correct
   $ amber.age = 38
   ```

2. Make sure you're updating the right character

#### Issue: Info Not Updating

**Symptoms:** Character bio doesn't change

**Solutions:**
1. Use `update_info()` to add:
   ```renpy
   $ amber.update_info("New information here.")
   ```

2. Or replace entirely:
   ```renpy
   $ amber.info = "Completely new bio."
   ```

### Best Practices

#### Use Placeholders for Flexibility

```renpy
# Good - uses placeholder
$ amber.info = "She lives with her [mo_r_low]."

# Bad - hard-coded term
$ amber.info = "She lives with her mom."
```

#### Keep Bios Concise

```renpy
# Good - clear and concise
$ amber.info = "A rebellious streamer who challenges beauty standards."

# Too long - hard to read
$ amber.info = "A very rebellious streaming girl who transformed herself from her mother's beauty expectations into something entirely her own through extensive tattooing and fierce personality development while harboring deep fears of abandonment beneath her aggressive exterior..."
```

#### Update Info Incrementally

```renpy
# Good - add new info as story progresses
$ amber.update_info("She recently became a successful entrepreneur.")

# Later...
$ amber.update_info("She's now engaged.")

# Bad - replace everything each time
$ amber.info = "New bio that replaces everything."
```

#### Validate Data Periodically

```renpy
# During development, check for errors
$ errors = validate_character_data()
if errors:
    "DATA ERRORS:"
    for error in errors:
        "[error]"
```

---

## Summary

The Character Information System provides:

- **Centralized Data**: All character information in one place
- **Dynamic Terms**: Automatic relationship term replacement
- **Easy Access**: Simple syntax to get character data
- **Flexible Updates**: Modify character info as story progresses
- **Helper Functions**: Useful utilities for character management

### Quick Reference

```renpy
# Access character data
$ name = amber.name
$ age = amber.age
$ bio = amber.info  # With term replacement

# Update character data
$ amber.set_age(38)
$ amber.update_info("New information.")
$ amber.set_measurements("b 100 - w 65 - h 107")

# Get full profile
$ profile = amber.get_full_profile()

# Helper functions
$ char = get_character_by_name("Amber")
$ all_lis = get_all_love_interests()
$ ages = get_character_ages()
$ summary = get_character_summary("Nanami")
$ errors = validate_character_data()
```

### Placeholder Reference

Common placeholders for family/relationship terms:
- `[mo_r_low]` - mom/landlady
- `[da_r_low]` - dad/landlord
- `[si_full_r_low]` - sister/close friend
- `[br_full_r_low]` - brother/close friend
- `[fm_r_low]` - family/household
- `[mc_name]` - player's name

---

**End of Documentation**
