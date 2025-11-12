## screen_music.rpy
## Music Player System - Enhanced with Duration Display & Progress Bar

################################################################################
## INITIALIZATION
################################################################################

init -1 python:
    # Ensure music player channel is properly registered early
    if not renpy.music.channel_defined("music1"):
        renpy.music.register_channel("music1", mixer="music", loop=True)

# Define the dimensions of the container where the visualizer will be displayed
define VIZ_CONTAINER_WIDTH = 553
define VIZ_CONTAINER_HEIGHT = 439

################################################################################
##  MUSIC ROOM
################################################################################

python early:
    class MusicPlayerProgressValue(BarValue):
        """
        A simplified progress bar value that works with the music player.
        Allows seeking by clicking and shows current position.
        """
        def __init__(self, channel="music1", update_interval=0.1):
            self.channel = channel
            self.update_interval = update_interval
            self.last_pos = 0.0
            self.last_duration = 1.0
            self.zero_count = 0

        def get_adjustment(self):
            pos = renpy.music.get_pos(self.channel)
            duration = renpy.music.get_duration(self.channel)
            
            # Handle None values gracefully
            if pos is None:
                pos = 0.0
                self.zero_count += 1
            else:
                self.last_pos = pos
                self.zero_count = 0
                
            if duration is None or duration == 0:
                duration = self.last_duration
            else:
                self.last_duration = duration
                
            # Use last known position if we're in a brief gap
            if self.zero_count < 10 and pos == 0.0:
                pos = min(self.last_pos, duration)

            return ui.adjustment(
                range=duration,
                value=pos,
                adjustable=True,
                changed=self.seek_to_position
            )

        def seek_to_position(self, value):
            """Seek to a specific position in the track"""
            track = renpy.music.get_playing(self.channel)
            if not track:
                return
                
            # Strip any existing position info
            clean_track = mp_strip_playback(track)
            duration = renpy.music.get_duration(self.channel)
            
            if duration and value is not None:
                # Clamp position to valid range
                position = max(0, min(value, duration))
                
                # Create new track with position
                positioned_track = "<from {} loop 0.0>{}".format(position, clean_track)
                renpy.music.play(positioned_track, channel=self.channel, loop=True, 
                               fadeout=0.1, fadein=0.1)

        def periodic(self, st):
            return self.update_interval

