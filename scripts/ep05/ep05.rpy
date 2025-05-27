label ep05_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ persistent.act2_play = True
    $ renpy.block_rollback()
    $ renpy.save_persistent()
    jump ep05_intro

## -- INTRO COFFEE
label ep05_intro:
    $ config.rollback_enabled = True
    scene eigengrau
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)
    show ep05_coffee01 at ken_burns_right_to_left with slowfade
    show screen stats_button
    show screen walkthrough_icon
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d003'])]"
    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_kitchen_rumm, "sfx", 1, False, 1, 0)
    hide ep05_coffee01
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d004'])]"
    $ stopAudio("sfx", 1, 0.5)
    $ setChannelVolume("sfx", 2, 0.7, 0)
    $ playAudio(sfx_coffee_mkr, "sfx", 2, False, 1, 0)
    show ep05_coffee02
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d006'])]"
    $ stopAudio("sfx", 2, 1)
    show ep05_coffee03 at ken_burns_corner_to_corner3 with slowfade
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d007'])]"
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d008'])]"
    mc_t "[renpy.substitute(dialogues5['E05INTRO_d009'])]"
    $ stopAllSubchannels("amb", 2.0)
    #######FIX STRIKES_BUG
    if ep03_amberstrike or ep03_amberangry:
        $ ss.add("amber", "strike")
    else:
        pass
    ########
    jump ep05_madyoga

