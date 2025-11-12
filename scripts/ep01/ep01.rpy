label ep01_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    call showNoise(0.1, 0.15, transition=dissolve)
    $ quick_menu = True
    show screen stats_button
    show screen walkthrough_icon
    $ renpy.block_rollback()
## -- SCENE 01: ISABELLA INTRO TRAIN
    show ep01_1stdream00
    $ config.rollback_enabled = True
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(isabella_theme, "music", 2, True, 5, 0)
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    mc_t "[renpy.substitute(dialogues['E01S01_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01S01_d002'])]"
    if renpy.loadable("wt.rpyc"):
        $ show_custom_notification("wt_tip")
    else:
        pass
    $ playAudio(sfx_trainstationquiet, "amb", 1, True, 1, 0)
    show ep01_1stdream01
    mc_t "[renpy.substitute(dialogues['E01S01_d003'])]"
    show ep01_1stdream03
    mc_t "[renpy.substitute(dialogues['E01S01_d004'])]"
    show ep01_1stdream02
    mc_t "[renpy.substitute(dialogues['E01S01_d005'])]"
    mc_t "[renpy.substitute(dialogues['E01S01_d006'])]"
    show ep01_1stdream04
    mc_t "[renpy.substitute(dialogues['E01S01_d007'])]"
    $ show_walkthrough("ep01_train_menu")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S01_d008'])]"
        "Walking at the park":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S01_d009'])]"
        "First steps":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S01_d010'])]"
    mc_t "[renpy.substitute(dialogues['E01S01_d011'])]"
    show ep01_1stdream05
    mc_t "[renpy.substitute(dialogues['E01S01_d012'])]"
    show ep01_1stdream06
    mc_t "[renpy.substitute(dialogues['E01S01_d013'])]"
    show ep01_1stdream07
    mc_t "[renpy.substitute(dialogues['E01S01_d014'])]"
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ stopAllSubchannels(channel="amb", fadeout=2)
    jump ep01_dream1

label ep01_dream1:
##RM.POINTS.TRACK (antonella, trust, +1, +2)
# --
## -- SCENE: MEETING ANTONELLA
    scene eigengrau with bokeh
    show ep01_1stdream09 with clouds_inverse
    $ playAudio(sfx_hshall, "amb", 1, True, 2, 0)
    "Girl" "[renpy.substitute(dialogues['E01S02u001'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d001'])]"
    show ep01_1stdream08
    "Girl" "[renpy.substitute(dialogues['E01S02u002'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d002'])]"
    show ep01_1stdream10
    "Girl" "[renpy.substitute(dialogues['E01S02u003'])]"
    $ show_walkthrough("ep01_antodemo_menu")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S02_d003'])]"
        "I've seen you before":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d004'])]"
            show ep01_1stdream11
            "Girl" "[renpy.substitute(dialogues['E01S02u004'])]"
        "You don't look from here":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d005'])]"
            show ep01_1stdream11
            "Girl" "[renpy.substitute(dialogues['E01S02u004b'])]"
        "You look lonely":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d006'])]"
            show ep01_1stdream11
            "Girl" "[renpy.substitute(dialogues['E01S02u004c'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d007'])]"
    show ep01_1stdream12
    "Girl" "[renpy.substitute(dialogues['E01S02u005'])]"
    $ show_walkthrough("ep01_antodemo_menu")
    menu:
        "Try again?":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d008'])]"
            "Girl" "[renpy.substitute(dialogues['E01S02u006'])]"
        "Leave her be":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d009'])]"
            "Girl" "[renpy.substitute(dialogues['E01S02u007'])]"
    show ep01_1stdream13
    mc_s "[renpy.substitute(dialogues['E01S02_d010'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u008'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u009'])]"
    show ep01_1stdream14
    "Girl" "[renpy.substitute(dialogues['E01S02u010'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u011'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u012'])]"
    show ep01_1stdream15
    "Girl" "[renpy.substitute(dialogues['E01S02u013'])]"
    show ep01_1stdream16 with vpunch
    $ setChannelVolume(channel="music", subchannel=3, volume=0.8)
    $ playAudio(antonella_love, "music", 3, True, 2, 0)
    "Girl" "[renpy.substitute(dialogues['E01S02u014'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d011'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u015'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u016'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u017'])]"
    show ep01_1stdream18
    "Girl" "[renpy.substitute(dialogues['E01S02u018'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d012'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u019'])]"
    show ep01_1stdream17
    "Girl" "[renpy.substitute(dialogues['E01S02u020'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d013'])]"
    show ep01_1stdream19
    "Girl" "[renpy.substitute(dialogues['E01S02u021'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d014'])]"
    show ep01_1stdream20
    "Girl" "[renpy.substitute(dialogues['E01S02u022'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d015'])]"
    show ep01_1stdream21
    "Girl" "[renpy.substitute(dialogues['E01S02u023'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d016'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u024'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u025'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d017'])]"
    show ep01_1stdream22
    "Girl" "[renpy.substitute(dialogues['E01S02u026'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d018'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u027'])]"
    show ep01_1stdream23
    "Girl" "[renpy.substitute(dialogues['E01S02u028'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d019'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u029'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d020'])]"
    show ep01_1stdream24
    "Girl" "[renpy.substitute(dialogues['E01S02u030'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d021'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u031'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d022'])]"
    show ep01_1stdream25
    "Girl" "[renpy.substitute(dialogues['E01S02u032'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d023'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u033'])]"
    $ show_walkthrough("ep01_dream1_menu")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S02_d024'])]"
        "Honest":
            $ rm.update("antonella", "trust", 1)
            $ check_levels("antonella", "trust", 1)
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d025'])]"
            show ep01_1stdream28 with vpunch
            "Girl" "[renpy.substitute(dialogues['E01S02u034'])]"
            mc_s "[renpy.substitute(dialogues['E01S02_d026'])]"
            "Girl" "[renpy.substitute(dialogues['E01S02u035'])]"
            "Girl" "[renpy.substitute(dialogues['E01S02u036'])]"
        "Joke about it":
            $ rm.update("antonella", "trust", 2)
            $ check_levels("antonella", "trust", 2)
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S02_d027'])]"
            show ep01_1stdream28 with vpunch
            "Girl" "[renpy.substitute(dialogues['E01S02u037'])]"
            mc_s "[renpy.substitute(dialogues['E01S02_d028'])]"
            "Girl" "[renpy.substitute(dialogues['E01S02u038'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d029'])]"
    show ep01_1stdream27
    "Girl" "[renpy.substitute(dialogues['E01S02u039'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u040'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u041'])]"
    show ep01_1stdream26
    mc_s "[renpy.substitute(dialogues['E01S02_d030'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u042'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d031'])]"
    show ep01_1stdream29 with hpunch
    "Girl" "[renpy.substitute(dialogues['E01S02u043'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d032'])]"
    show ep01_1stdream30
    "Girl" "[renpy.substitute(dialogues['E01S02u044'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u045'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u046'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u047'])]"
    show ep01_1stdream31
    "Girl" "[renpy.substitute(dialogues['E01S02u048'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d033'])]"
    show ep01_1stdream32
    "Girl" "[renpy.substitute(dialogues['E01S02u049'])]"
    "Girl" "[renpy.substitute(dialogues['E01S02u050'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d034'])]"
    anto "[renpy.substitute(dialogues['E01S02_d035'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d036'])]"
    anto "[renpy.substitute(dialogues['E01S02_d037'])]"
    show ep01_1stdream33 with dissolve
    $ stopAllSubchannels(channel="amb", fadeout=2)
    $ stopAllSubchannels(channel="music", fadeout=2)
    pause 1
#BACK TO REALITY
    scene eigengrau with clouds
    show ep01_1stdream34
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    $ rm.set_knows("isabella", True)
    isa "[renpy.substitute(dialogues['E01S02_d038'])]"
    isa "[renpy.substitute(dialogues['E01S02_d039'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d040'])]"
    isa "[renpy.substitute(dialogues['E01S02_d041'])]"
    mc_t "[renpy.substitute(dialogues['E01S02_d042'])]"
    show ep01_1stdream35
    mc_s "[renpy.substitute(dialogues['E01S02_d043'])]"
    isa "[renpy.substitute(dialogues['E01S02_d044'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d045'])]"
    show ep01_1stdream36
    isa "[renpy.substitute(dialogues['E01S02_d046'])]"
    isa "[renpy.substitute(dialogues['E01S02_d047'])]"
    show ep01_1stdream37
    mc_s "[renpy.substitute(dialogues['E01S02_d048'])]"
    mc_s "[renpy.substitute(dialogues['E01S02_d049'])]"
    isa "[renpy.substitute(dialogues['E01S02_d050'])]"
    $ stopAllSubchannels(channel="amb", fadeout=2)
    jump ep01_2nddream

label ep01_2nddream:
    scene eigengrau with clouds_inverse 
##RM.POINTS.TRACK (antonella, trust, +1/+2)
# --
## -- SCENE: ANTONELLA'S TREE
    $ playAudio(sfx_hshall, "amb", 1, True, 2, 0)
    show ep01_2nddream01 with clouds_inverse 
    mc_t "[renpy.substitute(dialogues['E01S03_d001'])]"
    show ep01_2nddream02
    mc_t "[renpy.substitute(dialogues['E01S03_d002'])]"
    $ playAudio(sfx_footsteps_female_semirun, "sfx", 1, False, 1, 1)
    show ep01_2nddream03
    mc_t "[renpy.substitute(dialogues['E01S03_d003'])]"
    show ep01_2nddream04
    anto "[renpy.substitute(dialogues['E01S03_d004'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=0.5)
    show ep01_2nddream05 with vpunch
    mc_s "[renpy.substitute(dialogues['E01S03_d005'])]"
    $ setChannelVolume(channel="music", subchannel=3, volume=0.8)
    $ playAudio(antonella_love, "music", 3, True, 2, 0)
    anto "[renpy.substitute(dialogues['E01S03_d006'])]"
    show ep01_2nddream06
    mc_s "[renpy.substitute(dialogues['E01S03_d007'])]"
    anto "[renpy.substitute(dialogues['E01S03_d008'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d009'])]"
    show ep01_2nddream07
    anto "[renpy.substitute(dialogues['E01S03_d010'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d011'])]"
    show ep01_2nddream08
    anto "[renpy.substitute(dialogues['E01S03_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d013'])]"
    show ep01_2nddream09
    anto "[renpy.substitute(dialogues['E01S03_d014'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d016'])]"
    show ep01_2nddream10
    anto "[renpy.substitute(dialogues['E01S03_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d018'])]"
    anto "[renpy.substitute(dialogues['E01S03_d019'])]"
    show ep01_2nddream11
    anto "[renpy.substitute(dialogues['E01S03_d020'])]"
    anto "[renpy.substitute(dialogues['E01S03_d021'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d022'])]"
    anto "[renpy.substitute(dialogues['E01S03_d023'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d024'])]"
    show ep01_2nddream12
    mc_s "[renpy.substitute(dialogues['E01S03_d025'])]"
    anto "[renpy.substitute(dialogues['E01S03_d026'])]"
    show ep01_2nddream13
    mc_s "[renpy.substitute(dialogues['E01S03_d027'])]"
    anto "[renpy.substitute(dialogues['E01S03_d028'])]"
    show ep01_2nddream14
    anto "[renpy.substitute(dialogues['E01S03_d029'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d030'])]"
    anto "[renpy.substitute(dialogues['E01S03_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d032'])]"
    show ep01_2nddream15
    anto "[renpy.substitute(dialogues['E01S03_d033'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d034'])]"
    anto "[renpy.substitute(dialogues['E01S03_d035'])]"
    show ep01_2nddream16 with slowfade
    anto "[renpy.substitute(dialogues['E01S03_d036'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d037'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d038'])]"
    anto "[renpy.substitute(dialogues['E01S03_d039'])]"
    anto "[renpy.substitute(dialogues['E01S03_d040'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d041'])]"
    show ep01_2nddream17
    anto "[renpy.substitute(dialogues['E01S03_d042'])]"
    $ show_walkthrough("ep01_2nddream_menu")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S03_d043'])]"
        "Odd but charming":
            $ rm.update("antonella", "trust", 2)
            $ check_levels("antonella", "trust", 2)
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S03_d044'])]"
            anto "[renpy.substitute(dialogues['E01S03_d045'])]"
        "Mysterious":
            $ rm.update("antonella", "trust", 1)
            $ check_levels("antonella", "trust", 1)
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S03_d046'])]"
            anto "[renpy.substitute(dialogues['E01S03_d047'])]"
        "You make me uncomfortable":
            mc_s "[renpy.substitute(dialogues['E01S03_d048'])]"
            anto "[renpy.substitute(dialogues['E01S03_d049'])]"
            mc_s "[renpy.substitute(dialogues['E01S03_d050'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d051'])]"
    anto "[renpy.substitute(dialogues['E01S03_d052'])]"
    show ep01_2nddream18 with slowfade
    mc_s "[renpy.substitute(dialogues['E01S03_d053'])]"
    anto "[renpy.substitute(dialogues['E01S03_d054'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d055'])]"
    anto "[renpy.substitute(dialogues['E01S03_d056'])]"
    show ep01_2nddream19 with slowfade
    anto "[renpy.substitute(dialogues['E01S03_d057'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d058'])]"
    anto "[renpy.substitute(dialogues['E01S03_d059'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d060'])]"
    anto "[renpy.substitute(dialogues['E01S03_d061'])]"
    anto "[renpy.substitute(dialogues['E01S03_d062'])]"
    show ep01_2nddream20 with slowfade
    mc_s "[renpy.substitute(dialogues['E01S03_d063'])]"
    anto "[renpy.substitute(dialogues['E01S03_d064'])]"
    $ stopAudio(channel="music", subchannel=3, fadeout=2)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 4, 0)
    show ep01_2nddream21 with vpunch
    anto "[renpy.substitute(dialogues['E01S03_d065'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d066'])]"
    anto "[renpy.substitute(dialogues['E01S03_d067'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d068'])]"
    show ep01_2nddream22
    anto "[renpy.substitute(dialogues['E01S03_d069'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d070'])]"
    anto "[renpy.substitute(dialogues['E01S03_d071'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d072'])]"
    $ show_walkthrough("ep01_antodemo_menu")
    menu:
        "See nothing":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S03_d073'])]"
            anto "[renpy.substitute(dialogues['E01S03_d074'])]"
        "See something":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S03_d075'])]"
            anto "[renpy.substitute(dialogues['E01S03_d076'])]"
        "Same tree?":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S03_d077'])]"
            anto "[renpy.substitute(dialogues['E01S03_d078'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d079'])]"
    show ep01_2nddream23
    anto "[renpy.substitute(dialogues['E01S03_d080'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d081'])]"
    anto "[renpy.substitute(dialogues['E01S03_d082'])]"
    anto "[renpy.substitute(dialogues['E01S03_d083'])]"
    anto "[renpy.substitute(dialogues['E01S03_d084'])]"
    show ep01_2nddream24 with vpunch
    mc_s "[renpy.substitute(dialogues['E01S03_d085'])]"
    anto "[renpy.substitute(dialogues['E01S03_d086'])]"
    show ep01_2nddream25
    mc_s "[renpy.substitute(dialogues['E01S03_d087'])]"
    anto "[renpy.substitute(dialogues['E01S03_d088'])]"
    show ep01_2nddream26
    mc_s "[renpy.substitute(dialogues['E01S03_d089'])]"
    anto "[renpy.substitute(dialogues['E01S03_d090'])]"
    show ep01_2nddream27 with slowfade
    anto "[renpy.substitute(dialogues['E01S03_d091'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d092'])]"
    $ playAudio(antonella_sad_theme, "music", 2, True, 1, 0)
    show ep01_2nddream28 with slowfade
    anto "[renpy.substitute(dialogues['E01S03_d093'])]"
    anto "[renpy.substitute(dialogues['E01S03_d094'])]"
    anto "[renpy.substitute(dialogues['E01S03_d095'])]"
    anto "[renpy.substitute(dialogues['E01S03_d096'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d097'])]"
    show ep01_2nddream29
    anto "[renpy.substitute(dialogues['E01S03_d098'])]"
    anto "[renpy.substitute(dialogues['E01S03_d099'])]"
    anto "[renpy.substitute(dialogues['E01S03_d100'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d101'])]"
    show ep01_2nddream30
    anto "[renpy.substitute(dialogues['E01S03_d102'])]"
    anto "[renpy.substitute(dialogues['E01S03_d103'])]"
    anto "[renpy.substitute(dialogues['E01S03_d104'])]"
    anto "[renpy.substitute(dialogues['E01S03_d105'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d022'])]"
    show ep01_2nddream31
    anto "[renpy.substitute(dialogues['E01S03_d106'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d107'])]"
    show ep01_2nddream32
    anto "[renpy.substitute(dialogues['E01S03_d108'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d109'])]"
    anto "[renpy.substitute(dialogues['E01S03_d110'])]"
    anto "[renpy.substitute(dialogues['E01S03_d111'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_2nddream33
    mc_t "[renpy.substitute(dialogues['E01S03_d112'])]"
    mc_t "[renpy.substitute(dialogues['E01S03_d113'])]"
    mc_t "[renpy.substitute(dialogues['E01S03_d114'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d115'])]"
    show ep01_2nddream34
    anto "[renpy.substitute(dialogues['E01S03_d116'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d117'])]"
    anto "[renpy.substitute(dialogues['E01S03_d118'])]"
    anto "[renpy.substitute(dialogues['E01S03_d119'])]"
    anto "[renpy.substitute(dialogues['E01S03_d120'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d022'])]"
    show ep01_2nddream35
    anto "[renpy.substitute(dialogues['E01S03_d121'])]"
    anto "[renpy.substitute(dialogues['E01S03_d122'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d123'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d124'])]"
    show ep01_2nddream36
    anto "[renpy.substitute(dialogues['E01S03_d125'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d126'])]"
    anto "[renpy.substitute(dialogues['E01S03_d127'])]"
    $ playAudio(antonella_love, "music", 2, True, 1, 0)
    show ep01_2nddream37
    anto "[renpy.substitute(dialogues['E01S03_d128'])]"
    anto "[renpy.substitute(dialogues['E01S03_d129'])]"
    show ep01_2nddream38
    anto "[renpy.substitute(dialogues['E01S03_d130'])]"
    anto "[renpy.substitute(dialogues['E01S03_d131'])]"
    anto "[renpy.substitute(dialogues['E01S03_d132'])]"
    show ep01_2nddream39
    mc_s "[renpy.substitute(dialogues['E01S03_d133'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with clouds
    show ep01_2nddream40 with bokeh2
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    isa "[renpy.substitute(dialogues['E01S03_d134'])]"
    isa "[renpy.substitute(dialogues['E01S03_d135'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d136'])]"
    show ep01_2nddream41
    pause 1.0
    hide ep01_2nddream41
    show ep01_2nddream42
    isa "[renpy.substitute(dialogues['E01S03_d137'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d138'])]"
    isa "[renpy.substitute(dialogues['E01S03_d139'])]"
    show ep01_2nddream43
    mc_t "[renpy.substitute(dialogues['E01S03_d140'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d141'])]"
    isa "[renpy.substitute(dialogues['E01S03_d142'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d143'])]"
    show ep01_2nddream44
    isa "[renpy.substitute(dialogues['E01S03_d144'])]"
    isa "[renpy.substitute(dialogues['E01S03_d145'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d146'])]"
    isa "[renpy.substitute(dialogues['E01S03_d147'])]"
    mc_s "[renpy.substitute(dialogues['E01S03_d148'])]"
    show ep01_2nddream45 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S03_d149'])]"
    show ep01_2nddream46
    isa "[renpy.substitute(dialogues['E01S03_d150'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_3rddream

label ep01_3rddream:
    scene eigengrau with clouds_inverse
