label ep03_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ renpy.block_rollback()
    jump ep03_isatalk
## -- INTRO SCENE HOME

label ep03_isatalk:
    call showNoise(0.1, 0.15, transition=dissolve)
    show ep03_backtohome01 with slowfade
    $ config.rollback_enabled = True
    show screen stats_button
    show screen walkthrough_icon
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    isa "[renpy.substitute(dialogues3['E03ISATALK_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d002'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d003'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d004'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d005'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d006'])]"
    $ playAudio(sfx_bedmove4, "sfx", 1, False, 0, 0)
    show ep03_backtohome02
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d007'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d008'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d009'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d010'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d011'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d012'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d013'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(isabella_sad, "music", 1, True, 0, 0)
    show ep03_backtohome03 at camera_zoom
    isa "[renpy.substitute(dialogues3['E03ISATALK_d014'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d015'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d016'])]"
    show ep03_backtohome04
    isa "[renpy.substitute(dialogues3['E03ISATALK_d017'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d018'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d019'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d020'])]"
    show ep03_backtohome05
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d021'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d022'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d023'])]"
    show ep03_backtohome06
    isa "[renpy.substitute(dialogues3['E03ISATALK_d024'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d025'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d026'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d027'])]"
    show ep03_backtohome07
    isa "[renpy.substitute(dialogues3['E03ISATALK_d028'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d029'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d030'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d031'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d032'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d033'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d034'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d035'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d036'])]"
    $ playAudio(sfx_drop_ontable, "sfx", 2, False, 0, 0)
    show ep03_backtohome08
    mc_t "[renpy.substitute(dialogues3['E03ISATALK_d037'])]"
    show ep03_backtohome09
    isa "[renpy.substitute(dialogues3['E03ISATALK_d038'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d039'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d040'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d041'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d042'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d043'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d044'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.4)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
    show ep03_backtohome10 with dissolve
    isa "[renpy.substitute(dialogues3['E03ISATALK_d045'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISATALK_d046'])]"
    show ep03_backtohome14
    mc_t "[renpy.substitute(dialogues3['E03ISATALK_d047'])]"
    isa "[renpy.substitute(dialogues3['E03ISATALK_d048'])]"
    mc_t "[renpy.substitute(dialogues3['E03ISATALK_d049'])]"
    show ep03_backtohome11
    isa "[renpy.substitute(dialogues3['E03ISATALK_d050'])]"
    $ show_walkthrough("ep03_isahug_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03ISATALK_d051'])]"
        "Comfort Isabella with a hug":
            hide screen walkthrough_screen
            $ ep03_isahug = True
            $ rm.update("isabella", "trust", 5)
            $ check_levels("isabella", "trust", 5)
            isa "[renpy.substitute(dialogues3['E03ISATALK_d052'])]"
            mc_s "[renpy.substitute(dialogues3['E03ISATALK_d053'])]"
            jump ep03_isatalk_hug
        "Give Isabella a reassuring pat on the head":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", 1)
            $ check_levels("isabella", "trust", 1)
            isa "[renpy.substitute(dialogues3['E03ISATALK_d054'])]"
            jump ep03_isatalk_nohug

label ep03_isatalk_hug:
    show ep03_backtohome12 with hpunch
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d002'])]"
    show ep03_backtohome16
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d003'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d004'])]"
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d005'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d006'])]"
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d007'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d008'])]"
    show ep03_backtohome18
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d009'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d010'])]"
    jump ep03_isatalk_end

label ep03_isatalk_nohug:
    show ep03_backtohome13 with vpunch
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d011'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d012'])]"
    show ep03_backtohome17
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d013'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d014'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAHUG_d015'])]"
    show ep03_backtohome16
    isa "[renpy.substitute(dialogues3['E03ISAHUG_d016'])]"
    jump ep03_isatalk_end

label ep03_isatalk_end:
    show ep03_backtohome19
    isa "[renpy.substitute(dialogues3['E03ISAEND_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAEND_d002'])]"
    isa "[renpy.substitute(dialogues3['E03ISAEND_d003'])]"
    isa "[renpy.substitute(dialogues3['E03ISAEND_d004'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAEND_d005'])]"
    show ep03_backtohome20
    isa "[renpy.substitute(dialogues3['E03ISAEND_d006'])]"
    isa "[renpy.substitute(dialogues3['E03ISAEND_d007'])]"
    isa "[renpy.substitute(dialogues3['E03ISAEND_d008'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAEND_d009'])]"
    isa "[renpy.substitute(dialogues3['E03ISAEND_d010'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAEND_d011'])]"
    isa "[renpy.substitute(dialogues3['E03ISAEND_d012'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAEND_d013'])]"
    show ep03_backtohome21
    isa "[renpy.substitute(dialogues3['E03ISAEND_d014'])]"
    mc_s "[renpy.substitute(dialogues3['E03ISAEND_d015'])]"
    mc_t "[renpy.substitute(dialogues3['E03ISAEND_d016'])]"
    mc_t "[renpy.substitute(dialogues3['E03ISAEND_d017'])]"
    $ stopAllSubchannels(channel="music", fadeout=2.5)
    $ stopAllSubchannels(channel="amb", fadeout=2)
    $ stopAllSubchannels(channel="sfx", fadeout=2)
    jump ep03_antodream

label ep03_antodream:
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    show ep03_antodream01 with slowfade
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d001'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d002'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d003'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d004'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d005'])]"
    show ep03_antodream02
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d006'])]"
    show screen mcpov_dying
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d007'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d008'])]"
    #begins transition to dream
    hide screen mcpov_dying
    $ stopAudio(channel="amb", subchannel=1, fadeout=1)
    scene eigengrau with clouds_inverse
    pause 1
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.7)
    $ playAudio(sfx_windyprairie, "amb", 2, True, 1.5, 0)
    show ep03_antodream03 with slowfade
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d009'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d010'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.8)
    $ playAudio(antonella_love, "music", 1, True, 1.5, 0)
    show ep03_antodream04
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d011'])]"
    show ep03_antodream05
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d012'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d013'])]"
    show ep03_antodream06
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d014'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d015'])]"
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d016'])]"
    show ep03_antodream07
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d017'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d018'])]"
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d019'])]"
    mc_t "[renpy.substitute(dialogues3['E03ANTODREAM_d020'])]"
    #roll
    show ep03_antodream08 at slow_pan with vpunch
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d021'])]"
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d022'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d023'])]"
    #end roll
    show ep03_antodream09
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d024'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d025'])]"
    show ep03_antodream10
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d026'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d027'])]"
    show ep03_antodream11
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d028'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=1, volume=0, fade_duration=1)
    $ playAudio(sfx_glitch, "sfx", 1, True, 1, 0)
    show ep03_antodream11 at animated_glitch
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d029'])]"
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d030'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d031'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.8, fade_duration=1)
    show ep03_antodream12 with vpunch
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d032'])]"
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d033'])]"
    show ep03_antodream13
    mc_s "[renpy.substitute(dialogues3['E03ANTODREAM_d034'])]"
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d035'])]"
    $ stopAudio(channel="music", subchannel=1, fadeout=2.5)
    show ep03_antodream14 with hpunch
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d036'])]"
    anto "[renpy.substitute(dialogues3['E03ANTODREAM_d037'])]"
    #end dream
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    jump ep03_madtalk