init python:

    def mp_strip_playback(filename):
        """Strip out any existing <> playback information from a filename."""
        if filename and filename.startswith("<"):
            return '>'.join(filename.split(">")[1:])
        else:
            return filename

    # Music player state class (enhanced)
    class MusicPlayerState:
        def __init__(self):
            self.current_character = "common"
            self.current_track_index = 0
            self.is_playing = False
            self.current_volume = 1.0
            self.current_track_file = None
            self.main_menu_music_was_playing = False
            # New attributes for duration display
            self.saved_pos = "--:--"
            self.saved_duration = "--:--"
            self.last_zero = 0

        def pos_dd(self, st, at, style="music_pos_text"):
            """DynamicDisplayable function for current position."""
            x = renpy.music.get_pos(channel="music1")
            if x is None:
                txt = "--:--"
                self.last_zero += 1
            else:
                txt = "{:02}:{:02}".format(int(x/60), int(x%60))
                self.saved_pos = txt
                self.last_zero = 0

            if self.last_zero < 10:  # Grace period
                txt = self.saved_pos
            
            return Text(txt, style=style), 0.2

        def duration_dd(self, st, at, style="music_duration_text"):
            """DynamicDisplayable function for total duration."""
            x = renpy.music.get_duration(channel="music1")
            if not x:
                txt = "--:--"
            else:
                txt = "{:02}:{:02}".format(int(x/60), int(x%60))
                self.saved_duration = txt
            
            if self.last_zero < 10:
                txt = self.saved_duration
                
            return Text(txt, style=style), None

        def get_pos(self, style="music_pos_text"):
            """Get current position as DynamicDisplayable."""
            return DynamicDisplayable(self.pos_dd, style=style)

        def get_duration(self, style="music_duration_text"):
            """Get total duration as DynamicDisplayable."""
            return DynamicDisplayable(self.duration_dd, style=style)

    # Create global instance
    if not hasattr(store, 'music_player_state'):
        music_player_state = MusicPlayerState()

    ############################################################################
    ## DYNAMIC MULTI-BAR MUSIC VISUALIZER
    ############################################################################

    import math

    class DynamicVisualizerState:
        def __init__(self, num_bars=25):
            # Use percentages for scalability, reading the defined values
            self.max_width = int(VIZ_CONTAINER_WIDTH * 0.75)  # Occupies 75% of the container width
            self.max_height = int(VIZ_CONTAINER_HEIGHT * 0.70) # Occupies 70% of the container height

            self.num_bars = num_bars

            # Calculate bar width and spacing to fit perfectly
            total_spacing = (self.num_bars - 1) * 2  # 2px spacing between bars
            self.bar_width = int((self.max_width - total_spacing) / self.num_bars)

            # Initialize bars and their targets
            self.bars = [0.0] * self.num_bars
            self.target_bars = [0.0] * self.num_bars
            self.velocities = [0.0] * self.num_bars
            
            # Individual characteristics for each bar (for variety)
            self.bar_sensitivity = []
            self.bar_max_heights = []
            self.bar_spring_strength = []
            self.bar_friction = []
            self.bar_timers = []  # Individual timers for each bar
            self.bar_hold_time = []  # How long each bar holds its current target
            
            # Initialize individual characteristics for each bar
            for i in range(self.num_bars):
                # Each bar has different sensitivity - more random distribution
                sensitivity = 0.15 + renpy.random.random() * 0.45  # 0.15 to 0.60 - completely random
                self.bar_sensitivity.append(sensitivity)
                
                # Each bar has different maximum height potential - more varied
                height_variation = 0.3 + renpy.random.random() * 0.7  # 0.3 to 1.0
                self.bar_max_heights.append(int(self.max_height * height_variation))
                
                # More varied physics for each bar
                spring_strength = 0.06 + renpy.random.random() * 0.08  # 0.06 to 0.14
                friction = 0.60 + renpy.random.random() * 0.35  # 0.60 to 0.95
                self.bar_spring_strength.append(spring_strength)
                self.bar_friction.append(friction)
                
                # Initialize timers for more natural behavior
                self.bar_timers.append(0.0)
                self.bar_hold_time.append(renpy.random.randint(5, 20))  # Hold target for 5-20 frames

        def update_bars(self):
            """
            Updates the bars. If music is playing, it moves them to random heights.
            If not, it moves them towards zero with smooth fade-out.
            Each bar behaves independently for realistic effect.
            """
            is_playing = music_player_state.is_playing

            for i in range(len(self.bars)):
                # Update individual bar timer
                self.bar_timers[i] += 1
                
                # If music is playing, generate new random heights
                if is_playing:
                    # Only change target when timer exceeds hold time (less predictable)
                    if self.bar_timers[i] >= self.bar_hold_time[i]:
                        # Reset timer and set new hold time
                        self.bar_timers[i] = 0
                        self.bar_hold_time[i] = renpy.random.randint(3, 25)  # Variable hold times
                        
                        # Random chance to change (each bar independent)
                        if renpy.random.random() < self.bar_sensitivity[i]:
                            # More varied height generation
                            if renpy.random.random() < 0.3:  # 30% chance for very low
                                min_height = 1
                                max_height = int(self.bar_max_heights[i] * 0.3)
                            elif renpy.random.random() < 0.6:  # 60% chance for medium
                                min_height = int(self.bar_max_heights[i] * 0.2)
                                max_height = int(self.bar_max_heights[i] * 0.8)
                            else:  # 10% chance for high peaks
                                min_height = int(self.bar_max_heights[i] * 0.6)
                                max_height = self.bar_max_heights[i]
                            
                            if max_height > min_height:
                                self.target_bars[i] = renpy.random.randint(min_height, max_height)
                            else:
                                self.target_bars[i] = min_height
                else:
                    # When music stops, all bars smoothly move toward zero
                    self.target_bars[i] = 0
                    # Reset timers for next time music plays
                    self.bar_timers[i] = 0

                # Smooth physics with individual characteristics
                diff = self.target_bars[i] - self.bars[i]
                
                # Enhanced physics for smoother movement
                if is_playing:
                    # When playing, use normal spring physics
                    self.velocities[i] += diff * self.bar_spring_strength[i]
                    self.velocities[i] *= self.bar_friction[i]
                else:
                    # When stopping, apply stronger downward force for smooth fade
                    if self.bars[i] > 0:
                        downward_force = -self.bars[i] * 0.08  # Gentle downward pull
                        self.velocities[i] += downward_force
                        self.velocities[i] *= 0.85  # Higher friction when stopping
                    else:
                        self.velocities[i] = 0
                
                self.bars[i] += self.velocities[i]

                # Ensure bars don't go below zero
                if self.bars[i] < 0:
                    self.bars[i] = 0
                    self.velocities[i] = 0

        def reset_visualizer(self):
            """
            Function to force a visualizer reset with smooth fade-out.
            Used when changing tracks for a cleaner effect.
            """
            for i in range(len(self.bars)):
                self.target_bars[i] = 0
                # Reset timers for new track
                self.bar_timers[i] = 0
                self.bar_hold_time[i] = renpy.random.randint(5, 20)

    # Initialize the state of the new visualizer
    if not hasattr(store, 'dynamic_viz_state'):
        dynamic_viz_state = DynamicVisualizerState(num_bars=25)

    ############################################################################
    ## MAIN MENU MUSIC HANDLING
    ############################################################################

    def mp_debug_music():
        """Debug function to check what's playing"""
        debug_info = []

        # Check main music channel
        current = renpy.music.get_playing(channel="music")
        if current:
            debug_info.append("Music channel: " + str(current))
        else:
            debug_info.append("Music channel: Nothing")

        # Check music1 channel
        current1 = renpy.music.get_playing(channel="music1")
        if current1:
            debug_info.append("Music1 channel: " + str(current1))
        else:
            debug_info.append("Music1: Nothing")

        # Check all music subchannels
        for i in range(1, 11):
            channel_name = "music{}".format(i)
            try:
                current_sub = renpy.music.get_playing(channel=channel_name)
                if current_sub:
                    debug_info.append(channel_name + ": " + str(current_sub))
            except:
                pass

        # Show all info at once
        renpy.notify("\n".join(debug_info))

    def mp_force_stop_all_music():
        """Force stop all music on all channels"""
        # Stop main music channel
        renpy.music.stop(channel="music", fadeout=0.5)
        # IMPORTANT: Always stop music1 (music player channel)
        renpy.music.stop(channel="music1", fadeout=0)

        # Stop all music subchannels (based on py_core_audio.rpy system)
        for i in range(1, 11):
            try:
                renpy.music.stop(channel="music{}".format(i), fadeout=0.5)
            except:
                pass

        # Use the game's stopAllSubchannels function if available
        if 'stopAllSubchannels' in globals():
            stopAllSubchannels("music", fadeout=0.5)

        # Reset music player state
        music_player_state.is_playing = False
        music_player_state.current_track_file = None

    def mp_cleanup_on_exit():
        """Clean up music player when exiting"""
        # Stop music player music
        mp_stop_music()
        renpy.music.stop(channel="music1", fadeout=0.5)

        # Resume main menu music
        mp_resume_main_menu_music()

    def mp_pause_main_menu_music():
        """Pause main menu music when entering music player"""
        # Check all possible music channels
        music_found = False

        # Check main music channel
        current_music = renpy.music.get_playing(channel="music")
        if current_music:
            music_player_state.main_menu_music_was_playing = True
            music_player_state.stored_music = current_music
            music_player_state.stored_channel = "music"
            music_found = True

        # Also check music subchannels if using custom audio system
        if not music_found:
            for i in range(1, 11):
                channel_name = "music{}".format(i)
                try:
                    current = renpy.music.get_playing(channel=channel_name)
                    if current:
                        music_player_state.main_menu_music_was_playing = True
                        music_player_state.stored_music = current
                        music_player_state.stored_channel = channel_name
                        music_found = True
                        break
                except:
                    pass

        return music_found

    def mp_resume_main_menu_music():
        """Resume main menu music when leaving music player"""
        # FIRST: Stop any music player tracks
        mp_stop_music()
        renpy.music.stop(channel="music1", fadeout=0.5)

        # Only resume main menu music if it was playing before
        if music_player_state.main_menu_music_was_playing:
            # If we're in any menu context (not in-game)
            if main_menu or renpy.context().main_menu:
                # Determine which channel to use
                channel_to_use = getattr(music_player_state, 'stored_channel', 'music')

                # Check if nothing is playing on the target channel
                if not renpy.music.get_playing(channel=channel_to_use):
                    # Try to resume the stored music or the default main menu music
                    music_to_play = getattr(music_player_state, 'stored_music', None)
                    if not music_to_play and hasattr(store, 'config') and hasattr(config, 'main_menu_music'):
                        music_to_play = config.main_menu_music

                    if music_to_play:
                        # If using custom audio system, use playAudio
                        if 'playAudio' in globals() and channel_to_use.startswith('music') and channel_to_use != 'music':
                            try:
                                subchannel = int(channel_to_use.replace('music', ''))
                                playAudio(music_to_play, "music", subchannel, True, 1.0, 0)
                            except:
                                renpy.music.play(music_to_play, channel=channel_to_use, loop=True, fadein=1.0)
                        else:
                            renpy.music.play(music_to_play, channel=channel_to_use, loop=True, fadein=1.0)
        else:
            # Even if music wasn't playing before, if we're in main menu, start the default music
            if main_menu and hasattr(store, 'config') and hasattr(config, 'main_menu_music'):
                if not renpy.music.get_playing(channel="music"):
                    renpy.music.play(config.main_menu_music, channel="music", loop=True, fadein=1.0)

        # Reset the flags
        music_player_state.main_menu_music_was_playing = False
        music_player_state.is_playing = False
        music_player_state.current_track_file = None
        if hasattr(music_player_state, 'stored_music'):
            delattr(music_player_state, 'stored_music')
        if hasattr(music_player_state, 'stored_channel'):
            delattr(music_player_state, 'stored_channel')

    ############################################################################
    ## MUSIC PLAYER CONTROL FUNCTIONS
    ############################################################################

    def mp_play_track(track_file):
        """Play a track on the music player channel"""
        if track_file:
            # Stop any currently playing music on music1 channel
            renpy.music.stop(channel="music1", fadeout=0.5)
            # Queue the new track to play after the fadeout
            renpy.music.queue(track_file, channel="music1", loop=True, fadein=2.0)
            music_player_state.current_track_file = track_file
            music_player_state.is_playing = True

    def mp_stop_music():
        """Stop the current music on music player channel only"""
        # Stop music1 channel (music player channel)
        renpy.music.stop(channel="music1", fadeout=0.5)
        # Update state
        music_player_state.is_playing = False
        music_player_state.current_track_file = None

    def mp_set_volume(volume):
        """Set the volume for the music player channel"""
        renpy.music.set_volume(volume, delay=0.5, channel="music1")
        music_player_state.current_volume = volume

    def mp_change_character(char_name):
        """Change the selected character and reset track index"""
        music_player_state.current_character = char_name
        music_player_state.current_track_index = 0
        mp_stop_music()

    def mp_change_track(index):
        """Change to a specific track index"""
        tracks = get_character_tracks(music_player_state.current_character)
        if tracks and 0 <= index < len(tracks):
            music_player_state.current_track_index = index
            track_name, track_file = tracks[index]
            mp_play_track(track_file)

    def mp_prev_track():
        """Go to previous track"""
        if music_player_state.current_track_index > 0:
            music_player_state.current_track_index -= 1
        mp_stop_music()

    def mp_next_track():
        """Go to next track"""
        tracks = get_character_tracks(music_player_state.current_character)
        if tracks and music_player_state.current_track_index < len(tracks) - 1:
            music_player_state.current_track_index += 1
        mp_stop_music()

    def mp_toggle_play():
        """Toggle play/pause"""
        tracks = get_character_tracks(music_player_state.current_character)
        if tracks and music_player_state.current_track_index < len(tracks):
            if music_player_state.is_playing:
                mp_stop_music()
            else:
                track_name, track_file = tracks[music_player_state.current_track_index]
                mp_play_track(track_file)

    ############################################################################
    ## TRACK LISTS
    ############################################################################

    def get_character_tracks(character_name):
        """Get track lists for each character. Uses variables, not strings."""
        tracks = {
            "amber": [
                ("A Day Without You", amber_2nd_theme),
                ("Fading Lullaby", amber_sad_theme),
                ("Fuel the Fire", amber_anger_theme),
                ("Frost & Ashes", amber_theme),
                ("Shadow Waltz", amber_sexy_theme2),
                ("Sin & Silence", amber_sexy_theme),
                ("The Last Embrace", mc_amber_x_theme),
                #("Veil of Joy", amber_happy_theme)
            ],
            "nanami": [
                ("儚い願い (Hakanai Negai)", nanami_innocence_theme),
                ("ちょっと待って! (Chotto Matte!)", nanami_clumsy_theme),
                ("秘密の恋 (Himitsu no Koi)", nanami_love_theme),
                ("ふわり夢 (Fuwari Yume)", nanami_chill_theme),
                ("夢の中で (Yume no Naka de)", nanami_secure_theme),
                ("光の歌 (Hikari no Uta)", nanami_theme),
                ("静かな心 (Shizuka na Kokoro)", mc_nanami_theme),
            ],
            "elizabeth": [
                ("Distorted Memory", elizabeth_anger_theme),
                ("Echoes of You", mc_elizabeth_theme),
                ("Falling in Slow Motion", elizabeth_sexy_theme),
                ("Glimmer Between Us", elizabeth_play_theme),
                ("Paper Skyline", elizabeth_theme),
                ("レコードに落ちる涙 (Rekōdo ni Ochiru Namida)", elizabeth_singing_song),
                ("Smoke & Silk", elizabeth_sexy_theme2),
                ("Unfinished Goodbyes", elizabeth_sad_theme)
            ],
            "isabella": [
                ("Adagio for Lost Time", isabella_sad),
                ("Between the Lines", isabella_sexy),
                ("Midnight Serenade", isabella_theme),
                ("Resonance of Resistance", isabella_serious),
                ("Rupture of Silence", isabella_anger_theme),
                ("Skipping Notes", isabella_happy)
            ],
            "kanae": [
                # ("Kanae's Theme", kanae_theme),
                # ("Kanae's Love", kanae_love)
            ],
            "arlette": [
                ("À fleur de peau", arlette_sexy_theme),
                ("Dans l'ombre du passé", arlette_nostalgia_theme),
                ("L'écho d'un adieu", arlette_theme),
                ("Le temps suspendu", arlette_sad_theme),
                ("Un dernier espoir", arlette_love_theme)
            ],
            "antonella": [
                ("A Game of Skin", antonella_sexy_theme),
                ("A Little Bit of Hope", antonella_past_theme),
                ("Any Questions", antonella_game_theme),
                ("Kitsune's Theme - Red", redkitsune_theme),
                ("Race of Hearts", antonella_past_happy_theme),
                ("Sakura in Spring", antonella_theme),
                ("Sakura Memories", antonella_love),
                ("She Waits in the Fog", antonella_mistery_theme),
                ("Unborn Sakura", antonella_sad_theme),
                ("桜散る夜 (Sakura Chiru Yoru)", antonella_singing_act1)
            ],
            "madison": [
                ("Glassfang", madison_bad_theme),
                ("Queen of the Hollow", madison_dom_theme),
                ("Residue of Me", madison_sad_theme),
                ("Sugartrap", madison_theme),
                ("Through Her Eyes, I Vanish", madison_nan_theme),
                ("Undress the Night", madison_sexy_theme)
            ],
            "paz": [
                ("Ember Glow", paz_theme),
                #("Golden Tide", paz_happy_theme)
            ],
            "common": [
                ("Diamond Pulse", photos_theme),
                ("Éclats d'aurore", heaven_theme),
                ("Fractured Identity", chaos_theme),
                ("No Signal", dotonbori_theme),
                ("The Serpent's Elegy", mic_theme),
                ("Valse pour l'Enfer", hell_theme),
                ("闇の刻 (Yami no Koku)", title_theme),
                #("怒れる地響き (Ikareru Jihibiki)", mc_action_theme2),
                ("戻らぬ時 (Modoranu Toki)", mc_theme),
                ("帰らぬ昨日 (Kaeranu Kinō)", mc_broken_theme),
                ("終わらない連鎖 (Owaranai Rensa)", mc_suspense_theme),
                ("影の儀式 (Kage no Gishiki)", yakuza_theme),
                ("鬼灯の影 (Hōzuki no Kage)", tobita_theme),
                ("狂乱の刻 (Kyōran no Koku)", mc_action_theme),
                ("夢と分析 (Yume to Bunseki)", mc_thinking_theme)
            ]
        }
        return tracks.get(character_name, [])

