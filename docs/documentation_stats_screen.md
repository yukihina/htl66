# Stats Screen Documentation

**Version:** 1.0  
**Language:** English  
**Last Updated:** November 2024

---

## Introduction

The **Stats Screen** displays comprehensive character information including biographies, physical stats, sexual statistics, relationship status, and character traits. Players can view all love interests and the main character, switch between Bio and Stats tabs, and navigate through character outfits.

### What Does It Do?

- **Character Selection**: Browse all characters from a side menu
- **Two Tab System**: Switch between Biography and Sexual Stats
- **Outfit Preview**: View and cycle through unlocked outfits
- **Relationship Status**: Visual corruption and trust level indicators
- **Character Traits**: Icons showing pregnancy, virginity, and strike status
- **Hover Tooltips**: Detailed information when hovering over icons

---

## Opening the Stats Screen

### From Your Game

```renpy
# Show stats button (recommended - always accessible)
show screen stats_button

# Or open directly from a menu
textbutton "Character Stats" action Show("li_stats")
```

### Stats Button Location

The stats button appears in the top-right corner:
- Position: X=1806, Y=55
- Appears on notifications layer (always visible)
- Shows `gui/stats_off.png` normally
- Shows `gui/stats_on.png` on hover

---

## How to Use

### Step 1: Select a Character

Click any character tab on the left side to view their information:

**Available Characters:**
- Main Character (MC)
- Amber
- Antonella
- Arlette
- Elizabeth
- Isabella
- Kanae
- Madison
- Nanami
- Paz

### Step 2: View Information

**Bio Tab** shows:
- Character name
- Age
- Height and weight
- Body measurements
- Character biography
- Current outfit (with navigation if multiple unlocked)

**Stats Tab** shows (love interests only):
- Sexual experience statistics
- Counts for each activity type
- All stats from the SexStats system

### Step 3: Check Status Icons

Three icons in the top-right show:

**Heart Icon** (Strikes):
- Empty heart: No strikes (relationship possible)
- 1 crack: 1 strike (be careful)
- 2 cracks: 2 strikes (relationship in jeopardy)
- Broken heart: 3 strikes (emotionally locked)

**Pregnancy Icon**:
- Lit: Character is pregnant
- Gray: Not pregnant

**Flower Icon** (Virginity):
- Lit: Character is a virgin
- Gray: Not a virgin

### Step 4: Navigate Outfits

If character has multiple unlocked outfits:
- Click left arrow for previous outfit
- Click right arrow for next outfit
- Current/Total shown between arrows (e.g., "2/5")

### Step 5: View Levels

Bottom-right shows visual indicators:
- **Top Bar**: Corruption level (0-5)
- **Bottom Bar**: Trust/Love level (0-5)

---

## Character Data Displayed

### Love Interest Information

**Bio Tab:**
```
Name:         [Character Name]
Age:          [Age] YEARS OLD
Physical:     [Height] & [Weight]
Measurements: [B-W-H measurements]
Bio:          [Character description]
```

**Stats Tab:**
```
SEXUAL EXPERIENCE

Anal:       [count]
Assjob:     [count]
Blowjob:    [count]
Creampie:   [count]
Pussyjob:   [count]
Sex:        [count]
Titjob:     [count]
```

### Main Character Information

```
Name:       [MC Name]
Age:        [Age] YEARS OLD
Physical:   [Height] & [Weight]
Bio:        [MC description]
Alignment:  [Visual integrity indicator]
```

**Note:** MC doesn't have sexual stats tab or trait icons.

---

## Unknown Characters

Before meeting a character:

**Display:**
- Name shows as "???"
- All information shows as "???"
- No profile picture (shows placeholder)
- Trait icons don't appear
- Levels don't display

**After `rm.set_knows()`:**
- Full information appears
- Profile picture shows
- Trait icons visible
- Levels display

**Example:**
```renpy
# Before meeting
if not rm.get("amber", "knows"):
    "You don't know much about her yet..."

# Meet Amber
label meet_amber:
    $ rm.set_knows("amber", True)
    "You've met Amber!"
    
# Now stats screen shows full info
```

---

## Visual Indicators

### Corruption Levels

Images change based on corruption value:

| Corruption | Level | Image         |
|------------|-------|---------------|
| 0-16       | 0     | gui/cor_0.png |
| 17-32      | 1     | gui/cor_1.png |
| 33-48      | 2     | gui/cor_2.png |
| 49-64      | 3     | gui/cor_3.png |
| 65-80      | 4     | gui/cor_4.png |
| 81-100     | 5     | gui/cor_5.png |

### Trust/Love Levels

Images change based on trust value:

| Trust   | Level | Image          |
|---------|-------|----------------|
| 0-16    | 0     | gui/love_0.png |
| 17-32   | 1     | gui/love_1.png |
| 33-48   | 2     | gui/love_2.png |
| 49-64   | 3     | gui/love_3.png |
| 65-80   | 4     | gui/love_4.png |
| 81-100  | 5     | gui/love_5.png |

### MC Integrity Alignment

Images show moral alignment:

| Integrity | Image                | Alignment         |
|-----------|----------------------|-------------------|
| 0         | gui/stats_mc_0.png   | Fully Corrupted   |
| 1-10      | gui/stats_mc_10.png  | Very Dark         |
| 11-20     | gui/stats_mc_20.png  | Dark              |
| 21-30     | gui/stats_mc_30.png  | Somewhat Dark     |
| 31-40     | gui/stats_mc_40.png  | Slightly Dark     |
| 41-50     | gui/stats_mc_50.png  | Neutral           |
| 51-60     | gui/stats_mc_60.png  | Slightly Good     |
| 61-70     | gui/stats_mc_70.png  | Somewhat Good     |
| 71-80     | gui/stats_mc_80.png  | Good              |
| 81-90     | gui/stats_mc_90.png  | Very Good         |
| 91-100    | gui/stats_mc_100.png | Pure/Heroic       |

---

## Strike System Display

### Heart Icon States

**0 Strikes** (gui/strike_0.png):
- **Icon**: Whole heart
- **Tooltip**: "[Name] has not been emotionally hurt yet. A relationship is still possible."

**1 Strike** (gui/strike_1.png):
- **Icon**: Heart with small crack
- **Tooltip**: "[Name] has been slightly hurt. Be careful with your choices."

**2 Strikes** (gui/strike_2.png):
- **Icon**: Heart with large crack
- **Tooltip**: "[Name]'s heart has been significantly damaged. Your relationship is in jeopardy."

**3 Strikes** (gui/strike_3.png):
- **Icon**: Broken heart
- **Tooltip**: "You've completely broken [Name]'s heart. A romantic path may no longer be possible."

---

## Outfit System

### Navigation

If character has 2+ unlocked outfits:

**Previous Button:**
- Image: `gui/btn_prev_off.png` (idle)
- Image: `gui/btn_prev_on.png` (hover)
- Action: Shows previous unlocked outfit

**Next Button:**
- Image: `gui/btn_next_off.png` (idle)
- Image: `gui/btn_next_on.png` (hover)
- Action: Shows next unlocked outfit

**Counter:**
- Format: "[current]/[total]"
- Example: "3/7" (showing outfit 3 of 7 unlocked)

### How It Works

```renpy
# Character starts with outfit 0 unlocked
$ wm.get_all_unlocked("amber")  # Returns: [0]

# Unlock new outfits during gameplay
$ wm.unlock("amber", 2)
$ wm.unlock("amber", 3)

# Now player can navigate between 0, 2, 3 in stats screen
```

**Navigation Loop:**
- At last outfit, "next" goes to first
- At first outfit, "previous" goes to last
- Cycles through unlocked outfits only

---

## Practical Examples

### Example 1: First Time Opening

```renpy
label tutorial:
    "Let me show you the character stats screen."
    
    # Show the stats button
    show screen stats_button
    
    "Click the icon in the top-right to view character information."
    
    # Player clicks and explores
    
    "You can select different characters from the left menu."
```

### Example 2: Character Discovery

```renpy
label meet_nanami:
    show nanami happy
    
    nanami "Hi! I'm Nanami!"
    
    # Mark as known
    $ rm.set_knows("nanami", True)
    
    "You can now view Nanami's profile in the stats screen."
    
    # Optional: Directly show her profile
    $ set_selected_character("nanami")
    show screen li_stats
    call screen li_stats_secondary(li_name="nanami")
```

### Example 3: Outfit Unlock Reward