label ep03_madtalk:
    scene eigengrau with clouds
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    show ep03_ambertalk01 with slowfade
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d001'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d002'])]"
    show ep03_ambertalk02
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d003'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d004'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d005'])]"
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)
    show ep03_madtalk01 with circlewipe
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d006'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d007'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d008'])]"
    show ep03_madtalk02
    show screen mcpov_dying
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d009'])]"
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    hide screen mcpov_dying
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=3)
    $ playAudio(sfx_bed_sitdown, "sfx", 1, False, 1, 0)
    show ep03_madtalk03 with slowfade
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d010'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d011'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d012'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d013'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d014'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.6)
    $ playAudio(madison_theme, "music", 2, True, 2.5, 0)
    show ep03_madtalk04
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d015'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d016'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d017'])]"
    $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)
    show ep03_madtalk05 with hpunch
    $ rm.set_knows("madison", True)
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d018'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d019'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d020'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d021'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d022'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d023'])]"
    show ep03_madtalk06
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d024'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d025'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d026'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d027'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d028'])]"
    show ep03_madtalk07 at camera_zoom
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d029'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d030'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d031'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d032'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d033'])]"
    show ep03_madtalk08
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d034'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d035'])]"
    mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d036'])]"
    mad "[renpy.substitute(dialogues3['E03MADISONTALK_d037'])]"
    $ show_walkthrough("ep03_maddie_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d038'])]"
        "Admit that Madison is attractive":
            hide screen walkthrough_screen
            $ ep03_madtalk = True
            $ rm.update("madison", "trust", 5)
            $ check_levels("madison", "trust", 5)
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d039'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d040'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d041'])]"
            mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d042'])]"
            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)
            show ep03_madtalk09 with vpunch
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d043'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d044'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d045'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d046'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d047'])]"
            mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d048'])]"
            mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d049'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d050'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d051'])]"
            show ep03_madtalk10
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d052'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d053'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d054'])]"
        "Deny finding Madison attractive":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d055'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d056'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d057'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d058'])]"
            mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d042'])]"
            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)
            show ep03_madtalk11 with vpunch
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d060'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d061'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d062'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d063'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d064'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d065'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d066'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d067'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d068'])]"
            show ep03_madtalk12
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d069'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d070'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d071'])]"
            mad "[renpy.substitute(dialogues3['E03MADISONTALK_d072'])]"
            mc_s "[renpy.substitute(dialogues3['E03MADISONTALK_d073'])]"
    mc_t "[renpy.substitute(dialogues3['E03MADISONTALK_d074'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_reunion

label ep03_reunion:
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    show ep03_ambertalk03 with slowfade
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d001'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d002'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d003'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d004'])]"
    show ep03_ambertalk04
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d005'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d006'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d007'])]"
    show ep03_ambertalk04 with hpunch
    mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d008'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.7)
    $ playAudio(amber_2nd_theme, "music", 1, True, 2.5, 0)
    show ep03_ambertalk05 with dissolve
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d009'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d010'])]"
    show ep03_ambertalk06
    $ rm.set_knows("amber", True)
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d011'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d012'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d013'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d014'])]"
    show ep03_ambertalk07
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d015'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d016'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d017'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d018'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d019'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d020'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d021'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d022'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d023'])]"
    show ep03_ambertalk08 with slowfade
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d024'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d025'])]"
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d026'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d027'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d028'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d029'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d030'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d031'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d026'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d033'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d034'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d035'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d036'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d037'])]"
        if ep01_lieamber:
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d038'])]"
        else:
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d039'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d040'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d041'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d042'])]"
    show ep03_ambertalk09
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d043'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d044'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d045'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d046'])]"
    $ show_walkthrough("ep03_ambertits_menu")
    menu:
        "Focus on Amber's breasts":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ ep03_ambertits = True
            show ep03_ambertalk10 at zoom_in with dissolve
            mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d047'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d048'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d049'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d050'])]"
        "Listen to what Amber is saying":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d051'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d052'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d053'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d054'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d055'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d056'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d057'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d058'])]"
    show ep03_ambertalk11
    if ep03_ambertits:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d059'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d060'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d061'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d062'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d063'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d064'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d065'])]"
    show ep03_ambertalk12
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d066'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d067'])]"
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d068'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d069'])]"
    show ep03_ambertalk13
    amb "[renpy.substitute(dialogues3['E03AMBREUNION_d070'])]"
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d071'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d072'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d073'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d074'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d075'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d076'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d077'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d078'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d079'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d080'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d081'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d010'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d083'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d084'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d085'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d086'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d087'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d088'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d089'])]"
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d090'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d091'])]"
    show ep03_ambertalk14
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d092'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBREUNION_d093'])]"
    $ show_walkthrough("ep03_amberfeels_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03AMBREUNION_d094'])]"
        "Listen to Amber's feelings":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d095'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d096'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d097'])]"
            $ stopAllSubchannels(channel="music", fadeout=2)
            jump ep03_reunion_stay1
        "Refuse to hear Amber out":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ ep03_amberleft = True
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d098'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBREUNION_d099'])]"
            amb "[renpy.substitute(dialogues3['E03AMBREUNION_d100'])]"
            $ stopAudio(channel="music", subchannel=1, fadeout=4)
            jump ep03_reunion_left