################################################################################
## DYNAMIC MULTI-BAR VISUALIZER SCREEN
################################################################################

screen dynamic_music_visualizer():
    # The visualizer state updates continuously so the fade-out animation works
    # even after the is_playing state has changed.
    if music_player_state.is_playing or max(dynamic_viz_state.bars) > 1.0:
        timer 0.04 action Function(dynamic_viz_state.update_bars) repeat True

    hbox:
        # Use the calculated values from the class for size and spacing
        xsize dynamic_viz_state.max_width
        spacing 2  # Reduced spacing to match the calculation
        xalign 0.5
        yalign 1.0  # Align bars to the bottom of the container

        for i in range(dynamic_viz_state.num_bars):
            $ height = max(1, int(dynamic_viz_state.bars[i]))  # Ensure minimum height of 1

            # More dynamic color assignment with less predictable patterns
            $ bar_position_factor = i / float(dynamic_viz_state.num_bars - 1)  # 0.0 to 1.0
            $ height_factor = height / float(dynamic_viz_state.max_height)  # 0.0 to 1.0
            $ velocity_factor = abs(dynamic_viz_state.velocities[i]) / 10.0  # Factor in movement speed
            
            # Create more varied color selection with random elements
            $ color_seed = (i * 7 + int(height * 0.5)) % 12  # More varied base for color selection
            
            if height_factor > 0.85:  # Very high peaks
                $ color_choices = ["#ff4757", "#ff3838", "#ff6348", "#e74c3c"]
                $ bar_color = color_choices[color_seed % len(color_choices)]
            elif height_factor > 0.65:  # High peaks  
                $ color_choices = ["#ffa502", "#ff9500", "#f39c12", "#e67e22"]
                $ bar_color = color_choices[color_seed % len(color_choices)]
            elif height_factor > 0.45:  # Medium-high
                $ color_choices = ["#1dd1a1", "#00d2d3", "#00cec9", "#17a2b8"]
                $ bar_color = color_choices[color_seed % len(color_choices)]
            elif height_factor > 0.25:  # Medium
                $ color_choices = ["#5f27cd", "#00a8ff", "#3742fa", "#2f3542"]
                $ bar_color = color_choices[color_seed % len(color_choices)]
            else:  # Low
                $ color_choices = ["#27dc95", "#2ed573", "#6c5ce7", "#a29bfe"]
                $ bar_color = color_choices[color_seed % len(color_choices)]
            
            # Add velocity-based brightness variation
            if velocity_factor > 0.5:
                $ bar_color = bar_color  # Keep original color for fast-moving bars
            elif height < 5:
                $ bar_color = "#2d3436"  # Dark color for very low bars

            # Create each individual bar
            frame:
                background Solid(bar_color)
                xsize dynamic_viz_state.bar_width
                ysize height
                yalign 1.0  # Makes each bar grow from the bottom up
                padding (0, 0, 0, 0)
                
                # Dynamic alpha based on height and velocity for more life
                $ alpha_value = 0.7 + (height_factor * 0.3)  # 0.7 to 1.0 alpha
                if velocity_factor > 0.3:
                    $ alpha_value = min(1.0, alpha_value + 0.2)  # Boost alpha for moving bars
                
                at transform:
                    alpha alpha_value

