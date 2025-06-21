label ep04_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ renpy.block_rollback()
    jump ep04_intro
## -- INTRO SCENE HOME

label ep04_intro:
    
    call showNoise(0.1, 0.15, transition=dissolve)
    $ config.rollback_enabled = True
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 1, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_wind_pool, "amb", 2, True, 1, 0)
    show ep04_intro1 at zoom_out with slowfade
    show screen stats_button
    show screen walkthrough_icon
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d003'])]"
    show ep04_intro2 at concentrate
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d005'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d006'])]"
    show ep04_intro3 at ken_burns_bottom_to_top with normalfade
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d007'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d008'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d009'])]"
    show ep04_intro4 at focus_shift, ken_burns_corner_to_corner
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d010'])]"
    mc_t "[renpy.substitute(dialogues4['E04INTRO_d011'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    jump ep04_nanapool

label ep04_nanapool:
    scene eigengrau with bokeh2
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_intro01 at slow_reveal with slowfade
    mc_t "[renpy.substitute(dialogues4['E04POOL_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d002'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d003'])]"
    show ep04_nan_intro02 at focus_shift, ken_burns_left_to_right
    mc_t "[renpy.substitute(dialogues4['E04POOL_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d006'])]"
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_yellnana, "sfx", 9, False, 0, 0)
    show ep04_nan_intro03 with hpunch
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d008'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_splashpool, "sfx", 1, False, 0, 0)
    show ep04_nan_intro04 at subtle_zoom_out with vpunch
    mc_t "[renpy.substitute(dialogues4['E04POOL_d009'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d010'])]"
    scene eigengrau with circlewipe
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_pool_splash, "sfx", 2, False, 0, 0)
    show ep04_nan_intro05 with circlewipe
    mc_s "[renpy.substitute(dialogues4['E04POOL_d011'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d013'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d015'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d017'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.5)
    $ playAudio(sfx_pool_surfacing, "sfx", 3, False, 0, 0)
    show ep04_nan_intro07 at slow_reveal with vpunch
    mc_t "[renpy.substitute(dialogues4['E04POOL_d018'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d019'])]"
    show ep04_nan_intro06
    mc_s "[renpy.substitute(dialogues4['E04POOL_d020'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d021'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d022'])]"
    show ep04_nan_intro08 at ken_burns_right_to_left
    mc_s "[renpy.substitute(dialogues4['E04POOL_d023'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d025'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d026'])]"
    show ep04_nan_intro09
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d028'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d030'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d032'])]"
    show ep04_nan_intro10
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d033'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d021'])]"
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d036'])]"
    show ep04_nan_intro11
    "Girl" "[renpy.substitute(dialogues4['E04POOL_d037'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.15)
    $ playAudio(nanami_theme, "music", 1, True, 5, 0)
    nana "[renpy.substitute(dialogues4['E04POOL_d038'])]"
    $ rm.set_knows("nanami", True)
    mc_s "[renpy.substitute(dialogues4['E04POOL_d039'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d040'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d041'])]"
    show ep04_nan_intro12
    nana "[renpy.substitute(dialogues4['E04POOL_d042'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d043'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d044'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d045'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d046'])]"
    show ep04_nan_intro13
    mc_s "[renpy.substitute(dialogues4['E04POOL_d047'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d049'])]"
    show ep04_nan_intro14
    nana "[renpy.substitute(dialogues4['E04POOL_d050'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d051'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d052'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d053'])]"
    show ep04_nan_intro15 at ken_burns_left_to_right
    mc_s "[renpy.substitute(dialogues4['E04POOL_d054'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d055'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d057'])]"
    show ep04_nan_intro16
    nana "[renpy.substitute(dialogues4['E04POOL_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d052'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d060'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d061'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d062'])]"
    show ep04_nan_intro17 at focus_shift, subtle_zoom_out
    mc_t "[renpy.substitute(dialogues4['E04POOL_d063'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d064'])]"
    show ep04_nan_intro18 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues4['E04POOL_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d066'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d067'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d068'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d069'])]"
    show ep04_nan_intro19
    nana "[renpy.substitute(dialogues4['E04POOL_d070'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d071'])]"
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_eeeh_female, "sfx", 4, False, 0, 0)
    show ep04_nan_intro20 with hpunch
    $ stopAudio(channel="music", subchannel=1, fadeout=1)
    nana "[renpy.substitute(dialogues4['E04POOL_d072'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d073'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d074'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d075'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d076'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d077'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d078'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d079'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d080'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d081'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d082'])]"
    show ep04_nan_intro21 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues4['E04POOL_d083'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d084'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d085'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d086'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d087'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d088'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d089'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d090'])]"
    hide ep04_nan_intro21 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04POOL_d091'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d092'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d093'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d094'])]"
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.8)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)
    show ep04_nan_intro22 with vpunch
    nana "[renpy.substitute(dialogues4['E04POOL_d095'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d096'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d097'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d098'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 2, True, 0, 0)
    show ep04_nan_intro23
    nana "[renpy.substitute(dialogues4['E04POOL_d099'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d100'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d101'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d102'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d103'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d104'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d105'])]"
    show ep04_nan_intro24 at focus_shift, subtle_zoom_out
    mc_t "[renpy.substitute(dialogues4['E04POOL_d106'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d107'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d059'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d108'])]"
    show ep04_nan_intro25 with vpunch
    nana "[renpy.substitute(dialogues4['E04POOL_d109'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d110'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d111'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_hallwalkmale, "sfx", 7, False, 0, 1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAudio(channel="music", subchannel=2, fadeout=1)
    scene eigengrau with slowfade
    pause 2
    $ stopAudio(channel="sfx", subchannel=7, fadeout=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_intro26 with circlewipe
    nana "[renpy.substitute(dialogues4['E04POOL_d112'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d113'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d114'])]"
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.8)
    $ playAudio(sfx_bodyfall, "sfx", 8, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.8)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)
    show ep04_nan_intro27 at subtle_zoom_in with vpunch
    nana "[renpy.substitute(dialogues4['E04POOL_d115'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4)
    $ playAudio(sfx_water_walk, "sfx", 1, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04POOL_d116'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d117'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 3, True, 0, 0)
    show ep04_nan_intro28 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04POOL_d118'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d119'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d120'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d121'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d122'])]"
    show ep04_nan_intro29
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_laughnana2, "sfx", 2, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04POOL_d123'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d124'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d125'])]"
    show ep04_nan_intro30
    nana "[renpy.substitute(dialogues4['E04POOL_d126'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d127'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d128'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d129'])]"
    show ep04_nan_intro31 at ken_burns_right_to_left
    nana "[renpy.substitute(dialogues4['E04POOL_d130'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d131'])]"
    show ep04_nan_intro32
    nana "[renpy.substitute(dialogues4['E04POOL_d132'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d133'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d134'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d135'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d136'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d137'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d138'])]"
    $ stopAudio(channel="music", subchannel=3, fadeout=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 9, False, 0, 0)
    show ep04_nan_intro33 at subtle_zoom_in with slowfade
    mc_t "[renpy.substitute(dialogues4['E04POOL_d139'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d140'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d141'])]"
    mc_t "[renpy.substitute(dialogues4['E04POOL_d142'])]"
    $ stopAudio(channel="sfx", subchannel=9, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_eeh_nanami, "sfx", 1, False, 0, 0)
    show ep04_nan_intro34 at ken_burns_bottom_to_top with hpunch
    nana "[renpy.substitute(dialogues4['E04POOL_d143'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d144'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d145'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d146'])]"
    show ep04_nan_intro35
    nana "[renpy.substitute(dialogues4['E04POOL_d147'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d052'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d149'])]"
    mc_s "[renpy.substitute(dialogues4['E04POOL_d150'])]"
    nana "[renpy.substitute(dialogues4['E04POOL_d151'])]"
    $ show_walkthrough("ep04_nana_m1")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04POOL_d152'])]"
        "Don't stop her":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues4['E04POOL_d153'])]"
            mc_t "[renpy.substitute(dialogues4['E04POOL_d154'])]"
            mc_s "[renpy.substitute(dialogues4['E04POOL_d155'])]"
            $ ep04_nanpath += 1
            $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
            $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
            jump ep04_nanpool
        "Stop her":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues4['E04POOL_d156'])]"
            mc_t "[renpy.substitute(dialogues4['E04POOL_d157'])]"
            mc_t "[renpy.substitute(dialogues4['E04POOL_d158'])]"
            mc_s "[renpy.substitute(dialogues4['E04POOL_d159'])]"
            nana "[renpy.substitute(dialogues4['E04POOL_d160'])]"
            mc_s "[renpy.substitute(dialogues4['E04POOL_d161'])]"
            $ ep04_nanpath += 2
            jump ep04_nantowel

label ep04_nanpool:
    scene eigengrau with slowfade
    pause 1.5 
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_bikini01 at dramatic_realization with circlewipe
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(nanami_chill_theme, "music", 1, True, 5, 0)
    nana "[renpy.substitute(dialogues4['E04BIK_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d003'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d005'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d006'])]"
    $ show_walkthrough("ep04_nana_m2")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04BIK_d007'])]"
        "Be honest and check her out":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04BIK_d008'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d009'])]"
            show ep04_nan_bikini02 at subtle_zoom_in, ken_burns_bottom_to_top
            mc_s "[renpy.substitute(dialogues4['E04BIK_d010'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d011'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d012'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d013'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d014'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d015'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d016'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d017'])]"
            show ep04_nan_bikini03 at subtle_zoom_in, ken_burns_top_to_bottom
            nana "[renpy.substitute(dialogues4['E04BIK_d018'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d019'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d020'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d021'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d022'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d023'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d024'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d025'])]"
            nana "[renpy.substitute(dialogues4['E04BIK_d026'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIK_d027'])]"
        "Don't":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04BIK_d028'])]"
            pass
    show ep04_nan_bikini04 with vpunch
    nana "[renpy.substitute(dialogues4['E04BIK_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d030'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d032'])]"
    show ep04_nan_bikini05 with normalfade
    nana "[renpy.substitute(dialogues4['E04BIK_d033'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d034'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d035'])]"
    show ep04_nan_bikini06
    nana "[renpy.substitute(dialogues4['E04BIK_d036'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d037'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d038'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d039'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d040'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d041'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d042'])]"
    show ep04_nan_bikini07
    nana "[renpy.substitute(dialogues4['E04BIK_d043'])]"
    $ stopAudio(channel="music", subchannel=1, fadeout=2.5)
    mc_s "[renpy.substitute(dialogues4['E04BIK_d044'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d045'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d046'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d047'])]"
    show ep04_nan_bikini08 at ken_burns_left_to_right with hpunch
    nana "[renpy.substitute(dialogues4['E04BIK_d048'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d049'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d050'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d051'])]"
    show ep04_nan_bikini09 at focus_shift, subtle_zoom_in
    nana "[renpy.substitute(dialogues4['E04BIK_d052'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d053'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d054'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d055'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d057'])]"
    $ setChannelVolume(channel="music", subchannel=5, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 5, True, 0, 0)
    show ep04_nan_bikini10 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04BIK_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d059'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d060'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d061'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d062'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d063'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d064'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d066'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d067'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d068'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d069'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d070'])]"
    show ep04_nan_bikini11 at ken_burns_top_to_bottom with vpunch
    nana "[renpy.substitute(dialogues4['E04BIK_d071'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d072'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d073'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d074'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d075'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d076'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d077'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d078'])]"
    nana "[renpy.substitute(dialogues4['E04BIK_d079'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIK_d080'])]"
    $ stopAudio(channel="music", subchannel=5, fadeout=2)
    show ep04_nan_bikini12
    nana "[renpy.substitute(dialogues4['E04BIK_d081'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIK_d082'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms01

label ep04_amb_sms01_bik_post:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_bikini12
    hide ep04_ambersmsbg1
    mc_s "[renpy.substitute(dialogues4['E04NANP_d001'])]"
    nana "[renpy.substitute(dialogues4['E04NANP_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANP_d003'])]"
    scene eigengrau with dissolve
    show ep04_nan_bikini13 at focus_pulse, subtle_breathing with slowfade
    nana "[renpy.substitute(dialogues4['E04NANP_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANP_d005'])]"
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)
            show ep04_nan_bikini13 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "[renpy.substitute(dialogues4['EP04SMS5PA_d007'])]..."
    hide photo_flash
    show ep04_nan_bikini14 at focus_pulse, subtle_breathing
    nana "[renpy.substitute(dialogues4['E04NANP_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANP_d007'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANP_d008'])]"
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)
            show ep04_nan_bikini14 at photo_effect with flash
            show photo_flash with dissolve
            pause
    mc_t "[renpy.substitute(dialogues4['E04NANP_d009'])]"
    show ep04_nan_bikini15
    hide photo_flash
    nana "[renpy.substitute(dialogues4['E04NANP_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANP_d011'])]"
    nana "[renpy.substitute(dialogues4['E04NANP_d012'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms02

label ep04_nanpool2:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    hide ep04_ambersmsbg2
    if ep03_amberstrike:
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d001'])]"
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d002'])]"
    elif ep03_amberangry: 
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d003'])]"
    elif ep04_amberno: 
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d004'])]"
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d005'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d006'])]"
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d007'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_eeh_nanami, "sfx", 1, False, 0, 0)
    show ep04_nan_bikini16 with vpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d008'])]"
    if ep03_amberangry or ep03_amberstrike:
        pass
    else:
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d009'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d011'])]"
    show ep04_nan_bikini18
    nana "[renpy.substitute(dialogues4['E04BIKINI_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d013'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d015'])]"
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 4, True, 0, 0)
    show ep04_nan_bikini17
    nana "[renpy.substitute(dialogues4['E04BIKINI_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d017'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d019'])]"
    show ep04_nan_bikini19 at ken_burns_left_to_right
    nana "[renpy.substitute(dialogues4['E04BIKINI_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d021'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d022'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d023'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d025'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
    $ playAudio(sfx_pool_moving, "sfx", 1, False, 0, 0)
    show ep04_nan_bikini20 at subtle_zoom_in, ken_burns_bottom_to_top with normalfade
    nana "[renpy.substitute(dialogues4['E04BIKINI_d026'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d027'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d028'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d029'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d030'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d031'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d032'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d033'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d034'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d035'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d036'])]"
    $ show_walkthrough("ep04_nana_m3")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d037'])]"
        "Accept her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", 12)
            $ check_levels("nanami", "trust", 12)
            $ ep04_nanadad = True
            mc_s "[renpy.substitute(dialogues4['E04BIKINI_d038'])]"
            nana "[renpy.substitute(dialogues4['E04BIKINI_d039'])]"
            mc_s "[renpy.substitute(dialogues4['E04BIKINI_d040'])]"
        "Deny her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", -5)
            $ check_levels("nanami", "trust", -5)
            mc_s "[renpy.substitute(dialogues4['E04BIKINI_d041'])]"
            nana "[renpy.substitute(dialogues4['E04BIKINI_d042'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_pool_moving, "sfx", 2, False, 0, 0)
    show ep04_nan_bikini21 at ken_burns_right_to_left with slowfade
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d043'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d044'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d045'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d046'])]"
    show ep04_nan_bikini22 at ken_burns_corner_to_corner2 with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d047'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d049'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d050'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d051'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d052'])]"
    show ep04_nan_bikini23 at ken_burns_bottom_to_top
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d053'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d054'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d055'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d056'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d057'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d058'])]"
    show ep04_nan_bikini24 at ken_burns_top_to_bottom with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d059'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d060'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d061'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d062'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d063'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d064'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d066'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d067'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d068'])]"
    $ stopAudio(channel="music", subchannel=4, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.6)
    $ playAudio(sfx_water_walk, "sfx", 8, False, 0, 0)
    show ep04_nan_bikini25 with hpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d069'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d070'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d071'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d072'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d073'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d074'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d075'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d076'])]"
    $ stopAudio(channel="sfx", subchannel=8, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_pool_outof, "sfx", 2, False, 0, 0)
    show ep04_nan_bikini26 with normalfade
    nana "[renpy.substitute(dialogues4['E04BIKINI_d077'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d078'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d079'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d080'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=5)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_bikini27 at focus_shift, ken_burns_right_to_left with dissolve
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d081'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d082'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d083'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d084'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d085'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d086'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d087'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d088'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d089'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d090'])]"
    show ep04_nan_bikini28 at subtle_zoom_out, subtle_breathing
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d091'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d092'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d093'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d094'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d095'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d096'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d097'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d098'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d099'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d100'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d101'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d102'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d103'])]"
    show ep04_nan_bikini29 with vpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d104'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d105'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d106'])]"
    show ep04_nan_bikini30 with normalfade
    nana "[renpy.substitute(dialogues4['E04BIKINI_d107'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d108'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d109'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d110'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d111'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d112'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d113'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d114'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 1, True, 0, 0)
    show ep04_nan_bikini31
    nana "[renpy.substitute(dialogues4['E04BIKINI_d115'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d116'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d117'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d118'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d119'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d120'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d121'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d122'])]"
    show ep04_nan_bikini32 with hpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d123'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d124'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d125'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d126'])]"
    show ep04_nan_bikini33 at ken_burns_right_to_left
    nana "[renpy.substitute(dialogues4['E04BIKINI_d127'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d128'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d129'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d130'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d131'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d132'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d133'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d134'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d135'])]"
    show ep04_nan_bikini34 at ken_burns_top_to_bottom
    nana "[renpy.substitute(dialogues4['E04BIKINI_d136'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d137'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d138'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d139'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d140'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d141'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d142'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_surprisenana, "sfx", 1, False, 0, 0)
    show ep04_nan_bikini35 with vpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d143'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d144'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d145'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d146'])]"
    show ep04_nan_bikini36 with hpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d147'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d148'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d149'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d150'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d151'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d152'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d153'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d154'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d155'])]"
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 3, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_bikini37 at ken_burns_top_to_bottom with circlewipe
    $ stopAudio(channel="sfx", subchannel=3, fadeout=1)
    nana "[renpy.substitute(dialogues4['E04BIKINI_d156'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d157'])]"
        mc_t "[renpy.substitute(dialogues4['E04BIKINI_d158'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d159'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d160'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d161'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d162'])]"
    show ep04_nan_bikini38 at impact_shake
    nana "[renpy.substitute(dialogues4['E04BIKINI_d163'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d164'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d165'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d166'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d167'])]"
    show ep04_nan_bikini39 at ken_burns_left_to_right with hpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d168'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d014'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d170'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d171'])]"
    show ep04_nan_bikini40 at dramatic_focus with vpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d172'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d173'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d174'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d175'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d176'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 2, True, 0, 0)
    show ep04_nan_bikini41 at ken_burns_left_to_right with hpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d177'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d178'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d179'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d180'])]"
    show ep04_nan_bikini42 at ken_burns_bottom_to_top with hpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d181'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d182'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d183'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d184'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    show ep04_nan_bikini43 at subtle_breathing with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d185'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d186'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d187'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d188'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d189'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d190'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d191'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.6)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)
    show ep04_nan_bikini44 with vpunch
    nana "[renpy.substitute(dialogues4['E04BIKINI_d192'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d193'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d194'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d195'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d196'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d197'])]"
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d198'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d199'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d200'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 7, False, 0, 0)
    show ep04_nan_bikini45 at subtle_zoom_out
    mc_s "[renpy.substitute(dialogues4['E04BIKINI_d201'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d202'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04BIKINI_d203'])]"
    nana "[renpy.substitute(dialogues4['E04BIKINI_d204'])]"
    mc_t "[renpy.substitute(dialogues4['E04BIKINI_d205'])]"
    $ ep04_ach_nanabikini = True
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_madcaught

