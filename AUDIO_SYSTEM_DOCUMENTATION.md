# Audio System Documentation

**Version:** 1.0  
**Language:** English  
**Last Updated:** November 2024

---

## Introduction

The **Audio System** manages all music, ambient sounds, and sound effects in your game. It provides 10 subchannels for each audio type, allowing complex audio layering and smooth transitions.

### What Does It Do?

- **30 Total Channels**: 10 music + 10 ambient + 10 SFX channels
- **Fade Effects**: Smooth audio transitions with customizable fade times
- **Volume Control**: Individual volume for each channel or bulk operations
- **Loop Management**: Automatic looping or one-shot playback
- **Audio Queues**: Play playlists in sequence
- **Conflict Prevention**: Prevents audio overlapping issues

---

## Quick Start

### Play Background Music

```renpy
# Play music on channel 1, looping, with 2-second fade-in
$ playAudio("audio/main_theme.opus", "music", 1, True, 2.0)
```

### Play Ambient Sound

```renpy
# Play ambient city sounds on channel 1, looping
$ playAudio("audio/city_ambient.opus", "amb", 1, True, 1.0)
```

### Play Sound Effect

```renpy
# Play UI click sound on channel 1, no loop
$ playAudio("audio/click.opus", "sfx", 1, False)
```

---

## Channel System

### Channel Types

**Music Channels** (`music1` through `music10`):
- Background music
- Character themes
- Title music
- Combat/action music

**Ambient Channels** (`amb1` through `amb10`):
- Environmental sounds
- Room atmospheres
- Weather effects
- Background noise

**SFX Channels** (`sfx1` through `sfx10`):
- UI sounds
- Dialogue blips
- Action effects
- Short one-shot sounds

### Channel Numbers

Channels are numbered 1-10 for each type:

```renpy
$ playAudio(song, "music", 1)   # music1
$ playAudio(song, "music", 2)   # music2
$ playAudio(song, "music", 10)  # music10

$ playAudio(sound, "amb", 1)    # amb1
$ playAudio(sound, "sfx", 5)    # sfx5
```

---

## Playing Audio

### playAudio() Function

**Syntax:**
```renpy
$ playAudio(file, channel, subchannel, isLoop, fadein, fadeout)
```

**Parameters:**

| Parameter    | Type    | Default | Description                                   |
|--------------|---------|---------|-----------------------------------------------|
| file         | String  | ""      | Path to audio file (required)                 |
| channel      | String  | "music" | Channel type: "music", "amb", or "sfx"        |
| subchannel   | Number  | 1       | Channel number (1-10)                         |
| isLoop       | Boolean | True    | Whether to loop the audio                     |
| fadein       | Float   | None    | Fade-in duration in seconds (None = no fade)  |
| fadeout      | Float   | None    | Fade-out duration for current audio           |

**Returns:** `True` if audio started, `False` if same file already playing

### Basic Examples

```renpy
# Simple music playback
$ playAudio("audio/theme.opus", "music", 1)

# Music with fade-in
$ playAudio("audio/theme.opus", "music", 1, True, 3.0)

# Ambient sound, no loop
$ playAudio("audio/thunder.opus", "amb", 2, False)

# SFX with both fades
$ playAudio("audio/whoosh.opus", "sfx", 1, False, 0.5, 0.5)
```

### Multiple Audio Layers

```renpy
label complex_scene:
    # Background music on music1
    $ playAudio("audio/dramatic.opus", "music", 1, True, 2.0)
    
    # Add string overlay on music2
    $ playAudio("audio/strings.opus", "music", 2, True, 3.0)
    
    # Rain ambience on amb1
    $ playAudio("audio/rain.opus", "amb", 1, True, 2.0)
    
    # Thunder on amb2 (will play once)
    $ playAudio("audio/thunder.opus", "amb", 2, False)
```

---

## Stopping Audio

### stopAudio() Function

**Syntax:**
```renpy
$ stopAudio(channel, subchannel, fadeout)
```

**Parameters:**

| Parameter    | Type          | Default | Description                              |
|--------------|---------------|---------|------------------------------------------|
| channel      | String        | "music" | Channel type: "music", "amb", or "sfx"   |
| subchannel   | Number        | 1       | Channel number (1-10)                    |
| fadeout      | Float/String  | ""      | Fadeout duration ("" = immediate stop)   |

### Examples

```renpy
# Stop immediately
$ stopAudio("music", 1)

# Stop with 2-second fade
$ stopAudio("music", 1, 2.0)

# Stop ambient sound
$ stopAudio("amb", 1, 1.0)
```

### Bulk Stop Functions

**Stop All Subchannels of One Type:**
```renpy
# Stop all music channels with 2s fade
$ stopAllSubchannels("music", 2.0)

# Stop all ambient immediately
$ stopAllSubchannels("amb")
```

**Stop Everything:**
```renpy
# Stop all audio with 3s fade
$ stopAllAudio(3.0)

# Stop all audio immediately
$ stopAllAudio()
```

---