label ep05_madyoga:
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.4, 0)
    $ setChannelVolume("amb", 2, 0.5, 0)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 1, 0)
    $ playAudio(sfx_wind_pool, "amb", 2, True, 1, 0)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(madison_nan_theme, "music", 1, True, 4, 0)
    show ep05_madintro01 at ken_burns_corner_to_corner4 with circlewipe
    mad "[renpy.substitute(dialogues5['E05MADYOG_d001'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d002'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d003'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d004'])]"
    show ep05_madintro02 at ken_burns_left_to_right
    mad "[renpy.substitute(dialogues5['E05MADYOG_d005'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d006'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d007'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d008'])]"
    show ep05_madintro03 at subtle_zoom_out
    mad "[renpy.substitute(dialogues5['E05MADYOG_d009'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d010'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d011'])]"
    show ep05_madintro04 with vpunch
    mad "[renpy.substitute(dialogues5['E05MADYOG_d012'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d013'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d014'])]"
    show ep05_madintro05 with normalfade
    mad "[renpy.substitute(dialogues5['E05MADYOG_d015'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d016'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d017'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d018'])]"
    show ep05_madintro06 at dramatic_focus with normalfade
    nana "[renpy.substitute(dialogues5['E05MADYOG_d019'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d020'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d021'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d022'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d023'])]"
    show ep05_madintro07 with hpunch
    mad "[renpy.substitute(dialogues5['E05MADYOG_d024'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d025'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d026'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d027'])]"
    show ep05_madintro08
    mad "[renpy.substitute(dialogues5['E05MADYOG_d028'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d029'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d030'])]"
    show ep05_madintro09 with normalfade
    mad "[renpy.substitute(dialogues5['E05MADYOG_d031'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d032'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d033'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d034'])]"
    show ep05_madintro10 at ken_burns_left_to_right with normalfade
    mad "[renpy.substitute(dialogues5['E05MADYOG_d035'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d036'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d037'])]"
    show ep05_madintro11 at camera_zoom with vpunch
    nana "[renpy.substitute(dialogues5['E05MADYOG_d038'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d039'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d040'])]"
    show ep05_madintro12 at ken_burns_corner_to_corner2
    mad "[renpy.substitute(dialogues5['E05MADYOG_d041'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d042'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d043'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d044'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d045'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d046'])]"
    show ep05_madintro13 with hpunch
    nana "[renpy.substitute(dialogues5['E05MADYOG_d047'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d048'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d049'])]"
    show ep05_madintro14 with normalfade
    mad "[renpy.substitute(dialogues5['E05MADYOG_d050'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d051'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d052'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d053'])]"
    show ep05_madintro15
    nana "[renpy.substitute(dialogues5['E05MADYOG_d054'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d055'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d056'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d057'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d058'])]"
    show ep05_madintro16
    nana "[renpy.substitute(dialogues5['E05MADYOG_d059'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d060'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d061'])]"
    show ep05_madintro17 at subtle_zoom_out
    mad "[renpy.substitute(dialogues5['E05MADYOG_d062'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d063'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d064'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d065'])]"
    show ep05_madintro18 at dramatic_focus_out with slowfade
    if ep04_madstory and ep04_madnanastory:
        mc_t "[renpy.substitute(dialogues5['E05MADYOG_d066'])]"
        mc_t "[renpy.substitute(dialogues5['E05MADYOG_d067'])]"
        mc_t "[renpy.substitute(dialogues5['E05MADYOG_d068'])]"
        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("sfx", 2.0)
        $ stopAllSubchannels("music", 2.0)
        jump ep05_ambercof
    else:
        mc_t "[renpy.substitute(dialogues5['E05MADYOG_d069'])]"
        mc_t "[renpy.substitute(dialogues5['E05MADYOG_d070'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d071'])]"
        pass
    show ep05_madintro19 with hpunch
    nana "[renpy.substitute(dialogues5['E05MADYOG_d072'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d073'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d074'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d075'])]"
    show ep05_madintro20
    nana "[renpy.substitute(dialogues5['E05MADYOG_d076'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d077'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d078'])]"
    show ep05_madintro21
    mad "[renpy.substitute(dialogues5['E05MADYOG_d079'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d080'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d081'])]"
    show ep05_madintro22
    mad "[renpy.substitute(dialogues5['E05MADYOG_d082'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d083'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d084'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep05_madintro23 with circlewipe
    mad "[renpy.substitute(dialogues5['E05MADYOG_d085'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d086'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d087'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d088'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d089'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d090'])]"
    show ep05_madintro24
    mad "[renpy.substitute(dialogues5['E05MADYOG_d091'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d092'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d093'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d094'])]"
    show ep05_madintro25
    mad "[renpy.substitute(dialogues5['E05MADYOG_d095'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d096'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d097'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d098'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d099'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d100'])]"
    if not ep04_madstory:
        show ep05_madintro26
        mad "[renpy.substitute(dialogues5['E05MADYOG_d101'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d102'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d103'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d104'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d105'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d106'])]"
        show ep05_madintro27
        mad "[renpy.substitute(dialogues5['E05MADYOG_d107'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d108'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d109'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d110'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d111'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d112'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d113'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d114'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d115'])]"
        show ep05_madintro28
        mad "[renpy.substitute(dialogues5['E05MADYOG_d116'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d117'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d118'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d119'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d120'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d121'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d122'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d123'])]"
        show ep05_madintro29
        mad "[renpy.substitute(dialogues5['E05MADYOG_d124'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d125'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d126'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d127'])]"
    else:
        pass
    scene eigengrau
    $ setChannelVolume("music", 2, 0.4, 0)
    $ playAudio(madison_theme, "music", 2, True, 4, 0)
    show ep05_madintro30 with slowfade
    mad "[renpy.substitute(dialogues5['E05MADYOG_d128'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d129'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d130'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d131'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d132'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d133'])]"
    show ep05_madintro31
    mad "[renpy.substitute(dialogues5['E05MADYOG_d134'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d135'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d136'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d137'])]"
    show ep05_madintro32
    mad "[renpy.substitute(dialogues5['E05MADYOG_d138'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d139'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d140'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d141'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d142'])]"
    show ep05_madintro33
    mad "[renpy.substitute(dialogues5['E05MADYOG_d143'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d144'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d145'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d146'])]"
    show ep05_madintro34
    mad "[renpy.substitute(dialogues5['E05MADYOG_d147'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d148'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d149'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d150'])]"
    show ep05_madintro35
    mad "[renpy.substitute(dialogues5['E05MADYOG_d151'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d152'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d153'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d154'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d155'])]"
    show ep05_madintro36
    mad "[renpy.substitute(dialogues5['E05MADYOG_d156'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d157'])]"
    show ep05_madintro37
    mad "[renpy.substitute(dialogues5['E05MADYOG_d158'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d159'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d160'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d161'])]"
    show ep05_madintro38
    mad "[renpy.substitute(dialogues5['E05MADYOG_d162'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d163'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d164'])]"
    show ep05_madintro39
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d165'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d166'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d167'])]"
    show ep05_madintro40
    mad "[renpy.substitute(dialogues5['E05MADYOG_d168'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d169'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d170'])]"
    show ep05_madintro41
    if ep04_mcdrunk:
        mad "[renpy.substitute(dialogues5['E05MADYOG_d000'])]"
    else:
        mad "[renpy.substitute(dialogues5['E05MADYOG_d171'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d172'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d173'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d174'])]"
    show ep05_madintro42
    mad "[renpy.substitute(dialogues5['E05MADYOG_d175'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d176'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d177'])]"
    show ep05_madintro43
    nana "[renpy.substitute(dialogues5['E05MADYOG_d178'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d179'])]"
    nana "[renpy.substitute(dialogues5['E05MADYOG_d180'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d181'])]"
    show ep05_madintro44 at ken_burns_left_to_right with slowfade
    mad "[renpy.substitute(dialogues5['E05MADYOG_d182'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d183'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d184'])]"
    if ep04_madnight == 0:
        show ep05_madintro45 with slowfade
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d185'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d186'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d187'])]"
        show ep05_madintro46 at photo_effect with flash
        show photo_flash with dissolve
        mad "[renpy.substitute(dialogues5['E05MADYOG_d188'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d189'])]"
        mc_s "[renpy.substitute(dialogues5['E05MADYOG_d190'])]"
        show ep05_madintro47
        mad "[renpy.substitute(dialogues5['E05MADYOG_d191'])]"
        mad "[renpy.substitute(dialogues5['E05MADYOG_d192'])]"
    else:
        pass
    show ep05_madintro48
    if ep04_madnight == 0:
        mad "[renpy.substitute(dialogues5['E05MADYOG_d193'])]"
    else:
        mad "[renpy.substitute(dialogues5['E05MADYOG_d196'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d194'])]"
    mad "[renpy.substitute(dialogues5['E05MADYOG_d195'])]"
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("sfx", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep05_ambercof

label ep05_ambercof:
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)
    show ep05_amberintro01 at dramatic_focus with circlewipe
    $ setChannelVolume("sfx", 8, 0.4, 0)
    $ playAudio(sfx_yawnfem, "sfx", 8, False, 1, 0)
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d002'])]"
    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 1, False, 1, 0)
    show ep05_amberintro02 at zoom_out
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d003'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d004'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d005'])]"
    $ stopAudio("sfx", 1, 1)
    if ss.get("amber", "strike") > 0:
        show ep05_amberintro03
        mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d006'])]"
        mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d007'])]"
        $ show_walkthrough("ep05_ambcofmenu")
        menu:
            mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d008'])]"
            "Apologize to her":
                hide screen walkthrough_screen
                show ep05_amberintro04
                mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d009'])]"
                amb "[renpy.substitute(dialogues5['E05AMBERCOF_d010'])]"
                mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d011'])]"
                show ep05_amberintro05
                mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d012'])]"
                amb "[renpy.substitute(dialogues5['E05AMBERCOF_d013'])]"
                amb "[renpy.substitute(dialogues5['E05AMBERCOF_d014'])]"
                $ rm.update("amber", "trust",4)
                $ check_levels("amber", "trust", 4)
                $ ss.set("amber", "strike", ss.get("amber", "strike") - 1)
                pass
            "Don't apologize to her":
                hide screen walkthrough_screen
                show ep05_amberintro06
                mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d015'])]"
                amb "[renpy.substitute(dialogues5['E05AMBERCOF_d016'])]"
                mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d017'])]"
                $ rm.update("amber", "trust", -10)
                $ check_levels("amber", "trust", -10)
                $ setChannelVolume("sfx", 2, 0.7, 0)
                $ playAudio(sfx_coffee_mkr, "sfx", 2, False, 1, 0)
                show ep05_amberintro07
                mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d018'])]"
                isa "[renpy.substitute(dialogues5['E05AMBERCOF_d019'])]"
                mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d020'])]"
                $ ep05_ambignore = True
                $ stopAllSubchannels("sfx", 2.0)
                $ stopAllSubchannels("amb", 2.0)
                jump ep05_isacos
    else:
        pass
    show ep05_amberintro08
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d021'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d022'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d023'])]"
    $ setChannelVolume("sfx", 2, 0.7, 0)
    $ playAudio(sfx_coffee_mkr, "sfx", 2, False, 1, 0)
    show ep05_amberintro09
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d024'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d025'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d026'])]"
    show ep05_amberintro10
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d027'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d028'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d029'])]"
    $ stopAudio("sfx", 2, 2)
    show ep05_amberintro11
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d030'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d031'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d032'])]"
    $ setChannelVolume("sfx", 3, 0.7, 0)
    $ playAudio(sfx_glass_ontable, "sfx", 3, False, 0, 0)
    show ep05_amberintro12
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d033'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d034'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d035'])]"
    $ stopAudio("sfx", 3, 2)
    $ setChannelVolume("music", 1, 0.2, 0)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 4, 0)
    show ep05_amberintro13
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d036'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d037'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d038'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d015'])]"
    show ep05_amberintro14 with hpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d040'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d041'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d042'])]"
    show ep05_amberintro15
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d043'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d044'])]"
    show ep05_amberintro16
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d046'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d047'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d048'])]"
    show ep05_amberintro17 with vpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d049'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d050'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d051'])]"
    show ep05_amberintro24
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d052'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d053'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d054'])]"
    $ show_walkthrough("ep05_ambsexmenu")
    menu:
        mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d055'])]"
        "Accept her advances":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d056'])]"
            amb "[renpy.substitute(dialogues5['E05AMBERCOF_d057'])]"
            mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d058'])]"
            $ rm.update("amber", "cor", 4)
            $ check_levels("amber", "cor", 4)
            pass
        "Reject her":
            hide screen walkthrough_screen
            show ep05_amberintro18
            mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d059'])]"
            mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d060'])]"
            amb "[renpy.substitute(dialogues5['E05AMBERCOF_d061'])]"
            $ rm.update("amber", "cor", -4)
            $ check_levels("amber", "cor", -4)
            $ stopAllSubchannels("music", 2.0)
            show ep05_amberintro07
            amb "[renpy.substitute(dialogues5['E05AMBERCOF_d062'])]"
            mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d063'])]"
            isa "[renpy.substitute(dialogues5['E05AMBERCOF_d019'])]"
            $ ep05_ambignore = True
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("sfx", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep05_isacos
    show ep05_amberintro19 with hpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d065'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d066'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d067'])]"
    show ep05_amberintro20 at ken_burns_top_to_bottom
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d068'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d069'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d070'])]"
    show ep05_amberintro21
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d071'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d015'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d073'])]"
    show ep05_amberintro22 with hpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d074'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d075'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d076'])]"
    scene eigengrau with slowfade
    show ep05_amberintro24 with circlewipe
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d077'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d078'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d079'])]"
    show ep05_amberintro23
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d080'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d081'])]"
    show ep05_amberintro25 with vpunch
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d082'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d083'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d084'])]"
    show ep05_amberintro26 at dramatic_focus
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d085'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d086'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d087'])]"
    show ep05_amberintro27 with normalfade
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d088'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d089'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d090'])]"
    show ep05_amberintro28 with hpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d091'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d092'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d093'])]"
    show ep05_amberintro29 with hpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d094'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d095'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d096'])]"
    scene eigengrau
    show ep05_amber_anim at dramatic_focus_out
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d097'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d098'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d099'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d100'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d101'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d102'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d103'])]"
    scene eigengrau
    show ep05_amber_anim2 at dramatic_focus, vpunch_effect(time=0.3, offset=10, pause=0.4), concentrate
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d104'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d105'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d106'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d107'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d108'])]"
    scene eigengrau with slowfade
    show ep05_amberintro30 at dramatic_realization with vpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d109'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d110'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d111'])]"
    show ep05_amberintro31 at subtle_zoom_out with vpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d112'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d113'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d114'])]"
    scene eigengrau
    show ep05_amber_anim4 at dramatic_focus, vpunch_effect(time=0.3, offset=10, pause=0.3), concentrate
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d115'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d116'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d117'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d118'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d119'])]"
    scene eigengrau
    show ep05_amber_anim3 at slow_reveal, camera_zoom, ken_burns_left_to_right
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d120'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d121'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d122'])]"
    scene eigengrau with slowfade
    show ep05_amberintro32 with vpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d123'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d124'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d125'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d126'])]"
    show ep05_amberintro33 at subtle_zoom_in
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d127'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d128'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d129'])]"
    scene eigengrau with slowfade
    show ep05_amberintro34 with vpunch
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d130'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d131'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d132'])]"
    show ep05_amberintro35
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d133'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d134'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d135'])]"
    show ep05_amberintro36
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d136'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d137'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d138'])]"
    show ep05_amberintro37 at ken_burns_left_to_right
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d139'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d140'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d141'])]"
    show white zorder 1.0 at ejaculation_flash
    show ep05_amberintro38 at vpunch with flash
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d142'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d143'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d144'])]"
    show ep05_amberintro39 at dramatic_focus_out
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d145'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d146'])]"
    show ep05_amberintro40
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d147'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d149'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d150'])]"
    show ep05_amberintro41
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d151'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d152'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d153'])]"
    show ep05_amberintro42
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d154'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d155'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d156'])]"
    show ep05_amberintro43
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d160'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d161'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d162'])]"
    show ep05_amberintro44
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d157'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d158'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d159'])]"
    show ep05_amberintro45
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d163'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d164'])]"
    if ep04_ambnight_cum == 1:
        amb "[renpy.substitute(dialogues5['E05AMBERCOF_d165'])]"
        mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d166'])]"
    else:
        amb "[renpy.substitute(dialogues5['E05AMBERCOF_d167'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d168'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d170'])]"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep05_amberintro46
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d171'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d172'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d173'])]"
    show ep05_amberintro47
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d174'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d175'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d176'])]"
    show ep05_amberintro48
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d177'])]"
    mc_s "[renpy.substitute(dialogues5['E05AMBERCOF_d178'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d179'])]"
    show ep05_amberintro49
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d180'])]"
    mc_t "[renpy.substitute(dialogues5['E05AMBERCOF_d181'])]"
    amb "[renpy.substitute(dialogues5['E05AMBERCOF_d182'])]"
    $ stopAllSubchannels("amb", 2.0)
    jump ep05_isacos