################################################################################
## MUSIC PLAYER SCREEN
################################################################################

screen music_player():
    tag menu
    modal True

    default dropdown_open = False

    ## Force stop ALL music on the main music channel when entering
    on "show" action [
        Function(mp_pause_main_menu_music),
        Function(mp_force_stop_all_music)
    ]

    ## Stop music player and resume main menu music when leaving
    on "hide" action Function(mp_cleanup_on_exit)
    on "replaced" action Function(mp_cleanup_on_exit)

    use game_menu(_("Music Player"), scroll="viewport"):
        style_prefix "music"

    if main_menu:
        add "gui/mmtitle_extras_mp.png" ypos 151 xpos 1230 at igm_appear_fg

    ## Get current state
    $ current_character = music_player_state.current_character
    $ current_track_index = music_player_state.current_track_index
    $ is_playing = music_player_state.is_playing
    $ current_volume = music_player_state.current_volume

    ## Get tracks for selected character
    $ character_tracks = get_character_tracks(current_character)

    ## Get current track info
    if character_tracks and current_track_index < len(character_tracks):
        $ track_name, track_file = character_tracks[current_track_index]
    else:
        $ track_name = "No tracks available"
        $ track_file = None

    ## Character selection dropdown button
    frame at igm_appear_fg:
        xpos 1100
        ypos 270
        xsize 583
        ysize 40
        background None

        textbutton "SELECT CHARACTER":
            xsize 583
            ysize 40
            background "gui/music_dropdown_idle.png"
            hover_background "gui/music_dropdown_hover.png"
            action SetScreenVariable("dropdown_open", not dropdown_open)
            style "centered_dropdown_button"

    ## Main content area
    hbox:
        xpos 331
        ypos 270
        spacing 50

        ## Left side - Player and track list
        vbox:
            spacing 30

            ## Music player controls
            frame at igm_appear_fg:
                background "gui/music_player_bg.png"
                xsize 600
                ysize 150  # Back to original size

                vbox:
                    spacing 5  # Reduced from 8 to 5 for tighter spacing
                    xalign 0.5
                    yalign 0.5

                    ## Current track name
                    text track_name style "music_current_track" xalign 0.5

                    ## NEW: Duration display (pos / duration) - closer to title
                    hbox:
                        spacing 8
                        xalign 0.5
                        add music_player_state.get_pos(style="music_pos_text")
                        text " / " style "music_duration_separator"
                        add music_player_state.get_duration(style="music_duration_text")

                    ## Control buttons (reduced size to 0.4)
                    hbox:
                        spacing 20  # Reduced spacing more
                        xalign 0.5

                        ## Previous button
                        imagebutton:
                            idle "gui/music_prev_off.png"
                            hover "gui/music_prev_on.png"
                            sensitive len(character_tracks) > 0
                            action [Function(dynamic_viz_state.reset_visualizer), Function(mp_prev_track)]
                            style "igm_button"
                            at Transform(zoom=0.5)

                        ## Play/Pause button
                        if is_playing:
                            imagebutton:
                                idle "gui/music_pause_off.png"
                                hover "gui/music_pause_on.png"
                                sensitive track_file is not None
                                action Function(mp_stop_music)
                                style "igm_button"
                                at Transform(zoom=0.5)
                        else:
                            imagebutton:
                                idle "gui/music_play_off.png"
                                hover "gui/music_play_on.png"
                                sensitive track_file is not None
                                action [Function(dynamic_viz_state.reset_visualizer), Function(mp_toggle_play)]
                                style "igm_button"
                                at Transform(zoom=0.5)

                        ## Stop button
                        imagebutton:
                            idle "gui/music_stop_off.png"
                            hover "gui/music_stop_on.png"
                            sensitive is_playing
                            action Function(mp_stop_music)
                            style "igm_button"
                            at Transform(zoom=0.5)

                        ## Next button
                        imagebutton:
                            idle "gui/music_next_off.png"
                            hover "gui/music_next_on.png"
                            sensitive len(character_tracks) > 0
                            action [Function(dynamic_viz_state.reset_visualizer), Function(mp_next_track)]
                            style "igm_button"
                            at Transform(zoom=0.5)

                    ## NEW: Progress bar (without label)
                    bar:
                        value MusicPlayerProgressValue("music1")
                        xsize 500
                        xalign 0.5
                        style "music_progress_bar"

                    ## Volume control
                    hbox:
                        spacing 10
                        xalign 0.5

                        text "Volume:" style "music_volume_text"
                        bar:
                            value FieldValue(music_player_state, "current_volume", 1.0, max_is_zero=False, style="bar", offset=0, step=.05)
                            changed mp_set_volume
                            xsize 300
                            style "music_volume_bar"

            ## Track list (back to original size)
            frame at igm_appear_fg:
                background None
                xsize 600
                ysize 320  # Back to original size

                if character_tracks:
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 5

                            for i, (track_name, track_file) in enumerate(character_tracks):
                                button:
                                    xsize 580
                                    ysize 40

                                    if i == current_track_index:
                                        background "gui/music_track_selected.png"
                                    else:
                                        background "gui/music_track_idle.png"
                                        hover_background "gui/music_track_hover.png"

                                    text track_name style "music_track_text"

                                    action [Function(dynamic_viz_state.reset_visualizer), Function(mp_change_track, i)]
                else:
                    text "No tracks available for this character" style "music_no_tracks_text" xalign 0.5 yalign 0.5

        ## Right side - Character background with visualizer overlay
        frame at igm_appear_fg:
            background None
            xsize 553
            ysize 439
            yalign 1.0

            ## Background image
            add "gui/music_common_bg.png" xalign 0.5 yalign 1.0

            ## Visualizer overlay
            if dynamic_viz_state:
                # This container ensures the visualizer is positioned correctly inside the frame
                frame:
                    xalign 0.5
                    yalign 0.95 # Position the visualizer near the bottom edge
                    xsize VIZ_CONTAINER_WIDTH
                    ysize VIZ_CONTAINER_HEIGHT
                    background None
                    padding (0, 0, 0, 0)

                    use dynamic_music_visualizer

    ## Dropdown menu
    if dropdown_open:
        ## Invisible button to close dropdown when clicking outside
        button:
            xfill True
            yfill True
            action SetScreenVariable("dropdown_open", False)

        frame at igm_appear_fg:
            xpos 1100
            ypos 320
            xsize 352
            ysize 400
            background None

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 2

                    for char_name in ["common", "amber", "nanami", "elizabeth", "isabella", "kanae", "arlette", "antonella", "madison", "paz"]:
                        button:
                            xsize 352
                            ysize 40

                            if char_name == current_character:
                                background "gui/music_dropdown_selected.png"
                            else:
                                background "gui/music_dropdown_idle.png"
                                hover_background "gui/music_dropdown_hover.png"

                            text char_name.upper() style "music_dropdown_item_text"

                            action [Function(mp_change_character, char_name), SetScreenVariable("dropdown_open", False)]

    ## Handle escape/close to stop music and resume main menu music
    key "game_menu" action [Function(mp_cleanup_on_exit), Return()]

    ## Additional timer to ensure main menu music stops when first entering
    if not music_player_state.is_playing:
        timer 0.1 action Function(renpy.music.stop, channel="music", fadeout=0)

    ## Override the default return button action if present
    if main_menu:
        imagebutton:
            xpos 332
            ypos 824
            idle "gui/return_off.png"
            hover "gui/return_on.png"
            action [Function(mp_cleanup_on_exit), ShowMenu("main_menu")]
            style "igm_button"
            focus_mask None
            at igm_appear

