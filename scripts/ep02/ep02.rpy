label ep02_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    call showNoise(0.1, 0.15, transition=dissolve)
    $ quick_menu = True
    $ renpy.block_rollback()
## -- INTRO SCENE HOME
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    show ep02_home1 with slowfade
    $ config.rollback_enabled = True
    show screen stats_button
    show screen walkthrough_icon
    mc_t "[renpy.substitute(dialogues2['E02START_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02START_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02START_d003'])]"
    show ep02_home2
    mc_t "[renpy.substitute(dialogues2['E02START_d004'])]"
    mc_t "[renpy.substitute(dialogues2['E02START_d005'])]"
    show ep02_home3
    mc_t "[renpy.substitute(dialogues2['E02START_d006'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_lovehotel

## -- AOI SEX SCENE HOME
label ep02_lovehotel:
    scene eigengrau with clouds_inverse
    show ep02_osaka1 with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_nightroad, "amb", 2, True, 1.5, 0)
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    mc_t "[renpy.substitute(dialogues2['E02LOVEHOTEL_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02LOVEHOTEL_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02LOVEHOTEL_d003'])]"
    show ep02_osaka2
    mc_t "[renpy.substitute(dialogues2['E02LOVEHOTEL_d004'])]"
    mc_t "[renpy.substitute(dialogues2['E02LOVEHOTEL_d005'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(mc_theme, "music", 2, True, 2.5, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.4, fade_duration=1.5)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    show ep02_hotel01
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d006'])]"
    show ep02_hotel02
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d007'])]"
    $ stopAudio(channel="amb", subchannel=2, fadeout=10)
    show ep02_hotel03
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d008'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d009'])]"
    show ep02_hotel04
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d010'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d011'])]"
    show ep02_hotel05
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d012'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d013'])]"
    show ep02_hotel06
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d014'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d015'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d016'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d017'])]"
    show ep02_hotel07 with ccirclewipe
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d018'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d019'])]"
    show ep02_hotel08
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d020'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d021'])]"
    show ep02_hotel09
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d022'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d023'])]"
    show ep02_hotel10
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d024'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d025'])]"
    show ep02_hotel11
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d026'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d027'])]"
    show ep02_hotel12 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d028'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d029'])]"
    show ep02_hotel13 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d030'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d031'])]"
    show ep02_01_anim2
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d032'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d033'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d034'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d035'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d036'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d037'])]"
    show ep02_hotel14 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d038'])]"
    show ep02_hotel14 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d039'])]"
    show ep02_hotel15 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d040'])]"
    show ep02_hotel15 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d041'])]"
    show ep02_01_anim1 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d042'])]"
    show ep02_01_anim1 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d043'])]"
    show ep02_01_anim1 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d044'])]"
    show ep02_01_anim1 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d045'])]"
    show ep02_hotel16 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d046'])]"
    show ep02_hotel16 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d047'])]"
    show ep02_hotel16 with hpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d048'])]"
    show ep02_hotel17
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d049'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d050'])]"
    show ep02_hotel18
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d051'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d052'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d053'])]"
    show ep02_hotel19
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d054'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d055'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d056'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d057'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d058'])]"
    scene eigengrau with dissolve
    show ep02_hotel20 with circlewipe
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d059'])]"
    show ep02_hotel20 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d060'])]"
    show ep02_hotel20 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d061'])]"
    show ep02_hotel21 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d062'])]"
    show ep02_hotel21 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d063'])]"
    show ep02_hotel21 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d064'])]"
    show ep02_hotel22
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d065'])]"
    show ep02_hotel22 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d066'])]"
    show ep02_hotel23
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d067'])]"
    show ep02_hotel23 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d068'])]"
    show ep02_hotel23 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d069'])]"
    show ep02_hotel23 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d070'])]"
    show ep02_hotel24
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d071'])]"
    show ep02_hotel24 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d072'])]"
    show ep02_hotel24 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d073'])]"
    show ep02_hotel24 with vpunch
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d074'])]"
    show ep02_hotel25
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d075'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d076'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d077'])]"
    show ep02_hotel26 with slowfade
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d078'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d079'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d080'])]"
    show ep02_hotel27 with dissolve
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d081'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d082'])]"
    show ep02_hotel28 with slowflash
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d083'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d084'])]"
    show ep02_hotel29
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d085'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d086'])]"
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d087'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d088'])]"
    show ep02_hotel30
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d089'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEHOTEL_d090'])]"
    show ep02_hotel31
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d091'])]"
    show ep02_hotel32
    aoi "[renpy.substitute(dialogues2['E02LOVEHOTEL_d092'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_mc_depression

label ep02_mc_depression:
#WALKKING TO HOME
    scene eigengrau with dissolve
    $ playAudio(sfx_raining_ext, "amb", 1, True, 2.5, 0)
    show ep02_booze01 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d001'])]"
    show ep02_booze02
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d003'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d004'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d005'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d006'])]"
    show ep02_booze03
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d007'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d008'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d009'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d010'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d011'])]"
    show ep02_booze04
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d012'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d013'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d014'])]"
    show ep02_booze05
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d015'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d016'])]"
    show ep02_booze06
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d017'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d018'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d019'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d020'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d021'])]"
    show ep02_booze07
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d022'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d023'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCDEP_d024'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_booze08 with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_evening_pool, "amb", 2, True, 2.5, 0)
    mc_s "[renpy.substitute(dialogues2['E02MCDEP_d025'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCDEP_d026'])]"
    show ep02_booze09
    $ rm.set_knows("paz", True)
    pa_s "[renpy.substitute(dialogues2['E02MCDEP_d027'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCDEP_d028'])]"
    show ep02_booze10
    pa_s "[renpy.substitute(dialogues2['E02MCDEP_d029'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCDEP_d030'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCDEP_d031'])]"
    $ show_walkthrough("ep02_pazmctits_menu")
    menu:
        "Check her tits":
            hide screen walkthrough_screen
            jump ep02_paz_tits
        "Check her legs":
            hide screen walkthrough_screen
            jump ep02_paz_legs


    
label ep02_paz_tits:
    show ep02_booze12
    $ ep02_checkpaz += 1
    mc_t "[renpy.substitute(dialogues2['E02PAZTITS_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02PAZTITS_d002'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZTITS_d003'])]"
    if ep02_checkpaz == 3:
        mc_s "[renpy.substitute(dialogues2['E02PAZTITS_d004'])]"
        jump ep02_mc_paz_fight
    else:
        mc_s "[renpy.substitute(dialogues2['E02PAZTITS_d005'])]"
        jump ep02_paz_legs
    
label ep02_paz_legs:
    show ep02_booze11
    $ ep02_checkpaz += 2
    mc_t "[renpy.substitute(dialogues2['E02PAZLEGS_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02PAZLEGS_d002'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZLEGS_d003'])]"
    if ep02_checkpaz == 3:
        mc_s "[renpy.substitute(dialogues2['E02PAZLEGS_d004'])]"
        jump ep02_mc_paz_fight
    else:
        mc_s "[renpy.substitute(dialogues2['E02PAZLEGS_d005'])]"
        jump ep02_paz_tits


label ep02_mc_paz_fight: 
    mc_t "[renpy.substitute(dialogues2['E02PAZFIGHT_d001'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(mc_broken_theme, "music", 1, True, 4, 0)
    show ep02_booze13 with vpunch
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d002'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d003'])]"
    $ show_walkthrough("ep02_mc_paz_fight_menu1")
    menu:
        mc_t "[renpy.substitute(dialogues2['E02PAZFIGHT_d004'])]"
        "I'll talk to them":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 1)
            $ check_levels("paz", "trust", 1)
            mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d005'])]"
            pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d006'])]"
            mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d007'])]"
            show ep02_booze14
            pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d008'])]"
            mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d009'])]"
        "I don't care":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d010'])]"
            pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d011'])]"
            pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d012'])]"
            show ep02_booze14
            mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d013'])]"
    show ep02_booze15 with hpunch
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d014'])]"
    mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d015'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d016'])]"
    show ep02_booze16
    mc_t "[renpy.substitute(dialogues2['E02PAZFIGHT_d017'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d018'])]"
    show ep02_booze17
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d019'])]"
    mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d020'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d021'])]"
    show ep02_booze18
    mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d022'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d023'])]"
    mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d024'])]"
    show ep02_booze19 with vpunch
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d025'])]"
    mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d026'])]"
    mc_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d027'])]"
    scene eigengrau with dissolve
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_slamdoor, "sfx", 1, False, 0, 0)
    show ep02_booze20 with vpunch
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d028'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d029'])]"
    pa_s "[renpy.substitute(dialogues2['E02PAZFIGHT_d030'])]"
    mc_t "[renpy.substitute(dialogues2['E02PAZFIGHT_d031'])]"
    mc_t "[renpy.substitute(dialogues2['E02PAZFIGHT_d032'])]"
    show ep02_booze21
    mc_t "[renpy.substitute(dialogues2['E02PAZFIGHT_d033'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_tobita_sinchi