label ep05_isacos:
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.4, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)
    if ep05_ambignore:
        show ep05_isaintro01
        isa "[renpy.substitute(dialogues5['E05ISACOS_d001'])]"
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d002'])]"
        isa "[renpy.substitute(dialogues5['E05ISACOS_d003'])]"
    else:
        $ setChannelVolume("sfx", 1, 1, 0)
        $ playAudio(sfx_door_knock, "sfx", 1, False, 0, 0)
        show ep05_isaintro02
        mc_s "[renpy.substitute(dialogues5['E05ISACOS_d004'])]"
        isa "[renpy.substitute(dialogues5['E05ISACOS_d005'])]"
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d006'])]"
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    show ep05_isaintro03 at ken_burns_right_to_left
    isa "[renpy.substitute(dialogues5['E05ISACOS_d007'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d008'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d009'])]"
    $ setChannelVolume("sfx", 3, 1, 0)
    $ playAudio(sfx_door_open2, "sfx", 3, False, 0, 0)
    show ep05_isaintro04
    isa "[renpy.substitute(dialogues5['E05ISACOS_d010'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d011'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d012'])]"
    show ep05_isaintro05
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d013'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d014'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d015'])]"
    show ep05_isaintro06 at ken_burns_top_to_bottom
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d016'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d017'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d018'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d019'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d020'])]"
    show ep05_isaintro07 with normalfade
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d021'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d022'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d023'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d024'])]"
    show ep05_isaintro08
    isa "[renpy.substitute(dialogues5['E05ISACOS_d025'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d026'])]"
    show ep05_isaintro09 at ken_burns_bottom_to_top with vpunch
    isa "[renpy.substitute(dialogues5['E05ISACOS_d027'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d028'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d029'])]"
    show ep05_isaintro10 with normalfade
    isa "[renpy.substitute(dialogues5['E05ISACOS_d030'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d031'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d032'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d033'])]"
    show ep05_isaintro11
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d034'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d035'])]"
    show ep05_isaintro12 at ken_burns_bottom_to_top
    isa "[renpy.substitute(dialogues5['E05ISACOS_d036'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d037'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d038'])]"
    $ setChannelVolume("music", 1, 0.6, 0)
    $ playAudio(isabella_sexy, "music", 1, True, 4, 0)
    show ep05_isaintro13 with hpunch
    isa "[renpy.substitute(dialogues5['E05ISACOS_d039'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d040'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d041'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d042'])]"
    show ep05_isaintro14
    isa "[renpy.substitute(dialogues5['E05ISACOS_d043'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d044'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d045'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)
    show ep05_isaintro15
    isa "[renpy.substitute(dialogues5['E05ISACOS_d046'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d047'])]"
    show ep05_isaintro16
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d048'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d049'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d050'])]"
    show ep05_isaintro17
    isa "[renpy.substitute(dialogues5['E05ISACOS_d051'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d052'])]"
    $ show_walkthrough("ep05_isacheckmenu")
    menu:
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d053'])]"
        "Let me check your outfit":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro18 with hpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d054'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d055'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d056'])]"
            show ep05_isaintro19 at ken_burns_top_to_bottom
            isa "[renpy.substitute(dialogues5['E05ISACOS_d057'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d058'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d059'])]"
            show ep05_isaintro20
            isa "[renpy.substitute(dialogues5['E05ISACOS_d060'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d061'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d062'])]"
            show ep05_isaintro21 with hpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d063'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d064'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d065'])]"
            $ rm.update("isabella", "trust", 2)
            $ check_levels("isabella", "trust", 2)
        "This isn't right...":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro22 with hpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d066'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d067'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d068'])]"
            show ep05_isaintro23
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d069'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d070'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d071'])]"
            show ep05_isaintro24 at ken_burns_bottom_to_top
            isa "[renpy.substitute(dialogues5['E05ISACOS_d072'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d073'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d074'])]"
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)
            show ep05_isaintro25 at ken_burns_right_to_left
            isa "[renpy.substitute(dialogues5['E05ISACOS_d075'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d076'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d077'])]"
            $ rm.update("isabella", "trust", 4)
            $ check_levels("isabella", "trust", 4)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Let me check you":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro26 with vpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d078'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d079'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d080'])]"
            show ep05_isaintro27
            isa "[renpy.substitute(dialogues5['E05ISACOS_d081'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d082'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d083'])]"
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)
            show ep05_isaintro28 at ken_burns_corner_to_corner4 with vpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d084'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d085'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d086'])]"
            show ep05_isaintro29 at ken_burns_left_to_right with hpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d087'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d088'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d089'])]"
            show ep05_isaintro30 with normalfade
            isa "[renpy.substitute(dialogues5['E05ISACOS_d090'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d091'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d092'])]"
            show ep05_isaintro31
            isa "[renpy.substitute(dialogues5['E05ISACOS_d093'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d094'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d095'])]"
            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 4)
            $ check_levels("isabella", "cor", 4)
            $ ep05_isacosplay -= 1
    show ep05_isaintro32 with slowfade
    isa "[renpy.substitute(dialogues5['E05ISACOS_d096'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d097'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d098'])]"
    $ show_walkthrough("ep05_isacheckmenu2")
    menu:
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d099'])]"
        "Hold still":
            hide screen walkthrough_screen
            show ep05_isaintro33
            isa "[renpy.substitute(dialogues5['E05ISACOS_d100'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d101'])]"
            show ep05_isaintro34
            isa "[renpy.substitute(dialogues5['E05ISACOS_d102'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d103'])]"
            show ep05_isaintro35 with hpunch
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d104'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d105'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d106'])]"
            $ rm.update("isabella", "trust", 4)
            $ check_levels("isabella", "trust", 4)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Let me adjust it":
            hide screen walkthrough_screen
            show ep05_isaintro36 with vpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d107'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d108'])]"
            show ep05_isaintro37
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d109'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d110'])]"
            show ep05_isaintro38
            isa "[renpy.substitute(dialogues5['E05ISACOS_d111'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d112'])]"
            show ep05_isaintro39 at dramatic_focus_out with normalfade
            isa "[renpy.substitute(dialogues5['E05ISACOS_d113'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d114'])]"
            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 4)
            $ check_levels("isabella", "cor", 4)
            $ ep05_isacosplay -= 1
    scene eigengrau with slowfade
    show ep05_isaintro40
    isa "[renpy.substitute(dialogues5['E05ISACOS_d115'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d116'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d117'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)
    show ep05_isaintro41 at ken_burns_top_to_bottom
    isa "[renpy.substitute(dialogues5['E05ISACOS_d118'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d119'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d120'])]"
    show ep05_isaintro42 with vpunch
    isa "[renpy.substitute(dialogues5['E05ISACOS_d121'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d122'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d123'])]"
    $ show_walkthrough("ep05_isacheckmenu3")
    menu:
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d124'])]"
        "Let me help with the buckles":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro43 at ken_burns_left_to_right
            isa "[renpy.substitute(dialogues5['E05ISACOS_d125'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d126'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d127'])]"
            $ rm.update("isabella", "trust", 4)
            $ check_levels("isabella", "trust", 4)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Show me exactly how":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)
            show ep05_isaintro44 with vpunch
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d128'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d129'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d130'])]"
            show ep05_isaintro43 at ken_burns_left_to_right
            isa "[renpy.substitute(dialogues5['E05ISACOS_d131'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d132'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d133'])]"
            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 4)
            $ check_levels("isabella", "cor", 4)
            $ ep05_isacosplay -= 1
    scene eigengrau with slowfade
    show ep05_isaintro45 at ken_burns_corner_to_corner3 with vpunch
    isa "[renpy.substitute(dialogues5['E05ISACOS_d134'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d135'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d136'])]"
    $ show_walkthrough("ep05_isacheckmenu4")
    menu:
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d137'])]"
        "Let's finish the costume":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)
            show ep05_isaintro46 at ken_burns_left_to_right
            isa "[renpy.substitute(dialogues5['E05ISACOS_d138'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d139'])]"
            scene eigengrau with slowfade
            show ep05_isaintro48 at ken_burns_top_to_bottom with vpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d140'])]"
            isa "[renpy.substitute(dialogues5['E05ISACOS_d141'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d142'])]"
            $ rm.update("isabella", "trust", 4)
            $ check_levels("isabella", "trust", 4)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Stand still":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)
            show ep05_isaintro47 at ken_burns_corner_to_corner4 with hpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d143'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d144'])]"
            scene eigengrau with slowfade
            show ep05_isaintro49 at ken_burns_top_to_bottom with vpunch
            isa "[renpy.substitute(dialogues5['E05ISACOS_d145'])]"
            mc_s "[renpy.substitute(dialogues5['E05ISACOS_d146'])]"
            mc_t "[renpy.substitute(dialogues5['E05ISACOS_d147'])]"
            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 4)
            $ check_levels("isabella", "cor", 4)
            $ ep05_isacosplay -= 1
    show ep05_isaintro50 with normalfade
    isa "[renpy.substitute(dialogues5['E05ISACOS_d148'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d149'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d150'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d151'])]"
    while not (look_down_seen and look_middle_seen and look_up_seen):
        menu:
            "Look down" if not look_down_seen:
                $ look_down_seen = True
                show ep05_isaintro51 at subtle_zoom_in
                mc_t "[renpy.substitute(dialogues5['E05ISACOS_d152'])]"
                isa "[renpy.substitute(dialogues5['E05ISACOS_d153'])]"
                mc_t "[renpy.substitute(dialogues5['E05ISACOS_d154'])]"
            "Look at the middle" if not look_middle_seen:
                $ look_middle_seen = True
                show ep05_isaintro52 at subtle_zoom_out
                mc_t "[renpy.substitute(dialogues5['E05ISACOS_d155'])]"
                isa "[renpy.substitute(dialogues5['E05ISACOS_d156'])]"
                mc_t "[renpy.substitute(dialogues5['E05ISACOS_d157'])]"
            "Look up" if not look_up_seen:
                $ look_up_seen = True
                show ep05_isaintro53 at ken_burns_bottom_to_top
                mc_t "[renpy.substitute(dialogues5['E05ISACOS_d158'])]"
                isa "[renpy.substitute(dialogues5['E05ISACOS_d159'])]"
                mc_t "[renpy.substitute(dialogues5['E05ISACOS_d160'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d161'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d162'])]"
    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_inhale_fem, "sfx", 5, False, 0, 0)
    show ep05_isaintro54 at subtle_zoom_out with vpunch
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d163'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d164'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d165'])]"
    $ stopAudio("sfx", 5, 2)
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_kiss_op_isa, "sfx", 4, False, 1, 0)
    show ep05_isaintro55 at ken_burns_right_to_left
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d166'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d167'])]"
    if ep04_isabellakiss:
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d168'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05ISACOS_d169'])]"
    $ stopAudio("sfx", 4, 2)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep05_isaintro56
    isa "[renpy.substitute(dialogues5['E05ISACOS_d170'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d171'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d172'])]"
    isa "[renpy.substitute(dialogues5['E05ISACOS_d173'])]"
    show ep05_isaintro57
    isa "[renpy.substitute(dialogues5['E05ISACOS_d174'])]"
    mc_s "[renpy.substitute(dialogues5['E05ISACOS_d175'])]"
    mc_t "[renpy.substitute(dialogues5['E05ISACOS_d176'])]"
    $ stopAllSubchannels("amb", 2.0)
    if ep05_isacosplay == 4 or ep05_isacosplay == -4:
        $ ep05_ach_isaintro = True
    else:
        pass
    jump ep05_elizintro