## -- SCENE: ANTONELLA'S LIBRARY
    show ep01_3rddream01 with clouds_inverse
    $ playAudio(sfx_library, "amb", 1, True, 1, 0)
    mc_t "[renpy.substitute(dialogues['E01S04_d001'])]"
    $ show_walkthrough("ep01_antolib_menu")
    menu:
        "Talk to her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S04_d002'])]"
            mc_s "[renpy.substitute(dialogues['E01S04_d003'])]"
            show ep01_3rddream02
            anto "[renpy.substitute(dialogues['E01S04_d004'])]"
            anto "[renpy.substitute(dialogues['E01S04_d005'])]"
            mc_s "[renpy.substitute(dialogues['E01S04_d006'])]"
        "Check her":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S04_d007'])]"
            show ep01_3rddream03
            mc_t "[renpy.substitute(dialogues['E01S04_d008'])]"
            mc_t "[renpy.substitute(dialogues['E01S04_d009'])]"
            show ep01_3rddream02
            anto "[renpy.substitute(dialogues['E01S04_d005'])]"
            anto "[renpy.substitute(dialogues['E01S04_d011'])]"
            anto "[renpy.substitute(dialogues['E01S04_d004'])]"
            mc_s "[renpy.substitute(dialogues['E01S04_d006'])]"
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)
    show ep01_3rddream04 with vpunch
    anto "[renpy.substitute(dialogues['E01S04_d014'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d015'])]"
    mc_t "[renpy.substitute(dialogues['E01S04_d016'])]"
    show ep01_3rddream05
    anto "[renpy.substitute(dialogues['E01S04_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d018'])]"
    show ep01_3rddream06
    anto "[renpy.substitute(dialogues['E01S04_d019'])]"
    anto "[renpy.substitute(dialogues['E01S04_d020'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d021'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d022'])]"
    $ playAudio(antonella_love, "music", 1, True, 2.5, 0)
    show ep01_3rddream07 with hpunch
    mc_s "[renpy.substitute(dialogues['E01S04_d023'])]"
    show ep01_3rddream08 with vpunch
    anto "[renpy.substitute(dialogues['E01S04_d024'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d025'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d026'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d027'])]"
    anto "[renpy.substitute(dialogues['E01S04_d028'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d029'])]"
    show ep01_3rddream09
    anto "[renpy.substitute(dialogues['E01S04_d030'])]"
    anto "[renpy.substitute(dialogues['E01S04_d031'])]"
    anto "[renpy.substitute(dialogues['E01S04_d032'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d033'])]"
    anto "[renpy.substitute(dialogues['E01S04_d034'])]"
    anto "[renpy.substitute(dialogues['E01S04_d035'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d036'])]"
    $ unlock_memory("m_ep01_library")
    show ep01_3rddream10
    anto "[renpy.substitute(dialogues['E01S04_d037'])]"
    anto "[renpy.substitute(dialogues['E01S04_d038'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d039'])]"
    show ep01_3rddream11
    anto "[renpy.substitute(dialogues['E01S04_d040'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d041'])]"
    anto "[renpy.substitute(dialogues['E01S04_d042'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d043'])]"
    anto "[renpy.substitute(dialogues['E01S04_d044'])]"
    show ep01_3rddream12
    anto "[renpy.substitute(dialogues['E01S04_d045'])]"
    anto "[renpy.substitute(dialogues['E01S04_d046'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d047'])]"
    anto "[renpy.substitute(dialogues['E01S04_d048'])]"
    anto "[renpy.substitute(dialogues['E01S04_d049'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d050'])]"
    show ep01_3rddream13
    anto "[renpy.substitute(dialogues['E01S04_d051'])]"
    anto "[renpy.substitute(dialogues['E01S04_d052'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d053'])]"
    anto "[renpy.substitute(dialogues['E01S04_d054'])]"
    show ep01_3rddream14
    mc_s "[renpy.substitute(dialogues['E01S04_d055'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d056'])]"
    anto "[renpy.substitute(dialogues['E01S04_d057'])]"
    anto "[renpy.substitute(dialogues['E01S04_d058'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d059'])]"
    show ep01_3rddream15
    mc_t "[renpy.substitute(dialogues['E01S04_d060'])]"
    mc_t "[renpy.substitute(dialogues['E01S04_d061'])]"
    show ep01_3rddream16
    anto "[renpy.substitute(dialogues['E01S04_d062'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d063'])]"
    anto "[renpy.substitute(dialogues['E01S04_d064'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d065'])]"
    anto "[renpy.substitute(dialogues['E01S04_d066'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d067'])]"
    show ep01_3rddream17
    anto "[renpy.substitute(dialogues['E01S04_d068'])]"
    anto "[renpy.substitute(dialogues['E01S04_d069'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d070'])]"
    show ep01_3rddream18
    anto "[renpy.substitute(dialogues['E01S04_d071'])]"
    anto "[renpy.substitute(dialogues['E01S04_d072'])]"
    anto "[renpy.substitute(dialogues['E01S04_d073'])]"
    mc_s "[renpy.substitute(dialogues['E01S04_d074'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with clouds
    show ep01_3rddream19 with bokeh
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    mc_t "[renpy.substitute(dialogues['E01S04_d067'])]"
    $ playAudio(sfx_phone, "sfx", 1, True, 0, 0)
    mc_t "[renpy.substitute(dialogues['E01S04_d076'])]"
    ##SMS WINDOW
    call screen phone_icons("ep01_sms01")
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    show ep01_3rddream20 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S04_d078'])]"
    jump ep01_smslater

label ep01_smslater:
    scene eigengrau with dissolve
    show ep01_3rddream22 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S04_d079'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d161'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_pregame

label ep01_pregame:
    scene eigengrau with clouds_inverse
##RM.POINTS.TRACK (antonella, trust, +1)
# --
## -- SCENE: ANTONELLA'S FAVOR
    show ep01_pregame01 with clouds_inverse
    $ playAudio(sfx_park2, "amb", 1, True, 1.5, 0)
    mc_t "[renpy.substitute(dialogues['E01S05_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d002'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d003'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d004'])]"
    show ep01_pregame02 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S05_d005'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d006'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d007'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d008'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d009'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d010'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d011'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d012'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d013'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d014'])]"
    $ playAudio(antonella_love, "music", 1, True, 1, 0)
    show ep01_pregame03 with vpunch
    anto "[renpy.substitute(dialogues['E01S05_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d016'])]"
    show ep01_pregame04
    anto "[renpy.substitute(dialogues['E01S05_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d018'])]"
    anto "[renpy.substitute(dialogues['E01S05_d019'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d020'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d021'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d022'])]"
    show ep01_pregame05
    anto "[renpy.substitute(dialogues['E01S05_d023'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d024'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d025'])]"
    show ep01_pregame06
    anto "[renpy.substitute(dialogues['E01S05_d026'])]"
    anto "[renpy.substitute(dialogues['E01S05_d027'])]"
    anto "[renpy.substitute(dialogues['E01S05_d028'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d029'])]"
    show ep01_pregame07
    anto "[renpy.substitute(dialogues['E01S05_d030'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d031'])]"
    show ep01_pregame08 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S05_d032'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d033'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d034'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d035'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d036'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d037'])]"
    show ep01_pregame11
    anto "[renpy.substitute(dialogues['E01S05_d038'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d039'])]"
    show ep01_pregame10
    anto "[renpy.substitute(dialogues['E01S05_d040'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d041'])]"
    anto "[renpy.substitute(dialogues['E01S05_d042'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d042x'])]"
    show ep01_pregame09
    anto "[renpy.substitute(dialogues['E01S05_d043'])]"
    anto "[renpy.substitute(dialogues['E01S05_d044'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d045'])]"
    anto "[renpy.substitute(dialogues['E01S05_d046'])]"
    anto "[renpy.substitute(dialogues['E01S05_d047'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d048'])]"
    show ep01_pregame12 with vpunch
    anto "[renpy.substitute(dialogues['E01S05_d049'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d050'])]"
    anto "[renpy.substitute(dialogues['E01S05_d051'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d052'])]"
    anto "[renpy.substitute(dialogues['E01S05_d053'])]"
    show ep01_pregame13 with slowfade
    anto "[renpy.substitute(dialogues['E01S05_d054'])]"
    anto "[renpy.substitute(dialogues['E01S05_d055'])]"
    anto "[renpy.substitute(dialogues['E01S05_d056'])]"
    anto "[renpy.substitute(dialogues['E01S05_d057'])]"
    anto "[renpy.substitute(dialogues['E01S05_d058'])]"
    anto "[renpy.substitute(dialogues['E01S05_d059'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d060'])]"
    anto "[renpy.substitute(dialogues['E01S05_d061'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d062'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d063'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d064'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d065'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    ## MOTHER'S OFFICE
    scene eigengrau with dissolve
    show ep01_pregame14 with slowfade
    $ playAudio(sfx_earlymor, "amb", 2, True, 2, 0)
    mc_s "[renpy.substitute(dialogues['E01S05_d066'])]"
    anto "[renpy.substitute(dialogues['E01S05_d067'])]"
    anto "[renpy.substitute(dialogues['E01S05_d068'])]"
    anto "[renpy.substitute(dialogues['E01S05_d069'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d070'])]"
    show ep01_pregame15
    mc_s "[renpy.substitute(dialogues['E01S05_d071'])]"
    anto "[renpy.substitute(dialogues['E01S05_d072'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d073'])]"
    anto "[renpy.substitute(dialogues['E01S05_d074'])]"
    anto "[renpy.substitute(dialogues['E01S05_d075'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d076'])]"
    show ep01_pregame16 with hpunch
    mc_s "[renpy.substitute(dialogues['E01S05_d077'])]"
    anto "[renpy.substitute(dialogues['E01S05_d078'])]"
    anto "[renpy.substitute(dialogues['E01S05_d079'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d080'])]"
    anto "[renpy.substitute(dialogues['E01S05_d081'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d082'])]"
    show ep01_pregame17
    anto "[renpy.substitute(dialogues['E01S05_d083'])]"
    anto "[renpy.substitute(dialogues['E01S05_d084'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d085'])]"
    anto "[renpy.substitute(dialogues['E01S05_d086'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d087'])]"
    show ep01_pregame18
    anto "[renpy.substitute(dialogues['E01S05_d088'])]"
    anto "[renpy.substitute(dialogues['E01S05_d089'])]"
    anto "[renpy.substitute(dialogues['E01S05_d090'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d091'])]"
    show ep01_pregame19 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S05_d092'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d093'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d094'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d095'])]"
    anto "[renpy.substitute(dialogues['E01S04_d022'])]"
    show ep01_pregame20 with hpunch
    anto "[renpy.substitute(dialogues['E01S05_d096'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d097'])]"
    anto "[renpy.substitute(dialogues['E01S05_d098'])]"
    show ep01_pregame21
    mc_s "[renpy.substitute(dialogues['E01S05_d099'])]"
    anto "[renpy.substitute(dialogues['E01S05_d100'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d085'])]"
    show ep01_pregame22
    anto "[renpy.substitute(dialogues['E01S05_d101'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d102'])]"
    anto "[renpy.substitute(dialogues['E01S05_d103'])]"
    show ep01_pregame23 with slowfade
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(antonella_past_theme, "music", 2, True, 1.5, 0)
    mc_s "[renpy.substitute(dialogues['E01S05_d104'])]"
    anto "[renpy.substitute(dialogues['E01S05_d105'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d106'])]"
    anto "[renpy.substitute(dialogues['E01S05_d107'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d108'])]"
    show ep01_pregame24
    anto "[renpy.substitute(dialogues['E01S05_d109'])]"
    anto "[renpy.substitute(dialogues['E01S05_d110'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d111'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d112'])]"
    show ep01_pregame25
    anto "[renpy.substitute(dialogues['E01S05_d113'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d114'])]"
    anto "[renpy.substitute(dialogues['E01S05_d115'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d116'])]"
    anto "[renpy.substitute(dialogues['E01S05_d117'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d118'])]"
    show ep01_pregame26
    anto "[renpy.substitute(dialogues['E01S05_d119'])]"
    anto "[renpy.substitute(dialogues['E01S05_d120'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d121'])]"
    anto "[renpy.substitute(dialogues['E01S05_d122'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d123'])]"
    show ep01_pregame28
    anto "[renpy.substitute(dialogues['E01S05_d124'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d125'])]"
    anto "[renpy.substitute(dialogues['E01S05_d126'])]"
    anto "[renpy.substitute(dialogues['E01S05_d127'])]"
    anto "[renpy.substitute(dialogues['E01S05_d127b'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d128'])]"
    show ep01_pregame27
    anto "[renpy.substitute(dialogues['E01S05_d129'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d130'])]"
    anto "[renpy.substitute(dialogues['E01S05_d131'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d132'])]"
    anto "[renpy.substitute(dialogues['E01S05_d133'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d134'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_pregame29 with hpunch
    anto "[renpy.substitute(dialogues['E01S05_d135'])]"
    anto "[renpy.substitute(dialogues['E01S05_d136'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d137'])]"
    anto "[renpy.substitute(dialogues['E01S05_d138'])]"
    anto "[renpy.substitute(dialogues['E01S05_d139'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d140'])]"
    anto "[renpy.substitute(dialogues['E01S05_d141'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d141b'])]"
    show ep01_pregame30 with hpunch
    mc_s "[renpy.substitute(dialogues['E01S05_d142'])]"
    anto "[renpy.substitute(dialogues['E01S05_d143'])]"
    anto "[renpy.substitute(dialogues['E01S05_d144'])]"
    anto "[renpy.substitute(dialogues['E01S05_d145'])]"
    $ show_walkthrough("ep01_pregame_menu")
    menu:
        "Hug tenderly":
            $ rm.update("antonella", "trust", 1)
            $ check_levels("antonella", "trust", 1)
            $ ep01_hug = True
            hide screen walkthrough_screen
            show ep01_pregame31 with hpunch
            mc_s "[renpy.substitute(dialogues['E01S05_d146'])]"
            mc_s "[renpy.substitute(dialogues['E01S05_d147'])]"
            show ep01_pregame32
            anto "[renpy.substitute(dialogues['E01S05_d148'])]"
            mc_t "[renpy.substitute(dialogues['E01S05_d149'])]"
        "Hesitate awkwardly":
            hide screen walkthrough_screen
            show ep01_pregame33 with vpunch
            mc_t "[renpy.substitute(dialogues['E01S05_d150'])]"
            mc_t "[renpy.substitute(dialogues['E01S05_d151'])]"
            mc_t "[renpy.substitute(dialogues['E01S05_d152'])]"
            mc_t "[renpy.substitute(dialogues['E01S05_d153'])]"
            anto "[renpy.substitute(dialogues['E01S05_d154'])]"
            mc_s "[renpy.substitute(dialogues['E01S05_d155'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    ## PHONE CALL #2
    scene eigengrau with clouds
    show ep01_pregame34 with bokeh
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    $ playAudio(sfx_phone, "sfx", 1, True, 0, 0)
    mc_t "[renpy.substitute(dialogues['E01S05_d156'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d157'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d158'])]"
    ##SMS WINDOW
    call screen phone_icons("ep01_sms02")
    show ep01_pregame35 with slowfade
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    mc_t "[renpy.substitute(dialogues['E01S05_d231'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d159'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d160'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d161'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_pregame2

label ep01_pregame2:
    scene eigengrau with clouds_inverse
    ##BACK TO DREAM
    show ep01_pregame37 with clouds_inverse
    nvl clear
    $ playAudio(sfx_earlymor, "amb", 2, True, 2, 0)
    anto "[renpy.substitute(dialogues['E01S05_d162'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d163'])]"
    anto "[renpy.substitute(dialogues['E01S05_d164'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d165'])]"
    anto "[renpy.substitute(dialogues['E01S05_d166'])]"
    show ep01_pregame38
    anto "[renpy.substitute(dialogues['E01S05_d167'])]"
    anto "[renpy.substitute(dialogues['E01S05_d168'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d169'])]"
    show ep01_pregame39
    anto "[renpy.substitute(dialogues['E01S05_d170'])]"
    anto "[renpy.substitute(dialogues['E01S05_d171'])]"
    anto "[renpy.substitute(dialogues['E01S05_d172'])]"
    anto "[renpy.substitute(dialogues['E01S05_d173'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d174'])]"
    show ep01_pregame40
    anto "[renpy.substitute(dialogues['E01S05_d175'])]"
    anto "[renpy.substitute(dialogues['E01S05_d176'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d177'])]"
    show ep01_pregame41
    anto "[renpy.substitute(dialogues['E01S05_d178'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d179'])]"
    anto "[renpy.substitute(dialogues['E01S05_d180'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d181'])]"
    ##ADD POINTS... LOW POINT NO THE GAME, 5 POINTS GO TO  THE GAME
    if rm.get("antonella", "trust") < 4:
        anto "[renpy.substitute(dialogues['E01S05_d182'])]"
        jump q3_date
    else:
        anto "[renpy.substitute(dialogues['E01S05_d182b'])]"
        pass
    show ep01_pregame42
    anto "[renpy.substitute(dialogues['E01S05_d183'])]"
    anto "[renpy.substitute(dialogues['E01S05_d184'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d185'])]"
    show ep01_pregame43
    anto "[renpy.substitute(dialogues['E01S05_d186'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d187'])]"
    show ep01_pregame44
    anto "[renpy.substitute(dialogues['E01S05_d188'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d189'])]"
    anto "[renpy.substitute(dialogues['E01S05_d190'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d191'])]"
    show ep01_pregame45
    anto "[renpy.substitute(dialogues['E01S05_d192'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d193'])]"
    anto "[renpy.substitute(dialogues['E01S05_d194'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d195'])]"
    show ep01_pregame46  with slowfade
    mc_s "[renpy.substitute(dialogues['E01S05_d196'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d197'])]"
    anto "[renpy.substitute(dialogues['E01S05_d198'])]"
    show ep01_pregame47
    anto "[renpy.substitute(dialogues['E01S05_d199'])]"
    anto "[renpy.substitute(dialogues['E01S05_d200'])]"
    anto "[renpy.substitute(dialogues['E01S05_d201'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d202'])]"
    show ep01_pregame48
    anto "[renpy.substitute(dialogues['E01S05_d203'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d204'])]"
    anto "[renpy.substitute(dialogues['E01S05_d205'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d206'])]"
    anto "[renpy.substitute(dialogues['E01S05_d207'])]"
    show ep01_pregame49
    anto "[renpy.substitute(dialogues['E01S05_d208'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d209'])]"
    anto "[renpy.substitute(dialogues['E01S05_d210'])]"
    show ep01_pregame50
    anto "[renpy.substitute(dialogues['E01S05_d211'])]"
    anto "[renpy.substitute(dialogues['E01S05_d212'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d213'])]"
    anto "[renpy.substitute(dialogues['E01S05_d214'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d215'])]"
    show ep01_pregame51
    anto "[renpy.substitute(dialogues['E01S05_d216'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d217'])]"
    anto "[renpy.substitute(dialogues['E01S05_d218'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d219'])]"
    show ep01_pregame52
    anto "[renpy.substitute(dialogues['E01S05_d220'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d221'])]"
    show ep01_pregame53
    anto "[renpy.substitute(dialogues['E01S05_d222'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d223'])]"
    show ep01_pregame54
    anto "[renpy.substitute(dialogues['E01S05_d224'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d225'])]"
    anto "[renpy.substitute(dialogues['E01S05_d226'])]"
    mc_s "[renpy.substitute(dialogues['E01S05_d227'])]"
    $ playAudio(antonella_game_theme, "music", 2, True, 2.5, 0)
    show ep01_pregame55
    anto "[renpy.substitute(dialogues['E01S05_d228'])]"
    anto "[renpy.substitute(dialogues['E01S05_d229'])]"
    anto "[renpy.substitute(dialogues['E01S05_d230'])]"
    jump ep01_thegame

label ep01_thegame:
    scene eigengrau with slowfade
## -- SCENE: ANTONELLA'S GAME REVEAL
    show ep01_game01 with dissolve
    mc_s "[renpy.substitute(dialogues['E01S06_d001'])]"
    anto "[renpy.substitute(dialogues['E01S06_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d003'])]"
    show ep01_game02
    anto "[renpy.substitute(dialogues['E01S06_d004'])]"
    anto "[renpy.substitute(dialogues['E01S06_d005'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d006'])]"
    show ep01_game03
    anto "[renpy.substitute(dialogues['E01S06_d007'])]"
    mc_t "[renpy.substitute(dialogues['E01S06_d008'])]"
    mc_t "[renpy.substitute(dialogues['E01S06_d009'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d010'])]"
    show ep01_game04
    anto "[renpy.substitute(dialogues['E01S06_d011'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d012'])]"
    show ep01_game05
    anto "[renpy.substitute(dialogues['E01S06_d013'])]"
    anto "[renpy.substitute(dialogues['E01S06_d014'])]"
    anto "[renpy.substitute(dialogues['E01S06_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d016'])]"
    show ep01_game06
    anto "[renpy.substitute(dialogues['E01S06_d017'])]"
    anto "[renpy.substitute(dialogues['E01S06_d018'])]"
    anto "[renpy.substitute(dialogues['E01S06_d019'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d020'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_game07
    anto "[renpy.substitute(dialogues['E01S06_d021'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d022'])]"
    anto "[renpy.substitute(dialogues['E01S06_d023'])]"
    mc_s "[renpy.substitute(dialogues['E01S06_d024'])]"
    anto "[renpy.substitute(dialogues['E01S06_d025'])]"
    anto "[renpy.substitute(dialogues['E01S06_d026'])]"
    $ playAudio(mc_thinking_theme, "music", 2, True, 2.5, 0)

