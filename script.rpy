init:
    default persistent.effectsOn = True
    define _scene_show_hide_transition = Dissolve(0.35)
    default mc_name = ""
    default walkthrough_enabled = False
    default persistent.walkthrough_all = False
    default persistent.walkthrough_li = set()
    default persistent.disclaimer = False
    default htl_episodes = 6.1
    default rm = RM()
    default ss = SexStats()

    # Persistent path lock variables for Milestone Decision System
    # Values: "love", "corruption", "neutral", or None (unlocked)
    default persistent.amber_path = None
    default persistent.nanami_path = None
    default persistent.elizabeth_path = None
    default persistent.isabella_path = None
    default persistent.kanae_path = None
    default persistent.arlette_path = None
    default persistent.antonella_path = None
    default persistent.madison_path = None
    default persistent.paz_path = None

    # MC Alignment System
    # Values: "rogue", "neutral", "paragon", or None (unlocked)
    default persistent.mc_alignment = None
    default persistent.current_episode = 0


################################################################################
## MILESTONE DECISION SYSTEM - Episode 6+ Path Locking
################################################################################
## These counters track significant path-defining choices for each character
## When a counter reaches a threshold (typically 3), the character's path locks

# Amber milestone counters
default amber_love_choices = 0
default amber_cor_choices = 0

# Nanami milestone counters
default nanami_love_choices = 0
default nanami_cor_choices = 0

# Elizabeth milestone counters
default elizabeth_love_choices = 0
default elizabeth_cor_choices = 0

# Isabella milestone counters
default isabella_love_choices = 0
default isabella_cor_choices = 0

# Kanae milestone counters
default kanae_love_choices = 0
default kanae_cor_choices = 0

# Arlette milestone counters
default arlette_love_choices = 0
default arlette_cor_choices = 0

# Antonella milestone counters
default antonella_love_choices = 0
default antonella_cor_choices = 0

# Madison milestone counters
default madison_love_choices = 0
default madison_cor_choices = 0

# Paz milestone counters
default paz_love_choices = 0
default paz_cor_choices = 0


################################################################################
## SAVE SYSTEM VERSION - For Migration Tracking
################################################################################
## Version 1: Original system without automatic progression rates (default for old saves)
## Version 2: New system with automatic character progression rate multipliers
default save_system_version = 1


init python:
    def show_walkthrough(key):
        if walkthrough_enabled and renpy.loadable("wt_core.rpyc"):
            if walkthrough_all:
                messages = []
                for option in walkthrough_data.get(key, {}):
                    if option != "all":
                        messages.append(walkthrough_data[key][option])
                message = " ".join(messages)
            else:
                message = ""
                for option in walkthrough_li:
                    if option in walkthrough_data.get(key, {}):
                        message += walkthrough_data[key][option] + " "

            if message:
                renpy.show_screen("walkthrough_screen", message=message)

    def update_htl_episodes():
        global htl_episodes
        if not htl_episodes == 6.1:
            htl_episodes = 6.1

label splashscreen:
    scene black
    show nl_bg with clouds_inverse_simple
    $ renpy.pause(0.1, hard=True)
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.5)
    $ playAudio(sfx_logo_brush, "sfx", 5, False, fadein=0, fadeout=0)
    show nl_lo:
            yalign 0.30
            xalign 0.5
    with horicolor_simple
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.5)
    $ playAudio(sfx_logo, "sfx", 8, False, fadein=0, fadeout=0)
    show nl_qo at bounce with bubbles_simple
    show nl_ga at neon_flicker, concentrate, sway with bubbles_simple
    show nl_jp at dizzyness with cwside_simple
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_logo_jp, "sfx", 2, False, fadein=0, fadeout=0)
    $ renpy.pause(3, hard=True)
    scene black with clouds_simple
    $ stopAllSubchannels(channel="sfx", fadeout=0.3)
    $ renpy.pause(0.3, hard=True)
    $ resetAllVolumes()
    return


label get_player_name:
    # Asking for the player's name
    $ mc_name = renpy.input("What is your name?", default="Chris", length=20).strip()
    $ mc_name = mc_name if mc_name else "Chris"
    
    return



