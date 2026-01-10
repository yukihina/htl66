# Phone System Documentation

**Version:** 1.0
**Language:** English
**Last Updated:** November 2024

---

## Table of Contents

1. [Introduction](#introduction)
2. [System Overview](#system-overview)
3. [Getting Started](#getting-started)
4. [Basic Phone Conversations](#basic-phone-conversations)
5. [Character Configuration](#character-configuration)
6. [Advanced Features](#advanced-features)
7. [Message Types](#message-types)
8. [Sound Effects](#sound-effects)
9. [Practical Examples](#practical-examples)
10. [Customization](#customization)
11. [Troubleshooting](#troubleshooting)

---

## Introduction

The **Phone System** creates realistic text message conversations in your game using a mobile phone interface. Messages appear in colored bubbles with character profile pictures and sound effects, just like a real messaging app.

### What Does It Do?

- **Displays Text Messages**: Shows conversations in phone-style bubbles
- **Character-Specific Design**: Each character has unique colors and profile pictures
- **Sound Effects**: Plays send/receive sounds automatically
- **Animated Messages**: Messages slide in smoothly
- **Scrollable Conversations**: Long conversations can be scrolled through
- **Narrator Support**: Can show scene descriptions between messages

---

## System Overview

The Phone System uses Ren'Py's NVL (Novel) mode to create a messenger-style interface. It's designed to look and feel like a modern messaging app.

### Key Components

1. **NVL Mode**: Special "phone" mode for message display
2. **Character Profiles**: Pictures and colors for each character
3. **Sound System**: Automatic send/receive sound effects
4. **Message Bubbles**: Different frames for sent and received messages
5. **Animations**: Smooth message appearance effects

### Visual Layout

```
┌─────────────────────────┐
│   Phone Background      │
│                         │
│  [Profile]              │
│  Character Name         │
│  ┌─────────────────┐   │
│  │ Their message   │   │
│  └─────────────────┘   │
│                         │
│          ┌─────────────┐│
│          │ Your reply  ││
│          └─────────────┘│
│                         │
└─────────────────────────┘
```

---

## Getting Started

### Required Assets

Before using the phone system, you need these files in your `gui/` folder:

**Background and Frames:**
- `phone_bg.png` - Phone interface background
- `phone_send_frame.png` - Bubble frame for your messages (right side)
- `phone_received_frame.png` - Bubble frame for their messages (left side)
- `phone_received_icon.png` - Default profile icon (fallback)

**Profile Pictures:**
- `profile_pic_mc.png` - Main character profile picture
- `profile_pic_amb.png` - Amber's profile picture
- `profile_pic_nana.png` - Nanami's profile picture
- `profile_pic_eli.png` - Elizabeth's profile picture
- `profile_pic_isa.png` - Isabella's profile picture
- `profile_pic_kan.png` - Kanae's profile picture
- `profile_pic_arl.png` - Arlette's profile picture
- `profile_pic_anto.png` - Antonella's profile picture
- `profile_pic_mad.png` - Madison's profile picture
- `profile_pic_paz.png` - Paz's profile picture

**Sound Effects** (in `audio/` folder):
- `ReceiveText.opus` - Sound when receiving a message
- `SendText.opus` - Sound when sending a message

---

## Basic Phone Conversations

### Starting a Phone Conversation

To start a text message conversation:

```renpy
label phone_scene:
    # Activate phone mode
    $ nvl_mode = "phone"

    # Clear previous messages
    nvl clear

    # Now you can send messages!
    amber "Hey! How are you doing?"
    mc "I'm good! How about you?"

    # Continue the conversation...
```

### Ending a Phone Conversation

When the conversation is done:

```renpy
    # Clear the messages
    nvl clear

    # Return to normal mode (optional)
    $ nvl_mode = "normal"

    # Continue with your story
    "You put your phone away."
```

### Simple Example

```renpy
label amber_text:
    $ nvl_mode = "phone"
    nvl clear

    amber "Are you free tonight?"
    mc "Yeah, what's up?"
    amber "Want to grab dinner?"
    mc "Sounds great!"

    nvl clear
    $ nvl_mode = "normal"

    "You smile and put your phone in your pocket."
```

---

## Character Configuration

### Available Characters

The system comes pre-configured with these characters:

| Character  | Display Name | Color Scheme | Profile Picture         |
|-----------|--------------|--------------|-------------------------|
| MC        | Your name    | Yellow       | profile_pic_mc.png      |
| Amber     | Amber        | Red/Pink     | profile_pic_amb.png     |
| Nanami    | Nanami       | Pink         | profile_pic_nana.png    |
| Elizabeth | Elizabeth    | Purple/Pink  | profile_pic_eli.png     |
| Isabella  | Isabella     | Blue         | profile_pic_isa.png     |
| Kanae     | Kanae        | Cyan         | profile_pic_kan.png     |
| Arlette   | Arlette      | Peach        | profile_pic_arl.png     |
| Antonella | Antonella    | Red          | profile_pic_anto.png    |
| Madison   | Madison      | Coral Red    | profile_pic_mad.png     |
| Paz       | Paz          | Purple       | profile_pic_paz.png     |

### Character Colors

Each character has two colors:

1. **Name Color**: Color of their name at the top of messages
2. **Text Color**: Color of the text bubble background

**Examples:**
- **Amber**: Name is bright red (#FF3333), bubble is light pink (#ff9090)
- **Nanami**: Name is pink (#FFB6C1), bubble is pale pink (#facbd2)
- **Isabella**: Name is blue (#00b7eb), bubble is light blue (#b9f2ff)

### Message Positioning

**Other Characters** (left side):
- Profile picture on the left
- Name shown above first message
- Message bubble to the right of profile

**Main Character** (right side):
- Message bubble on the right
- No profile picture shown by default
- Yellow text color (#FFD119)

---

## Advanced Features

### Using Scene Descriptions

You can add narrator text for context:

```renpy
label phone_drama:
    $ nvl_mode = "phone"
    nvl clear

    "Your phone buzzes with a new message."

    amber "We need to talk."

    "Your heart sinks."

    mc "About what?"
    amber "About us."

    "Three dots appear, then disappear. She's typing..."

    amber "I think we should take a break."

    nvl clear
    $ nvl_mode = "normal"
```

**How It Works:**
- Narrator messages appear centered in italics
- They don't have profile pictures or bubbles
- Great for setting mood and pacing

### Long Conversations

The phone interface automatically scrolls for long conversations:

```renpy
label long_chat:
    $ nvl_mode = "phone"
    nvl clear

    amber "Hey!"
    mc "Hi!"
    amber "What are you up to?"
    mc "Just relaxing. You?"
    amber "Same. Kind of bored though."
    mc "Want to do something?"
    amber "Like what?"
    mc "Movie? Dinner?"
    amber "Both sounds perfect!"
    mc "Great! I'll pick you up at 7?"
    amber "Can't wait! 😊"
    mc "See you then!"

    # Conversation automatically scrolls if it gets too long
    nvl clear
    $ nvl_mode = "normal"
```

### Clearing Messages Mid-Conversation

You can clear messages and continue the conversation:

```renpy
label phone_chapters:
    $ nvl_mode = "phone"
    nvl clear

    # First part of conversation
    amber "Good morning!"
    mc "Morning! Sleep well?"
    amber "Like a baby!"

    nvl clear  # Clear these messages

    # Later in the conversation
    amber "So, about tonight..."
    mc "What about it?"
    amber "Still on for dinner?"
    mc "Absolutely!"

    nvl clear
    $ nvl_mode = "normal"
```

---

## Message Types

### Regular Messages

```renpy
character "Message text here"
```

**Example:**
```renpy
amber "How was your day?"
mc "Pretty good! Got a lot done."
```

### Emoji and Special Characters

```renpy
amber "That's great! 😊"
mc "Thanks! 💪"
```

**Supported:**
- Emoji (😊, 😂, ❤️, etc.)
- Symbols (♥, ★, ✓, etc.)
- Special characters work in messages

### Multiple Messages in a Row

Same character can send multiple messages:

```renpy
amber "Hey"
amber "Are you there?"
amber "Please respond..."
```

**Behavior:**
- First message shows profile picture and name
- Following messages only show the bubble
- Creates natural conversation flow

---

## Sound Effects

### Automatic Sound System

The phone system automatically plays sounds:

- **Received Message**: When other characters send messages
- **Sent Message**: When MC sends messages

### Sound Files

**Required Files:**
- `audio/ReceiveText.opus` - Plays when you receive a message
- `audio/SendText.opus` - Plays when you send a message

### When Sounds Play

```renpy
# This plays ReceiveText.opus
amber "Hello!"

# This plays SendText.opus
mc "Hi there!"

# This plays ReceiveText.opus
nanami "How are you?"

# This plays SendText.opus
mc "I'm good!"
```

### Sound Timing

Sounds play when the message bubble appears on screen, creating a realistic messaging experience.

---

## Practical Examples

### Example 1: Simple Morning Text

```renpy
label morning_text:
    "Your phone vibrates on the nightstand."

    $ nvl_mode = "phone"
    nvl clear

    nanami "Good morning! ☀️"
    mc "Morning! You're up early."
    nanami "Couldn't sleep. Excited for today!"
    mc "Me too! See you at school?"
    nanami "Definitely! 😊"

    nvl clear
    $ nvl_mode = "normal"

    "You get out of bed with a smile."
```

### Example 2: Emergency Text

```renpy
label emergency_text:
    "Your phone buzzes urgently."

    $ nvl_mode = "phone"
    nvl clear

    amber "CALL ME NOW"

    "The message is in all caps. This must be serious."

    mc "What's wrong??"
    amber "Can't explain in text"
    amber "Please just call"
    mc "Calling now"

    nvl clear
    $ nvl_mode = "normal"

    "You quickly dial her number."

    # Continue with voice conversation...
```

### Example 3: Flirty Conversation

```renpy
label flirt_text:
    $ nvl_mode = "phone"
    nvl clear

    isabella "Thinking about you... 💕"

    menu:
        "Be flirty back":
            mc "Can't stop thinking about you either 😘"
            isabella "Really? ☺️"
            mc "Really. Want to come over?"
            isabella "On my way! ❤️"

        "Be casual":
            mc "That's sweet!"
            isabella "Just sweet? 😔"
            mc "Sorry, bad timing. Busy right now."
            isabella "Oh... okay. Text me later?"
            mc "Will do!"

    nvl clear
    $ nvl_mode = "normal"
```

### Example 4: Group Planning

```renpy
label group_planning:
    $ nvl_mode = "phone"
    nvl clear

    "Group chat: Girls Night Out"

    amber "So what time are we meeting?"
    nanami "I can be ready by 7!"
    isabella "7 works for me too"
    mc "7 it is then. Where should we go?"
    amber "How about that new restaurant?"
    nanami "The Italian place?"
    isabella "Ooh yes! I've been wanting to try it!"
    mc "Perfect! I'll make a reservation."
    amber "You're the best! 😘"
    nanami "Can't wait!!"

    nvl clear
    $ nvl_mode = "normal"

    "You open the restaurant's website to make a booking."
```

### Example 5: Late Night Confession

```renpy
label late_confession:
    "Your phone lights up in the dark room. 2:37 AM."

    $ nvl_mode = "phone"
    nvl clear

    arlette "You awake?"

    "You hesitate before replying."

    mc "Yeah. Can't sleep. You okay?"
    arlette "I need to tell you something"
    arlette "I've been thinking about it all night"
    mc "What is it?"

    "Three dots appear. She's typing. They disappear. Then reappear."

    arlette "I think I'm falling for you"

    "Your heart races."

    menu:
        "I feel the same way":
            mc "I've been feeling the same thing"
            mc "Was afraid to say it first"
            arlette "Really?"
            arlette "I'm so relieved"
            arlette "Can I see you tomorrow?"
            mc "Absolutely"
            arlette "Goodnight ❤️"
            mc "Goodnight ❤️"

        "This is complicated":
            mc "Arlette... I care about you"
            mc "But this is complicated"
            arlette "I know"
            arlette "I'm sorry for dumping this on you"
            mc "Don't apologize"
            mc "Let's talk tomorrow. In person."
            arlette "Okay. Goodnight."
            mc "Goodnight."

    nvl clear
    $ nvl_mode = "normal"

    "You stare at the ceiling, unable to sleep now."
```

### Example 6: Building Suspense

```renpy
label suspense_text:
    $ nvl_mode = "phone"
    nvl clear

    "Unknown Number"

    "???" "I know what you did"

    "Your blood runs cold."

    mc "Who is this?"

    "No response. Just those four words staring back at you."

    mc "This isn't funny"
    mc "Who are you?"

    "Still nothing."

    "Seen at 9:47 PM"

    nvl clear
    $ nvl_mode = "normal"

    "Your hands shake as you set down the phone."
```

---

## Customization

### Phone Position

You can change where the phone appears on screen:

```renpy
# In your script, before showing phone conversation
$ phone_position_x = 0.5  # Center horizontally (0.0 = left, 1.0 = right)
$ phone_position_y = 0.5  # Center vertically (0.0 = top, 1.0 = bottom)
```

**Examples:**
```renpy
# Phone on left side
$ phone_position_x = 0.2
$ phone_position_y = 0.5

# Phone on right side
$ phone_position_x = 0.7
$ phone_position_y = 0.5

# Phone at top
$ phone_position_x = 0.5
$ phone_position_y = 0.2
```

### Adding New Characters

To add a new character to the phone system, you need to edit the configuration in `py_ core_phone.rpy`:

1. **Add Profile Picture Mapping:**
```python
character_profiles = {
    # Existing characters...
    "NewCharacter": "gui/profile_pic_newchar.png",
}
```

2. **Add Name Color:**
```python
character_name_colors = {
    # Existing characters...
    "NewCharacter": "#FF00FF",  # Purple
}
```

3. **Add Text Color:**
```python
character_text_colors = {
    # Existing characters...
    "NewCharacter": "#FFCCFF",  # Light purple
}
```

4. **Create the Profile Picture:**
   - Make `gui/profile_pic_newchar.png`
   - Should be a square image
   - Recommended size: 100x100 pixels or larger

### Changing Message Colors

To change a character's colors, edit the dictionaries in `py_ core_phone.rpy`:

```python
# Make Amber's name bright green instead of red
character_name_colors = {
    "Amber": "#00FF00",  # Bright green
}

# Make Amber's text bubble light green
character_text_colors = {
    "Amber": "#CCFFCC",  # Light green
}
```

### Custom Message Frames

You can create custom bubble frames:

1. Create new PNG files:
   - `gui/phone_send_frame.png` - Your messages
   - `gui/phone_received_frame.png` - Their messages

2. Requirements:
   - Must support transparency (PNG format)
   - Should have padding for text
   - Recommended: Use 9-patch style for scaling

---

## Troubleshooting

### Common Issues

#### Issue: Messages Don't Appear

**Symptoms:** Phone screen is blank or messages don't show

**Solutions:**
1. Make sure you activated phone mode:
   ```renpy
   $ nvl_mode = "phone"
   ```

2. Clear NVL history before starting:
   ```renpy
   nvl clear
   ```

3. Check that phone background image exists:
   - File: `gui/phone_bg.png`

#### Issue: No Sound Effects

**Symptoms:** Messages appear but no sounds play

**Solutions:**
1. Check that sound files exist:
   - `audio/ReceiveText.opus`
   - `audio/SendText.opus`

2. Check file format (should be `.opus` or `.ogg`)

3. Make sure audio volume is not muted in preferences

#### Issue: Profile Pictures Don't Show

**Symptoms:** Messages appear but no profile pictures

**Solutions:**
1. Check that profile pictures exist in `gui/` folder

2. Verify character name matches exactly:
   - Correct: `"Amber"`
   - Wrong: `"amber"` or `"AMBER"`

3. Check file path in `character_profiles` dictionary

#### Issue: Wrong Colors

**Symptoms:** Messages have incorrect colors

**Solutions:**
1. Check character name spelling in your script

2. Verify color codes in configuration:
   ```python
   character_name_colors = {
       "Amber": "#FF3333",  # Must be valid hex color
   }
   ```

3. Make sure character is in the color dictionaries

#### Issue: Messages Overlap

**Symptoms:** Messages appear on top of each other

**Solutions:**
1. Check phone background size matches viewport

2. Verify frame images have proper padding

3. Make sure you're using `nvl clear` between conversations

#### Issue: Crashes on Phone Mode

**Symptoms:** Game crashes when entering phone conversation

**Solutions:**
1. Check that NVL mode is properly configured

2. Verify all required images exist

3. Look for errors in the phone system configuration

4. Make sure character is defined before use

### Best Practices

#### Keep Messages Short

```renpy
# Good - short, readable messages
amber "Want to grab coffee?"
mc "Sure! When?"

# Bad - too long for a text message
amber "I was wondering if perhaps you might be interested in getting together for a coffee or perhaps some other beverage at your earliest convenience?"
```

#### Use nvl clear Appropriately

```renpy
# Good - clear between separate conversations
label morning_text:
    $ nvl_mode = "phone"
    nvl clear
    amber "Good morning!"
    mc "Morning!"
    nvl clear

label evening_text:
    $ nvl_mode = "phone"
    nvl clear  # Clear old messages
    amber "How was your day?"
    mc "Great!"
    nvl clear
```

#### Test on Different Screen Sizes

The phone interface should work on various resolutions:
- 1920x1080 (Full HD)
- 1280x720 (HD)
- 1366x768 (Common laptop)

#### Use Narrator for Pacing

```renpy
# Good - creates suspense
amber "I need to tell you something"
"You wait nervously for her to continue."
amber "I'm moving away"

# Less effective
amber "I need to tell you something"
amber "I'm moving away"
```

### Performance Tips

1. **Clear Messages Regularly**: Use `nvl clear` to prevent too many messages from accumulating

2. **Optimize Images**: Compress profile pictures and frames to reduce file size

3. **Limit Simultaneous Sounds**: The system handles this automatically

4. **Use Appropriate Image Formats**:
   - PNG for frames and profile pictures (supports transparency)
   - OPUS or OGG for sound effects

---

## Summary

The Phone System provides a realistic messaging interface that:

- **Looks Professional**: Phone-style bubbles with character colors
- **Sounds Authentic**: Automatic send/receive sound effects
- **Easy to Use**: Simple syntax for conversations
- **Fully Customizable**: Change colors, positions, and characters
- **Integrates Smoothly**: Works with your existing story

### Quick Reference

```renpy
# Start phone conversation
$ nvl_mode = "phone"
nvl clear

# Send messages
character "Message text"
mc "Your response"

# Add narration
"Scene description in italics"

# End conversation
nvl clear
$ nvl_mode = "normal"

# Change position (optional)
$ phone_position_x = 0.5
$ phone_position_y = 0.5
```

### Required Files Checklist

**GUI Folder:**
- [ ] phone_bg.png
- [ ] phone_send_frame.png
- [ ] phone_received_frame.png
- [ ] profile_pic_mc.png
- [ ] profile_pic_[character].png for each character

**Audio Folder:**
- [ ] ReceiveText.opus
- [ ] SendText.opus

---

**End of Documentation**