label ep02_tobita_sinchi:
    scene eigengrau with dissolve
    $ playAudio(sfx_raining_ext, "amb", 1, True, 2.5, 0)
    $ playAudio(sfx_nighttobita, "amb", 2, True, 2.5, 0)
    show ep02_tobita1
    show tobita_location zorder 2 with dissolve
    pause 4
    hide tobita_location with dissolve
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d003'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d004'])]"
    show ep02_tobita2
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d005'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d006'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d007'])]"
    show ep02_whore01
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d008'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d009'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITA_d010'])]"
    show ep02_whore02
    aya "[renpy.substitute(dialogues2['E02TOBITA_d011'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITA_d012'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITA_d013'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITA_d014'])]"
    show ep02_whore03
    aya "[renpy.substitute(dialogues2['E02TOBITA_d015'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITA_d016'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITA_d017'])]"
    show ep02_whore04
    mc_s "[renpy.substitute(dialogues2['E02TOBITA_d018'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITA_d019'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITA_d020'])]"
    $ show_walkthrough("ep02_whore_menu1")
    menu:
        mc_t "[renpy.substitute(dialogues2['E02TOBITA_d021'])]"
        "Got it, thanks":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 1)
            jump ep02_tobita_sinchi_good
        "Fuck off":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -1)
            jump ep02_tobita_sinchi_bad

label ep02_tobita_sinchi_bad:
    show ep02_whore06
    mc_s "[renpy.substitute(dialogues2['E02TOBITABAD_d001'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d002'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d003'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d004'])]"
    show ep02_whore05
    mc_s "[renpy.substitute(dialogues2['E02TOBITABAD_d005'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d006'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITABAD_d007'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d008'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITABAD_d009'])]"
    hide ep02_whore05
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d010'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d011'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITABAD_d012'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITABAD_d013'])]"
    jump ep02_tobita_sinchi_aoicomes

label ep02_tobita_sinchi_good:
    show ep02_whore08
    mc_s "[renpy.substitute(dialogues2['E02TOBITAGOOD_d001'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITAGOOD_d002'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITAGOOD_d003'])]"
    show ep02_whore07
    aya "[renpy.substitute(dialogues2['E02TOBITAGOOD_d004'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITAGOOD_d005'])]"
    mc_t "[renpy.substitute(dialogues2['E02TOBITAGOOD_d006'])]"
    hide ep02_whore07
    mc_s "[renpy.substitute(dialogues2['E02TOBITAGOOD_d007'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITAGOOD_d008'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITAGOOD_d009'])]"
    jump ep02_tobita_sinchi_aoicomes

label ep02_tobita_sinchi_aoicomes:
    show ep02_whore09 with hpunch
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d001'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d002'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d003'])]"
    show ep02_whore10
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d004'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d005'])]"
    hide ep02_whore10
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d006'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d007'])]"
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1.5)
    show ep02_whore11 with ccirclewipe
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d008'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d009'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d010'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d011'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d012'])]"
    show ep02_whore12
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d013'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d014'])]"
    show ep02_whore13
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d015'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d016'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d017'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d018'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(tobita_theme, "music", 1, True, 4, 0)
    scene eigengrau with dissolve
    show ep02_whore14 at dizzyness with circlewipe
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d019'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d020'])]"
    show ep02_whore15 at dizzyness with slowfade
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d021'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d022'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d023'])]"
    show ep02_whore16 at dizzyness
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d024'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d025'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d026'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d027'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d028'])]"
    show ep02_whore17 at dizzyness with hpunch
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d029'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d030'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d031'])]"
    show ep02_whore18 at dizzyness
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d032'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d033'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d034'])]"
    show ep02_whore19 at dizzyness
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d035'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d036'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d037'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d038'])]"
    show ep02_whore20 at dizzyness
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d039'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d040'])]"
    show ep02_whore21 at dizzyness with vpunch
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d041'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d042'])]"
    show ep02_whore22 at dizzyness with hpunch
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d043'])]"
    show ep02_whore23 at dizzyness
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d044'])]"
    show ep02_whore24 at dizzyness
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d045'])]"
    show ep02_whore25 at dizzyness with slowfade
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d046'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d047'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d048'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d049'])]"
    scene eigengrau with dissolve
    show ep02_whore26 at dizzyness with circlewipe 
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d050'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d051'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d052'])]"
    show ep02_whore27 at dizzyness
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d053'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d054'])]"
    show ep02_whore28 at dizzyness
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d055'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d056'])]"
    show ep02_whore29 at dizzyness
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d057'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d058'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d059'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d060'])]"
    show ep02_whore30 at dizzyness
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d061'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d062'])]"
    mc_s "[renpy.substitute(dialogues2['E02TOBITACOMES_d063'])]"
    aya "[renpy.substitute(dialogues2['E02TOBITACOMES_d064'])]"
    aoi "[renpy.substitute(dialogues2['E02TOBITACOMES_d065'])]"
    $ show_walkthrough("ep02_sexwhorescene_menu")
    menu:
        mc_t "[renpy.substitute(dialogues2['E02TOBITACOMES_d066'])]"
        "Just Aoi":
            hide screen walkthrough_screen
            $ ep02_tobitabj += 1
            jump ep02_tobita_sinchi_bj
        "Both of them":
            hide screen walkthrough_screen
            $ ep02_tobitabj += 2
            jump ep02_tobita_sinchi_bj

label ep02_tobita_sinchi_bj:
    show ep02_whore31 at dizzyness
    if ep02_tobitabj == 1:
        mc_s "[renpy.substitute(dialogues2['E02TOBITABJ_d001'])]"
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d002'])]"
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d003'])]"
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d004'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02TOBITABJ_d005'])]"
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d006'])]"
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d007'])]"
    scene eigengrau with dissolve
    show ep02_whore33 at dizzyness with circlewipe
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d008'])]"
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d009'])]"
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d010'])]"
    else:
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d011'])]"
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d012'])]"
    show ep02_whore34 at dizzyness
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d013'])]"
    else:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d014'])]"
        mc_s "[renpy.substitute(dialogues2['E02TOBITABJ_d015'])]"
    show ep02_whore35 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d016'])]"
    else:
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d017'])]"
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d018'])]"
        mc_s "[renpy.substitute(dialogues2['E02TOBITABJ_d019'])]"
    show ep02_whore36 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d020'])]"
    else:
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d021'])]"
        show ep02_whore37 at dizzyness with hpunch
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d022'])]"
    show ep02_whore38 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d023'])]"
    else:
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d024'])]"
    show ep02_whore39 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d025'])]"
    else:
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d026'])]"
    show ep02_whore40 with dissolve
    if ep02_tobitabj == 1:
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d027'])]"
        aoi "[renpy.substitute(dialogues2['E02TOBITABJ_d028'])]"
    else:
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d030'])]"
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d031'])]"
        aya "[renpy.substitute(dialogues2['E02TOBITABJ_d032'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_yakuza_club