################################################################################
## MUSIC PLAYER STYLES
################################################################################

style music_tab_text:
    kerning 0
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    hover_color "#27dc95"
    selected_color "#27dc95"
    selected_hover_color "#27dc95"
    outlines [(1, "#198c5f", 0, 0)]

style music_dropdown_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xalign 0.5
    yalign 0.5

style music_dropdown_item_text:
    kerning 0
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xalign 0.5
    yalign 0.5

style music_current_track:
    kerning 0
    size 22
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"
    outlines [(1, "#198c5f", 0, 0)]

## NEW STYLES FOR DURATION DISPLAY
style music_pos_text:
    kerning 0
    size 16
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    adjust_spacing False

style music_duration_text:
    kerning 0
    size 16
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    adjust_spacing False

style music_duration_separator:
    kerning 0
    size 16
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"

## NEW STYLE FOR PROGRESS BAR (Using orange bar)
style music_progress_bar:
    left_bar Frame("gui/orange_bar_on.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/orange_bar_off.png", gui.bar_borders, tile=gui.bar_tile)
    ysize 12
    thumb None

style music_track_text:
    kerning 0
    size 18
    font "fonts/wd7.otf"
    color "#34323d"
    xalign 0.0
    xoffset 10
    yalign 0.5

style music_volume_text:
    kerning 0
    size 16
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"

style music_volume_bar:
    left_bar Frame("gui/bar_magenta_on.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar_magenta_off.png", gui.bar_borders, tile=gui.bar_tile)
    ysize 18

style music_no_tracks_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"

style centered_dropdown_button is button:
    xsize 583
    ysize 40

style centered_dropdown_button_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xalign 0.5
    yalign 0.5
    text_align 0.5
    xoffset -112
    yoffset 1.5