label ep03_reunion_stay1:
    scene eigengrau with dissolve
    pause 1
    show ep03_ambertalk15 with slowfade
    mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d001'])]"
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d002'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d003'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d004'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d005'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d006'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d007'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d008'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d009'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d010'])]"
    show ep03_ambertalk16
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d011'])]"
        if ep01_first:
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d012'])]"
        else:
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d013'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d014'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d015'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d016'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d017'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d018'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d019'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d020'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d021'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 4, 0)
    show ep03_ambertalk17 with vpunch
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d022'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d023'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d024'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d025'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d026'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d027'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d028'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d029'])]"
    show ep03_ambertalk19
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d030'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d031'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d032'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d033'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d034'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d035'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d036'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d037'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d038'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d039'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d040'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d041'])]"
    show ep03_ambertalk18
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d042'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d043'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d044'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d045'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d046'])]"
    show ep03_ambertalk20
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d047'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d048'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d049'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d050'])]"
    show ep03_ambertalk21
    if ep01_amblove:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d051'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d052'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d053'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d054'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d055'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d056'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d057'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d058'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d059'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d060'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d061'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d062'])]"
    show ep03_ambertalk22
    amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d063'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d064'])]"
    amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d065'])]"
    amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d066'])]"
    $ show_walkthrough("ep03_amberstaygo_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03AMBERSTAY_d067'])]"
        "Tell her to stay":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d068'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d069'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d070'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d071'])]"
            jump ep03_reunion_stay2
        "Tell her to leave":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ ep03_amberleft = True
            $ ep03_amberpastbehind = True
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d072'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d073'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d074'])]"
            show ep03_ambertalk23 with hpunch
            mc_t "[renpy.substitute(dialogues3['E03AMBERSTAY_d075'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d076'])]"
            show ep03_ambertalk24
            mc_t "[renpy.substitute(dialogues3['E03AMBERSTAY_d077'])]"
            show ep03_ambertalk25 with vpunch
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d078'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d079'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d080'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d081'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d082'])]"
            $ stopAllSubchannels(channel="music", fadeout=2)
            show ep03_ambertalk27 with slowfade
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d083'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d084'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d085'])]"
            show ep03_ambertalk28
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d086'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d087'])]"
            show ep03_ambertalk29
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d088'])]"
            show ep03_ambertalk30 with vpunch
            amb "[renpy.substitute(dialogues3['E03AMBERSTAY_d089'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERSTAY_d090'])]"
            jump ep03_reunion_left

label ep03_reunion_stay2:
    show ep03_ambertalk31 with vpunch
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d002'])]"
    show ep03_ambertalk32
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d003'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d004'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d005'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d006'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d007'])]"
    show ep03_ambertalk33
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d008'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d009'])]"
    show ep03_ambertalk34
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d010'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d011'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d012'])]"
    $ stopAllSubchannels(channel="music", fadeout=3)
    show ep03_ambertalk35
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d013'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d014'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d015'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d016'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d017'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d018'])]"
    show ep03_ambertalk36
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d019'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d020'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d021'])]"
    show ep03_ambertalk37
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d022'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d023'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d024'])]"
    show ep03_ambertalk38
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d025'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d026'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d027'])]"
    show ep03_ambertalk39
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d028'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d029'])]"
    show ep03_ambertalk40
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d030'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d031'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d032'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d033'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d034'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d035'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d036'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d037'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(amber_theme, "music", 1, True, 3, 0)
    show ep03_ambertalk41 with vpunch
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d038'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d039'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d040'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d041'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d042'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d043'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d044'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d045'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d046'])]"
    show ep03_ambertalk42
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d047'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d048'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d049'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d050'])]"
    mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d051'])]"
    amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d052'])]"
    $ show_walkthrough("ep03_amberinvpool_menu")
    menu:
        "Accompany Amber to the pool":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            $ ep03_talkaboutpast = True
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d053'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d054'])]"
            $ stopAllSubchannels(channel="music", fadeout=2)
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            $ stopAllSubchannels(channel="sfx", fadeout=1)
            jump ep03_poolnight
        "Decline Amber's invitation to the pool":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -15)
            $ check_levels("amber", "trust", -15)
            $ ep03_amberstrike = True
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d055'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d056'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d057'])]"
            $ stopAllSubchannels(channel="music", fadeout=2)
            show ep03_ambertalk51 with hpunch
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d058'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d059'])]"
            show ep03_ambertalk52
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d060'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d061'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d062'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d063'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d064'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d065'])]"
            show ep03_ambertalk53
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d066'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d067'])]"
            show ep03_ambertalk54
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d068'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d069'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d070'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d071'])]"
            show ep03_ambertalk55
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d072'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d073'])]"
            show ep03_ambertalk56
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d074'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d075'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d076'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d077'])]"
            show ep03_ambertalk57
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d078'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d079'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d080'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d081'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d082'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d083'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d084'])]"
            show ep03_ambertalk58
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d085'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d086'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d087'])]"
            show ep03_ambertalk59
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d088'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d089'])]"
            show ep03_ambertalk60
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d090'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d091'])]"
            show ep03_ambertalk61 with vpunch
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d092'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d093'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d094'])]"
            show ep03_ambertalk62
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d095'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d096'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d097'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d098'])]"
            mc_s "[renpy.substitute(dialogues3['E03SAMBSTAY2_d099'])]"
            show ep03_ambertalk63
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d100'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d101'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d102'])]"
            show ep03_ambertalk64
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d103'])]"
            amb "[renpy.substitute(dialogues3['E03SAMBSTAY2_d104'])]"
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            scene eigengrau with dissolve
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            $ stopAllSubchannels(channel="music", fadeout=2)
            $ stopAllSubchannels(channel="sfx", fadeout=1)
            jump ep03_photofound

label ep03_reunion_left:
    show ep03_ambertalk43
    amb "[renpy.substitute(dialogues3['E03REULEFT_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03REULEFT_d002'])]"
    show ep03_ambertalk44
    amb "[renpy.substitute(dialogues3['E03REULEFT_d003'])]"
    amb "[renpy.substitute(dialogues3['E03REULEFT_d004'])]"
    show ep03_ambertalk64
    amb "[renpy.substitute(dialogues3['E03REULEFT_d005'])]"
    if not ep03_amberpastbehind:
        $ show_walkthrough("ep03_amberstop_menu")
        menu:
            mc_t "[renpy.substitute(dialogues3['E03REULEFT_d006'])]"
            "Stop Amber before she leaves":
                hide screen walkthrough_screen
                $ ep03_amberleft = False
                mc_t "[renpy.substitute(dialogues3['E03REULEFT_d007'])]"
                mc_y "[renpy.substitute(dialogues3['E03REULEFT_d008'])]"
                jump ep03_reunion_left_stop
            "Let Amber leave without saying anything":
                hide screen walkthrough_screen
                mc_t "[renpy.substitute(dialogues3['E03REULEFT_d009'])]"
                mc_t "[renpy.substitute(dialogues3['E03REULEFT_d010'])]"
                $ stopAllSubchannels(channel="music", fadeout=2)
                $ stopAllSubchannels(channel="amb", fadeout=1.5)
                jump ep03_photofound
    else:
        $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
        scene eigengrau with dissolve
        $ stopAllSubchannels(channel="music", fadeout=2)
        $ stopAllSubchannels(channel="amb", fadeout=1.5)
        $ stopAllSubchannels(channel="sfx", fadeout=1)
        jump ep03_photofound

