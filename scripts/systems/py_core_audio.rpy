## py_core_audio.rpy
## Core Audio Management System for Ren'Py - Complete English Version
## 
## How to use:
## This script provides a robust system for managing audio in the game, including
## music, ambient sounds, and sound effects across multiple channels and subchannels.
## 
## To play audio:
## $ playAudio(file_name, channel, subchannel, isLoop, fadein, fadeout)
## $ playAudio(antonella_theme, "music", 1, True, 2.0, 1.0)
## 
## The system automatically:
## - Manages 10 subchannels for each main channel type (music, ambient, sfx)
## - Handles smooth audio transitions with fade effects
## - Prevents audio conflicts and overlapping
## - Provides granular volume control per channel/subchannel
## - Supports both looping and non-looping audio playback
##
## Audio Channel System:
## - Music channels (music1-music10): Background music and themes
## - Ambient channels (amb1-amb10): Environmental sounds and atmospheres
## - SFX channels (sfx1-sfx10): Sound effects and one-shot audio
## - Individual volume control for each subchannel
## - Automatic channel registration and management
##
## Advanced Features:
## - Fade-in and fade-out effects for smooth transitions
## - Bulk operations (stop all subchannels, reset all volumes)
## - Volume ramping with configurable fade duration
## - Audio conflict prevention and file change detection
## - Support for different mixer assignments per channel type

################################################################################
## INITIALIZATION
################################################################################