##1ST QUESTION BY MC
    show ep01_game08 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S07_d001'])]"
    $ show_walkthrough("ep01_game_menu1")
    $ ep01_q1 = random_menu(
        mc_s,  # The character who speaks before the menu. If none, use None.
        "My first question is...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Ask about an American writer", "q1_usa"),
            (True, "Ask about an Argentine writer", "q1_arg"),
            (True, "Ask about an English writer", "q1_uk"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q1 == "q1_arg":
        hide screen walkthrough_screen
        mc_s "[renpy.substitute(dialogues['E01S07_d002'])]"
        $ ep01_mcquestion += 1
        jump ep01_mcpoint_1
    elif ep01_q1 in ["q1_usa", "q1_uk"]:
        hide screen walkthrough_screen
        if ep01_q1 == "q1_usa":
            mc_s "[renpy.substitute(dialogues['E01S07_d003'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S07_d004'])]"
        show ep01_game18 with vpunch
        anto "[renpy.substitute(dialogues['E01S07_d005'])]"
        mc_s "[renpy.substitute(dialogues['E01S07_d006'])]"
        mc_t "[renpy.substitute(dialogues['E01S07_d007'])]"
        show ep01_game19
        if ep01_q1 == "q1_usa":
            anto "[renpy.substitute(dialogues['E01S07_d008'])]"
            anto "[renpy.substitute(dialogues['E01S07_d009'])]"
        else:
            anto "[renpy.substitute(dialogues['E01S07_d010'])]"
            anto "[renpy.substitute(dialogues['E01S07_d011'])]"
        show ep01_game20
        mc_s "[renpy.substitute(dialogues['E01S07_d012'])]"
        mc_s "[renpy.substitute(dialogues['E01S07_d013'])]"
        mc_t "[renpy.substitute(dialogues['E01S07_d014'])]"
        $ ep01_mcquestion += 1
        jump ep01_thegame_q2

label ep01_mcpoint_1:
    scene eigengrau with slowfade
##MC WINS 1 POINT FOR THE FIRST TIME
    show ep01_game09 with hpunch
    mc_t "[renpy.substitute(dialogues['E01S08_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01S08_d002'])]"
    mc_t "[renpy.substitute(dialogues['E01S08_d003'])]"
    if ep01_mcquestion == 1:
        mc_s "[renpy.substitute(dialogues['E01S08_d004'])]"
    elif ep01_mcquestion == 2:
        mc_s "[renpy.substitute(dialogues['E01S08_d005'])]"
    else:
        pass
    show ep01_game10 with vpunch
    if ep01_mcquestion == 1:
        anto "[renpy.substitute(dialogues['E01S08_d006'])]"
        mc_s "[renpy.substitute(dialogues['E01S08_d007'])]"
        mc_s "[renpy.substitute(dialogues['E01S08_d008'])]"
    elif ep01_mcquestion == 2:
        anto "[renpy.substitute(dialogues['E01S08_d009'])]"
        mc_s "[renpy.substitute(dialogues['E01S08_d010'])]"
        mc_s "[renpy.substitute(dialogues['E01S08_d011'])]"
    else:
        anto "[renpy.substitute(dialogues['E01S08_d012'])]"
        anto "[renpy.substitute(dialogues['E01S08_d013'])]"
        mc_t "[renpy.substitute(dialogues['E01S08_d014'])]"
    show ep01_game11 with hpunch
    mc_t "[renpy.substitute(dialogues['E01S08_d015'])]"
    mc_t "[renpy.substitute(dialogues['E01S08_d016'])]"
    mc_t "[renpy.substitute(dialogues['E01S08_d017'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.5)
    $ playAudio(antonella_sexy_theme, "music", 4, True, 1.5, 0)
    show ep01_game12 with slowfade
    anto "[renpy.substitute(dialogues['E01S08_d018'])]"
    mc_t "[renpy.substitute(dialogues['E01S08_d019'])]"
    show ep01_game13 with flash
    anto "[renpy.substitute(dialogues['E01S08_d020'])]"
    anto "[renpy.substitute(dialogues['E01S08_d021'])]"
    show ep01_game14 with flash
    anto "[renpy.substitute(dialogues['E01S08_d022'])]"
    if ep01_mcquestion <= 2:
        anto "[renpy.substitute(dialogues['E01S08_d023'])]"
    else:
        pass
    show ep01_game15 with flash
    if ep01_mcquestion <= 2:
        anto "[renpy.substitute(dialogues['E01S08_d024'])]"
    else:
        anto "[renpy.substitute(dialogues['E01S08_d025'])]"
    show ep01_game16  with flash
    if ep01_mcquestion <= 2:
        anto "[renpy.substitute(dialogues['E01S08_d026'])]"
    else:
        pass
    mc_t "[renpy.substitute(dialogues['E01S08_d027'])]"
    show ep01_game17
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
    anto "[renpy.substitute(dialogues['E01S08_d028'])]"
    if ep01_mcquestion <= 2:
        mc_s "[renpy.substitute(dialogues['E01S08_d029'])]"
        anto "[renpy.substitute(dialogues['E01S08_d030'])]"
    else:
        mc_s "[renpy.substitute(dialogues['E01S08_d031'])]"
    $ ep01_anto_clothing += 1
    if ep01_mcquestion == 1:
        jump ep01_thegame_q2
    elif ep01_mcquestion == 2:
        jump ep01_thegame_q4
label ep01_thegame_q2:
    scene eigengrau with dissolve
##1ST QUESTION BY ANTONELLA
    show ep01_game21 with slowfade
    anto "[renpy.substitute(dialogues['E01S09x_d001'])]"
    anto "[renpy.substitute(dialogues['E01S09x_d002'])]"
    mc_t "[renpy.substitute(dialogues['E01S09x_d003'])]"
    anto "[renpy.substitute(dialogues['E01S09x_d004'])]"
    $ show_walkthrough("ep01_game_menu2")
    $ ep01_q2 = random_menu(
        mc_t,  # The character who speaks before the menu. If none, use None.
        "Who the hell wrote that...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Niccolò Machiavelli", "ep01_q2_1"),
            (True, "Dante Alighieri", "ep01_q2_2"),
            (True, "Umberto Eco", "ep01_q2_3"),
        ]
    )

    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q2 == "ep01_q2_1":
        hide screen walkthrough_screen
        mc_s "[renpy.substitute(dialogues['E01S09x_d005'])]"
        show ep01_game23
        anto "[renpy.substitute(dialogues['E01S09x_d012'])]"
        mc_s "[renpy.substitute(dialogues['E01S09x_d013'])]"
        jump ep01_thegame_q3
    elif ep01_q2 in ["ep01_q2_2", "ep01_q2_3"]:
        hide screen walkthrough_screen
        if ep01_q2 == "ep01_q2_2":
            mc_s "[renpy.substitute(dialogues['E01S09x_d006'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S09x_d007'])]"
        show ep01_game25
        if ep01_q2 == "ep01_q2_2":
            anto "[renpy.substitute(dialogues['E01S09x_d008'])]"
        else:
            anto "[renpy.substitute(dialogues['E01S09x_d009'])]"
        mc_s "[renpy.substitute(dialogues['E01S09x_d010'])]"
        anto "[renpy.substitute(dialogues['E01S09x_d011'])]"
        $ ep01_mc_clothing += 1
        jump ep01_thegame_mc_nude

label ep01_thegame_mc_nude: ##*
    scene eigengrau with slowfade
##MC NUDE ANIMATION
    if ep01_mc_clothing == 1:
        show ep01_game27 with dissolve
        mc_s "[renpy.substitute(dialogues['E01S15_d001'])]"
        mc_s "[renpy.substitute(dialogues['E01S15_d002'])]"
        if ep01_mcquestion == 1:
            jump ep01_thegame_q3
        elif ep01_mcquestion == 2:
            jump ep01_thegame_q5
        else:
            hide ep01_game94
            hide ep01_game107
            jump ep01_endgame
    elif ep01_mc_clothing == 2:
        show ep01_game28 with dissolve
        mc_s "[renpy.substitute(dialogues['E01S15_d003'])]"
        mc_s "[renpy.substitute(dialogues['E01S15_d004'])]"
        if ep01_mcquestion == 2:
            jump ep01_thegame_q5
        else:
            hide ep01_game94
            hide ep01_game107
            jump ep01_endgame
    else:
        show ep01_game29 with dissolve
        mc_s "[renpy.substitute(dialogues['E01S15_d005'])]" 
        show ep01_game32 with hpunch
        anto "[renpy.substitute(dialogues['E01S15_d006'])]"
        mc_s "[renpy.substitute(dialogues['E01S15_d007'])]"
        jump ep01_endgame

label ep01_thegame_q3:
    scene eigengrau with slowfade
##2ND QUESTION BY MC
    show ep01_game33
    anto "[renpy.substitute(dialogues['E01S09_d001'])]"
    if ep01_anto_clothing == 1:
        anto "[renpy.substitute(dialogues['E01S09_d002'])]"
    else:
        anto "[renpy.substitute(dialogues['E01S09_d003'])]"
    $ show_walkthrough("ep01_game_menu3")
    $ ep01_q3 = random_menu(
        mc_t,  # The character who speaks before the menu. If none, use None.
        "What should I ask?",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Ask about \"A Tale of Two Cities\"", "q3_2city"),
            (True, "Ask about \"The Little Prince\"", "q3_lilprince"),
            (True, "Ask about \"Demian\"", "q3_demian"),
        ]
    )

    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q3 == "q3_demian":
        hide screen walkthrough_screen
        if ep01_anto_clothing == 0:
            $ ep01_mcquestion += 1
            jump ep01_mcpoint_1
        else:   
            $ ep01_mcquestion += 1
            jump ep01_mcpoint_2
    elif ep01_q3 in ["q3_2city", "q3_lilprince"]:
        hide screen walkthrough_screen
        show ep01_game45
        if ep01_q3 == "q3_2city":
            mc_s "[renpy.substitute(dialogues['E01S09_d004'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S09_d005'])]"
        if ep01_anto_clothing >= 1:
            mc_t "[renpy.substitute(dialogues['E01S09_d006'])]"
        else:
            mc_t "[renpy.substitute(dialogues['E01S09_d007'])]"
        show ep01_game47
        if ep01_q3 == "q3_2city":
            anto "[renpy.substitute(dialogues['E01S09_d008'])]"
            anto "[renpy.substitute(dialogues['E01S09_d009'])]"
        else:
            anto "[renpy.substitute(dialogues['E01S09_d010'])]"
            anto "[renpy.substitute(dialogues['E01S09_d011'])]"
        show ep01_game49
        mc_t "[renpy.substitute(dialogues['E01S09_d012'])]"
        mc_s "[renpy.substitute(dialogues['E01S09_d013'])]"
        $ ep01_mcquestion += 1
        jump ep01_thegame_q4

label ep01_mcpoint_2:
    scene eigengrau with slowfade
##MC WINS 2 POINTS (or 1 if failed)
    if ep01_anto_clothing == 0:
        jump ep01_mcpoint_1
    else:
        show ep01_game35 with dissolve
        mc_s "[renpy.substitute(dialogues['E01S10_d001'])]"
        mc_t "[renpy.substitute(dialogues['E01S10_d002'])]"
        mc_s "[renpy.substitute(dialogues['E01S10_d003'])]"
        show ep01_game36
        anto "[renpy.substitute(dialogues['E01S10_d004'])]"
        mc_s "[renpy.substitute(dialogues['E01S10_d005'])]"
        mc_t "[renpy.substitute(dialogues['E01S10_d006'])]"
        show ep01_game37 with hpunch
        mc_s "[renpy.substitute(dialogues['E01S10_d007'])]"
        anto "[renpy.substitute(dialogues['E01S10_d008'])]"
        mc_s "[renpy.substitute(dialogues['E01S10_d009'])]"
        mc_t "[renpy.substitute(dialogues['E01S10_d010'])]"
        mc_t "[renpy.substitute(dialogues['E01S10_d011'])]"
        $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=4, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
        show ep01_game38 with slowfade
        anto "[renpy.substitute(dialogues['E01S10_d012'])]"
        anto "[renpy.substitute(dialogues['E01S10_d013'])]"
        show ep01_game39 with flash
        anto "[renpy.substitute(dialogues['E01S10_d014'])]"
        anto "[renpy.substitute(dialogues['E01S10_d015'])]"
        show ep01_game40 with flash
        anto "[renpy.substitute(dialogues['E01S10_d016'])]"
        show ep01_game41 with flash
        anto "[renpy.substitute(dialogues['E01S10_d017'])]"
        anto "[renpy.substitute(dialogues['E01S10_d018'])]"
        show ep01_game42 with flash
        mc_s "[renpy.substitute(dialogues['E01S10_d019'])]"
        $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
        show ep01_game43
        anto "[renpy.substitute(dialogues['E01S10_d020'])]"
        show ep01_game44
        anto "[renpy.substitute(dialogues['E01S10_d021'])]"
        anto "[renpy.substitute(dialogues['E01S10_d022'])]"
        mc_t "[renpy.substitute(dialogues['E01S10_d023'])]"
        mc_s "[renpy.substitute(dialogues['E01S10_d024'])]"
        $ ep01_anto_clothing +=1
        jump ep01_thegame_q4

label ep01_thegame_q4:
    scene eigengrau with slowfade
##2ND QUESTION BY ANTONELLA
    show ep01_game51 with dissolve
    anto "[renpy.substitute(dialogues['E01S11_d001'])]"
    anto "[renpy.substitute(dialogues['E01S11_d002'])]"
    mc_t "[renpy.substitute(dialogues['E01S11_d003'])]"
    anto "[renpy.substitute(dialogues['E01S11_d004'])]"
    $ show_walkthrough("ep01_game_menu4")
    $ ep01_q4 = random_menu(
        mc_t,  # The character who speaks before the menu. If none, use None.
        "I remember it was a Russian dude...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Nikos Kazantzakis", "ep01_q4_1"),
            (True, "Vladimir Nabokov", "ep01_q4_2"),
            (True, "Fyodor Dostoevsky", "ep01_q4_3"),
        ]
    )

    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q4 == "ep01_q4_2":
        hide screen walkthrough_screen
        mc_s "[renpy.substitute(dialogues['E01S11_d005'])]"
        show ep01_game52 with hpunch
        anto "[renpy.substitute(dialogues['E01S11_d006'])]"
        anto "[renpy.substitute(dialogues['E01S11_d007'])]"
        mc_s "[renpy.substitute(dialogues['E01S11_d008'])]"
        jump ep01_thegame_q5
    elif ep01_q4 in ["ep01_q4_1", "ep01_q4_3"]:
        hide screen walkthrough_screen
        if ep01_q4 == "ep01_q4_1":
            mc_s "[renpy.substitute(dialogues['E01S11_d009'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S11_d010'])]"
        show ep01_game59 with hpunch
        anto "[renpy.substitute(dialogues['E01S11_d011'])]"
        anto "[renpy.substitute(dialogues['E01S11_d012'])]"
        show ep01_game56
        mc_s "[renpy.substitute(dialogues['E01S11_d013'])]"
        $ ep01_mc_clothing += 1
        jump ep01_thegame_mc_nude

label ep01_thegame_q5:
    scene eigengrau with slowfade
##3RD QUESTION BY MC
    show ep01_game64 with dissolve
    mc_t "[renpy.substitute(dialogues['E01S12_d001'])]"
    $ show_walkthrough("ep01_game_menu5")
    $ ep01_q5 = random_menu(
        mc_s,  # The character who speaks before the menu. If none, use None.
        "Ughh... Okay... Here goes nothing...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Something about Agatha Christie", "q1_agatha"),
            (True, "Something about \"The Count of Monte Cristo\"", "q1_mcrist"),
            (True, "Something about \"War and Peace\"", "q1_warpeace"),
        ]
    )

    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q5 == "q1_agatha":
        hide screen walkthrough_screen
        mc_s "[renpy.substitute(dialogues['E01S12_d003'])]"
        mc_t "[renpy.substitute(dialogues['E01S12_d004'])]"
        $ ep01_mcquestion += 1
        jump ep01_mcpoint_3
    elif ep01_q5 in ["q1_mcrist", "q1_warpeace"]:
        hide screen walkthrough_screen
        if ep01_q5 == "q1_mcrist":
            mc_s "[renpy.substitute(dialogues['E01S12_d005'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S12_d006'])]"
        mc_t "[renpy.substitute(dialogues['E01S12_d007'])]"
        show ep01_game67
        if ep01_q5 == "q1_mcrist":
            anto "[renpy.substitute(dialogues['E01S12_d008'])]"
        else:
            anto "[renpy.substitute(dialogues['E01S12_d009'])]"
        mc_s "[renpy.substitute(dialogues['E01S12_d010'])]"
        show ep01_game71 with hpunch
        mc_s "[renpy.substitute(dialogues['E01S12_d011'])]"
        mc_t "[renpy.substitute(dialogues['E01S12_d012'])]"
        $ ep01_mcquestion += 1
        jump ep01_thegame_q6

label ep01_mcpoint_3:
##MC WINS 3 POINTS (or less if failed)
    if ep01_anto_clothing == 0:
        jump ep01_mcpoint_1
    elif ep01_anto_clothing == 1:
        jump ep01_mcpoint_2
    else:
        show ep01_game70 with vpunch
        anto "[renpy.substitute(dialogues['E01S13_d001'])]"
        hide ep01_game64
        anto "[renpy.substitute(dialogues['E01S13_d002'])]"
        mc_t "[renpy.substitute(dialogues['E01S13_d003'])]"
        mc_s "[renpy.substitute(dialogues['E01S13_d004'])]"
        mc_s "[renpy.substitute(dialogues['E01S13_d005'])]"
        show ep01_game64 with hpunch
        anto "[renpy.substitute(dialogues['E01S13_d006'])]"
        $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=4, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
        show ep01_game72 with slowfade
        anto "[renpy.substitute(dialogues['E01S13_d007'])]"
        show ep01_game73 with flash
        mc_s "[renpy.substitute(dialogues['E01S13_d008'])]"
        show ep01_game74 with flash
        anto "[renpy.substitute(dialogues['E01S13_d009'])]"
        mc_s "[renpy.substitute(dialogues['E01S13_d010'])]"
        show ep01_game75 with flash
        anto "[renpy.substitute(dialogues['E01S13_d011'])]"
        anto "[renpy.substitute(dialogues['E01S13_d012'])]"
        show ep01_game76 with flash
        anto "[renpy.substitute(dialogues['E01S13_d013'])]"
        anto "[renpy.substitute(dialogues['E01S13_d014'])]"
        show ep01_game77 with flash
        mc_s "[renpy.substitute(dialogues['E01S13_d015'])]"
        anto "[renpy.substitute(dialogues['E01S13_d016'])]"
        show ep01_game78 with flash
        mc_s "[renpy.substitute(dialogues['E01S13_d017'])]"
        mc_s "[renpy.substitute(dialogues['E01S13_d018'])]"
        show ep01_game79 with flash
        anto "[renpy.substitute(dialogues['E01S13_d019'])]"
        mc_s "[renpy.substitute(dialogues['E01S13_d020'])]"
        $ ep01_anto_clothing += 1
        $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
        jump ep01_thegame_q6

label ep01_thegame_q6:
    scene eigengrau with slowfade
