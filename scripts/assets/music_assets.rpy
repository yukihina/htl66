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
        "yukana_theme": "ottom_cherry-blossom",
        "discussion_theme": "es_indus-valley-craft-case",
        "danger_theme": "gone-rough-no-keys-by-ian-post",
        "photos_theme": "sundays-by-aves",
        "title_theme": "thetomb",
        "tobita_theme": "totalbliss",
        "dotonbori_theme": "hurracaine",
        "yakuza_theme": "hesitation",
        "heaven_theme": "jakub_pietras_-_heirloom",
        "hell_theme": "quinten_john_coblentz_-_thursday",
        "chaos_theme": "chaos_theme",

        # Antonella themes
        "antonella_mistery_theme": "cicada-killer-by-idokay",
        "antonella_theme": "es_erudition-ambre-jaune",
        "antonella_love": "smellofmorningcoffee",
        "antonella_sad_theme": "thirdperson",
        "antonella_past_theme": "canibeforgiven",
        "antonella_game_theme": "tasteofsangria",
        "antonella_sexy_theme": "babyitsyou",
        "antonella_past_happy_theme": "racinglightbeam",
        "redkitsune_theme": "red_kitsune",

        # Amber themes
        "amber_2nd_theme": "darktavern",
        "amber_theme": "oak-and-cherry-flower",
        "amber_anger_theme": "es_blood-of-garuda-(instrumental-version)-carvings",
        "amber_sad_theme": "alon-peretz-spiral",
        "amber_sexy_theme": "es_get-back-in-the-game-(instrumental-version)-clandestyne",
        "amber_sexy_theme2": "notize-come-closer-(instrumental)",
        "amber_action_theme": "es_spread-the-wings-of-winter-off-cuts",

        # Arlette themes
        "arlette_theme": "wedontlisten",
        "arlette_love_theme": "present",
        "arlette_nostalgia_theme": "clairedelune",
        "arlette_sexy_theme": "trappedintime",
        "arlette_sad_theme": "lasthope",

        # Elizabeth themes
        "elizabeth_theme": "clouds-instrumental-version-by-sensitive-detective",
        "elizabeth_sexy_theme": "dogbeat-love-boat",
        "elizabeth_sexy_theme2": "copenhagen-instrumental-version-by-oran-loyfer",
        "elizabeth_anger_theme": "es_bimini-road-craft-case",
        "elizabeth_sad_theme": "a-different-meaning-by-tengrams",
        "elizabeth_play_theme": "ticket-to-ride-by-repina",
        "elizabeth_singing_song": "elizabeth_song",

        # Isabella themes
        "isabella_guitar": "es_northern-stems-instruments-daniel-kaede",
        "isabella_themev": "livingrooms-hold-me-closer",
        "isabella_theme": "hold-me-closer-instrumental-version-by-livingrooms",
        "isabella_anger_theme_b": "es_approaching-meltdown-stems-bass-pearce-roswell",
        "isabella_anger_theme_d": "es_approaching-meltdown-stems-drums-pearce-roswell",
        "isabella_anger_theme_i": "es_approaching-meltdown-stems-instruments-pearce-roswell",
        "isabella_anger_theme_m": "es_approaching-meltdown-stems-melody-pearce-roswell",
        "isabella_happy": "es_its-a-new-day-(instrumental-version)-holy-see",
        "isabella_serious": "ohad-ben-ari-prelude-cm",
        "isabella_sad": "prelude-in-e-minor,-op.-28,-no.-4-by-birraj,-artlist-classics,-frederic-chopin",
        "isabella_sexy": "slow_hands_-_master",

        # Kanae themes
        "kanae_theme": "es_shapes-of-shadows-franz-gordon",
        "kanae_love": "es_togetherless-franz-gordon",

        # Madison themes
        "madison_theme": "blueberrysmoker",
        "madison_bad_theme": "madison_bad_theme",
        "madison_nan_theme": "madison_nanami_theme",
        "madison_dom_theme": "walz_-_hellhound",
        "madison_sad_theme": "limbo_-_master",
        "madison_sexy_theme": "es_lurking in the shadows",

        # Nanami themes
        "nanami_chill_theme": "es_after-image-(instrumental-version)-i'min",
        "nanami_theme": "nanamitheme",
        "nanami_love_theme": "nanami_love",
        "nanami_secure_theme": "nanami_secure",
        "nanami_clumsy_theme": "nanami_clumsy",
        "nanami_innocence_theme": "eva_tiedemann_-_what_falling_in_love_feels_like",

        # Paz themes
        "paz_peace_theme": "justbones",

        # MC themes
        "mc_peace_theme": "andean-feeling-by-pangal-and-gana",
        "mc_theme": "es_chukou-ambre-jaune",
        "mc_theme_b": "es_chukou-stems-bass-ambre-jaune",
        "mc_theme_d": "es_chukou-stems-drums-ambre-jaune",
        "mc_theme_i": "es_chukou-stems-instruments-ambre-jaune",
        "mc_theme_m": "es_chukou-stems-melody-ambre-jaune",
        "mc_thinking_theme": "criticalthinking",
        "mc_broken_theme": "whispersofthewasteland",
        "mc_hope_theme": "anomadsjourney",
        "mc_alone_theme": "arizona",
        "mc_suspense_theme": "steepencounters",
        "mc_action_theme": "lostregister",

        # Takeo themes
        "takeo_theme": "es_the-detective-christoffer-moe-ditlevsen",

        # Relationship themes
        "mc_elizabeth_theme": "phoenix-instrumental-version-by-ben-goldstein",
        "mc_nanami_theme": "samurai-royal-magic-hour",
        "mc_amber_x_theme": "stunned-man-by-nils-baumgartel",
        "mc_isabella_theme": "yuval-vilner-nocturne-in-e-flat-major-(op.-9-no.-2)"
    })

    # Create global variables for each theme
    globals().update(all_themes)