## Volume Control

### setChannelVolume() Function

Set volume for a specific channel:

```renpy
$ setChannelVolume(channel, subchannel, volume, fade_duration)
```

**Parameters:**

| Parameter     | Type   | Description                           |
|---------------|--------|---------------------------------------|
| channel       | String | "music", "amb", or "sfx"              |
| subchannel    | Number | Channel number (1-10)                 |
| volume        | Float  | Volume level (0.0 = silent, 1.0 = max)|
| fade_duration | Float  | Fade time in seconds (0 = instant)    |

**Examples:**

```renpy
# Set music1 to 50% volume instantly
$ setChannelVolume("music", 1, 0.5, 0)

# Fade music1 to 70% over 2 seconds
$ setChannelVolume("music", 1, 0.7, 2.0)

# Mute amb1 over 1 second
$ setChannelVolume("amb", 1, 0.0, 1.0)

# Restore amb1 to full volume
$ setChannelVolume("amb", 1, 1.0, 1.5)
```

### Bulk Volume Functions

**Set All Subchannels of One Type:**
```renpy
# Set all music to 80% with 1s fade
$ setAllSubchannelsVolume("music", 0.8, 1.0)

# Mute all SFX instantly
$ setAllSubchannelsVolume("sfx", 0.0, 0)
```

**Reset All Volumes:**
```renpy
# Reset everything to 100%
$ resetAllVolumes()
```

**Set Master Volume:**
```renpy
# Set all audio to 50% with 2s fade
$ setMasterVolume(0.5, 2.0)
```

---

## Advanced Features

### fadeToAudio() Function

Crossfade from current audio to new audio:

```renpy
$ fadeToAudio(new_file, channel, subchannel, fade_duration, isLoop)
```

**Example:**
```renpy
# Crossfade to new music over 3 seconds
$ fadeToAudio("audio/new_theme.opus", "music", 1, 3.0, True)
```

### playAudioQueue() Function

Play a playlist in sequence:

```renpy
$ playAudioQueue(file_list, channel, subchannel, fadein, fadeout)
```

**Example:**
```renpy
# Create playlist
$ playlist = ["audio/song1.opus", "audio/song2.opus", "audio/song3.opus"]

# Play playlist on music2
$ playAudioQueue(playlist, "music", 2, 1.0, 0.5)
```

**How It Works:**
- First track plays with fade-in
- Subsequent tracks queue automatically
- Each transition uses the fadeout value
- All tracks play once (no loop)

---

## Audio Information

### getPlayingAudio() Function

Check what's currently playing:

```renpy
$ current = getPlayingAudio("music", 1)

if current:
    "Music1 is playing: [current]"
else:
    "Music1 is silent"
```

### isChannelPlaying() Function

Check if audio is playing:

```renpy
$ is_playing = isChannelPlaying("music", 1)

if is_playing:
    "Music is playing"
else:
    "Music is stopped"
```

### getChannelVolume() Function

Get current volume level:

```renpy
$ volume = getChannelVolume("music", 1)

"Current volume: [volume]"  # Shows 0.0 to 1.0
```

---

## Practical Examples

### Example 1: Scene Transition

```renpy
label day_to_night:
    # Fade out day music
    $ stopAudio("music", 1, 2.0)
    
    # Wait for fade
    pause 2.0
    
    # Start night music
    $ playAudio("audio/night_theme.opus", "music", 1, True, 3.0)
    
    # Add night ambience
    $ playAudio("audio/crickets.opus", "amb", 1, True, 2.0)
```

### Example 2: Tension Building

```renpy
label build_tension:
    # Start quiet tension music
    $ playAudio("audio/tension.opus", "music", 1, True, 2.0)
    $ setChannelVolume("music", 1, 0.3, 0)
    
    "Something feels wrong..."
    
    # Increase volume as tension builds
    $ setChannelVolume("music", 1, 0.6, 3.0)
    
    "The air feels thick..."
    
    $ setChannelVolume("music", 1, 1.0, 2.0)
    
    "Suddenly—"
    
    # Climax sound
    $ playAudio("audio/stinger.opus", "sfx", 1, False)
```

### Example 3: Character Theme

```renpy
label amber_appears:
    # Fade current music down
    $ setChannelVolume("music", 1, 0.2, 1.0)
    
    # Play Amber's theme on music2
    $ playAudio("audio/amber_theme.opus", "music", 2, True, 2.0)
    
    show amber happy
    
    amber "Hey there!"
    
    # When she leaves, fade her theme out
    hide amber
    
    $ stopAudio("music", 2, 2.0)
    $ setChannelVolume("music", 1, 1.0, 2.0)
```

### Example 4: Combat Scene