label ep02_yakuza_club:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.7)
    $ playAudio(sfx_evenstreet, "amb", 3, True, 2.5, 0)
    show ep02_dotonbori1 with slowfade
    show doton_location zorder 2 with dissolve
    pause 4
    hide doton_location with dissolve
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d003'])]"
    $ stopAudio(channel="amb", subchannel=3, fadeout=1.5)
    show ep02_hostclub01 with slowfade
    $ playAudio(dotonbori_theme, "music", 2, True, 2.5, 0)
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d004'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d005'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d006'])]"
    show ep02_hostclub02
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d007'])]"
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d008'])]"
    show ep02_hostclub03
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d009'])]"
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d010'])]"
    show ep02_hostclub04
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d011'])]"
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d012'])]"
    show ep02_hostclub05
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d013'])]"
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d014'])]"
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d015'])]"
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d016'])]"
    show ep02_hostclub06
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d017'])]"
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d018'])]"
    show ep02_hostclub07
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d019'])]"
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d020'])]"
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d021'])]"
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d022'])]"
    show ep02_hostclub08
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d023'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d024'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d025'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d026'])]"
    show ep02_hostclub09
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d027'])]"
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d028'])]"
    show ep02_hostclub10
    mc_t "[renpy.substitute(dialogues2['E02YAKUCLUB_d029'])]"
    show ep02_hostclub11
    rin "[renpy.substitute(dialogues2['E02YAKUCLUB_d030'])]"
    show ep02_hostclub12
    "Bodyguard" "[renpy.substitute(dialogues2['E02YAKUCLUB_d034'])]"
    show ep02_hostclub13
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d031'])]"
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d032'])]"
    hid "[renpy.substitute(dialogues2['E02YAKUCLUB_d033'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_the_day_after

label ep02_the_day_after:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2.5, 0)
    show ep02_nxtbooze01 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d001'])]" 
    show ep02_nxtbooze02
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d002'])]"
    show ep02_nxtbooze03
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d003'])]"
    show ep02_nxtbooze04
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d004'])]"
    show ep02_nxtbooze05
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d005'])]"
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d006'])]"
    show ep02_nxtbooze06
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d007'])]"
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d008'])]"
    show ep02_nxtbooze07
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d009'])]"
    show ep02_nxtbooze08
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d010'])]"
    show ep02_nxtbooze09
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d011'])]"
    show ep02_nxtbooze10
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d012'])]"
    show ep02_nxtbooze11
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d013'])]"
    show ep02_nxtbooze12
    mc_t "[renpy.substitute(dialogues2['E02DAYAFTER_d014'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_arle_intro

label ep02_arle_intro:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_eveningtraffic, "amb", 2, True, 2.5, 0)
    show ep02_friends01 with slowfade
    show kama_location zorder 2 with dissolve
    pause 4
    hide kama_location with dissolve
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d001'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d002'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.15, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.4)
    $ playAudio(arlette_theme, "music", 3, True, 2.5, 0)
    show ep02_friends02
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d003'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d004'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d005'])]"
    show ep02_friends03
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d006'])]"
    show ep02_friends04
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d007'])]"
    show ep02_friends05 with hpunch
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d008'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d009'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d010'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d011'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d012'])]"
    show ep02_friends06
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d013'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d014'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d015'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d016'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d017'])]"
    show ep02_friends07
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d018'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d019'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d020'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d021'])]"
    show ep02_friends08
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d022'])]"
    show ep02_friends09
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d023'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d024'])]"
    show ep02_friends10
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d025'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d026'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d027'])]"
    show ep02_friends11
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d028'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEINTRO_d029'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEINTRO_d030'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_the_talk

label ep02_the_talk:
    scene eigengrau with dissolve
    $ playAudio(sfx_japanday_cross, "amb", 2, True, 2.5, 0)
    show ep02_partners01 with slowfade
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d001'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d002'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d003'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.7)
    $ playAudio(paz_theme, "music", 1, True, 2.5, 0)
    show ep02_partners02
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d004'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d005'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d006'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d007'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d008'])]"
    show ep02_partners03
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d009'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d010'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d011'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d012'])]"
    show ep02_partners04
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d013'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d014'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d015'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d016'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d017'])]"
    show ep02_partners05
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d018'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d019'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d020'])]"
    show ep02_partners06
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d021'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d022'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d023'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d024'])]"
    show ep02_partners07
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d025'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d026'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d027'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d028'])]"
    show ep02_partners08
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d029'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d030'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d031'])]"
    show ep02_partners09
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d032'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d033'])]"
    show ep02_partners10
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d034'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d019'])]"
    show ep02_partners11
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d036'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d037'])]"
    show ep02_partners12
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d038'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d039'])]"
    show ep02_partners13
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d040'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d041'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d042'])]"
    show ep02_partners14
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d043'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d044'])]"
    show ep02_partners15
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d045'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d046'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d047'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d048'])]"
    show ep02_partners16
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d049'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d050'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d051'])]"
    mc_s "[renpy.substitute(dialogues2['E02THETALK_d052'])]"
    pa_s "[renpy.substitute(dialogues2['E02THETALK_d053'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_mc_meet_arle

label ep02_mc_meet_arle:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.7)
    $ playAudio(sfx_evenstreet, "amb", 3, True, 2.5, 0)
    show ep02_dotonite1 with slowfade
    show doton_location zorder 2 with dissolve
    pause 4
    hide doton_location with dissolve
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d001'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d002'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d003'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.5)
    $ playAudio(sfx_nightclub, "amb", 1, True, 2.5, 0)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(dotonbori_theme, "music", 2, True, 2.5, 0)
    show ep02_arlehost01 with slowfade
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d004'])]"
    show ep02_arlehost02
    "Host" "[renpy.substitute(dialogues2['E02MCMEETARLE_d131'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d005'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d006'])]"
    "Host" "[renpy.substitute(dialogues2['E02MCMEETARLE_d132'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=1, fade_duration=1.5)
    show ep02_arlehost03
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d007'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d008'])]"
    show ep02_arlehost04
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d009'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d010'])]"
    hide ep02_arlehost04
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d011'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d012'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d013'])]"
    show ep02_arlehost05 with hpunch
    $ rm.set_knows("arlette", True)
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d014'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d015'])]"
    show ep02_arlehost06
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d016'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d017'])]"
    show ep02_arlehost07
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d018'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d019'])]"
    show ep02_arlehost08
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d020'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d021'])]"
    show ep02_arlehost09
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d022'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d023'])]"
    show ep02_arlehost10
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d024'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d025'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d026'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d027'])]"
    show ep02_arlehost11
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d028'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d029'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d030'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d031'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d032'])]"
    show ep02_arlehost12
    "Host" "[renpy.substitute(dialogues2['E02MCMEETARLE_d133'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d033'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d034'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d035'])]"
    show ep02_arlehost13
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d036'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d037'])]"
    show ep02_arlehost14
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d038'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d039'])]"
    show ep02_arlehost15
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d040'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d041'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d042'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d043'])]"
    show ep02_arlehost16
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d044'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d045'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep02_arlehost17 with slowfade
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d046'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d047'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d048'])]"
    show ep02_arlehost18
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d049'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d050'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d051'])]"
    hide ep02_arlehost18
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d052'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d053'])]"
    show ep02_arlehost19
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d054'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d055'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d056'])]"
    show ep02_arlehost20
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d057'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d058'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d059'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d060'])]"
    show ep02_arlehost21
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d061'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d062'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d063'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d064'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d065'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d066'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d067'])]"
    show ep02_arlehost22
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d068'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d069'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d070'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d071'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d072'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d073'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d074'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d075'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d076'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d077'])]"
    show ep02_arlehost23 with slowfade
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d078'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d079'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d080'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d081'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d082'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d083'])]"
    pa_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d084'])]"
    show ep02_arlehost24
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d085'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d086'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d087'])]"
    show ep02_arlehost25
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d088'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d089'])]"
    mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d090'])]"
    arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d091'])]"
    $ show_walkthrough("ep02_arlehost_menu1")
    menu:
        mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d092'])]"
        "Tell the truth":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d093'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d094'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d095'])]"
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d096'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d097'])]"
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d098'])]"
        "Avoid answer":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d099'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d100'])]"
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d101'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d102'])]"
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d103'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d104'])]"
            mc_s "[renpy.substitute(dialogues2['E02MCMEETARLE_d105'])]"
            arl "[renpy.substitute(dialogues2['E02MCMEETARLE_d106'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ playAudio(arlette_love_theme, "music", 1, True, 2.5, 0)
    show ep02_arlehost26 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d107'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d108'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d109'])]"
    show ep02_arlehost28
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d110'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d111'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d112'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d113'])]"
    show ep02_arlehost27
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d114'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d115'])]"
    show ep02_arlehost29 with dissolve
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d116'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d117'])]"
    show ep02_arlehost30 with dissolve
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d118'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d119'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d120'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d121'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d122'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d123'])]"
    show ep02_arlehost32
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d124'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d125'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d126'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d127'])]"
    show ep02_arlehost31 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d128'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d129'])]"
    mc_t "[renpy.substitute(dialogues2['E02MCMEETARLE_d130'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_arle_past