```renpy
label amber_gift:
    amber "Thank you for the gift!"
    
    # Increase trust
    $ rm.update("amber", "trust", 10)
    $ check_levels("amber", "trust", 10)
    
    # Unlock special outfit as reward
    $ wm.unlock("amber", 4)
    
    "Amber has unlocked a new outfit!"
    "Check her profile in the stats screen to see it."
```

### Example 4: Strike Warning

```renpy
label bad_decision:
    menu:
        "Apologize":
            "She accepts your apology."
        
        "Say something worse":
            # Add strike
            $ ss.set("nanami", "strike", ss.get("nanami", "strike") + 1)
            
            "Nanami looks hurt."
            
            # Check current strikes
            $ strike_count = ss.get("nanami", "strike")
            
            if strike_count < 3:
                "Check her profile to see the damage..."
            else:
                $ rm.check_emotional_lock("nanami")
                "Nanami has emotionally shut you out."
```

### Example 5: Progression Tracking

```renpy
label check_progress:
    "Let's see how your relationships are progressing."
    
    # Show stats screen
    show screen li_stats
    
    "Check the corruption and love levels at the bottom-right of each character."
    
    "Icons in the top-right show pregnancy, virginity, and emotional status."
```

---

## Required Assets

### GUI Images

**Background and Frames:**
- `gui/popup_bg.png` - Main stats background
- `gui/label_li.png` - Love interest label
- `gui/label_mc.png` - Main character label

**Character Tabs:**
- `gui/tab_mc_off.png`, `gui/tab_mc_on.png`
- `gui/tab_amber_off.png`, `gui/tab_amber_on.png`
- `gui/tab_[character]_off.png`, `gui/tab_[character]_on.png`
  (for all characters)

**Trait Icons:**
- `gui/strike_0.png` through `gui/strike_3.png`
- `gui/preg_on.png`, `gui/preg_off.png`
- `gui/virgin_on.png`, `gui/virgin_off.png`

**Level Indicators:**
- `gui/cor_0.png` through `gui/cor_5.png`
- `gui/love_0.png` through `gui/love_5.png`
- `gui/stats_mc_0.png` through `gui/stats_mc_100.png`

**Navigation Buttons:**
- `gui/btn_prev_off.png`, `gui/btn_prev_on.png`
- `gui/btn_next_off.png`, `gui/btn_next_on.png`
- `gui/btn_close_on.png`, `gui/btn_close_off.png`

**Stats Button:**
- `gui/stats_off.png` - Normal state
- `gui/stats_on.png` - Hover state

**Character Images:**
- Obtained via `get_character_outfit_pic(char_name)`
- Must exist for each character and outfit combination

---

## Troubleshooting

### Stats Screen Won't Open

**Check:**
1. Stats button is shown:
   ```renpy
   show screen stats_button
   ```

2. Required background images exist

3. No conflicting screens with same tag

### Character Shows as "???"

**Cause:** Character hasn't been marked as known

**Solution:**
```renpy
$ rm.set_knows("character_name", True)
```

### Outfit Navigation Missing

**Cause:** Character has only 1 outfit unlocked

**Solution:** Unlock more outfits:
```renpy
$ wm.unlock("amber", 2)
$ wm.unlock("amber", 3)
# Now navigation appears
```

### Wrong Stats Displayed

**Check:**
1. Character data exists in RM and SS systems
2. Functions `rm.get()` and `ss.get()` work correctly
3. Character variable name matches system

### Icons Don't Show Tooltips

**Cause:** Missing hover functions

**Check:**
1. Icon uses proper hover actions:
   ```renpy
   hovered Function(set_icon_hover, description, x, y)
   unhovered Function(clear_icon_hover)
   ```

2. Tooltip frame is properly configured

---

## Summary

The Stats Screen provides:

- **Complete Character Profiles**: Biography, stats, and status
- **Visual Indicators**: Easy-to-read level and trait icons
- **Outfit Preview**: View and navigate character outfits
- **Progress Tracking**: Monitor relationship development
- **Discovery System**: Information unlocks as you meet characters

### Quick Reference

```renpy
# Show stats button
show screen stats_button

# Open stats directly
show screen li_stats

# Mark character as known
$ rm.set_knows("character_name", True)

# Unlock outfits for preview
$ wm.unlock("character", outfit_id)

# Stats auto-update from RM/SS systems
$ rm.update("char", "cor", 10)
$ ss.add("char", "sex")
```

---

**End of Documentation**
