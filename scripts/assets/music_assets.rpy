# Documentation for the Ren'Py Music Definition Script
# ----------------------------------------------------

# Purpose:
# This script defines and organizes all music themes used in the game.
# It ensures consistency in file naming and easy maintenance of audio assets.

# Main Components:
# 1. Helper Functions:
#    - ensure_opus(): Adds .opus extension to filenames if not present.
#    - define_tracks(): Creates a dictionary of track names and their file paths.

# 2. all_themes Dictionary:
#    Contains all music themes organized by characters and categories.

# 3. globals().update(all_themes):
#    Creates global variables for each theme for easy access in the game.

# Usage:
# To play a theme in your game, use the playAudio function like this:
# $ playAudio(theme_name, "music", 1, True, 2, 0)
# Example: $ playAudio(antonella_theme, "music", 1, True, 2, 0)

# Adding New Themes:
# To add a new theme, simply add a new key-value pair to the all_themes dictionary.
# The key should be the theme name, and the value should be the filename without path.
# Example: "new_character_theme": "new_character_music_file"

# Naming Conventions:
# - Most themes end with '_theme' suffix, but some exceptions exist for compatibility.
# - File paths are automatically prefixed with "music/" and suffixed with ".opus".

# Compatibility Notes:
# - This script maintains backward compatibility with existing save games.
# - Some theme names (like 'antonella_love') don't have '_theme' suffix for this reason.

# Organization:
# Themes are grouped in the all_themes dictionary by character or category:
# - Various themes (general use)
# - Character-specific themes (e.g., Antonella, Amber, Elizabeth)
# - Relationship themes

# Maintenance:
# When updating this script, ensure that:
# 1. Existing theme names remain unchanged to maintain save game compatibility.
# 2. New themes follow the established naming patterns.
# 3. All audio files are in .opus format and located in the "music/" directory.

# Remember: This script only defines the themes. To change music during gameplay,
# use the playAudio function in your script or in conjunction with Ren'Py's audio system.

