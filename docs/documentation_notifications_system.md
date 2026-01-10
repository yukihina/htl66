# Notifications System Documentation

**Version:** 1.0  
**Language:** English  
**Last Updated:** November 2024

---

## Introduction

The **Notifications System** displays popup messages during gameplay to inform players about stat changes, achievements, tips, and important game events. Notifications appear in the bottom-right corner and automatically disappear after 10 seconds.

### Key Features

- **Transition-Immune**: Notifications persist through scene transitions and fades
- **Auto-Display**: Integrates with core systems for automatic notifications
- **Custom Messages**: Support for various notification types
- **Smart Queueing**: Manages multiple notifications elegantly
- **Random Variations**: Message text can randomize for variety

---

## Quick Start

### Show a Basic Notification

```renpy
$ show_custom_notification("start_tip")
```

### Show Corruption Increase

```renpy
$ show_custom_notification("corruption_increase", char="Amber")
```

### Show Trust Level Up

```renpy
$ show_custom_notification("trust_level_up", char="Nanami", level=3)
```

---

## How It Works

### Automatic Integration

The notification system automatically works with:

**Core System Integration:**
- When you use `rm.update()` and `check_levels()`, notifications show automatically
- Corruption/trust changes trigger appropriate notifications
- Level changes show special level-up/down notifications

**Example:**
```renpy
# This automatically triggers a notification
$ rm.update("amber", "cor", 10)
$ check_levels("amber", "cor", 10)
```

### Custom Layer Technology

Notifications use a dedicated layer that sits above everything else:
- **Never affected by transitions**: Fade, dissolve, wipes don't hide notifications
- **Always visible**: Stays on screen during scene changes
- **Independent**: Doesn't interfere with gameplay

---

## Notification Types

### Tips and Information

**start_tip** - Reminds player about Help section:
```renpy
$ show_custom_notification("start_tip")
```

**wt_tip** - Reminds about walkthrough:
```renpy
$ show_custom_notification("wt_tip")
```

**sms_tip** - Photo viewing tip (shows once):
```renpy
$ show_custom_notification("sms_tip")
```

**multicam_tip** - Camera switching reminder:
```renpy
$ show_custom_notification("multicam_tip")
```

**save_tip** - End of update warning:
```renpy
$ show_custom_notification("save_tip")
```

### Corruption Notifications

**corruption_increase** - Small corruption gain:
```renpy
$ show_custom_notification("corruption_increase", char="Amber")
```
Shows random message like:
- "Amber is becoming more flirtatious..."
- "Amber's sexy side is emerging..."
- "Amber is losing her innocence..."

**corruption_level_up** - Gained corruption level:
```renpy
$ show_custom_notification("corruption_level_up", char="Amber", level=3)
```
Shows: "Amber's corruption is now at level 3!"

**corruption_decrease** - Small corruption loss:
```renpy
$ show_custom_notification("corruption_decrease", char="Nanami")
```

**corruption_level_down** - Lost corruption level:
```renpy
$ show_custom_notification("corruption_level_down", char="Nanami", level=2)
```

### Trust/Love Notifications

**trust_increase** - Small trust gain:
```renpy
$ show_custom_notification("trust_increase", char="Isabella")
```
Shows random message like:
- "Isabella's love for you is increasing..."
- "Isabella feels closer to you..."
- "Isabella trusts you more..."

**trust_level_up** - Gained love level:
```renpy
$ show_custom_notification("trust_level_up", char="Isabella", level=4)
```
Shows: "Isabella has reached love level 4!"

**trust_decrease** - Small trust loss:
```renpy
$ show_custom_notification("trust_decrease", char="Madison")
```

**trust_level_down** - Lost love level:
```renpy
$ show_custom_notification("trust_level_down", char="Madison", level=2)
```

### Strike System Notifications

**strike1** - First strike warning:
```renpy
$ show_custom_notification("strike1")
```
Shows: "You've got one strike. Two more, and she'll be out of your life for good."

**strike2** - Second strike warning:
```renpy
$ show_custom_notification("strike2")
```
Shows: "Be Careful! You've got two strikes..."

**strike3** - Final strike:
```renpy
$ show_custom_notification("strike3")
```
Shows: "The End - She's out of your life for good."

**emotional_lock** - Emotional shutdown:
```renpy
$ show_custom_notification("emotional_lock")
```
Shows: "Emotional Shutdown - Trust: 0. Corruption: 0."

### Path Lock System Notifications

**path_lock_love** - Love path locked:
```renpy
$ show_custom_notification("path_lock_love", char="Amber")
```
Shows: "Love Path Locked - Your relationship with Amber is now committed to the love path. Corruption gains blocked. Trust gains doubled."

**path_lock_corruption** - Corruption path locked:
```renpy
$ show_custom_notification("path_lock_corruption", char="Madison")
```
Shows: "Corruption Path Locked - Your relationship with Madison is now committed to the corruption path. Trust gains blocked. Corruption gains doubled."