label ep04_nantowel:
    show ep04_nan_clothes01
    nana "[renpy.substitute(dialogues4['E04TOW_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d002'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d004'])]"
    show ep04_nan_clothes02 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues4['E04TOW_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d007'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d008'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.1)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)
    show ep04_nan_clothes03
    mc_s "[renpy.substitute(dialogues4['E04TOW_d009'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d010'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d012'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d013'])]"
    show ep04_nan_clothes04
    nana "[renpy.substitute(dialogues4['E04TOW_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d015'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d016'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.2, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(nanami_chill_theme, "music", 1, True, 5, 0)
    show ep04_nan_clothes05 at subtle_breathing, ken_burns_left_to_right with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04TOW_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d018'])]"
    show ep04_nan_clothes06 at subtle_breathing, ken_burns_right_to_left with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04TOW_d019'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d020'])]"
    show ep04_nan_clothes07 at focus_shift, dramatic_realization
    mc_t "[renpy.substitute(dialogues4['E04TOW_d021'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d022'])]"
    pause 1.5
    show ep04_nan_clothes08 at subtle_breathing, ken_burns_left_to_right with normalfade
    mc_t "[renpy.substitute(dialogues4['E04TOW_d023'])]"
    show ep04_nan_clothes09 at focus_shift, ken_burns_top_to_bottom
    mc_t "[renpy.substitute(dialogues4['E04TOW_d024'])]"
    pause 1.5
    show ep04_nan_clothes10 at subtle_breathing, ken_burns_right_to_left with normalfade
    mc_t "[renpy.substitute(dialogues4['E04TOW_d025'])]"
    show ep04_nan_clothes11 at focus_shift, subtle_zoom_out
    mc_t "[renpy.substitute(dialogues4['E04TOW_d026'])]"
    pause 1.5
    show ep04_nan_clothes12 at subtle_breathing, ken_burns_left_to_right with normalfade
    mc_t "[renpy.substitute(dialogues4['E04TOW_d027'])]"
    show ep04_nan_clothes13 at focus_shift, ken_burns_bottom_to_top
    mc_t "[renpy.substitute(dialogues4['E04TOW_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d029'])]"
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_clothes14 with circlewipe
    $ stopAudio(channel="music", subchannel=1, fadeout=2)
    nana "[renpy.substitute(dialogues4['E04TOW_d030'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d031'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d032'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d033'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d034'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d036'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d037'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d038'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d039'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_hallwalkmale, "sfx", 2, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_clothes15 at ken_burns_bottom_to_top with circlewipe
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1)
    mc_s "[renpy.substitute(dialogues4['E04TOW_d040'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d041'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d042'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d043'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d044'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d045'])]"
    show ep04_nan_clothes17
    nana "[renpy.substitute(dialogues4['E04TOW_d046'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d047'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 2, True, 0, 0)
    nana "[renpy.substitute(dialogues4['E04TOW_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d049'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d050'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d051'])]"
    show ep04_nan_clothes19
    nana "[renpy.substitute(dialogues4['E04TOW_d052'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d053'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d055'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d057'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d059'])]"
    show ep04_nan_clothes20
    nana "[renpy.substitute(dialogues4['E04TOW_d060'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d061'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d062'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d063'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d064'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d065'])]"
    show ep04_nan_clothes16 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues4['E04TOW_d066'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d067'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d068'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d069'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d070'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d071'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d072'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d073'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d074'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d075'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d076'])]"
    show ep04_nan_clothes18 at subtle_zoom_out with vpunch
    nana "[renpy.substitute(dialogues4['E04TOW_d077'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d078'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d079'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d080'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d081'])]"
    $ stopAudio(channel="music", subchannel=2, fadeout=2)
    show ep04_nan_clothes21 with vpunch
    nana "[renpy.substitute(dialogues4['E04TOW_d082'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d083'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d084'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d085'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d086'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d087'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d088'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d089'])]"
    show ep04_nan_clothes22 at ken_burns_right_to_left with normalfade
    nana "[renpy.substitute(dialogues4['E04TOW_d090'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d091'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOW_d092'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d093'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOW_d094'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d095'])]"
    show ep04_nan_clothes23 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04TOW_d096'])]"
    nana "[renpy.substitute(dialogues4['E04TOW_d097'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms01

label ep04_amb_sms01_tow_post:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_clothes23
    hide ep04_ambersmsbg1
    mc_s "[renpy.substitute(dialogues4['E04TOWPHO_d001'])]"
    nana "[renpy.substitute(dialogues4['E04TOWPHO_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOWPHO_d003'])]"
    scene eigengrau with dissolve
    show ep04_nan_clothes24 at focus_pulse, subtle_breathing with slowfade
    nana "[renpy.substitute(dialogues4['E04TOWPHO_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOWPHO_d005'])]"
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)
            show ep04_nan_clothes24 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "[renpy.substitute(dialogues4['EP04SMS5PA_d007'])]..."
    hide photo_flash
    show ep04_nan_clothes25 at focus_pulse, subtle_breathing
    nana "[renpy.substitute(dialogues4['E04TOWPHO_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOWPHO_d007'])]"
    mc_t "[renpy.substitute(dialogues4['E04TOWPHO_d008'])]"
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)
            show ep04_nan_clothes25 at photo_effect with flash
            show photo_flash with dissolve
            pause
    mc_t "[renpy.substitute(dialogues4['E04TOWPHO_d009'])]"
    show ep04_nan_clothes26 with normalfade
    nana "[renpy.substitute(dialogues4['E04TOWPHO_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOWPHO_d011'])]"
    nana "[renpy.substitute(dialogues4['E04TOWPHO_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04TOWPHO_d013'])]"
    nana "[renpy.substitute(dialogues4['E04TOWPHO_d014'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms02

label ep04_nantowel2:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    hide ep04_ambersmsbg2
    if ep03_amberstrike:
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d001'])]"
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d002'])]"
    elif ep03_amberangry: 
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d003'])]"
    elif ep04_amberno: 
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d004'])]"
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d005'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d006'])]"
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d007'])]"
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_eeh_nanami, "sfx", 4, False, 0, 0)
    show ep04_nan_clothes27 with vpunch
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d009'])]"
    if ep03_amberstrike or ep03_amberangry or ep04_amberno:
        pass
    else:
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d010'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d011'])]"
    if ep03_amberstrike or ep03_amberangry:
        mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d012'])]"
        mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d013'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d014'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_towelshake, "sfx", 2, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_laughnana, "sfx", 4, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
    $ playAudio(nanami_theme, "music", 3, True, 0, 0)
    show ep04_nan_clothes28 at ken_burns_corner_to_corner2 with hpunch
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d015'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d016'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d018'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d019'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.6)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 3, False, 0, 0)
    show ep04_nan_clothes29 with vpunch
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d021'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d022'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d024'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d025'])]"
    $ stopAudio(channel="music", subchannel=3, fadeout=2)
    scene eigengrau with slowfade
    pause 1
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 4, True, 0, 0)
    show ep04_nan_clothes30 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d026'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d027'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d028'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d029'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2, fade_duration=1.5)
    show ep04_nan_clothes31 with circlewipe
    $ stopAudio(channel="sfx", subchannel=5, fadeout=1)
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d030'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d032'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d033'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d034'])]"
    $ show_walkthrough("ep04_nana_m3")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d035'])]"
        "Accept her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", 12)
            $ check_levels("nanami", "trust", 12)
            $ ep04_nanadad = True
            mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d036'])]"
            nana "[renpy.substitute(dialogues4['E04NANGOTH_d037'])]"
            mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d038'])]"
        "Deny her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", -5)
            $ check_levels("nanami", "trust", -5)
            mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d039'])]"
            nana "[renpy.substitute(dialogues4['E04NANGOTH_d040'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d041'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d042'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d043'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d044'])]"
    else:
        pass
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAudio(channel="music", subchannel=4, fadeout=2)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=5, volume=0.2)
    $ playAudio(nanami_chill_theme, "music", 5, True, 4, 0)
    show ep04_nan_clothes32 at subtle_breathing, ken_burns_left_to_right with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d045'])]"
    show ep04_nan_clothes33 at focus_shift, ken_burns_bottom_to_top
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d046'])]"
    pause 1.5
    show ep04_nan_clothes34 at subtle_breathing, ken_burns_right_to_left with normalfade
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d047'])]"
    show ep04_nan_clothes35 at focus_shift, ken_burns_top_to_bottom
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d048'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d049'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANGOTH_d050'])]"
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAudio(channel="music", subchannel=5, fadeout=2)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    show ep04_nan_clothes36 with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d051'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d052'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d053'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d055'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d057'])]"
    show ep04_nan_clothes37 with hpunch
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d059'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d060'])]"
    $ setChannelVolume(channel="music", subchannel=7, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 7, True, 0, 0)
    show ep04_nan_clothes38 at subtle_breathing
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d061'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d062'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d063'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d064'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d065'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d066'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d067'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d068'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d069'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d070'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANGOTH_d071'])]"
    show ep04_nan_clothes39 with vpunch
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d072'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANGOTH_d073'])]"
    nana "[renpy.substitute(dialogues4['E04NANGOTH_d074'])]"
    $ ep04_ach_nanagoth = True
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_madcaught

label ep04_madcaught:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(madison_bad_theme, "music", 1, True, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_impact, "sfx", 1, False, 0, 0)
    show ep04_nanmad01 at action_sequence, subtle_zoom_out
    mad "[renpy.substitute(dialogues4['E04MADNAN_d001'])]"
    nana "[renpy.substitute(dialogues4['E04MADNAN_d002'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MADNAN_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADNAN_d005'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d006'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)
    show ep04_nanmad02 at ken_burns_left_to_right with hpunch
    nana "[renpy.substitute(dialogues4['E04MADNAN_d007'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADNAN_d009'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADNAN_d011'])]"
    nana "[renpy.substitute(dialogues4['E04MADNAN_d012'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MADNAN_d014'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d015'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADNAN_d016'])]"
    mad "[renpy.substitute(dialogues4['E04MADNAN_d017'])]"
    $ show_walkthrough("ep04_nanamad_1")
    menu:
        "Defend Nanami":
            hide screen walkthrough_screen
            $ ep04_madpath += 1
            $ rm.update("nanami", "trust", 12)
            $ check_levels("nanami", "trust", 12)
            mc_s "[renpy.substitute(dialogues4['E04MADNAN_d018'])]"
            jump ep04_madcaught_defend
        "Make peace with Madison":
            hide screen walkthrough_screen
            $ ep04_madpath += 2
            $ rm.update("madison", "trust", 5)
            $ check_levels("madison", "trust", 5)
            jump ep04_madcaught_agree

label ep04_madcaught_defend:
    show ep04_nanmad03 at ken_burns_bottom_to_top with hpunch
    mad "[renpy.substitute(dialogues4['E04NANDEF_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d002'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d003'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d005'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d007'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d009'])]"
    show ep04_nanmad04 at ken_burns_left_to_right
    mad "[renpy.substitute(dialogues4['E04NANDEF_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d011'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d013'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d015'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d016'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d017'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d018'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d019'])]"
    show ep04_nanmad05 at subtle_breathing with vpunch
    mad "[renpy.substitute(dialogues4['E04NANDEF_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d021'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d022'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d023'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_hallwalkfemale, "sfx", 1, False, 0, 0)
    show ep04_nanmad06 at subtle_zoom_in with normalfade
    mad "[renpy.substitute(dialogues4['E04NANDEF_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d025'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d026'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d027'])]"
    mad "[renpy.substitute(dialogues4['E04NANDEF_d028'])]"
    $ stopAudio(channel="music", subchannel=1, fadeout=2)
    show ep04_nanmad07 with normalfade
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    nana "[renpy.substitute(dialogues4['E04NANDEF_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d030'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d032'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d033'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d034'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d036'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_tablehit, "sfx", 2, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.8)
    $ playAudio(sfx_sofa_move, "sfx", 3, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2)
    $ playAudio(nanami_clumsy_theme, "music", 4, True, 0, 0)
    show ep04_nanmad08 with hpunch
    nana "[renpy.substitute(dialogues4['E04NANDEF_d037'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d038'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1)
    scene eigengrau with hpunch
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2, fade_duration=1.5)
    show ep04_nanmad09 at dramatic_focus with normalfade
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_bodyfall, "sfx", 4, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.7)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04NANDEF_d039'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d040'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d041'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d042'])]"
    show ep04_nanmad10 at focus_shift, subtle_breathing, subtle_zoom_out with normalfade
    nana "[renpy.substitute(dialogues4['E04NANDEF_d043'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANDEF_d044'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d045'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d046'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANDEF_d047'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d049'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d050'])]"
    show ep04_nanmad11 at subtle_breathing, impact_shake
    nana "[renpy.substitute(dialogues4['E04NANDEF_d051'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d052'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d053'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d055'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d057'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANDEF_d058'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d059'])]"
    $ stopAudio(channel="music", subchannel=4, fadeout=2)
    show ep04_nanmad12 with vpunch
    nana "[renpy.substitute(dialogues4['E04NANDEF_d060'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d061'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d062'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d063'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d064'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d065'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 1, True, 0, 0)
    show ep04_nanmad13
    nana "[renpy.substitute(dialogues4['E04NANDEF_d066'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d067'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d068'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d069'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d070'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d071'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d072'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d073'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d074'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d075'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d076'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d077'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d078'])]"
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d079'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=1)
    $ playAudio(sfx_kiss_nana, "sfx", 7, False, 0, 0)
    show ep04_nanmad14 at subtle_breathing with vpunch
    nana "[renpy.substitute(dialogues4['E04NANDEF_d080'])]"
    mc_t "[renpy.substitute(dialogues4['E04NANDEF_d081'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d082'])]"
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.8)
    $ playAudio(sfx_footsteps_female_semirun, "sfx", 8, False, 0, 0)
    show ep04_nanmad15 at ken_burns_bottom_to_top with hpunch
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_laughnana, "sfx", 9, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04NANDEF_d083'])]"
    nana "[renpy.substitute(dialogues4['E04NANDEF_d084'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d085'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04NANDEF_d086'])]"
    $ ep04_nanakiss = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_nanarun

label ep04_madcaught_agree:
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d001'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d003'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d004'])]"
    show ep04_nanmad16
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MADAGR_d005'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MADAGR_d006'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d007'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d008'])]"
    show ep04_nanmad17
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d009'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d010'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d012'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d013'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d014'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d015'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d016'])]"
    show ep04_nanmad18 at ken_burns_top_to_bottom with vpunch
    mad "[renpy.substitute(dialogues4['E04MADAGR_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d018'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d019'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d020'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d022'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d023'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d024'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d026'])]"
    show ep04_nanmad19
    nana "[renpy.substitute(dialogues4['E04MADAGR_d027'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d028'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d029'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d030'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d031'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d032'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d033'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d034'])]"
    show ep04_nanmad20
    mad "[renpy.substitute(dialogues4['E04MADAGR_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d036'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d037'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d038'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d039'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d040'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d041'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d042'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d043'])]"
    $ stopAudio(channel="music", subchannel=1, fadeout=2)
    show ep04_nanmad21 at ken_burns_right_to_left
    nana "[renpy.substitute(dialogues4['E04MADAGR_d044'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d045'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d046'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d047'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d048'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d049'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d050'])]"
    if ep04_nanpath == 1:
        mad "[renpy.substitute(dialogues4['E04MADAGR_d051'])]"
    elif ep04_nanpath == 2:
        mad "[renpy.substitute(dialogues4['E04MADAGR_d052'])]"
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
    $ playAudio(sfx_footsteps_heelstile, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=7, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 7, True, 0, 0)
    show ep04_nanmad22
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0, fade_duration=6)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MADAGR_d053'])]"
        mad "[renpy.substitute(dialogues4['E04MADAGR_d054'])]"
        nana "[renpy.substitute(dialogues4['E04MADAGR_d055'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MADAGR_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d057'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d058'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d059'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d060'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_bodygrab, "sfx", 3, False, 0, 0)
    show ep04_nanmad23 with hpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_surprisenana, "sfx", 2, False, 0, 0)
    mad "[renpy.substitute(dialogues4['E04MADAGR_d061'])]"
    nana "[renpy.substitute(dialogues4['E04MADAGR_d062'])]"
    mad "[renpy.substitute(dialogues4['E04MADAGR_d063'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAGR_d064'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAGR_d065'])]"
    if ep03_madtalk:
        $ ep04_ach_madison = True
    else:
        pass
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_nanarun

label ep04_nanarun:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.3)
    $ playAudio(sfx_earlymor, "amb", 3, True, 1, 0)   
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_footsteps_heelstile, "sfx", 1, False, 0, 0)
    show ep04_madnan01 at ken_burns_right_to_left
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0, fade_duration=8)
    mad "[renpy.substitute(dialogues4['E04MADJEL_d001'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d002'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d004'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)
    show ep04_madnan02 at ken_burns_left_to_right with hpunch
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_fearanana, "sfx", 9, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(madison_nan_theme, "music", 2, True, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MADJEL_d005'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d006'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d007'])]"
    if ep04_nanpath == 1:
        mad "[renpy.substitute(dialogues4['E04MADJEL_d008'])]"
    elif ep04_nanpath == 2:
        mad "[renpy.substitute(dialogues4['E04MADJEL_d009'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d010'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d011'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d012'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d014'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d015'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d016'])]"
    show ep04_madnan03 at subtle_zoom_in, ken_burns_bottom_to_top
    if ep04_nanpath == 1:
        mad "[renpy.substitute(dialogues4['E04MADJEL_d017'])]"
    elif ep04_nanpath == 2:
        mad "[renpy.substitute(dialogues4['E04MADJEL_d018'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d019'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d020'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d021'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d022'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d023'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d024'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d025'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d026'])]"
    show ep04_madnan04 at ken_burns_right_to_left with hpunch
    nana "[renpy.substitute(dialogues4['E04MADJEL_d027'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d028'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d029'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d030'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d031'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d032'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d033'])]"
    show ep04_madnan05
    mad "[renpy.substitute(dialogues4['E04MADJEL_d034'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d035'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d036'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d037'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d038'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d039'])]"
    show ep04_madnan06 at dramatic_focus
    mad "[renpy.substitute(dialogues4['E04MADJEL_d040'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d041'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d042'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d043'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d044'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d045'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d046'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d047'])]"
    show ep04_madnan07 at subtle_zoom_out
    mad "[renpy.substitute(dialogues4['E04MADJEL_d048'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d049'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d050'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d051'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d052'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d053'])]"
    mad "[renpy.substitute(dialogues4['E04MADJEL_d054'])]"
    nana "[renpy.substitute(dialogues4['E04MADJEL_d055'])]"
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_isajelously

label ep04_isajelously:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.8)
    $ playAudio(sfx_midnightpast, "amb", 4, True, 1, 0)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
    $ playAudio(sfx_hairdryeron, "sfx", 1, True, 1, 0)
    show ep04_isajel01 at ken_burns_left_to_right with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d001'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d002'])]"
    if ep03_amberleft or ep03_amberstrike:
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d003'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d004'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d005'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d006'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d007'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d008'])]"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=2)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_hairdryeroff, "sfx", 2, False, 0, 0)
    show ep04_isajel02 with normalfade
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d009'])]"
    if sawpic_ep03_sms1:
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d010'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d011'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d012'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d013'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d014'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d015'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d016'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d018'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d020'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d021'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d022'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d023'])]"
    $ show_walkthrough("ep04_isa_m1")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d024'])]"
        "Tell her the truth":
            hide screen walkthrough_screen
            $ ep04_isatruth = True
            $ rm.update("isabella", "trust", 5)
            $ check_levels("isabella", "trust", 5)
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d025'])]"
        "Try to investigate":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", -2)
            $ check_levels("isabella", "trust", -2)
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d026'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(isabella_anger_theme, "music", 2, True, 0, 0)
    show ep04_isajel03 at dramatic_realization
    if ep04_isatruth:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d027'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d028'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d029'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d030'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d031'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d032'])]"
    else:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d033'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d034'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d035'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d036'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d037'])]"
    show ep04_isajel04 at dramatic_focus
    if ep04_isatruth:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d038'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d039'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d040'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d041'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d042'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d043'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d044'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d045'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d046'])]"
    else:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d047'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d048'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d049'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d050'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d051'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d052'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d053'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d054'])]"
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_walk_barefoot, "sfx", 4, False, 0, 0)
    show ep04_isajel05 with normalfade
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d055'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d056'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d057'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d058'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d059'])]"
    $ stopAudio(channel="sfx", subchannel=4, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.4)
    $ playAudio(sfx_chair_rolling, "sfx", 5, False, 0, 0)
    show ep04_isajel06 with normalfade
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.7)
    $ playAudio(sfx_officechair_creak, "sfx", 6, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d060'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d061'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d062'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d063'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d064'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d065'])]"
    $ show_walkthrough("ep04_isa_m2")
    menu:
        "Help her":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", 2)
            $ check_levels("isabella", "trust", 2)
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d066'])]"
        "Leave her alone":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", -2)
            $ check_levels("isabella", "trust", -2)
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d067'])]"
    show ep04_isajel07 at impact_shake
    if ep04_nanadad:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d068'])]"
    else:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d069'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d070'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d071'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d072'])]"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_officechair_sit, "sfx", 7, False, 0, 0)
    show ep04_isajel08 at ken_burns_top_to_bottom with vpunch
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d073'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d074'])]"
    if not sawpic_ep03_sms1:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d075'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d076'])]"
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d077'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d078'])]"
    else:
        if ep04_nanadad:
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d079'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d080'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d081'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d082'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d083'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d084'])]"
        else:
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d085'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d086'])]"
            if ep04_nanpath == 1:
                isa "[renpy.substitute(dialogues4['E04ISAJEL_d087'])]"
            elif ep04_nanpath == 2:
                isa "[renpy.substitute(dialogues4['E04ISAJEL_d088'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d089'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d090'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d091'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.4)
    $ playAudio(sfx_chair_rolling, "sfx", 5, False, 0, 0)
    show ep04_isajel09 with hpunch
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d092'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d093'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d094'])]"
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with slowfade
    pause 1
    $ setChannelVolume(channel="music", subchannel=5, volume=0.2)
    $ playAudio(isabella_happy, "music", 5, True, 0, 0)
    show ep04_isajel10 at impact_shake
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d095'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d096'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d097'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d098'])]"
    $ setChannelVolume(channel="sfx", subchannel=9, volume=0.8)
    $ playAudio(sfx_licklolli, "sfx", 9, False, 0, 0)
    show ep04_isajel11 at slow_reveal
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d099'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d100'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d101'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d102'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d103'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d104'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d105'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_bed_creaking, "sfx", 1, False, 0, 0)
    $ stopAudio(channel="music", subchannel=5, fadeout=2)
    show ep04_isajel12 at ken_burns_right_to_left with normalfade
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d106'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d107'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d108'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)
    show ep04_isajel13 with vpunch
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d109'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.4)
    $ playAudio(isabella_serious, "music", 1, True, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d110'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d111'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d112'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d113'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d114'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d115'])]"
    if ep03_madtalk or ep03_madcaught:
        isa "[renpy.substitute(dialogues4['E04ISAJEL_d116'])]"
    else:
        pass
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d117'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d118'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d119'])]"
    show ep04_isajel14
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d120'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d121'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d122'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d123'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d124'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d125'])]"
    show ep04_isajel16
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d126'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d127'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d128'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d129'])]"
    $ stopAudio(channel="music", subchannel=1, fadeout=2)
    show ep04_isajel15
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d130'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d131'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d132'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d133'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d134'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d135'])]"
    show ep04_isajel17
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d136'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d137'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d138'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d139'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d138'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d141'])]"
    show ep04_isajel19
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d142'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d143'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d144'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d145'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d146'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d147'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(isabella_theme, "music", 2, True, 0, 0)
    show ep04_isajel18
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d148'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d149'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d150'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d151'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d152'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d153'])]"
    show ep04_isajel20
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d154'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d155'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d156'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d157'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d158'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d159'])]"
    show ep04_isajel21
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d160'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d161'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d162'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d163'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    show ep04_isajel22 at ken_burns_left_to_right with vpunch
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d164'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d165'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d166'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d167'])]"
    show ep04_isajel23 at ken_burns_right_to_left
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d168'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d169'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d170'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d171'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d165'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d173'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d174'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    show ep04_isajel24 with vpunch
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d175'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d176'])]"
    show ep04_isajel25
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d177'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d178'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d179'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d180'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d181'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d182'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d183'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d184'])]"
    isa "[renpy.substitute(dialogues4['E04ISAJEL_d185'])]"
    $ show_walkthrough("ep04_isa_m3")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d186'])]"
        "Give her your cheeks":
            hide screen walkthrough_screen
            $ setChannelVolume(channel="sfx", subchannel=3, volume=1)
            $ playAudio(sfx_kiss_one, "sfx", 3, False, 0, 0)
            $ stopAudio(channel="music", subchannel=2, fadeout=2)
            show ep04_isajel26 at subtle_breathing with hpunch
            $ rm.update("isabella", "trust", 2)
            $ check_levels("isabella", "trust", 2)
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d187'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d188'])]"
            $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
            $ playAudio(isabella_happy, "music", 3, True, 0, 0)
            show ep04_isajel27 at ken_burns_bottom_to_top with vpunch
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d189'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d190'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d191'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d192'])]"
            show ep04_isajel28 with hpunch
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d193'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d194'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d195'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d196'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d197'])]"
            show ep04_isajel29 with normalfade
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d198'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d199'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d200'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d201'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d202'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d203'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d204'])]"
        "Give her your lips":
            hide screen walkthrough_screen
            $ ep04_isabellakiss = True
            $ setChannelVolume(channel="sfx", subchannel=4, volume=0.81)
            $ playAudio(sfx_kiss_op_isa, "sfx", 4, False, 0, 0)
            $ stopAudio(channel="music", subchannel=2, fadeout=2)
            show ep04_isajel26 at subtle_breathing with hpunch
            $ rm.update("isabella", "trust", 5)
            $ check_levels("isabella", "trust", 5)
            $ rm.update("isabella", "cor", 5)
            $ check_levels("isabella", "cor", 5)
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d205'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d206'])]"
            show ep04_isajel30 at subtle_breathing, impact_shake
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d207'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d208'])]"
            $ stopAudio(channel="sfx", subchannel=4, fadeout=1)
            $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
            $ playAudio(isabella_happy, "music", 3, True, 0, 0)
            show ep04_isajel31 at ken_burns_bottom_to_top
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d209'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d210'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d211'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d212'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d213'])]"
            show ep04_isajel32 at impact_shake
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d214'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d215'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d216'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d041'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d218'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d219'])]"
            show ep04_isajel33 at ken_burns_left_to_right with normalfade
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d220'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d221'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d222'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d223'])]"
            show ep04_isajel34 at ken_burns_top_to_bottom with vpunch
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d224'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d225'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d226'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d227'])]"
            show ep04_isajel29
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d228'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAJEL_d203'])]"
            isa "[renpy.substitute(dialogues4['E04ISAJEL_d230'])]"
    if ep03_isahug:
        $ ep04_ach_isabella = True
    else:
        pass
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with slowfade
    show ep03_antoback01 with circlewipe
    if ep04_isabellakiss:
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d231'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d232'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d233'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d234'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d235'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d236'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d237'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d238'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAJEL_d239'])]"
    nvl clear
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.1, fade_duration=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)      
    jump ep04_paz_sms