init -6 python:
    # Helper function to ensure .opus extension
    def ensure_opus(filename):
        return filename if filename.endswith('.opus') else f"{filename}.opus"

    # Define tracks with automatic .opus extension
    def define_tracks(tracks):
        return {name: f"music/{ensure_opus(filename)}" for name, filename in tracks.items()}

    # All themes
    all_themes = define_tracks({
        # Various themes
        "chaos_theme": "fractured-identity",#Fractured Identity
        "heaven_theme": "clats-d-aurore",#Éclats d'aurore
        "hell_theme": "valse-pour-l-enfer",#Valse pour l'Enfer
        "photos_theme": "diamond-pulse",#Diamond Pulse
        "title_theme": "yami-no-koku",#闇の刻 (Yami no Koku)

        # Antonella themes
        "antonella_game_theme": "any-questions", #any questions
        "antonella_horror_theme": "queen-of-carrion", #Queen of Carrion
        "antonella_love": "sakura-memories",#sakura memories
        "antonella_mistery_theme": "she-waits-in-the-fog",#She Waits in the Fog
        "antonella_past_happy_theme": "race-of-hearts", #race of hearts
        "antonella_past_theme": "a-little-bit-of-hope", #a little bit of hope
        "antonella_sad_theme": "unborn-sakura", #unborn sakura
        "antonella_sexy_theme": "a-game-of-skin", #a game of skin
        "antonella_singing_act1": "sakura-chiru-yoru",#桜散る夜 (Sakura Chiru Yoru)
        "antonella_theme": "sakura-in-spring",#Sakura in Spring

        # Amber themes
        "amber_2nd_theme": "a-day-without-you",#A Day Without You
        "amber_anger_theme": "fuel-the-fire",#Fuel the Fire
        "amber_happy_theme": "veil-of-joy",#veil of joy
        "amber_sad_theme": "fading-lullaby",#Fading Lullaby
        "amber_sexy_theme": "sin-silence",#Sin & Silence
        "amber_sexy_theme2": "shadow-waltz",#Shadow Waltz
        "amber_theme": "frost-ashes",#Frost & Ashes
        "amber2_love_theme": "in-ewiger-umarmung",#In ewiger Umarmung
        #"amber2_action_theme": "mein-besitz-mein-schutz",#Mein Besitz, mein Schutz
        #"amber2_past_theme": "unvergessliche-jahre",#Unvergessliche Jahre
        #"amber2_happy_theme": "tanz-ins-licht",#Tanz ins Licht
        "amber2_theme": "unvergessliche-jahre",#Unvergessliche Jahre
        #"amber2_lost_theme": "schwarzestes-herz",#Schwärzestes Herz

        # Arlette themes
        "arlette_love_theme": "un-dernier-espoir",#Un dernier espoir
        "arlette_nostalgia_theme": "dans-l-ombre-du-pass",#Dans l'ombre du passé
        "arlette_sad_theme": "le-temps-suspendu",#Le temps suspendu
        "arlette_sexy_theme": "fleur-de-peau",#À fleur de peau
        "arlette_theme": "l-cho-d-un-adieu",#L'écho d'un adieu

        # Elizabeth themes
        "elizabeth_anger_theme": "distorted-memory",#Distorted Memory
        "elizabeth_play_theme": "glimmer-between-us",#Glimmer Between Us
        "elizabeth_sad_theme": "unfinished-goodbyes",#Unfinished Goodbyes
        "elizabeth_sexy_theme": "falling-in-slow-motion",#Falling in Slow Motion
        "elizabeth_sexy_theme2": "smoke-silk",#Smoke & Silk
        "elizabeth_singing_song": "tears-on-vinyl",#レコードに落ちる涙 (Tears on Vinyl)
        "elizabeth_theme": "paper-skyline",#Paper Skyline

        # Isabella themes
        "isabella_anger_theme": "rupture-of-silence",#Rupture of Silence
        "isabella_happy": "skipping-notes",#Skipping Notes
        "isabella_sad": "adagio-for-lost-time",#Adagio for Lost Time
        "isabella_serious": "resonance-of-resistance",#Resonance of Resistance
        "isabella_sexy": "between-the-lines",#Between the Lines
        "isabella_theme": "midnight-serenade",#Midnight Serenade

        # Kanae themes

        # Kitsune themes
        "redkitsune_theme": "kitsune-s-theme-red",#kitsune theme - red

        # Madison themes
        "madison_bad_theme": "glassfang",#Glassfang
        "madison_dom_theme": "queen-of-the-hollow",#Queen of the Hollow
        "madison_nan_theme": "through-her-eyes-i-vanish",#Through Her Eyes, I Vanish
        "madison_sad_theme": "residue-of-me",#Residue of Me
        "madison_sexy_theme": "undress-the-night",#Undress the Night
        "madison_theme": "sugartrap",#Sugartrap

        # Nanami themes
        "nanami_chill_theme": "fuwari-yume",#Fuwari Yume - ふわり夢
        "nanami_clumsy_theme": "chotto-matte",#Chotto Matte! - ちょっと待って!
        "nanami_innocence_theme": "hakanai-negai",#Hakanai Negai  - 儚い願い
        "nanami_love_theme": "himitsu-no-koi",#Himitsu no Koi - 秘密の恋
        "nanami_secure_theme": "yume-no-naka-de",#Yume no Naka de - 夢の中で
        "nanami_theme": "hikari-no-uta",#Hikari no Uta - 光の歌

        # Paz themes
        "paz_happy_theme": "golden-tide",#Golden Tide
        "paz_theme": "ember-glow",#Ember Glow

        # MC themes
        "mc_action_theme": "ky-ran-no-koku",#狂乱の刻 (Kyōran no Koku)
        "mc_action_theme2": "ikareru-jihibiki",#怒れる地響き (Ikareru Jihibiki)
        "mc_broken_theme": "kaeranu-kin",#帰らぬ昨日 (Kaeranu Kinō)
        "mc_suspense_theme": "owaranai-rensa",#終わらない連鎖 (Owaranai Rensa)
        "mc_theme": "modoranu-toki",#戻らぬ時 (Modoranu Toki)
        "mc_thinking_theme": "yume-to-bunseki",#夢と分析 (Yume to Bunseki)

        # Michael themes
        "mic_theme": "the-serpents-elegy",#The Serpent's Elegy

        # Takeo themes

        # Relationship themes
        "mc_amber_x_theme": "the-last-embrace",#The Last Embrace
        "mc_elizabeth_theme": "echoes-of-you",#Echoes of You
        "mc_nanami_theme": "shizuka-na-kokoro", #Shizuka na Kokoro - 静かな心

        # Yakuza themes
        "dotonbori_theme": "no-signal",#No Signal
        "tobita_theme": "h-zuki-no-kage",#鬼灯の影 (Hōzuki no Kage)
        #"onsen_theme": "sakazuki-steam",#Sakazuki Steam
        "kobeyamaguchi_theme": "kage-no-gishiki",#影の儀式 (Kage no Gishiki)
        #"inagawakai_theme": "sakazuki-s-shadow",#Sakazuki's Shadow
        #"sumiyoshikai_theme": "irezumi-s-hum",#Irezumi's Hum
        #"yamaguchigumi_theme": "the-sixth-clan-s-decree",#The Sixth Clan's Decree
        "kudokai_theme": "the-silent-kumicho",#The Silent Kumicho
    })

    # Create global variables for each theme
    globals().update(all_themes)