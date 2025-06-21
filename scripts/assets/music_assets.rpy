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
        "photos_theme": "sundays-by-aves",#Diamond Pulse
        "title_theme": "thetomb",#闇の刻 (Yami no Koku)
        "tobita_theme": "totalbliss",#鬼灯の影 (Hōzuki no Kage)
        "dotonbori_theme": "hurracaine",#No Signal
        "yakuza_theme": "hesitation",#影の儀式 (Kage no Gishiki)
        "heaven_theme": "jakub_pietras_-_heirloom",#Éclats d’aurore
        "hell_theme": "quinten_john_coblentz_-_thursday",#Valse pour l’Enfer
        "chaos_theme": "chaos_theme",#Fractured Identity

        # Antonella themes
        "antonella_mistery_theme": "cicada-killer-by-idokay",
        "antonella_theme": "es_erudition-ambre-jaune",#Sakura in Spring
        "antonella_love": "smellofmorningcoffee",#sakura memories
        "antonella_sad_theme": "thirdperson", #unborn sakura
        "antonella_past_theme": "canibeforgiven", #a little bit of hope
        "antonella_game_theme": "tasteofsangria", #any questions
        "antonella_sexy_theme": "babyitsyou", #a game of skin
        "antonella_past_happy_theme": "racinglightbeam", #race of hearts
        "redkitsune_theme": "red_kitsune",#kitsune theme - red

        # Amber themes
        "amber_2nd_theme": "darktavern",#A Day Without You
        "amber_theme": "oak-and-cherry-flower",#Frost & Ashes
        "amber_anger_theme": "es_blood-of-garuda-(instrumental-version)-carvings",#Fuel the Fire
        "amber_sad_theme": "alon-peretz-spiral",#Fading Lullaby
        "amber_sexy_theme": "es_get-back-in-the-game-(instrumental-version)-clandestyne",#Sin & Silence
        "amber_sexy_theme2": "notize-come-closer-(instrumental)",#Shadow Waltz
        "amber_happy_theme": "es_spread-the-wings-of-winter-off-cuts",#veil of joy

        # Arlette themes
        "arlette_theme": "wedontlisten",#L’écho d’un adieu
        "arlette_love_theme": "present",#Un dernier espoir
        "arlette_nostalgia_theme": "clairedelune",#Dans l’ombre du passé
        "arlette_sexy_theme": "trappedintime",#À fleur de peau
        "arlette_sad_theme": "lasthope",#Le temps suspendu

        # Elizabeth themes
        "elizabeth_theme": "clouds-instrumental-version-by-sensitive-detective",#Paper Skyline
        "elizabeth_sexy_theme": "dogbeat-love-boat",#Falling in Slow Motion
        "elizabeth_sexy_theme2": "copenhagen-instrumental-version-by-oran-loyfer",#Smoke & Silk
        "elizabeth_anger_theme": "es_bimini-road-craft-case",#Distorted Memory
        "elizabeth_sad_theme": "a-different-meaning-by-tengrams",#Unfinished Goodbyes
        "elizabeth_play_theme": "ticket-to-ride-by-repina",#Glimmer Between Us
        "elizabeth_singing_song": "elizabeth_song",#レコードに落ちる涙 (Tears on Vinyl)

        # Isabella themes
        "isabella_theme": "hold-me-closer-instrumental-version-by-livingrooms",#Midnight Serenade
        "isabella_anger_theme": "es_approaching-meltdown-stems-bass-pearce-roswell",#Rupture of Silence
        "isabella_happy": "es_its-a-new-day-(instrumental-version)-holy-see",#Skipping Notes
        "isabella_serious": "ohad-ben-ari-prelude-cm",#Resonance of Resistance
        "isabella_sad": "prelude-in-e-minor,-op.-28,-no.-4-by-birraj,-artlist-classics,-frederic-chopin",#Adagio for Lost Time
        "isabella_sexy": "slow_hands_-_master",#Between the Lines

        # Kanae themes

        # Madison themes
        "madison_theme": "blueberrysmoker",#Sugartrap
        "madison_bad_theme": "madison_bad_theme",#Glassfang
        "madison_nan_theme": "madison_nanami_theme",#Through Her Eyes, I Vanish
        "madison_dom_theme": "walz_-_hellhound",#Queen of the Hollow
        "madison_sad_theme": "limbo_-_master",#Residue of Me
        "madison_sexy_theme": "es_lurking in the shadows",#Undress the Night

        # Nanami themes
        "nanami_chill_theme": "es_after-image-(instrumental-version)-i'min",#Fuwari Yume - ふわり夢
        "nanami_theme": "nanamitheme",#Hikari no Uta - 光の歌
        "nanami_love_theme": "nanami_love",#Himitsu no Koi - 秘密の恋
        "nanami_secure_theme": "nanami_secure",#Yume no Naka de - 夢の中で
        "nanami_clumsy_theme": "nanami_clumsy",#Chotto Matte! - ちょっと待って!
        "nanami_innocence_theme": "eva_tiedemann_-_what_falling_in_love_feels_like",#Hakanai Negai  - 儚い願い

        # Paz themes
        "paz_peace_theme": "justbones",#Golden Tide

        # MC themes
        "mc_theme": "es_chukou-ambre-jaune",#戻らぬ時 (Modoranu Toki)
        "mc_thinking_theme": "criticalthinking",#夢と分析 (Yume to Bunseki)
        "mc_broken_theme": "whispersofthewasteland",#帰らぬ昨日 (Kaeranu Kinō)
        "mc_suspense_theme": "steepencounters",#終わらない連鎖 (Owaranai Rensa)
        "mc_action_theme": "lostregister",#狂乱の刻 (Kyōran no Koku)
        "mc_action_theme2": "lostregister",#怒れる地響き (Ikareru Jihibiki)

        # Takeo themes

        # Relationship themes
        "mc_elizabeth_theme": "phoenix-instrumental-version-by-ben-goldstein",#Echoes of You
        "mc_nanami_theme": "samurai-royal-magic-hour", #Shizuka na Kokoro - 静かな心
        "mc_amber_x_theme": "stunned-man-by-nils-baumgartel",#The Last Embrace
    })

    # Create global variables for each theme
    globals().update(all_themes)