label ep03_reunion_left_stop:
    show ep03_ambertalk45 with hpunch
    amb "[renpy.substitute(dialogues3['E03REULEFT_d011'])]"
    mc_s "[renpy.substitute(dialogues3['E03REULEFT_d012'])]"
    amb "[renpy.substitute(dialogues3['E03REULEFT_d013'])]"
    show ep03_ambertalk46
    amb "[renpy.substitute(dialogues3['E03REULEFT_d014'])]"
    mc_s "[renpy.substitute(dialogues3['E03REULEFT_d015'])]"
    show ep03_ambertalk47
    amb "[renpy.substitute(dialogues3['E03REULEFT_d016'])]"
    mc_s "[renpy.substitute(dialogues3['E03REULEFT_d017'])]"
    amb "[renpy.substitute(dialogues3['E03REULEFT_d018'])]"
    $ show_walkthrough("ep03_amberconvinc_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03REULEFT_d019'])]"
        "Try to convince Amber to stay by appealing to her emotions":
            hide screen walkthrough_screen
            $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
            $ playAudio(amber_sexy_theme2, "music", 2, True, 2.5, 0)
            amb "[renpy.substitute(dialogues3['E03REULEFT_d020'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d021'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d022'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d023'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d024'])]"
            show ep03_ambertalk48 with vpunch
            amb "[renpy.substitute(dialogues3['E03REULEFT_d025'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d026'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d027'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d011'])]"
            show ep03_ambertalk49 at zoom_in
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d029'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d030'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d031'])]"
            show ep03_ambertalk68 with vpunch
            amb "[renpy.substitute(dialogues3['E03REULEFT_d032'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d033'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d034'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d035'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d036'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d037'])]"
        "Attempt to make Amber stay by guilt-tripping her":
            hide screen walkthrough_screen
            amb "[renpy.substitute(dialogues3['E03REULEFT_d020'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d039'])]"
            $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
            $ playAudio(amber_anger_theme, "music", 2, True, 2.5, 0)
            show ep03_ambertalk65
            amb "[renpy.substitute(dialogues3['E03REULEFT_d040'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d041'])]"
            show ep03_ambertalk50
            amb "[renpy.substitute(dialogues3['E03REULEFT_d042'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d043'])]"
            show ep03_ambertalk66
            amb "[renpy.substitute(dialogues3['E03REULEFT_d044'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d045'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d046'])]"
            show ep03_ambertalk67
            amb "[renpy.substitute(dialogues3['E03REULEFT_d047'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d048'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d049'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d050'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d051'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d052'])]"
            amb "[renpy.substitute(dialogues3['E03REULEFT_d053'])]"
            mc_s "[renpy.substitute(dialogues3['E03REULEFT_d054'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_poolnight

label ep03_poolnight:
    scene eigengrau with dissolve
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7)
    $ playAudio(sfx_wind_pool, "amb", 1, True, 2, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_tokyo_residential, "amb", 2, True, 2, 0)
    show ep03_ambernight01 with circlewipe
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d002'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d003'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d004'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d005'])]"
    show ep03_ambernight02
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d006'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d007'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d008'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d009'])]"
    show ep03_ambernight03
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d010'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d011'])]"
    show ep03_ambernight04
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d012'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d013'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d014'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d015'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d016'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d017'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d018'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d019'])]"
    show ep03_ambernight06
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d020'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d021'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d022'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d023'])]"
    show ep03_ambernight07
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d024'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d025'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d026'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d027'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d028'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d029'])]"
    show ep03_ambernight08
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d030'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_glitch, "sfx", 1, True, 2, 0)
    show ep03_ambernight08 at animated_glitch
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d031'])]"
    show ep03_ambernight09 at animated_glitch
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d032'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d033'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d034'])]"
    show ep03_ambernight10 at animated_glitch
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d035'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d036'])]"
    show ep03_ambernight11 at animated_glitch, dizzyness
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d037'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d038'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d039'])]"
    show ep03_ambernight12 at animated_glitch, dizzyness
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d040'])]"
    mc_t "[renpy.substitute(dialogues3['E03POOLNIGHT_d041'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    scene eigengrau with slowfade
    pause 1
    show screen mcpov_dying
    $ playAudio(sfx_splashpool, "sfx", 2, False, 0, 0)
    show ep03_ambernight13 with vpunch
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.7)
    $ playAudio(sfx_underwater, "amb", 4, True, 1, 0)
    mc_t "[renpy.substitute(dialogues3['E03POOLNIGHT_d042'])]"
    amb_y "[renpy.substitute(dialogues3['E03POOLNIGHT_d043'])]"
    show ep03_ambernight14
    mc_t "[renpy.substitute(dialogues3['E03POOLNIGHT_d044'])]"
    amb_y"NO, NO, NO, NO! [mc_name]! [mc_name], PLEASE!"
    show ep03_ambernight15
    mc_t "[renpy.substitute(dialogues3['E03POOLNIGHT_d045'])]"
    hide screen mcpov_dying
    $ setChannelVolume(channel="amb", subchannel=4, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    scene eigengrau with slowfade
    $ playAudio(sfx_pool_dive, "sfx", 7, False, 0, 0)
    show ep03_ambernight16 with vpunch
    amb_y "[renpy.substitute(dialogues3['E03POOLNIGHT_d046'])]"
    show screen mcpov_dying
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ playAudio(sfx_pool_moving, "sfx", 8, False, 0, 0)
    show ep03_ambernight17
    mc_t "[renpy.substitute(dialogues3['E03POOLNIGHT_d047'])]"
    hide screen mcpov_dying
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAudio(channel="amb", subchannel=4, fadeout=1.5)
    scene eigengrau with slowfade
    pause 1
    $ playAudio(sfx_pool_surfacing, "sfx", 3, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    show screen mcpov_dying
    show ep03_ambernight19 at dizzyness with bokeh
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d048'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d049'])]"
    mc_s "[renpy.substitute(dialogues3['E03POOLNIGHT_d050'])]"
    show ep03_ambernight18 at dizzyness
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d051'])]"
    amb "[renpy.substitute(dialogues3['E03POOLNIGHT_d052'])]"
    scene eigengrau with dissolve
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    hide screen mcpov_dying
    jump ep03_afterpool

