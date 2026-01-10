# Achievements System Documentation

**Version:** 1.0  
**Language:** English  
**Last Updated:** November 2024

---

## Introduction

The **Achievements System** tracks player progress through significant story moments and choices. When achievements are unlocked, players receive notifications and can view full-screen achievement artwork with zoom and pan capabilities.

### What Does It Do?

- **Automatic Tracking**: Monitors game progress and unlocks achievements
- **Notifications**: Shows popup when achievement is unlocked
- **Gallery View**: Browse achievements organized by ACTs (episodes)
- **Detailed View**: Click achievements to view full-screen artwork
- **Zoom & Pan**: Explore high-resolution achievement images
- **Persistent Progress**: Achievements save across all playthroughs

---

## Quick Start

### Open Achievements Screen

```renpy
# From extras menu or main menu
textbutton "Achievements" action ShowMenu("achievements")
```

### How It Works

Achievements unlock automatically based on story progress. The system checks achievement conditions on every interaction and shows a notification when unlocked.

**No manual coding required** - achievements unlock as players progress through the story!

---

## Achievement Organization

### ACT System

Achievements are organized by story ACTs:

**ACT 1** (Episodes 1-5):
- Episode 1 achievements
- Episode 2 achievements
- Episode 3 achievements
- Episode 4 achievements
- Episode 5 achievements

**ACT 2** (Episodes 6-10):
- Episode 6 achievements
- Episode 7 achievements
- (Future episodes)

**ACT 3** (Episodes 11-15):
- Reserved for future content

**ACT 4** (Episodes 16-20):
- Reserved for future content

### Grid Display

- Achievements displayed in **3-column grid**
- Scroll through achievements vertically
- Click ACT tabs to switch between acts
- Locked achievements show as darkened thumbnails

---

## Achievement States

### Locked State

**Before Unlocking:**
- Shows darkened thumbnail (`thumb_off.png`)
- Title visible but grayed
- Click does nothing
- No notification

### Unlocked State

**After Unlocking:**
- Shows colored thumbnail (`thumb_on.png`)
- Hovers to highlighted version (`thumb_on_hover.png`)
- Title shown in full color
- Click to view full artwork
- Notification appears once

---

## Viewing Achievements

### Thumbnail View

In the achievements grid:
- **3x3 layout** (3 achievements per row)
- **Thumbnail size**: 345x194 pixels
- **Spacing**: 90 pixels between achievements
- **Scrollable**: Mouse wheel to scroll through list

### Full-Screen View

Click unlocked achievement to view:

**Features:**
- **Full artwork**: 7680x4320 high-resolution image
- **Zoom**: Mouse wheel to zoom in/out (0.25x to 1.0x)
- **Pan**: Click and drag to move image
- **Info Box**: Title and description shown
- **Close Button**: Top-right corner

**Controls:**
- **Mouse Wheel Up**: Zoom in
- **Mouse Wheel Down**: Zoom out
- **Click + Drag**: Pan image
- **Close Button**: Exit to grid

---

## Achievement Data Structure

Each achievement has:

| Property        | Type   | Description                              |
|-----------------|--------|------------------------------------------|
| title           | String | Achievement title                        |
| text            | String | Achievement description                  |
| persistent_var  | String | Variable name for unlock status          |
| notified_var    | String | Variable name for notification status    |
| thumb_on        | String | Path to colored thumbnail                |
| thumb_on_hover  | String | Path to hover thumbnail                  |
| thumb_off       | String | Path to locked thumbnail                 |

### Example Achievement

```python
"ach_ep01_amber": {
    "title": "Forbidden Love",
    "text": "Amber bares her heart, confessing her deep affection for you.",
    "persistent_var": "ep01_ach3",
    "notified_var": "ep01_ach3_notified",
    "thumb_on": "achievements/ach_ep01_amber2_thumb_on.webp",
    "thumb_on_hover": "achievements/ach_ep01_amber2_thumb_onh.webp",
    "thumb_off": "achievements/ach_ep01_amber2_thumb_off.webp"
}
```

---

## Achievement Unlocking

### Automatic System

Achievements unlock automatically based on conditions:

```python
achievement_conditions = [
    {
        "condition": lambda: rm.get("isabella", "knows"),
        "persistent_var": "ep01_ach1",
        "notified_var": "ep01_ach1_notified",
        "achievement_key": "ach_ep01_isabella"
    }
]
```