init python:
    ############################################################################
    ## AUDIO CHANNEL CONFIGURATION
    ############################################################################
    
    # Audio channel mapping system - defines subchannels for each main channel type
    channel_map = {
        "music": ["music{}".format(i) for i in range(1, 11)],    # music1 to music10
        "amb": ["amb{}".format(i) for i in range(1, 11)],        # amb1 to amb10
        "sfx": ["sfx{}".format(i) for i in range(1, 11)]         # sfx1 to sfx10
    }
    
    ############################################################################
    ## CORE AUDIO PLAYBACK FUNCTIONS
    ############################################################################
    
    def playAudio(file="", channel="music", subchannel=1, isLoop=True, fadein=None, fadeout=None):
        """
        Generic function to play music or sounds with advanced options
        
        Args:
            file (str): Audio file path/name to play
            channel (str): Main channel type ("music", "amb", "sfx")
            subchannel (int): Subchannel number (1-10)
            isLoop (bool): Whether to loop the audio
            fadein (float): Fade-in duration in seconds (None for no fade)
            fadeout (float): Fade-out duration for currently playing audio
            
        Returns:
            bool: True if audio was started, False if already playing same file
        """
        # Validate channel and subchannel
        if channel not in channel_map or not (1 <= subchannel <= 10):
            return False
        
        # Get the specific channel name
        channel_name = channel_map[channel][subchannel-1]
        
        # Check if the same file is already playing on this channel
        if renpy.music.get_playing(channel=channel_name) != file:
            # Stop current audio with fadeout if specified
            if fadeout is not None:
                renpy.music.stop(channel=channel_name, fadeout=fadeout)
            else:
                renpy.music.stop(channel=channel_name)
            
            # Play new audio if file is specified
            if file != "":
                fadein_duration = fadein if fadein is not None else 0
                fadeout_duration = fadeout if fadeout is not None else 0
                
                renpy.music.play(
                    file, 
                    channel=channel_name, 
                    loop=isLoop, 
                    fadein=fadein_duration,
                    fadeout=fadeout_duration
                )
                return True
        
        return False
    
    ############################################################################
    ## VOLUME CONTROL FUNCTIONS
    ############################################################################
    
    def setChannelVolume(channel, subchannel, volume, fade_duration=0):
        """
        Set the volume of a specified channel and subchannel with fade effect
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            subchannel (int): Subchannel number (1-10)
            volume (float): Volume level (0.0 to 1.0)
            fade_duration (float): Duration of volume fade transition
        """
        if channel in channel_map and 1 <= subchannel <= 10:
            channel_name = channel_map[channel][subchannel-1]
            renpy.music.set_volume(volume, fade_duration, channel=channel_name)

    def setAllSubchannelsVolume(channel, volume, fade_duration=0):
        """
        Set the volume for all subchannels of a main channel
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            volume (float): Volume level (0.0 to 1.0)
            fade_duration (float): Duration of volume fade transition
        """
        if channel in channel_map:
            for subchannel_name in channel_map[channel]:
                renpy.music.set_volume(volume, fade_duration, channel=subchannel_name)
    
    def resetAllVolumes():
        """Reset all channel and subchannel volumes to maximum (1.0)"""
        for channel in channel_map:
            for subchannel in range(1, 11):
                setChannelVolume(channel, subchannel, 1.0)
    
    ############################################################################
    ## AUDIO STOPPING FUNCTIONS
    ############################################################################
    
    def stopAudio(channel="music", subchannel=1, fadeout=""):
        """
        Stop audio on a specified channel and subchannel
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            subchannel (int): Subchannel number (1-10)
            fadeout (float or str): Fadeout duration ("" for no fade)
        """
        if channel in channel_map and 1 <= subchannel <= 10:
            channel_name = channel_map[channel][subchannel-1]
            
            if fadeout == "":
                renpy.music.stop(channel=channel_name)
            else:
                renpy.music.stop(channel=channel_name, fadeout=fadeout)

    def stopAllSubchannels(channel, fadeout=0):
        """
        Stop all audio on all subchannels of a main channel
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            fadeout (float): Fadeout duration for all subchannels
        """
        if channel in channel_map:
            for subchannel in channel_map[channel]:
                renpy.music.stop(channel=subchannel, fadeout=fadeout)
    
    def stopAllAudio(fadeout=0):
        """
        Stop all audio on all channels and subchannels
        
        Args:
            fadeout (float): Fadeout duration for all audio
        """
        for channel in channel_map:
            stopAllSubchannels(channel, fadeout)
    
    ############################################################################
    ## AUDIO QUERY FUNCTIONS
    ############################################################################
    
    def getPlayingAudio(channel, subchannel):
        """
        Get currently playing audio file on a specific channel/subchannel
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            subchannel (int): Subchannel number (1-10)
            
        Returns:
            str or None: Currently playing audio file name or None
        """
        if channel in channel_map and 1 <= subchannel <= 10:
            channel_name = channel_map[channel][subchannel-1]
            return renpy.music.get_playing(channel=channel_name)
        return None
    
    def isChannelPlaying(channel, subchannel):
        """
        Check if audio is currently playing on a channel/subchannel
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            subchannel (int): Subchannel number (1-10)
            
        Returns:
            bool: True if audio is playing, False otherwise
        """
        return getPlayingAudio(channel, subchannel) is not None
    
    def getChannelVolume(channel, subchannel):
        """
        Get current volume of a channel/subchannel
        
        Args:
            channel (str): Main channel type ("music", "amb", "sfx")
            subchannel (int): Subchannel number (1-10)
            
        Returns:
            float: Current volume level (0.0 to 1.0)
        """
        if channel in channel_map and 1 <= subchannel <= 10:
            channel_name = channel_map[channel][subchannel-1]
            return renpy.music.get_volume(channel=channel_name)
        return 0.0
    
    ############################################################################
    ## ADVANCED AUDIO FUNCTIONS
    ############################################################################
    
    def fadeToAudio(new_file, channel="music", subchannel=1, fade_duration=2.0, isLoop=True):
        """
        Fade out current audio and fade in new audio seamlessly
        
        Args:
            new_file (str): New audio file to play
            channel (str): Main channel type
            subchannel (int): Subchannel number
            fade_duration (float): Duration of crossfade
            isLoop (bool): Whether new audio should loop
        """
        # Fade out current, then fade in new
        current_file = getPlayingAudio(channel, subchannel)
        if current_file:
            stopAudio(channel, subchannel, fade_duration)
        
        # Wait for fadeout to complete, then start new audio
        if new_file:
            playAudio(new_file, channel, subchannel, isLoop, fade_duration, 0)
    
    def playAudioQueue(file_list, channel="music", subchannel=1, fadein=0, fadeout=0):
        """
        Play a queue of audio files in sequence
        
        Args:
            file_list (list): List of audio files to play in order
            channel (str): Main channel type
            subchannel (int): Subchannel number
            fadein (float): Fade-in duration for first track
            fadeout (float): Fade-out duration between tracks
        """
        if not file_list:
            return
        
        # Play first track
        playAudio(file_list[0], channel, subchannel, False, fadein, 0)
        
        # Queue remaining tracks
        channel_name = channel_map[channel][subchannel-1]
        for file_name in file_list[1:]:
            renpy.music.queue(file_name, channel=channel_name, loop=False, fadein=0, fadeout=fadeout)
    
    def setMasterVolume(volume, fade_duration=1.0):
        """
        Set master volume for all audio channels
        
        Args:
            volume (float): Master volume level (0.0 to 1.0)
            fade_duration (float): Duration of volume change
        """
        for channel in channel_map:
            setAllSubchannelsVolume(channel, volume, fade_duration)

################################################################################
## CHANNEL REGISTRATION
################################################################################