##3RD QUESTION BY ANTONELLA
    show ep01_game80 with dissolve
    anto "[renpy.substitute(dialogues['E01S14_d001'])]"
    anto "[renpy.substitute(dialogues['E01S14_d002'])]"
    anto "[renpy.substitute(dialogues['E01S14_d003'])]"
    anto "[renpy.substitute(dialogues['E01S14_d004'])]"
    hide ep01_game67
    if ep01_mc_clothing == 0:
        mc_t "[renpy.substitute(dialogues['E01S14_d005'])]"
        mc_t "[renpy.substitute(dialogues['E01S14_d006'])]"
    elif ep01_mc_clothing >= 1:
        mc_t "[renpy.substitute(dialogues['E01S14_d007'])]"
    $ show_walkthrough("ep01_game_menu6")
    $ ep01_q6 = random_menu(
        mc_t,  # The character who speaks before the menu. If none, use None.
        "Which one is it?",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "The Mahabharata", "ep01_q6_1"),
            (True, "The Epic of Gilgamesh", "ep01_q6_2"),
            (True, "Book of the Dead", "ep01_q6_3"),
        ]
    )

    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q6 == "ep01_q6_2":
        hide screen walkthrough_screen
        mc_s "[renpy.substitute(dialogues['E01S14_d008'])]"
        show ep01_game84
        anto "[renpy.substitute(dialogues['E01S14_d009'])]"
        mc_s "[renpy.substitute(dialogues['E01S14_d010'])]"
        anto "[renpy.substitute(dialogues['E01S14_d011'])]"
        jump ep01_endgame
    elif ep01_q6 in ["ep01_q6_1", "ep01_q6_3"]:
        hide screen walkthrough_screen
        if ep01_q6 == "ep01_q6_1":
            mc_s "[renpy.substitute(dialogues['E01S14_d012'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S14_d013'])]"
        show ep01_game67
        if ep01_q6 == "ep01_q6_1":
            anto "[renpy.substitute(dialogues['E01S14_d014'])]"
            mc_s "[renpy.substitute(dialogues['E01S14_d015'])]"
        else:
            anto "[renpy.substitute(dialogues['E01S14_d016'])]"
            mc_s "[renpy.substitute(dialogues['E01S14_d017'])]"
        $ ep01_mc_clothing += 1
        jump ep01_thegame_mc_nude

label ep01_endgame:
    scene eigengrau with dissolve
    if ep01_anto_clothing == 3 and ep01_mc_clothing == 0:
        $ ep01_bestprize = True
        jump ep01_endgame_w
    else:
        jump ep01_endgame_f

label ep01_endgame_w:
#THE GAME, BEST SCENARIO#THE GAME, BEST SCENARIO
    $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.5, fade_duration=5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    show ep01_game87 with hpunch
    anto "[renpy.substitute(dialogues['E01S17_d001'])]"
    anto "[renpy.substitute(dialogues['E01S17_d002'])]"
    anto "[renpy.substitute(dialogues['E01S17_d003'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d004'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d005'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d006'])]"
    show ep01_game88
    anto "[renpy.substitute(dialogues['E01S17_d007'])]"
    anto "[renpy.substitute(dialogues['E01S17_d008'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d009'])]"
    show ep01_game89
    mc_s "[renpy.substitute(dialogues['E01S17_d010'])]"
    anto "[renpy.substitute(dialogues['E01S17_d011'])]"
    anto "[renpy.substitute(dialogues['E01S17_d012'])]"
    anto "[renpy.substitute(dialogues['E01S17_d013'])]"
    show ep01_game92
    anto "[renpy.substitute(dialogues['E01S17_d014'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d016'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d017'])]"
    show ep01_game93
    anto "[renpy.substitute(dialogues['E01S17_d018'])]"
    anto "[renpy.substitute(dialogues['E01S17_d019'])]"
    anto "[renpy.substitute(dialogues['E01S17_d020'])]"
    show ep01_game94
    anto "[renpy.substitute(dialogues['E01S17_d021'])]"
    show ep01_game99
    mc_t "[renpy.substitute(dialogues['E01S17_d022'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d023'])]"
    show ep01_game100
    mc_t "[renpy.substitute(dialogues['E01S17_d024'])]"
    show ep01_game101 with slowfade
    anto "[renpy.substitute(dialogues['E01S17_d025'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d027'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d004'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d029'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d030'])]"
    show ep01_game103
    anto "[renpy.substitute(dialogues['E01S17_d031'])]"
    anto "[renpy.substitute(dialogues['E01S17_d032'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d033'])]"
    show ep01_game106
    mc_s "[renpy.substitute(dialogues['E01S17_d004'])]"
    anto "[renpy.substitute(dialogues['E01S17_d035'])]"
    anto "[renpy.substitute(dialogues['E01S17_d036'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d037'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d038'])]"
    show ep01_game110
    anto "[renpy.substitute(dialogues['E01S17_d039'])]"
    show ep01_game107
    anto "[renpy.substitute(dialogues['E01S17_d040'])]"
    show ep01_game111
    anto "[renpy.substitute(dialogues['E01S17_d041'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d012'])]"
    show ep01_game115 with slowfade
    anto "[renpy.substitute(dialogues['E01S17_d043'])]"
    anto "[renpy.substitute(dialogues['E01S17_d044'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d045'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d046'])]"
    anto "[renpy.substitute(dialogues['E01S17_d047'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d048'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d049'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d050'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d051'])]"
    show ep01_game116
    anto "[renpy.substitute(dialogues['E01S17_d052'])]"
    anto "[renpy.substitute(dialogues['E01S17_d053'])]"
    anto "[renpy.substitute(dialogues['E01S17_d054'])]"
    mc_t "[renpy.substitute(dialogues['E01S17_d055'])]"
    show ep01_game118
    anto "[renpy.substitute(dialogues['E01S17_d056'])]"
    show ep01_game119
    anto "[renpy.substitute(dialogues['E01S17_d057'])]"
    show ep01_game120
    mc_t "[renpy.substitute(dialogues['E01S17_d058'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
    show ep01_game121
    $ playAudio(sfx_keys, "sfx", 1, True, 0, 0)
    anto "[renpy.substitute(dialogues['E01S17_d059'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d053'])]"
    anto "[renpy.substitute(dialogues['E01S16_d054'])]"
    mc_s "[renpy.substitute(dialogues['E01S17_d012'])]"
    show ep01_game122
    anto "[renpy.substitute(dialogues['E01S17_d035'])]"
    anto "[renpy.substitute(dialogues['E01S17_d064'])]"
    anto "[renpy.substitute(dialogues['E01S17_d065'])]"
    show ep01_game123
    anto "[renpy.substitute(dialogues['E01S17_d066'])]"
    show ep01_game124
    anto "[renpy.substitute(dialogues['E01S17_d067'])]"
    show ep01_game125
    anto "[renpy.substitute(dialogues['E01S17_d068'])]"
    show ep01_game126
    anto "[renpy.substitute(dialogues['E01S17_d069'])]"
    anto "[renpy.substitute(dialogues['E01S17_d070'])]"
    show ep01_game127
    anto "[renpy.substitute(dialogues['E01S17_d071'])]"
    anto "[renpy.substitute(dialogues['E01S17_d072'])]"
    anto "[renpy.substitute(dialogues['E01S17_d073'])]"
    anto "[renpy.substitute(dialogues['E01S17_d074'])]"
    jump q3_date

label ep01_endgame_f:
#THE GAME, WORST SCENARIO FOR MC#THE GAME, WORST SCENARIO FOR MC
    show ep01_game94 with slowfade
    anto "[renpy.substitute(dialogues['E01S16_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d003'])]"
    show ep01_game107
    anto "[renpy.substitute(dialogues['E01S16_d004'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d002'])]"
    anto "[renpy.substitute(dialogues['E01S16_d006'])]"
    mc_t "[renpy.substitute(dialogues['E01S07_d014'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_game95 with fade
    mc_s "[renpy.substitute(dialogues['E01S16_d007'])]"
    if ep01_anto_clothing == 0:
        anto "[renpy.substitute(dialogues['E01S16_d008'])]"
        anto "[renpy.substitute(dialogues['E01S16_d009'])]"
    elif ep01_anto_clothing >=1:
        anto "[renpy.substitute(dialogues['E01S16_d010'])]"
    show ep01_game96
    anto "[renpy.substitute(dialogues['E01S16_d011'])]"
    anto "[renpy.substitute(dialogues['E01S16_d012'])]"
    mc_t "[renpy.substitute(dialogues['E01S16_d002'])]"
    show ep01_game97 with hpunch
    mc_s "[renpy.substitute(dialogues['E01S16_d014'])]"
    anto "[renpy.substitute(dialogues['E01S16_d015'])]"
    show ep01_game98
    anto "[renpy.substitute(dialogues['E01S16_d016'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d017'])]"
    anto "[renpy.substitute(dialogues['E01S16_d018'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d019'])]"
    show ep01_game102 with vpunch
    anto "[renpy.substitute(dialogues['E01S16_d020'])]"
    anto "[renpy.substitute(dialogues['E01S16_d021'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d002'])]"
    anto "[renpy.substitute(dialogues['E01S16_d023'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d024'])]"
    anto "[renpy.substitute(dialogues['E01S16_d025'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d026'])]"
    show ep01_game104 with slowfade
    anto "[renpy.substitute(dialogues['E01S16_d027'])]"
    show ep01_game105
    mc_t "[renpy.substitute(dialogues['E01S16_d028'])]"
    mc_t "[renpy.substitute(dialogues['E01S16_d029'])]"
    show ep01_game108
    anto "[renpy.substitute(dialogues['E01S16_d030'])]"
    anto "[renpy.substitute(dialogues['E01S16_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d032'])]"
    anto "[renpy.substitute(dialogues['E01S16_d033'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d034'])]"
    show ep01_game109 with vpunch
    anto "[renpy.substitute(dialogues['E01S16_d035'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d036'])]"
    mc_t "[renpy.substitute(dialogues['E01S16_d037'])]"
    show ep01_game112
    anto "[renpy.substitute(dialogues['E01S16_d038'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d033'])]"
    anto "[renpy.substitute(dialogues['E01S16_d040'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d033'])]"
    anto "[renpy.substitute(dialogues['E01S16_d042'])]"
    mc_t "[renpy.substitute(dialogues['E01S16_d043'])]"
    show ep01_game113 with hpunch
    anto "[renpy.substitute(dialogues['E01S16_d044'])]"
    mc_t "[renpy.substitute(dialogues['E01S16_d045'])]"
    show ep01_game114
    mc_s "[renpy.substitute(dialogues['E01S16_d046'])]"
    anto "[renpy.substitute(dialogues['E01S16_d047'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d033'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d049'])]"
    $ playAudio(sfx_keys, "sfx", 1, True, 0, 0)
    show ep01_game117 with hpunch
    anto "[renpy.substitute(dialogues['E01S16_d050'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d051'])]"
    anto "[renpy.substitute(dialogues['E01S16_d052'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d053'])]"
    anto "[renpy.substitute(dialogues['E01S16_d054'])]"
    jump q3_date

label q3_date:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (antonella, trust, -1)
# --
#THE DATE
    if rm.get("antonella", "trust") < 4:
        pass
    else:
        show ep01_game128 with vpunch
        anto "[renpy.substitute(dialogues['E01S07_d015'])]"
        mc_s "[renpy.substitute(dialogues['E01S18_d001'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    show ep01_game129 with slowfade
    mc_s "[renpy.substitute(dialogues['E01S18_d002'])]"
    anto "[renpy.substitute(dialogues['E01S18_d003'])]"
    show ep01_game130
    anto "[renpy.substitute(dialogues['E01S18_d004'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d005'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep01_postgame01 with slowfade
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(antonella_past_happy_theme, "music", 2, True, 8, 0)
    mc_y "[renpy.substitute(dialogues['E01S18_d006'])]"
    anto_y "[renpy.substitute(dialogues['E01S18_d007'])]"
    show ep01_postgame02
    anto "[renpy.substitute(dialogues['E01S18_d008'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d009'])]"
    anto "[renpy.substitute(dialogues['E01S18_d010'])]"
    show ep01_postgame03
    anto "[renpy.substitute(dialogues['E01S18_d011'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d012'])]"
    show ep01_postgame04 with hpunch
    mc_t "[renpy.substitute(dialogues['E01S18_d013'])]"
    show ep01_postgame06 with vpunch
    anto_y "[renpy.substitute(dialogues['E01S18_d014'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d015'])]"
    show ep01_postgame05
    anto "[renpy.substitute(dialogues['E01S18_d016'])]"
    anto "[renpy.substitute(dialogues['E01S18_d017'])]"
    anto "[renpy.substitute(dialogues['E01S18_d018'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=2.5)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4)
    $ playAudio(sfx_glitch, "sfx", 1, False, 2.5, 0)
    show ep01_postgame05 at animated_glitch
    mc_s "[renpy.substitute(dialogues['E01S18_d019'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d020'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d021'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d022'])]"
    if rm.get("antonella", "trust") < 4:
        pass
    else:
        $ setChannelVolume(channel="sfx", subchannel=1, volume=0, fade_duration=2.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=2.5)
        show ep01_postgame07 with vpunch
        anto "[renpy.substitute(dialogues['E01S18_d023'])]"
        anto "[renpy.substitute(dialogues['E01S18_d024'])]"
        show ep01_postgame08
        mc_t "[renpy.substitute(dialogues['E01S18_d025'])]"
        mc_t "[renpy.substitute(dialogues['E01S18_d026'])]"
        show ep01_postgame09
        anto "[renpy.substitute(dialogues['E01S18_d027'])]"
        $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4, fade_duration=2.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=2.5)
    scene eigengrau with slowfade
    show ep01_postgame10 at animated_glitch
    mc_t "[renpy.substitute(dialogues['E01S18_d028'])]"
    anto "[renpy.substitute(dialogues['E01S18_d029'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d030'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d031'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d032'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=2.5)
    show ep01_postgame11
    anto "[renpy.substitute(dialogues['E01S18_d033'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d034'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d035'])]"
    show ep01_postgame12
    anto "[renpy.substitute(dialogues['E01S18_d036'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d037'])]"
    anto "[renpy.substitute(dialogues['E01S18_d038'])]"
    show ep01_postgame13 with slowfade
    anto "[renpy.substitute(dialogues['E01S18_d039'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d040'])]"
    anto "[renpy.substitute(dialogues['E01S18_d041'])]"
    show ep01_postgame14
    mc_s "[renpy.substitute(dialogues['E01S18_d042'])]"
    anto "[renpy.substitute(dialogues['E01S18_d043'])]"
    mc_s "[renpy.substitute(dialogues['E01S18_d044'])]"
    anto "[renpy.substitute(dialogues['E01S18_d045'])]"
    anto "[renpy.substitute(dialogues['E01S18_d046'])]"
    $ show_walkthrough("ep01_postgame_menu")
    menu:
        "Yes":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S18_d047'])]"
            anto "[renpy.substitute(dialogues['E01S18_d048'])]"
            $ ep01_clothstore = True
            $ stopAllSubchannels(channel="music", fadeout=1.5)
        "No":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S18_d049'])]"
            anto "[renpy.substitute(dialogues['E01S18_d050'])]"
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            jump ep01_park_situation
    scene eigengrau with dissolve
    $ playAudio(sfx_mall, "amb", 1, True, 1.5, 0)
    show ep01_clothing01 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S18_d051'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d052'])]"
    show ep01_clothing02
    mc_t "[renpy.substitute(dialogues['E01S18_d053'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d054'])]"
    mc_t "[renpy.substitute(dialogues['E01S18_d055'])]"
    $ show_walkthrough("ep01_clothing_menu")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S18_d056'])]"
        "Chat with goth girl":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S18_d057'])]"
            $ rm.update("antonella", "trust", -1)
            $ check_levels("antonella", "trust", -1)
            jump ep01_proleather
        "Find perfect gift":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S18_d058'])]"
            jump ep01_proseller

label ep01_proleather:
#THE CLOTHING_1
    show ep01_clothing03 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S19_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01S19_d002'])]"
    mc_t "[renpy.substitute(dialogues['E01S19_d003'])]"
    show ep01_clothing04
    mc_t "[renpy.substitute(dialogues['E01S19_d004'])]"
    mc_t "[renpy.substitute(dialogues['E01S19_d005'])]"
    show ep01_clothing05
    mc_t "[renpy.substitute(dialogues['E01S19_d006'])]"
    show ep01_clothing06
    mc_t "[renpy.substitute(dialogues['E01S19_d007'])]"
    mc_t "[renpy.substitute(dialogues['E01S19_d008'])]"
    show ep01_clothing07
    mc_t "[renpy.substitute(dialogues['E01S19_d009'])]"
    mc_t "[renpy.substitute(dialogues['E01S19_d010'])]"
    mc_s "[renpy.substitute(dialogues['E01S19_d011'])]"
    "Goth girl" "[renpy.substitute(dialogues['E01S19_d016'])]"
    show ep01_clothing08 with vpunch
    "Goth girl" "[renpy.substitute(dialogues['E01S19_d017'])]"
    show ep01_clothing09 with hpunch
    "Goth girl" "[renpy.substitute(dialogues['E01S19_d018'])]"
    "Goth girl" "[renpy.substitute(dialogues['E01S19_d019'])]"
    mc_s "[renpy.substitute(dialogues['E01S19_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S19_d013'])]"
    "Goth Girl" "[renpy.substitute(dialogues['E01S19_d020'])]"
    $ unlock_memory("m_ep01_clothes")
    show ep01_clothing10
    mc_t "[renpy.substitute(dialogues['E01S19_d014'])]"
    mc_t "[renpy.substitute(dialogues['E01S19_d015'])]"
    $ ep01_gothgirl = True
    jump ep01_proseller

label ep01_proseller:
#THE CLOTHING_2
    show ep01_clothing11 with slowfade
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d075'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d001'])]"
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d076'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d002'])]"
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d077'])]"
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d078'])]"
    show ep01_clothing12
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d079'])]"
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d080'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d003'])]"
    show ep01_clothing13
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d081'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d004'])]"
    "Salesgirl" "[renpy.substitute(dialogues['E01S20_d082'])]"
    show ep01_clothing14 with hpunch
    anto "[renpy.substitute(dialogues['E01S20_d005'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d006'])]"
    anto "[renpy.substitute(dialogues['E01S20_d007'])]"
    anto "[renpy.substitute(dialogues['E01S20_d008'])]"
    show ep01_clothing15 at concentrate with dissolve
    anto "[renpy.substitute(dialogues['E01S20_d009'])]"
    mc_t "[renpy.substitute(dialogues['E01S20_d010'])]"
    show ep01_clothing16 with vpunch
    if ep01_gothgirl:
        anto "[renpy.substitute(dialogues['E01S20_d011'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d012'])]"
        anto "[renpy.substitute(dialogues['E01S20_d013'])]"
    else:
        anto "[renpy.substitute(dialogues['E01S20_d014'])]"
        anto "[renpy.substitute(dialogues['E01S20_d015'])]"
        anto "[renpy.substitute(dialogues['E01S20_d016'])]"
    show ep01_clothing17
    anto "[renpy.substitute(dialogues['E01S20_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d018'])]"
    anto "[renpy.substitute(dialogues['E01S20_d019'])]"
    show ep01_clothing18 with vpunch
    "Saleswoman" "[renpy.substitute(dialogues['E01S20_d083'])]"
    anto "[renpy.substitute(dialogues['E01S20_d020'])]"
    show ep01_clothing19
    anto "[renpy.substitute(dialogues['E01S20_d021'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d022'])]"
    show ep01_clothing20 with slowfade
    $ playAudio(antonella_game_theme, "music", 2, True, 2.5, 0)
    mc_t "[renpy.substitute(dialogues['E01S20_d023'])]"
    show ep01_clothing21 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S20_d024'])]"
    show ep01_clothing22 at concentrate
    anto "[renpy.substitute(dialogues['E01S20_d025'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d026'])]"
    if ep01_anto_clothing >=1:
        show ep01_clothing24
        anto "[renpy.substitute(dialogues['E01S20_d027'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d028'])]"
        anto "[renpy.substitute(dialogues['E01S20_d029'])]"
    else:
        anto "[renpy.substitute(dialogues['E01S20_d030'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d031'])]"
        anto "[renpy.substitute(dialogues['E01S20_d032'])]"
    show ep01_clothing23 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S20_d033'])]"
    if ep01_anto_clothing >=2:
        anto "[renpy.substitute(dialogues['E01S20_d034'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d035'])]"
        anto "[renpy.substitute(dialogues['E01S20_d036'])]"
    else:
        pass
    if ep01_anto_clothing >= 2:
        show ep01_clothing25 at concentrate with hpunch
        anto "[renpy.substitute(dialogues['E01S20_d037'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d038'])]"
        anto "[renpy.substitute(dialogues['E01S20_d039'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d040'])]"
        anto "[renpy.substitute(dialogues['E01S20_d041'])]"
        mc_t "[renpy.substitute(dialogues['E01S20_d042'])]"
        show ep01_clothing26
        anto "[renpy.substitute(dialogues['E01S20_d043'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d044'])]"
        anto "[renpy.substitute(dialogues['E01S20_d045'])]"
        if ep01_anto_clothing == 3 and ep01_mc_clothing == 0:
            anto "[renpy.substitute(dialogues['E01S20_d046'])]"
        else:
            anto "[renpy.substitute(dialogues['E01S20_d047'])]"
    else:
        pass
    if ep01_anto_clothing == 3 and ep01_mc_clothing == 0:
        show ep01_clothing27 with slowfade
        anto "[renpy.substitute(dialogues['E01S20_d048'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d049'])]"
        anto "[renpy.substitute(dialogues['E01S20_d050'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d051'])]"
        anto "[renpy.substitute(dialogues['E01S20_d052'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d053'])]"
        show ep01_clothing28 with vpunch
        anto "[renpy.substitute(dialogues['E01S20_d054'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d055'])]"
        anto "[renpy.substitute(dialogues['E01S20_d056'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d057'])]"
        show ep01_clothing29
        anto "[renpy.substitute(dialogues['E01S20_d058'])]"
        mc_s "[renpy.substitute(dialogues['E01S20_d059'])]"
        show ep01_clothing30
        anto "[renpy.substitute(dialogues['E01S20_d060'])]" 
        anto "[renpy.substitute(dialogues['E01S20_d061'])]"
        $ show_walkthrough("ep01_antochangeclothes_menu")
        menu:
            mc_t "[renpy.substitute(dialogues['E01S20_d062'])]"
            "Ask for a booty shot":
                hide screen walkthrough_screen
                mc_s "[renpy.substitute(dialogues['E01S20_d063'])]"
                anto "[renpy.substitute(dialogues['E01S20_d064'])]"
                mc_s "[renpy.substitute(dialogues['E01S20_d065'])]"
                anto "[renpy.substitute(dialogues['E01S20_d066'])]"
                mc_s "[renpy.substitute(dialogues['E01S20_d067'])]"
                anto "[renpy.substitute(dialogues['E01S20_d068'])]"
                show ep01_clothing31 with hpunch
                anto "[renpy.substitute(dialogues['E01S20_d069'])]"
                mc_s "[renpy.substitute(dialogues['E01S20_d070'])]"
                anto "[renpy.substitute(dialogues['E01S20_d071'])]"
            "Don't risk it":
                hide screen walkthrough_screen
                pass
        mc_s "[renpy.substitute(dialogues['E01S20_d072'])]"
    else:
        pass
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_clothing32
    anto "[renpy.substitute(dialogues['E01S20_d073'])]"
    mc_s "[renpy.substitute(dialogues['E01S20_d074'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_park_situation