**How It Works:**
1. System checks condition every interaction
2. If condition is `True` and achievement is locked:
   - Sets `persistent.ep01_ach1 = True`
   - Shows notification (once)
   - Marks notification as shown
3. Achievement now appears unlocked in gallery

### Condition Types

**Simple Variable Check:**
```python
lambda: rm.get("amber", "knows")
# Unlocks when you meet Amber
```

**Story Flag Check:**
```python
lambda: ep01_first
# Unlocks based on story choice
```

**Combined Conditions:**
```python
lambda: ep03_madtalk and ep04_ach_madison
# Unlocks when BOTH conditions are true
```

**Value Comparisons:**
```python
lambda: ep05_guilt_points >= 3
# Unlocks when variable reaches threshold
```

---

## Adding New Achievements

### Step 1: Add Persistent Variables

In `screen_achievements.rpy`, init section:

```renpy
init -1:
    default persistent.my_ach = False
    default persistent.my_ach_notified = False
```

### Step 2: Add Achievement Data

In `achievement_data` dictionary:

```python
achievement_data = {
    # Existing achievements...
    
    "ach_my_achievement": {
        "title": "My Achievement",
        "text": "You accomplished something amazing!",
        "persistent_var": "my_ach",
        "notified_var": "my_ach_notified",
        "thumb_on": "achievements/my_ach_thumb_on.webp",
        "thumb_on_hover": "achievements/my_ach_thumb_onh.webp",
        "thumb_off": "achievements/my_ach_thumb_off.webp"
    }
}
```

### Step 3: Add Unlock Condition

In `achievement_conditions` list:

```python
achievement_conditions.append(
    create_achievement_condition(
        lambda: my_condition_variable,
        "my_ach",
        "my_ach_notified",
        "ach_my_achievement"
    )
)
```

### Step 4: Create Images

Create 4 images in `achievements/` folder:

1. **Full Image**: `ach_my_achievement.avif`
   - Size: 7680x4320 pixels
   - High resolution artwork

2. **Thumbnail (Unlocked)**: `my_ach_thumb_on.webp`
   - Size: 345x194 pixels
   - Colored version

3. **Thumbnail (Hover)**: `my_ach_thumb_onh.webp`
   - Size: 345x194 pixels
   - Highlighted/brightened version

4. **Thumbnail (Locked)**: `my_ach_thumb_off.webp`
   - Size: 345x194 pixels
   - Darkened/grayed version

---

## Practical Examples

### Example 1: Story Milestone

```renpy
# Define flag for achievement
default ep06_romance = False

label romance_scene:
    "You share a tender moment..."
    
    # Set flag
    $ ep06_romance = True
    
    # Achievement unlocks automatically!
    # System checks condition and shows notification
```

### Example 2: Collection Achievement

```renpy
# Track collectibles
default photos_collected = 0

label find_photo:
    "You found a photo!"
    
    $ photos_collected += 1
    
    # Achievement unlocks at 10 photos
    # Condition: lambda: photos_collected >= 10
```

### Example 3: Choice-Based Achievement

```renpy
label critical_choice:
    menu:
        "Take the high road":
            $ heroic_choice = True
            # Unlocks "Hero's Path" achievement
            
        "Take the low road":
            $ dark_choice = True
            # Unlocks "Dark Path" achievement
```

### Example 4: Cumulative Achievement

```renpy
# Track total corruption across all characters
default total_corruption = 0

label update_total_corruption:
    $ total_corruption = 0
    
    for li in get_all_love_interests():
        $ total_corruption += rm.get(li.name.lower(), "cor")
    
    # Achievement unlocks when total >= 500
    # Condition: lambda: total_corruption >= 500
```

---

## Notification System

### When Notification Shows

Notification appears when:
1. Achievement condition becomes `True`
2. Achievement was previously locked
3. Notification hasn't been shown before

### Notification Display

- **Position**: Bottom-right corner
- **Duration**: 12 seconds
- **Content**:
  - Achievement icon
  - Achievement title
  - "You have unlocked a new achievement!"

### Notification Timing