label ep05_elizintro:
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.5
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_dooropen, "sfx", 2, False, 0, 0)
    $ setChannelVolume("amb", 1, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)
    show ep05_elizintro01
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d003'])]"
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(elizabeth_sad_theme, "music", 1, True, 4, 0)
    show ep05_elizintro02 at ken_burns_bottom_to_top
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d004'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d006'])]"
    show ep05_elizintro03 at ken_burns_left_to_right
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d007'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d008'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d009'])]"
    show ep05_elizintro04 at ken_burns_bottom_to_top with hpunch
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d010'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d011'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d012'])]"
    show ep05_elizintro05 with vpunch
    mc_s "[renpy.substitute(dialogues5['E05ELIZIN_d013'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d014'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d015'])]"
    ## save notification
    if htl_episodes == 5.1:
        $ show_custom_notification("save_tip")
    else:
        pass
    show ep05_elizintro06 at ken_burns_left_to_right with slowfade
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d016'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d017'])]"
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d018'])]"
    show ep05_elizintro07
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d019'])]"
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d020'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d021'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)
    show ep05_elizintro08 at subtle_zoom_in
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d022'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIZIN_d023'])]"
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d024'])]"
    show ep05_elizintro09 with vpunch
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d025'])]"
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d026'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d027'])]"
    show ep05_elizintro10 at ken_burns_bottom_to_top with normalfade
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d028'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d029'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIZIN_d030'])]"
    show ep05_elizintro11 at focus_shift
    mc_s "[renpy.substitute(dialogues5['E05ELIZIN_d031'])]"
    eli "[renpy.substitute(dialogues5['E05ELIZIN_d032'])]"
#-- End Update
    if htl_episodes == 5.1:
        $ stopAllSubchannels(channel="sfx", fadeout=1)
        $ stopAllSubchannels(channel="amb", fadeout=1.5)
        $ stopAllSubchannels(channel="music", fadeout=2)
        scene eigengrau with rose
        pause 2.0
        $ resetAllVolumes()
        return
    else:
        jump ep05_elipast




## - 2ND DELIVERY
label ep05_elipast:
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAudio("amb", 1, 2)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene white with slowflash
    pause 1.2
    $ setChannelVolume("amb", 2, 0.4, 0)
    $ playAudio(sfx_tokyo_residential, "amb", 2, True, 2, 0)
    show ep05_elipast01 at focus_shift, subtle_zoom_out
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d003'])]"
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    show ep05_elipast02
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d004'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d005'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d006'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d007'])]"
    # Decision point 1: affects elizabeth trust
    $ show_walkthrough("ep05_2nd_elipst")
    menu:
        "Annoyed response":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d008'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d009'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d010'])]"
            $ rm.update("elizabeth", "trust", -2)
            $ check_levels("elizabeth", "trust", -2)
        "Focus on studying":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d011'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d012'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d013'])]"
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
    $ setChannelVolume("sfx", 2, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(elizabeth_play_theme, "music", 1, True, 4, 0)
    show ep05_elipast03 with hpunch
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d014'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d015'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d016'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d017'])]"
    show ep05_elipast04 at subtle_zoom_in
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d018'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d019'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d020'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d021'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d022'])]"
    $ setChannelVolume("music", 1, 0.15, 2.5)
    show ep05_elipast05 with normalfade
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d023'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d024'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d025'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d026'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d027'])]"
    show ep05_elipast06
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d028'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d029'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d030'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d031'])]"
    $ setChannelVolume("music", 1, 0.4, 2.5)
    show ep05_elipast07 at concentrate
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d032'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d033'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d034'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d035'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d036'])]"
    show ep05_elipast08 at concentrate
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d037'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d038'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d039'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d040'])]"
    show ep05_elipast09
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d041'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d042'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d043'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d044'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d045'])]"
    show ep05_elipast10
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d046'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d047'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d048'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d049'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d050'])]"
    show ep05_elipast11 at ken_burns_right_to_left
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d051'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d052'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d053'])]"
    # Decision point 2: affects elizabeth corruption
    $ show_walkthrough("ep05_2nd_elipst2")
    menu:
        "Maintain innocence":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d054'])]"
            $ setChannelVolume("music", 1, 0, 3)
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d055'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d056'])]"
            $ setChannelVolume("sfx", 3, 1, 0)
            $ playAudio(sfx_footsteps_bare_wood, "sfx", 3, False, 0, 0)
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d057'])]"
            $ rm.update("elizabeth", "cor", -2)
            $ check_levels("elizabeth", "cor", -2)
        "Flirtatious reply":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d058'])]"
            $ setChannelVolume("music", 1, 0, 3)
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d059'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d060'])]"
            $ setChannelVolume("sfx", 3, 1, 0)
            $ playAudio(sfx_footsteps_bare_wood, "sfx", 3, False, 0, 0)
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d061'])]"
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
    show ep05_elipast12 with hpunch
    $ stopAudio("sfx", 3, 0.5)
    amb "[renpy.substitute(dialogues5['E05ELIPAST_d062'])]"
    amb "[renpy.substitute(dialogues5['E05ELIPAST_d063'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d064'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d065'])]"
    show ep05_elipast13
    amb "[renpy.substitute(dialogues5['E05ELIPAST_d066'])]"
    amb "[renpy.substitute(dialogues5['E05ELIPAST_d067'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d068'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d069'])]"
    show ep05_elipast14 at ken_burns_top_to_bottom
    amb "[renpy.substitute(dialogues5['E05ELIPAST_d070'])]"
    amb "[renpy.substitute(dialogues5['E05ELIPAST_d071'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d072'])]"
    # Decision point 3: affects amber trust
    $ show_walkthrough("ep05_2nd_elipst3")
    menu:
        "Defend Amber":
            hide screen walkthrough_screen
            show ep05_elipast15
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d073'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d074'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d075'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d076'])]"
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
        "Ignore the situation":
            hide screen walkthrough_screen
            show ep05_elipast15
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d077'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d078'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d079'])]"
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d080'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d081'])]"
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_kiss_one, "sfx", 4, False, 0, 0)
    show ep05_elipast16 with hpunch
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d082'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d083'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d084'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d085'])]"
    show ep05_elipast17 with normalfade
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d086'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d087'])]"
    $ stopAudio("amb", 2, 2)
    scene eigengrau with circlewipe
    pause 1
    show ep05_elipast18 with circlewipe
    $ setChannelVolume("amb", 3, 0.4, 0)
    $ playAudio(sfx_midnightpast, "amb", 3, True, 2, 0)
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d088'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d089'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d090'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d091'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False, 0, 0)
    show ep05_elipast19 at impact_shake with vpunch
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d092'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d093'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d094'])]"
    show ep05_elipast20 at focus_shift
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d095'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d096'])]"
    mc_s "[renpy.substitute(dialogues5['E05MADYOG_d056'])]"
    $ setChannelVolume("sfx", 6, 1, 0)
    $ playAudio(sfx_tea, "sfx", 6, False, 0, 0)
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d097'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d098'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d099'])]"
    show ep05_elipast21 at ken_burns_top_to_bottom
    $ stopAudio("sfx", 6, 0.5)
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d100'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d101'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d102'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d103'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d104'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d105'])]"
    show ep05_elipast22
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d106'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d107'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d108'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d109'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d112'])]"
    show ep05_elipast23 with hpunch
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d110'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d111'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d113'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d114'])]"
    $ setChannelVolume("sfx", 7, 1, 0)
    $ playAudio(sfx_tea_splash, "sfx", 7, False, 0, 0)
    scene eigengrau
    pause 1
    show ep05_elipast24 at ken_burns_top_to_bottom
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d115'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d116'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d117'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d118'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d119'])]"
    $ setChannelVolume("sfx", 8, 1, 0)
    $ playAudio(sfx_clothes, "sfx", 8, False, 0, 0)
    show ep05_elipast25 at ken_burns_bottom_to_top
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d120'])]"
    $ setChannelVolume("music", 1, 0.4, 3)
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d121'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d122'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d123'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d124'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d125'])]"
    show ep05_elipast26 at concentrate
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d126'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d127'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d128'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d129'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d130'])]"
    show ep05_elipast27
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d131'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d132'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d133'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d134'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d135'])]"
    $ stopAudio("amb", 3, 2)
    $ stopAudio("music", 1, 2)
    scene eigengrau with slowfade
    pause 1
    show ep05_elipast28 at focus_shift
    $ setChannelVolume("amb", 4, 0.4, 0)
    $ playAudio(sfx_mc_room_night, "amb", 4, True, 2, 0)
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d136'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d137'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d138'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d139'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d140'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d141'])]"
    $ setChannelVolume("music", 2, 0.4, 0)
    $ playAudio(elizabeth_theme, "music", 2, True, 4, 0)
    show ep05_elipast29 at ken_burns_corner_to_corner2
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d142'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d143'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d144'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d145'])]"
    $ setChannelVolume("sfx", 9, 0.4, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 9, False, 0, 0)
    show ep05_elipast30
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d146'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d147'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d148'])]"
    eli "[renpy.substitute(dialogues5['E05ELIPAST_d149'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d150'])]"
    $ setChannelVolume("sfx", 1, 0.7, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    show ep05_elipast31
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d151'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d152'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d153'])]"
    # Decision point 4: core amber suspicious of eli
    $ show_walkthrough("ep05_2nd_elipst4")
    menu:
        "Freeze in place":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d154'])]"
            mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d155'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d156'])]"
            eli "[renpy.substitute(dialogues5['E05ELIPAST_d157'])]"
            $ setChannelVolume("sfx", 3, 1, 0)
            $ playAudio(sfx_door_wood, "sfx", 3, False, 0, 0)
            $ stopAudio("music", 2, 3)
            scene eigengrau
            pause 1
            amb "[renpy.substitute(dialogues5['E05ELIPAST_d159'])]"
            $ ep05_ambersus_eli = True
            $ ep05_ach_ambvseli = True
        "Push her away":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d158'])]"
            $ setChannelVolume("sfx", 2, 1, 0)
            $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)
            $ setChannelVolume("sfx", 3, 0.6, 0)
            $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)
            $ stopAudio("music", 2, 3)
            scene eigengrau
            pause 1
            $ ep05_ambersus_eli = False
            $ ep05_ach_novseli = True
    show ep05_elipast32
    if ep05_ambersus_eli:
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d160'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d161'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d162'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d163'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d164'])]"
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d165'])]"
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d166'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d167'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d168'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d169'])]"
    show ep05_elipast33
    if ep05_ambersus_eli:
        $ setChannelVolume("music", 3, 0.4, 0)
        $ playAudio(elizabeth_anger_theme, "music", 3, True, 4, 0)
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d170'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d171'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d118'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d173'])]"
        mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d174'])]"
    else:
        $ setChannelVolume("music", 3, 0.4, 0)
        $ playAudio(amber_sad_theme, "music", 3, True, 4, 0)
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d175'])]"
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d176'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d177'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d178'])]"
        mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d179'])]"
    show ep05_elipast34
    if ep05_ambersus_eli:
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d180'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d181'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d182'])]"
        mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d183'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d184'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d185'])]"
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d186'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d187'])]"
        amb "[renpy.substitute(dialogues5['E05ELIPAST_d188'])]"
        mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d189'])]"
    show ep05_elipast35
    if ep05_ambersus_eli:
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d190'])]"
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d191'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d192'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d193'])]"
        mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d194'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d195'])]"
        mc_s "[renpy.substitute(dialogues5['E05ELIPAST_d196'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d197'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d198'])]"
        mc_t "[renpy.substitute(dialogues5['E05ELIPAST_d199'])]"
    $ setChannelVolume("sfx", 4, 0.6, 0)
    $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)
    show ep05_elipast36 at ken_burns_top_to_bottom
    if ep05_ambersus_eli:
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d200'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d201'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d202'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d203'])]"
    else:
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d204'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d205'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d206'])]"
        eli "[renpy.substitute(dialogues5['E05ELIPAST_d207'])]"
    $ stopAudio("amb", 4, 2)
    $ stopAudio("music", 3, 2)
    jump ep05_elishower