**How Path Locks Work:**
- Auto-triggered when milestone counters reach threshold (3 by default)
- Happens automatically during `rm.update()` calls
- Path stored permanently in `persistent.{char}_path`
- After lock:
  - Love locked: trust gains x2, corruption blocked
  - Corruption locked: corruption gains x2, trust blocked

**Example Flow:**
```renpy
# Episode 6 - First milestone decision
$ amber_love_choices += 1  # Counter = 1
$ rm.update("amber", "trust", 15)  # No lock yet

# Episode 7 - Second milestone decision
$ amber_love_choices += 1  # Counter = 2
$ rm.update("amber", "trust", 15)  # No lock yet

# Episode 8 - Third milestone decision
$ amber_love_choices += 1  # Counter = 3
$ rm.update("amber", "trust", 10)
# Auto-locks! Shows "path_lock_love" notification
# Actually adds 20 trust (10 x2 doubled)

# After lock - all future updates affected
$ rm.update("amber", "trust", 10)  # Adds 20 (doubled)
$ rm.update("amber", "cor", 5)     # Adds 0 (blocked)
```

---

## Using With Helper Functions

### show_corruption_notification()

Simplified function for corruption notifications:

```renpy
$ show_corruption_notification(character_name, change_type, level)
```

**Examples:**
```renpy
# Small increase
$ show_corruption_notification("Amber", "increase")

# Small decrease
$ show_corruption_notification("Nanami", "decrease")

# Level up
$ show_corruption_notification("Isabella", "level_up", 3)

# Level down
$ show_corruption_notification("Madison", "level_down", 2)
```

### show_trust_notification()

Simplified function for trust notifications:

```renpy
$ show_trust_notification(character_name, change_type, level)
```

**Examples:**
```renpy
# Small increase
$ show_trust_notification("Kanae", "increase")

# Small decrease
$ show_trust_notification("Arlette", "decrease")

# Level up
$ show_trust_notification("Paz", "level_up", 4)

# Level down
$ show_trust_notification("Antonella", "level_down", 3)
```

### show_strike_notification()

Display strike warnings:

```renpy
$ show_strike_notification(strike_count)
```

**Examples:**
```renpy
# First strike
$ show_strike_notification(1)

# Second strike
$ show_strike_notification(2)

# Third strike (game over for that character)
$ show_strike_notification(3)
```

### show_tip_notification()

Show contextual tips:

```renpy
$ show_tip_notification(tip_type)
```

**Examples:**
```renpy
# Photo tip (only shows once)
$ show_tip_notification("sms")

# Mouse wheel tip (only shows once)
$ show_tip_notification("sms2")

# Other tips
$ show_tip_notification("start")
$ show_tip_notification("wt")
$ show_tip_notification("multicam")
$ show_tip_notification("save")
```

---

## Practical Examples

### Example 1: Manual Notification Trigger

```renpy
label special_event:
    "Something important happens!"
    
    # Show custom notification
    $ show_custom_notification("bugfix")
    
    "The game continues..."
```

### Example 2: Strike System Integration

```renpy
label bad_choice_scene:
    menu:
        "Apologize sincerely":
            "She accepts your apology."
        
        "Make it worse":
            # Add a strike
            $ current_strikes = ss.get("amber", "strike")
            $ ss.set("amber", "strike", current_strikes + 1)
            
            # Show strike notification
            $ show_strike_notification(current_strikes + 1)
            
            # Check for emotional lock
            if rm.check_emotional_lock("amber"):
                $ show_custom_notification("emotional_lock")
                "Amber has emotionally shut you out."
```

### Example 3: Corruption Progress

```renpy
label corruption_scene:
    # Increase corruption
    $ rm.update("isabella", "cor", 15)
    $ check_levels("isabella", "cor", 15)
    
    # The above automatically shows a notification!
    # No need to manually call show_corruption_notification()
    
    "Isabella seems different now..."
```

### Example 4: Trust Building

```renpy
label heart_to_heart:
    isabella "Thank you for always being there."
    
    # Increase trust
    $ rm.update("isabella", "trust", 20)
    $ check_levels("isabella", "trust", 20)
    
    # Notification shows automatically
    
    "You've grown closer to Isabella."
```

### Example 5: Important Tips

```renpy
label first_photo:
    "You receive a photo message!"
    
    # Show photo viewing tip (only first time)
    $ show_tip_notification("sms")
    
    # Display photo
    call screen photo_viewer
```

---

## Creating Custom Notifications

### Adding New Notification Templates

Edit `custom_notifications` dictionary in `screen_notifications.rpy`:

```python
custom_notifications = {
    # Existing notifications...
    
    # Add your custom notification
    "my_custom_notif": {
        "title": "Achievement!",
        "message": "You did something amazing!",
        "icon": "info"  # or "corr", "love", "strike"
    }
}
```

Then use it:
```renpy
$ show_custom_notification("my_custom_notif")
```

### Icons

Available icon types:
- `"info"` - Information/tip icon (gui/icon_info.png)
- `"corr"` - Corruption icon (gui/icon_corr.png)
- `"love"` - Love/trust icon (gui/icon_love.png)
- `"strike"` - Strike/warning icon (gui/icon_strike.png)

### Variable Messages