label ep02_arle_past:
    scene eigengrau with dissolve
    $ playAudio(sfx_beach, "amb", 1, True, 2.5, 0)
    show ep02_arlestory01 with slowfade
    show taniwa_location zorder 2 with dissolve
    pause 4
    hide taniwa_location with dissolve
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d002'])]"
    show ep02_arlestory02
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d003'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d004'])]"
    $ stopAudio(channel="amb", subchannel=1, fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_beach2, "amb", 2, True, 2.5, 0)
    scene eigengrau with dissolve
    show ep02_arlestory03 with circlewipe
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d005'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d006'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d007'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d008'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d009'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d010'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d011'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d012'])]"
    show ep02_arlestory04
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d013'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d014'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d015'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    $ playAudio(arlette_nostalgia_theme, "music", 1, True, 2.5, 0)
    show ep02_arlestory05 with slowfade
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d016'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d017'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d018'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d019'])]"
    show ep02_arlestory06 with slowfade
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d020'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d021'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d022'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d023'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
    show ep02_arlestory08
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d024'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d025'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d026'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d027'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d028'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d029'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d030'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d031'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d032'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d033'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d034'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d035'])]"
    show ep02_arlestory07
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d036'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d037'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d038'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d039'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d040'])]"
    show ep02_arlestory09
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d041'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d042'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d043'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d044'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d045'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d046'])]"
    show ep02_arlestory10
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d047'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d048'])]"
    show ep02_arlestory11
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d049'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d050'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEPAST_d051'])]"
    show ep02_arlestory12
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d052'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d053'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d054'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d055'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d056'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEPAST_d057'])]"
    show ep02_arlestory13
    arl "[renpy.substitute(dialogues2['E02ARLEPAST_d058'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_arle_mc_sex

label ep02_arle_mc_sex:
    scene eigengrau with dissolve
    show ep02_arlehotel19 with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_beach2, "amb", 2, True, 2.5, 0)
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d001'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d002'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.1, fade_duration=2.5)
    show ep02_arlehotel01
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d003'])]"
    $ playAudio(arlette_theme, "music", 1, True, 2.5, 0)
    show ep02_arlehotel02
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d004'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d005'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d006'])]"
    show ep02_arlehotel03 with vpunch
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d007'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d008'])]"
    show ep02_arlehotel04 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d009'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d010'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d011'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d012'])]"
    show ep02_arlehotel05 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d013'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d014'])]"
    $ show_walkthrough("ep02_arlehotel_menu1")
    menu:
        "I thought about it a few times":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d015'])]"
            arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d016'])]"
        "Yeah, I was...":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d017'])]"
            arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d018'])]"
        "I've jerked off thinking about you.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d019'])]"
            arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d020'])]"
    show ep02_arlehotel06 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d021'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d022'])]"
    show ep02_arlehotel07
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d023'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d024'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d025'])]"
    show ep02_arlehotel08
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d026'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d027'])]"
    show ep02_arlehotel09
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d028'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d029'])]"
    show ep02_arlehotel10
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d030'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d031'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d032'])]"
    show ep02_arlehotel11
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d033'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d034'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d035'])]"
    show ep02_arlehotel12
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d036'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d037'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d038'])]"
    show ep02_arlehotel13
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d039'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d040'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d041'])]"
    show ep02_arlehotel14 at concentrate
    $ show_walkthrough("ep02_arlehotel_menu2")
    menu:
        "Cum on her face":
            hide screen walkthrough_screen
            $ ep02_beachcum += 1
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)
            pass
        "Cum on her tits":
            hide screen walkthrough_screen
            $ ep02_beachcum += 2
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            pass
    show ep02_arlehotel15 with flash
    show white zorder 1.0 at ejaculation_flash
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d042'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d043'])]"
    show ep02_arlehotel16
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d044'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d045'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_arlehotel17 with slowfade
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d046'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d047'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d048'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d049'])]"
    show ep02_arlehotel18
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d050'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d051'])]"
    if ep02_beachcum ==2:
        arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d052'])]"
    else:
        arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d053'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d054'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d055'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d056'])]"
    scene eigengrau with dissolve
    show ep02_arlehotel20 with circlewipe
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.6, fade_duration=2.5)
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d057'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d058'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d059'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d060'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d061'])]"
    show ep02_arlehotel21
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d062'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d063'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d064'])]"
    $ show_walkthrough("ep02_arlehotel_menu3")
    menu:
        "You mean in lingerie?":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d065'])]"
            arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d066'])]"
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d067'])]"
        "I wouldn't mind if you stayed in less":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d068'])]"
            arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d069'])]"
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d070'])]"
        "Stay as long as you like.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d071'])]"
            arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d072'])]"
            mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d073'])]"
    $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSEX_d074'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=2.5)
    show ep02_arlehotel22
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSEX_d075'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSEX_d076'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSEX_d077'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSEX_d078'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSEX_d079'])]"
    scene eigengrau with dissolve
    show ep02_arlehotel23 with slowfade
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d080'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d081'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d082'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d083'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d084'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d085'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d086'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d087'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSEX_d088'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d089'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d090'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSEX_d091'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_grandma

label ep02_grandma:
    scene eigengrau with dissolve
    show ep02_hospital1 with slowfade
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.8)
    $ playAudio(sfx_japansirens, "amb", 3, True, 2.5, 0)
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d003'])]"
    $ stopAudio(channel="amb", subchannel=3, fadeout=1.5)
    show ep02_hospital2 with slowfade
    $ setChannelVolume(channel="amb", subchannel=4, volume=1)
    $ playAudio(sfx_hospital_hall, "amb", 4, True, 2.5, 0)
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d004'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d005'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d006'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d007'])]"
    rin "[renpy.substitute(dialogues2['E02GRANDMA_d008'])]"
    show ep02_hospital3
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d009'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d010'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d011'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d012'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d013'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d014'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d015'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d016'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d017'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d018'])]"
    show ep02_hospital4
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d019'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d020'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d021'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d022'])]"
    show ep02_hospital5 with vpunch
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d023'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d024'])]"
    show ep02_hospital6
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d025'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d026'])]"
    hide ep02_hospital6
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d027'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d028'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d029'])]"
    show ep02_hospital7 with hpunch
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d030'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d031'])]"
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d032'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d033'])]"
    arl "[renpy.substitute(dialogues2['E02GRANDMA_d034'])]"
    show ep02_hospital8 with slowfade
    mc_s "[renpy.substitute(dialogues2['E02GRANDMA_d035'])]"
    mc_t "[renpy.substitute(dialogues2['E02GRANDMA_d036'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_arle_hell