label ep05_elishower:
    scene white with slowflash
    pause 1
    # Initial sequence (01-05)
    show ep05_elibath01
    $ setChannelVolume("amb", 5, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 5, True, 2, 0)
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d003'])]"
    show ep05_elibath02
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d004'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d006'])]"
    show ep05_elibath03
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d007'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d008'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d009'])]"
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_door_knock, "sfx", 1, False, 0, 0)
    show ep05_elibath04
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d010'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d011'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d012'])]"
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(elizabeth_singing_song, "music", 1, True, 4, 0)
    show ep05_elibath05 at ken_burns_corner_to_corner4
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d013'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d014'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d015'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d016'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d017'])]"
    # First branch decision
    $ show_walkthrough("ep05_2nd_elishow")
    menu:
        "Show concern":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d018'])]"
            mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d019'])]"
            $ ep05_mcthinksex = False
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
        "Be suspicious":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d020'])]"
            mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d021'])]"
            $ ep05_mcthinksex = False
        "Inappropriate thoughts":
            hide screen walkthrough_screen
            mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d022'])]"
            mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d023'])]"
            $ ep05_mcthinksex = True
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
    # Path after first decision (06-08)
    scene eigengrau with dissolve
    $ setChannelVolume("sfx", 3, 1, 0)
    $ playAudio(sfx_showering, "sfx", 3, True, 3, 0)
    pause 1
    show ep05_elishower1 at focus_shift, ken_burns_right_to_left with normalfade
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d024'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d025'])]"
    $ setChannelVolume("sfx", 3, 0.4, 1.0)
    show ep05_elibath06 with normalfade
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d026'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d027'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d028'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d029'])]"
    $ setChannelVolume("sfx", 3, 0.8, 1.0)
    show ep05_elibath07 at ken_burns_corner_to_corner3
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d030'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d031'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d032'])]"
    $ setChannelVolume("sfx", 3, 1, 1.0)
    show ep05_elishower2 at focus_shift, ken_burns_bottom_to_top
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d033'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d034'])]"
    $ setChannelVolume("sfx", 3, 0.4, 1.0)
    show ep05_elibath08 with normalfade
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d035'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d036'])]"
    # Middle sequence (09-15) and reset mcthinksex
    $ setChannelVolume("sfx", 3, 0.7, 1.0)
    show ep05_elibath09 at ken_burns_left_to_right
    $ ep05_mcthinksex = False  # Reset mcthinksex
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d037'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d038'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d039'])]"
    $ stopAudio("sfx", 3, 2)
    scene eigengrau with slowfade
    pause 1
    show ep05_elibath10 at ken_burns_bottom_to_top
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d040'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d041'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d042'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d043'])]"
    $ stopAudio("music", 1, 4)
    show ep05_elibath11 with normalfade
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d044'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d045'])]"
    show ep05_elibath12 at ken_burns_right_to_left
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d046'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d047'])]"
    show ep05_elibath13
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d048'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d049'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d050'])]"
    show ep05_elibath14
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d051'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d052'])]"
    show ep05_elibath15
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d053'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d054'])]"
    # Second branch decision
    $ show_walkthrough("ep05_2nd_elishow2")
    menu:
        "Positive memory":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d055'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d056'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d057'])]"
            $ ep05_mcthinksex = False
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
        "Vague recollection":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d058'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d059'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d060'])]"
            $ ep05_mcthinksex = False
        "Inappropriate memory":
            hide screen walkthrough_screen
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d061'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d062'])]"
            mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d063'])]"
            $ ep05_mcthinksex = True
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
    # Path after second decision (16-19)
    $ setChannelVolume("music", 2, 0.4, 0)
    $ playAudio(mc_elizabeth_theme, "music", 2, True, 4, 0)
    show ep05_elibath16
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d064'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d065'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d066'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d067'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d068'])]"
    show ep05_elibath17 at concentrate
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d069'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d070'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d071'])]"
    show ep05_elibath18 at ken_burns_top_to_bottom
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d072'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d073'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d074'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d075'])]"
    show ep05_elibath19
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d076'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d077'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d078'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d079'])]"
    # Determine which path to follow (naughty or love)
    $ ep05_naughty_path = False
    if rm.get("elizabeth", "cor") > rm.get("elizabeth", "trust"):
        $ ep05_naughty_path = True
    elif rm.get("elizabeth", "trust") == rm.get("elizabeth", "cor"):
        # Equal values - random choice
        $ ep05_naughty_path = renpy.random.randint(0, 1) == 1
    # Show appropriate images based on path
    if ep05_naughty_path:
        show ep05_elibath21
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d080'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d081'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d082'])]"
        show ep05_elibath23 at ken_burns_left_to_right
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d083'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d084'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d085'])]"
        show ep05_elibath25 at ken_burns_corner_to_corner4
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d086'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d087'])]"
    else:
        show ep05_elibath20
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d080'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d089'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d090'])]"
        show ep05_elibath22 at ken_burns_left_to_right
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d083'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d092'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d085'])]"
        show ep05_elibath24 at ken_burns_corner_to_corner4
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d094'])]"
        eli "[renpy.substitute(dialogues5['E05ELISHOW_d095'])]"
    # Final sequence (20-25)
    show ep05_elibath26
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d096'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d097'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d098'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELISHOW_d099'])]"
    show ep05_elibath27
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d100'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d101'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d102'])]"
    eli "[renpy.substitute(dialogues5['E05ELISHOW_d103'])]"
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_slamdoor, "sfx", 4, False, 0, 0)
    $ stopAudio("music", 2, 2)
    show ep05_elibath28
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d104'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d105'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELISHOW_d106'])]"
    $ stopAudio("amb", 5, 2)
    jump ep05_smspaz_intro