label ep04_pazosaka:
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_quietnite, "amb", 1, True, 1, 0)
    show ep04_mcapartment at ken_burns_bottom_to_top with ccirclewipe
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_door_open2, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.7)
    $ playAudio(sfx_extnight, "amb", 2, True, 1, 0)   
    show ep04_paztask01 at ken_burns_left_to_right
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d001'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d002'])]"
    #NOTIFICATION SAVE
    $ update_htl_episodes()
    if htl_episodes == 4.1:
        $ show_custom_notification("save_tip")
    else:
        pass
    show ep04_paztask02
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d003'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d004'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d005'])]"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)    
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    show ep04_paztask03 at ken_burns_bottom_to_top
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d006'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d007'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d008'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(redkitsune_theme, "music", 1, True, 4, 0)
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d009'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d010'])]"
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.6)
    $ playAudio(sfx_lamp_turnon, "sfx", 3, False, 0, 1)
    pause 1.0
    show ep04_paztask04 with normalfade
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_flaslight_turnon, "sfx", 4, False, 0, 0)
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d011'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d012'])]"
    show ep04_paztask05 at ken_burns_corner_to_corner
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d013'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d014'])]"
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_door_open_creak, "sfx", 4, False, 0, 0)
    show ep04_paztask06 with normalfade
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d015'])]"
    show ep04_paztask07 at subtle_zoom_out
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d016'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d017'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d018'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d019'])]"
    show ep04_paztask08 at ken_burns_top_to_bottom
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d020'])]"
    pa_t "[renpy.substitute(dialogues4['E04OSAPAZ_d021'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d022'])]"
    $ setChannelVolume(channel="sfx", subchannel=5, volume=1)
    $ playAudio(sfx_katana_warn, "sfx", 5, False, 0, 0)
    show ep04_paztask09 with hpunch
    pa_s "[renpy.substitute(dialogues4['E04OSAPAZ_d023'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d024'])]"
    pa_s "[renpy.substitute(dialogues4['E04OSAPAZ_d025'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d026'])]"
    show ep04_paztask10
    pa_s "[renpy.substitute(dialogues4['E04OSAPAZ_d027'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d028'])]"
    pa_s "[renpy.substitute(dialogues4['E04OSAPAZ_d029'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d030'])]"
    pa_s "[renpy.substitute(dialogues4['E04OSAPAZ_d031'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d032'])]"
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.7)
    $ playAudio(sfx_katana_sheath_hit, "sfx", 6, False, 0, 0)
    show ep04_paztask11 at action_sequence, subtle_zoom_out with flash
    pa_s "[renpy.substitute(dialogues4['E04OSAPAZ_d033'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d034'])]"
    show ep04_paztask12 with normalfade
    $ setChannelVolume(channel="sfx", subchannel=7, volume=1)
    $ playAudio(sfx_breathmouth_sleep_f, "sfx", 7, False, 0, 0)
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d035'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d036'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d037'])]"
    show ep04_paztask13 at emotional_flashback with slowfade
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d040'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d038'])]"
    "Masked Woman" "[renpy.substitute(dialogues4['E04OSAPAZ_d039'])]"
#-- Hide and Turn off stuff
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
#-- End Update
    if htl_episodes == 4.1:
        pause 2
        scene eigengrau
        call hideNoise(transition=dissolve)
        return
    else:
        jump ep04_mcnananight
    # else:
    #     scene eigengrau with rose
    #     pause 2
    #     $ resetAllVolumes()
    #     jump ep05_title

label ep04_mcnananight:
##episode 3 bug fix (delete on final version)
    if rm.get("elizabeth", "cor") > 2:
        $ rm.update("amber", "cor", 2)
        $ show_custom_notification("bugfix")
    else:
        pass
    if rm.get("elizabeth", "trust") > 2:
        $ rm.update("amber", "trust", 2)
        $ show_custom_notification("bugfix")
    else:
        pass
#####
#opening scene
    call hideNoise(transition=dissolve)
    scene eigengrau with clouds_inverse
    
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)
    show ep04_mcroom01 at ken_burns_bottom_to_top with slowfade
    show home_location zorder 2 with dissolve
    pause 4
    hide home_location with dissolve
    show ep04_mcroom02  at slow_reveal with slowfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANINTRO_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANINTRO_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANINTRO_d003'])]"
    show ep04_mcroom03
    mc_t "[renpy.substitute(dialogues4['E04MCNANINTRO_d004'])]"
    if rm.get('nanami', 'trust') > 23:
        $ ep04_nanaskimpy = True
    else:
        $ ep04_nanaskimpy = False
    $ stopAudio("amb", 2, 1)
    jump ep04_nanameet


label ep04_nanameet:
    
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.6)
    $ playAudio(sfx_dooropen, "sfx", 1, False, 0, 0)
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.3)
    $ playAudio(sfx_fridge_hum, "sfx", 2, True, 1, 0)
    show ep04_nanakitchen01 at ken_burns_right_to_left
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d001'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d002'])]"
    show ep04_nanakitchen02 at subtle_zoom_in with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d003'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d004'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d005'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d006'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d008'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d010'])]"
    $ playAudio(nanami_theme, "music", 1, True, 2.0, 1.0)
    show ep04_nanakitchen03 with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d011'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d012'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d014'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_fridge_closedoor, "sfx", 1, False, 0, 0)
    $ stopAudio("sfx", 2, 1)
    show ep04_nanakitchen04 with hpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d015'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d017'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d018'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d019'])]"
    show ep04_nanakitchen05 at subtle_zoom_out with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d020'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d021'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d022'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d024'])]"
    show ep04_nanakitchen06
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d026'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d028'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d030'])]"
    show ep04_nanakitchen07
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d031'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d032'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d033'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d034'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d035'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d036'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d037'])]"
    show ep04_nanakitchen08 at dramatic_realization
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d038'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d039'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d040'])]"
    show ep04_nanakitchen10
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d041'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d042'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d043'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d044'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d045'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d046'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d047'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d048'])]"
    show ep04_nanakitchen09
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d049'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d050'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d051'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d052'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d053'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d055'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d056'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d057'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d058'])]"
    $ stopAudio("music", 1, 2)
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    pause 0.5
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0) 
    show ep04_nanakitchen11 with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d059'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d060'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d061'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d062'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d063'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d064'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d066'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d067'])]"
    show ep04_nanakitchen12 at subtle_zoom_out with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d068'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d069'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d070'])]"
    show ep04_nanakitask01 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d071'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d072'])]"
    if ep04_nanaskimpy:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d073'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d074'])]"
    else:
        pass
    show ep04_nanakitask02
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d075'])]"
    if ep04_nanaskimpy:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d076'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d077'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d078'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d079'])]"
    if ep04_nanaskimpy:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d080'])]"
    else:
        pass
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d081'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d082'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d083'])]"
    $ setAllSubchannelsVolume("amb", 0, 1.0) 
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1
    $ setAllSubchannelsVolume("amb", 0.3, 1.0) 
    show ep04_nanakitask05 with circlewipe
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d084'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d085'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d086'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d087'])]"
    show ep04_nanakitask06 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d088'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d089'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d090'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d091'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d092'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d093'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMEET_d094'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d095'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d096'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d097'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMEET_d098'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d099'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d100'])]"
    $ show_walkthrough("ep04_nanameetmenu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d101'])]"
        "Let her try the beer":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d102'])]"
            mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d103'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANMEET_d104'])]"
            $ rm.update("nanami", "cor", 2)
            $ check_levels("nanami", "cor", 2)
            jump ep04_nanabooze #to beer scene (condition have points on corruption)
        "Keep it innocent":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d105'])]"
            scene eigengrau with slowfade
            show ep04_nanakitask03
            nana "[renpy.substitute(dialogues4['E04MCNANMEET_d106'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANMEET_d107'])]"
            mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d108'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANMEET_d109'])]"
            show ep04_nanakitask04
            $ rm.update("nanami", "trust", 6)
            $ check_levels("nanami", "trust", 6)
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANMEET_d110'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANMEET_d111'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d037'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANMEET_d113'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANMEET_d114'])]"
            mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d115'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANMEET_d116'])]"
            mc_s "[renpy.substitute(dialogues4['E04MCNANMEET_d117'])]"
            $ ep04_mcmilk = True
            jump ep04_nanamilk


label ep04_nanamilk:
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_chair_lather_sit, "sfx", 1, False, 0, 0)
    pause 1
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)
    show ep04_nanakitmilk01 at ken_burns_right_to_left with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d001'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d005'])]"
    $ setChannelVolume("amb", 1, 0, 1.5)
    pause 0.5
    scene eigengrau with smoke
    $ playAudio(antonella_love, "music", 1, True, 2.0, 1.0)
    show ep01_postgame07 at ken_burns_left_to_right with smoke
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d006'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d009'])]"
    show ep01_postgame09 with smoke
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d012'])]"
    show ep01_postgame08 at ken_burns_right_to_left with smoke
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_kiss_one, "sfx", 1, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d015'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d017'])]"
    $ stopAudio("music", 1, 2)
    pause 0.5
    scene eigengrau with smoke
    $ setChannelVolume("amb", 1, 0.3, 1.5)
    show ep04_nanakitmilk02 with smoke
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d019'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d020'])]"
    show ep04_nanakitmilk03 at dramatic_focus
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d021'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d022'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d023'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d026'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d027'])]"
    $ playAudio(nanami_chill_theme, "music", 2, True, 2.0, 1.0)
    show ep04_nanakitmilk04 with vpunch
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d029'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d030'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d028'])]"
    show ep04_nanakitmilk05 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d032'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d033'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d035'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d036'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_glass_ontable, "sfx", 1, False, 0, 0)
    show ep04_nanakitmilk06 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d037'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d038'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d039'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d040'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d041'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d042'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d043'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d044'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d045'])]"
    show ep04_nanakitmilk07 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d046'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d047'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d049'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d050'])]"
    show ep04_nanakitmilk08
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d051'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d052'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d053'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d055'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d056'])]"
    show ep04_nanakitmilk09 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d057'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d059'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d060'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d061'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d062'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d063'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d064'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d066'])]"
    show ep04_nanakitmilk10 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d067'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d068'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d069'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d070'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d071'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanakitmilk11 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d072'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d073'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d074'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d075'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d076'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d077'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d078'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d079'])]"
    show ep04_nanakitmilk12 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d080'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d081'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d082'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d083'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d084'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d085'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d086'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d087'])]"
    show ep04_nanakitmilk13
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d088'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d089'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d090'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d091'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d092'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d093'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMILK_d094'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMILK_d095'])]"
    $ show_walkthrough("ep04_nanamilkmenu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANMILK_d096'])]"
        "Make her stay":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d097'])]"
            ##already giving 2 points on love @ label
            jump ep04_nana_askkiss
        "Send her to bed":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANMILK_d098'])]"
            jump ep04_nananostay


label ep04_nananostay:
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(nanami_secure_theme, "music", 1, True, 2, 0)
    show ep04_nanakitmorekiss00
    $ rm.update("nanami", "trust", 1)
    $ check_levels("nanami", "trust", 1)
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d002'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d004'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d006'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d007'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d009'])]"
    show ep04_nanakitmorekiss05
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNO_d010'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNO_d011'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d014'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d015'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d016'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d018'])]"
    show ep04_nanakitmorekiss06 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNO_d019'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNO_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d021'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d022'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d023'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNO_d024'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d025'])]"
    show ep04_nanakitkiss07 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNO_d026'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNO_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNO_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d029'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d030'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d031'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNO_d032'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom


label ep04_nana_askkiss:
    show ep04_nanakitkiss01
    $ rm.update("nanami", "trust", 3)
    $ check_levels("nanami", "trust", 3)
    nana "[renpy.substitute(dialogues4['E04MCNANASK_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d002'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANASK_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d005'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANASK_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d007'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANASK_d008'])]"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(nanami_love_theme, "music", 1, True, 2, 0)
    show ep04_nanakitkiss02 at slow_reveal with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANASK_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d010'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANASK_d011'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANASK_d012'])]"
    if ep04_nanakiss:
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d013'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d014'])]"
    show ep04_nanakitkiss03 at subtle_zoom_out with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANASK_d015'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANASK_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d017'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d018'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d019'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d020'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d021'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d022'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d023'])]"
    $ show_walkthrough("ep04_nanaaskismenu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANASK_d024'])]"
        "Kiss her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d025'])]"
            if not ep04_nanakiss:
                $ ep04_nanakiss = True
            else:
                pass
            # +2 cor @ end of label
            jump ep04_nanakiss
        "Reject her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANASK_d026'])]"
            # no points @ end of label
            jump ep04_nananokiss


label ep04_nananokiss:
    $ ep04_refusednanakiss = True
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanakitmorekiss05
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d001'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNOK_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNOK_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d005'])]"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.3)
    $ playAudio(nanami_innocence_theme, "music", 2, True, 2, 0)
    show ep04_nanakitmorekiss00
    nana "[renpy.substitute(dialogues4['E04MCNANNOK_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d008'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNOK_d009'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNOK_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d011'])]"
    show ep04_nanakitkiss07 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANNOK_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNOK_d013'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNOK_d014'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNOK_d015'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNOK_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNOK_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNOK_d018'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNOK_d019'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom


label ep04_nanakiss:
    show ep04_nanakitkiss04
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_kiss_nana, "sfx", 1, False, 0, 0)
    mc_t "[renpy.substitute(dialogues4['E04MCNANKIS_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANKIS_d002'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANKIS_d003'])]"
    show ep04_nanakitkiss05
    nana "[renpy.substitute(dialogues4['E04MCNANKIS_d004'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANKIS_d005'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d006'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d007'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANKIS_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANKIS_d009'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANKIS_d010'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANKIS_d011'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANKIS_d012'])]"
    if ep04_madpath == 1:
        show ep04_nanakitkiss06 with normalfade
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d013'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANKIS_d014'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANKIS_d015'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANKIS_d016'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANKIS_d017'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d018'])]"
        jump ep04_nana2ndkiss
    else:
        show ep04_nanakitkiss06 with normalfade
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d019'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d020'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANKIS_d021'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANKIS_d022'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANKIS_d023'])]"
        show ep04_nanakitkiss07 with normalfade
        nana "[renpy.substitute(dialogues4['E04MCNANKIS_d024'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANKIS_d025'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANKIS_d026'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANKIS_d027'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANKIS_d028'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANKIS_d029'])]"
        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("music", 2.0)
        jump ep04_isabella_mcroom


label ep04_nana2ndkiss:
    menu:
        "Kiss her again":
            pass
    show ep04_nanakitmorekiss01 with vpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_kiss_op_isa, "sfx", 2, False, 0, 0)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d001'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d005'])]"
    show ep04_nanakitmorekiss02
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d006'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d008'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d009'])]"
    show ep04_nanakitmorekiss03
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d010'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d011'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d012'])]"
    show ep04_nanakitmorekiss04
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d014'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d004'])]"
    $ stopAllSubchannels("sfx", 1.0)
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanakitmorekiss05 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d016'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d018'])]"
    show ep04_nanakitmorekiss06 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d019'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d022'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d023'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d024'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d026'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d027'])]"
    show ep04_nanakitmorekiss07
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d029'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d030'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d032'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d033'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d034'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d035'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d036'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d037'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanakitmorekiss08 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d038'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d039'])]"
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d040'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d041'])]"
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d042'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d043'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d044'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d045'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d046'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d047'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d048'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d049'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d050'])]"
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_surprisenana, "sfx", 1, False, 0, 0)
    show ep04_nanakitmorekiss09 with vpunch
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d051'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d052'])]"
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d053'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d054'])]"
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d055'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_bodydrop_ontable, "sfx", 2, False, 0, 0)
    pause 0.2
    show ep04_nanakitmorekiss10 with vpunch
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d057'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d058'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d059'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d060'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d061'])]"
    $ playAudio(mc_nanami_theme, "music", 3, True, 2.0, 1.0)
    show ep04_nanakitmorekiss11
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d062'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d063'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d064'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d066'])]"
    show ep04_nanakitmorekiss12
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d067'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d068'])]"
    show ep04_nana_spread01 with hpunch
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d069'])]"
    show ep04_nana_spread02
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d070'])]"
    show ep04_nana_spread03
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d071'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d072'])]"
    show ep04_nana_spread04
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d073'])]"
        show ep04_nana_spread05
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d074'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d075'])]"
        show ep04_nana_spread06
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d076'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d077'])]"
        show ep04_nana_spread05
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d078'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d079'])]"
        show ep04_nana_spread06
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d080'])]"
    show ep04_nana_spread07
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d081'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d082'])]"
    show ep04_nana_spread08
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d083'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d084'])]"
        show ep04_nana_spread09
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d085'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d086'])]"
        show ep04_nana_spread09
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d087'])]"
    show ep04_nana_spread10
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d088'])]"
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    $ stopAllSubchannels("music", 2.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)
    show ep04_nanakitmorekiss13
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d089'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d090'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d091'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d092'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d093'])]"
    show ep04_nanakitmorekiss14
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d094'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d095'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d096'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d097'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d098'])]"
    $ playAudio(nanami_love_theme, "music", 1, True, 2.0, 1.0)
    show ep04_nanakitmorekiss15
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d099'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d100'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d101'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d102'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 3, False, 0, 0)
    show ep04_nanakitmorekiss16 with vpunch
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d103'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d104'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d105'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d106'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d107'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d108'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d109'])]"
    show ep04_nanakitkiss07 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d110'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d111'])]"
    nana "[renpy.substitute(dialogues4['E04MCNAN2KIS_d112'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNAN2KIS_d113'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d114'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNAN2KIS_d115'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom



label ep04_nanabooze:
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_chair_lather_sit, "sfx", 1, False, 0, 0)
    pause 1
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)
    show ep04_nanakitdrunk01 at ken_burns_left_to_right with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d001'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d003'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d005'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d006'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d008'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d009'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d011'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d012'])]"
    $ setChannelVolume("amb", 1, 0, 1)
    scene eigengrau with smoke
    if not ep01_first:
        $ playAudio(antonella_sad_theme, "music", 1, True, 2.0, 1.0)
        show ep04_anto_memory01 at ken_burns_right_to_left with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d013'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d014'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d015'])]"
        hide ep04_nanakitdrunk01
        show ep04_anto_memory02 at subtle_zoom_in with smoke
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d016'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d017'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d018'])]"
        $ setChannelVolume("amb", 1, 0, 1.5)
        scene eigengrau with smoke
        show ep04_nanakitdrunk01 with smoke
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d019'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d020'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d021'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d022'])]"
        $ setChannelVolume("amb", 1, 0, 1)
        scene eigengrau with smoke
        show ep01_game49 at subtle_zoom_out with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d023'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d024'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d025'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d026'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d027'])]"
        show ep01_pregame08 at ken_burns_left_to_right
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d028'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d029'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d030'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d031'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d032'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d033'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d034'])]"
        show ep04_anto_memory03
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d035'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d036'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d037'])]"
        show ep04_anto_memory04 at ken_burns_top_to_bottom
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d038'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d039'])]"
        show ep04_anto_memory05
        hide ep04_nanakitdrunk01
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d040'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d041'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d042'])]"
        show ep04_anto_memory06 at ken_burns_right_to_left
        mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d043'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d044'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d045'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d046'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d047'])]"
    else:
        $ playAudio(amber_sad_theme, "music", 1, True, 2.0, 1.0)
        show ep01_amberconfess24 at ken_burns_right_to_left with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d048'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d049'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d050'])]"
        show ep01_amberconfess33 with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d051'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d052'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d053'])]"
        show ep01_amberconfess34 at ken_burns_bottom_to_top with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d054'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d055'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d056'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d057'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d058'])]"
        show ep01_home12 with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d059'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d060'])]"
        show ep04_amber_remember01 at subtle_zoom_out with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d061'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d062'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d063'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d064'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d065'])]"
        show ep01_amberconfess06 with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d066'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d067'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d068'])]"
        hide ep04_nanakitdrunk01
        show ep01_amberconfess38 at ken_burns_top_to_bottom with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d069'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d070'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d071'])]"
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d072'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d073'])]"
        show ep04_amber_remember02 at ken_burns_left_to_right with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d074'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d075'])]"
        show ep04_amber_remember03 at subtle_zoom_in with smoke
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d076'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d077'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d078'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d079'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with smoke
    $ setChannelVolume("amb", 1, 0.3, 1.5)
    show ep04_nanakitdrunk01 with smoke
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d080'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d081'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d082'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d083'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d084'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d085'])]"
    $ playAudio(nanami_chill_theme, "music", 2, True, 2.0, 1.0)
    show ep04_nanakitdrunk02 with vpunch
    if ep04_nanaskimpy:
        mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d086'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d087'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d088'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d089'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d090'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d091'])]"
    show ep04_nanakitdrunk03 with vpunch
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d092'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d093'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d094'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d095'])]"
    show ep04_nanakitdrunk04 with vpunch
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d096'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d097'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d098'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d099'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d100'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d101'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d102'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d103'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d104'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d105'])]"
    show ep04_nanakitdrunk05
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d106'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d107'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d108'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d109'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d110'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d111'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d112'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d113'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d114'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d115'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d116'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d117'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d118'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d119'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d120'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d121'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d122'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d123'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d124'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d125'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d126'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d127'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d128'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d129'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANBOZ_d130'])]"
    $ show_walkthrough("ep04_nanaboozmenu")
    menu:
        "Give her more beer":
            hide screen walkthrough_screen
            if ep04_nanadad:
                mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d131'])]"
                show ep04_nanakitdrunk06 with normalfade
                $ rm.update("nanami", "cor", 1)
                $ check_levels("nanami", "cor", 1)
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d132'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d133'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d134'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d135'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d136'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d137'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d138'])]"
            else:
                mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d139'])]"
                show ep04_nanakitdrunk06 with normalfade
                $ rm.update("nanami", "cor", 1)
                $ check_levels("nanami", "cor", 1)
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d140'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d141'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d142'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d143'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d144'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d145'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANBOZ_d146'])]"
            #only way to see isabella mast
            $ setAllSubchannelsVolume("amb", 0, 1.0)
            jump ep04_nanamorebooze
        "Better stop now":
            hide screen walkthrough_screen
            #only way to dream heaven and hell
            $ ep04_mcdrunk = True
            mc_s "[renpy.substitute(dialogues4['E04MCNANBOZ_d147'])]"
            if not ep04_nanakiss:
                $ ep04_nanakiss = True
            else:
                pass
            jump ep04_nana_nobooze


label ep04_nana_nobooze:
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanakitmilk13 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d001'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d002'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d003'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d004'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d005'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d006'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d007'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d008'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d009'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d010'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d011'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d015'])]"
    show ep04_nanakitkiss01
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d016'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d019'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d020'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d021'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d022'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d024'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d025'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d026'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d027'])]"
    $ playAudio(nanami_love_theme, "music", 3, True, 2.0, 1.0)
    show ep04_nanakitkiss02 at slow_reveal with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d028'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d029'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d030'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d031'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d032'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d033'])]"
    show ep04_nanakitkiss03 at subtle_zoom_out with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d034'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d036'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d037'])]"
    menu:
        "Kiss her":
            pass
    show ep04_nanakitkiss04
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_kiss_nana, "sfx", 1, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d038'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d039'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d040'])]"
    show ep04_nanakitkiss05
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d041'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d042'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d043'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d044'])]"
    show ep04_nanakitkiss06 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d045'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d046'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d047'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d048'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d049'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d050'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d051'])]"
    menu:
        "Kiss her again":
            pass
    show ep04_nanakitmorekiss01 with vpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_kiss_op_isa, "sfx", 2, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d052'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d053'])]"
    show ep04_nanakitmorekiss04
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d054'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d055'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d056'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNB_d057'])]"
    $ stopAllSubchannels("sfx", 1.0)
    show ep04_nanakitmorekiss08 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d058'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d059'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d060'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d061'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d062'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d063'])]"
    show ep04_nanakitmorekiss06 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d064'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d065'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d066'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d067'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d068'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d069'])]"
    show ep04_nanakitmorekiss07
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d070'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d071'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d072'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d073'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d074'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d075'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNB_d076'])]"
    show ep04_nanakitkiss07 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d077'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNB_d078'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d079'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d080'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNB_d081'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom


label ep04_nanamorebooze:
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)
    show ep04_nanakitdrunk07 with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d001'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d002'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d003'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d004'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d006'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d007'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d009'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d010'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d011'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d012'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d013'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d014'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d015'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d016'])]"
    show ep04_nanakitdrunk08 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANMBO_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d018'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMBO_d019'])]"
    scene eigengrau with slowfade
    show ep04_nanakitdrunk09 with hpunch
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d020'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d021'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d022'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d024'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d025'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d026'])]"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_bodydrop_ontable, "sfx", 3, False, 0, 0)
    show ep04_nanakitdrunk10 with vpunch
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d027'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMBO_d028'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d029'])]"
    show ep04_nanakitdrunk11 with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d030'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d031'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMBO_d032'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d033'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANMBO_d034'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d035'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d036'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d037'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d038'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d039'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d040'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d041'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d042'])]"
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 4, False, 0, 0)
    show ep04_nanakitdrunk12 with vpunch
    nana "[renpy.substitute(dialogues4['E04MCNANMBO_d043'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d044'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d045'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d046'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d047'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d048'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d049'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d050'])]"
    scene eigengrau with slowfade
    show ep04_nanakitdrunk13 at ken_burns_left_to_right
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d051'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d052'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d053'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d054'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANMBO_d055'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d056'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d057'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANMBO_d058'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d059'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANMBO_d060'])]"
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_nanadrunkmcroom



label ep04_nanadrunkmcroom:
    
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)
    show ep04_nanamcroom01 at ken_burns_top_to_bottom with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d001'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d003'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d005'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d006'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d007'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d008'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d011'])]"
    $ setChannelVolume("sfx", 1, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom02 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d012'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d013'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d014'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d015'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d016'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d017'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d018'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d020'])]"
    show ep04_nanamcroom03
    nana "[renpy.substitute(dialogues4['E04MCNANDMR_d021'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d022'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANDMR_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d024'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d025'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d026'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d027'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDMR_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d030'])]"
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)
    show ep04_nanamcroom04 at ken_burns_corner_to_corner with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d031'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d032'])]"
    show ep04_nanamcroom05 at subtle_zoom_in
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d033'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d034'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d035'])]"
    $ show_walkthrough("ep04_nanadrumcmenu")
    menu:
        "Wake her up":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d036'])]"
            if ep04_nanadad:
                mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d037'])]"
            else:
                mc_s "[renpy.substitute(dialogues4['E04MCNANDMR_d038'])]"
            jump ep04_nanadrunkawake
        "Let her sleep":
            hide screen walkthrough_screen
            $ ep04_nanastay = True
            mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d039'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d040'])]"
            if ep04_nanadad:
                mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d041'])]"
            else:
                mc_t "[renpy.substitute(dialogues4['E04MCNANDMR_d042'])]"
            $ stopAllSubchannels("amb", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 1, 1, 0)
            $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
            pause 0.5
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1.0
            jump ep04_elimeet_intro



label ep04_nanadrunkawake:
    show ep04_nanamcroom06 with hpunch
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_surprisenana, "sfx", 1, False, 0, 0)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d001'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d003'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d004'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d005'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d007'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d009'])]"
    $ playAudio(nanami_secure_theme, "music", 1, True, 2.0, 1.0)
    show ep04_nanamcroom07
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d010'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d011'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d013'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d015'])]"
    show ep04_nanamcroom08
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d016'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d017'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d018'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d019'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d020'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d022'])]"
    show ep04_nanamcroom09 with vpunch
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d023'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d024'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d026'])]"
    show ep04_nanamcroom10 with hpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d027'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d028'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d029'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d030'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d031'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d032'])]"
    show ep04_nanamcroom11
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d033'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d034'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d035'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d036'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d037'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d038'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d039'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d040'])]"
    $ show_walkthrough("ep04_nanadrumcmenu_2")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d041'])]"
        "Give her a peck":
            hide screen walkthrough_screen
            show ep04_nanamcroom12 at subtle_zoom_in with hpunch
            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
            $ playAudio(sfx_kiss_nana, "sfx", 1, False, 0, 0)
            if ep04_nanadad:
                mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d042'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d043'])]"
            else:
                mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d044'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d045'])]"
        "French kiss her":
            hide screen walkthrough_screen
            show ep04_nanamcroom12 at subtle_zoom_in with hpunch
            $ rm.update("nanami", "trust", 6)
            $ check_levels("nanami", "trust", 6)
            $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
            $ playAudio(sfx_kiss_op_isa, "sfx", 2, False, 0, 0)
            mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d046'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d047'])]"
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d048'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d049'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d050'])]"
            show ep04_nanamcroom13 at subtle_zoom_out
            nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d051'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d052'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d053'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d054'])]"
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d055'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d056'])]"
            $ stopAllSubchannels("sfx", 1.0)
    show ep04_nanamcroom14 with hpunch
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d057'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d058'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d059'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d060'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d061'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d062'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d063'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d064'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d065'])]"
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom15
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d066'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d067'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d068'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d069'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d070'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d071'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d072'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d073'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d074'])]"
    show ep04_nanamcroom16 at subtle_zoom_out with normalfade
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_shortmakeout, "sfx", 2, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d075'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d076'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d077'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d078'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d079'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d080'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d081'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d082'])]"
    $ stopAllSubchannels("sfx", 1.0)
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom17 at ken_burns_top_to_bottom with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d075'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d084'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d085'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d086'])]"
    show ep04_nanamcroom18 with normalfade
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_shortmakeout, "sfx", 2, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d075'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d088'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d089'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d090'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d091'])]"
    $ stopAllSubchannels("sfx", 1.0)
    $ show_walkthrough("ep04_nanadruawaksmenu")
    menu:
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d092'])]"
        "Suck her tits":
            hide screen walkthrough_screen
            show ep04_nanamcroom19 at ken_burns_left_to_right
            $ ep04_nanakiss_breasts = True
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d093'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d094'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d095'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d096'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d097'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d094'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d099'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d100'])]"
            nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d101'])]"
        "Go down on her":
            hide screen walkthrough_screen
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d102'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d103'])]"
    show ep04_nanamcroom20 at ken_burns_bottom_to_top with normalfade
    if ep04_nanakiss_breasts:
        if ep04_nanadad:
            nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d104'])]"
        else:
            nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d105'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d106'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d107'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d108'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d109'])]"
    show ep04_nana_pussy_play01
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d110'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d111'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d112'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANDAAW_d113'])]"
    show ep04_nana_pussy_play02
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d114'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d115'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d116'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d117'])]"
    show ep04_nana_pussy_play03
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d118'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d119'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d120'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d121'])]"
    show ep04_nana_pussy_play04
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d122'])]"
    show ep04_nana_pussy_play05
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d123'])]"
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
    show ep04_nanamcroom22 at subtle_zoom_out with vpunch
    $ setChannelVolume("sfx", 4, 0.7, 0)
    $ playAudio(sfx_surprisenana, "sfx", 4, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d124'])]"
    $ stopAllSubchannels("music", 2.0)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d125'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d126'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d127'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d128'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d129'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d130'])]"
    show ep04_nanamcroom23 at ken_burns_top_to_bottom
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d131'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d132'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d133'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d134'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d135'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d136'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d137'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d138'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d139'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d140'])]"
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
    show ep04_nanamcroom24 at ken_burns_bottom_to_top with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d141'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d142'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d143'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d144'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d145'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d146'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d147'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d148'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d149'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d150'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d151'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d152'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d153'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d154'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d155'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d156'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d157'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d158'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d159'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d160'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d161'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d162'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d163'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d164'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d165'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d166'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d167'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d168'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANDAAW_d169'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d170'])]"
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(nanami_chill_theme, "music", 1, True, 4, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d171'])]"
    $ show_walkthrough("ep04_nanagamesmenu")
    menu nanami_choice_menu:
        "Her neck" if not ep04_neck_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 2:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed
            else:
                $ ep04_neck_completed = True
                show ep04_nanamcroom26 at ken_burns_top_to_bottom with normalfade
                if ep04_nanadad:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d172'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d173'])]"
                else:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d174'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d175'])]"
                jump ep04_nanami_next_choice
        "Her shoulders" if not ep04_shoulders_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 3:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed
            else:
                $ ep04_shoulders_completed = True
                show ep04_nanamcroom28 at ken_burns_left_to_right with normalfade
                if ep04_nanadad:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d176'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d177'])]"
                else:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d178'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d179'])]"
                jump ep04_nanami_next_choice
        "Her mouth" if not ep04_mouth_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 1:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed
            else:
                $ ep04_mouth_completed = True
                show ep04_nanamcroom25 at subtle_zoom_out with normalfade
                nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d180'])]"
                if ep04_nanadad:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d181'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d182'])]"
                else:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d183'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d184'])]"
                jump ep04_nanami_next_choice
        "Her breasts" if not ep04_breasts_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 4:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed
            else:
                $ ep04_breasts_completed = True
                show ep04_nanamcroom27 at subtle_zoom_in with normalfade
                if ep04_nanadad:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d185'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d186'])]"
                else:
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d187'])]"
                    nana "[renpy.substitute(dialogues4['E04MCNANDAAW_d188'])]"
                jump ep04_nanami_success_path


label ep04_nanami_next_choice:
    if ep04_neck_completed and ep04_shoulders_completed and ep04_mouth_completed and ep04_breasts_completed:
        jump ep04_nanami_success_path
    else:
        jump nanami_choice_menu

label ep04_nanami_success_path:
    hide screen walkthrough_screen
    show ep04_nanamcroom30 with hpunch
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d001'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d002'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d003'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d005'])]"
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom29 at ken_burns_top_to_bottom with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d006'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d007'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d008'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d009'])]"
    show ep04_nanamcroom34 with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d010'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d011'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d012'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d013'])]"
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
    show ep04_nanamcroom35 at ken_burns_bottom_to_top with hpunch
    $ setChannelVolume("sfx", 4, 0.3, 0)
    $ playAudio(sfx_shortmakeout, "sfx", 4, False, 0, 0)
    mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d014'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d015'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d018'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d020'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d021'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d022'])]"
    $ stopAudio("sfx", 4, 1)
    show ep04_nanamcroom36
    $ setChannelVolume("sfx", 5, 0.3, 0)
    $ playAudio(sfx_kiss_op_isa, "sfx", 5, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d023'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d024'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d025'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d026'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d027'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d028'])]"
    $ stopAudio("sfx", 5, 1)
    scene eigengrau with slowfade
    show ep04_nanakissbreast01
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d029'])]"
    show ep04_nanakissbreast02
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d030'])]"
        show ep04_nanakissbreast03
        mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d031'])]"
        show ep04_nanakissbreast04
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d032'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d033'])]"
        show ep04_nanakissbreast03
        mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d034'])]"
        show ep04_nanakissbreast04
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d035'])]"
    show ep04_nanakissbreast05
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d036'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    pause 1
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom37 at ken_burns_left_to_right with vpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d037'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d038'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d039'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANNSP_d040'])]"
    show ep04_nanadrunknude01 at subtle_zoom_out with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d041'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANNSP_d042'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d043'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANNSP_d044'])]"
    $ stopAllSubchannels("music", 2.0)
    $ show_walkthrough("ep04_nanasucpathmenu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANNSP_d045'])]"
        "Try to wake her":
            hide screen walkthrough_screen
            # +2x cor @ end label
            jump ep04_nanalicking
        "Let her rest":
            $ ep04_nanastay = True
            hide screen walkthrough_screen
            # +1x love @ end label
            jump ep04_nanacarrybed


label ep04_nanami_sequence_failed:
    hide screen walkthrough_screen
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanamcroom31 at hpunch
    nana "[renpy.substitute(dialogues4['E04MCNANSQF_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANSQF_d002'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANSQF_d003'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANSQF_d004'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANSQF_d005'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANSQF_d006'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANSQF_d007'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANSQF_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANSQF_d009'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANSQF_d010'])]"
    jump ep04_nanaleave


label ep04_nanacarrybed:
    $ playAudio(nanami_love_theme, "music", 3, True, 2.0, 1.0)
    show ep04_nanasleep02 at ken_burns_right_to_left
    $ rm.update("nanami", "trust", 3)
    $ check_levels("nanami", "trust", 3)
    mc_t "[renpy.substitute(dialogues4['E04MCNANCB_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANCB_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANCB_d003'])]"
    show ep04_nanasleep01 at subtle_zoom_out with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANCB_d004'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANCB_d005'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANCB_d006'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANCB_d007'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANCB_d008'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANCB_d009'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANCB_d010'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANCB_d011'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANCB_d012'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANCB_d013'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANCB_d014'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANCB_d015'])]"
    jump ep04_nana_sleepbed



label ep04_nana_sleepbed:
    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_bedmove2, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom32 at ken_burns_right_to_left with normalfade
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANSLEB_d001'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANSLEB_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d003'])]"
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 0.5
    show ep04_nanamcroom33 at ken_burns_corner_to_corner with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d005'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d006'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d007'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d008'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d009'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANSLEB_d010'])]"
    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    pause 0.5
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_elimeet_intro



label ep04_nanalicking:
    scene eigengrau
    show ep04_nanadrunknude02 with hpunch
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_sigh_nana, "sfx", 1, False, 0, 0)
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d001'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d002'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d003'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d004'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d005'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d006'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d007'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d008'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d009'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d010'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d011'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d013'])]"
    $ playAudio(nanami_chill_theme, "music", 5, True, 2.0, 1.0)
    show ep04_nanadrunkforced01 at subtle_zoom_out with hpunch
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d014'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d015'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d017'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d018'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d019'])]"
    scene eigengrau
    show ep04_nanadrunknude03 at subtle_zoom_in with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d020'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d021'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d022'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d023'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d024'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d025'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d026'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d027'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d028'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d029'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d030'])]"
    show ep04_nanadrunknude_xx with slowfade
    $ setChannelVolume("sfx", 3, 0.2, 0)
    $ playAudio(sfx_madbreathxxx, "sfx", 3, False, 0, 0)
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d031'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d032'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d033'])]"
    show ep04_nanadrunknude_x2 with Dissolve (1)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d034'])]"
    show ep04_nana_pussy_show01 with Dissolve (1)
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d035'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d036'])]"
    show ep04_nana_pussy_show02 with Dissolve (1)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d037'])]"
    show ep04_nana_pussy_show03 with Dissolve (1)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d038'])]"
        show ep04_nana_pussy_show04 with Dissolve (1)
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d039'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d040'])]"
        show ep04_nana_pussy_show05 with Dissolve (1)
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d041'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d042'])]"
        show ep04_nana_pussy_show04 with Dissolve (1)
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d043'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d044'])]"
        show ep04_nana_pussy_show05 with Dissolve (1)
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d045'])]"
    $ stopAudio("sfx", 3, 1)
    show ep04_nana_pussylick01 with Dissolve (0.5)
    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_madohxxx, "sfx", 4, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d046'])]"
    show ep04_nana_pussylick02 with Dissolve (0.5)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d047'])]"
    show ep04_nana_pussylick03 with Dissolve (0.5)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d048'])]"
    show ep04_nana_pussylick04 with Dissolve (0.5)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d049'])]"
    show ep04_nana_pussylick05 with Dissolve (0.5)
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d050'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d051'])]"
    $ stopAudio("sfx", 4, 0.5)
    show ep04_nana_pussylick2_01 with Dissolve (0.5)
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_moan_breath2, "sfx", 5, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d052'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d053'])]"
    show ep04_nana_pussylick2_02 with Dissolve (0.5)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d054'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d055'])]"
    show ep04_nana_pussylick2_03 with Dissolve (0.5)
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d056'])]"
    show ep04_nana_pussylick2_04 with Dissolve (0.5)
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d057'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d058'])]"
    show ep04_nana_pussylick2_05 with Dissolve (0.5)
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d059'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d060'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d061'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d062'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep04_nanadrunkforced02 at subtle_zoom_out with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d063'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d064'])]"
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
    show ep04_nanadrunkforced03 with vpunch
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d065'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d066'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d067'])]"
    if ep04_nanadad:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d068'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d069'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d070'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d071'])]"
    $ setChannelVolume("music", 1, 0.5, 1.0) 
    $ playAudio(nanami_innocence_theme, "music", 1, True, 2.0, 1.0)
    show ep04_nanadrunkforced04 at ken_burns_bottom_to_top with vpunch
    $ setChannelVolume("sfx", 4, 0.5, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 4, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d072'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d073'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d074'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d075'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d076'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d077'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d078'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d079'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d080'])]"
    show ep04_nanadrunkforced05
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d081'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d082'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d083'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d084'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d085'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d086'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d087'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d088'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d089'])]"
    show ep04_nanadrunkforced06 at ken_burns_top_to_bottom
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d090'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d091'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d092'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d093'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d094'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d095'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d096'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d097'])]"
    show ep04_nanadrunkforced07
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d098'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d099'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLIC_d100'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d101'])]"
    show ep04_nanadrunkforced08
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d102'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d103'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d104'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d105'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d106'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d107'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLIC_d108'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLIC_d109'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLIC_d110'])]"
    jump ep04_nanaleave2