label ep03_afterpool:
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    $ playAudio(sfx_bodydrag, "sfx", 2, False, 0, 0)
    $ playAudio(sfx_bodygrab, "sfx", 3, False, 0, 0)
    show ep03_afterpool01 with circlewipe
    amb "[renpy.substitute(dialogues3['E03RESCUE_d001'])]"
    amb_t "[renpy.substitute(dialogues3['E03RESCUE_d002'])]"
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)
    show ep03_afterpool02 with hpunch
    amb_t "[renpy.substitute(dialogues3['E03RESCUE_d003'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d004'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 2, True, 1.5, 0)
    show ep03_afterpool03 with circlewipe
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d005'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d006'])]"
    show ep03_afterpool04
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d007'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d008'])]"
    show ep03_afterpool05 at zoom_in
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d009'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d010'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d011'])]"
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)
    show ep03_afterpool06 with vpunch
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d012'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d013'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d014'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d015'])]"
    show ep03_afterpool07
    amb "[renpy.substitute(dialogues3['E03RESCUE_d016'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d017'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d018'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d019'])]"
    show ep03_afterpool08 with hpunch
    amb "[renpy.substitute(dialogues3['E03RESCUE_d020'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d021'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d022'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d023'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d024'])]"
    show ep03_afterpool09
    amb "[renpy.substitute(dialogues3['E03RESCUE_d025'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d026'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d027'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d028'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d029'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d030'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d031'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d032'])]"
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)
    show ep03_afterpool10 with vpunch
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d033'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d034'])]"
    if ep01_first:
        mc_s "[renpy.substitute(dialogues3['E03RESCUE_d035'])]"
    else:
        mc_s "[renpy.substitute(dialogues3['E03RESCUE_d036'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d037'])]"
    show ep03_afterpool11
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d038'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d039'])]"
    if ep01_first:
        mc_s "[renpy.substitute(dialogues3['E03RESCUE_d040'])]"
    else:
        mc_s "[renpy.substitute(dialogues3['E03RESCUE_d041'])]"
    show ep03_afterpool12
    amb "[renpy.substitute(dialogues3['E03RESCUE_d042'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d043'])]"
    scene eigengrau with dissolve
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 2, 0)
    show ep03_afterpool13 with hpunch
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d044'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d045'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d046'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d047'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d048'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d049'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d050'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d051'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d052'])]"
    show ep03_afterpool14 with hpunch
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d053'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d054'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d055'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d056'])]"
    mc_t "[renpy.substitute(dialogues3['E03RESCUE_d057'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d058'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d059'])]"
    show ep03_afterpool15
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d060'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d061'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d062'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d063'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d064'])]"
    show ep03_afterpool16
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d065'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d066'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d067'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d068'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d069'])]"
    amb "[renpy.substitute(dialogues3['E03RESCUE_d070'])]"
    mc_s "[renpy.substitute(dialogues3['E03RESCUE_d071'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_amberclothes

label ep03_amberclothes:
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)
    show ep03_caught1 with circlewipe
    $ ep03_madsuspicion = True
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d001'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d002'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d003'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d004'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(madison_theme, "music", 2, True, 2, 0)
    show ep03_caught2 with vpunch
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d005'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d006'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d007'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d008'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d009'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d010'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d011'])]"
    show ep03_caught3
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d012'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d013'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d014'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d015'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d016'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d017'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d018'])]"
    $ show_walkthrough("ep03_maddiebod_menu")
    menu:
        "Check out Madison's body":
            hide screen walkthrough_screen
            $ rm.update("madison", "cor", 2)
            $ check_levels("madison", "cor", 2)
            $ ep03_madcheck += 1
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d019'])]"
            show ep03_caught4 at camera_zoom with dissolve
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d020'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d021'])]"
            mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d022'])]"
            mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d023'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d024'])]"
            mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d025'])]"
        "Avert your gaze":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d026'])]"
            mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d022'])]"
    show ep03_caught5
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d028'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d029'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d030'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d031'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d032'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d033'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d034'])]"
    show ep03_caught6 with hpunch
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d035'])]"
    mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d036'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d037'])]"
    $ show_walkthrough("ep03_maddieass_menu")
    menu:
        "Stare at Madison's ass as she leaves":
            hide screen walkthrough_screen
            $ rm.update("madison", "cor", 5)
            $ check_levels("madison", "cor", 5)
            $ ep03_madcheck += 2
            show ep03_caught7 at camera_zoom with dissolve
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d038'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d039'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d040'])]"
            mad_y "[renpy.substitute(dialogues3['E03AMBERCLOTH_d041'])]"
            mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d042'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERCLOTH_d043'])]"
            mad "[renpy.substitute(dialogues3['E03AMBERCLOTH_d044'])]"
        "Resist the temptation to ogle Madison":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d045'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d046'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    pause 1.5
    $ playAudio(sfx_cardoor_open, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=7, volume=0.5)
    $ playAudio(sfx_midnightpast, "amb", 7, True, 1.5, 0)
    show ep03_caught8 with circlewipe
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d047'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d048'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d049'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d050'])]"
    $ show_walkthrough("ep03_amberroom_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d051'])]"
        "Get the sweater":
            hide screen walkthrough_screen
            $ ep03_ambclothes += 2
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d052'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d053'])]"
        "Forget about the sweater":
            hide screen walkthrough_screen
            $ ep03_ambclothes += 1
            $ rm.update("amber", "cor", 5)
            $ check_levels("amber", "cor", 5)
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d054'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d055'])]"
            mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d056'])]"
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_ambernite

label ep03_ambernite:
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 2, True, 1.5, 0)
    show ep03_night01 with circlewipe
    amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d001'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d002'])]"
    amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d003'])]"
    if ep03_ambclothes == 2:
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d004'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d005'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d005x'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d006'])]"
    else:
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d007'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d008'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d009'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d010'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d011'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    show ep03_night02 with circlewipe
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d012'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d013'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d014'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d015'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d016'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d017'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d018'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d019'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d020'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d021'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d022'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d023'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d024'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d025'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d026'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d027'])]"
    show ep03_night03 with slowfade
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(amber_theme, "music", 1, True, 3, 0)
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d028'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d029'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d030'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d031'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d032'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d033'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d034'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d035'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d036'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d037'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d038'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d039'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d040'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d041'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d042'])]"
    show ep03_night04
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d043'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d044'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d045'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d046'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d047'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d048'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d049'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d050'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d051'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d052'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d053'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d054'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d055'])]"
    $ show_walkthrough("ep03_ambersleep_menu")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d056'])]"
        "Invite Amber to spend the night":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d057'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d058'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d059'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d060'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d061'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d062'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d063'])]"
            jump ep03_ambernite_sleep
        "Let Amber leave without inviting her to stay":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d064'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d065'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d066'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d067'])]"
            jump ep03_ambernite_bye

label ep03_ambernite_bye:
    show ep03_night05
    mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d068'])]"
    amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d069'])]"
    mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d070'])]"
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d071'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d072'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_photofound