label ep01_park_situation:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (amber, trust, +1)
# --
#THE PARK SITUATION
    $ playAudio(sfx_evenpark, "amb", 2, True, 2.5, 0)
    show ep01_thepark01 with slowfade
    anto "[renpy.substitute(dialogues['E01S21_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d002'])]"
    anto "[renpy.substitute(dialogues['E01S21_d003'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(antonella_love, "music", 2, True, 2.5, 0)
    show ep01_thepark03 with slowfade
    anto "[renpy.substitute(dialogues['E01S21_d004'])]"
    anto "[renpy.substitute(dialogues['E01S21_d005'])]"
    anto "[renpy.substitute(dialogues['E01S21_d006'])]"
    anto "[renpy.substitute(dialogues['E01S21_d007'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d008'])]"
    anto "[renpy.substitute(dialogues['E01S21_d009'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d010'])]"
    show ep01_thepark02
    anto "[renpy.substitute(dialogues['E01S21_d011'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d012'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d013'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d014'])]"
    show ep01_thepark04 with hpunch
    mc_t "[renpy.substitute(dialogues['E01S21_d015'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d016'])]"
    if ep01_hug:
        anto "[renpy.substitute(dialogues['E01S21_d017'])]"
        anto "[renpy.substitute(dialogues['E01S21_d018'])]"
    else:
        anto "[renpy.substitute(dialogues['E01S21_d019'])]"
        anto "[renpy.substitute(dialogues['E01S21_d020'])]"
    anto "[renpy.substitute(dialogues['E01S21_d021'])]"
    anto "[renpy.substitute(dialogues['E01S21_d022'])]"
    mc_s "[renpy.substitute(dialogues['E01S16_d049'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_thepark05 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S21_d023'])]"
    $ setChannelVolume(channel="music", subchannel=4, volume=0.5)
    $ playAudio(amber_theme, "music", 4, True, 3, 0)
    mc_t "[renpy.substitute(dialogues['E01S21_d024'])]"
    show ep01_thepark06 with vpunch
    amb "[renpy.substitute(dialogues['E01S21_d025'])]"
    amb "[renpy.substitute(dialogues['E01S21_d026'])]"
    show ep01_thepark07
    mc_s "[renpy.substitute(dialogues['E01S21_d027'])]"
    amb "[renpy.substitute(dialogues['E01S21_d028'])]"
    show ep01_thepark08
    anto "[renpy.substitute(dialogues['E01S21_d029'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d030'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d032'])]"
    amb "[renpy.substitute(dialogues['E01S21_d033'])]"
    show ep01_thepark09
    anto "[renpy.substitute(dialogues['E01S21_d034'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d035'])]"
    anto "[renpy.substitute(dialogues['E01S21_d036'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d037'])]"
    anto "[renpy.substitute(dialogues['E01S21_d038'])]"
    anto "[renpy.substitute(dialogues['E01S21_d039'])]"
    anto "[renpy.substitute(dialogues['E01S21_d040'])]"
    show ep01_thepark10
    amb_y "[renpy.substitute(dialogues['E01S21_d041'])]"
    anto "[renpy.substitute(dialogues['E01S21_d042'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d043'])]"
    mc_y "[renpy.substitute(dialogues['E01S21_d044'])]"
    show ep01_thepark11
    mc_s "[renpy.substitute(dialogues['E01S21_d045'])]"
    amb "[renpy.substitute(dialogues['E01S21_d046'])]"
    show ep01_thepark12
    anto "[renpy.substitute(dialogues['E01S21_d047'])]"
    amb "[renpy.substitute(dialogues['E01S21_d048'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d049'])]"
    show ep01_thepark13
    amb "[renpy.substitute(dialogues['E01S21_d050'])]"
    amb "[renpy.substitute(dialogues['E01S21_d051'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d052'])]"
    show ep01_thepark14
    mc_s "[renpy.substitute(dialogues['E01S21_d053'])]"
    anto "[renpy.substitute(dialogues['E01S21_d054'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d055'])]"
    anto "[renpy.substitute(dialogues['E01S21_d056'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d057'])]"
    amb "[renpy.substitute(dialogues['E01S21_d058'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d059'])]"
    show ep01_thepark15
    amb_y "[renpy.substitute(dialogues['E01S21_d060'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d061'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d062'])]"
    show ep01_thepark16
    $ stopAllSubchannels(channel="music", fadeout=5)
    amb_y "[renpy.substitute(dialogues['E01S21_d063'])]"
    amb_y "[renpy.substitute(dialogues['E01S21_d064'])]"
    show ep01_thepark17
    anto "[renpy.substitute(dialogues['E01S21_d065'])]"
    mc_s "[renpy.substitute(dialogues['E01S21_d066'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d067'])]"
    mc_t "[renpy.substitute(dialogues['E01S21_d068'])]"
    $ show_walkthrough("ep01_thepark_menu1")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S21_d069'])]"
        "Go after Amber":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S21_d070'])]"
            mc_t "[renpy.substitute(dialogues['E01S21_d071'])]"
            mc_s "[renpy.substitute(dialogues['E01S21_d075'])]"
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            $ ep01_park += 2
            jump ep01_chaseamb
        "Comfort Antonella":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S21_d072'])]"
            mc_t "[renpy.substitute(dialogues['E01S21_d073'])]"
            mc_s "[renpy.substitute(dialogues['E01S21_d074'])]"
            $ ep01_park += 1
            jump ep01_stayanto

label ep01_chaseamb:
##RM.POINTS.TRACK (amber, trust, +1, -1)
##RM.POINTS.TRACK (antonella, trust, -5)
# --
#PICKING AMBER
    show ep01_thepark18 with hpunch
    mc_y "[renpy.substitute(dialogues['E01S23_d001'])]"
    show ep01_thepark19 with slowfade
    $ playAudio(amber_sad_theme, "music", 2, True, 2.5, 0)
    amb "[renpy.substitute(dialogues['E01S23_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S23_d003'])]"
    amb "[renpy.substitute(dialogues['E01S23_d004'])]"
    mc_s "[renpy.substitute(dialogues['E01S23_d005'])]"
    show ep01_thepark20 with vpunch
    amb "[renpy.substitute(dialogues['E01S23_d006'])]"
    mc_s "[renpy.substitute(dialogues['E01S23_d007'])]"
    amb "[renpy.substitute(dialogues['E01S23_d008'])]"
    amb "[renpy.substitute(dialogues['E01S23_d009'])]"
    amb "[renpy.substitute(dialogues['E01S23_d010'])]"
    mc_s "[renpy.substitute(dialogues['E01S23_d011'])]"
    show ep01_thepark21
    amb "[renpy.substitute(dialogues['E01S23_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S23_d013'])]"
    amb "[renpy.substitute(dialogues['E01S23_d014'])]"
    mc_t "[renpy.substitute(dialogues['E01S23_d015'])]"
    mc_t "[renpy.substitute(dialogues['E01S23_d016'])]"
    $ show_walkthrough("ep01_thepark_menu2")
    menu:
        "Lie to Amber":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            $ ep01_lieamber = True
            $ stopAllSubchannels(channel="music", fadeout=2.5)
            mc_t "[renpy.substitute(dialogues['E01S23_d017'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d018'])]"
            amb "[renpy.substitute(dialogues['E01S23_d019'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d020'])]"
            show ep01_thepark22
            amb "[renpy.substitute(dialogues['E01S23_d021'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d022'])]"
            show ep01_thepark24 with vpunch
            amb "[renpy.substitute(dialogues['E01S23_d023'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d024'])]"
            show ep01_thepark25
            amb "[renpy.substitute(dialogues['E01S23_d025'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d026'])]"
            amb "[renpy.substitute(dialogues['E01S23_d027'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d028'])]"
            amb "[renpy.substitute(dialogues['E01S23_d029'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d030'])]"
            show ep01_thepark26
            amb "[renpy.substitute(dialogues['E01S23_d031'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d032'])]"
            amb "[renpy.substitute(dialogues['E01S23_d033'])]"
            show ep01_thepark27 with slowfade
            amb "[renpy.substitute(dialogues['E01S23_d034'])]"
            mc_t "[renpy.substitute(dialogues['E01S23_d035'])]"
            anto "[renpy.substitute(dialogues['E01S23_d036'])]"
            amb "[renpy.substitute(dialogues['E01S23_d037'])]"
            anto "[renpy.substitute(dialogues['E01S23_d038'])]"
            amb "[renpy.substitute(dialogues['E01S23_d039'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d040'])]"
            amb "[renpy.substitute(dialogues['E01S23_d041'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d042'])]"
            show ep01_thepark28 with slowfade
            anto "[renpy.substitute(dialogues['E01S23_d043'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d044'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d045'])]"
            show ep01_thepark30
            anto "[renpy.substitute(dialogues['E01S23_d046'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d047'])]"
            anto "[renpy.substitute(dialogues['E01S23_d048'])]"
            $ show_walkthrough("ep01_thepark_menu3")
            menu:
                mc_t "[renpy.substitute(dialogues['E01S23_d049'])]"
                "Make excuses":
                    hide screen walkthrough_screen
                    $ ep01_losttrust = True
                    mc_s "[renpy.substitute(dialogues['E01S23_d050'])]"
                "Be honest and apologize":
                    hide screen walkthrough_screen
                    mc_s "[renpy.substitute(dialogues['E01S23_d051'])]"
            show ep01_thepark29
            if ep01_losttrust:
                $ rm.update("antonella", "trust", -5)
                $ check_levels("antonella", "trust", -5)
                anto "[renpy.substitute(dialogues['E01S23_d052'])]"
                mc_s "[renpy.substitute(dialogues['E01S23_d053'])]"
                anto "[renpy.substitute(dialogues['E01S23_d054'])]"
                mc_s "[renpy.substitute(dialogues['E01S23_d055'])]"
                mc_s "[renpy.substitute(dialogues['E01S23_d056'])]"
            else:
                anto "[renpy.substitute(dialogues['E01S23_d057'])]"
                anto "[renpy.substitute(dialogues['E01S23_d058'])]"
                mc_s "[renpy.substitute(dialogues['E01S23_d055'])]"
                anto "[renpy.substitute(dialogues['E01S23_d060'])]"
                mc_s "[renpy.substitute(dialogues['E01S23_d061'])]"
            jump ep01_postpark
        "Tell Amber the truth":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -1)
            $ check_levels("amber", "trust", -1)
            $ stopAudio(channel="music", subchannel=2, fadeout=2.5)
            mc_t "[renpy.substitute(dialogues['E01S23_d062'])]"
            $ playAudio(amber_anger_theme, "music", 4, True, 2.5, 0)
            mc_s "[renpy.substitute(dialogues['E01S23_d063'])]"
            show ep01_thepark23 with vpunch
            amb_y "[renpy.substitute(dialogues['E01S23_d064'])]"
            amb "[renpy.substitute(dialogues['E01S23_d065'])]"
            mc_t "[renpy.substitute(dialogues['E01S23_d066'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d067'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d068'])]"
            show ep01_thepark32 with hpunch
            amb_y "[renpy.substitute(dialogues['E01S23_d069'])]"
            amb "[renpy.substitute(dialogues['E01S23_d070'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d071'])]"
            show ep01_thepark33 with hpunch
            amb "[renpy.substitute(dialogues['E01S23_d072'])]"
            amb "[renpy.substitute(dialogues['E01S23_d073'])]"
            amb "[renpy.substitute(dialogues['E01S23_d074'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d075'])]"
            show ep01_thepark34
            amb "[renpy.substitute(dialogues['E01S23_d076'])]"
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            show ep01_thepark28 with slowfade
            anto "[renpy.substitute(dialogues['E01S23_d077'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d078'])]"
            anto "[renpy.substitute(dialogues['E01S23_d079'])]"
            show ep01_thepark36
            anto "[renpy.substitute(dialogues['E01S23_d080'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d081'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d082'])]"
            show ep01_thepark38
            anto "[renpy.substitute(dialogues['E01S23_d083'])]"
            anto "[renpy.substitute(dialogues['E01S23_d084'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d085'])]"
            show ep01_thepark31
            anto "[renpy.substitute(dialogues['E01S23_d086'])]"
            mc_s "[renpy.substitute(dialogues['E01S23_d041'])]"
            anto "[renpy.substitute(dialogues['E01S03_d010'])]"
            jump ep01_postpark

label ep01_stayanto:
#PICKING ANTO
    $ playAudio(antonella_past_theme, "music", 2, True, 2.5, 0)
    show ep01_thepark35 with slowfade
    anto "[renpy.substitute(dialogues['E01S22_d001'])]"
    anto "[renpy.substitute(dialogues['E01S22_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d003'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d004'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d005'])]"
    show ep01_thepark36
    anto "[renpy.substitute(dialogues['E01S22_d006'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d007'])]"
    show ep01_thepark37
    anto "[renpy.substitute(dialogues['E01S22_d008'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d009'])]"
    anto "[renpy.substitute(dialogues['E01S22_d010'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d011'])]"
    show ep01_thepark38
    anto "[renpy.substitute(dialogues['E01S22_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d013'])]"
    anto "[renpy.substitute(dialogues['E01S22_d014'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d015'])]"
    anto "[renpy.substitute(dialogues['E01S22_d016'])]"
    show ep01_thepark31
    mc_s "[renpy.substitute(dialogues['E01S22_d017'])]"
    anto "[renpy.substitute(dialogues['E01S22_d018'])]"
    mc_s "[renpy.substitute(dialogues['E01S22_d019'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep01_postpark

label ep01_postpark:
#THE TAXI INCIDENT
    scene eigengrau with dissolve
    show ep01_thepark39 with slowfade
    $ playAudio(sfx_footsteps_male_semirun, "sfx", 1, True, 1, 0)
    if ep01_park == 1: #MC picked Antonella
        mc_t "[renpy.substitute(dialogues['E01S24x_d001'])]"
        mc_t "[renpy.substitute(dialogues['E01S24x_d002'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            if ep01_losttrust: #MC made excuses to Antonella
                mc_t "[renpy.substitute(dialogues['E01S24x_d003'])]"
                mc_t "[renpy.substitute(dialogues['E01S24x_d004'])]"
            else: #MC was honest to Antonella
                mc_t "[renpy.substitute(dialogues['E01S24x_d005'])]"
                mc_t "[renpy.substitute(dialogues['E01S24x_d006'])]"
        else: #MC told the truth to Amber
            mc_t "[renpy.substitute(dialogues['E01S24x_d007'])]"
            mc_t "[renpy.substitute(dialogues['E01S24x_d008'])]"
    show ep01_thepark40
    mc_s "[renpy.substitute(dialogues['E01S24x_d009'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=0)
    $ playAudio(sfx_taxihorn, "sfx", 2, False, 0, 0)
    show ep01_thepark41 with vpunch
    mc_t "[renpy.substitute(dialogues['E01S24x_d010'])]"
    show ep01_thepark42 with hpunch
    amb "[renpy.substitute(dialogues['E01S24x_d011'])]"
    $ playAudio(sfx_carhit, "sfx", 3, False, 0, 0)
    show ep01_thepark43 with vpunch
    mc_s "[renpy.substitute(dialogues['E01S24x_d012'])]"
    show ep01_thepark44
    mc_s "[renpy.substitute(dialogues['E01S24x_d013'])]"
    amb_y "[renpy.substitute(dialogues['E01S24x_d014'])]"
    show ep01_thepark45 with slowfade
    mc_s "[renpy.substitute(dialogues['E01S24x_d015'])]"
    amb "[renpy.substitute(dialogues['E01S24x_d016'])]"
    mc_s "[renpy.substitute(dialogues['E01S24x_d017'])]"
    $ playAudio(sfx_punch, "sfx", 4, False, 0, 0)
    show ep01_thepark46 with vpunch
    amb_y "[renpy.substitute(dialogues['E01S24x_d018'])]"
    mc_s "[renpy.substitute(dialogues['E01S24x_d019'])]"
    show ep01_thepark47
    amb "[renpy.substitute(dialogues['E01S24x_d020'])]"
    mc_s "[renpy.substitute(dialogues['E01S24x_d021'])]"
    amb "[renpy.substitute(dialogues['E01S24x_d022'])]"
    mc_s "[renpy.substitute(dialogues['E01S24x_d023'])]"
    amb "[renpy.substitute(dialogues['E01S24x_d024'])]"
    show ep01_thepark48
    mc_s "[renpy.substitute(dialogues['E01S24x_d025'])]"
    amb "[renpy.substitute(dialogues['E01S24x_d026'])]"
    mc_s "[renpy.substitute(dialogues['E01S24x_d027'])]"
    amb "[renpy.substitute(dialogues['E01S24x_d028'])]"
    mc_s "[renpy.substitute(dialogues['E01S24x_d029'])]"