label ep02_arle_hell:
    scene eigengrau with dissolve
    show ep02_temptation1 with slowfade
    $ playAudio(sfx_japancrossing, "amb", 1, True, 2.5, 0)
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d001'])]"
    show ep02_temptation2
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d002'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d003'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d004'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d005'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d006'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.5, fade_duration=4)
    $ playAudio(arlette_sad_theme, "music", 1, True, 2.5, 0)
    show ep02_temptation3
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d007'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d008'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d009'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d010'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d011'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d012'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d013'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d014'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d015'])]"
    show ep02_temptation4
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d016'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d017'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d018'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d019'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d020'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d021'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d022'])]"
    show ep02_temptation5 with slowfade
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d023'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d024'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d025'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d026'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d027'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d028'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d029'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d030'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d031'])]"
    show ep02_temptation6
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d032'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d033'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d034'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d035'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d036'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d037'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d038'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_escort01 with ccirclewipe
    mc_t "[renpy.substitute(dialogues2['E02ARLEHELL_d039'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEHELL_d040'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d041'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d042'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d043'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d044'])]"
    show ep02_escort02 with hpunch
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d045'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d046'])]"
    show ep02_escort03
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d047'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d048'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d049'])]"
    show ep02_escort03 with vpunch
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d050'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d051'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d052'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_room_noise3, "amb", 1, True, 2.5, 0)
    show ep02_escort04 with ccirclewipe
    $ playAudio(yakuza_theme, "music", 1, True, 2.5, 0)
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d053'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d054'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d055'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d056'])]"
    show ep02_escort05
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d057'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d058'])]"
    show ep02_escort06 with slowfade
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d059'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d060'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d061'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d062'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d063'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d064'])]"
    show ep02_escort07
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d065'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d066'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d067'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d068'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d069'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d070'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d071'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d072'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d073'])]"
    show ep02_escort08
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d074'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d075'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d076'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d077'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d078'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d079'])]"
    show ep02_escort09
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d080'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d081'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d082'])]" 
    show ep02_escort10
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d083'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d084'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d085'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d086'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d087'])]"
    show ep02_escort11
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d088'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d089'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d090'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d091'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d092'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d093'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d094'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d095'])]"
    show ep02_escort12
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d096'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d097'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ playAudio(sfx_heartbeatfast, "sfx", 1, True, 0.5, 0)
    show ep02_escort13 with vpunch
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d098'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d099'])]"
    arl_t "[renpy.substitute(dialogues2['E02ARLEHELL_d100'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d101'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d102'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ playAudio(sfx_femalerun, "sfx", 2, True, 0.5, 0)
    show ep02_escort14 with hpunch
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d103'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d104'])]"
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1)
    $ playAudio(sfx_punch, "sfx", 3, False, 0, 0)
    show ep02_escort15 with hpunch
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d105'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d106'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d107'])]"
    show ep02_escort16
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d108'])]"
    scene eigengrau with dissolve
    show ep02_escort17 with slowfade
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d109'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d110'])]"
    yaw "[renpy.substitute(dialogues2['E02ARLEHELL_d111'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d112'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEHELL_d113'])]"
    yas "[renpy.substitute(dialogues2['E02ARLEHELL_d114'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_nightroad, "amb", 4, True, 2.5, 0)
    $ playAudio(sfx_windyprairie, "amb", 5, True, 2.5, 0)
    show ep02_sadness1 with circlewipe
    mc_t "[renpy.substitute(dialogues2['E02ARLEHELL_d115'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEHELL_d116'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d117'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.4)
    $ playAudio(arlette_sad_theme, "music", 1, True, 2.5, 0)
    show ep02_sadness2 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d118'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d119'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d120'])]"
    show ep02_sadness3
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d121'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d122'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d123'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d124'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d125'])]"
    show ep02_sadness4
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d126'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d127'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d128'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d129'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d130'])]"
    mc_y "[renpy.substitute(dialogues2['E02ARLEHELL_d131'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d132'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d133'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d134'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d135'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d136'])]"
    show ep02_sadness5
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d137'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d138'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d139'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d140'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d141'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d142'])]"
    show ep02_sadness6
    arl "[renpy.substitute(dialogues2['E02ARLEHELL_d143'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEHELL_d144'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEHELL_d145'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEHELL_d146'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_lovemaking

label ep02_lovemaking:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=7, volume=0.2)
    $ playAudio(sfx_eveningtraffic, "amb", 7, True, 2.5, 0)
    show ep02_arlesex01 with ccirclewipe
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d001'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d002'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d003'])]"
    show ep02_arlesex02
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d004'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d005'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d006'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d007'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d008'])]"
    show ep02_arlesex03 with vpunch
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d009'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d010'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d011'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d012'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d013'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d014'])]"
    show ep02_arlesex04
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d015'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d016'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d017'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d018'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d019'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d020'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d021'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d022'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d023'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d024'])]"
    scene eigengrau with dissolve
    show ep02_arlesex05 with circlewipe
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d025'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d026'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d027'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d028'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d029'])]"
    show ep02_arlesex06 with vpunch
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d030'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d031'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d032'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d033'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d034'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d035'])]"
    show ep02_arlesex07 with hpunch
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d036'])]"
    mc_s "[renpy.substitute(dialogues['E01S24_d046'])]"
    mc_s "[renpy.substitute(dialogues['E01S24_d052'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d037'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d038'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d039'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d040'])]"
    show ep02_arlesex08
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d041'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d042'])]"
    show ep02_arlesex09
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d043'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d044'])]"
    $ show_walkthrough("ep02_arlesex_menu1")
    menu:
        "Agree":
            hide screen walkthrough_screen
            $ ep02_anal = True
            $ rm.update("arlette", "cor", 5)
            $ check_levels("arlette", "cor", 5)
            show ep02_arlesex10
            mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d045'])]"
        "Deny":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d127'])]"
    show ep02_arlesex11
    if ep02_anal:
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d046'])]"
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d047'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d128'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d129'])]"
        jump ep02_arlette_mc_story
    show ep02_arlesex12 with vpunch
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d048'])]"
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    $ playAudio(arlette_sexy_theme, "music", 1, True, 2.5, 0)
    show ep02_arlesex13
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d049'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d050'])]"
    show ep02_arlesex14
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d051'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d052'])]"
    show ep02_arlesex16 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d053'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d054'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d055'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d056'])]"
    show ep02_arlesex15 with vpunch
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d057'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d058'])]"
    show ep02_arlesex17
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d059'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d060'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d061'])]"
    show ep02_arlesex18
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d062'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d063'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d064'])]"
    show ep02_arlesex19
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d065'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d066'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d067'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d068'])]"
    $ show_walkthrough("ep02_arlesex_menu2")
    menu:
        "Talk dirty":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            $ ep02_talkdirty = True
            mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d069'])]"
            mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d070'])]"
        "Talk with love":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)
            pass
    show ep02_arlesex20
    if ep02_talkdirty:
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d071'])]"
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d072'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d073'])]"
    else:
        pass
    show ep02_arlesex21
    if ep02_talkdirty:
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d074'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d075'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d076'])]"
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d077'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d078'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d079'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d080'])]"
    else:
        pass
    show ep02_arlesex23
    if ep02_talkdirty:
        $ ep02_talkdirty = False
        $ show_walkthrough("ep02_arlesex_menu3")
        menu:
            "Keep talking dirty":
                hide screen walkthrough_screen
                $ rm.update("arlette", "cor", 2)
                $ check_levels("arlette", "cor", 2)
                $ ep02_talkdirty = True
                mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d081'])]"
                arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d082'])]"
            "Talk with love":
                hide screen walkthrough_screen
                $ rm.update("arlette", "trust", 1)
                $ check_levels("arlette", "trust", 1)
                pass
    else:
        $ show_walkthrough("ep02_arlesex_menu4")
        menu:
            "Talk dirty":
                hide screen walkthrough_screen
                $ rm.update("arlette", "cor", 1)
                $ check_levels("arlette", "cor", 1)
                $ ep02_talkdirty = True
                mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d081'])]"
                arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d082'])]"
            "Keep talking with love":
                hide screen walkthrough_screen
                $ rm.update("arlette", "trust", 2)
                $ check_levels("arlette", "trust", 2)
                pass
    show ep02_arlesex24
    if ep02_talkdirty:
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d085'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d086'])]"
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d087'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d088'])]"
    else:
        pass
    scene eigengrau with dissolve
    show ep02_arlesex25 with vpunch
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d089'])]"
    if ep02_talkdirty:
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d090'])]"
    else:
        pass
    show ep02_arlesex26
    if ep02_talkdirty:
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d091'])]"
        arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d092'])]"
        mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d093'])]"
    else:
        pass
    show ep02_arlesex27
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d094'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d095'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d096'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d097'])]"
    show ep02_arlesex28
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d098'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d099'])]"
    show ep02_arlesex29
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d100'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d101'])]"
    show ep02_arlesex30 with flash
    show white zorder 1.0 at ejaculation_flash
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d102'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d103'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d104'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d105'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d106'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d107'])]"
    show ep02_arlesex31
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d108'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d109'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d110'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d111'])]"
    show ep02_arlesex32
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d112'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d113'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d114'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d115'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d116'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d117'])]"
    show ep02_arlesex33
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d118'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d119'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d120'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d121'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d122'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d123'])]"
    $ show_walkthrough("ep02_arlesex_menu5")
    menu:
        mc_t "[renpy.substitute(dialogues2['E02LOVEMAKING_d124'])]"
        "Cum inside her":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)
            mc_s "[renpy.substitute(dialogues2['E02LOVEMAKING_d125'])]"
            arl "[renpy.substitute(dialogues2['E02LOVEMAKING_d126'])]"
            jump ep02_lovemaking_inside
        "Cum all over her ass":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            jump ep02_lovemaking_over