label ep03_ambernite_sleep:
    show ep03_night06 with hpunch
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d073'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d074'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d075'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d076'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d077'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d078'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d079'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d080'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d081'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d082'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d083'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d084'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d085'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d086'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d087'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d088'])]"
    show ep03_night07
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d089'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d090'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d091'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d092'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d093'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d094'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d095'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d096'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d097'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d067'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d099'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    pause 2
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep03_night08 with circlewipe
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d100'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d101'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d102'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d103'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d104'])]"
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d105'])]"
    show ep03_night09
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d106'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d107'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d108'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d109'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d110'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d111'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d112'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d113'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d114'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d115'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d116'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d117'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d118'])]"
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep03_night10 with vpunch
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d119'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d120'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d121'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d122'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d123'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d124'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d125'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d126'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d127'])]"
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    $ playAudio(sfx_bedmove2, "sfx", 2, False, 0, 0)
    show ep03_night11 with hpunch
    if ep03_ambclothes == 2:
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d128'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d129'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d130'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d131'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d132'])]"
    else:
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d133'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d134'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d135'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d136'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d137'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d138'])]"
    show ep03_night12
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d139'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d140'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d141'])]"
    else:
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d142'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d143'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d144'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d145'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d146'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d147'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d148'])]"
        amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d149'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d150'])]"
    $ show_walkthrough("ep03_ambersleep_menu2")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d151'])]"
        "Turn off the lights and go to sleep":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d152'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d153'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d154'])]"
            $ ep03_madcaught = True
        "Lock the door before turning off the lights":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d155'])]"
            mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d156'])]"
            amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d157'])]"
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    $ stopAllSubchannels(channel="amb", fadeout=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 2, True, 1.5, 0)
    show ep03_night13 with circlewipe
    mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d158'])]"
    amb "[renpy.substitute(dialogues3['E03AMBERNIGHT_d159'])]"
    if ep03_madcaught:
        show ep03_night14 with dissolve
        mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d160'])]"
        mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d161'])]"
        mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d162'])]"
        if ep03_madcheck == 1:
            mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d163'])]"
        elif ep03_madcheck == 2:
            mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d164'])]"
        elif ep03_madcheck == 3:
            mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d165'])]"
        mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d166'])]"
        mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d167'])]"
        mad_t "[renpy.substitute(dialogues3['E03AMBERNIGHT_d168'])]"
    else:
        pass
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_morningwithamber

label ep03_morningwithamber:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
    $ playAudio(sfx_morning, "amb", 5, True, 2, 0)
    show ep03_atmorning01 with circlewipe
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d001'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d002'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d003'])]"
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)
    show ep03_atmorning02 at zoom_in with vpunch
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d011'])]"
    mc_t "[renpy.substitute(dialogues3['E03AMBERCLOTH_d018'])]"
    if ep03_ambclothes == 2:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d004'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d005'])]"
    else:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d006'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d007'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d008'])]"
    $ playAudio(sfx_bedmove2, "sfx", 2, False, 0, 0)
    show ep03_atmorning03 with vpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d009'])]"
    if ep03_ambclothes == 2:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d010'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d011'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d012'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d013'])]"
    else:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d014'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d015'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d012'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d017'])]"
    show ep03_atmorning04
    if ep03_ambclothes == 2:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d018'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d019'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d020'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d021'])]"
    else:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d022'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d023'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d024'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d025'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d026'])]"
    $ show_walkthrough("ep03_ambersleep_menu3")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d027'])]"
        "Grope Amber":
            hide screen walkthrough_screen
            $ ep03_gropeamber = True
            jump ep03_morningwithamber_grope
        "Cover Amber up":
            hide screen walkthrough_screen
            jump ep03_morningwithamber_b2sleep

label ep03_morningwithamber_b2sleep:
    $ playAudio(sfx_bedmove2, "sfx", 4, False, 0, 0)
    show ep03_atmorning05 with hpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d028'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d029'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_photofound

label ep03_morningwithamber_grope:
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 3, 0)
    show ep03_atmorning06 with hpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d030'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d031'])]"
    show ep03_atmorning07 at camera_zoom with flash
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d032'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d033'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d034'])]"
    show ep03_atmorning08
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d035'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d036'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d037'])]"
    show ep03_atmorning09 with hpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d038'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d039'])]"
    show ep03_atmorning10 with hpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_breath_sleep_f, "sfx", 2, False, 0, 0)
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d040'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d041'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d042'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d043'])]"
    show ep03_atmorning11
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d044'])]"
    show ep03_atmorning11 with hpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d045'])]"
    show ep03_atmorning11 with hpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d046'])]"
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_changeclothes_nozip, "sfx", 9, False, 0, 0)
    show ep03_atmorning12 with vpunch
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d047'])]"
    show ep03_atmorning12 at zoom_in
    if ep01_first:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d048'])]"
    else:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d049'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_sighbreathfem, "sfx", 3, False, 0, 0)
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d050'])]"
    if not ep01_first:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d051'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d052'])]"
        $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
        $ playAudio(sfx_recstop, "sfx", 5, False, 0, 0)
        $ stopAllSubchannels(channel="music", fadeout=0.5)
        show ep03_atmorning13 with vpunch
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d053'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d054'])]"
        show ep03_atmorning13 with hpunch
        amb_y "[renpy.substitute(dialogues3['E03MORNINGAMBER_d055'])]"
        $ setChannelVolume(channel="music", subchannel=7, volume=0.3)
        $ playAudio(amber_anger_theme, "music", 7, True, 2, 0)
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d056'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d057'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d058'])]"
        show ep03_atmorning13 with hpunch
        amb_y "[renpy.substitute(dialogues3['E03MORNINGAMBER_d059'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d060'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d061'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d062'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d063'])]"
        show ep03_atmorning13 with hpunch
        amb_y "[renpy.substitute(dialogues3['E03MORNINGAMBER_d064'])]"
        jump ep03_morningwithamber_grope_sex_ruined
    else:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d051'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d052'])]"
        jump ep03_morningwithamber_grope_sex
    
label ep03_morningwithamber_grope_sex:
    show ep03_atmorning14 with vpunch
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d054'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d068'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d069'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d070'])]"
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d071'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d072'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d073'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d074'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d075'])]"
    if ep03_ambclothes == 2:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d076'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d077'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d078'])]"
    scene eigengrau with slowfade
    pause 1
    show ep03_atmorning19 with circlewipe
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d079'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d080'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d081'])]"
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)
    show ep03_atmorning20 at camera_zoom with hpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d082'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d083'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d084'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d085'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d086'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d087'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d088'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d089'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d090'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d091'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d092'])]"
    $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)
    show ep03_atmorning21 with hpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d093'])]"
    show ep03_atmorning21 with hpunch
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d094'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d095'])]"
    $ show_walkthrough("ep03_ambersex_menu")
    menu:
        "Insist on having sex":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", -2)
            $ check_levels("amber", "cor", -2)
            $ ep03_insistamber = True
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d096'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d097'])]"
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d098'])]"
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ stopAllSubchannels(channel="music", fadeout=2)
            jump ep03_morningwithamber_grope_sex_ruined
        "Respect Amber's wishes":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", 5)
            $ check_levels("amber", "cor", 5)
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d099'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d100'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d101'])]"
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d102'])]"
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            show ep03_atmorning23 with vpunch
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d103'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d104'])]"
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d105'])]"
            $ show_walkthrough("ep03_ambersex_menu2")
            menu:
                amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d106'])]"
                "Start with a titjob":
                    hide screen walkthrough_screen
                    $ ep03_ambersex_bbj = True
                    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d107'])]"
                    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d108'])]"
                    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d109'])]"
                    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d110'])]"
                    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d111'])]"
                    $ stopAllSubchannels(channel="amb", fadeout=1.5)
                    jump ep03_morningwithamber_grope_sex_bbj
                "Skip the titjob and go for pussy play":
                    hide screen walkthrough_screen
                    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d112'])]"
                    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d113'])]"
                    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d114'])]"
                    $ stopAllSubchannels(channel="amb", fadeout=1.5)
                    jump ep03_morningwithamber_grope_sex_pj

