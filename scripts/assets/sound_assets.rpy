# Documentation for the Ren'Py Sound Effects (SFX) Script
# ------------------------------------------------------

# Purpose:
# This script defines and organizes all sound effects used in the game.
# It ensures consistency in file naming and easy maintenance of audio assets.

# Main Components:
# 1. Helper Functions:
#    - ensure_opus(): Adds .opus extension to filenames if not present.
#    - define_sfx(): Creates a dictionary of SFX names and their file paths.

# 2. sfx_categories Dictionary:
#    Contains all sound effects organized by categories (e.g., ambient, body, objects).

# 3. Global Variable Creation:
#    Creates global variables for each SFX for easy access in the game.

# Usage:
# To play a sound effect in your game, use the playAudio function like this:
# $ playAudio(sfx_name, "sfx", subchannel_1_10, False, fadein=fade_duration, fadeout=fade_duration)
# Example: $ playAudio(sfx_dooropen, "sfx", 1, False, fadein=0.5, fadeout=0.5)

# Adding New Sound Effects:
# To add a new SFX, simply add a new key-value pair to the appropriate category in sfx_categories.
# The key should be the SFX name (without 'sfx_' prefix), and the value should be the filename without path.
# Example: "new_sound": "new_sound_file_name"

# Categorization:
# Sound effects are grouped in the sfx_categories dictionary by type:
# - ambient: Background and environmental sounds
# - body: Human body-related sounds
# - objects: Sounds produced by various objects
# - vehicles: Vehicle-related sounds
# - electronics: Sounds from electronic devices
# - human_sounds: Specific sounds produced by humans
# - misc: Miscellaneous sounds that don't fit other categories

# File Naming Convention:
# All sound files should be in .opus format and located in the "sfx/" directory.
# The script automatically adds the "sfx/" prefix and ".opus" extension if not present.

# Backward Compatibility:
# This script maintains compatibility with existing save games and older script versions.
# All SFX are accessible as global variables with the 'sfx_' prefix.

# Performance Note:
# This script defines all SFX at init, which might impact initial loading time for large numbers of SFX.
# However, it ensures quick access during gameplay.

# Maintenance:
# When updating this script, ensure that:
# 1. New sound effects are added to the appropriate category in sfx_categories.
# 2. File paths and names are correct.
# 3. Any removed or renamed SFX are also updated in the game scripts where they are used.

# Remember: The playAudio function and related audio system must be defined elsewhere in your project.
# This script only defines the sound effects, not the playback system.