label ep05_smspaz_intro:
    scene eigengrau with slowfade
    pause 1
    show ep05_smspz01 at ken_burns_left_to_right with circlewipe
    $ setChannelVolume("amb", 6, 0.5, 0)
    $ playAudio(sfx_earlypast, "amb", 6, True, 2, 0)
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d003'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d004'])]"
    show ep05_smspz02 at ken_burns_top_to_bottom
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d006'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d007'])]"
    show ep05_smspz03
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d008'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d009'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZSMS_d010'])]"
    jump ep05_smspaz_phone




label ep05_smspaz_call:
    # Initial sequence (01-21)
    show ep05_smspz03 at focus_shift
    pause 1.0
    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_vcall, "sfx", 5, True, 0, 0)
    call screen videocall_icons("ep05_pazvc")

label ep05_pazvc:
    hide ep05_smspz03
    $ stopAudio("sfx", 5, 0.5)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(paz_peace_theme, "music", 1, True, 4, 0)
    show ep05_callpz01 at scale_down, videocall_open
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d001'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d002'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d003'])]"
    show ep05_callpz02 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d004'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZVC_d005'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d006'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d007'])]"
    show ep05_callpz03 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d008'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZVC_d009'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d010'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d011'])]"
    show ep05_callpz04 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d012'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d013'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d014'])]"
    show ep05_callpz05 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d015'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZVC_d016'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d017'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d018'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d019'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d020'])]"
    show ep05_callpz06 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d021'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d022'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d023'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d024'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZVC_d025'])]"
    show ep05_callpz07 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d026'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d027'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d028'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d029'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d030'])]"
    show ep05_callpz08 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d031'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d032'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d033'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d034'])]"
    show ep05_callpz09 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d035'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d036'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d037'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d038'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d039'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d040'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d041'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZVC_d042'])]"
    show ep05_callpz10 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d043'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d044'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d045'])]"
    show ep05_callpz11 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d046'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d047'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d048'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d049'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d050'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d051'])]"
    show ep05_callpz12 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d052'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d053'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d054'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d055'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d056'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d057'])]"
    show ep05_callpz13 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d058'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d059'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d060'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d061'])]"
    show ep05_callpz14 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d062'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZVC_d063'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d064'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d065'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d066'])]"
    show ep05_callpz15 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d067'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d068'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d069'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d070'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d071'])]"
    show ep05_callpz16 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d072'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZVC_d073'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d074'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d075'])]"
    show ep05_callpz17 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d076'])]"
    mc_t "[renpy.substitute(dialogues5['E05PZVC_d077'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d078'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d079'])]"
    show ep05_callpz18 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d080'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d081'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d082'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d083'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d084'])]"
    show ep05_callpz19 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d085'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d086'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d087'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d088'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d089'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d090'])]"
    show ep05_callpz20 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d091'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d092'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d093'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d094'])]"
    mc_s "[renpy.substitute(dialogues5['E05PZVC_d095'])]"
    show ep05_callpz21 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d096'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d097'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d098'])]"
    pa_s "[renpy.substitute(dialogues5['E05PZVC_d099'])]"
    $ show_walkthrough("ep05_2nd_paz")
    menu:
        "Support stealing evidence":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -10)
            $ ep05_integrity_choice = "negative"
        "Insist on legal methods":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 10)
            $ ep05_integrity_choice = "positive"
    # Final sequence with different dialogues based on choice
    show ep05_callpz22 at scale_down
    if ep05_integrity_choice == "negative":
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d100'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d101'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d102'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d103'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d104'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d105'])]"
    show ep05_callpz23 at scale_down
    if ep05_integrity_choice == "negative":
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d106'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d107'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d108'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d109'])]"
    else:
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d110'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d111'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d112'])]"
    show ep05_callpz24 at scale_down
    if ep05_integrity_choice == "negative":
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d113'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d114'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d115'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d116'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d117'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d118'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d119'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d120'])]"
    show ep05_callpz25 at scale_down
    if ep05_integrity_choice == "negative":
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d121'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d122'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d123'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d124'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d125'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d126'])]"
    show ep05_callpz26 at scale_down
    if ep05_integrity_choice == "negative":
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d127'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d128'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d129'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d130'])]"
    else:
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d131'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d132'])]"
        pa_s "[renpy.substitute(dialogues5['E05PZVC_d133'])]"
        mc_s "[renpy.substitute(dialogues5['E05PZVC_d134'])]"
    show ep05_smspz03 at focus_shift
    pause 1.0
    $ stopAudio("music", 1, 4)
    jump ep05_intromn