```renpy
label combat_scene:
    # Stop peaceful music
    $ stopAllSubchannels("music", 0.5)
    
    # Combat music with fast fade-in
    $ playAudio("audio/combat.opus", "music", 1, True, 0.5)
    
    # Battle ambience
    $ playAudio("audio/battle_amb.opus", "amb", 1, True, 0.5)
    
    "The fight begins!"
    
    # Hit sound effects on different channels
    $ playAudio("audio/punch.opus", "sfx", 1, False)
    pause 0.5
    $ playAudio("audio/kick.opus", "sfx", 2, False)
    pause 0.5
    $ playAudio("audio/impact.opus", "sfx", 3, False)
```

### Example 5: Dynamic Weather

```renpy
label weather_system:
    # Start light rain
    $ playAudio("audio/rain_light.opus", "amb", 1, True, 3.0)
    
    "It starts to drizzle..."
    
    pause 2.0
    
    # Increase to heavy rain
    $ fadeToAudio("audio/rain_heavy.opus", "amb", 1, 2.0, True)
    
    "The rain intensifies!"
    
    # Add thunder on separate channel
    $ playAudio("audio/thunder.opus", "amb", 2, False)
    
    pause 3.0
    
    # Another thunder
    $ playAudio("audio/thunder.opus", "amb", 2, False)
    
    # Eventually fade to storm ambience
    $ fadeToAudio("audio/storm.opus", "amb", 1, 3.0, True)
```

---

## Channel Assignment Strategy

### Recommended Usage

**Music Channels:**
- `music1`: Main background music
- `music2`: Character themes/overlays
- `music3`: Secondary music layers
- `music4-10`: Reserved for complex scenes

**Ambient Channels:**
- `amb1`: Primary ambient (room tone, weather)
- `amb2`: Secondary ambient (distant sounds)
- `amb3-5`: Environmental effects
- `amb6-10`: Reserved for complex scenes

**SFX Channels:**
- `sfx1`: UI sounds (clicks, hovers)
- `sfx2`: Dialogue sounds
- `sfx3-5`: Action effects
- `sfx6-10`: Reserved for rapid-fire effects

### Layering Example

```renpy
label complex_audio_scene:
    # Layer 1: Base music
    $ playAudio("audio/base.opus", "music", 1, True, 2.0)
    
    # Layer 2: Melody
    $ playAudio("audio/melody.opus", "music", 2, True, 2.0)
    
    # Layer 3: Atmosphere
    $ playAudio("audio/atmosphere.opus", "music", 3, True, 2.0)
    
    # Ambient: Room tone
    $ playAudio("audio/room.opus", "amb", 1, True, 1.0)
    
    # Ambient: Wind outside
    $ playAudio("audio/wind.opus", "amb", 2, True, 1.0)
```

---

## Troubleshooting

### Audio Doesn't Play

**Check:**
1. File path is correct
2. File format is supported (OGG, OPUS, MP3)
3. File exists in audio folder
4. Channel and subchannel are valid (1-10)

```renpy
# Correct
$ playAudio("audio/music.opus", "music", 1)

# Wrong - missing audio/
$ playAudio("music.opus", "music", 1)
```

### Audio Cuts Off Abruptly

**Solution:** Use fadeout when stopping:

```renpy
# Bad - harsh cut
$ stopAudio("music", 1)

# Good - smooth fade
$ stopAudio("music", 1, 2.0)
```

### Can't Hear Audio

**Check:**
1. Volume level:
   ```renpy
   $ volume = getChannelVolume("music", 1)
   "Volume is: [volume]"
   ```

2. Reset if needed:
   ```renpy
   $ setChannelVolume("music", 1, 1.0, 0)
   ```

### Audio Overlaps

**Solution:** Stop old audio before playing new:

```renpy
# Stop current music
$ stopAudio("music", 1, 1.0)

# Wait for fade
pause 1.0

# Play new music
$ playAudio("audio/new.opus", "music", 1, True, 2.0)
```

Or use `fadeToAudio()`:
```renpy
$ fadeToAudio("audio/new.opus", "music", 1, 2.0, True)
```

---

## Summary

The Audio System provides professional audio management with:

- **30 Channels**: 10 music + 10 ambient + 10 SFX
- **Smooth Transitions**: Fade-in/out with customizable durations
- **Flexible Control**: Individual or bulk volume adjustments
- **Advanced Features**: Crossfading, playlists, audio queries
- **Easy to Use**: Simple function calls with clear parameters

### Quick Reference

```renpy
# Play audio
$ playAudio(file, channel, subchannel, isLoop, fadein, fadeout)

# Stop audio
$ stopAudio(channel, subchannel, fadeout)
$ stopAllSubchannels(channel, fadeout)
$ stopAllAudio(fadeout)

# Volume control
$ setChannelVolume(channel, subchannel, volume, fade)
$ setAllSubchannelsVolume(channel, volume, fade)
$ setMasterVolume(volume, fade)
$ resetAllVolumes()

# Advanced
$ fadeToAudio(file, channel, subchannel, fade, isLoop)
$ playAudioQueue(file_list, channel, subchannel, fadein, fadeout)

# Information
$ getPlayingAudio(channel, subchannel)
$ isChannelPlaying(channel, subchannel)
$ getChannelVolume(channel, subchannel)
```

---

**End of Documentation**