init -5 python:
    # Define SFX with automatic .opus extension
    def define_sfx(sfx_dict):
        return {name: f"sfx/{ensure_opus(filename)}" for name, filename in sfx_dict.items()}

    # Categorized SFX
    sfx_categories = {
        "ambient": define_sfx({
            "airplane_interior": "nc/transportation-collection-aircraft-interior-ambience-hum",
            "airbus_flyby": "nc/transports-plane,-airbus-a320-airliner,-flyby",
            "airportwalla": "nc/busy_departure_lounge-_japanese_accent-_new_chitose_airport-_hokkaido-_japan-01_normal_1",
            "applause": "nc/applause-small-group-clapping",
            "ambergameplay": "nc/ambergameplay",
            "birds1": "es_birds-park-3-sfx-producer",
            "beach" : "nc/beach",
            "beach2" : "nc/beach2",
            "citypast": "es_san-francisco-sfx-producer",
            "clinicwalla": "nc/clinic_basewalla",
            "clinicwalla2": "nc/clinic_beepwalla",
            "clinicwalla3": "nc/clinic_announcingwalla",
            "clinicroom": "nc/clinicroom_basewalla",
            "clinicrooftop": "nc/clinic_rooftop",
            "earlymor": "quiet-cityscapes-early-morning-street-ambience-bird",
            "earlypast": "city-living-morning-ambience-breeze-distant-traffic-distant-dogs-and-birds-by-daniel-vasquez",
            "evenpark": "this-is-tokyo-by-omnibit-park",
            "evenstreet": "this-is-tokyo-street-ambience-traffic-vehicles-walla",
            "extnight": "inner-city-traffic-quiet-night-ambience,-crickets-chirping,-distant-vehicles",
            "evening_pool": "es_city-ambience-5-sfx-producer",
            "evenbalcony": "tokyo-ambiences-16th-floor-balcony-city-traffic-rumble-by-glitchedtones",
            "eveningtraffic": "this-is-tokyo-evening-traffic-ambience,-cars-passing-by-by-omnibit-sound",
            "fireplace": "es_fireplace-constant-burning-flame-4-sfx-producer",
            "fashion": "nc/fashion_backstage",
            "factory": "nc/factory_walla",
            "hospital_hall": "hospital-corridor-beeping-people-ambiance-by-db-studios",
            "hshall": "school_hall",
            "hotel_lobby": "nc/hotel_lobby",
            "japancrossing": "this-is-tokyo-busy-crossing-loud-advertisements-walla-traffic-by-omnibit-sound",
            "japanbuilding": "es_tokyo-japan-skyline-city-sfx-producer",
            "japanday_cross": "this-is-tokyo-busy-crossing-ambience-daytime-traffic-distant-trains-by-omnibit",
            "japansirens": "tokyo-sirens-in-the-street-people-walking-by-talking-by-rob-kubicki",
            "library": "es_library-main-entrance-ambience-2-sfx-producer",
            "mall": "this-is-tokyo-by-omnibit-sound",
            "midnightpast": "quiet-cityscapes-downtown-ambience-night-air-conditioner-unit-hum-by-west-wolf",
            "midnighthome": "quiet-cityscapes-empty-city-ambience-night-crows-by-west-wolf",
            "morning": "es_suburb-morning-sfx-producer",
            "morning_late": "city-living-morning-ambience-birds-chipping-distant-traffic",
            "morning_late2": "england-and-ireland-calm-morning-birds-chirping-distant-traffic-by-junglesonic",
            "morning_tobita": "anime-mania-summer-ambience-cicadas-in-the-forest-birds-by-omnibit-sound",
            "nightpool": "es_night-ambience-2-sfx-producer",
            "nightclub": "es_nightclub-walla-4-sfx-producer",
            "nightsleep": "es_subdivision-night-sfx-producer",
            "nighttobita": "city-center-suburbian-ambience-crickets-distant-traffic-by-sava-ivanov",
            "nightroad": "the-recordist-city-street,-quiet-night,-distant-train-horn,-crickets,-car-passing",
            "night_cicada": "nc/tokyo-ambiences-buzzing-cicadas,-warm-summer-time",
            "park1": "es_amb-park-sfx-producer",
            "park2": "es_park-1-sfx-producer",
            "parking": "es_parking-structure-sfx-producer",
            "public_bath": "es_fan-public-bathroom-sfx-producer",
            "quietnite": "this-is-tokyo-quiet-neighborhood,-vehicles-passing-b",
            "quietnite2": "city-living-apartment-room-tone,-hum,-distant-bird-by-daniel-vasquez",
            "raining_ext": "nature-of-japan-rain-on-village-street-by-omnibit-sound",
            "restaurant": "es_restaurant-ambience-sfx-producer",
            "stationamb": "this-is-tokyo-train-ride-ambience-japanese-announcements-by-omnibit-sound",
            "stationbeep": "this-is-tokyo-train-station-ambience-ticket-gate-beeping-distant-people-by-omnibit-sound",
            "trainstopped": "this-is-tokyo-train-ride-ambience-stopped-announcements-engine-starting-by-omnibit-sound",
            "train_ext": "es_japanese-train-3-sfx-producer",
            "trainstationquiet": "tel-aviv-ambiences-quiet-train-station",
            "traininterior": "tokyo-train-ambience-passengers-talking-public-announcements-by-rob-kubicki",
            "tokyo_residential": "nc/this-is-tokyo-residential-area,-crickets-chirping,-vehicles-passing-by",
            "temple_outside": "nc/temple_outside",
            "underwater": "es_underwater-ambience-4-sfx-producer",
            "windyprairie": "qp01-0085-prairie-day-wind-crickets",
            "wind_pool": "qp02-0163-wind-plants-breeze-dry-twigs-leaves",
        }),

        "body": define_sfx({
            "backpack": "es_bag-zips-open-sfx-producer",
            "bedmove": "es_cloth-bed-sheet-move-sfx-producer",
            "bedmove2": "es_bed-slaps-covers-movement-4-sfx-producer",
            "bedmove3": "es_bed-movement-7-sfx-producer",
            "bedmove4": "es_bed-movement-8-sfx-producer",
            "bedmove5": "es_bed-sheet-movement-3-sfx-producer",
            "bodyfall": "es_body-falls-39-sfx-producer",
            "bodyfall_carpet": "es_body-falls-30-sfx-producer",
            "bodygrab": "es_hair-grab-sfx-producer",
            "bodydrag": "es_body-drag-5-sfx-producer",
            "breath_sleep_f": "the-lungs-breath,-female,-deep-nasal,-sleepy-calm-breath-by-articulated-sounds",
            "breathmouth_sleep_f": "the-lungs-breath,-female,-deep,-soft,-inhale-exhale,-open-mouth-by-articulated-sounds",
            "boxing_alone": "nc/boxing-gym-bag-punches",
            "bed_sitdown": "nc/es_bed-sit-down-sfx-producer",
            "bed_laying": "nc/furniture-movements-vol-2-single-bed-jump",
            "bed_creaking": "nc/es_bed-creaks-11-sfx-producer",
            "blood_splash": "nc/blood_splash",
            "changeclothes_nozip": "es_clothes-short-sfx-producer",
            "changeclothes_zip": "nc/raw_fabrics_vol_2_-_37_-_leather_zip",
            "drinking_fem": "nc/drink_water",
            "earringin": "es_tonal-ring-bys-sfx-producer",
            "eeeh_female": "anime-mania-female-voice-shocked-ehh-by-omnibit-sound",
            "eeh_nanami": "nanami_eeh",
            "femexhale": "es_female-exhale-7-sfx-producer",
            "femheavybreath": "teen-spirit-female-heavy-breathing-inhaling-exhaling-by-borrtex",
            "fem_surprised": "womanly-surprised-reaction-breath-in-shocked-female-by-daruma",
            "fem_huhquest": "womanly-surprised-reaction-huh",
            "fem_hmm": "real-voices-female-hmm-reaction-confused",
            "footsteps_bare": "es_footsteps-bare-foot-sfx-producer",
            "footsteps_bare_wood": "nc/wood_barefoot_running",
            "footsteps_heelstile": "elegant-footsteps-high-heels-walk-on-tile-floor",
            "footsteps_female_semirun": "es_female-boots-run-1-sfx-producer",
            "footsteps_male_semirun": "es_work-boots-14-sfx-producer",
            "femalerun": "steps-neutral-dress-shoes-running-by-the-foley-bros",
            "femaletiredrun": "female-breathing-after-run-by-foley-walkers",
            "fem_huh_girly": "female-emotes-misunderstood,-huh-by-john-silke",
            "fem_sigh_girly": "jrpg-voices-female-voice-reaction,-deep-sigh-by-ni-sound",
            "fem_sighyay_girly": "jrpg-voices-female-voice-reaction,-coquettish-sigh-by-ni-sound",
            "fem_yay_girly": "jrpg-voices-female-voice-reaction,-laughter,-giggles-by-ni-sound",
            "fearanana": "fearnana",
            "gulping_water": "nc/gulping_water",
            "gasp_female": "sensual-female-relaxed-orgasm-panting-gasping-",
            "hallwalkmale": "es_footsteps-cement-19-sfx-producer",
            "hallwalkfemale": "es_female-boots-jog-sfx-producer",
            "heartbeatslow": "es_heartbeat-slow-low-sfx-producer",
            "heartbeatfast": "es_heartbeat-fast-low-sfx-producer",
            "heart_monitor": "nc/heart_monitor",
            "inhale_fem2": "es_sigh-inhale-exhale-sfx-producer",
            "jumpoverbody": "es_jump-swish-sfx-producer",
            "jump_to_floor": "nc/jump_on_deck",
            "kiss": "es_human-kiss-1-sfx-producer",
            "kiss_one": "kiss,-single-peck-by-martin-scaglia",
            "kiss_nana": "kissnana",
            "kiss_op_isa": "kiss_open_isa",
            "kiss_water": "nc/kiss_water",
            "knife_jab": "nc/knife_jab",
            "laughcutefem": "anime-mania-female-voice,-laugh,-cute",
            "laughnana": "nanalaugh",
            "licklolli": "lickinglollipop",
            "laughnana2": "laughnanami2",
            "onknees": "brawl-body-fall-on-grass-by-giacomo-maraboli",
            "ouch_nana": "female-voice-reaction-deep-pantiong-and-shivering-jrpg-voices-by-ni-sound-",
            "punch": "in-your-face-hit-body-punch-whooshing-by-the-sound-pack-tree",
            "punch_floor": "nc/punch_floor",
            "punch_glass": "nc/punching_glass",
            "runconcrete": "steps-running-with-boots-on-concrete",
            "sighbreathfem": "female-essentials-deep-breath-tired-sigh-by-cline-woodburn",
            "sigh_nana": "female-reaction-coquettish-sigh-jrpg-voices-by-ni-sound",
            "slap": "es_slap-face-2-sfx-producer",
            "sigh_relief": "satisfaction-woman,-sigh-of-relief,-ahh-by-john-silke",
            "stairs_up": "es_carpet-stairs-up-2-sfx-producer",
            "surprisenana": "surpriselownana",
            "walk_slow_f": "shoe-collection-heels-slow-walk-by-periscope-post-&-audio",
            "walk_barefoot": "shoe-collection-bare-walking,-slow,-barefoot-by-periscope-post-&-audio",
            "water_walk": "nc/es_water-walk-wade-slow-sfx-producer",
            "wet_barefoot": "nc/step-it-up-footsteps,-barefoot-on-wet-tile-floor,-walking",
            "yawnfem": "es_yawn-long-female-sfx-producer",
            "yawnnana": "nc/young_woman_reactions_vol_2_-_relief_yawn",
            "yellnana": "nanayell",
        }),

        "objects": define_sfx({
            "bells": "es_multimedia-184-sfx-producer",
            "blip": "es_bubble-blip-1-sfx-producer",
            "boobdrama": "boom-bouncy-dramatic-tension-by-federico-soler",
            "box_search": "es_boxes-stack-sfx-producer",
            "bodydrop_ontable": "nc/wood_table-_organic",
            "bathtub_sink1": "nc/bathtub1",
            "bathtub_sink2": "nc/bathtub2",
            "clic1": "clic1",
            "clic2": "clic2",
            "celldoor": "nc/doors-101-prison-cell-door,-metallic,-slammed",
            "clothes": "nc/take-off_clothes",
            "coffee_mkr": "nc/coffeemaker",
            "disclaimer": "animdisclaimer",
            "door_wood": "nc/wood_door",
            "doorclose": "es_door-close-2-sfx-producer",
            "dooropen_public": "es_door-open-public-sfx-producer",
            "doorclose_public": "es_door-close-gym-2-sfx-producer",
            "doorcknob": "es_door-knob-turn-11-sfx-producer",
            "dooropen": "es_wood-door-open-soft-close-sfx-producer",
            "door_shower": "our-bathroom-shower-door,-open,-rattle-by-glitchedtones",
            "door_knock": "nc/es_door-knock-door-1-sfx-producer",
            "door_open2": "nc/es_bedroom-door-open-3-sfx-producer",
            "drop_ontable": "nc/es_textbook-drop-3-sfx-producer",
            "door_front_getin": "nc/front-door-getting-in,-closing-door,-street-to-interior-perspective",
            "digitalcamera1": "nc/digital-cameras-snapping-pictures-with-auto-focus",
            "digitalcamera2": "nc/digital-cameras-slr-flash-popup,-shutter-clicks",
            "digitalcamera3": "nc/digital-cameras-slr-flash-popup,-shutter-clicks-and-beeps",
            "door_glass": "nc/es_door-open-glass-2-sfx-producer",
            "door_bell": "nc/es_bell-store-door-2-sfx-producer",
            "door_open_creak": "door_open_creak",
            "fridge_opendoor": "essential-doors-fridge-door,-opening-by-sonic-bat",
            "fridge_closedoor": "essential-doors-fridge-door,-closing-by-sonic-bat",
            "fridge_hum": "empty-rooms-kitchen-roomtone,-fridge-suction,-whir-by-soundbits",
            "faucet_close": "es_faucet-squeak-2-sfx-producer",
            "flaslight_turnon": "flashlight_turnon",
            "glassbreak": "fight-double-punch-with-glass-break-by-refocus",
            "guncock9mm": "es_gun-handgun-731-sfx-producer",
            "gunshots_glock": "marine-pistols-glock-19,-two-shots-by-dfmg-signature-series",
            "gunshot_beretta": "top-gun-beretta-pistol-single-shot-by-bjorn-lynne",
            "garageopen": "around-the-house-garage-door,-opening-by-stuart-duffield",
            "glass_knock": "nc/es_glass-knock-3-sfx-producer",
            "glass_ontable": "nc/glass_-_leave_bottle_on_table",
            "glass_bottle": "nc/glass-bottle,-picking-up-glass-bottle",
            "glitch": "glitch",
            "hairdryeron": "hairdryer_on",
            "hairdryeroff": "hairdryer_off",
            "hover": "button-click",
            "impact": "ff_et_impact_sparkle",
            "intro_episode": "nc/intro_episode",
            "insect_flying": "nc/es_insect-wings-fly-3-sfx-producer",
            "insect_flying2": "nc/es_insect-wings-fly-4-sfx-producer",
            "keys": "es_door-key-locked-sfx-producer",
            "kick_door": "nc/es_crash-door-kick-open-2-sfx-producer",
            "katana_warn": "katana_warning",
            "katana_sheath_hit": "katana_sheath_hit",
            "kitchen_rumm": "nc/rummingkitchen",
            "lightswitchon": "es_light-switch-flip-1-sfx-producer",
            "lick1": "es_lick-fingers-sfx-producer",
            "liquorbottle": "es_liquor-bottle-1-sfx-producer",
            "logo": "nc/cute-interface-synth-bells-phrase,-notification",
            "logo_brush": "nc/es_wire-brush-scrape-3-sfx-producer",
            "logo_jp": "nc/cute-interface-far-east-string-arpeggio-notification",
            "lamp_turnon": "lamp_turnon",
            "magic": "es_magical-shimmer-sfx-producer",
            "monster": "nc/es_monster-demon-sfx-producer",
            "mug": "nc/es_mug-sfx-producer",
            "phone": "es_cell-phone-vibrate-11-sfx-producer",
            "phone_typing": "nc/phone_typing",
            "phone_eli": "es_mobile-phone-vibrate-sfx-producer",
            "police_siren": "es_police-siren-int-2-sfx-producer",
            "pills": "es_pill-drop-glass-2-sfx-producer",
            "piss_fem": "nc/peeing_fem",
            "phonering": "es_telephone-ring-two-tone-sfx-producer",
            "paperhandling": "es_envelope-manila-hand-1-sfx-producer",
            "paperhandling2": "es_leather-bible-8-sfx-producer",
            "pool_moving": "nc/es_pool-indoor-enter-2-sfx-producer",
            "pool_splash": "nc/swimming-a-water-splash",
            "pool_outof": "nc/swimming-getting-out-of-pool",
            "pool_dive": "nc/swimming-swimmer-single-dive,-water-splash,-close-up",
            "pc_playing_kbm": "nc/typing-playing-video-game,-fast-keyboard-and-mouse-action",
            "pool_surfacing": "nc/swimming-swimmer-surfacing",
            "paper_mov": "nc/es_paper-movement-book-sfx-producer",
            "recordscratch": "tddc_crackle_05_7_inch_45rpm_90",
            "recstop": "es_record-scratch-4-sfx-producer",
            "room_noise": "nc/es_room-tone-23-sfx-producer",
            "room_noise2": "nc/es_room-tone-22-sfx-producer",
            "room_noise3": "nc/room-tones-empty-room,-air-condition-hum,-movements-next-door",
            "rubble": "nc/es_rocks-rattle-sfx-producer",
            "scup": "es_suction-cup-3-sfx-producer",
            "showerrun": "es_water-shower-run-3-sfx-producer",
            "slamdoor": "es_bedroom-door-slam-sfx-producer",
            "splashpool": "es_pool-indoor-splash-3-sfx-producer",
            "spop": "es_suction-pop-6-sfx-producer",
            "stab": "ff_et_ping_atonal_flutter_a",
            "stars": "es_prel-pixie-dust-tin-3-sfx-producer",
            "stairsdown_fast": "es_stairs-down-wood-1-sfx-producer",
            "swallow1": "es_human-swallow-1-sfx-producer",
            "shirtripe": "es_dress-shirt-wipe-2-sfx-producer",
            "sniff": "es_sniff-breathe-in-4-sfx-producer",
            "slamdoorhard": "our-living-room-door-slam-by-glitchedtones",
            "showering": "es_shower-run-1-sfx-producer",
            "sms": "smartphone-notification-sounds-water-drip,-incoming,-message,-reminder-by-axlsound",
            "sms2": "smartphone-notification-sounds-strings,-fast-plucking,-message,-incoming,-reminder,-alert-by-axlsound",
            "swing_children": "nc/introvert-rocking-chair,-vintage,-wood-creaking,-slow_1",
            "sofa_move": "nc/furniture-movements-vol-2-heavy-leather-sofa-friction,-sitting-down",
            "scissors_cutting": "nc/barber-scissors,-cutting",
            "shower_faucet": "nc/es_faucet-squeak-2-sfx-producer",
            "taxidoor": "es_police-car-int-sfx-producer",
            "taxihorn": "es_car-horn-honk-61-sfx-producer",
            "tooltip": "bleeping-synth-notes-ni-sound-",
            "tea": "nc/pouring_tea",
            "tea_splash": "nc/throw_cup",
            "tibetantitle": "es_tibetan-instrument-4-sfx-producer",
            "tires_screech": "es_auto-tires-squeal-sfx-producer",
            "tablehit": "nc/vibrant-hits-wood-table-hit",
            "towelshake": "nc/es_towel-shake-out-2-sfx-producer",
            "toweldrop": "nc/es_towel-dry-drop-sfx-producer",
            "unfold": "nc/es_suit-coat-unfold-sfx-producer",
            "vendingmachine": "es_vending-machine-35-sfx-producer",
            "vcall": "nc/videocall",
            "void": "nc/es_drone-empty-void-sfx-producer",
            "wood": "es_table-move-sfx-producer",
            "walletpickup": "es_wallet-pick-up-2-sfx-producer",
            "wardrobe": "nc/odds-and-ends-wardrobe-coat-hangers-squeaking",
            "wings": "nc/flying_flock_of_birds_to_the_food",
            "wings_evil": "nc/jurassic_sounds_-_pterodactyl-_wings_flapping-_flying_v2",
            "zipper": "es_dress-pants-zipper-1-sfx-producer",
        }),

        "vehicles": define_sfx({
            "car_idle_to_off": "bmw-740-executive-car-idle-to-turn-off-interior-by-redline-sound-library",
            "car_start_to_idle": "bmw-740-executive-car-start-and-idle-interior-by-redline-sound-library",
            "carhit": "body-fall-on-metal-surface-two-hits-by-martin-scaglia-royalty-free-sound-effects-track",
            "car_runover": "es_car-run-over-body-2-sfx-producer",
            "car_parking": "bmw-740-executive-car-passing-by-and-parking,-turn-and-reversing-slow,-exterior-by-redline-sound-library",
            "car_racing": "astonmartin",
            "cardoor_open": "nc/es_car-door-open-39-sfx-producer",
            "carcrash": "carcrash",
            "car_driveaway": "driveaway",
            "motorbike_passingby": "nc/triumph-motorcycle-drive-by,-50-mph,-left-to-right",
            "motorbike_stop": "nc/triumph-motorcycle-idle,-strong-revs,-back-perspective",
            "taxiint": "es_car-ride-interior-sfx-producer",
        }),

        "electronics": define_sfx({
            "cameras_photoshoot": "nc/press-conference,-camera-flashing,-walla",
            "camer_shutter": "nc/es_camera-clicks-sfx-producer",
            "cute_igbutton": "nc/cute-interface-bottle-cap-notification",
            "camerashot": "camer_shot",
            "cell_ringtone": "nc/es_cell-ringtone-27-sfx-producer",
        }),

        "human_sounds": define_sfx({
            "applause": "nc/applause-small-group-clapping",
            "bj1": "632000__lesbian-siren__pov-i-m-giving-you-head",
            "children_laugh": "nc/es_children-laughing-sfx-producer",
            "deeptsub": "ameafterdark__sub-blowjob-intense-bpm-34",
            "female_hmm": "female_ls_a_grunt09",
            "female_hmm2": "sensual-female-sexy-approval",
            "fellatio1": "making-love-french-kissing-tongue-wet",
            "flirtsmile": "sensual-female-smile",
            "gagreflex1": "sdtgag22",
            "gagreflex2": "sexgag4",
            "gagreflex3": "sexgag3",
            "gagreflex4": "sexgag6",
            "madbreathxxx": "female-breathing-middle-by-foley-walkers",
            "madmoanxxx": "jrpg-voices-female-voice-reaction-panting-and-sharp-moan-by-ni-sound",
            "madmoan2xxx": "jrpg-voices-female-voice-reaction-panting-and-moaning-by-ni-sound",
            "madmoan3xxx": "satisfaction-woman-moaning-enjoying-by-john-silke",
            "madohxxx": "jrpg-voices-female-voice-reaction-gasping-for-air-by-ni-sound",
            "mast_fem": "445838__jchiledred__masturbating-index-finger",
            "moan_breath": "swfmoan184",
            "moan_breath2": "swfmoan193",
            "moan_breath3": "swfmoan164",
            "moan_generic": "sensual-female-gasp-into-relaxed-moan-mmm-by-evg-sound-fx",
            "moan_cum_generic": "sensual-female-short-intense-panting-by-evg-sound-fx-",
            "moan_orgasm_generic": "sensual-female-intense-orgasm-moaning-panting-by-evg-sound-fx",
            "panting1": "clairepant1",
            "shortmakeout": "es_kissing-sloppy-make-out-2-sfx-producer",
            "sexslide1": "swfslide16",
            "slosh1": "sdtslosh7",
        }),

        "misc": define_sfx({
            "cum_bigload_fast": "es_blood-spurt-3-sfx-producer",
            "cunni_slippery": "making-love-french-kissing-tongues-wet-by-evg-sound-fx",
            "clock": "nc/small-clocks-clock-ticking,-analog-clock",
            "chair_rolling": "nc/trivial-foley-rolling-office-chair,-slide",
            "cafewalla": "nc/city-perspectives-cafe,-people-walla,-cashier,-coffee-machine,-edinburgh,-scotland",
            "curtains_open": "nc/household-pulling-curtains,-long-motion",
            "chair_lather_sit": "nc/es_leather-chair-sfx-producer",
            "grass_walk": "nc/es_footsteps-grass-3-sfx-producer",
            "gym_ambience": "nc/ambiences-vol-1-large-gym,-few-people,-reverberant",
            "livingroom": "nc/house-tones-living-room-tone",
            "loud_bg": "nc/this-is-tokyo-loud-construction,-machinery,-hammering",
            "mc_room_night": "nc/worldwide-empty-hotel-room-tone",
            "metro_opendoor": "nc/england-and-ireland-train,-doors-open,-exiting",
            "office": "nc/tel-aviv-ambiences-office,-people-type,-talk",
            "office2": "nc/es_office-walla-light-sfx-producer",
            "officechair_creak": "officechair_creaking",
            "officechair_sit": "officechair_sit",
            "prison": "nc/es_prison-ambience-3-sfx-producer",
            "echodot": "nc/notifications_6",
            "sirens_passby": "nc/emergency-sirens-police-car-siren,-approaching,-passing-by,-left-to-right"
        })
    }

    # Create global variables for each SFX
    for category, sfx_dict in sfx_categories.items():
        for sfx_name, sfx_path in sfx_dict.items():
            globals()[f"sfx_{sfx_name}"] = sfx_path