label ep02_lovemaking_inside:
    $ AddView("ep02_arlesex40", "ep02_arlesex41", "ep02_arlesex42")
    show screen camera_view with flash
    show white zorder 1.0 at ejaculation_flash
    arl "[renpy.substitute(dialogues2['E02LOVEMAKINS_d001'])]"
    $ show_custom_notification("multicam_tip")
    arl "[renpy.substitute(dialogues2['E02LOVEMAKINS_d002'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKINS_d003'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKINS_d004'])]"
    hide screen camera_view
    pause 1
    jump ep02_arlette_mc_story

label ep02_lovemaking_over:
    $ AddView("ep02_arlesex34", "ep02_arlesex35", "ep02_arlesex36")
    show screen camera_view
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d001'])]"
    $ show_custom_notification("multicam_tip")
    arl "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d002'])]"
    mc_s "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d003'])]"
    hide screen camera_view
    $ AddView("ep02_arlesex37", "ep02_arlesex38", "ep02_arlesex39")
    show screen camera_view with flash
    show white zorder 1.0 at ejaculation_flash
    arl "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d004'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d005'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d006'])]"
    arl "[renpy.substitute(dialogues2['E02LOVEMAKOVER_d007'])]"
    hide screen camera_view
    pause 1
    jump ep02_arlette_mc_story

label ep02_arlette_mc_story:
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(arlette_love_theme, "music", 1, True, 2.5, 0)
    show ep02_lovestory1 at concentrate with slowfade
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d002'])]"
    show ep02_lovestory2 at concentrate with flash
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d003'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d004'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d005'])]"
    show ep02_lovestory3 at concentrate with flash
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d006'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d007'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d008'])]"
    show ep02_lovestory4 at concentrate with flash
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d009'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d010'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d011'])]"
    show ep02_lovestory5 at concentrate with flash
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d012'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d013'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d014'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d015'])]"
    show ep02_lovestory6 at concentrate with flash
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d016'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d017'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d018'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d019'])]"
    show ep02_lovestory7 at concentrate with flash
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d020'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d021'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d022'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_nightclub, "amb", 1, True, 2.5, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2)
    $ playAudio(sfx_evenstreet, "amb", 2, True, 2.5, 0)
    show ep02_arlefight1 with slowfade
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d023'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d024'])]"
    show ep02_arlefight2
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d025'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d026'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d027'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d028'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d029'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d030'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d031'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d032'])]"
    show ep02_arlefight3
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d033'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d034'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d035'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d036'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d037'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d038'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d039'])]"
    $ playAudio(sfx_tablehit, "sfx", 1, False, 0, 0)
    show ep02_arlefight4 with vpunch
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d040'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d041'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d042'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d043'])]"
    show ep02_arlefight5
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d044'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d045'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d046'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d047'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d048'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d049'])]"
    rin "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d050'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.4)
    $ playAudio(sfx_mc_room_night, "amb", 3, True, 2.5, 0)
    $ playAudio(arlette_love_theme, "music", 1, True, 2.5, 0)
    show ep02_arledeath01 with slowfade
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d051'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d052'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d053'])]"
    show ep02_arledeath02
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d054'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d055'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d056'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d057'])]"
    show ep02_arledeath03
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d058'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d059'])]"
    $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d060'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.7, fade_duration=1.5)
    show ep02_arledeath04 with slowfade
    $ stopAudio(channel="sfx", subchannel=1, fadeout=0.5)
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d061'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d062'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d063'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d064'])]"
    $ playAudio(sfx_tablehit, "sfx", 1, False, 0, 0)
    show ep02_arledeath05 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d065'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d066'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d067'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d068'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d069'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d070'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d071'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d072'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d073'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d074'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d075'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d076'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d077'])]"
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    scene eigengrau with dissolve
    $ playAudio(arlette_nostalgia_theme, "music", 1, True, 2.5, 0)
    show ep02_arledeath06 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d078'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d079'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d080'])]"
    show ep02_arledeath07
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d081'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d082'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d083'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d084'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_windyprairie, "amb", 2, True, 2.5, 0)
    $ playAudio(sfx_birds1, "amb", 1, True, 2.5, 0)
    show ep02_arledeath08 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d085'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d086'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d087'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d088'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d089'])]"
    show ep02_arledeath09
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d090'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d091'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d092'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d093'])]"
    show ep02_arledeath10
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d094'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d095'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d096'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d097'])]"
    show ep02_arledeath11
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d098'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d099'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d100'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d101'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d102'])]"
    show ep02_arledeath12 with hpunch
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d103'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d104'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d105'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d106'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d107'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d108'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d109'])]"
    show ep02_arledeath13
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d110'])]"
    mc_s "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d111'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d112'])]"
    arl "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d113'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d078'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d115'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d116'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep02_arledeath14 with slowfade
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d117'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d118'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d119'])]"
    mc_t "[renpy.substitute(dialogues2['E02ARLEMCSTORY_d120'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ resetAllVolumes()
    jump ep02_revenge_night