label ep03_morningwithamber_grope_sex_bbj:
    scene eigengrau with dissolve
    pause 1.5
    show ep03_atmorning24 at zoom_in with slowfade
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d115'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d116'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d117'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d118'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.4)
    $ playAudio(sfx_inhale_fem, "sfx", 3, False, 0, 0)
    show ep03_atmorning25 with hpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d272'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d119'])]"
    show ep03_atmorning25
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d120'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d121'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d122'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d123'])]"
    show ep03_atmorning26
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d124'])]"
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)
    show ep03_atmorning26 at camera_zoom
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d125'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d126'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d127'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d128'])]"
    show ep03_atmorning27 with hpunch
    $ playAudio(sfx_inhale_fem, "sfx", 3, False, 0, 0)
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d129'])]"
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)
    show ep03_atmorning27 at camera_zoom
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d130'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d131'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d132'])]"
    show ep03_atmorning28 with hpunch
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d133'])]"
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)
    show ep03_atmorning28
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d134'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d135'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d136'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d137'])]"
    jump ep03_morningwithamber_grope_sex_pj

label ep03_morningwithamber_grope_sex_pj:
    scene eigengrau with dissolve
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    pause 1.5
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep03_atmorning29 with vpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d138'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d139'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d140'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d141'])]"
    show ep03_atmorning31
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d142'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d143'])]"
    show ep03_atmorning30
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d144'])]"
    $ playAudio(sfx_gasp_female, "sfx", 3, False, 0, 0)
    show ep03_atmorning32 with vpunch
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d145'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d146'])]"
    hide ep03_atmorning32
    if ep03_ambersex_bbj:
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d147'])]"
    else:
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d148'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.7)
    $ playAudio(sfx_femheavybreath, "sfx", 5, False, 0, 0)
    show ep03_atmorning32 with vpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d149'])]"
    hide ep03_atmorning32
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d150'])]"
    show ep03_atmorning32 with vpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d151'])]"
    hide ep03_atmorning32
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d152'])]"
    show ep03_atmorning33
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d153'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d154'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d155'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d156'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d157'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d158'])]"
    $ show_walkthrough("ep03_ambersex_menu3")
    menu:
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d159'])]"
        "Penetrate her":
            hide screen walkthrough_screen
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d160'])]"
            $ ep03_amberpenetrate = True
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            jump ep03_morningwithamber_grope_sex_inside
        "Respect her boundaries":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d160'])]"
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            jump ep03_morningwithamber_grope_sex_pj_cont

label ep03_morningwithamber_grope_sex_inside:
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.25)
    $ playAudio(sfx_fem_surprised, "sfx", 6, False, 0, 0)
    show ep03_atmorning34 with hpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d162'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_femheavybreath, "sfx", 7, False, 0, 0)
    show ep03_atmorning34
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d163'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d164'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d165'])]"
    show ep03_atmorning35
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d166'])]"
    amb_y "[renpy.substitute(dialogues3['E03MORNINGAMBER_d167'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d168'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_morningwithamber_grope_sex_ruined

label ep03_morningwithamber_grope_sex_ruined:
    if ep03_amberpenetrate:
        scene eigengrau with dissolve
        $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
        $ playAudio(sfx_morning, "amb", 5, True, 2, 0)
        pause 1
        show ep03_atmorning22 with vpunch
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d169'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d170'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d171'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d172'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d173'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d174'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d175'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d176'])]"
    elif ep03_insistamber:
        show ep03_atmorning22 with hpunch
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d177'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d178'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d179'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d180'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d181'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d182'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d183'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d184'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d185'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d186'])]"
    else:
        pass
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)
    show ep03_atmorning15 with vpunch
    if ep03_amberpenetrate:
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d187'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d188'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d189'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d190'])]"
        mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d191'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d192'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d193'])]"
    elif ep03_insistamber:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d194'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d195'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d196'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d197'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d198'])]"
        mc_s "[renpy.substitute(dialogues3['E03AMBERNIGHT_d011'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d199'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d200'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d201'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d202'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d203'])]"
    show ep03_atmorning16
    if ep03_amberpenetrate:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d204'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d205'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d206'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d207'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d208'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d209'])]"
    elif ep03_insistamber:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d210'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d211'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d212'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d213'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d214'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d215'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d216'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d217'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d218'])]"
    show ep03_atmorning17
    if ep03_amberpenetrate:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d219'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d220'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d221'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d222'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d223'])]"
    elif ep03_insistamber:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d224'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d225'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d226'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d227'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d228'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d229'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d230'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d231'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d232'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d233'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d234'])]"
    show ep03_atmorning18
    if ep03_amberpenetrate:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d235'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d236'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d237'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d238'])]"
    elif ep03_insistamber:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d239'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d240'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d241'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d242'])]"
    else:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d243'])]"
        mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d244'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d245'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d246'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d247'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d248'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d249'])]"
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d250'])]"
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d251'])]"
    $ ep03_amberangry = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_photofound