init -1 python:
    # Register all audio channels with appropriate mixer assignments
    for i in range(1, 11):
        # Music channels - assigned to music mixer, loop by default
        renpy.music.register_channel("music{}".format(i), mixer="music", loop=True)
        
        # Ambient channels - assigned to voice mixer, loop by default
        renpy.music.register_channel("amb{}".format(i), mixer="voice", loop=True)
        
        # SFX channels - assigned to sfx mixer, no loop by default
        renpy.music.register_channel("sfx{}".format(i), mixer="sfx", loop=False)

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this audio management system in your game:
## 
## 1. Playing audio files:
##    $ playAudio(my_music_file, "music", 1, True, 2.0, 1.0)
##    $ playAudio(ambient_sound, "amb", 2, True)
##    $ playAudio(sound_effect, "sfx", 1, False)
##
## 2. The system will automatically:
##    - Manage audio conflicts and prevent overlapping
##    - Handle smooth transitions with fade effects
##    - Register all necessary channels at initialization
##    - Provide granular control over audio playback
##
## 3. Volume control:
##    $ setChannelVolume("music", 1, 0.7, 1.0)  # Set music1 to 70% volume with 1s fade
##    $ setAllSubchannelsVolume("amb", 0.5, 2.0)  # Set all ambient to 50% with 2s fade
##    $ resetAllVolumes()  # Reset all volumes to maximum
##
## 4. Stopping audio:
##    $ stopAudio("music", 1, 1.5)  # Stop music1 with 1.5s fadeout
##    $ stopAllSubchannels("sfx", 0.5)  # Stop all SFX with 0.5s fadeout
##    $ stopAllAudio(2.0)  # Stop everything with 2s fadeout
##
## 5. Advanced features:
##    $ fadeToAudio(new_song, "music", 1, 3.0, True)  # Crossfade to new music
##    $ playAudioQueue([song1, song2, song3], "music", 2)  # Play playlist
##    $ setMasterVolume(0.8, 2.0)  # Set master volume to 80%
##
## 6. Audio information queries:
##    $ current_music = getPlayingAudio("music", 1)
##    $ is_playing = isChannelPlaying("amb", 3)
##    $ volume_level = getChannelVolume("sfx", 2)
##
## Channel organization:
## - Music channels (music1-music10): Character themes, background music, title music
## - Ambient channels (amb1-amb10): Environmental sounds, atmosphere, room tones
## - SFX channels (sfx1-sfx10): UI sounds, dialogue sounds, action effects
##
## Example usage patterns:
## label game_start:
##     # Play main theme on music1
##     $ playAudio(main_theme, "music", 1, True, 3.0)
##     
##     # Add ambient city sounds on amb1
##     $ playAudio(city_ambient, "amb", 1, True, 2.0)
##     
##     # Play UI click sound on sfx1
##     $ playAudio(click_sound, "sfx", 1, False)
##
## label character_scene:
##     # Fade to character theme on music2
##     $ fadeToAudio(character_theme, "music", 2, 2.5, True)
##     
##     # Lower ambient volume during important dialogue
##     $ setChannelVolume("amb", 1, 0.3, 1.0)
##
## Asset organization:
## audio/music/
##   ├── themes/
##   ├── ambient/
##   └── effects/
##
## Performance considerations:
## - The system uses Ren'Py's built-in audio management for efficiency
## - Multiple subchannels allow for complex audio layering without conflicts
## - Fade effects are hardware-accelerated where possible
## - Channel registration happens early to prevent initialization issues
##
## Best practices:
## - Use music channels for longer, looping audio (themes, background music)
## - Use ambient channels for environmental sounds and atmosphere
## - Use SFX channels for short, non-looping sounds (UI, dialogue effects)
## - Always specify fadeout when stopping audio to avoid jarring cuts
## - Test audio levels across different devices and volume settings
##
## Troubleshooting:
## - If audio doesn't play: Check file paths and format compatibility
## - If channels conflict: Ensure you're using different subchannels
## - If fades don't work: Verify fade duration values are reasonable (0.1-5.0 seconds)
## - If volume changes are ignored: Check that channel and subchannel numbers are valid (1-10)
##
## Advanced integration with other systems:
## # Integration with music player system
## $ playAudio(selected_track, "music", 5, True, 1.0, 1.0)
##
## # Integration with scene transitions
## $ stopAllSubchannels("music", 2.0)
## $ playAudio(new_area_theme, "music", 1, True, 3.0, 0)
##
## # Integration with dialogue system
## $ playAudio(character_voice, "sfx", character_sfx_channel, False)