label ep02_revenge_night:
    scene eigengrau with dissolve 
    $ playAudio(sfx_nightroad, "amb", 1, True, 2.5, 0)
    show ep02_revenge01 at concentrate with circlewipe
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d001'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d002'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d003'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d004'])]"
    show ep02_revenge02 at concentrate
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d005'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d006'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d007'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d008'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(mc_broken_theme, "music", 1, True, 2.5, 0)
    scene eigengrau with dissolve 
    show ep02_revenge03 with circlewipe
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d009'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d010'])]"
    show ep02_revenge04 with flash
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d011'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d012'])]"
    show ep02_revenge05 with flash
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d013'])]"
    $ playAudio(sfx_slamdoorhard, "sfx", 1, False, 0, 0)
    show ep02_revenge06 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d014'])]"
    $ stopAllSubchannels(channel="music", fadeout=4)
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_extnight, "amb", 1, True, 2.5, 0)
    $ playAudio(sfx_heartbeatslow, "sfx", 2, True, 4, 0)
    hid "[renpy.substitute(dialogues2['E02REVENGE_d015'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d016'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d017'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d018'])]"
    show ep02_revenge07
    hid "[renpy.substitute(dialogues2['E02REVENGE_d019'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d020'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d021'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d022'])]"
    menu ep02_shootingcheck:
        "Check left" if not ep02_checkleft:
            $ ep02_checkleft = True
            jump ep02_shootleft
        "Check right" if not ep02_checkright:
            $ ep02_checkright = True
            jump ep02_shotright
        "Check back" if not ep02_checkback:
            $ ep02_checkback = True
            jump ep02_shootback
    
    label ep02_shotright:
    show ep02_revenge09 with dissolve
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d023'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d024'])]"
    if ep02_checkleft and ep02_checkright and ep02_checkback:
        jump ep02_shootcontinue
    else:
        jump ep02_shootingcheck

    label ep02_shootback:
    show ep02_revenge10 with dissolve
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d025'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d026'])]"
    show ep02_revenge08
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d027'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d028'])]"
    if ep02_checkleft and ep02_checkright and ep02_checkback:
        jump ep02_shootcontinue
    else:
        jump ep02_shootingcheck

    label ep02_shootleft:
    show ep02_revenge11 with dissolve
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d029'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d030'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d031'])]"
    if ep02_checkleft and ep02_checkright and ep02_checkback:
        jump ep02_shootcontinue
    else:
        jump ep02_shootingcheck

    label ep02_shootcontinue:
    show ep02_revenge12 with hpunch
    hid "[renpy.substitute(dialogues2['E02REVENGE_d032'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d033'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d034'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d035'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d036'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d037'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d038'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d039'])]"
    $ playAudio(sfx_tablehit, "sfx", 1, False, 0, 0)
    show ep02_revenge13 with vpunch
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d040'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d041'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d042'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d043'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d044'])]"
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1.5)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(mc_suspense_theme, "music", 2, True, 2.5, 0)
    $ playAudio(sfx_heartbeatfast, "sfx", 3, True, 2.5, 0)
    show ep02_revenge14 with hpunch
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d045'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d046'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d047'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d048'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d049'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d050'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d051'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d052'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d053'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d054'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d055'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d056'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d057'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d058'])]"
    show ep02_revenge15
    rin "[renpy.substitute(dialogues2['E02REVENGE_d059'])]"
    rin "[renpy.substitute(dialogues2['E02REVENGE_d060'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d061'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d062'])]"
    rin "[renpy.substitute(dialogues2['E02REVENGE_d063'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d064'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d065'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d066'])]"
    rin "[renpy.substitute(dialogues2['E02REVENGE_d067'])]"
    show ep02_revenge16
    hid "[renpy.substitute(dialogues2['E02REVENGE_d068'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d069'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d070'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d071'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d072'])]"
    hid "[renpy.substitute(dialogues2['E02REVENGE_d073'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d074'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d075'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d076'])]"
    
    $ show_walkthrough("ep02_revenge_menu1")
    menu:
        mc_t "[renpy.substitute(dialogues2['E02REVENGE_d077'])]"
        "Walk away":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 5)
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d078'])]"
            $ stopAllSubchannels(channel="sfx", fadeout=1.5)
            $ stopAllSubchannels(channel="music", fadeout=2.5)
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d079'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d080'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d081'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d082'])]"
            hid "[renpy.substitute(dialogues2['E02REVENGE_d083'])]"
        "Attack him": 
            hide screen walkthrough_screen
            $ ep02_shootout = True
            $ rm.update("mc", "integrity", -5)
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d084'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d085'])]"
            $ stopAllSubchannels(channel="sfx", fadeout=3.5)
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d086'])]"
            hid "[renpy.substitute(dialogues2['E02REVENGE_d087'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d088'])]"
            hid "[renpy.substitute(dialogues2['E02REVENGE_d089'])]"
            hid "[renpy.substitute(dialogues2['E02REVENGE_d090'])]"
    show ep02_revenge17
    if ep02_shootout:
        yaw "[renpy.substitute(dialogues2['E02REVENGE_d091'])]"
        rin "[renpy.substitute(dialogues2['E02REVENGE_d092'])]"
        mc_s "[renpy.substitute(dialogues2['E02REVENGE_d093'])]"
        $ stopAllSubchannels(channel="music", fadeout=2.5)
        show ep02_revenge17 with vpunch
        yaw "[renpy.substitute(dialogues2['E02REVENGE_d094'])]"
        $ playAudio(mc_action_theme, "music", 1, True, 2.5, 0)
        mc_t "[renpy.substitute(dialogues2['E02REVENGE_d095'])]"
    else:
        yaw "[renpy.substitute(dialogues2['E02REVENGE_d096'])]"
        rin "[renpy.substitute(dialogues2['E02REVENGE_d097'])]"
        mc_s "[renpy.substitute(dialogues2['E02REVENGE_d098'])]"
        jump ep02_consequences
    show ep02_revenge18 with hpunch
    $ playAudio(sfx_bedmove2, "sfx", 1, False, 0, 0)
    $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)
    $ playAudio(sfx_sofa_move, "sfx", 3, False, 0, 0)
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d099'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d100'])]"
    yaw "[renpy.substitute(dialogues2['E02REVENGE_d101'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d102'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d103'])]"
    $ playAudio(sfx_gunshots_glock, "sfx", 4, False, 0, 0)
    show ep02_revenge19 with hpunch
    rin "[renpy.substitute(dialogues2['E02REVENGE_d104'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d105'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d106'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d107'])]"
    show ep02_revenge20
    hid "[renpy.substitute(dialogues2['E02REVENGE_d108'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02REVENGE_d156'])]"
    $ playAudio(sfx_gunshot_beretta, "sfx", 5, False, 0, 0)
    show ep02_revenge21 with vpunch
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d109'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d110'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d111'])]"
    $ playAudio(sfx_gunshots_glock, "sfx", 4, False, 0, 0)
    show ep02_revenge22 with vpunch
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d112'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d113'])]"
    $ playAudio(sfx_celldoor, "sfx", 1, False, 0, 0)
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d114'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve 
    show ep02_revenge23 with circlewipe
    $ playAudio(sfx_hallwalkmale, "sfx", 2, True, 1, 0)
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d115'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d116'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d117'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d118'])]"
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1)
    show ep02_revenge24
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d119'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d120'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d121'])]"
    rin "[renpy.substitute(dialogues2['E02REVENGE_d122'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d123'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d124'])]"
    $ setChannelVolume(channel="music", subchannel=3, volume=0.5)
    $ playAudio(mc_suspense_theme, "music", 3, True, 2.5, 0)
    show ep02_revenge25
    rin "[renpy.substitute(dialogues2['E02REVENGE_d125'])]"
    rin "[renpy.substitute(dialogues2['E02REVENGE_d126'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d127'])]"
    mc_t "[renpy.substitute(dialogues2['E02REVENGE_d128'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d129'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d130'])]"
    mc_s "[renpy.substitute(dialogues2['E02REVENGE_d131'])]"
    $ show_walkthrough("ep02_revenge_menu2")
    menu:
        "Threaten her":
            hide screen walkthrough_screen
            $ ep02_hitrina = True
            $ rm.update("mc", "integrity", -2)
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d132'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d133'])]"
            rin "[renpy.substitute(dialogues2['E02REVENGE_d134'])]"
            $ playAudio(sfx_bodygrab, "sfx", 1, False, 0, 0)
            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)
            show ep02_revenge26 with hpunch
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d135'])]"
            rin "[renpy.substitute(dialogues2['E02REVENGE_d136'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d137'])]"
            rin "[renpy.substitute(dialogues2['E02REVENGE_d138'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d139'])]"
            rin "[renpy.substitute(dialogues2['E02REVENGE_d140'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d141'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d142'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d143'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d144'])]"
            $ playAudio(sfx_bodygrab, "sfx", 1, False, 0, 0)
            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)
            show ep02_revenge26 with hpunch
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d145'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d146'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d147'])]"
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
        "Let her go":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 2)
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d148'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d149'])]"
            rin "[renpy.substitute(dialogues2['E02REVENGE_d134'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d132'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d133'])]"
            mc_t "[renpy.substitute(dialogues2['E02REVENGE_d153'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d154'])]"
            mc_s "[renpy.substitute(dialogues2['E02REVENGE_d155'])]"
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_consequences