label ep04_nanaleave:
    $ stopAllSubchannels("music", 2.0)
    show ep04_nanadrunkleave01 with normalfade
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d001'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEV_d002'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d003'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d004'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d005'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d006'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEV_d007'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d008'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d009'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d010'])]"
    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_yawnnana, "sfx", 4, False, 0, 0)
    show ep04_nanadrunkleave02
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d011'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d012'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d013'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEV_d014'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEV_d015'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEV_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d017'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLEV_d018'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLEV_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d020'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLEV_d021'])]"
    $ show_walkthrough("ep04_nanaleavemenu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEV_d022'])]"
        "Ask her to stay":
            hide screen walkthrough_screen
            $ ep04_nanastay = True
            mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d023'])]"
            # +1x love @ endlabel
            jump ep04_nanaleave_bed
        "Let her go to Madison":
            hide screen walkthrough_screen
            # -1x love @ endlabel
            mc_s "[renpy.substitute(dialogues4['E04MCNANLEV_d024'])]"
            jump ep04_nanaleave_hall



label ep04_nanaleave2:
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep04_nanadrunkleave01 with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d001'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLV2_d002'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANLV2_d003'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d004'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLV2_d005'])]"
        mc_t "[renpy.substitute(dialogues4['E04MCNANLV2_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLV2_d007'])]"
    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_yawnnana, "sfx", 4, False, 0, 0)
    show ep04_nanadrunkleave02
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d008'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLV2_d010'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLV2_d011'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d012'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d013'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d014'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d015'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d016'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLV2_d017'])]"
    $ show_walkthrough("ep04_nanaleave2menu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MCNANLV2_d018'])]"
        "Ask her to stay":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANLV2_d019'])]"
            $ ep04_nanastay = True
            # +1x love @ endlabel
            jump ep04_nanaleave_bed
        "Let her go to Madison":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MCNANLV2_d020'])]"
            # -1x love @ endlabel
            jump ep04_nanaleave_hall


label ep04_nanaleave_bed:
    scene eigengrau
    $ setChannelVolume("music",2, 0.3, 1.0)
    $ playAudio(nanami_love_theme, "music", 2, True, 2.0, 1.0)
    show ep04_nanadrunkleave03
    $ rm.update("nanami", "trust", 3)
    $ check_levels("nanami", "trust", 3)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d001'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d002'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d003'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d004'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d005'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d006'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d007'])]"
        mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d008'])]"
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    show ep04_nanasleep03 with hpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d009'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d010'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d011'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d012'])]"
    show ep04_nanasleep04 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d014'])]"
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    show ep04_nanasleep05 at ken_burns_right_to_left with hpunch
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d015'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d016'])]"
    show ep04_nanasleep06
    $ setChannelVolume("sfx", 3, 0.6, 0)
    $ playAudio(sfx_kiss_nana, "sfx", 3, False, 0, 0)
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d017'])]"
    show ep04_nanasleep07
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d018'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d019'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d020'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d021'])]"
    show ep04_nanasleep08 at subtle_zoom_in
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d022'])]"
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d023'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d024'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d026'])]"
    hide ep04_nanasleep08
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d028'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d029'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d030'])]"
    show ep04_nanasleep09 with normalfade
    nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d032'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d033'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d034'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d035'])]"
        nana "[renpy.substitute(dialogues4['E04MCNANLEVBD_d036'])]"
    mc_s "[renpy.substitute(dialogues4['E04MCNANLEVBD_d037'])]"
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_bedmove2, "sfx", 1, False, 0, 0)
    show ep04_nanamcroom32 at ken_burns_right_to_left with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d038'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d039'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d040'])]"
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 0.5
    show ep04_nanamcroom33 at ken_burns_corner_to_corner with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d041'])]"
    if ep04_nanadad:
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d042'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MCNANLEVBD_d043'])]"
    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    pause 0.5
    $ stopAllSubchannels("music", 2.0)
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_elimeet_intro


label ep04_nanaleave_hall:
    show ep04_nanadrunkleave04
    $ rm.update("nanami", "trust", -3)
    $ check_levels("nanami", "trust", -3)
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANHAL_d001'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANHAL_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d003'])]"
    scene eigengrau with slowfade
    show ep04_nanadrunkleave05 with circlewipe
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues4['E04MCNANHAL_d004'])]"
    else:
        nana "[renpy.substitute(dialogues4['E04MCNANHAL_d005'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d006'])]"
    mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d007'])]"
    $ show_walkthrough("ep04_nanalehallmenu")
    menu:
        "Walk her to her room":
            hide screen walkthrough_screen
            # +1x love @ endlabel
            if ep04_nanadad:
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d008'])]"
            else:
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d009'])]"
            show ep04_nanadrunkleave07 at ken_burns_left_to_right with normalfade
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d010'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d011'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d012'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d013'])]"
            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1.0
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with slowfade
            $ setChannelVolume(channel="amb", subchannel=3, volume=0.3)
            $ playAudio(sfx_nightsleep, "amb", 3, True, 1.5, 0)
            show ep04_hallmeeting01 at ken_burns_bottom_to_top with circlewipe
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d014'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d015'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d016'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d017'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d018'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d019'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d020'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d021'])]"
            show ep04_hallmeeting02 with normalfade
            if ep04_nanadad:
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d022'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d023'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d024'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d025'])]"
            else:
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d026'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d027'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d028'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d029'])]"
            show ep04_hallmeeting03
            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)
            nana "[renpy.substitute(dialogues4['E04MCNANHAL_d030'])]"
            if ep04_nanadad:
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d031'])]"
            else:
                mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d032'])]"
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d033'])]"
            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 0.5
            show ep04_hallmeeting04 at ken_burns_left_to_right with circlewipe
            mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d034'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d035'])]"
            amb "[renpy.substitute(dialogues4['E04MCNANHAL_d036'])]"
            jump ep04_ambhall
        "Let her go alone":
            hide screen walkthrough_screen
            # -2x love @ endlabel
            if ep04_nanadad:
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d037'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d038'])]"
            else:
                mc_s "[renpy.substitute(dialogues4['E04MCNANHAL_d039'])]"
                nana "[renpy.substitute(dialogues4['E04MCNANHAL_d040'])]"
            show ep04_nanadrunkleave06  at ken_burns_left_to_right with normalfade
            mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d041'])]"
            mc_t "[renpy.substitute(dialogues4['E04MCNANHAL_d042'])]"
            $ rm.update("nanami", "trust", -6)
            $ check_levels("nanami", "trust", -6)
            $ ep04_afternanami += 1
            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1.0
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep04_mad_mcroom



label ep04_ambhall:
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(amber_2nd_theme, "music", 1, True, 5.0, 0)
    scene eigengrau with slowfade
    show ep04_hallmeeting05 at ken_burns_bottom_to_top
    amb "[renpy.substitute(dialogues4['E04AMBHAL_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d002'])]"
    amb "[renpy.substitute(dialogues4['E04AMBHAL_d003'])]"
    if ep03_amberstrike or ep03_amberangry:
        show ep04_hallmeeting07 with normalfade
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d004'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d005'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d006'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d007'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d008'])]"
        show ep04_hallmeeting09 with normalfade
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d009'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d010'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d011'])]"
        mc_t "[renpy.substitute(dialogues4['E04AMBHAL_d012'])]"
        $ show_walkthrough("ep04_ambhallmenu")
        menu:
            mc_t "[renpy.substitute(dialogues4['E04AMBHAL_d013'])]"
            "Go to the livingroom":
                hide screen walkthrough_screen
                $ ep04_amber_rejects_mc = True
                $ stopAllSubchannels("music", 2.0)
                $ stopAllSubchannels("amb", 2.0)
                jump ep04_elimeet_intro
            "Go to your room":
                hide screen walkthrough_screen
                $ ep04_amber_rejects_mc = True
                $ ep04_afternanami += 2
                $ stopAllSubchannels("music", 2.0)
                $ stopAllSubchannels("amb", 2.0)
                jump ep04_mad_mcroom
    else:
        show ep04_hallmeeting07 with normalfade
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d014'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d015'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d016'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d017'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d018'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d019'])]"
        show ep04_hallmeeting06
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d020'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d021'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d022'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d023'])]"
        show ep04_hallmeeting08 with normalfade
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d024'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d025'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d026'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d027'])]"
        amb "[renpy.substitute(dialogues4['E04AMBHAL_d028'])]"
        mc_s "[renpy.substitute(dialogues4['E04AMBHAL_d029'])]"  
        $ stopAllSubchannels("music", 2.0)
        $ stopAllSubchannels("amb", 2.0)
        scene eigengrau with normalfade
        $ setChannelVolume("sfx", 2, 0.6, 0)
        $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
        pause 1.0
        jump ep04_ambroom_intro



label ep04_ambroom_intro:
    
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 4, True, 1.5, 0)
    show ep04_ambroom01 at ken_burns_left_to_right with circlewipe
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d002'])]"
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d004'])]"
    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_changeclothes_nozip, "sfx", 2, False, 0, 0)
    pause 1.5
    show ep04_ambroom02 with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d006'])]"
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d008'])]"
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(antonella_sexy_theme, "music", 1, True, 5.0, 0)
    show ep04_ambroom03 at ken_burns_bottom_to_top
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d010'])]"
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d012'])]"
    show ep04_ambroom04 with hpunch
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d013'])]"
    amb "[renpy.substitute(dialogues4['E04AMBRIN_d014'])]"
    $ show_walkthrough("ep04_ambroommenu")
    menu:
        "You?":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d015'])]"
            show ep04_ambroom07 at ken_burns_top_to_bottom with vpunch
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d016'])]"
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d017'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d018'])]"
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d019'])]"
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d020'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d021'])]"
            $ stopAllSubchannels("music", 2.0)
            $ setChannelVolume("amb", 4, 0, 1.0)
            jump ep04_amber_dancing
        "LEDs?":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d022'])]"
            $ ep04_mc_amber_dumb = True
            $ stopAllSubchannels("music", 1.0)
            $ setChannelVolume("sfx", 1, 0.4, 0)
            $ playAudio(sfx_recstop, "sfx", 1, False, 0, 0)
            show ep04_ambroom06 with vpunch
            $ rm.update("amber", "cor", -2)
            $ check_levels("amber", "cor", -2)
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d023'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d024'])]"
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d025'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d026'])]"
            show ep04_ambroom05 with hpunch
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d027'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d028'])]"
            amb "[renpy.substitute(dialogues4['E04AMBRIN_d029'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBRIN_d030'])]"
            $ show_walkthrough("ep04_ambroommenu_2")
            menu:
                mc_t "[renpy.substitute(dialogues4['E04AMBRIN_d031'])]"
                "Go to the livingroom":
                    hide screen walkthrough_screen
                    $ stopAllSubchannels("amb", 2.0)
                    jump ep04_elimeet_intro
                "Go to your room":
                    hide screen walkthrough_screen
                    $ ep04_afternanami += 3
                    $ stopAllSubchannels("amb", 2.0)
                    jump ep04_mad_mcroom



label ep04_amber_dancing:
    scene eigengrau
    pause 1.0
    $ setChannelVolume("amb", 4, 0.3, 1.0)
    show ep04_ambdance01 at ken_burns_left_to_right with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d002'])]"
    show ep04_ambdance02
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d004'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d005'])]"
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 2.0, 0)
    show ep04_ambdance03
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d007'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d009'])]"
    show ep04_ambdance04 at ken_burns_right_to_left with vpunch
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d011'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d013'])]"
    show ep04_ambdance05 at ken_burns_corner_to_corner2
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d015'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d017'])]"
    show ep04_ambdance06 at ken_burns_bottom_to_top with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d019'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d021'])]"
    show ep04_ambdance07 at subtle_zoom_out with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d022'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d023'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d025'])]"
    show ep04_ambdance08 with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d026'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d028'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d030'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 0.9, 0)
    $ playAudio(sfx_changeclothes_zip, "sfx", 1, False, 0, 0)
    pause 2.0
    show ep04_ambdance09 with circlewipe
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBDAN_d032'])]"
    amb "[renpy.substitute(dialogues4['E04AMBDAN_d033'])]"
    jump ep04_amber_tasting_d



label ep04_amber_tasting_d:
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d002'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d004'])]"
    show ep04_ambtaste01
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d005'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d006'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d007'])]"
    if ep01_first:
        mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d008'])]"
        amb "[renpy.substitute(dialogues4['E04AMBTSD_d009'])]"
    else:
        mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d010'])]"
        amb "[renpy.substitute(dialogues4['E04AMBTSD_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d012'])]"
    show ep04_ambtaste02
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d014'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d015'])]"
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(amber_sexy_theme2, "music", 1, True, 2.0, 0)
    show ep04_ambtaste03
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d017'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d019'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d020'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d021'])]"
    show ep04_ambtaste04
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_female_hmm2, "sfx", 1, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d022'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d023'])]"
    show ep04_ambtaste05 at ken_burns_bottom_to_top with normalfade
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d024'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d025'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d026'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d027'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d028'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d029'])]"
    show ep04_ambtaste06
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_female_hmm, "sfx", 2, False, 0, 0)
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d030'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d031'])]"
    mc_t "[renpy.substitute(dialogues4['E04AMBTSD_d032'])]"
    mc_t "[renpy.substitute(dialogues4['E04AMBTSD_d033'])]"
    show ep04_ambtaste07 at ken_burns_bottom_to_top
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d034'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d035'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d036'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d037'])]"
    show ep04_ambtaste08
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d038'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d039'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d040'])]"
    show ep04_ambtaste09
    $ setChannelVolume("sfx", 3, 0.4, 0)
    $ playAudio(sfx_female_hmm2, "sfx", 3, False, 0, 0)
    mc_t "[renpy.substitute(dialogues4['E04AMBTSD_d041'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d042'])]"
    mc_t "[renpy.substitute(dialogues4['E04AMBTSD_d043'])]"
    show ep04_ambtaste10
    $ setChannelVolume("sfx", 4, 0.4, 0)
    $ playAudio(sfx_gagreflex4, "sfx", 4, False, 0, 0)
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d044'])]"
    mc_t "[renpy.substitute(dialogues4['E04AMBTSD_d045'])]"
    show ep04_ambtaste11
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d046'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d047'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d048'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d049'])]"
    mc_t "[renpy.substitute(dialogues4['E04AMBTSD_d050'])]"
    show ep04_ambtaste12 with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d051'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d052'])]"
    show ep04_ambtaste13
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d053'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d054'])]"
    show ep04_ambtaste14
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d055'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d057'])]"
    show ep04_ambtaste15 with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d058'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d059'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBTSD_d060'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d061'])]"
    amb "[renpy.substitute(dialogues4['E04AMBTSD_d062'])]"
    $ stopAllSubchannels("sfx", 1.0)
    jump ep04_amber_bj



label ep04_amber_bj:
    scene eigengrau
    $ ss.add("amber", "blowjob")
    show ep04_amber_bj01
    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_fellatio1, "sfx", 5, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d001'])]"
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d002'])]"
    show ep04_amber_bj02
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d003'])]"
    show ep04_amber_bj03
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d004'])]"
    show ep04_amber_bj04
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d005'])]"
    show ep04_amber_bj05
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d006'])]"
    show ep04_amber_bj06
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d007'])]"
    show ep04_amber_bj07
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d008'])]"
    show ep04_amber_bj08
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d009'])]"
    show ep04_amber_bj09
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d010'])]"
    show ep04_amber_bj10
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d011'])]"
    show ep04_amber_bj11
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d012'])]"
    show ep04_amber_bj12
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d013'])]"
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d014'])]"
    $ stopAllSubchannels("sfx", 1.0)
    scene eigengrau
    show ep04_amber_bj_back01 with normalfade
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d015'])]"
    show ep04_amber_bj_back03
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d016'])]"
    show ep04_amber_bj_back04
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d017'])]"
    show ep04_amber_bj_back06
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d018'])]"
    show ep04_amber_bj_back08
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d019'])]"
    show ep04_amber_bj_back09
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d020'])]"
    show ep04_amber_bj_back12
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d021'])]"
    show ep04_ambblow01 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04AMBBJ_d022'])]"
    show ep04_amber_bj_side01 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04AMBBJ_d023'])]"
    show ep04_amber_bj_side02
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d024'])]"
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d025'])]"
    show ep04_amber_bj_side03
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d026'])]"
    show ep04_amber_bj_side04
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d028'])]"
    show ep04_amber_bj_side05
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d029'])]"
    show ep04_amber_bj_side06
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d030'])]"
    show ep04_amber_bj_side07
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d032'])]"
    show ep04_amber_bj_side08
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d033'])]"
    show ep04_amber_bj_side09
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d034'])]"
    show ep04_amber_bj_side10
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d036'])]"
    show ep04_amber_bj_side11
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d037'])]"
    show ep04_amber_bj_side12
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d038'])]"
    scene eigengrau
    show ep04_ambblow02
    amb "[renpy.substitute(dialogues4['E04AMBBJ_d039'])]"
    $ show_walkthrough("ep04_ambbjmenu")
    menu:
        "Cum on her tits":
            hide screen walkthrough_screen
            $ ep04_ambnight_cum += 2
            show white zorder 1.0 at ejaculation_flash
            show ep04_ambblow03 at vpunch with flash
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d040'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d041'])]"
            show ep04_ambblow04
            $ stopAllSubchannels("music", 2.0)
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d042'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d043'])]"
            show ep04_ambblow05 at subtle_zoom_in
            $ playAudio(amber_sexy_theme, "music", 3, True, 2.0, 1.0)
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d044'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d045'])]"
            show ep04_ambblow06 with hpunch
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d046'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d047'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d048'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d049'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d050'])]"
            show ep04_ambblow07 with normalfade
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d051'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d052'])]"
            show ep04_ambblow08
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d053'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d054'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d055'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d056'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d057'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d058'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d059'])]"
            show ep04_ambblow09 at subtle_zoom_out with normalfade
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d060'])]"
            mc_t "[renpy.substitute(dialogues4['E04AMBBJ_d061'])]"
            mc_t "[renpy.substitute(dialogues4['E04AMBBJ_d062'])]"
            jump ep04_amber_endscene
        "Cum on her face":
            hide screen walkthrough_screen
            $ ep04_ambnight_cum += 1
            show white zorder 1.0 at ejaculation_flash
            show ep04_ambblow03 at vpunch with flash
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d063'])]"
            show ep04_ambblow10
            $ stopAllSubchannels("music", 2.0)
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d064'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d043'])]"
            show ep04_ambblow11 with hpunch
            $ playAudio(amber_sexy_theme, "music", 3, True, 2.0, 1.0)
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d066'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d067'])]"
            show ep04_ambblow12
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d068'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d069'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d070'])]"
            show ep04_ambblow13 with normalfade
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d071'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d072'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d073'])]"
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d074'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d075'])]"
            show ep04_ambblow14 with normalfade
            amb "[renpy.substitute(dialogues4['E04AMBBJ_d076'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d077'])]"
            amb_y "[renpy.substitute(dialogues4['E04AMBBJ_d078'])]"
            mc_s "[renpy.substitute(dialogues4['E04AMBBJ_d079'])]"
            mc_t "[renpy.substitute(dialogues4['E04AMBBJ_d080'])]"
            jump ep04_amber_endscene



label ep04_amber_endscene:
    if ep04_ambnight_cum == 2:
        $ ep04_ach_amber = True
    else:
        pass
    $ show_walkthrough("ep04_ambendmenu")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04AMBENDSC_d001'])]"
        "Go to the livingroom":
            hide screen walkthrough_screen
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep04_elimeet_intro
        "Go to your room":
            hide screen walkthrough_screen
            $ ep04_afternanami += 4
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep04_mad_mcroom