label ep05_intromn:
    scene eigengrau with slowfade
    show ep05_mnintro01 at ken_burns_left_to_right
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d003'])]"
    $ stopAudio("amb", 6, 2)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_door_knock, "sfx", 1, False, 0, 0)
    pause 1
    show ep05_mnintro02 with circlewipe
    $ setChannelVolume("amb", 7, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 7, True, 2, 0)
    isa "[renpy.substitute(dialogues5['E05NMBATH_d004'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d005'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d006'])]"
    show ep05_mnintro03 at ken_burns_right_to_left
    isa "[renpy.substitute(dialogues5['E05NMBATH_d008'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d009'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d010'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d011'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d007'])]"
    show ep05_mnintro04
    isa "[renpy.substitute(dialogues5['E05NMBATH_d012'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d013'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d014'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d015'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d016'])]"
    $ stopAudio("amb", 7, 2)
    scene eigengrau with slowfade
    pause 1
    show ep05_mnintro05
    $ setChannelVolume("amb", 1, 0.4, 0)
    $ setChannelVolume("amb", 2, 0.5, 0)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 1, 0)
    $ playAudio(sfx_wind_pool, "amb", 2, True, 1, 0)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(isabella_theme, "music", 1, True, 4, 0)
    isa "[renpy.substitute(dialogues5['E05NMBATH_d017'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d018'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d019'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d020'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d021'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d022'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d023'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d024'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d025'])]"
    $ stopAudio("amb", 2, 2)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_door_glass, "sfx", 2, False, 0, 0)
    pause 1
    show ep05_mnintro06
    isa "[renpy.substitute(dialogues5['E05NMBATH_d026'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d027'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d028'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d029'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d030'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d031'])]"
    show ep05_mnintro07 at ken_burns_bottom_to_top
    isa "[renpy.substitute(dialogues5['E05NMBATH_d032'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d033'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d034'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d035'])]"
    show ep05_mnintro08
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d036'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d037'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d038'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d039'])]"
    isa "[renpy.substitute(dialogues5['E05NMBATH_d040'])]"
    $ stopAudio("music", 1, 2)
    show ep05_mnintro09 at subtle_zoom_out with normalfade
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d041'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d042'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d043'])]"
    $ setChannelVolume("sfx", 3, 0.7, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 3, False, 0, 0)
    show ep05_mnintro10
    mad "[renpy.substitute(dialogues5['E05NMBATH_d044'])]"
    $ stopAudio("sfx", 3, 2)
    mad "[renpy.substitute(dialogues5['E05NMBATH_d045'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d046'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d047'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d048'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d049'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d050'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d051'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d052'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d053'])]"
    $ setChannelVolume("sfx", 3, 0.7, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 3, False, 0, 0)
    show ep05_mnintro11 at ken_burns_left_to_right
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d054'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d055'])]"
    $ stopAudio("sfx", 3, 2)
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d056'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d057'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d058'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d059'])]"
    # First choice - Wait or Don't Wait
    $ show_walkthrough("ep05_2nd_mnbath")
    menu:
        "Wait for Madison to leave":
            hide screen walkthrough_screen
            $ ep05_mnwait = True
        "Check on Nanami now":
            hide screen walkthrough_screen
            $ ep05_mnwait = False
            # DON'T WAIT path - exits after completion
            $ stopAudio("amb", 1, 2)
            scene eigengrau with slowfade
            pause 1
            show ep05_mnbath01 at ken_burns_right_to_left
            $ setChannelVolume("amb", 3, 0.5, 0)
            $ playAudio(sfx_evening_pool, "amb", 3, True, 2, 0)
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d060'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d061'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d062'])]"
            $ setChannelVolume("sfx", 4, 0.7, 0)
            $ playAudio(sfx_grass_walk, "sfx", 4, False, 0, 0)
            show ep05_mnbath02
            mad "[renpy.substitute(dialogues5['E05NMBATH_d063'])]"
            $ stopAudio("sfx", 4, 2)
            mad "[renpy.substitute(dialogues5['E05NMBATH_d064'])]"
            $ setChannelVolume("music", 2, 0.4, 0)
            $ playAudio(madison_bad_theme, "music", 2, True, 4, 0)
            mad "[renpy.substitute(dialogues5['E05NMBATH_d065'])]"
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bodygrab, "sfx", 5, False, 0, 0)
            show ep05_mnbath03 at ken_burns_top_to_bottom with vpunch
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d066'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d067'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d068'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d069'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d070'])]"
            show ep05_mnbath04
            mad "[renpy.substitute(dialogues5['E05NMBATH_d071'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d072'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d073'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d074'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d075'])]"
            show ep05_mnbath05
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d076'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d077'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d078'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d079'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d080'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d081'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d082'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d083'])]"
            $ stopAudio("music", 2, 2)
            $ stopAudio("amb", 3, 2)
            jump ep05_elibdown
    
    # If we get here, player chose WAIT path
    scene eigengrau with slowfade
    show ep05_mnbath01 with circlewipe
    mad "[renpy.substitute(dialogues5['E05NMBATH_d084'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d085'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d086'])]"
    scene eigengrau with slowfade
    show ep05_mnbath02
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d087'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d088'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d089'])]"
    $ stopAudio("amb", 1, 2)
    scene eigengrau
    pause 1
    show ep05_mnbath03 at ken_burns_right_to_left with normalfade
    $ setChannelVolume("amb", 3, 0.5, 0)
    $ playAudio(sfx_evening_pool, "amb", 3, True, 2, 0)
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d090'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d091'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d092'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d093'])]"
    $ setChannelVolume("sfx", 6, 0.5, 0)
    $ playAudio(sfx_drinking_fem, "sfx", 6, False, 0, 0)
    show ep05_mnbath04
    nana "[renpy.substitute(dialogues5['E05NMBATH_d094'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d095'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d096'])]"
    $ setChannelVolume("sfx", 7, 0.5, 0)
    $ playAudio(sfx_kiss_water, "sfx", 7, False, 0, 0)
    $ setChannelVolume("sfx", 8, 0.5, 0)
    $ playAudio(sfx_gulping_water, "sfx", 8, False, 0, 0)
    show ep05_mnbath05 at dramatic_focus
    nana "[renpy.substitute(dialogues5['E05NMBATH_d097'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d098'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d099'])]"
    $ setChannelVolume("music", 3, 0.4, 0)
    $ playAudio(madison_nan_theme, "music", 3, True, 4, 0)
    show ep05_mnbath06 at ken_burns_bottom_to_top with normalfade
    mad "[renpy.substitute(dialogues5['E05NMBATH_d100'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d101'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d102'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d103'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d104'])]"
    show ep05_mnbath07
    nana "[renpy.substitute(dialogues5['E05NMBATH_d105'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d106'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d107'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d108'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d109'])]"
    show ep05_mnbath08 at ken_burns_bottom_to_top
    mad "[renpy.substitute(dialogues5['E05NMBATH_d110'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d111'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d112'])]"
    $ setChannelVolume("sfx", 9, 0.8, 0)
    $ playAudio(sfx_kiss_one, "sfx", 9, False, 0, 0)
    show ep05_mnbath09 at dramatic_focus_out
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d113'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d114'])]"
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_bathtub_sink1, "sfx", 1, False, 0, 0)
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_bathtub_sink2, "sfx", 2, False, 0, 0)
    scene eigengrau with slowfade
    pause 1
    show ep05_mnbath10
    mad "[renpy.substitute(dialogues5['E05NMBATH_d115'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d116'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d117'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d118'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d119'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d120'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d121'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d122'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d123'])]"
    show ep05_mnbath11
    nana "[renpy.substitute(dialogues5['E05NMBATH_d124'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d125'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d126'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d127'])]"
    $ setChannelVolume("sfx", 3, 0.5, 0)
    $ playAudio(sfx_pool_splash, "sfx", 3, False, 0, 0)
    show ep05_mnbath12 at ken_burns_left_to_right
    mad "[renpy.substitute(dialogues5['E05NMBATH_d128'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d129'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d130'])]"
    $ setChannelVolume("sfx", 4, 0.5, 0)
    $ playAudio(sfx_pool_outof, "sfx", 4, False, 0, 0)
    scene eigengrau
    pause 1
    show ep05_mnbath13
    nana "[renpy.substitute(dialogues5['E05NMBATH_d131'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d132'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d133'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d134'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d135'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d136'])]"
    show ep05_mnbath14
    mad "[renpy.substitute(dialogues5['E05NMBATH_d137'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d138'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d139'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d140'])]"
    show ep05_mnbath15
    mad "[renpy.substitute(dialogues5['E05NMBATH_d141'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d142'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d143'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d144'])]"
    show ep05_mnbath16 at ken_burns_right_to_left
    nana "[renpy.substitute(dialogues5['E05NMBATH_d145'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d146'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d147'])]"

    # Second choice - Voyeur or Active Path
    $ show_walkthrough("ep05_2nd_mnbath2")
    menu:
        "Continue watching":
            hide screen walkthrough_screen
            $ ep05_mnvoy = True
            # VOYEUR PATH - exits after completion
            scene eigengrau with slowfade
            show ep05_mnpaths01
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d148'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d149'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d150'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d151'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d152'])]"
            show ep05_mnpaths02
            mad "[renpy.substitute(dialogues5['E05NMBATH_d153'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d154'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d155'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d156'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d157'])]"
            show ep05_mnpaths03
            mad "[renpy.substitute(dialogues5['E05NMBATH_d158'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d159'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d160'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d161'])]"
            show ep05_mnpaths04
            mad "[renpy.substitute(dialogues5['E05NMBATH_d162'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d163'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d164'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d165'])]"
            show ep05_mnpaths05
            mad "[renpy.substitute(dialogues5['E05NMBATH_d166'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d167'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d168'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d169'])]"
            show ep05_mnpaths06 with vpunch
            mad "[renpy.substitute(dialogues5['E05NMBATH_d170'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d171'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d172'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d173'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d174'])]"
            $ setChannelVolume("sfx", 4, 0.8, 0)
            $ playAudio(sfx_madohxxx, "sfx", 4, False, 0, 0)
            show ep05_mnpaths07 at ken_burns_corner_to_corner3
            mad "[renpy.substitute(dialogues5['E05NMBATH_d175'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d176'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d177'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d178'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d179'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d180'])]" #CUM
            show white zorder 1.0 at ejaculation_flash
            show ep05_mnpaths08 at vpunch with flash
            mad "[renpy.substitute(dialogues5['E05NMBATH_d181'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d182'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d183'])]"
            $ stopAudio("music", 3, 4)
            show ep05_mnpaths09 at ken_burns_right_to_left
            nana "[renpy.substitute(dialogues5['E05NMBATH_d184'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d185'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d186'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d187'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d188'])]"
            show ep05_mnpaths10
            mad "[renpy.substitute(dialogues5['E05NMBATH_d189'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d190'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d191'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d192'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d193'])]"
            show ep05_mnpaths11
            mad "[renpy.substitute(dialogues5['E05NMBATH_d194'])]"
            $ setChannelVolume("music", 4, 0.4, 0)
            $ playAudio(madison_bad_theme, "music", 4, True, 4, 0)
            mad "[renpy.substitute(dialogues5['E05NMBATH_d195'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d192'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d197'])]"
            show ep05_mnpaths12 at ken_burns_top_to_bottom
            mad "[renpy.substitute(dialogues5['E05NMBATH_d198'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d199'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d200'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d201'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d202'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d203'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d204'])]"
            $ stopAudio("music", 4, 2)
            $ stopAudio("amb", 3, 2)
            jump ep05_elibdown
        "Intervene":
            hide screen walkthrough_screen
            $ ep05_mnvoy = False

    # If we get here, player chose ACTIVE path
    scene eigengrau with slowfade
    show ep05_mnpaths01
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d205'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d206'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d207'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d208'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d209'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d210'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d211'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d212'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d213'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d214'])]"
    show ep05_mnpaths02
    nana "[renpy.substitute(dialogues5['E05NMBATH_d215'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d216'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d217'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d218'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d219'])]"
    show ep05_mnpaths03
    nana "[renpy.substitute(dialogues5['E05NMBATH_d220'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d221'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d222'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d223'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d224'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d225'])]"
    show ep05_mnpaths04 at subtle_zoom_out
    nana "[renpy.substitute(dialogues5['E05NMBATH_d226'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d227'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d228'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d229'])]"
    show ep05_mnpaths05 with normalfade
    mad "[renpy.substitute(dialogues5['E05NMBATH_d230'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d231'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d232'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d233'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d234'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d235'])]"
    show ep05_mnpaths06
    nana "[renpy.substitute(dialogues5['E05NMBATH_d236'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d237'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d238'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d239'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d240'])]"
    $ stopAudio("music", 3, 4)
    show ep05_mnpaths07 at ken_burns_right_to_left
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d241'])]"
    mc_t "[renpy.substitute(dialogues5['E05NMBATH_d242'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d243'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d244'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d245'])]"
    show ep05_mnpaths08 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues5['E05NMBATH_d246'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d247'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d248'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d249'])]"
    show ep05_mnpaths09
    mad "[renpy.substitute(dialogues5['E05NMBATH_d250'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d251'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d252'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d253'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d254'])]"
    show ep05_mnpaths10
    mad "[renpy.substitute(dialogues5['E05NMBATH_d255'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d256'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d257'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d258'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d259'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d260'])]"
    $ setChannelVolume("music", 4, 0.4, 0)
    $ playAudio(madison_theme, "music", 4, True, 4, 0)
    show ep05_mnpaths11 at subtle_zoom_out with normalfade
    mad "[renpy.substitute(dialogues5['E05NMBATH_d261'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d262'])]"
    mc_s "[renpy.substitute(dialogues5['E05NMBATH_d263'])]"
    scene eigengrau
    pause 1
    show ep05_mnpaths12 with vpunch
    nana "[renpy.substitute(dialogues5['E05NMBATH_d220'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d265'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d266'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d267'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d268'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d269'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d270'])]"
    show ep05_mnpaths13 at ken_burns_top_to_bottom
    nana "[renpy.substitute(dialogues5['E05NMBATH_d271'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d272'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d273'])]"
    nana "[renpy.substitute(dialogues5['E05NMBATH_d274'])]"
    show ep05_mnpaths14 with normalfade
    mad "[renpy.substitute(dialogues5['E05NMBATH_d275'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d276'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d277'])]"
    mad "[renpy.substitute(dialogues5['E05NMBATH_d278'])]"

# Third choice - Accept or Deny
    $ show_walkthrough("ep05_2nd_mnbath3")
    menu:
        "Accept her challenge":
            hide screen walkthrough_screen
            $ ep05_mntouch = True
            # ACCEPT path
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d279'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d280'])]"
            show ep05_mnpaths15 with hpunch
            # Update variables
            $ rm.update("nanami", "trust", -10)
            $ check_levels("nanami", "trust", -10)
            $ ss.add("nanami", "strike")
            $ show_custom_notification("strike1")
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d281'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d282'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d283'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d284'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d285'])]"
            show ep05_mnpaths16
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d286'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d287'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d288'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d289'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d290'])]"
            show ep05_mnpaths17 at ken_burns_bottom_to_top with vpunch
            mad "[renpy.substitute(dialogues5['E05NMBATH_d291'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d292'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d293'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d294'])]"
            show ep05_mnpaths18 with normalfade
            mad "[renpy.substitute(dialogues5['E05NMBATH_d295'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d296'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d297'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d298'])]"
            show ep05_mnpaths19
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d299'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d300'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d301'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d302'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d303'])]"
            show ep05_mnpaths20
            mad "[renpy.substitute(dialogues5['E05NMBATH_d304'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d305'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d306'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d307'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d308'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d309'])]"
            show ep05_mnpaths21 at ken_burns_left_to_right
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d310'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d311'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d312'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d313'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d314'])]"
            $ ep05_ach_nanastrike = True

        "Refuse to participate":
            hide screen walkthrough_screen
            $ ep05_mntouch = False
            # DENY path
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d315'])]"
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d316'])]"
            show ep05_mnpaths15
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d317'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d318'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d319'])]"
            $ stopAudio("music", 4, 2)
            mad "[renpy.substitute(dialogues5['E05NMBATH_d320'])]"
            # Update variables
            $ rm.update("nanami", "trust", 10)
            $ check_levels("nanami", "trust", 10)
            show ep05_mnpaths16
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d321'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d322'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d323'])]"
            $ setChannelVolume("music", 5, 0.4, 0)
            $ playAudio(mc_nanami_theme, "music", 5, True, 4, 0)
            show ep05_mnpaths17
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d324'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d325'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d326'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d327'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d328'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d329'])]"
            show ep05_mnpaths18 with hpunch
            nana "[renpy.substitute(dialogues5['E05NMBATH_d330'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d331'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d332'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d333'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d334'])]"
            show ep05_mnpaths19 at ken_burns_right_to_left
            mad "[renpy.substitute(dialogues5['E05NMBATH_d335'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d336'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d337'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d338'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d339'])]"
            show ep05_mnpaths20
            mad "[renpy.substitute(dialogues5['E05NMBATH_d340'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d341'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d342'])]"
            mc_s "[renpy.substitute(dialogues5['E05NMBATH_d343'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d344'])]"
            show ep05_mnpaths21 at ken_burns_left_to_right with normalfade
            mc_t "[renpy.substitute(dialogues5['E05NMBATH_d345'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d346'])]"
            nana "[renpy.substitute(dialogues5['E05NMBATH_d347'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d348'])]"
            mad "[renpy.substitute(dialogues5['E05NMBATH_d349'])]"
    $ stopAudio("amb", 3, 2)
    $ stopAllSubchannels("music", 2.0)
    jump ep05_elibdown