#HOME SWEET HOME
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep01_home01 with slowfade
    $ playAudio(sfx_midnightpast, "amb", 1, True, 2.5, 0)
    mc_s "[renpy.substitute(dialogues['E01S24_d001'])]"
    amb "[renpy.substitute(dialogues['E01S24_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S24_d003'])]"
    amb "[renpy.substitute(dialogues['E01S24_d004'])]"
    $ playAudio(amber_theme, "music", 2, True, 2.5, 0)
    show ep01_home02 with slowfade
    amb "[renpy.substitute(dialogues['E01S24_d005'])]"
    amb "[renpy.substitute(dialogues['E01S24_d006'])]"
    mc_s "[renpy.substitute(dialogues['E01S24_d007'])]"
    amb "[renpy.substitute(dialogues['E01S24_d008'])]"
    mc_s "[renpy.substitute(dialogues['E01S24_d009'])]"
    show ep01_home03
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d010'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d011'])]"
        amb "[renpy.substitute(dialogues['E01S24_d012'])]"
        $ show_walkthrough("ep01_home_menu")
        menu:
            "Reassure Amber":
                hide screen walkthrough_screen
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                mc_s "[renpy.substitute(dialogues['E01S24_d013'])]"
                amb "[renpy.substitute(dialogues['E01S24_d014'])]"
                mc_s "[renpy.substitute(dialogues['E01S24_d015'])]"
            "Stand your ground":
                hide screen walkthrough_screen
                $ rm.update("amber", "trust", -1)
                $check_levels("amber", "trust", -1)
                mc_s "[renpy.substitute(dialogues['E01S24_d016'])]"
                amb "[renpy.substitute(dialogues['E01S24_d017'])]"
                mc_s "[renpy.substitute(dialogues['E01S24_d018'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d019'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d020'])]"
            amb "[renpy.substitute(dialogues['E01S24_d021'])]"
            $ show_walkthrough("ep01_home_menu")
            menu:
                "Reassure Amber":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", 1)
                    $ check_levels("amber", "trust", 1)
                    mc_s "[renpy.substitute(dialogues['E01S24_d022'])]"
                    amb "[renpy.substitute(dialogues['E01S24_d023'])]"
                    mc_s "[renpy.substitute(dialogues['E01S24_d024'])]"
                "Be evasive":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", -1)
                    $ check_levels("amber", "trust", -1)
                    mc_s "[renpy.substitute(dialogues['E01S24_d025'])]"
                    amb "[renpy.substitute(dialogues['E01S24_d026'])]"
                    mc_s "[renpy.substitute(dialogues['E01S24_d027'])]"
        else: #MC told the truth to Amber
            amb "[renpy.substitute(dialogues['E01S24_d028'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d029'])]"
            amb "[renpy.substitute(dialogues['E01S24_d030'])]"
            $ show_walkthrough("ep01_home_menu")
            menu:
                "Explain calmly":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", 1)
                    $ check_levels("amber", "trust", 1)
                    mc_s "[renpy.substitute(dialogues['E01S24_d031'])]"
                    amb "[renpy.substitute(dialogues['E01S24_d032'])]"
                    mc_s "[renpy.substitute(dialogues['E01S24_d033'])]"
                "Be defensive":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", -1)
                    $ check_levels("amber", "trust", -1)
                    mc_s "[renpy.substitute(dialogues['E01S24_d034'])]"
                    amb "[renpy.substitute(dialogues['E01S24_d035'])]"
                    mc_s "[renpy.substitute(dialogues['E01S24_d036'])]"
    show ep01_home04 with vpunch
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d037'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d038'])]"
        amb "[renpy.substitute(dialogues['E01S24_d039'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d040'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d041'])]"
            amb "[renpy.substitute(dialogues['E01S24_d042'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d043'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d044'])]"
            amb "[renpy.substitute(dialogues['E01S24_d045'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d046'])]"
    show ep01_home05 with hpunch
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d047'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d048'])]"
        amb "[renpy.substitute(dialogues['E01S24_d049'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            mc_s "[renpy.substitute(dialogues['E01S24_d050'])]"
            amb "[renpy.substitute(dialogues['E01S24_d051'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d052'])]"
            amb "[renpy.substitute(dialogues['E01S24_d053'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d054'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d055'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d056'])]"
            amb "[renpy.substitute(dialogues['E01S24_d057'])]"
            amb "[renpy.substitute(dialogues['E01S24_d058'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d059'])]"
    show ep01_home06
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d060'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d061'])]"
        amb "[renpy.substitute(dialogues['E01S24_d062'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d063'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d064'])]"
            amb "[renpy.substitute(dialogues['E01S24_d065'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d066'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d067'])]"
            amb "[renpy.substitute(dialogues['E01S24_d068'])]"
    show ep01_home07
    if ep01_park == 1: #MC picked Antonella
        mc_s "[renpy.substitute(dialogues['E01S24_d069'])]"
        amb "[renpy.substitute(dialogues['E01S24_d070'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d071'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            mc_s "[renpy.substitute(dialogues['E01S24_d069'])]"
            amb "[renpy.substitute(dialogues['E01S24_d073'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d074'])]"
        else:
            mc_s "[renpy.substitute(dialogues['E01S24_d069'])]"   
            amb "[renpy.substitute(dialogues['E01S24_d076'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d077'])]"
    show ep01_home08
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d078'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d079'])]"
        amb "[renpy.substitute(dialogues['E01S24_d080'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d081'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d082'])]"
            amb "[renpy.substitute(dialogues['E01S24_d083'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d084'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d085'])]"
            amb "[renpy.substitute(dialogues['E01S24_d086'])]"
    show ep01_home09
    if ep01_park == 1: #MC picked Antonella
        mc_s "[renpy.substitute(dialogues['E01S24_d087'])]"
        amb "[renpy.substitute(dialogues['E01S24_d088'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d089'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            mc_s "[renpy.substitute(dialogues['E01S24_d090'])]"
            amb "[renpy.substitute(dialogues['E01S24_d091'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d092'])]"
            amb "[renpy.substitute(dialogues['E01S24_d093'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d094'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d095'])]"   
            mc_s "[renpy.substitute(dialogues['E01S24_d096'])]"
            amb "[renpy.substitute(dialogues['E01S24_d097'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d098'])]"
    show ep01_home10 with slowfade
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d099'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d100'])]"
        amb "[renpy.substitute(dialogues['E01S24_d101'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d102'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d103'])]"
            amb "[renpy.substitute(dialogues['E01S24_d104'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d105'])]"
            amb "[renpy.substitute(dialogues['E01S24_d106'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d107'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d108'])]"   
            mc_s "[renpy.substitute(dialogues['E01S24_d109'])]"
            amb "[renpy.substitute(dialogues['E01S24_d110'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d111'])]"
            amb "[renpy.substitute(dialogues['E01S24_d112'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d113'])]"
    show ep01_home11
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d114'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d115'])]"
        amb "[renpy.substitute(dialogues['E01S24_d116'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d117'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d118'])]"
            amb "[renpy.substitute(dialogues['E01S24_d119'])]"
            amb "[renpy.substitute(dialogues['E01S24_d120'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d115'])]"
            amb "[renpy.substitute(dialogues['E01S24_d116'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d123'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d124'])]"
            amb "[renpy.substitute(dialogues['E01S24_d125'])]"
            amb "[renpy.substitute(dialogues['E01S24_d126'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d127'])]"
            amb "[renpy.substitute(dialogues['E01S24_d128'])]"
    show ep01_home12
    $ stopAllSubchannels(channel="music", fadeout=4)
    if ep01_park == 1: #MC picked Antonella
        amb "[renpy.substitute(dialogues['E01S24_d129'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d130'])]"
        mc_s "[renpy.substitute(dialogues['E01S24_d069'])]"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "[renpy.substitute(dialogues['E01S24_d129'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d133'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d069'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S24_d129'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d136'])]"
            mc_s "[renpy.substitute(dialogues['E01S24_d069'])]"
    $ unlock_memory("m_ep01_home")

#ALONE AT LIVINGROOM
    scene eigengrau with dissolve
    show ep01_home13 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S25_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01S25_d002'])]"
    show ep01_home14
    mc_t "[renpy.substitute(dialogues['E01S25_d003'])]"
    mc_t "[renpy.substitute(dialogues['E01S25_d004'])]"
    amb_y "[renpy.substitute(dialogues['E01S25_d005'])]"
    eli_y "[renpy.substitute(dialogues['E01S25_d006'])]"
    mc_t "[renpy.substitute(dialogues['E01S25_d007'])]"
    mc_y "[renpy.substitute(dialogues['E01S25_d008'])]"
    $ show_walkthrough("ep01_home_menu2")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S25_d009'])]"
        "Answer Mom's call":
            hide screen walkthrough_screen
            $ ep01_elicall = True
            jump ep01_bath
        "Answer Amber's call":
            hide screen walkthrough_screen
            $ ep01_ambcall = True
            jump ep01_home

label ep01_bath:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (elizabeth, trust & cor, +1)
##RM.POINTS.TRACK (elizabeth, cor/trust, +1)
# --
#MOM'S CONUNDRUM
    show ep01_elidress01 with dissolve
    mc_s "[renpy.substitute(dialogues['E01S26_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d003'])]"
    mc_y "[renpy.substitute(dialogues['E01S26_d004'])]"
    $ playAudio(sfx_dooropen, "sfx", 1, False, 0, 0)
    show ep01_elidress04 with slowfade
    $ playAudio(elizabeth_theme, "music", 2, True, 2.5, 0)
    mc_t "[renpy.substitute(dialogues['E01S26_d005'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d006'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d007'])]"
    show ep01_elidress03
    mc_t "[renpy.substitute(dialogues['E01S26_d008'])]"
    eli "[renpy.substitute(dialogues['E01S26_d009'])]"
    show ep01_elidress02
    mc_s "[renpy.substitute(dialogues['E01S26_d010'])]"
    eli "[renpy.substitute(dialogues['E01S26_d011'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d012'])]"
    eli "[renpy.substitute(dialogues['E01S26_d013'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d014'])]"
    show ep01_elidress05
    eli "[renpy.substitute(dialogues['E01S26_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d016'])]"
    eli "[renpy.substitute(dialogues['E01S26_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d018'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d019'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d020'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d021'])]"
    show ep01_elidress06
    eli "[renpy.substitute(dialogues['E01S26_d022'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d023'])]"
    eli "[renpy.substitute(dialogues['E01S26_d024'])]"
    eli "[renpy.substitute(dialogues['E01S26_d025'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d026'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d027'])]"
    show ep01_elidress07 with vpunch
    eli "[renpy.substitute(dialogues['E01S26_d028'])]"
    eli "[renpy.substitute(dialogues['E01S26_d029'])]"
    mc_s "[renpy.substitute(dialogues['E01S25_d010'])]"
    show ep01_elidress08
    eli "[renpy.substitute(dialogues['E01S26_d030'])]"
    eli "[renpy.substitute(dialogues['E01S26_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d032'])]"
    eli "[renpy.substitute(dialogues['E01S26_d033'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d034'])]"
    show ep01_elidress09
    eli "[renpy.substitute(dialogues['E01S26_d035'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d036'])]"
    eli "[renpy.substitute(dialogues['E01S26_d037'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d038'])]"
    eli "[renpy.substitute(dialogues['E01S26_d039'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d040'])]"
    show ep01_elidress10
    eli "[renpy.substitute(dialogues['E01S26_d041'])]"
    eli "[renpy.substitute(dialogues['E01S26_d042'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d043'])]"
    eli "[renpy.substitute(dialogues['E01S26_d044'])]"
    eli "[renpy.substitute(dialogues['E01S26_d045'])]"
    $ show_walkthrough("ep01_elidress_menu")
    menu:
        "Play along":
            hide screen walkthrough_screen
            $ ep01_elimemories = True
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
            mc_s "[renpy.substitute(dialogues['E01S26_d046'])]"
            show ep01_elidress12 with vpunch
            eli "[renpy.substitute(dialogues['E01S26_d047'])]"
            eli "[renpy.substitute(dialogues['E01S26_d048'])]"
            eli "[renpy.substitute(dialogues['E01S26_d049'])]"
            $ rm.update("elizabeth", "cor", 1)
            $ check_levels("elizabeth", "cor", 1)
            eli "[renpy.substitute(dialogues['E01S26_d050'])]"
            eli "[renpy.substitute(dialogues['E01S26_d051'])]"
            mc_s "[renpy.substitute(dialogues['E01S26_d052'])]"
            eli "[renpy.substitute(dialogues['E01S26_d053'])]"
        "Stop her":
            hide screen walkthrough_screen
            mc_y "[renpy.substitute(dialogues['E01S26_d054'])]"
            show ep01_elidress11 with hpunch
            eli "[renpy.substitute(dialogues['E01S26_d055'])]"
            mc_s "[renpy.substitute(dialogues['E01S26_d056'])]"
            eli "[renpy.substitute(dialogues['E01S26_d057'])]"
            eli "[renpy.substitute(dialogues['E01S26_d058'])]"
            mc_s "[renpy.substitute(dialogues['E01S26_d059'])]"
            eli "[renpy.substitute(dialogues['E01S26_d060'])]"
            mc_s "[renpy.substitute(dialogues['E01S26_d061'])]"
            eli "[renpy.substitute(dialogues['E01S26_d062'])]"
            mc_s "[renpy.substitute(dialogues['E01S26_d063'])]"
            mc_s "[renpy.substitute(dialogues['E01S26_d064'])]"
            eli "[renpy.substitute(dialogues['E01S26_d065'])]"
    show ep01_elidress13 with vpunch
    if ep01_elimemories:
        eli "[renpy.substitute(dialogues['E01S26_d066'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d067'])]"
        eli "[renpy.substitute(dialogues['E01S26_d068'])]"
        eli "[renpy.substitute(dialogues['E01S26_d069'])]"
        eli "[renpy.substitute(dialogues['E01S26_d070'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d071'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d072'])]"
    else:
        eli "[renpy.substitute(dialogues['E01S26_d073'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d074'])]"
        eli "[renpy.substitute(dialogues['E01S26_d075'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d076'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d077'])]"
        eli "[renpy.substitute(dialogues['E01S26_d078'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d079'])]"
    show ep01_elidress14 with vpunch
    if ep01_elimemories:
        eli "[renpy.substitute(dialogues['E01S26_d080'])]"
        eli "[renpy.substitute(dialogues['E01S26_d081'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d082'])]"
        eli "[renpy.substitute(dialogues['E01S26_d083'])]"
        eli "[renpy.substitute(dialogues['E01S26_d084'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d085'])]"
        eli "[renpy.substitute(dialogues['E01S26_d086'])]"
        eli "[renpy.substitute(dialogues['E01S26_d087'])]"
        show ep01_elidress16 with hpunch
        mc_s "[renpy.substitute(dialogues['E01S26_d088'])]"
        eli "[renpy.substitute(dialogues['E01S26_d089'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d090'])]"  
        mc_t "[renpy.substitute(dialogues['E01S26_d091'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d092'])]"
        show ep01_elidress15
        mc_t "[renpy.substitute(dialogues['E01S26_d093'])]"
        hide ep01_elidress16
        eli "[renpy.substitute(dialogues['E01S26_d094'])]" 
        mc_t "[renpy.substitute(dialogues['E01S26_d095'])]"
        eli "[renpy.substitute(dialogues['E01S26_d096'])]"
        show ep01_elidress16
        mc_s "[renpy.substitute(dialogues['E01S26_d097'])]"
        eli "[renpy.substitute(dialogues['E01S26_d098'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d003'])]"
        eli "[renpy.substitute(dialogues['E01S26_d100'])]"
    else:
        eli "[renpy.substitute(dialogues['E01S26_d101'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d102'])]"
        mc_t "[renpy.substitute(dialogues['E01S26_d103'])]"
        eli "[renpy.substitute(dialogues['E01S26_d104'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d105'])]"
        eli "[renpy.substitute(dialogues['E01S26_d106'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d107'])]"
        eli "[renpy.substitute(dialogues['E01S26_d108'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d109'])]"
        $ show_walkthrough("ep01_elidress_menu2")
        menu:
            eli "[renpy.substitute(dialogues['E01S26_d110'])]"
            "Check her":
                hide screen walkthrough_screen
                $ rm.update("elizabeth", "cor", 1)
                $ check_levels("elizabeth", "cor", 1)
                show ep01_elidress15
                mc_t "[renpy.substitute(dialogues['E01S26_d111'])]"
                mc_t "[renpy.substitute(dialogues['E01S26_d112'])]"
                eli "[renpy.substitute(dialogues['E01S26_d113'])]"
                eli "[renpy.substitute(dialogues['E01S26_d114'])]" 
                mc_s "[renpy.substitute(dialogues['E01S26_d115'])]"
                mc_t "[renpy.substitute(dialogues['E01S26_d116'])]"
                show ep01_elidress16
                mc_t "[renpy.substitute(dialogues['E01S26_d117'])]"
                eli "[renpy.substitute(dialogues['E01S26_d118'])]"
                mc_s "[renpy.substitute(dialogues['E01S26_d119'])]"
                eli "[renpy.substitute(dialogues['E01S26_d120'])]"
                eli "[renpy.substitute(dialogues['E01S26_d121'])]"
            "Turn around":
                hide screen walkthrough_screen
                $ rm.update("elizabeth", "trust", 1)
                $ check_levels("elizabeth", "trust", 1)
                show ep01_elidress16
                mc_t "[renpy.substitute(dialogues['E01S26_d122'])]"
                mc_t "[renpy.substitute(dialogues['E01S26_d123'])]"
                mc_t "[renpy.substitute(dialogues['E01S26_d124'])]"
                eli "[renpy.substitute(dialogues['E01S26_d125'])]"
    $ stopAudio(channel="music", subchannel=2, fadeout=1.5)
    show ep01_elidress17 with slowfade
    $ playAudio(elizabeth_sexy_theme, "music", 4, True, 2.5, 0)
    mc_t "[renpy.substitute(dialogues['E01S26_d126'])]"
    eli "[renpy.substitute(dialogues['E01S26_d127'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d128'])]"
    eli "[renpy.substitute(dialogues['E01S26_d129'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d130'])]"
    eli "[renpy.substitute(dialogues['E01S26_d131'])]"
    eli "[renpy.substitute(dialogues['E01S26_d132'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d133'])]"
    show ep01_elidress18
    eli "[renpy.substitute(dialogues['E01S26_d134'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d135'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d136'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d137'])]"
    eli "[renpy.substitute(dialogues['E01S26_d138'])]"
    show ep01_elidress19
    eli "[renpy.substitute(dialogues['E01S26_d139'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d140'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d141'])]"
    eli "[renpy.substitute(dialogues['E01S26_d142'])]"
    eli "[renpy.substitute(dialogues['E01S26_d143'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d144'])]"
    show ep01_elidress20
    eli "[renpy.substitute(dialogues['E01S26_d145'])]"
    eli "[renpy.substitute(dialogues['E01S26_d146'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d147'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d148'])]"
    eli "[renpy.substitute(dialogues['E01S26_d149'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d150'])]"
    scene eigengrau with circlewipe
    show ep01_elidress21 with circlewipe
    mc_s "[renpy.substitute(dialogues['E01S26_d151'])]"
    eli "[renpy.substitute(dialogues['E01S26_d152'])]"
    eli "[renpy.substitute(dialogues['E01S26_d153'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d154'])]"
    eli "[renpy.substitute(dialogues['E01S26_d155'])]"
    eli "[renpy.substitute(dialogues['E01S26_d156'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d157'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d158'])]"
    show ep01_elidress23
    eli "[renpy.substitute(dialogues['E01S26_d159'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d160'])]"
    eli "[renpy.substitute(dialogues['E01S26_d161'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d162'])]"
    eli "[renpy.substitute(dialogues['E01S26_d163'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d164'])]"
    show ep01_elidress22
    eli "[renpy.substitute(dialogues['E01S26_d165'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d166'])]"
    eli "[renpy.substitute(dialogues['E01S26_d167'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d168'])]"
    eli "[renpy.substitute(dialogues['E01S26_d169'])]"
    show ep01_elidress24
    eli "[renpy.substitute(dialogues['E01S26_d170'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d003'])]"
    eli "[renpy.substitute(dialogues['E01S26_d172'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d173'])]"
    eli "[renpy.substitute(dialogues['E01S26_d174'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d175'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d176'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_elidress25
    $ show_walkthrough("ep01_elibathdress_menu")
    menu:
        eli "[renpy.substitute(dialogues['E01S26_d177'])]"
        "Pick black dress":
            hide screen walkthrough_screen
            $ ep01_elidress += 1
            mc_s "[renpy.substitute(dialogues['E01S26_d178'])]"
            mc_t "[renpy.substitute(dialogues['E01S26_d179'])]"
        "Pick red dress":
            hide screen walkthrough_screen
            $ ep01_elidress += 2
            mc_s "[renpy.substitute(dialogues['E01S26_d180'])]"
            mc_t "[renpy.substitute(dialogues['E01S26_d181'])]"
    eli "[renpy.substitute(dialogues['E01S26_d182'])]"
    eli "[renpy.substitute(dialogues['E01S26_d183'])]"
    eli "[renpy.substitute(dialogues['E01S26_d184'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d185'])]"
    show ep01_elidress26
    eli "[renpy.substitute(dialogues['E01S26_d186'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d187'])]"
    eli "[renpy.substitute(dialogues['E01S26_d188'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d189'])]"
    eli "[renpy.substitute(dialogues['E01S26_d190'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d191'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d192'])]"
    show ep01_elidress27 with hpunch
    if ep01_elidress == 1:
        eli "[renpy.substitute(dialogues['E01S26_d193'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d194'])]"
        eli "[renpy.substitute(dialogues['E01S26_d195'])]"
        eli "[renpy.substitute(dialogues['E01S26_d196'])]"
    elif ep01_elidress == 2:
        eli "[renpy.substitute(dialogues['E01S26_d197'])]"
        mc_s "[renpy.substitute(dialogues['E01S26_d198'])]"
        eli "[renpy.substitute(dialogues['E01S26_d199'])]"
        eli "[renpy.substitute(dialogues['E01S26_d200'])]"
    mc_s "[renpy.substitute(dialogues['E01S26_d201'])]"
    mc_t "[renpy.substitute(dialogues['E01S26_d202'])]"
    if not ep01_ambcall:
        mc_t "[renpy.substitute(dialogues['E01S26_d203'])]"
    else:
        pass
    if ep01_ambcall:
        jump ep01_station
    else:
        jump ep01_home