label ep04_mad_mcroom:
    
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)
    show ep04_madmcroom01 with circlewipe
    if ep04_afternanami == 1:
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d001'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d002'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d003'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d004'])]"
    elif ep04_afternanami == 2:
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d005'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d006'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d007'])]"
    elif ep04_afternanami == 3:
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d008'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d009'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d010'])]"
    else:
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d011'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d012'])]"
        mc_t "[renpy.substitute(dialogues4['E04MADMCR_d013'])]"
    $ setChannelVolume("sfx", 1, 0.8, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 1, False, 0, 0)
    show ep04_madmcroom02 at focus_pulse:
        rotate 180
        xzoom -1
        align (0.5, 0.5)
    mc_t "[renpy.substitute(dialogues4['E04MADMCR_d014'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADMCR_d015'])]"
    $ stopAudio("sfx", 1, 1)
    show ep04_madmcroom03:
        rotate 180
        xzoom -1
        align (0.5, 0.5)
    $ setChannelVolume("sfx", 2, 0.8, 0)
    $ playAudio(sfx_phone_typing, "sfx", 2, False, 0, 0)
    mc_t "[renpy.substitute(dialogues4['E04MADMCR_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADMCR_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d018'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d020'])]"
    $ stopAudio("sfx", 2, 1)
    show ep04_madmcroom04:
        rotate 180
        xzoom -1
        align (0.5, 0.5)
    mad "[renpy.substitute(dialogues4['E04MADMCR_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d022'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d023'])]"
    $ setChannelVolume("music", 2, 0.5, 1.0) 
    $ playAudio(madison_theme, "music", 2, True, 2.0, 1.0)
    show ep04_madmcroom05 at ken_burns_bottom_to_top with normalfade
    mad "[renpy.substitute(dialogues4['E04MADMCR_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d025'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d026'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d027'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d028'])]"
    show ep04_madmcroom06
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d029'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d030'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d031'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d032'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMCR_d033'])]"
    mad "[renpy.substitute(dialogues4['E04MADMCR_d034'])]"
    $ show_walkthrough("ep04_madmcmenu")
    menu:
        "Massage her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d035'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d036'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d037'])]"
            jump ep04_mad_massagebody
        "Refuse":
            hide screen walkthrough_screen
            $ stopAudio("music", 2, 2)
            $ rm.update("madison", "trust", -1)
            $ check_levels("madison", "trust", -1)
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d038'])]"
            $ setChannelVolume("music", 3, 0.5, 1.0) 
            $ playAudio(madison_bad_theme, "music", 3, True, 2.0, 1.0)
            show ep04_madmcroom07 with vpunch
            $ setChannelVolume("sfx", 2, 0.8, 0)
            $ playAudio(sfx_phone_typing, "sfx", 2, False, 0, 0)
            mad "[renpy.substitute(dialogues4['E04MADMCR_d039'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d040'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d041'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d042'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d043'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d044'])]"
            $ stopAudio("sfx", 2, 1)
            show ep04_madmcroom08 at ken_burns_right_to_left with hpunch
            mad "[renpy.substitute(dialogues4['E04MADMCR_d045'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d046'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d047'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d048'])]"
            show ep04_madmcroom09 at subtle_zoom_out with normalfade
            mad "[renpy.substitute(dialogues4['E04MADMCR_d049'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d050'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d051'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d052'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d053'])]"
            show ep04_madmcroom10 with hpunch
            mad "[renpy.substitute(dialogues4['E04MADMCR_d054'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d055'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d056'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d057'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d058'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d059'])]"
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)
            show ep04_madmcroom11 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d060'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d061'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d062'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d063'])]"
            show ep04_madmcroom12 with normalfade
            mad "[renpy.substitute(dialogues4['E04MADMCR_d064'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d065'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d066'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d067'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d068'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d069'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d070'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d071'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMCR_d072'])]"
            show ep04_madmcroom13
            mad "[renpy.substitute(dialogues4['E04MADMCR_d073'])]"
            mad "[renpy.substitute(dialogues4['E04MADMCR_d074'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADMCR_d075'])]"
            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "[renpy.substitute(dialogues4['E04MADMCR_d076'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADMCR_d077'])]"
            $ ep04_madnight += 1
            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall



label ep04_mad_massagebody:
    scene eigengrau
    show ep04_madmassage01
    $ rm.update("madison", "trust", 1)
    $ check_levels("madison", "trust", 1)
    mc_t "[renpy.substitute(dialogues4['E04MADMAS_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADMAS_d002'])]"
    $ setChannelVolume("amb", 1, 0, 1.0)
    $ setAllSubchannelsVolume("music", 0, 1.0)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 1.0
    $ setChannelVolume("amb", 1, 0.3, 1.0)
    $ setAllSubchannelsVolume("music", 0.5, 1.0)
    show ep04_madmassage02 at ken_burns_top_to_bottom with circlewipe
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d003'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d005'])]"
    show ep04_madmassage03 at subtle_zoom_out
    mad "[renpy.substitute(dialogues4['E04MADMAS_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d007'])]"
    show ep04_madmassage04
    mad "[renpy.substitute(dialogues4['E04MADMAS_d008'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d010'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    show ep04_madmassage05
    mad "[renpy.substitute(dialogues4['E04MADMAS_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d012'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d013'])]"
    show ep04_madmassage06 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADMAS_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d015'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d017'])]"
    show ep04_madmassage07 at ken_burns_left_to_right with normalfade
    mad "[renpy.substitute(dialogues4['E04MADMAS_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d019'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d020'])]"
    show ep04_madmassage08 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d021'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d022'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d023'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d025'])]"
    show ep04_madmassage09 at ken_burns_top_to_bottom
    mad "[renpy.substitute(dialogues4['E04MADMAS_d026'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d027'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d028'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d029'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_madmassage10 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADMAS_d030'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d031'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d032'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.3)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)
    show ep04_madmassage11
    mad "[renpy.substitute(dialogues4['E04MADMAS_d033'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d034'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d035'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d036'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d037'])]"
    show ep04_madmassage12
    mad "[renpy.substitute(dialogues4['E04MADMAS_d038'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d039'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d040'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d041'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d042'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d043'])]"
    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(madison_dom_theme, "music", 1, True, 2.0, 1.0)
    show ep04_madmassage13 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADMAS_d044'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d045'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d046'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d047'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d025'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d050'])]"
    show ep04_madmassage14 at ken_burns_bottom_to_top with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d051'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d052'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d053'])]"
    $ stopAudio("music", 1, 2)
    show ep04_madmassage15 at ken_burns_top_to_bottom
    mad "[renpy.substitute(dialogues4['E04MADMAS_d054'])]"
    $ setChannelVolume("music", 2, 0.3, 1.0)
    $ playAudio(madison_sad_theme, "music", 2, True, 2.0, 1.0)
    mad "[renpy.substitute(dialogues4['E04MADMAS_d055'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d056'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d057'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d058'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d059'])]"
    show ep04_madmassage16
    mad "[renpy.substitute(dialogues4['E04MADMAS_d060'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d061'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d062'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d063'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d064'])]"
    show ep04_madmassage17 with hpunch
    mad "[renpy.substitute(dialogues4['E04MADMAS_d065'])]"
    $ stopAudio("music", 2, 2)
    mad "[renpy.substitute(dialogues4['E04MADMAS_d066'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d067'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADMAS_d068'])]"
    mad "[renpy.substitute(dialogues4['E04MADMAS_d069'])]"
    $ ep04_madstory = True
    $ show_walkthrough("ep04_madmassmenu")
    menu:
        "Help her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d070'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d071'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d072'])]"
            #+1X love @ endlabel
            jump ep04_mad_reward
        "Refuse":
            hide screen walkthrough_screen
            $ rm.update("madison", "trust", -1)
            $ check_levels("madison", "trust", -1)
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d073'])]"
            scene eigengrau
            $ setChannelVolume("music", 3, 0.3, 1.0)
            $ playAudio(madison_bad_theme, "music", 3, True, 2.0, 1.0)
            show ep04_madmassage18 at ken_burns_bottom_to_top with vpunch
            mad "[renpy.substitute(dialogues4['E04MADMAS_d074'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d075'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d076'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d077'])]"
            $ setChannelVolume("sfx", 1, 0.9, 0)
            $ playAudio(sfx_punch, "sfx", 1, False, 0, 0)
            show ep04_madmassage19 with hpunch
            mad "[renpy.substitute(dialogues4['E04MADMAS_d078'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d079'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d080'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d081'])]"
            scene eigengrau with slowfade
            show ep04_madmassage20 with vpunch
            mad "[renpy.substitute(dialogues4['E04MADMAS_d082'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d083'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d084'])]"
            show ep04_madmassage21
            mc_t "[renpy.substitute(dialogues4['E04MADMAS_d085'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADMAS_d086'])]"
            show ep04_madmassage22 with hpunch
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d087'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d027'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d089'])]"
            show ep04_madmassage23 with normalfade
            mad "[renpy.substitute(dialogues4['E04MADMAS_d090'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADMAS_d091'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d092'])]"
            show ep04_madmassage24
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d093'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d094'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d095'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d096'])]"
            show ep04_madmassage25
            mad "[renpy.substitute(dialogues4['E04MADMAS_d097'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d098'])]"
            mc_y "[renpy.substitute(dialogues4['E04MADMAS_d099'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d100'])]"
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)
            show ep04_madmassage26 at photo_effect with flash
            show photo_flash with dissolve
            mad "[renpy.substitute(dialogues4['E04MADMAS_d101'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d102'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d103'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d104'])]"
            show ep04_madmassage27
            mad "[renpy.substitute(dialogues4['E04MADMAS_d105'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d106'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d107'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADMAS_d108'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d109'])]"
            mad "[renpy.substitute(dialogues4['E04MADMAS_d110'])]"
            show ep04_madmassage28
            mad "[renpy.substitute(dialogues4['E04MADMAS_d111'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADMAS_d112'])]"
            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "[renpy.substitute(dialogues4['E04MADMAS_d113'])]"
            $ ep04_madnight += 2
            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall



label ep04_mad_reward:
    scene eigengrau
    $ setChannelVolume("music", 2, 0.3, 1.0)
    $ playAudio(madison_theme, "music", 2, True, 2.0, 1.0)
    show ep04_madnopanties01
    $ rm.update("madison", "trust", 1)
    $ check_levels("madison", "trust", 1)
    mad "[renpy.substitute(dialogues4['E04MADRE_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d002'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d002'])]"
    show ep04_madnopanties02 with vpunch
    mad "[renpy.substitute(dialogues4['E04MADRE_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d006'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d008'])]"
    show ep04_madnopanties03
    mad "[renpy.substitute(dialogues4['E04MADRE_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d010'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d012'])]"
    show ep04_madnopanties04 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADRE_d015'])]"
    show ep04_madnopanties05 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d017'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d019'])]"
    show ep04_madnopanties06 at ken_burns_left_to_right with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d021'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d022'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d023'])]"
    show ep04_madnopanties07 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d025'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d026'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d027'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_madnopanties08 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d028'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d030'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d032'])]"
    $ setChannelVolume("music", 5, 0.3, 1.0)
    $ playAudio(nanami_innocence_theme, "music", 5, True, 2.0, 1.0)
    show ep04_madnopanties09 at ken_burns_left_to_right with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d033'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d034'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d036'])]"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    show ep04_madnopanties10 with normalfade
    $ setChannelVolume("sfx", 3, 0.8, 0)
    $ playAudio(sfx_phone_typing, "sfx", 3, False, 0, 0)
    mad "[renpy.substitute(dialogues4['E04MADRE_d037'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d038'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d039'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d040'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d041'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d042'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d043'])]"
    show ep04_madnopanties11 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d044'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d045'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d046'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d047'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d048'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d049'])]"
    show ep04_madnopanties12
    mad "[renpy.substitute(dialogues4['E04MADRE_d050'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d051'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d052'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d053'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d054'])]"
    show ep04_madnopanties13
    mad "[renpy.substitute(dialogues4['E04MADRE_d055'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d056'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d057'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d059'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d060'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d061'])]"
    show ep04_madnopanties14
    mad "[renpy.substitute(dialogues4['E04MADRE_d062'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d063'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d064'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_madisonleave01 with normalfade
    $ ep04_madnanastory = True
    mad "[renpy.substitute(dialogues4['E04MADRE_d065'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d066'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d067'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d068'])]"
    show ep04_madisonleave02 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADRE_d069'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d070'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d071'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d072'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d073'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADRE_d074'])]"
    mad "[renpy.substitute(dialogues4['E04MADRE_d075'])]"
    $ show_walkthrough("ep04_madrewamenu")
    menu:
        "Continue":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADRE_d076'])]"
            mad "[renpy.substitute(dialogues4['E04MADRE_d077'])]"
            # 1x love @endlabel
            jump ep04_mad_assjob
        "Stop":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADRE_d078'])]"
            mad "[renpy.substitute(dialogues4['E04MADRE_d079'])]"
            # -1x love @endlabel
            $ ep04_madnight += 3
            jump ep04_mad_assjob_deny



label ep04_mad_assjob_deny:
    scene eigengrau with slowfade
    $ setChannelVolume("music", 2, 0.3, 1.0)
    $ playAudio(madison_bad_theme, "music", 2, True, 2.0, 1.0)
    show ep04_madisonleave03 with vpunch
    $ rm.update("madison", "trust", -1)
    $ check_levels("madison", "trust", -1)
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d001'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d002'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d003'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d004'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJDN_d005'])]"
    show ep04_madisonleave04 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d006'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d007'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJDN_d009'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d010'])]"
    $ setChannelVolume("sfx", 3, 0.8, 0)
    $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)
    show ep04_madmassage26 at photo_effect with flash
    show photo_flash with dissolve
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJDN_d012'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJDN_d014'])]"
    show ep04_madmassage27
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d015'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d016'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d017'])]"
    show ep04_madmassage28
    mad "[renpy.substitute(dialogues4['E04MADAJDN_d018'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJDN_d019'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.0
    show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
    mc_t "[renpy.substitute(dialogues4['E04MADAJDN_d020'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJDN_d021'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJDN_d022'])]"
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall



label ep04_mad_assjob:
    scene eigengrau with slowfade
    $ setChannelVolume("music", 1, 0.2, 1.0)
    $ playAudio(madison_sexy_theme, "music", 1, True, 2.0, 1.0)
    show ep04_madmovingass01 at concentrate with hpunch
    $ rm.update("madison", "trust", 1)
    $ check_levels("madison", "trust", 1)
    mad "[renpy.substitute(dialogues4['E04MADAJ_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d002'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d005'])]"
    show ep04_madmovingass02 at concentrate
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d006'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d008'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d010'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d011'])]"
    show ep04_madmovingass03 at concentrate
    mad "[renpy.substitute(dialogues4['E04MADAJ_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d013'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d014'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJ_d015'])]"
    $ show_walkthrough("ep04_madajmenu")
    menu:
        "Continue":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d016'])]"
            pass
        "Stop":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d017'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d018'])]"
            $ stopAllSubchannels("music", 2.0)
            $ ep04_madnight += 3
            # -1x love @endlabel
            jump ep04_mad_assjob_deny
    show ep04_madi_asslick01
    $ rm.update("madison", "trust", 1)
    $ check_levels("madison", "trust", 1)
    $ rm.update("madison", "cor", 2)
    $ check_levels("madison", "cor", 2)
    mad "[renpy.substitute(dialogues4['E04MADAJ_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    show ep04_madi_asslick02
    mad "[renpy.substitute(dialogues4['E04MADAJ_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    show ep04_madi_asslick03
    mad "[renpy.substitute(dialogues4['E04MADAJ_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    show ep04_madi_asslick04
    mad "[renpy.substitute(dialogues4['E04MADAJ_d025'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    show ep04_madi_asslick05
    mad "[renpy.substitute(dialogues4['E04MADAJ_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    show ep04_madi_asslick06
    mad "[renpy.substitute(dialogues4['E04MADAJ_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d004'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d002'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d033'])]"
    $ show_walkthrough("ep04_madajmenu_2")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MADAJ_d034'])]"
        "Continue":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d035'])]"
            $ setChannelVolume("amb", 1, 0, 1.0)
            pass
        "Stop":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d036'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d037'])]"
            $ ep04_madnight += 3
            $ stopAllSubchannels("music", 2.0)
            $ setChannelVolume("amb", 1, 0, 1.0)
            jump ep04_mad_assjob_deny
    $ ss.add("madison", "assjob")
    $ ep04_madnight += 4
    pause 1.0
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.3, 1.0)
    show ep04_madassj01 with circlewipe
    $ rm.update("madison", "cor", 2)
    $ check_levels("madison", "cor", 2)
    mad "[renpy.substitute(dialogues4['E04MADAJ_d038'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d039'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d040'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d041'])]"
    show ep04_madassj02 with normalfade
    mad "[renpy.substitute(dialogues4['E04MADAJ_d042'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d043'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d044'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d045'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d046'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d047'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d049'])]"
    show ep04_madi_assjob01
    mad "[renpy.substitute(dialogues4['E04MADAJ_d050'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJ_d051'])]"
    show ep04_madi_assjob02
    mad "[renpy.substitute(dialogues4['E04MADAJ_d052'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJ_d053'])]"
    show ep04_madi_assjob03
    mad "[renpy.substitute(dialogues4['E04MADAJ_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d055'])]"
    show ep04_madi_assjob04
    mad "[renpy.substitute(dialogues4['E04MADAJ_d056'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d057'])]"
    show ep04_madi_assjob05
    mad "[renpy.substitute(dialogues4['E04MADAJ_d058'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d059'])]"
    show ep04_madi_assjob06
    mad "[renpy.substitute(dialogues4['E04MADAJ_d060'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d061'])]"
    show ep04_madi_assjob07
    mad "[renpy.substitute(dialogues4['E04MADAJ_d062'])]"
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d063'])]"
    show ep04_madi_assjob08
    mad "[renpy.substitute(dialogues4['E04MADAJ_d064'])]"
    mc_t "[renpy.substitute(dialogues4['E04MADAJ_d065'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d066'])]"
    show ep04_madi_assjob09
    mc_s "[renpy.substitute(dialogues4['E04MADAJ_d067'])]"
    mad "[renpy.substitute(dialogues4['E04MADAJ_d068'])]"
    $ show_walkthrough("ep04_madajmenu_3")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04MADAJ_d069'])]"
        "Cum inside her":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d070'])]"
            $ stopAllSubchannels("music", 2.0)
            #rrec stop sound
            show white zorder 1.0 at ejaculation_flash
            show ep04_madassj03 at hpunch with flash
            mad "[renpy.substitute(dialogues4['E04MADAJ_d002'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d072'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d073'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d074'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d075'])]"
            $ rm.update("madison", "trust", -2)
            $ check_levels("madison", "trust", -2)
            $ rm.update("madison", "cor", 2)
            $ check_levels("madison", "cor", 2)
            show ep04_madassj04 at ken_burns_top_to_bottom with vpunch
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d076'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d077'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d078'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d079'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d080'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d081'])]"
            show ep04_madassj08 with normalfade
            mad "[renpy.substitute(dialogues4['E04MADAJ_d082'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d083'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d084'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d085'])]"
            $ setChannelVolume("music", 2, 0.3, 1.0)
            $ playAudio(madison_bad_theme, "music", 2, True, 2.0, 1.0)
            mad "[renpy.substitute(dialogues4['E04MADAJ_d086'])]"
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)
            show ep04_madassj07 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d087'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d088'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d089'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d090'])]"
            show ep04_madassj09
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d091'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d092'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d093'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d094'])]"
            show ep04_madmassage28
            mad "[renpy.substitute(dialogues4['E04MADAJ_d095'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d096'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d097'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d098'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d099'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d100'])]"
            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d101'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d102'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d103'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d104'])]"
        "Hold it":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d105'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d106'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d107'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d108'])]"
            $ ss.add("madison", "pussyjob")
            show ep04_madassj05 with normalfade
            mad "[renpy.substitute(dialogues4['E04MADAJ_d109'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d110'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d111'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d112'])]"
            show ep04_madassj06
            mad "[renpy.substitute(dialogues4['E04MADAJ_d113'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d114'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d115'])]"
            show ep04_madassj10
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d116'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d117'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d085'])]"
            show ep04_madassj11
            mad "[renpy.substitute(dialogues4['E04MADAJ_d119'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d120'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d121'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d122'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d123'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d124'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d125'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d126'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d127'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d128'])]"
            show white zorder 1.0 at ejaculation_flash
            show ep04_madassj13 with flash
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d129'])]"
            show white zorder 1.0 at ejaculation_flash
            show ep04_madassj14 with flash
            mad "[renpy.substitute(dialogues4['E04MADAJ_d130'])]"
            $ stopAllSubchannels("music", 2.0)
            show ep04_madassj12 with slowfade
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d100'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d132'])]"
            show ep04_madassj15 with hpunch
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d133'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d134'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d135'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d136'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d002'])]"
            show ep04_madassj16
            mad "[renpy.substitute(dialogues4['E04MADAJ_d138'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d139'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d140'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d120'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d142'])]"
            show ep04_madassj17 with normalfade
            $ rm.update("madison", "trust", 2)
            $ check_levels("madison", "trust", 2)
            $ rm.update("madison", "cor", 4)
            $ check_levels("madison", "cor", 4)
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d143'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d144'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d145'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d120'])]"
            $ setChannelVolume("music", 2, 0.3, 1.0)
            $ playAudio(madison_theme, "music", 2, True, 2.0, 1.0)
            mad "[renpy.substitute(dialogues4['E04MADAJ_d147'])]"
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)
            show ep04_madassj18 at photo_effect with flash
            show photo_flash with dissolve
            mad "[renpy.substitute(dialogues4['E04MADAJ_d148'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d144'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d150'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d106'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d109'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d153'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d154'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d155'])]"
            show ep04_madassj19
            mad "[renpy.substitute(dialogues4['E04MADAJ_d156'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d157'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d158'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d008'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d160'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d085'])]"
            show ep04_madassj08
            mad "[renpy.substitute(dialogues4['E04MADAJ_d162'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d163'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d164'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d165'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d166'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d167'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d168'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d169'])]"
            show ep04_madassj09
            mad "[renpy.substitute(dialogues4['E04MADAJ_d170'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d171'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d172'])]"
            show ep04_madmassage28
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d120'])]"
            mad "[renpy.substitute(dialogues4['E04MADAJ_d174'])]"
            mc_s "[renpy.substitute(dialogues4['E04MADAJ_d175'])]"
            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d176'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d177'])]"
            mc_t "[renpy.substitute(dialogues4['E04MADAJ_d178'])]"
            $ ep04_ach_madison2 = True
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall



label ep04_elimeet_intro:
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    $ setChannelVolume(channel="amb", subchannel=8, volume=0.3)
    $ playAudio(sfx_fireplace, "amb", 8, True, 1.5, 0)
    show ep04_elimeet01 with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d002'])]"
    show ep04_elimeet02
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d003'])]"
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_keys, "sfx", 1, False, 0, 0)
    show ep04_elimeet03 with hpunch
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d004'])]"
    $ stopAudio("sfx", 1, 0.5)
    show ep04_elimeet04 with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d005'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d006'])]"
    show ep04_elimeet05 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d007'])]"
    $ show_walkthrough("ep04_elimeetmenu")
    menu:
        "Be gentle":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d008'])]"
            show ep04_elimeet05_y
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
            eli "[renpy.substitute(dialogues4['E04ELIMET_d009'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d010'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d011'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d012'])]"
        "Be direct":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d013'])]"
            show ep04_elimeet05_n
            $ rm.update("elizabeth", "trust", -2)
            $ check_levels("elizabeth", "trust", -2)
            eli "[renpy.substitute(dialogues4['E04ELIMET_d014'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d015'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d016'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d017'])]"
    show ep04_elimeet06 with normalfade
    $ rm.set_knows("elizabeth", True)
    eli "[renpy.substitute(dialogues4['E04ELIMET_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d019'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d020'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d022'])]"
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_changeclothes_nozip, "sfx", 2, False, 0, 0)
    $ setChannelVolume("sfx", 3, 1, 0)
    $ playAudio(sfx_toweldrop, "sfx", 3, False, 0, 0)
    show ep04_elimeet07
    eli "[renpy.substitute(dialogues4['E04ELIMET_d023'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d024'])]"
    show ep04_elimeet08
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d025'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d026'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d027'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d028'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d029'])]"
    show ep04_elimeet09 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d030'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d031'])]"
    show ep04_elimeet10 at subtle_zoom_out
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d032'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d033'])]"
    $ setChannelVolume("music", 3, 0.3, 1.0)
    $ playAudio(elizabeth_theme, "music", 3, True, 2.0, 1.0)
    show ep04_elimeet11 at ken_burns_bottom_to_top
    eli "[renpy.substitute(dialogues4['E04ELIMET_d034'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d035'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d036'])]"
    show ep04_elimeet12
    eli "[renpy.substitute(dialogues4['E04ELIMET_d037'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d038'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d039'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d040'])]"
    scene eigengrau with slowfade
    show ep04_elimeet13 at ken_burns_left_to_right
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d041'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d042'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d043'])]"
    show ep04_elimeet14 with slowfade
    eli "[renpy.substitute(dialogues4['E04ELIMET_d044'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d045'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d046'])]"
    show ep04_elimeet15 at subtle_zoom_out
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d047'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d048'])]"
    $ show_walkthrough("ep04_elimeetmenu_2")
    menu:
        "Get the glasses":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d049'])]"
            pass
        "Refuse":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d050'])]"
            show ep04_elimeet16
            $ rm.update("elizabeth", "trust", 4)
            $ check_levels("elizabeth", "trust", 4)
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d051'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d052'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d053'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d054'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d055'])]"
            $ stopAllSubchannels("music", 2.0)
            show ep04_elimeet17 at ken_burns_corner_to_corner
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d056'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d057'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d058'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d059'])]"
            if ep04_nanastay:
                mc_t "[renpy.substitute(dialogues4['E04ELIMET_d057X'])]"
                jump ep04_pazcall
            else:
                jump ep04_mad_mcroom
    show ep04_elimeet18
    $ rm.update("elizabeth", "cor", 2)
    $ check_levels("elizabeth", "cor", 2)
    $ rm.update("elizabeth", "trust", -1)
    $ check_levels("elizabeth", "trust", -1)
    eli "[renpy.substitute(dialogues4['E04ELIMET_d060'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d061'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d062'])]"
    show ep04_elimeet19 at ken_burns_corner_to_corner
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d063'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d064'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d065'])]"
    $ stopAllSubchannels("music", 2.0)
    $ setChannelVolume("amb", 1, 0, 1.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.3, 1.0)
    show ep04_elimeet20 with circlewipe
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d066'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d067'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d068'])]"
    show ep04_elimeet21
    eli "[renpy.substitute(dialogues4['E04ELIMET_d069'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d070'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d071'])]"
    show ep04_elimeet22
    eli "[renpy.substitute(dialogues4['E04ELIMET_d072'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d073'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d074'])]"
    show ep04_elimeet23
    eli "[renpy.substitute(dialogues4['E04ELIMET_d075'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d076'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d077'])]"
    show ep04_elimeet24
    eli "[renpy.substitute(dialogues4['E04ELIMET_d078'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d079'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d080'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d081'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d082'])]"
    show ep04_elimeet25
    eli "[renpy.substitute(dialogues4['E04ELIMET_d083'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d084'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d085'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d086'])]"
    show ep04_elimeet26
    eli "[renpy.substitute(dialogues4['E04ELIMET_d087'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d088'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d089'])]"
    show ep04_elimeet27 at subtle_zoom_in
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d090'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d091'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d092'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d093'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d094'])]"
    $ setChannelVolume("music", 4, 0.2, 1.0)
    $ playAudio(elizabeth_sexy_theme2, "music", 4, True, 2.0, 1.0)
    show ep04_elimeet28
    eli "[renpy.substitute(dialogues4['E04ELIMET_d095'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d096'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d097'])]"
    show ep04_elimeet29
    eli "[renpy.substitute(dialogues4['E04ELIMET_d098'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d099'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d100'])]"
    show ep04_elimeet30 at ken_burns_left_to_right with normalfade
    eli "[renpy.substitute(dialogues4['E04ELIMET_d101'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d102'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d103'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d104'])]"
    show ep04_elimeet31 with normalfade
    eli "[renpy.substitute(dialogues4['E04ELIMET_d105'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d106'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d107'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d108'])]"
    show ep04_elimeet32 at subtle_zoom_in
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d109'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d110'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d111'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d112'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d113'])]"
    show ep04_elimeet33 with vpunch
    eli "[renpy.substitute(dialogues4['E04ELIMET_d114'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d115'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d116'])]"
    scene eigengrau with smoke
    show ep01_elidress07 with smoke
    eli "[renpy.substitute(dialogues4['E04ELIMET_d117'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d062'])]"
    scene eigengrau with smoke
    show ep04_elimeet33 with smoke
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d119'])]"
    show ep04_elimeet34
    eli "[renpy.substitute(dialogues4['E04ELIMET_d120'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d121'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d122'])]"
    show ep04_elimeet35
    eli "[renpy.substitute(dialogues4['E04ELIMET_d123'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d124'])]"
    show ep04_elimeet36
    eli "[renpy.substitute(dialogues4['E04ELIMET_d125'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d126'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d127'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d128'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d129'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_elimeet37
    eli "[renpy.substitute(dialogues4['E04ELIMET_d130'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d131'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d132'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d133'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d134'])]"
    show ep04_elimeet38
    eli "[renpy.substitute(dialogues4['E04ELIMET_d135'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d136'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d137'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d138'])]"
    show ep04_elimeet39
    eli "[renpy.substitute(dialogues4['E04ELIMET_d139'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d140'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d141'])]"
    show ep04_elimeet40
    eli "[renpy.substitute(dialogues4['E04ELIMET_d142'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d108'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d144'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d145'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d146'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d147'])]"
    show ep04_elimeet41
    eli "[renpy.substitute(dialogues4['E04ELIMET_d148'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d149'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d150'])]"
    show ep04_elimeet42
    eli "[renpy.substitute(dialogues4['E04ELIMET_d151'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d152'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d153'])]"
    show ep04_elimeet43
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d154'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d155'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d156'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False, 0, 0)
    show ep04_elimeet44 with vpunch
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d157'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d158'])]"
    show ep04_elimeet45
    eli "[renpy.substitute(dialogues4['E04ELIMET_d159'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d160'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d161'])]"
    $ setChannelVolume("music", 4, 0.3, 1.0)
    $ playAudio(elizabeth_theme, "music", 4, True, 2.0, 1.0)
    show ep04_elimeet46 at ken_burns_right_to_left with normalfade
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d162'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d163'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d164'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d165'])]"
    show ep04_elimeet47
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d166'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d167'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d168'])]"
    show ep04_elimeet48
    eli "[renpy.substitute(dialogues4['E04ELIMET_d169'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d170'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d171'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d172'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bodyfall, "sfx", 5, False, 0, 0)
    show ep04_elimeet49 at impact_shake with vpunch
    eli "[renpy.substitute(dialogues4['E04ELIMET_d173'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d174'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d175'])]"
    show ep04_elimeet50 with normalfade
    eli "[renpy.substitute(dialogues4['E04ELIMET_d176'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d177'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d178'])]"
    show ep04_elimeet51 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d179'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d180'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d181'])]"
    show ep04_elimeet52 at ken_burns_left_to_right
    eli "[renpy.substitute(dialogues4['E04ELIMET_d182'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d183'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d184'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d185'])]"
    show ep04_elimeet53
    eli "[renpy.substitute(dialogues4['E04ELIMET_d186'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d187'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d188'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d189'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d190'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d191'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.25
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)
    show ep04_elimeet54
    eli "[renpy.substitute(dialogues4['E04ELIMET_d192'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d193'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d194'])]"
    show ep04_elimeet55
    eli "[renpy.substitute(dialogues4['E04ELIMET_d195'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d196'])]"
    show ep04_elimeet56
    eli "[renpy.substitute(dialogues4['E04ELIMET_d197'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d198'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d199'])]"
    show ep04_elimeet57 at ken_burns_top_to_bottom with normalfade
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d200'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d201'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d202'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIMET_d203'])]"
    show ep04_elimeet58
    eli "[renpy.substitute(dialogues4['E04ELIMET_d204'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d205'])]"
    eli "[renpy.substitute(dialogues4['E04ELIMET_d206'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIMET_d207'])]"
    $ show_walkthrough("ep04_elimeetmenu_3")
    menu:
        mc_t "[renpy.substitute(dialogues4['E04ELIMET_d208'])]"
        "Stay and watch":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d209'])]"
            $ ep04_elilook = True
            $ ep04_elistay = True
            show ep04_elimeet60
            $ rm.update("elizabeth", "trust", 4)
            $ check_levels("elizabeth", "trust", 4)
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
            eli "[renpy.substitute(dialogues4['E04ELIMET_d210'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d211'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d212'])]"
            jump ep04_elizabeth_gold
        "Stay but look away":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d213'])]"
            $ ep04_elistay = True
            show ep04_elimeet59
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
            eli "[renpy.substitute(dialogues4['E04ELIMET_d214'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d215'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d216'])]"
            $ setChannelVolume("amb", 1, 0, 1.0)
            jump ep04_elizabeth_gold
        "Leave":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d217'])]"
            show ep04_elimeet61
            $ rm.update("elizabeth", "trust", -4)
            $ check_levels("elizabeth", "trust", -4)
            eli "[renpy.substitute(dialogues4['E04ELIMET_d218'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d219'])]"
            eli "[renpy.substitute(dialogues4['E04ELIMET_d220'])]"
            mc_s "[renpy.substitute(dialogues4['E04ELIMET_d221'])]"
            $ stopAllSubchannels("amb", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.25
            $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
            $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
            $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
            $ playAudio(sfx_fireplace, "amb", 2, True, 1.5, 0)
            show ep04_eligold31 with circlewipe
            mc_t "[renpy.substitute(dialogues4['E04ELIMET_d222'])]"
            mc_t "[renpy.substitute(dialogues4['E04ELIMET_d223'])]"
            mc_t "[renpy.substitute(dialogues4['E04ELIMET_d224'])]"
            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall



label ep04_elizabeth_gold:
    scene eigengrau
    if ep04_elilook:
        show ep04_eligold01 with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ELIGOL_d001'])]"
        mc_t "[renpy.substitute(dialogues4['E04ELIGOL_d002'])]"
        show ep04_eligold02
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d003'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d004'])]"
        $ show_walkthrough("ep04_eligolmenu")
        menu:
            "Look down":
                hide screen walkthrough_screen
                show ep04_eligold03
                $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
                $ playAudio(sfx_piss_fem, "sfx", 1, False, 0, 0)
                $ rm.update("elizabeth", "cor", 2)
                $ check_levels("elizabeth", "cor", 2)
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d005'])]"
                mc_t "[renpy.substitute(dialogues4['E04ELIGOL_d006'])]"
                show ep04_eligold04
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d007'])]"
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d008'])]"
                show ep04_eligold07
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d009'])]"
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d010'])]"
                show ep04_eligold06
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d011'])]"
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d012'])]"
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d013'])]"
                show ep04_eligold08 at ken_burns_bottom_to_top
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d014'])]"
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d015'])]"
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d016'])]"
                $ stopAllSubchannels("sfx", 2.0)
            "Keep looking her":
                hide screen walkthrough_screen
                show ep04_eligold05
                $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
                $ playAudio(sfx_piss_fem, "sfx", 1, False, 0, 0)
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d017'])]"
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d018'])]"
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d019'])]"
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d020'])]"
                show ep04_eligold08 at ken_burns_bottom_to_top
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d021'])]"
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d022'])]"
                eli "[renpy.substitute(dialogues4['E04ELIGOL_d023'])]"
                mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d024'])]"
                $ stopAllSubchannels("sfx", 2.0)
        show ep04_eligold09
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d025'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d026'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d027'])]"
        show ep04_eligold11 at ken_burns_top_to_bottom
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d028'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d029'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d030'])]"
        show ep04_eligold10
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d031'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d032'])]"
        show ep04_eligold12
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d033'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d034'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d035'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d036'])]"
        show ep04_eligold13
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d037'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d038'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d039'])]"
        mc_s "[renpy.substitute(dialogues4['E04ELIGOL_d040'])]"
        show ep04_eligold14
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d041'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d042'])]"
    else:
        pause 1.0
        scene eigengrau with slowfade
        $ setChannelVolume("amb", 1, 0.3, 1.0)
        show ep04_eligold15 with circlewipe
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d043'])]"
        eli "[renpy.substitute(dialogues4['E04ELIGOL_d044'])]"
    jump ep04_elizabeth_kiss



label ep04_elizabeth_kiss:
    show ep04_eligold16
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d002'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d003'])]"
    show ep04_eligold17
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d004'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d006'])]"
    $ stopAllSubchannels("amb", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.25
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    show ep04_eligold18 with circlewipe
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d007'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d008'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d009'])]"
    $ setChannelVolume("music", 3, 0.3, 1.0)
    $ playAudio(elizabeth_theme, "music", 3, True, 2.0, 1.0)
    show ep04_eligold19 with normalfade
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d010'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d012'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d013'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d014'])]"
    show ep04_eligold20
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d015'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d016'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d017'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d018'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d019'])]"
    show ep04_eligold22
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d020'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d021'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d022'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d023'])]"
    show ep04_eligold21
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d024'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d025'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d026'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d027'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d028'])]"
    show ep04_eligold24
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d029'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d030'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d031'])]"
    show ep04_eligold23
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d032'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d033'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d034'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d035'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d036'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d037'])]"
    show ep04_eligold26
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.6)
    $ playAudio(sfx_kiss_one, "sfx", 1, False, 0, 0)
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d038'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d039'])]"
    show ep04_eligold25
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d040'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d041'])]"
    show ep04_eligold27 with normalfade
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d042'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d043'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d044'])]"
    show ep04_eligold28
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d045'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d046'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d047'])]"
    show ep04_eligold29
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d048'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d049'])]"
    eli "[renpy.substitute(dialogues4['E04ELIKSS_d050'])]"
    eli "[renpy.substitute(dialogues4['E04MCNANNO_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04ELIKSS_d051'])]"
    show ep04_eligold30 at subtle_zoom_in with normalfade
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d052'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d053'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d054'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d055'])]"
    $ stopAllSubchannels("music", 2.0)
    $ setChannelVolume("amb", 1, 0, 1.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.3, 1.0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_fireplace, "amb", 2, True, 1.5, 0)
    show ep04_eligold31 with circlewipe
    $ ep04_ach_elizabeth = True
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d056'])]"
    mc_t "[renpy.substitute(dialogues4['E04ELIKSS_d057'])]"
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall



label ep04_isabella_mcroom:
    
    call hideNoise(transition=dissolve)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 1, True, 1.5, 0)
    show ep04_isamcroom01 with circlewipe
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d002'])]"
    $ setChannelVolume("sfx", 1, 0.2)
    $ playAudio(sfx_sighbreathfem, "sfx", 1, False, 0, 0)
    show ep04_isamcroom02
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d003'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d005'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d006'])]"
    $ setChannelVolume("sfx", 2, 0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 2, False, 0, 0)
    $ setChannelVolume("music", 1, 0.4)
    $ playAudio(isabella_serious, "music", 1, True, 4, 0)
    show ep04_isamcroom03 with hpunch
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d008'])]"
    show ep04_isamcroom04
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d010'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d011'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d012'])]"
    show ep04_isamcroom05
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d014'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d015'])]"
    show ep04_isamcroom06
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d016'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d018'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d019'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d020'])]"
    show ep04_isamcroom08
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d021'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d022'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d024'])]"
    show ep04_isamcroom07 at ken_burns_top_to_bottom
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d025'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d026'])]"
    $ stopAudio("music", 1, 2)
    hide ep04_isamcroom07
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d027'])]"
    $ setChannelVolume("music", 3, 0.2, 0)
    $ playAudio(isabella_theme, "music", 3, True, 2.0, 1.0)
    show ep04_isamcroom09 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d028'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d030'])]"
    show ep04_isamcroom10
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d032'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d033'])]"
    show ep04_isamcroom11
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d034'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d035'])]"
    show ep04_isamcroom12
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d036'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d037'])]"
    $ setChannelVolume("music", 3, 0, 2.0) 
    show ep04_isamcroom13 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d038'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d039'])]"
    show ep04_isamcroom14
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d040'])]"
    $ setChannelVolume("sfx", 1, 0.7)
    $ playAudio(sfx_footsteps_bare_wood, "sfx", 1, False, 0, 0)
    show ep04_isamcroom15 with normalfade
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d041'])]"
    show ep04_isamcroom16
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d042'])]"
    $ stopAudio("sfx", 1, 1.5)
    $ setChannelVolume("sfx", 2, 0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 2, False, 0, 0)
    show ep04_isamcroom17
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d043'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d044'])]"
    show ep04_isamcroom18
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d045'])]"
    $ setChannelVolume("sfx", 2, 0.7)
    $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)
    show ep04_isamcroom19 at impact_shake
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d046'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d047'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d048'])]"
    $ setChannelVolume("music", 3, 0.2, 2.0) 
    $ setChannelVolume("sfx", 3, 0.7)
    $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)
    show ep04_isamcroom20 with vpunch
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d049'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d050'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d051'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d052'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d053'])]"
    show ep04_isamcroom21 with normalfade
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d054'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d055'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d056'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d057'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d058'])]"
    show ep04_isamcroom22
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d059'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d060'])]"
    show ep04_isamcroom23
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d061'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d062'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d063'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d064'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d065'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_isamcroom24 with vpunch
    if ep04_nanadad:
        isa "[renpy.substitute(dialogues4['E04ISAMCR_d066'])]"
    else:
        isa "[renpy.substitute(dialogues4['E04ISAMCR_d067'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d068'])]"
    if ep04_nanadad:
        isa "[renpy.substitute(dialogues4['E04ISAMCR_d069'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d070'])]"
        isa "[renpy.substitute(dialogues4['E04ISAMCR_d071'])]"
    else:
        isa "[renpy.substitute(dialogues4['E04ISAMCR_d072'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d073'])]"
        isa "[renpy.substitute(dialogues4['E04ISAMCR_d074'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d075'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d076'])]"
    show ep04_isamcroom25
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d077'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d078'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMCR_d079'])]"
    $ show_walkthrough("ep04_isamcmenu")
    menu:
        "Let her stay":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d080'])]"
            jump ep04_isabella_nobra
        "Send her away":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d081'])]"
            show ep04_isamcroom26
            $ rm.update("isabella", "trust", -2)
            $ check_levels("isabella", "trust", -2)
            isa "[renpy.substitute(dialogues4['E04ISAMCR_d082'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d083'])]"
            isa "[renpy.substitute(dialogues4['E04ISAMCR_d084'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d085'])]"
            show ep04_isamcroom27
            isa "[renpy.substitute(dialogues4['E04ISAMCR_d086'])]"
            isa "[renpy.substitute(dialogues4['E04ISAMCR_d087'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISAMCR_d088'])]"
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.25
            show ep04_isamcroom28
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d089'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d090'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d091'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d092'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d093'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d094'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISAMCR_d095'])]"
            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall



label ep04_isabella_nobra:
    scene eigengrau
    show ep04_isanobra01
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d002'])]"
    show ep04_isanobra02
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d003'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d004'])]"
    show ep04_isanobra03
    $ rm.update("isabella", "trust", 2)
    $ check_levels("isabella", "trust", 2)
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d005'])]"
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d006'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d007'])]"
    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(isabella_sexy, "music", 1, True, 2.0, 1.0)
    show ep04_isanobra04
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d008'])]"
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d009'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d010'])]"
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d011'])]"
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d012'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d013'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d014'])]"
    show ep04_isanobra05
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d015'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d016'])]"
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d018'])]"
    isa "[renpy.substitute(dialogues4['E04ISANOBR_d019'])]"
    $ show_walkthrough("ep04_isanobramenu")
    menu:
        "Help her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d020'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d021'])]"
            show ep04_isanobra06
            $ rm.update("isabella", "cor", 2)
            $ check_levels("isabella", "cor", 2)
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d022'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d023'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d024'])]"
            show ep04_isanobra07
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d025'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d026'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d027'])]"
            show ep04_isanobra08
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d028'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d029'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d030'])]"
            mc_t "[renpy.substitute(dialogues4['E04ISANOBR_d031'])]"
            show ep04_isanobra09
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d032'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d033'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d034'])]"
            scene eigengrau with slowfade
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d035'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d036'])]"
            show ep04_isanobra13
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d037'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d038'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d039'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d040'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d041'])]"
            show ep04_isanobra14
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d042'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d043'])]"
            show ep04_isanobra15
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d044'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d045'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d046'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d047'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d048'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d049'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d050'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d051'])]"
            show ep04_isanobra16
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d052'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d053'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d054'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d055'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d056'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d057'])]"
            show ep04_isanobra17
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d058'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d059'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d060'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d061'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d062'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d063'])]"
            scene eigengrau with slowfade
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d064'])]"
            show ep04_isanobra10
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d065'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d066'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d067'])]"
            show ep04_isanobra11
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d068'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d069'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d070'])]"
            show ep04_isanobra12
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d071'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d072'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d073'])]"
        "Dont help her":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d074'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d075'])]"
            show ep04_isanobra07
            $ rm.update("isabella", "trust", 1)
            $ check_levels("isabella", "trust", 1)
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d076'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d077'])]"
            scene eigengrau with slowfade
            show ep04_isanobra10
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d078'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d079'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d080'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d081'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d082'])]"
            scene eigengrau with slowfade
            show ep04_isanobra11
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d083'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d084'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d085'])]"
            show ep04_isanobra12
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d086'])]"
            mc_s "[renpy.substitute(dialogues4['E04ISANOBR_d087'])]"
            isa "[renpy.substitute(dialogues4['E04ISANOBR_d088'])]"
    jump ep04_isabella_sleepnight



label ep04_isabella_sleepnight:
    show ep04_isanight01
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d001'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d002'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d003'])]"
    show ep04_isanight02 at ken_burns_top_to_bottom with vpunch
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d004'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d005'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d006'])]"
    show ep04_isanight03
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d007'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d008'])]"
    show ep04_isanight04
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d009'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d010'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d011'])]"
    show ep04_isanight05 at ken_burns_bottom_to_top
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d012'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d013'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d014'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d015'])]"
    show ep04_isanight07
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d016'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d017'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d018'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d019'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d020'])]"
    show ep04_isanight06 at ken_burns_bottom_to_top
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d021'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d022'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d023'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d024'])]"
    show ep04_isanight08
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d025'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d026'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d027'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d028'])]"
    show ep04_isanight09 at ken_burns_right_to_left
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d029'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d030'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d031'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d032'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 5, True, 1.5, 0)
    show ep04_isanight10
    mc_t "[renpy.substitute(dialogues4['E04ISASLNIT_d033'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d034'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d035'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d036'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d037'])]"
    show ep04_isanight11
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d038'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d039'])]"
    show ep04_isanight12
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d040'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d041'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d042'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d043'])]"
    show ep04_isanight13
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d044'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d045'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d046'])]"
    show ep04_isanight14
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d047'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d048'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d049'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d050'])]"
    mc_s "[renpy.substitute(dialogues4['E04ISASLNIT_d051'])]"
    isa "[renpy.substitute(dialogues4['E04ISASLNIT_d052'])]"
    $ setChannelVolume("sfx", 3, 0.7)
    $ playAudio(sfx_bedmove, "sfx", 3, False, 0, 0)
    show ep04_isanight15 with normalfade
    mc_t "[renpy.substitute(dialogues4['E04ISASLNIT_d053'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISASLNIT_d054'])]"
    $ setChannelVolume("amb", 5, 0, 1.0)
    if ep04_mcdrunk:
        jump ep04_isabella_dream
    else:
        jump ep04_isabella_masturbation



label ep04_isabella_dream:
    scene eigengrau with slowfade
    pause 1.0
    $ setChannelVolume("amb", 5, 0.3, 1.0)
    show vignette zorder 1.0 at pov_die
    show ep04_isanight24
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d001'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d002'])]"
    isa "[renpy.substitute(dialogues4['E04ISADR_d003'])]"
    $ setChannelVolume("sfx", 1, 0.6)
    $ playAudio(sfx_moan_breath, "sfx", 1, False, 0, 0)
    show ep04_isanight25
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d004'])]"
    isa "[renpy.substitute(dialogues4['E04ISADR_d005'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d006'])]"
    isa "[renpy.substitute(dialogues4['E04ISADR_d007'])]"
    $ setChannelVolume("sfx", 2, 0.4)
    $ playAudio(sfx_moan_breath2, "sfx", 2, False, 0, 0)
    show ep04_isanight26
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d008'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d009'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d010'])]"
    $ stopAllSubchannels("amb", 2.0)
    scene eigengrau with clouds
    hide vignette
    if ep04_isatruth:
        $ setChannelVolume(channel="amb", subchannel=8, volume=0.3)
        $ playAudio(sfx_wind_pool, "amb", 8, True, 1.5, 0)
        $ setChannelVolume("music", 1, 0.3, 1.0)
        $ playAudio(heaven_theme, "music", 1, True, 2.0, 1.0)
        show ep04_isaheaven01 at focus_pulse with clouds
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d011'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d012'])]"
        show ep04_isaheaven02 at ken_burns_left_to_right with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d013'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d014'])]"
        show ep04_isaheaven03 at ken_burns_bottom_to_top with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d015'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d016'])]"
        $ setChannelVolume("sfx", 1, 0.8)
        $ playAudio(sfx_bed_creaking, "sfx", 1, False, 0, 0)
        show ep04_isaheaven04 with vpunch
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d017'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d018'])]"
        $ setChannelVolume("sfx", 2, 0.8)
        $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
        show ep04_isaheaven05 with normalfade
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d019'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d020'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d021'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d022'])]"
        show ep04_isaheaven06 with normalfade
        isa "[renpy.substitute(dialogues4['E04ISADR_d023'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d024'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d025'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d026'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d027'])]"
        show ep04_isaheaven07 at subtle_zoom_in
        isa "[renpy.substitute(dialogues4['E04ISADR_d028'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d029'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d030'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d031'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d032'])]"
        $ setChannelVolume("sfx", 3, 0.4)
        $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
        show ep04_isaheaven08 with vpunch
        isa "[renpy.substitute(dialogues4['E04ISADR_d033'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d034'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d035'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d036'])]"
        show ep04_isaheaven09
        isa "[renpy.substitute(dialogues4['E04ISADR_d037'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d038'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d039'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d040'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d041'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d042'])]"
        scene white with flash
        $ setChannelVolume("sfx", 4, 0.4)
        $ playAudio(sfx_wings, "sfx", 4, False, 0, 0)
        show ep04_isaheaven10 at subtle_zoom_out with slowflash
        isa "[renpy.substitute(dialogues4['E04ISADR_d043'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d044'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d045'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d046'])]"
        show ep04_isaheaven11
        isa "[renpy.substitute(dialogues4['E04ISADR_d047'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d048'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d049'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d050'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d051'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d052'])]"
        scene white with flash
        $ setChannelVolume("sfx", 4, 0.4)
        $ playAudio(sfx_wings, "sfx", 4, False, 0, 0)
        show ep04_isaheaven12 with slowflash
        isa "[renpy.substitute(dialogues4['E04ISADR_d053'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d054'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d055'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d056'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d057'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d058'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d059'])]"
        show ep04_isaheaven13 with slowflash
        isa "[renpy.substitute(dialogues4['E04ISADR_d060'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d061'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d062'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d063'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d064'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d065'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d066'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d067'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d068'])]"
        show ep04_isaheaven14 at ken_burns_right_to_left with slowflash
        isa "[renpy.substitute(dialogues4['E04ISADR_d069'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d070'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d071'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d072'])]"
        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("music", 2.0)
    else:
        $ setChannelVolume(channel="amb", subchannel=8, volume=0.3)
        $ playAudio(sfx_fireplace, "amb", 8, True, 1.5, 0)
        $ setChannelVolume("music", 1, 0.3, 1.0)
        $ playAudio(hell_theme, "music", 1, True, 2.0, 1.0)
        show ep04_isahell01 at focus_pulse with clouds
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d073'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d074'])]"
        show ep04_isahell02 at ken_burns_bottom_to_top with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d075'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d076'])]"
        $ setChannelVolume("sfx", 3, 0.4)
        $ playAudio(sfx_bed_creaking, "sfx", 3, False, 0, 0)
        show ep04_isahell03 at vpunch with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d077'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d078'])]"
        $ setChannelVolume("sfx", 3, 0.25)
        $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)
        show ep04_isahell04 at ken_burns_bottom_to_top with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d079'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d080'])]"
        $ setChannelVolume("sfx", 4, 0.5)
        $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)
        show ep04_isahell05 at vpunch, ken_burns_left_to_right with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d081'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d082'])]"
        show ep04_isahell06 at ken_burns_bottom_to_top with normalfade
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d083'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d019'])]"
        show ep04_isahell07 with vpunch
        isa "[renpy.substitute(dialogues4['E04ISADR_d086'])]"
        mc_t "[renpy.substitute(dialogues4['E04ISADR_d085'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d087'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d088'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d089'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d090'])]"
        show ep04_isahell08
        isa "[renpy.substitute(dialogues4['E04ISADR_d091'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d092'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d093'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d094'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d068'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d096'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d097'])]"
        scene eigengrau with normalfade
        $ setChannelVolume("sfx", 1, 0.5)
        $ playAudio(sfx_wings_evil, "sfx", 1, False, 0, 0)
        show ep04_isahell09 at subtle_zoom_out with slowfade
        isa "[renpy.substitute(dialogues4['E04ISADR_d098'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d099'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d100'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d101'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d102'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d103'])]"
        show ep04_isahell10
        isa "[renpy.substitute(dialogues4['E04ISADR_d104'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d105'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d106'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d107'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d108'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d109'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d110'])]"
        scene eigengrau with normalfade
        $ setChannelVolume("sfx", 1, 0.5)
        $ playAudio(sfx_wings_evil, "sfx", 1, False, 0, 0)
        show ep04_isahell11 with slowfade
        isa "[renpy.substitute(dialogues4['E04ISADR_d111'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d112'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d113'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d114'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d103'])]"
        show ep04_isahell12 with slowfade
        isa "[renpy.substitute(dialogues4['E04ISADR_d116'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d117'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d068'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d119'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d120'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d121'])]"
        show ep04_isahell13 with slowfade
        isa "[renpy.substitute(dialogues4['E04ISADR_d122'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d123'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d124'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d125'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d126'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d127'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d128'])]"
        mc_s "[renpy.substitute(dialogues4['E04ISADR_d129'])]"
        show ep04_isahell14 at ken_burns_right_to_left with slowfade
        isa "[renpy.substitute(dialogues4['E04ISADR_d130'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d131'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d132'])]"
        isa "[renpy.substitute(dialogues4['E04ISADR_d133'])]"
        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("music", 2.0)
    scene eigengrau with clouds_inverse
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 5, True, 1.5, 0)
    show ep04_isanight27 at vpunch with clouds_inverse
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d134'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d135'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d136'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d137'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d138'])]"
    mc_t "[renpy.substitute(dialogues4['E04ISADR_d139'])]"
    $ ep04_ach_isabella2 = True
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall



label ep04_isabella_masturbation:
    scene eigengrau with slowfade
    pause 1.0
    $ setChannelVolume("amb", 5, 0.3, 1.0)
    show ep04_isanight16 at ken_burns_right_to_left with circlewipe
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d001'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d002'])]"
    show ep04_isanight17
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d003'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d004'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d005'])]"
    show ep04_isanight18
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d006'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d007'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d008'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d009'])]"
    show ep04_isanight19
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d010'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d011'])]"
    show ep04_isanight20 at ken_burns_bottom_to_top
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d012'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d013'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d014'])]"
    show ep04_isanight21
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d015'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d016'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d017'])]"
    show ep04_isanight22 with normalfade
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d018'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d019'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d020'])]"
    show ep04_isanight23
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d021'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d022'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d023'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d024'])]"
    show ep04_isanight26
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d025'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d026'])]"
    show ep04_isamast01
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d027'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d028'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d029'])]"
    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(isabella_sexy, "music", 1, True, 2.0, 1.0)
    show ep04_isamast02
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d030'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d031'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d032'])]"
    show ep04_isamast03
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d033'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d034'])]"
    show ep04_isamast04
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d035'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d036'])]"
    show ep04_isamast05
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d037'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d038'])]"
    $ setChannelVolume("sfx", 1, 0.4)
    $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)
    show ep04_isamast06 with hpunch
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d039'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d040'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d041'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d042'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d043'])]"
    show ep04_isamast07
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d044'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d045'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d046'])]"
    $ setChannelVolume("sfx", 2, 0.4)
    $ playAudio(sfx_femheavybreath, "sfx", 2, False, 0, 0)
    show ep04_isamast08
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d047'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d048'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d049'])]"
    show ep04_isamast09
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d050'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d051'])]"
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d052'])]"
    $ stopAudio("sfx", 2, 1)
    $ setChannelVolume("sfx", 3, 0.8)
    $ playAudio(sfx_moan_breath, "sfx", 3, False, 0, 0)
    show ep04_isamast10
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d053'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d054'])]"
    $ setChannelVolume("sfx", 4, 0.8)
    $ playAudio(sfx_mast_fem, "sfx", 4, False, 0, 0)
    show ep04_isamasturbation01 with normalfade
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d055'])]"
    show ep04_isamasturbation02
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d056'])]"
    show ep04_isamasturbation03
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d057'])]"
    show ep04_isamasturbation04
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d058'])]"
    show ep04_isamasturbation05
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d059'])]"
    $ setChannelVolume("sfx", 1, 0.25)
    $ playAudio(sfx_madbreathxxx, "sfx", 1, False, 0, 0)
    show ep04_isamastur201 with normalfade
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d060'])]"
    show ep04_isamastur202
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d061'])]"
    show ep04_isamastur203
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d062'])]"
    show ep04_isamastur204
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d063'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d064'])]"
    show ep04_isamastur205
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d065'])]"
    show ep04_isamastur206
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d066'])]"
    show ep04_isamastur207
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d067'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d068'])]"
    show ep04_isamastur208
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d069'])]"
    show ep04_isamastur209
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d070'])]"
    show ep04_isamastur210
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d071'])]"
    show ep04_isamastur211
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d072'])]"
    show ep04_isamastur212
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d073'])]"
    show ep04_isamast11 with normalfade
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d074'])]"
    $ setChannelVolume("sfx", 1, 0.4)
    $ playAudio(sfx_madmoan2xxx, "sfx", 1, False, 0, 0)
    show white zorder 1.0 at ejaculation_flash
    show ep04_isamast12 at impact_shake with flash
    isa "[renpy.substitute(dialogues4['E04ISAMAST_d075'])]"
    $ stopAllSubchannels("music", 2.0)
    show ep04_isamast13
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d076'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d077'])]"
    show ep04_isamast14
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d078'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d079'])]"
    show ep04_isamast15
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d080'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d081'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d082'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d083'])]"
    show ep04_isamast16
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d084'])]"
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d085'])]"
    show ep04_isamast17 at ken_burns_left_to_right
    isa_t "[renpy.substitute(dialogues4['E04ISAMAST_d086'])]"
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall



label ep04_pazcall:
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.15)
    $ playAudio(sfx_morning, "amb", 1, True, 1.5, 0)
    $ setChannelVolume("music", 1, 0, 1.0)
    $ playAudio(mc_theme, "music", 1, True, 2.0, 1.0)
    show ep04_pazwake01 at subtle_zoom_out with circlewipe
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    pa_s "[renpy.substitute(dialogues4['E04PZCAL_d001'])]"
    $ setChannelVolume("amb", 1, 0.05, 1.0)
    show ep04_pazwake02 with normalfade
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d002'])]"
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d003'])]"
    show ep04_pazwake03
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d004'])]"
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d005'])]"
    show ep04_pazwake04
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d006'])]"
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d007'])]"
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d008'])]"
    show ep04_pazwake05 at ken_burns_corner_to_corner4
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d009'])]"
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d010'])]"
    pa_t "[renpy.substitute(dialogues4['E04PZCAL_d011'])]"
    $ stopAllSubchannels("amb", 2.0)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_japanday_cross, "amb", 2, True, 1.5, 0)
    show ep04_mcmorn01 with lines
    show outside_home_for_work zorder 2 with dissolve
    pause 4
    hide outside_home_for_work with dissolve
    $ setChannelVolume("music", 1, 0.3, 2)
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d012'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d013'])]"
    show ep04_mcmorn02
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d014'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d015'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d016'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d017'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d018'])]"
    show ep04_mcmorn03
    mc_t "[renpy.substitute(dialogues4['E04PZCAL_d019'])]"
    nvl clear
    jump ep04_paz_sms_5
    #SMS



label ep04_pazcall_post:
    show ep04_mcmorn03 at focus_shift
    mc_t "[renpy.substitute(dialogues4['E04PZPST_d001'])]"
    show ep04_mcmorn04 with slowfade
    mc_t "[renpy.substitute(dialogues4['E04PZPST_d002'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZPST_d003'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZPST_d004'])]"
    mc_t "[renpy.substitute(dialogues4['E04PZPST_d005'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_antonella_return



label ep04_antonella_return:
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.3)
    $ playAudio(sfx_morning_late, "amb", 3, True, 1.5, 0)
    show ep04_antoshow01 at dramatic_focus_out
    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(antonella_theme, "music", 1, True, 2.0, 1.0)
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d001'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d002'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d003'])]"
    ## save notification
    if htl_episodes == 4.2:
        $ show_custom_notification("save_tip")
    else:
        pass
    $ setChannelVolume("amb", 3, 0.1, 1.0)
    show ep04_antoshow02 at ken_burns_right_to_left
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d004'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d005'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d006'])]"
    show ep04_antoshow03 at subtle_zoom_out
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d007'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d008'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d009'])]"
    show ep04_antoshow04 at ken_burns_corner_to_corner4
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d010'])]"
    $ setChannelVolume("sfx", 2, 0.3)
    $ playAudio(sfx_phonering, "sfx", 2, True, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d011'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d012'])]"
    $ stopAudio("sfx", 2, 1)
    show ep04_antoshow05 with normalfade
    anto "[renpy.substitute(dialogues4['E04ANR_d013'])]"
    $ rm.set_knows("antonella", True)
    hir "[renpy.substitute(dialogues4['E04ANR_d014'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d015'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d016'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d017'])]"
    show ep04_antoshow06 with normalfade
    hir "[renpy.substitute(dialogues4['E04ANR_d018'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d019'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d020'])]"
    show ep04_antoshow07
    hir "[renpy.substitute(dialogues4['E04ANR_d021'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d022'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d023'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d024'])]"
    show ep04_antoshow08 at subtle_zoom_in with slowfade
    anto_t "[renpy.substitute(dialogues4['E04ANR_d025'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d026'])]"
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d027'])]"
    ed "[renpy.substitute(dialogues4['E04ANR_d028'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d029'])]"
    anto_t "[renpy.substitute(dialogues4['E04ANR_d030'])]"
    scene eigengrau with slowfade
    show ep04_antoshow09 at subtle_zoom_out
    anto_t "[renpy.substitute(dialogues4['E04ANR_d031'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d032'])]"
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d033'])]"
    show ep04_antoshow10 with normalfade
    anto "[renpy.substitute(dialogues4['E04ANR_d034'])]"
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "[renpy.substitute(dialogues4['E04ANR_d035'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d036'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=6, volume=0.1)
    $ playAudio(sfx_airportwalla, "amb", 6, True, 1.5, 0)
    $ setChannelVolume(channel="amb", subchannel=7, volume=0.3)
    $ playAudio(sfx_earlypast, "amb", 7, True, 1.5, 0)
    show ep04_antoshow11 with circlewipe
    anto "[renpy.substitute(dialogues4['E04ANR_d037'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d038'])]"
    show ep04_antoshow12 at ken_burns_right_to_left
    hir "[renpy.substitute(dialogues4['E04ANR_d039'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d040'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d041'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d042'])]"
    $ rm.set_knows("antonella", True)
    show ep04_antoshow13 with normalfade
    anto "[renpy.substitute(dialogues4['E04ANR_d043'])]"
    hir "[renpy.substitute(dialogues4['E04ANR_d044'])]"
    anto "[renpy.substitute(dialogues4['E04ANR_d045'])]"
    #-- End Episode 4
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
    call hideNoise(transition=dissolve)
    pause 2.0
    if htl_episodes == 4.2:
        return
    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep05_title