label start:
    $ update_htl_episodes()
    $ save_system_version = 2  # New games start with version 2 (automatic progression rates)
    $ persistent.current_episode = 1  # New games start at episode 1
    stop music fadeout 0.5
    if not persistent.disclaimer:
        $ persistent.disclaimer = True
        call screen confirm_first_time(message="This R+ rated game contains explicit sexual content, strong language, graphic violence, and adult themes. All characters are fictional and 18+. Player discretion is advised.", yes_action=Return())
    else:
        pass
    scene black with smoke
    pause 0.5
    $ playAudio(sfx_hospital_hall, "amb", 1, True, 1, 0)
    call showNoise(0.1, 0.15, transition=dissolve)
    show namechg01 with bubbles
    "Nurse" "Good morning!"
    "Nurse" "I hope you're feeling better today. We've got most of the boring paperwork out of the way, thanks to that gorgeous companion of yours."
    "Nurse" "We just need you to confirm your name for our records. Think you can manage that for me?"
    "You" "Sure..."
    $ show_custom_notification("start_tip")
    show namechg02
    "Nurse" "I must say, your companion has been incredibly attentive in filling out your information."
    "Nurse" "It's not often we see such dedication around here."
    "Girl" "Oh, it's the least I could do for him."
    "You" "I really appreciate it, thank you both."
    show namechg03 with smoke
    "You" "My name... that's all that's left, huh? Everything else has been... handled."
    call get_player_name
    mc_t "Alright. It's [mc_name] then."
    scene black with watercolor
    $ stopAllSubchannels(channel="amb", fadeout=1)
    pause 1
    call hideNoise(transition=dissolve)
    jump ep01_title
    return

label after_load:
    call hideNoise(transition=dissolve)
    $ update_htl_episodes()

    python:
        try:

            global patched, patch_activated
            

            if renpy.persistent.patch_applied:
                patch_activated = True
                patched = True

            elif renpy.loadable("patch.rpyc"):
                patch_activated = True
                patched = True
                renpy.persistent.patch_applied = True
            
            if patched:
                characters = define_characters(True)
                relationships = define_relationships(True)
                globals().update(characters)
                globals().update(relationships)
        except:
            pass

    # Migrate old saves to new emotional lock system
    python:
        # Migrate RM class to include emotionally_locked field
        if hasattr(store, 'rm'):
            rm.migrate_old_saves()

        # Check and apply emotional locks for characters with 3 strikes
        for char in ["amber", "nanami", "elizabeth", "isabella", "kanae",
                     "arlette", "antonella", "madison", "paz"]:
            strikes = ss.get(char, "strike")
            if strikes >= 3:
                rm.check_emotional_lock(char)

    # Migrate old saves to new automatic progression rate system
    # Uses "!= 2" check to detect any save without the version 2 "seal"
    if save_system_version != 2:
        scene black with dissolve

        centered "{b}Character Progression System Updated{/b}\n\nWe've implemented an automatic character progression rate system\nto make stat changes more consistent and balanced.\n\n{color=#ffcc00}Your save will be automatically migrated.{/color}\n\nNote: Due to technical limitations, the migration may not be 100%% perfect.\nFor the best experience, we recommend starting a new playthrough.\n\n{size=24}Click to continue...{/size}"

        # Perform the migration
        $ rm.migrate_to_ratio_system()
        $ save_system_version = 2  # Apply version 2 "seal"

        centered "{b}Migration Complete{/b}\n\nYour character stats have been adjusted to the new system.\nFuture stat changes will use automatic progression rates.\n\n{size=24}Click to continue...{/size}"

    # Migrate current_episode for old saves
    # Auto-detect which episode the player is on based on seen labels
    python:
        if not hasattr(persistent, 'current_episode') or persistent.current_episode == 0:
            # Check which episode labels have been seen (in reverse order)
            for ep in range(20, 0, -1):  # Check from ep20 down to ep01
                if renpy.seen_label(f"ep{ep:02d}_start"):
                    persistent.current_episode = ep
                    break
            # If no episode labels seen, default to 1
            if persistent.current_episode == 0:
                persistent.current_episode = 1

    return