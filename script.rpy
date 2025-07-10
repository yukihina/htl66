﻿init:
    default persistent.effectsOn = True
    define _scene_show_hide_transition = Dissolve(0.35)
    default mc_name = ""
    default walkthrough_enabled = False
    default persistent.walkthrough_all = False
    default persistent.walkthrough_li = set()
    default persistent.disclaimer = False
    default htl_episodes = 5.3
    default rm = RM()
    default ss = SexStats()


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
        if not htl_episodes == 5.3:
            htl_episodes = 5.3 

label splashscreen:
    scene black
    show nl_bg with clouds_inverse_simple
    $ renpy.pause(0.1, hard=True)
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.5)
    $ playAudio(sfx_logo_brush, "sfx", 5, False, fadein=0, fadeout=0)
    show nl_lo:
            yalign 0.5
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

    return