You can use placeholders in messages:

```python
"my_message": {
    "title": "Character Progress",
    "message": "{char} has reached level {level}!",
    "icon": "info"
}
```

Then provide values:
```renpy
$ show_custom_notification("my_message", char="Amber", level=5)
```

### Random Message Variations

Provide a list of messages for variety:

```python
"random_praise": {
    "title": "Nice!",
    "message": [
        "Great choice!",
        "Well done!",
        "Excellent decision!",
        "Perfect!"
    ],
    "icon": "info"
}
```

System picks one randomly each time.

---

## Notification Behavior

### Display Duration

- Notifications show for **10 seconds** by default
- Timer starts when notification appears
- Automatically hides after duration

### Positioning

- Appears in **bottom-right corner**
- Position: X=1380, Y=625
- Icon on left, text on right
- Configured in `notification_state.positioning`

### Maximum Notifications

- Shows up to **2 notifications** simultaneously
- Older notifications are removed when new ones appear
- Prevents screen clutter

### Animations

- **Slide in**: From right side (0.5s)
- **Display**: Stays visible (10s)
- **Slide out**: To right side (0.5s)

---

## Integration with Core System

The notification system works seamlessly with `core.rpy`:

### Automatic Notifications

When using `check_levels()`, the system shows notifications automatically:

```renpy
# This triggers appropriate notification
$ rm.update("amber", "cor", 15)
$ check_levels("amber", "cor", 15)

# If corruption increased but didn't level up:
# Shows: "corruption_increase" notification

# If corruption increased AND leveled up:
# Shows: "corruption_level_up" notification
```

### Custom Integration

You can manually trigger in your own systems:

```renpy
label my_custom_system:
    # Your logic here
    
    if some_condition:
        $ show_custom_notification("my_notif")
```

---

## Troubleshooting

### Notifications Disappear During Transitions

**This should not happen** - notifications are transition-immune.

If it does happen:
1. Check that `config.layers` includes `'notifications'`
2. Verify in `options.rpy`:
   ```renpy
   define config.layers = [..., 'notifications']
   ```

### Notifications Don't Appear

**Check:**
1. Notification ID is correct
2. Notification exists in `custom_notifications`
3. Required images exist (icon, background)

```renpy
# Check if notification exists
if "my_notif" in custom_notifications:
    $ show_custom_notification("my_notif")
else:
    "Notification doesn't exist!"
```

### Too Many Notifications

The system limits to 2 simultaneous notifications. If you need more:

Edit `notification_state.max_notifications` in `screen_notifications.rpy`:
```python
self.max_notifications = 3  # Show up to 3
```

### Wrong Icon Shows

Make sure icon name is correct:

```python
"icon": "info"  # Correct
"icon": "information"  # Wrong - doesn't exist
```

Available: `"info"`, `"corr"`, `"love"`, `"strike"`

---

## Best Practices

### Don't Overuse

```renpy
# Bad - too many notifications
$ show_custom_notification("notif1")
$ show_custom_notification("notif2")
$ show_custom_notification("notif3")
$ show_custom_notification("notif4")

# Good - important moments only
if important_milestone:
    $ show_custom_notification("milestone_reached")
```

### Use Automatic Integration

```renpy
# Good - let the system handle it
$ rm.update("amber", "cor", 10)
$ check_levels("amber", "cor", 10)

# Bad - manual when unnecessary
$ rm.update("amber", "cor", 10)
$ show_corruption_notification("Amber", "increase")
```

### Provide Context

```renpy
# Good - notification with action
"You make a difficult choice."
$ rm.update("amber", "trust", -20)
$ check_levels("amber", "trust", -20)
# Notification explains the consequence

# Bad - notification without context
$ rm.update("amber", "trust", -20)
$ check_levels("amber", "trust", -20)
# Player doesn't know why trust dropped
```

---

## Summary

The Notifications System provides:

- **Automatic Integration**: Works with core relationship system
- **Transition-Proof**: Never disappears during scene changes
- **Variety**: Multiple notification types and random variations
- **Customizable**: Easy to add custom notifications
- **Smart Management**: Handles queueing and timing automatically

### Quick Reference

```renpy
# Manual notifications
$ show_custom_notification("notification_id")
$ show_custom_notification("corruption_increase", char="Name")
$ show_custom_notification("trust_level_up", char="Name", level=3)

# Helper functions
$ show_corruption_notification("Char", "increase")
$ show_corruption_notification("Char", "level_up", 3)
$ show_trust_notification("Char", "decrease")
$ show_trust_notification("Char", "level_down", 2)
$ show_strike_notification(1)
$ show_tip_notification("sms")

# Automatic (when using core system)
$ rm.update("char", "cor", 10)
$ check_levels("char", "cor", 10)  # Auto-shows notification
```

### Required Assets

**GUI Folder:**
- `gui/message_bg.png` - Notification background
- `gui/icon_info.png` - Information icon
- `gui/icon_corr.png` - Corruption icon
- `gui/icon_love.png` - Love/trust icon
- `gui/icon_strike.png` - Strike/warning icon

---

**End of Documentation**
