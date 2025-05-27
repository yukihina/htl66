# Documentation for the Ren'Py Core Audio Management Script
# ---------------------------------------------------------

# Purpose:
# This script provides a robust system for managing audio in the game, including
# music, ambient sounds, and sound effects. It offers functions for playing,
# stopping, and controlling the volume of audio across multiple channels.

# Main Components:
# 1. Channel Mapping:
#    - Defines multiple subchannels for music, ambient sounds, and sound effects.
# 2. Audio Playback Function:
#    - playAudio(): Plays audio files with various options.
# 3. Volume Control Function:
#    - setChannelVolume(): Adjusts volume for specific channels and subchannels.
# 4. Audio Stop Functions:
#    - stopAudio(): Stops audio on a specific channel and subchannel.
#    - stopAllSubchannels(): Stops all audio on a main channel.
# 5. Volume Reset Function:
#    - resetAllVolumes(): Resets all channel volumes to default.

# Detailed Usage:
# 1. Playing Audio:
#    $ playAudio(file_name, channel, subchannel, isLoop, fadein, fadeout)
#    Example: $ playAudio(antonella_theme, "music", 1, True, 2.0, 1.0)

# 2. Stopping Audio:
#    $ stopAudio(channel, subchannel, fadeout)
#    Example: $ stopAudio("sfx", 1, 0.5)

# 3. Adjusting Volume:
#    $ setChannelVolume(channel, subchannel, volume, fade_duration)
#    Example: $ setChannelVolume("music", 1, 0.7, 1.0)
#    Example: $ setAllSubchannelsVolume("music", 0.7, 1.0)  # Sets all music subchannels to 0.7 volume with 1s fade

# 4. Stopping All Subchannels:
#    $ stopAllSubchannels(channel, fadeout)
#    Example: $ stopAllSubchannels("amb", 2.0)

# 5. Resetting Volumes:
#    $ resetAllVolumes()

# Connections to Other Files:
# - This script is used in conjunction with music_assets.rpy and sound_assets.rpy,
#   which define the actual audio files used in the game.
# - It's called from various script files throughout the game to manage audio.

# Maintenance and Expansion:
# - When adding new audio types, update the channel_map dictionary.
# - Ensure that any new audio management functions are added here for centralized control.
# - When updating, consider backwards compatibility with existing save games.

# Note for Novices:
# - Audio in Ren'Py is managed through channels (music, sound, voice).
# - This script extends that system with subchannels for more granular control.
# - The 'fadeout' and 'fadein' parameters control how smoothly audio transitions occur.

# Remember: Proper audio management is crucial for creating atmosphere and avoiding
# abrupt changes in sound. Always test audio changes in various scenarios to ensure
# a smooth player experience.

init python:
    # Sound channel name mapping
    channel_map = {
        "music": ["music{}".format(i) for i in range(1, 11)],
        "amb": ["amb{}".format(i) for i in range(1, 11)],
        "sfx": ["sfx{}".format(i) for i in range(1, 11)]
    }

    # Generic function to play music or sounds
    def playAudio(file="", channel="music", subchannel=1, isLoop=True, fadein=None, fadeout=None):
        channel_name = channel_map[channel][subchannel-1]
        if renpy.music.get_playing(channel=channel_name) != file:
            renpy.music.stop(channel=channel_name)
            if file != "":
                renpy.music.play(file, channel=channel_name, loop=isLoop, fadein=fadein if fadein is not None else 0, fadeout=fadeout if fadeout is not None else 0)
                return True
        return False

    # Function to set the volume of a specified channel and subchannel with fade effect
    def setChannelVolume(channel, subchannel, volume, fade_duration=0):
        if channel in channel_map and 1 <= subchannel <= 10:
            channel_name = channel_map[channel][subchannel-1]
            renpy.music.set_volume(volume, fade_duration, channel=channel_name)

    def setAllSubchannelsVolume(channel, volume, fade_duration=0):
        if channel in channel_map:
            for subchannel_name in channel_map[channel]:
                renpy.music.set_volume(volume, fade_duration, channel=subchannel_name)
                
    # Function to stop the sound on a specified channel and subchannel
    def stopAudio(channel="music", subchannel=1, fadeout=""):
        if channel in channel_map:
            channel_name = channel_map[channel][subchannel-1]
            renpy.music.stop(channel=channel_name, fadeout=fadeout)

    # Register all channels
    for i in range(1, 11):
        renpy.music.register_channel("music{}".format(i), mixer="music", loop=True)
        renpy.music.register_channel("amb{}".format(i), mixer="voice", loop=True)
        renpy.music.register_channel("sfx{}".format(i), mixer="sfx", loop=False)

    def stopAllSubchannels(channel, fadeout=0):
        if channel in channel_map:
            for subchannel in channel_map[channel]:
                renpy.music.stop(channel=subchannel, fadeout=fadeout)
    
    # Function to reset all channel and subchannel volumes to 1.0
    def resetAllVolumes():
        for channel in channel_map:
            for subchannel in range(1, 11):
                setChannelVolume(channel, subchannel, 1.0)