```renpy
# Achievement unlocks during gameplay
label special_scene:
    "Something important happens!"
    
    $ special_flag = True
    
    # Notification appears automatically
    # Shows for 12 seconds
    # Fades in smoothly
    
    "The story continues..."
```

---

## Image Zoom & Pan System

### Zoom Controls

**Mouse Wheel Up**: Zoom in (+5% per scroll)
**Mouse Wheel Down**: Zoom out (-5% per scroll)

**Zoom Range:**
- Minimum: 0.25x (25% - shows full 7680x4320 image at 1920x1080)
- Maximum: 1.0x (100% - full resolution, 1:1 pixels)

### Pan Controls

**Click + Drag**: Move image around
- Drag starts on mouse down
- Image follows mouse movement
- Drag ends on mouse up

**Constraints:**
- Image can't go beyond viewport edges
- If image smaller than viewport, centers automatically
- Smooth dragging with offset tracking

### Usage Tips

1. **Zoom out** (0.25x) to see full artwork
2. **Zoom in** (up to 1.0x) to see details
3. **Drag** to pan around when zoomed in
4. **Scroll** to adjust zoom level smoothly

---

## Troubleshooting

### Achievement Doesn't Unlock

**Check:**
1. Condition variable is set correctly
2. Persistent variable hasn't been accidentally set
3. Condition logic is correct

**Debug:**
```renpy
# Check achievement status
$ ach_unlocked = persistent.my_ach
"Achievement unlocked: [ach_unlocked]"

# Check condition
$ condition_met = my_condition_variable
"Condition met: [condition_met]"
```

### Notification Doesn't Appear

**Causes:**
1. Notification was already shown
2. Persistent notified_var is True

**Reset:**
```renpy
# Reset notification (testing only!)
$ persistent.my_ach_notified = False
```

### Full Image Won't Load

**Check:**
1. Image exists: `achievements/ach_key.avif`
2. Image dimensions: Should be 7680x4320
3. File format: AVIF recommended for size

### Thumbnail Missing

**Check:**
1. Three thumbnails exist (on, hover, off)
2. File paths match achievement_data
3. Images are 345x194 pixels

### Zoom Doesn't Work

**Check:**
1. Image is high resolution (7680x4320)
2. Mouse wheel events are captured
3. Not at zoom limits already

---

## Best Practices

### Achievement Design

**Good Achievement:**
- Clear title
- Descriptive text
- Related to significant moment
- Not too easy or too hard

**Example:**
```python
"title": "First Steps",
"text": "You've taken the first step on your journey with Isabella."
```

**Poor Achievement:**
- Vague title
- No context
- Too common action

### Condition Design

**Good Condition:**
```python
# Specific and meaningful
lambda: ep05_romance and rm.get("amber", "trust") >= 70
```

**Poor Condition:**
```python
# Too easy/meaningless
lambda: True  # Always unlocks
```

### Image Quality

**Recommended:**
- Full image: 7680x4320 AVIF (high quality, small file)
- Thumbnails: 345x194 WEBP (optimized)
- Compress without losing quality

**Avoid:**
- Low resolution images
- Mismatched aspect ratios
- Huge file sizes

---

## Summary

The Achievements System provides:

- **Automatic Unlocking**: Based on story progress
- **Beautiful Presentation**: High-resolution artwork with zoom
- **Player Feedback**: Notifications and gallery
- **Progress Tracking**: Organized by story ACTs
- **Persistent Saving**: Works across all playthroughs

### Quick Reference

```renpy
# Open achievements screen
action ShowMenu("achievements")

# Set achievement flag (unlocks automatically)
$ achievement_flag = True

# Check if unlocked
$ is_unlocked = persistent.achievement_var

# Reset for testing
$ persistent.achievement_var = False
$ persistent.achievement_var_notified = False
```

### Required Assets

**Images:**
- `achievements/[key].avif` - Full 7680x4320 artwork
- `achievements/[key]_thumb_on.webp` - Unlocked thumbnail
- `achievements/[key]_thumb_onh.webp` - Hover thumbnail
- `achievements/[key]_thumb_off.webp` - Locked thumbnail

**GUI:**
- `gui/message_bg.png` - Notification background
- `gui/icon_achiev.png` - Achievement icon
- `gui/rectangle.png` - Grid item background
- `gui/btn_close_off.png`, `gui/btn_close_on.png` - Close button

---

**End of Documentation**