label ep02_consequences:
    scene eigengrau with dissolve
    $ resetAllVolumes()
    $ playAudio(sfx_eveningtraffic, "amb", 1, True, 2.5, 0)
    show ep02_aftermath01 with slowfade
    if ep02_shootout:
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d001'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d002'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d003'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d004'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d005'])]"
    else:
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d006'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d007'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d008'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d009'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d010'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d011'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d012'])]"
    $ stopAudio(channel="amb", subchannel=1, fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.35)
    $ playAudio(sfx_evenbalcony, "amb", 2, True, 2.5, 00)
    show ep02_aftermath02 with ccirclewipe
    if ep02_shootout:
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d013'])]"
        $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d014'])]"
    else: 
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d015'])]"
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d016'])]"
        $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)
        mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d017'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    show ep02_aftermath03
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d018'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d019'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d020'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d021'])]"
    show ep02_aftermath04
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d022'])]"
    $ show_walkthrough("ep02_aftermath_menu1")
    menu:
        "Everything's over...":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 2)
            $ check_levels("paz", "trust", 2)
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d023'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d024'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d025'])]"
        "I screwed up bad":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 1)
            $ check_levels("paz", "trust", 1)
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d026'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d027'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d028'])]"
        "I'm done, Paz":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d029'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d030'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d031'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6)
    $ playAudio(sfx_eveningtraffic, "amb", 3, True, 1, 0)
    show ep02_aftermath05
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d032'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d033'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d034'])]"
    show ep02_aftermath06
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d035'])]"
    $ show_walkthrough("ep02_aftermath_menu2")
    menu:
        "Don't--":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d036'])]"
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d037'])]"
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d038'])]"
        "I need you, Paz.":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 1)
            $ check_levels("paz", "trust", 1)
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d039'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d040'])]"
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d041'])]"
        "I said stay away!":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", -1)
            $ check_levels("paz", "trust", -1)
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d042'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d043'])]"
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d044'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d045'])]"
    $ stopAudio(channel="amb", subchannel=3, fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    show ep02_aftermath07 with ccirclewipe
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d046'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d047'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d048'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d049'])]"
    show ep02_aftermath08
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d050'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d051'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d052'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d053'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_eveningtraffic, "amb", 3, True, 2.5, 0)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.5)
    $ playAudio(mc_theme, "music", 3, True, 2.5, 0)
    show ep02_aftermath09 with ccirclewipe
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d054'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d055'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d056'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d057'])]"
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.1, fade_duration=1)
    show ep02_aftermath10
    if ep02_shootout:
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d058'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d059'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d060'])]"
        mc_y "[renpy.substitute(dialogues2['E02CONSEQ_d061'])]"
        mc_y "[renpy.substitute(dialogues2['E02CONSEQ_d062'])]"
    else:
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d063'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d059'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d065'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d066'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d067'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d068'])]"
    show ep02_aftermath11
    if ep02_shootout:
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d069'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d070'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d071'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d072'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d073'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d074'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d075'])]"
    else:
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d076'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d077'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d078'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d079'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d080'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d081'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d082'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d083'])]"
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6, fade_duration=1)
    $ playAudio(sfx_car_racing, "sfx", 1, False, 1, 0)
    show ep02_aftermath12 with hpunch
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d084'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d085'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d086'])]"
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.1, fade_duration=1)
    show ep02_aftermath13
    $ show_walkthrough("ep02_aftermath_menu3")
    menu:
        "I couldn't let her stay":
            hide screen walkthrough_screen
            $ ep02_distraction = False
            $ rm.update("mc", "integrity", 1)
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d087'])]"
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d088'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d089'])]"
            pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d090'])]"
        "I needed a distraction":
            hide screen walkthrough_screen
            $ ep02_distraction = True
            $ rm.update("mc", "integrity", -1)
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d091'])]"
            mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d092'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d093'])]"
            pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d094'])]"
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6, fade_duration=1)
    show ep02_aftermath14
    if ep02_distraction:
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d095'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d096'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d097'])]"
        pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d098'])]"
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d099'])]"
    show ep02_aftermath15
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d100'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d101'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d102'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d103'])]"
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.1, fade_duration=1)
    show ep02_aftermath16
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d104'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d105'])]"
    if ep02_distraction:
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d106'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d107'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d108'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d109'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d110'])]"
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6, fade_duration=1)
    $ playAudio(sfx_cardoor_open, "sfx", 1, False, 0, 0)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 3, False, 0, 0)
    show ep02_aftermath17 with hpunch
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d111'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d112'])]"
    if ep02_distraction:
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d113'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d114'])]"
    show ep02_aftermath18 with vpunch
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d115'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d116'])]"
    $ playAudio(sfx_carcrash, "sfx", 5, False, 0, 0)
    show ep02_aftermath19
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d117'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d118'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d119'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d120'])]"
    $ playAudio(sfx_car_driveaway, "sfx", 1, False, 0, 0)
    show ep02_aftermath20
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d121'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d122'])]"
    pa_s "[renpy.substitute(dialogues2['E02CONSEQ_d123'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d124'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d125'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="music", subchannel=2, volume=0.7)
    $ playAudio(mc_broken_theme, "music", 2, True, 2.5, 0)
    $ playAudio(sfx_car_idle_to_off, "amb", 4, False, 2.5, 1.5)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 2.5, 0)
    $ playAudio(sfx_extnight, "amb", 2, True, 2.5, 0)
    show ep02_aftermath21 with slowfade
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d126'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d127'])]"
    show ep02_aftermath23
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d128'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d129'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d130'])]"
    $ show_walkthrough("ep02_aftermath_menu3")
    menu:
        "I did what was right.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 1)
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d131'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d132'])]"
            hid "[renpy.substitute(dialogues2['E02CONSEQ_d133'])]"
        "Yeah, I'm a fucking idiot.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -1)
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d134'])]"
            mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d135'])]"
            hid "[renpy.substitute(dialogues2['E02CONSEQ_d136'])]"
    show ep02_aftermath22
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d137'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d138'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d139'])]"
    $ playAudio(sfx_guncock9mm, "sfx", 1, False, 0, 0)
    show screen mcpov_dying
    show ep02_aftermath24 with vpunch
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d140'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d141'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d142'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d143'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d144'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d145'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d146'])]"
    scene eigengrau with dissolve
    $ playAudio(sfx_cardoor_open, "sfx", 2, False, 0, 0)
    show ep02_aftermath25 with slowfade
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d147'])]"
    $ playAudio(sfx_guncock9mm, "sfx", 3, False, 0, 0)
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d148'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d149'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d150'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d151'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d152'])]"
    hid "[renpy.substitute(dialogues2['E02CONSEQ_d153'])]"
    $ playAudio(sfx_gunshot_beretta, "sfx", 5, False, 0, 0)
    scene eigengrau with dissolve
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)
    show ep02_aftermath26 with slowfade
    $ playAudio(sfx_footsteps_heelstile, "sfx", 7, True, 0, 0)
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d154'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d155'])]"
    $ stopAudio(channel="sfx", subchannel=7, fadeout=1)
    scene eigengrau with dissolve
    show ep02_aftermath27 with slowfade
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d156'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d157'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d158'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d159'])]"
    show ep02_aftermath28
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d160'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d161'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d162'])]"
    mc_t "[renpy.substitute(dialogues2['E02CONSEQ_d163'])]"
    show ep02_aftermath29
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d164'])]"
    mc_s "[renpy.substitute(dialogues2['E02CONSEQ_d165'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d166'])]"
    "Bodyguard" "[renpy.substitute(dialogues2['E02CONSEQ_d167'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    hide screen mcpov_dying
    jump ep02_arlette_breakup

label ep02_arlette_breakup:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.2)
    $ playAudio(sfx_hospital_hall, "amb", 1, True, 2.5, 1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_midnightpast, "amb", 2, True, 2.5, 1)
    show ep02_breakup1 with slowfade
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d001'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d002'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d003'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d004'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d005'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d006'])]"
    show ep02_breakup2
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d007'])]"
    if ep02_hitrina:
        mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d008'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d009'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d010'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.7)
    $ playAudio(arlette_nostalgia_theme, "music", 1, True, 1, 0)
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d011'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d012'])]"
    if ep02_shootout:
        mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d013'])]"
    else: 
        mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d014'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d015'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d016'])]"
    if ep02_shootout:
        mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d017'])]"
    else:
        mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d018'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d019'])]"
    show ep02_breakup3
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d020'])]"
    $ show_walkthrough("ep02_breakup_menu1")
    menu:
        "I'd do anything for you.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d021'])]"
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d022'])]"
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d023'])]"
            arl "[renpy.substitute(dialogues2['E02BREAKUP_d024'])]"
        "I had to protect you.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 2)
            $ check_levels("arlette", "trust", 2)
            $ rm.update("mc", "integrity", 1)
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d025'])]"
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d026'])]"
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d027'])]"
            arl "[renpy.substitute(dialogues2['E02BREAKUP_d028'])]"
        "It needed to be done.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -2)
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d029'])]"
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d030'])]"
            mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d031'])]"
            arl "[renpy.substitute(dialogues2['E02BREAKUP_d032'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d033'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d034'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d035'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d036'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d037'])]"
    show ep02_breakup4
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d038'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d039'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d040'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d041'])]"
    mc_s "[renpy.substitute(dialogues2['E02BREAKUP_d042'])]"
    arl "[renpy.substitute(dialogues2['E02BREAKUP_d043'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_breakup5 at concentrate with circlewipe
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d044'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d045'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d046'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d047'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d048'])]"
    show ep02_breakup6
    if htl_episodes == 2:
        $ show_custom_notification("save_tip")
    else:
        pass
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d049'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d050'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d051'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d052'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d053'])]"
    scene eigengrau with dissolve
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    show ep02_breakup7 with slowfade
    isa "[renpy.substitute(dialogues2['E02BREAKUP_d056'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d054'])]"
    mc_t "[renpy.substitute(dialogues2['E02BREAKUP_d055'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=1)
    $ update_htl_episodes()
    call hideNoise(transition=dissolve)
    #-- End Episode 2
    if htl_episodes == 2:
        return
    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep03_title