label ep03_morningwithamber_grope_sex_pj_cont:
    scene eigengrau with dissolve
    pause 1.5
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_femheavybreath, "sfx", 7, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.4)
    $ playAudio(sfx_sexslide1, "sfx", 2, False, 0, 0)
    show ep03_atmorning36
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d252'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d253'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d254'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d255'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d256'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d257'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d258'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d259'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d260'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d261'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_fem_surprised, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.4)
    $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)
    show ep03_atmorning41 with vpunch
    hide ep03_atmorning36
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d262'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d263'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d264'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d265'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d266'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d267'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d268'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d269'])]"
    $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)
    $ playAudio(sfx_sighbreathfem, "sfx", 1, False, 0, 0)
    show ep03_atmorning42 with hpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d138'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d139'])]"
    $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)
    show ep03_atmorning43 with vpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d272'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d273'])]"
    show ep03_atmorning43 with vpunch
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d274'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d275'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d276'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.9)
    $ playAudio(sfx_lick1, "sfx", 7, False, 0, 0)
    show ep03_atmorning45
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d277'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d278'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d279'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d280'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d050'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d282'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d283'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d284'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d285'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d286'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d287'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d288'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d289'])]"
    $ show_walkthrough("ep03_ambersex_menu4")
    menu:
        amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d290'])]"
        "Ignore Amber's pleas and fuck her":
            hide screen walkthrough_screen
            $ ep03_amberpenetrate = True
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)
            show ep03_atmorning44 with vpunch
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d291'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d292'])]"
            $ playAudio(sfx_gasp_female, "sfx", 3, False, 0, 0)
            show ep03_atmorning47 with hpunch
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d293'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d294'])]"
            $ playAudio(sfx_femheavybreath, "sfx", 7, False, 0, 0)
            show ep03_atmorning48
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d295'])]"
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d296'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d297'])]"
            mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d298'])]"
            amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d299'])]"
            $ stopAllSubchannels(channel="music", fadeout=2)
            $ stopAllSubchannels(channel="sfx", fadeout=1)
            jump ep03_morningwithamber_grope_sex_ruined
        "Listen to Amber and stop":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            $ rm.update("amber", "cor", 1)
            pass
    $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)
    show ep03_atmorning44 with vpunch
    $ ep03_ambersex = True
    mc_t "[renpy.substitute(dialogues3['E03MORNINGAMBER_d300'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d301'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d302'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d303'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with dissolve
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
    $ playAudio(sfx_morning, "amb", 5, True, 2, 0)
    show ep03_atmorning49 with slowfade
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d304'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d305'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d306'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d307'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d308'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d309'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep03_atmorning50 with vpunch
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d310'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d311'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d312'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.3)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)
    show ep03_atmorning51
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d313'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d314'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d315'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d316'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d317'])]"
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)
    show ep03_atmorning52
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d318'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d319'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d320'])]"
    show ep03_atmorning53
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d321'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d322'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d323'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d324'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d325'])]"
    mc_s "[renpy.substitute(dialogues3['E03MORNINGAMBER_d326'])]"
    amb "[renpy.substitute(dialogues3['E03MORNINGAMBER_d327'])]"
    if ep03_ambersex and ep03_ambclothes == 1:
        $ ep03_ambersex_l = True
    elif ep03_ambersex and ep03_ambclothes == 2:
        $ ep03_ambersex_c = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_photofound

label ep03_photofound:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_digitalcamera3, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.5)
    $ playAudio(sfx_room_noise3, "amb", 1, True, 2, 0)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.6)
    $ playAudio(photos_theme, "music", 1, True, 2, 0)
    show ep03_antoback03 with ccirclewipe
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d001'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d002'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d003'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d004'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d005'])]"
    $ playAudio(sfx_digitalcamera1, "sfx", 1, False, 0, 0)
    show ep03_antoback04
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d006'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d007'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d008'])]"
    isa "[renpy.substitute(dialogues3['E03PHOTOF_d009'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d010'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d011'])]"
    show ep03_antoback05
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d012'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d013'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d014'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d015'])]"
    show ep03_antoback07
    isa "[renpy.substitute(dialogues3['E03PHOTOF_d016'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d017'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d018'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d019'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d020'])]"
    show ep03_antoback09
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d021'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d022'])]"
    show ep03_antoback10
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d023'])]"
    isa "[renpy.substitute(dialogues3['E03PHOTOF_d024'])]" 
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d025'])]"
    show ep03_antoback11
    isa "[renpy.substitute(dialogues3['E03PHOTOF_d026'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d027'])]"
    isa "[renpy.substitute(dialogues3['E03PHOTOF_d028'])]"
    eli "[renpy.substitute(dialogues3['E03PHOTOF_d029'])]"
    mad "[renpy.substitute(dialogues3['E03PHOTOF_d030'])]"
    isa_t "[renpy.substitute(dialogues3['E03PHOTOF_d031'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
    $ playAudio(sfx_morning, "amb", 5, True, 2, 0)
    $ playAudio(sfx_phone, "sfx", 1, True, 0, 0)
    show ep03_antoback01 with dissolve
    mc_t "[renpy.substitute(dialogues3['E03PHOTOF_d032'])]"
    ##SMS WINDOW
    call screen phone_icons("ep03_sms01")
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    mc_t "[renpy.substitute(dialogues3['E03PHOTOF_d033'])]"
    mc_t "[renpy.substitute(dialogues3['E03PHOTOF_d034'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_boxes

label ep03_boxes:
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.7)
    $ playAudio(sfx_earlypast, "amb", 2, True, 2, 0)
    show ep03_antoback13 with ccirclewipe
    mc_t "[renpy.substitute(dialogues3['E03BOX_d001'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d002'])]"
    show ep03_antoback14
    mc_t "[renpy.substitute(dialogues3['E03BOX_d003'])]"
    if not ep03_amberleft:
        mc_t "[renpy.substitute(dialogues3['E03BOX_d004'])]"
    else:
        mc_t "[renpy.substitute(dialogues3['E03BOX_d005'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d006'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.6)
    $ playAudio(sfx_box_search, "sfx", 7, False, 0, 0)
    show ep03_antoback15
    mc_t "[renpy.substitute(dialogues3['E03BOX_d007'])]"
    if htl_episodes == 3:
        $ show_custom_notification("save_tip")
    else:
        pass
    mc_t "[renpy.substitute(dialogues3['E03BOX_d008'])]"
    $ stopAudio(channel="sfx", subchannel=7, fadeout=0.5)
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.9)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)
    show ep03_antoback16 with vpunch
    mc_t "[renpy.substitute(dialogues3['E03BOX_d009'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d010'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(antonella_love, "music", 1, True, 2, 0)
    show ep03_antoback17 at camera_zoom
    mc_t "[renpy.substitute(dialogues3['E03BOX_d011'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d012'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d013'])]"
    show ep03_antoback18 with smoke
    mc_t "[renpy.substitute(dialogues3['E03BOX_d014'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d015'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d016'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with smoke
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.4)
    $ playAudio(sfx_evenstreet, "amb", 2, True, 1, 0)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.3)
    $ playAudio(sfx_footsteps_heelstile, "sfx", 3, True, 0, 0)
    show ep03_antoback19 with dissolve
    mc_t "[renpy.substitute(dialogues3['E03BOX_d017'])]"
    show ep03_antoback20
    mc_t "[renpy.substitute(dialogues3['E03BOX_d018'])]"
    show ep03_antoback22
    mc_t "[renpy.substitute(dialogues3['E03BOX_d019'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d020'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.6)
    $ playAudio(sfx_doorclose, "sfx", 4, False, 0, 0)
    show ep03_antoback24 with slowfade
    mc_t "[renpy.substitute(dialogues3['E03BOX_d021'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d022'])]"
    mc_t "[renpy.substitute(dialogues3['E03BOX_d023'])]"
    show ep03_antoback25
    mc_t "[renpy.substitute(dialogues3['E03BOX_d024'])]"
    show ep03_antoback26
    mc_t "[renpy.substitute(dialogues3['E03BOX_d025'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
    call hideNoise(transition=dissolve)
#-- End Episode 3
    if htl_episodes == 3:
        return
    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep04_title