label ep05_elibdown:
    scene eigengrau with slowfade
    pause 1
    show ep05_elibreak01 at ken_burns_left_to_right
    $ setChannelVolume("amb", 4, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 4, True, 2, 0)
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_pills, "sfx", 1, False, 0, 0)
    eli "[renpy.substitute(dialogues5['E05ELBD_d001'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d002'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d003'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d004'])]"
    $ setChannelVolume("music", 1, 0.2, 0)
    $ playAudio(chaos_theme, "music", 1, True, 4, 0)
    show ep05_elibreak02 with flash
    eli "[renpy.substitute(dialogues5['E05ELBD_d005'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d006'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d007'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d008'])]"
    show ep05_elibreak03
    eli "[renpy.substitute(dialogues5['E05ELBD_d009'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d010'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d011'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d012'])]"
    show ep05_elibreak04 with flash
    eli "[renpy.substitute(dialogues5['E05ELBD_d013'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d014'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d015'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d016'])]"
    $ setChannelVolume("music", 1, 0, 0.5)
    show ep05_elibreak05 at subtle_zoom_out with slowflash
    eli "[renpy.substitute(dialogues5['E05ELBD_d017'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d018'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d019'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d020'])]"
    $ setChannelVolume("music", 1, 0.3, 0.5)
    show ep05_elibreak06 with flash
    eli "[renpy.substitute(dialogues5['E05ELBD_d021'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d022'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d023'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d024'])]"
    show ep05_elibreak07 at ken_burns_bottom_to_top with flash
    eli "[renpy.substitute(dialogues5['E05ELBD_d025'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d026'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d027'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d028'])]"
    show ep05_elibreak08 at ken_burns_right_to_left with flash
    eli "[renpy.substitute(dialogues5['E05ELBD_d029'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d030'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d031'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d032'])]"
    $ setChannelVolume("music", 1, 0, 0.5)
    show ep05_elibreak09 at focus_shift with slowflash
    eli "[renpy.substitute(dialogues5['E05ELBD_d033'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d034'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d035'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d036'])]"
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_punch_floor, "sfx", 2, False, 0, 0)
    $ setChannelVolume("music", 1, 0.4, 0.5)
    show ep05_elibreak10 with vpunch
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d037'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d038'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d039'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d040'])]"
    $ setChannelVolume("music", 1, 0, 0.5)
    show ep05_elibreak11 with slowfade
    eli "[renpy.substitute(dialogues5['E05ELBD_d041'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d042'])]"
    show ep05_elibreak12 with flash
    eli "[renpy.substitute(dialogues5['E05ELBD_d043'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d044'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d045'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d046'])]"
    $ setChannelVolume("sfx", 3, 0.5, 0)
    $ playAudio(sfx_glassbreak, "sfx", 3, False, 0, 0)
    $ setChannelVolume("music", 1, 0.5, 0.5)
    show ep05_elibreak13 at action_sequence with flash
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d047'])]"
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d048'])]"
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d049'])]"
    show ep05_elibreak14 at ken_burns_top_to_bottom
    eli "[renpy.substitute(dialogues5['E05ELBD_d050'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d051'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d052'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d053'])]"
    show ep05_elibreak15
    eli "[renpy.substitute(dialogues5['E05ELBD_d054'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d055'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d056'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d057'])]"
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_punch_floor, "sfx", 2, False, 0, 0)
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_punch_glass, "sfx", 4, False, 0, 0)
    show ep05_elibreak16
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d058'])]"
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d059'])]"
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d060'])]"
    eli_y "[renpy.substitute(dialogues5['E05ELBD_d061'])]"
    show ep05_elibreak17 at ken_burns_right_to_left
    eli "[renpy.substitute(dialogues5['E05ELBD_d062'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d063'])]"
    show ep05_elibreak18
    show vignette at pov_die
    eli "[renpy.substitute(dialogues5['E05ELBD_d064'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d065'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d066'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d067'])]"
    show ep05_elibreak19 at focus_pulse, dizzyness with slowfade
    eli "[renpy.substitute(dialogues5['E05ELBD_d068'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d069'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)
    show ep05_elibreak20 at focus_pulse, dizzyness with vpunch
    eli "[renpy.substitute(dialogues5['E05ELBD_d070'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d071'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d072'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d073'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d074'])]"
    eli "[renpy.substitute(dialogues5['E05ELBD_d075'])]"
    $ stopAllSubchannels("music", 2.0)
    $ setChannelVolume("amb", 4, 0, 1.0)
    ## save notification
    if htl_episodes == 5.2:
        $ show_custom_notification("save_tip")
    else:
        pass
    scene eigengrau with slowfade
    pause 1
    show ep05_elibreak21 with line80
    $ setChannelVolume("amb", 5, 0.5, 0)
    $ playAudio(sfx_earlypast, "amb", 5, True, 2, 0)
    amb "[renpy.substitute(dialogues5['E05ELBD_d076'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d077'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELBD_d078'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELBD_d079'])]"
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_stairs_up, "sfx", 5, False, 0, 0)
    show ep05_elibreak22 at subtle_zoom_out
    mc_t "[renpy.substitute(dialogues5['E05ELBD_d080'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELBD_d081'])]"
    show ep05_elibreak23 with hpunch
    amb "[renpy.substitute(dialogues5['E05ELBD_d082'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d083'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELBD_d084'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d085'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d086'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELBD_d095'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d096'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELBD_d097'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d098'])]"
    $ stopAudio("amb", 5, 2)
    $ setChannelVolume("sfx", 6, 1, 0)
    $ playAudio(sfx_dooropen, "sfx", 6, False, 0, 0)
    scene eigengrau with slowfade
    pause 1
    $ setChannelVolume("sfx", 2, 7, 0)
    $ playAudio(sfx_doorclose, "sfx", 7, False, 0, 0)
    show ep05_elibreak24 with slowfade
    $ setChannelVolume("amb", 4, 0.5, 1.0)
    amb "[renpy.substitute(dialogues5['E05ELBD_d087'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d088'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELBD_d089'])]"
    mc_t "[renpy.substitute(dialogues5['E05ELBD_d090'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELBD_d091'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d092'])]"
    mc_s "[renpy.substitute(dialogues5['E05ELBD_d093'])]"
    amb "[renpy.substitute(dialogues5['E05ELBD_d094'])]"
    #-- End Update
    if htl_episodes == 5.2:
        $ stopAllSubchannels(channel="sfx", fadeout=1)
        $ stopAllSubchannels(channel="amb", fadeout=1.5)
        $ stopAllSubchannels(channel="music", fadeout=2)
        scene eigengrau with rose
        pause 2.0
        $ resetAllVolumes()
        return
    else:
        jump ep05_elisuicide