label ep01_home:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (amber, trust, +1)
##RM.POINTS.TRACK (amber, trust, -1)
# --
#AMBER CALLOUT
    show ep01_amberfail01 with hpunch
    $ playAudio(sfx_slamdoorhard, "sfx", 1, False, 0, 0)
    mc_s "[renpy.substitute(dialogues['E01S27_d001'])]"
    if ep01_elicall:
        mc_s "[renpy.substitute(dialogues['E01S27_d002'])]"
    else:
        mc_s "[renpy.substitute(dialogues['E01S27_d003'])]"
    show ep01_amberfail02
    mc_s "[renpy.substitute(dialogues['E01S27_d004'])]"
    amb "[renpy.substitute(dialogues['E01S27_d005'])]"
    if ep01_elicall:
        mc_t "[renpy.substitute(dialogues['E01S27_d006'])]"
    else:
        mc_t "[renpy.substitute(dialogues['E01S27_d007'])]"
    mc_t "[renpy.substitute(dialogues['E01S27_d008'])]"
    show ep01_amberfail03
    mc_s "[renpy.substitute(dialogues['E01S27_d009'])]"
    if ep01_elicall:
        amb "[renpy.substitute(dialogues['E01S27_d010'])]"
    else:
        amb "[renpy.substitute(dialogues['E01S27_d011'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d012'])]"
    amb "[renpy.substitute(dialogues['E01S27_d013'])]"
    show ep01_amberfail04
    mc_s "[renpy.substitute(dialogues['E01S27_d014'])]"
    amb "[renpy.substitute(dialogues['E01S27_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d016'])]"
    amb "[renpy.substitute(dialogues['E01S27_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d018'])]"
    $ playAudio(amber_anger_theme, "music", 2, True, 2.5, 0)
    show ep01_amberfail05
    amb "[renpy.substitute(dialogues['E01S27_d019'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d020'])]"
    show ep01_amberfail06
    $ unlock_memory("m_ep01_laundry")
    amb "[renpy.substitute(dialogues['E01S27_d021'])]"
    amb "[renpy.substitute(dialogues['E01S27_d022'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d023'])]"
    amb "[renpy.substitute(dialogues['E01S27_d024'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d025'])]"
    amb "[renpy.substitute(dialogues['E01S27_d026'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d027'])]"
    amb "[renpy.substitute(dialogues['E01S27_d028'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    show ep01_amberconfess01 with slowfade
    mc_s "[renpy.substitute(dialogues['E01S27_d029'])]"
    amb "[renpy.substitute(dialogues['E01S27_d030'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d031'])]"
    show ep01_amberconfess02 with hpunch
    amb "[renpy.substitute(dialogues['E01S27_d032'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d033'])]"
    show ep01_amberconfess03
    mc_t "[renpy.substitute(dialogues['E01S27_d034'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d035'])]"
    amb "[renpy.substitute(dialogues['E01S27_d036'])]"
    amb "[renpy.substitute(dialogues['E01S27_d037'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d038'])]"
    amb "[renpy.substitute(dialogues['E01S27_d039'])]"
    mc_s "[renpy.substitute(dialogues['E01S27_d040'])]"
    amb "[renpy.substitute(dialogues['E01S27_d041'])]"
    amb "[renpy.substitute(dialogues['E01S27_d042'])]"
    $ show_walkthrough("ep01_amberconfess_menu")
    menu:
        "Stay":
            hide screen walkthrough_screen
            $ ep01_ambtalk = True
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            mc_t "[renpy.substitute(dialogues['E01S27_d043'])]"
            mc_s "[renpy.substitute(dialogues['E01S27_d044'])]"
            amb "[renpy.substitute(dialogues['E01S27_d045'])]"
            mc_s "[renpy.substitute(dialogues['E01S27_d046'])]"
            mc_t "[renpy.substitute(dialogues['E01S27_d047'])]"
            amb "[renpy.substitute(dialogues['E01S27_d048'])]"
        "Leave":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -1)
            $ check_levels("amber", "trust", -1)
            mc_t "[renpy.substitute(dialogues['E01S27_d049'])]"
            mc_t "[renpy.substitute(dialogues['E01S27_d050'])]"
            mc_s "[renpy.substitute(dialogues['E01S27_d051'])]"
            amb "[renpy.substitute(dialogues['E01S27_d052'])]"
            mc_s "[renpy.substitute(dialogues['E01S27_d053'])]"
            amb "[renpy.substitute(dialogues['E01S27_d054'])]"
            amb "[renpy.substitute(dialogues['E01S27_d055'])]"
            if ep01_elicall:
                jump ep01_station
            else:
                jump ep01_bath

#AMBER CONFESSION (ep01_ambtalk = True)
    $ playAudio(amber_sad_theme, "music", 2, True, 2.5, 0)
    show ep01_amberconfess04 with slowfade
    amb "[renpy.substitute(dialogues['E01S28_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d002'])]"
    if ep01_park == 1:
        amb "[renpy.substitute(dialogues['E01S28_d003'])]"
    elif ep01_park == 2:
        if ep01_lieamber:
            amb "[renpy.substitute(dialogues['E01S28_d004'])]"
        else:
            amb "[renpy.substitute(dialogues['E01S28_d005'])]"     
    amb "[renpy.substitute(dialogues['E01S28_d006'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d007'])]"
    amb "[renpy.substitute(dialogues['E01S28_d008'])]"
    amb "[renpy.substitute(dialogues['E01S28_d009'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d010'])]"
    show ep01_amberconfess05
    amb "[renpy.substitute(dialogues['E01S28_d011'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d012'])]"
    amb "[renpy.substitute(dialogues['E01S28_d013'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d014'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d015'])]"
    show ep01_amberconfess06
    amb "[renpy.substitute(dialogues['E01S28_d016'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d017'])]"
    amb "[renpy.substitute(dialogues['E01S28_d018'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d019'])]"
    amb "[renpy.substitute(dialogues['E01S28_d020'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d021'])]"
    show ep01_amberconfess07
    amb "[renpy.substitute(dialogues['E01S28_d022'])]"
    amb "[renpy.substitute(dialogues['E01S28_d023'])]"
    amb "[renpy.substitute(dialogues['E01S28_d024'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d025'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d026'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d027'])]"
    mc_t "[renpy.substitute(dialogues['E01S28_d028'])]"
    show ep01_amberconfess08
    amb "[renpy.substitute(dialogues['E01S28_d029'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d030'])]"
    amb "[renpy.substitute(dialogues['E01S28_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d032'])]"
    show ep01_amberconfess09
    mc_t "[renpy.substitute(dialogues['E01S28_d033'])]"
    mc_t "[renpy.substitute(dialogues['E01S28_d034'])]"
    mc_t "[renpy.substitute(dialogues['E01S28_d035'])]"
    mc_t "[renpy.substitute(dialogues['E01S28_d036'])]"
    show ep01_amberconfess10 with hpunch
    amb "[renpy.substitute(dialogues['E01S28_d037'])]"
    amb "[renpy.substitute(dialogues['E01S28_d038'])]"
    show ep01_amberconfess11
    $ unlock_memory("m_ep01_confession")
    amb "[renpy.substitute(dialogues['E01S28_d039'])]"
    amb "[renpy.substitute(dialogues['E01S28_d040'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d041'])]"
    amb "[renpy.substitute(dialogues['E01S28_d042'])]"
    show ep01_amberconfess12
    amb "[renpy.substitute(dialogues['E01S28_d043'])]"
    amb "[renpy.substitute(dialogues['E01S28_d044'])]"
    amb "[renpy.substitute(dialogues['E01S28_d045'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d046'])]"
    show ep01_amberconfess14 with vpunch
    amb "[renpy.substitute(dialogues['E01S28_d047'])]"
    amb "[renpy.substitute(dialogues['E01S28_d048'])]"
    mc_s "[renpy.substitute(dialogues['E01S28_d049'])]"
    amb "[renpy.substitute(dialogues['E01S28_d050'])]"
    amb "[renpy.substitute(dialogues['E01S28_d051'])]"
    amb "[renpy.substitute(dialogues['E01S28_d052'])]"
    amb "[renpy.substitute(dialogues['E01S28_d053'])]"
    show ep01_amberconfess15
    amb "[renpy.substitute(dialogues['E01S28_d054'])]"
    if not ep01_elicall:
        $ show_walkthrough("ep01_amberconfess_menu2")
    else:
        $ show_walkthrough("ep01_amberconfess_menu2b")
    menu:
        mc_t "[renpy.substitute(dialogues['E01S28_d055'])]"
        "Yes": #WILL SKIP ELIZABETH
            hide screen walkthrough_screen
            $ ep01_amblove = True
            $ stopAllSubchannels(channel="music", fadeout=8)
            mc_t "[renpy.substitute(dialogues['E01S28_d056'])]"
            mc_t "[renpy.substitute(dialogues['E01S28_d057'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d058'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d059'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d060'])]"
            amb "[renpy.substitute(dialogues['E01S28_d061'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d062'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d063'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d064'])]"
            mc_t "[renpy.substitute(dialogues['E01S28_d065'])]"
            show ep01_amberconfess16 with hpunch
            amb "[renpy.substitute(dialogues['E01S28_d066'])]"
            amb "[renpy.substitute(dialogues['E01S28_d067'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d068'])]"
            amb "[renpy.substitute(dialogues['E01S28_d069'])]"
            amb "[renpy.substitute(dialogues['E01S28_d070'])]"  
            amb "[renpy.substitute(dialogues['E01S28_d071'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d072'])]"
            amb "[renpy.substitute(dialogues['E01S28_d073'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d074'])]"
            amb "[renpy.substitute(dialogues['E01S28_d075'])]"
            show ep01_amberconfess17
            mc_t "[renpy.substitute(dialogues['E01S28_d076'])]"
            amb "[renpy.substitute(dialogues['E01S28_d077'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d078'])]"
            mc_t "[renpy.substitute(dialogues['E01S28_d079'])]"
            mc_t "[renpy.substitute(dialogues['E01S28_d080'])]"
            amb "[renpy.substitute(dialogues['E01S28_d081'])]"
            amb "[renpy.substitute(dialogues['E01S28_d082'])]"
        "No":
            hide screen walkthrough_screen
            $ stopAllSubchannels(channel="music", fadeout=8)
            mc_t "[renpy.substitute(dialogues['E01S28_d083'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d084'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d085'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d086'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d087'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d088'])]"
            show ep01_amberconfess13 with vpunch
            amb "[renpy.substitute(dialogues['E01S28_d089'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d090'])]"
            amb "[renpy.substitute(dialogues['E01S28_d091'])]" 
            mc_s "[renpy.substitute(dialogues['E01S28_d092'])]"
            amb "[renpy.substitute(dialogues['E01S28_d093'])]"
            amb "[renpy.substitute(dialogues['E01S28_d094'])]"
            mc_s "[renpy.substitute(dialogues['E01S28_d095'])]"
            amb "[renpy.substitute(dialogues['E01S28_d096'])]"
            mc_t "[renpy.substitute(dialogues['E01S28_d097'])]"
            if ep01_elicall:
                $ stopAllSubchannels(channel="amb", fadeout=1.5)
                jump ep01_station
            else:
                mc_t "[renpy.substitute(dialogues['E01S28_d098'])]"
                jump ep01_bath

#AMBER NIGHT
    scene eigengrau with dissolve
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    show ep01_amberconfess18 with ccirclewipe
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.1)
    $ playAudio(sfx_night_cicada, "amb", 2, True, 2.5, 0)
    amb_t "[renpy.substitute(dialogues['E01S29_d001'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d002'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d003'])]"
    show ep01_amberconfess19
    amb "[renpy.substitute(dialogues['E01S29_d004'])]"
    amb "[renpy.substitute(dialogues['E01S29_d005'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d006'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d007'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d008'])]"
    amb "[renpy.substitute(dialogues['E01S29_d009'])]"
    amb "[renpy.substitute(dialogues['E01S29_d005'])]"
    show ep01_amberconfess20 with vpunch
    amb "[renpy.substitute(dialogues['E01S29_d011'])]"
    show ep01_amberconfess20 with vpunch
    amb "[renpy.substitute(dialogues['E01S29_d005'])]"
    show ep01_amberconfess20 with vpunch
    amb_t "[renpy.substitute(dialogues['E01S29_d013'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d014'])]"
    show ep01_amberconfess21 with vpunch
    amb_t "[renpy.substitute(dialogues['E01S29_d015'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d016'])]"
    show ep01_amberconfess21 with vpunch
    amb "[renpy.substitute(dialogues['E01S29_d017'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d018'])]"
    show ep01_amberconfess21 with vpunch
    amb_t "[renpy.substitute(dialogues['E01S29_d019'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d020'])]"
    show ep01_amberconfess22
    amb_t "[renpy.substitute(dialogues['E01S29_d021'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d022'])]"
    show ep01_amberconfess23
    amb_t "[renpy.substitute(dialogues['E01S29_d023'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d024'])]"
    amb "[renpy.substitute(dialogues['E01S29_d025'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d026'])]"
    show ep01_amberconfess24
    amb_t "[renpy.substitute(dialogues['E01S29_d027'])]"
    show ep01_amberconfess24 with hpunch
    amb "[renpy.substitute(dialogues['E01S29_d028'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d029'])]"
    show ep01_amberconfess26 with slowfade
    amb_t "[renpy.substitute(dialogues['E01S29_d030'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d031'])]"
    amb_t "[renpy.substitute(dialogues['E01S29_d032'])]"
    show ep01_amberconfess26 with vpunch
    mc_s "[renpy.substitute(dialogues['E01S29_d033'])]"
    mc_s "[renpy.substitute(dialogues['E01S29_d034'])]"
    show ep01_amberconfess25
    amb "[renpy.substitute(dialogues['E01S29_d035'])]"
    mc_s "[renpy.substitute(dialogues['E01S29_d036'])]"
    amb "[renpy.substitute(dialogues['E01S29_d037'])]"
    amb "[renpy.substitute(dialogues['E01S29_d038'])]"
    amb "[renpy.substitute(dialogues['E01S29_d039'])]"
    mc_s "[renpy.substitute(dialogues['E01S29_d040'])]"
    amb "[renpy.substitute(dialogues['E01S29_d041'])]"
    amb "[renpy.substitute(dialogues['E01S29_d042'])]"
    mc_s "[renpy.substitute(dialogues['E01S29_d043'])]"
    amb "[renpy.substitute(dialogues['E01S29_d044'])]"
    mc_s "[renpy.substitute(dialogues['E01S29_d045'])]"
    amb "[renpy.substitute(dialogues['E01S29_d046'])]"
    $ show_walkthrough("ep01_amberconfess_menu3")
    menu:
        amb "[renpy.substitute(dialogues['E01S29_d047'])]"
        "Yes":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ ep01_first = True
            mc_t "[renpy.substitute(dialogues['E01S29_d048'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d049'])]"
            mc_t "[renpy.substitute(dialogues['E01S29_d050'])]"
            $ playAudio(amber_sexy_theme2, "music", 2, True, 2.5, 0)
            show ep01_amberconfess32 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d051'])]"  
            amb "[renpy.substitute(dialogues['E01S29_d052'])]"
            mc_t "[renpy.substitute(dialogues['E01S29_d053'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d054'])]"
            amb "[renpy.substitute(dialogues['E01S29_d055'])]" 
            show ep01_amberconfess33 with circlewipe
            amb "[renpy.substitute(dialogues['E01S29_d056'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d057'])]"
            amb "[renpy.substitute(dialogues['E01S29_d058'])]" 
            mc_s "[renpy.substitute(dialogues['E01S29_d059'])]"
            amb "[renpy.substitute(dialogues['E01S29_d060'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d061'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d062'])]"
            show ep01_amberconfess34
            amb "[renpy.substitute(dialogues['E01S29_d063'])]" 
            amb "[renpy.substitute(dialogues['E01S29_d064'])]"
            mc_t "[renpy.substitute(dialogues['E01S29_d065'])]"
            mc_t "[renpy.substitute(dialogues['E01S29_d066'])]"
            amb "[renpy.substitute(dialogues['E01S29_d067'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d068'])]" 
            show ep01_amberconfess35
            amb "[renpy.substitute(dialogues['E01S29_d069'])]"
            mc_t "[renpy.substitute(dialogues['E01S29_d070'])]"
            show ep01_amberconfess37
            amb "[renpy.substitute(dialogues['E01S29_d071'])]" 
            mc_t "[renpy.substitute(dialogues['E01S29_d072'])]"
            show ep01_amberconfess36
            amb "[renpy.substitute(dialogues['E01S29_d073'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d074'])]"
            amb "[renpy.substitute(dialogues['E01S29_d075'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d076'])]"
            amb "[renpy.substitute(dialogues['E01S29_d077'])]"  
            mc_s "[renpy.substitute(dialogues['E01S29_d078'])]"
            show ep01_amberconfess40 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d079'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d080'])]"
            amb "[renpy.substitute(dialogues['E01S29_d081'])]"  
            amb "[renpy.substitute(dialogues['E01S29_d082'])]" 
            mc_s "[renpy.substitute(dialogues['E01S29_d083'])]"
            amb "[renpy.substitute(dialogues['E01S29_d084'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d085'])]" 
            amb "[renpy.substitute(dialogues['E01S29_d086'])]"
            show ep01_amberconfess38
            amb "[renpy.substitute(dialogues['E01S29_d087'])]" 
            show ep01_amberconfess38 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d088'])]" 
            amb "[renpy.substitute(dialogues['E01S29_d089'])]"
            show ep01_amberconfess38 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d090'])]"
            show ep01_amberconfess38 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d091'])]"  
            mc_s "[renpy.substitute(dialogues['E01S29_d092'])]"
            show ep01_amberconfess41 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d093'])]"
            amb "[renpy.substitute(dialogues['E01S29_d094'])]"
            show ep01_amberconfess41 with vpunch
            mc_t "[renpy.substitute(dialogues['E01S29_d095'])]"
            mc_t "[renpy.substitute(dialogues['E01S29_d096'])]" 
            show ep01_amberconfess41 with vpunch 
            mc_s "[renpy.substitute(dialogues['E01S29_d097'])]"
            amb "[renpy.substitute(dialogues['E01S29_d098'])]"
            show ep01_amberconfess41 with vpunch
            eli_y "[renpy.substitute(dialogues['E01S29_d099'])]"
            show ep01_amberconfess42
            mc_s "[renpy.substitute(dialogues['E01S29_d100'])]"
            amb "[renpy.substitute(dialogues['E01S29_d101'])]" 
            amb_y "[renpy.substitute(dialogues['E01S29_d102'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d103'])]"
            amb "[renpy.substitute(dialogues['E01S29_d104'])]"
            amb_y "[renpy.substitute(dialogues['E01S29_d105'])]"  
            mc_s "[renpy.substitute(dialogues['E01S29_d106'])]"
            eli_y "[renpy.substitute(dialogues['E01S29_d107'])]"
            amb_y "[renpy.substitute(dialogues['E01S29_d108'])]"
            eli_y "[renpy.substitute(dialogues['E01S29_d109'])]"  
            mc_s "[renpy.substitute(dialogues['E01S29_d059'])]"  
            show ep01_amberconfess39
            mc_s "[renpy.substitute(dialogues['E01S29_d110'])]"
            amb "[renpy.substitute(dialogues['E01S29_d111'])]" 
            amb "[renpy.substitute(dialogues['E01S29_d112'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d005'])]"
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            jump ep01_station
        "No":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S29_d114'])]"
            show ep01_amberconfess28 with hpunch
            mc_s "[renpy.substitute(dialogues['E01S29_d115'])]"
            mc_s "[renpy.substitute(dialogues['E01S29_d116'])]"
            show ep01_amberconfess27
            amb "[renpy.substitute(dialogues['E01S29_d117'])]"  
            mc_s "[renpy.substitute(dialogues['E01S29_d118'])]"
            show ep01_amberconfess29 with vpunch
            amb "[renpy.substitute(dialogues['E01S29_d119'])]"  
            mc_s "[renpy.substitute(dialogues['E01S29_d120'])]"  
            amb "[renpy.substitute(dialogues['E01S29_d121'])]"
            show ep01_amberconfess30 with vpunch
            mc_y "[renpy.substitute(dialogues['E01S29_d122'])]"
            amb "[renpy.substitute(dialogues['E01S29_d123'])]"
            show ep01_amberconfess31 
            mc_s "[renpy.substitute(dialogues['E01S29_d124'])]"
            amb "[renpy.substitute(dialogues['E01S29_d125'])]"
            amb "[renpy.substitute(dialogues['E01S29_d126'])]"
            $ stopAllSubchannels(channel="amb", fadeout=1.5)  
            jump ep01_station

label ep01_station:
    scene eigengrau with clouds
##RM.POINTS.TRACK (isabella, trust, +1)
# --
#ARRIVING TO TOKYO
    show ep01_antobd01 with bokeh
    $ playAudio(sfx_stationbeep, "amb", 2, True, 2.5, 0)
    $ playAudio(sfx_trainstationquiet, "amb", 1, True, 2.5, 0)
    isa "[renpy.substitute(dialogues['E01S30_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d002'])]"
    isa "[renpy.substitute(dialogues['E01S30_d003'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d004'])]"
    isa "[renpy.substitute(dialogues['E01S30_d005'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d006'])]"
    show ep01_antobd02
    isa "[renpy.substitute(dialogues['E01S30_d007'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d008'])]"
    isa "[renpy.substitute(dialogues['E01S30_d009'])]"
    show ep01_antobd03 with ccirclewipe
    $ stopAudio(channel="amb", subchannel=1, fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    mc_t "[renpy.substitute(dialogues['E01S30_d010'])]"
    mc_t "[renpy.substitute(dialogues['E01S30_d011'])]"
    isa "[renpy.substitute(dialogues['E01S30_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d013'])]"
    show ep01_antobd05
    isa "[renpy.substitute(dialogues['E01S30_d014'])]"
    isa "[renpy.substitute(dialogues['E01S30_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d016'])]"
    isa "[renpy.substitute(dialogues['E01S30_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d018'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d019'])]"
    show ep01_antobd04
    isa "[renpy.substitute(dialogues['E01S30_d020'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d021'])]"
    isa "[renpy.substitute(dialogues['E01S30_d022'])]"
    $ show_walkthrough("ep01_antobd04_menu1")
    menu:
        "Mention Antonella":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", 1)
            $ check_levels("isabella", "trust", 1)
            mc_s "[renpy.substitute(dialogues['E01S30_d023'])]"
            mc_t "[renpy.substitute(dialogues['E01S30_d024'])]"
            show ep01_antobd06
            isa "[renpy.substitute(dialogues['E01S30_d025'])]"
            mc_s "[renpy.substitute(dialogues['E01S30_d026'])]"
            isa "[renpy.substitute(dialogues['E01S30_d027'])]"  
            mc_s "[renpy.substitute(dialogues['E01S30_d028'])]"
            isa "[renpy.substitute(dialogues['E01S30_d029'])]"
            mc_t "[renpy.substitute(dialogues['E01S30_d030'])]"
        "Don't mention Antonella":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues['E01S30_d031'])]"
            mc_t "[renpy.substitute(dialogues['E01S30_d032'])]"
            isa "[renpy.substitute(dialogues['E01S30_d033'])]"
            show ep01_antobd08
            isa "[renpy.substitute(dialogues['E01S30_d034'])]"
            mc_s "[renpy.substitute(dialogues['E01S30_d035'])]"
            isa "[renpy.substitute(dialogues['E01S30_d036'])]"  
            mc_s "[renpy.substitute(dialogues['E01S30_d037'])]"
            isa "[renpy.substitute(dialogues['E01S30_d038'])]"
            mc_s "[renpy.substitute(dialogues['E01S30_d039'])]"
            mc_s "[renpy.substitute(dialogues['E01S30_d040'])]"
    show ep01_antobd07
    isa "[renpy.substitute(dialogues['E01S30_d041'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d042'])]"
    isa "[renpy.substitute(dialogues['E01S30_d043'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d044'])]"
    isa "[renpy.substitute(dialogues['E01S30_d045'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d046'])]"
    isa "[renpy.substitute(dialogues['E01S30_d047'])]"
    show ep01_antobd09 with slowfade
    isa "[renpy.substitute(dialogues['E01S30_d048'])]"
    mc_s "[renpy.substitute(dialogues['E01S30_d049'])]"
    mc_t "[renpy.substitute(dialogues['E01S30_d050'])]"
    show ep01_antobd10
    mc_t "[renpy.substitute(dialogues['E01S30_d051'])]"
    $ show_walkthrough("ep01_antobd_menu2")
    menu:
        "Look at girl":
            hide screen walkthrough_screen
            $ ep01_antobday = True
            mc_t "[renpy.substitute(dialogues['E01S30_d052'])]"
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            show ep01_antobd11 with vpunch
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4)
            $ playAudio(sfx_glitch, "sfx", 1, True, 2.5, 0)
            show ep01_antobd11 at animated_glitch
            mc_t "[renpy.substitute(dialogues['E01S30_d053'])]"
            mc_t "[renpy.substitute(dialogues['E01S30_d054'])]"
            jump ep01_birthday
        "Don't look at her":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues['E01S30_d055'])]"
            mc_t "[renpy.substitute(dialogues['E01S30_d056'])]"
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            jump ep01_newhome

label ep01_birthday:
    scene eigengrau with dissolve
#ANTONELLA BDAY

    show ep01_antobd12 with clouds_inverse
    show ep01_antobd12 at animated_glitch
    mc_s "[renpy.substitute(dialogues['E01S31_d001'])]"
    anto "[renpy.substitute(dialogues['E01S31_d002'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d003'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=2.5)
    show ep01_antobd13
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_restaurant, "amb", 1, True, 1.5, 0)
    anto "[renpy.substitute(dialogues['E01S31_d004'])]"
    $ playAudio(antonella_past_happy_theme, "music", 2, True, 5, 0)
    mc_s "[renpy.substitute(dialogues['E01S31_d005'])]"
    anto "[renpy.substitute(dialogues['E01S31_d006'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d007'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d008'])]"
    show ep01_antobd14 with vpunch
    anto "[renpy.substitute(dialogues['E01S31_d009'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d010'])]"
    anto "[renpy.substitute(dialogues['E01S31_d011'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d012'])]"
    anto "[renpy.substitute(dialogues['E01S31_d013'])]"
    show ep01_antobd15 with slowfade
    anto "[renpy.substitute(dialogues['E01S31_d014'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d015'])]"
    anto "[renpy.substitute(dialogues['E01S31_d016'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d017'])]"
    show ep01_antobd16
    anto "[renpy.substitute(dialogues['E01S31_d018'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d019'])]"
    anto "[renpy.substitute(dialogues['E01S31_d020'])]"
    show ep01_antobd17
    anto "[renpy.substitute(dialogues['E01S31_d021'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d023'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d024'])]"
    $ stopAllSubchannels(channel="music", fadeout=2.5)
    show ep01_antobd18
    $ playAudio(sfx_glitch, "sfx", 1, True, 2.5, 0)
    show ep01_antobd18 at animated_glitch
    mc_t "[renpy.substitute(dialogues['E01S31_d025'])]"
    anto "[renpy.substitute(dialogues['E01S31_d026'])]"
    show ep01_antobd19 at animated_glitch
    mc_t "[renpy.substitute(dialogues['E01S31_d027'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d028'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    show ep01_antobd20 with slowfade
    anto "[renpy.substitute(dialogues['E01S31_d029'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d030'])]"
    anto "[renpy.substitute(dialogues['E01S31_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d032'])]"
    show ep01_antobd21
    anto "[renpy.substitute(dialogues['E01S31_d033'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d034'])]"
    anto "[renpy.substitute(dialogues['E01S31_d035'])]"
    anto "[renpy.substitute(dialogues['E01S31_d036'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d037'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d038'])]"
    show ep01_antobd22 with hpunch
    mc_t "[renpy.substitute(dialogues['E01S31_d039'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d040'])]"
    show ep01_antobd23 with slowfade
    $ playAudio(antonella_mistery_theme, "music", 3, True, 1.5, 0)
    mc_s "[renpy.substitute(dialogues['E01S31_d041'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d042'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d043'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d044'])]"
    show ep01_antobd24
    mc_s "[renpy.substitute(dialogues['E01S31_d045'])]"
    anto "[renpy.substitute(dialogues['E01S31_d046'])]"
    show ep01_antobd25
    mc_s "[renpy.substitute(dialogues['E01S31_d047'])]"
    anto "[renpy.substitute(dialogues['E01S31_d048'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d049'])]"
    show ep01_antobd26
    anto "[renpy.substitute(dialogues['E01S31_d050'])]"
    anto "[renpy.substitute(dialogues['E01S31_d051'])]"
    anto "[renpy.substitute(dialogues['E01S31_d052'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d053'])]"
    show ep01_antobd27
    anto "[renpy.substitute(dialogues['E01S31_d054'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d055'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d056'])]"
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    show ep01_antobd28
    mc_s "[renpy.substitute(dialogues['E01S31_d057'])]"
    anto "[renpy.substitute(dialogues['E01S31_d058'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d059'])]"
    show ep01_antobd29
    anto "[renpy.substitute(dialogues['E01S31_d060'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d061'])]"
    anto "[renpy.substitute(dialogues['E01S31_d062'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d063'])]"
    show ep01_antobd30
    anto "[renpy.substitute(dialogues['E01S31_d064'])]"
    anto "[renpy.substitute(dialogues['E01S31_d065'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d066'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d067'])]"
    anto "[renpy.substitute(dialogues['E01S31_d068'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d069'])]"
    $ playAudio(antonella_love, "music", 2, True, 2.5, 0)
    show ep01_antobd31
    mc_s "[renpy.substitute(dialogues['E01S31_d070'])]"
    anto "[renpy.substitute(dialogues['E01S31_d071'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d072'])]"
    show ep01_antobd32
    anto "[renpy.substitute(dialogues['E01S31_d073'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d066'])]"
    anto "[renpy.substitute(dialogues['E01S31_d075'])]"
    show ep01_antobd33
    anto "[renpy.substitute(dialogues['E01S31_d076'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d077'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d078'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d079'])]"
    show ep01_antobd34
    anto "[renpy.substitute(dialogues['E01S31_d080'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d081'])]"
    show ep01_antobd36
    anto "[renpy.substitute(dialogues['E01S31_d082'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d083'])]"
    show ep01_antobd37
    anto "[renpy.substitute(dialogues['E01S31_d084'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d085'])]"
    anto "[renpy.substitute(dialogues['E01S31_d086'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d087'])]"
    anto "[renpy.substitute(dialogues['E01S31_d088'])]"
    scene eigengrau with dissolve
    show ep01_antobd35 with hpunch
    anto "[renpy.substitute(dialogues['E01S31_d089'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d090'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d091'])]"
    anto "[renpy.substitute(dialogues['E01S31_d092'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d093'])]"
    anto "[renpy.substitute(dialogues['E01S31_d094'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d095'])]"
    show ep01_antobd38
    anto "[renpy.substitute(dialogues['E01S31_d096'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d097'])]"
    anto "[renpy.substitute(dialogues['E01S31_d098'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d099'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d100'])]"
    show ep01_antobd39 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S31_d001'])]"
    show ep01_antobd40 with flash
    mc_t "[renpy.substitute(dialogues['E01S31_d102'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d103'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d104'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d105'])]"
    show ep01_antobd41 with hpunch
    mc_s "[renpy.substitute(dialogues['E01S31_d106'])]"
    anto "[renpy.substitute(dialogues['E01S31_d107'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d108'])]"
    anto "[renpy.substitute(dialogues['E01S31_d109'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d110'])]"
    anto "[renpy.substitute(dialogues['E01S31_d111'])]"
    anto "[renpy.substitute(dialogues['E01S31_d112'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d113'])]"
    show ep01_antobd42
    anto "[renpy.substitute(dialogues['E01S31_d114'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d115'])]"
    anto "[renpy.substitute(dialogues['E01S31_d116'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d117'])]"
    show ep01_antobd43 with slowfade
    anto "[renpy.substitute(dialogues['E01S31_d118'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d119'])]"
    anto "[renpy.substitute(dialogues['E01S31_d120'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d068'])]"
    anto "[renpy.substitute(dialogues['E01S31_d122'])]"
    show ep01_antobd44 with hpunch
    anto "[renpy.substitute(dialogues['E01S31_d123'])]"
    anto "[renpy.substitute(dialogues['E01S31_d124'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d125'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with clouds
    show ep01_backhome01 with bokeh
    $ playAudio(sfx_stationbeep, "amb", 2, True, 2.5, 0)
    isa "[renpy.substitute(dialogues['E01S31_d126'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d127'])]"
    isa "[renpy.substitute(dialogues['E01S31_d128'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d129'])]"
    isa "[renpy.substitute(dialogues['E01S31_d130'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d131'])]"
    isa "[renpy.substitute(dialogues['E01S31_d132'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d133'])]"
    show ep01_backhome02 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S31_d134'])]"
    isa "[renpy.substitute(dialogues['E01S31_d135'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d136'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d137'])]"
    isa "[renpy.substitute(dialogues['E01S31_d138'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d139'])]"
    show ep01_backhome03
    isa "[renpy.substitute(dialogues['E01S31_d140'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d141'])]"
    isa "[renpy.substitute(dialogues['E01S31_d142'])]"
    isa "[renpy.substitute(dialogues['E01S31_d143'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d144'])]"
    isa "[renpy.substitute(dialogues['E01S31_d145'])]"
    mc_s "[renpy.substitute(dialogues['E01S31_d146'])]"
    mc_t "[renpy.substitute(dialogues['E01S31_d147'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_newhome

label ep01_newhome:
    scene eigengrau with dissolve
#TRAVEL TO NEW HOME
    $ playAudio(sfx_taxidoor, "sfx", 5, False, 0, 0)
    show ep01_backhome04 with circlewipe
    $ playAudio(sfx_taxiint, "amb", 1, True, 2.5, 0)
    isa "[renpy.substitute(dialogues['E01S32_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d002'])]"
    isa "[renpy.substitute(dialogues['E01S32_d003'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d004'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d005'])]"
    show ep01_backhome05
    isa "[renpy.substitute(dialogues['E01S32_d006'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d007'])]"
    isa "[renpy.substitute(dialogues['E01S32_d008'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d009'])]"
    isa "[renpy.substitute(dialogues['E01S32_d010'])]"
    show ep01_backhome06
    isa "[renpy.substitute(dialogues['E01S32_d011'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d012'])]"
    isa "[renpy.substitute(dialogues['E01S32_d013'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d014'])]"
    $ playAudio(isabella_theme, "music", 2, True, 2.5, 0)
    show ep01_backhome07
    isa "[renpy.substitute(dialogues['E01S32_d015'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d016'])]"
    isa "[renpy.substitute(dialogues['E01S32_d017'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d018'])]"
    isa "[renpy.substitute(dialogues['E01S32_d019'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d020'])]"
    isa "[renpy.substitute(dialogues['E01S32_d021'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d022'])]"
    show ep01_backhome08
    isa "[renpy.substitute(dialogues['E01S32_d023'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d024'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d025'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d026'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d027'])]"
    show ep01_backhome12 with vpunch
    isa "[renpy.substitute(dialogues['E01S32_d028'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d029'])]"
    isa "[renpy.substitute(dialogues['E01S32_d030'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d031'])]"
    show ep01_backhome11 with hpunch
    isa "[renpy.substitute(dialogues['E01S32_d032'])]"
    isa "[renpy.substitute(dialogues['E01S32_d033'])]"
    isa "[renpy.substitute(dialogues['E01S32_d034'])]"
    isa "[renpy.substitute(dialogues['E01S32_d035'])]"
    isa "[renpy.substitute(dialogues['E01S32_d036'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d037'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d038'])]"
    show ep01_backhome13 with vpunch
    isa "[renpy.substitute(dialogues['E01S32_d039'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d040'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d041'])]"
    isa "[renpy.substitute(dialogues['E01S32_d042'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d043'])]"
    show ep01_backhome14
    isa "[renpy.substitute(dialogues['E01S32_d044'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d045'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d046'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d047'])]"
    show ep01_backhome15
    isa "[renpy.substitute(dialogues['E01S32_d048'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d049'])]"
    isa "[renpy.substitute(dialogues['E01S32_d050'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d051'])]"
    isa "[renpy.substitute(dialogues['E01S32_d052'])]"
    isa "[renpy.substitute(dialogues['E01S32_d053'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d054'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d055'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d056'])]"
    isa "[renpy.substitute(dialogues['E01S32_d057'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d058'])]"
    show ep01_backhome16 with hpunch
    isa "[renpy.substitute(dialogues['E01S32_d059'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d060'])]"
    isa "[renpy.substitute(dialogues['E01S32_d061'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d062'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d063'])]"
    show ep01_backhome18
    isa "[renpy.substitute(dialogues['E01S32_d064'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d065'])]"
    isa "[renpy.substitute(dialogues['E01S32_d066'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d067'])]"
    isa "[renpy.substitute(dialogues['E01S32_d068'])]"
    show ep01_backhome17
    isa "[renpy.substitute(dialogues['E01S32_d069'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d070'])]"
    isa "[renpy.substitute(dialogues['E01S32_d071'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d072'])]"
    show ep01_backhome09 with slowfade
    isa "[renpy.substitute(dialogues['E01S32_d073'])]"
    mc_s "[renpy.substitute(dialogues['E01S32_d074'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d075'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d076'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d077'])]"
    show ep01_backhome10
    mc_t "[renpy.substitute(dialogues['E01S32_d078'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d079'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d080'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d081'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d082'])]"
    show ep01_backhome19 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S32_d083'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d084'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d085'])]"
    mc_t "[renpy.substitute(dialogues['E01S32_d086'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_glitch, "sfx", 1, True, 2.5, 0)
    show eigengrau at animated_glitch
    pause 1
#THE BABY
    show ep01_backhome23 with slowfade
    show ep01_backhome23 at animated_glitch
    mc_s "[renpy.substitute(dialogues['E01S33_d001'])]"
    mc_s "[renpy.substitute(dialogues['E01S33_d002'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1.5)
    $ playAudio(sfx_heartbeatfast, "sfx", 5, True, 2.5, 0)
    $ playAudio(mc_broken_theme, "music", 2, True, 2.5, 0)
    show ep01_backhome23
    mic "[renpy.substitute(dialogues['E01S33_d003'])]"
    mc_s "[renpy.substitute(dialogues['E01S33_d004'])]"
    eli "[renpy.substitute(dialogues['E01S33_d005'])]"
    mic "[renpy.substitute(dialogues['E01S33_d006'])]"
    eli "[renpy.substitute(dialogues['E01S33_d007'])]"
    mic "[renpy.substitute(dialogues['E01S33_d008'])]"
    show ep01_backhome29
    amb "[renpy.substitute(dialogues['E01S33_d009'])]"
    mic "[renpy.substitute(dialogues['E01S33_d010'])]"
    amb "[renpy.substitute(dialogues['E01S33_d011'])]"
    mic "[renpy.substitute(dialogues['E01S33_d012'])]"
    mc_s "[renpy.substitute(dialogues['E01S33_d013'])]"
    show ep01_backhome27
    mic "[renpy.substitute(dialogues['E01S33_d014'])]"
    mc_s "[renpy.substitute(dialogues['E01S33_d015'])]"
    mic "[renpy.substitute(dialogues['E01S33_d016'])]"
    mic "[renpy.substitute(dialogues['E01S33_d017'])]"
    show ep01_backhome24
    eli "[renpy.substitute(dialogues['E01S33_d018'])]"
    mic "[renpy.substitute(dialogues['E01S33_d019'])]"
    show ep01_backhome25
    eli "[renpy.substitute(dialogues['E01S33_d020'])]"
    mic "[renpy.substitute(dialogues['E01S33_d021'])]"
    eli "[renpy.substitute(dialogues['E01S33_d022'])]"
    mic "[renpy.substitute(dialogues['E01S33_d023'])]"
    eli "[renpy.substitute(dialogues['E01S33_d024'])]"
    mc_t "[renpy.substitute(dialogues['E01S33_d025'])]"
    mc_t "[renpy.substitute(dialogues['E01S33_d026'])]"
    show ep01_backhome28
    mc_t "[renpy.substitute(dialogues['E01S33_d027'])]"
    mc_t "[renpy.substitute(dialogues['E01S33_d028'])]"
    mc_t "[renpy.substitute(dialogues['E01S33_d029'])]"
    show ep01_backhome26
    mc_t "[renpy.substitute(dialogues['E01S33_d030'])]"
    amb "[renpy.substitute(dialogues['E01S33_d031'])]"
    mc_s "[renpy.substitute(dialogues['E01S33_d032'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ resetAllVolumes()
    scene eigengrau with rose
    pause 2
#-- End Episode 1
    call hideNoise(transition=dissolve)
    jump ep02_title

