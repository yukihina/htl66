label ep05_elisuicide:
    $ stopAllAudio(2.0)

    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0

    show days
    pause 3

    show loc_hospmichael_night with slowfade
    show hospital_location zorder 2 with dissolve
    pause 4
    hide hospital_location with dissolve
    
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)

    show ep05_hosd1_nan01 at ken_burns_bottom_to_top
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d002'])]"


    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(nanami_theme, "music", 1, True, 4, 0)

    show ep05_hosd1_nan02
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d003'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d004'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d005'])]"
    else:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d006'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d007'])]"
    
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d008'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d009'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d010'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d011'])]"
    
    show ep05_hosd1_nan03
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d012'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d013'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d014'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d015'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d016'])]"
    
    if ep04_mcdrunk:
        show ep05_hosd1_nan04
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d017'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d018'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d019'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d020'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d021'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d022'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d023'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d024'])]"

        $ stopAudio("music", 1, 2)
        
        $ setChannelVolume("amb", 2, 0.4, 0)
        $ playAudio(sfx_clinicwalla2, "amb", 2, False, 2, 3)

        scene eigengrau with slowfade
        show ep05_hosd1_nan05 with circlewipe
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d025'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d026'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d027'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d028'])]"
        
        $ show_walkthrough("ep05_hosnan_m1")
        menu:
            "Madison gave you bad advice":
                hide screen walkthrough_screen
                $ ep05_mc_blame_madison = True

                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d029'])]"
                nana "[renpy.substitute(dialogues5['E05_ELSUI_d030'])]"
                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d031'])]"

                $ rm.update("madison", "trust", -1)
                $ check_levels("madison", "trust", -1)
            
            "You didn't do anything wrong":
                hide screen walkthrough_screen
                $ ep05_mc_blame_madison = False

                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d032'])]"
                nana "[renpy.substitute(dialogues5['E05_ELSUI_d033'])]"
                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d034'])]"

                $ rm.update("madison", "trust", 1)
                $ check_levels("madison", "trust", 1)
        
        show ep05_hosd1_nan06
        mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d035'])]"

        if ep05_mc_blame_madison:
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d036'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d037'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d038'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d039'])]"
        else:
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d040'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d041'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d042'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d043'])]"
        
        show ep05_hosd1_nan07
        $ show_walkthrough("ep05_hosnan_m2")
        menu:
            "I should have protected you":
                hide screen walkthrough_screen
                $ ep05_mc_takes_responsibility = True

                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d044'])]"
                nana "[renpy.substitute(dialogues5['E05_ELSUI_d045'])]"
                nana "[renpy.substitute(dialogues5['E05_ELSUI_d046'])]"
                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d047'])]"

                $ rm.update("nanami", "trust", 6)
                $ check_levels("nanami", "trust", 6)
            
            "We were both confused":
                hide screen walkthrough_screen
                $ ep05_mc_takes_responsibility = False
                
                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d048'])]"
                nana "[renpy.substitute(dialogues5['E05_ELSUI_d049'])]"
                nana "[renpy.substitute(dialogues5['E05_ELSUI_d050'])]"
                mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d051'])]"

                $ rm.update("nanami", "trust", -6)
                $ check_levels("nanami", "trust", -6)
        
        $ setChannelVolume("music", 2, 0.3, 0)
        $ playAudio(nanami_clumsy_theme, "music", 2, True, 4, 0)

        show ep05_hosd1_nan08 with vpunch
        if ep05_mc_takes_responsibility:
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d052'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d053'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d054'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d055'])]"
        else:
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d056'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d057'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d058'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d059'])]"
        
        mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d060'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d061'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d062'])]"
    else:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d063'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d064'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d065'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d066'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d067'])]"
        
        $ stopAudio("music", 1, 2)
    
    $ setChannelVolume("amb", 2, 0.4, 0)
    $ playAudio(sfx_clinicwalla2, "amb", 2, False, 2, 3)
    
    show ep05_hosd1_nan09
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d068'])]"
    else:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d069'])]"
    
    $ stopAllSubchannels("music", 2)

    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d070'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d071'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d072'])]"
    
    $ show_walkthrough("ep05_hosnan_m3")
    menu:
        "We shouldn't talk about this":
            hide screen walkthrough_screen
            $ ep05_nanami_sex_education = False

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d073'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d074'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d075'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d076'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d077'])]"

            $ rm.update("nanami", "cor", -2)
            $ check_levels("nanami", "cor", -2)
        
        "Those feelings are normal":
            hide screen walkthrough_screen
            $ ep05_nanami_sex_education = True

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d078'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d079'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d080'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d081'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d082'])]"

            $ rm.update("nanami", "cor", 2)
            $ check_levels("nanami", "cor", 2)

            $ setChannelVolume("music", 3, 0.3, 0)
            $ playAudio(nanami_theme, "music", 3, True, 4, 0)
    
    show ep05_hosd1_nan10 at ken_burns_corner_to_corner3
    if ep05_nanami_sex_education:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d083'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d084'])]"
    else:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d085'])]"
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d086'])]"
    
    show ep05_hosd1_nan18 at concentrate
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d087'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d088'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d089'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d090'])]"
    
    show ep05_hosd1_nan11 with vpunch
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d091'])]"
    
    $ show_walkthrough("ep05_hosnan_m4")
    menu:
        "Madison cares but she's confused":
            hide screen walkthrough_screen
            $ ep05_madison_is_bad = False

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d092'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d093'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d094'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d095'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d096'])]"

            $ rm.update("madison", "trust", 2)
            $ check_levels("madison", "trust", 2)
        
        "What Madison does isn't okay":
            hide screen walkthrough_screen
            $ ep05_madison_is_bad = True

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d097'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d098'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d099'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d100'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d101'])]"

            $ rm.update("madison", "trust", -2)
            $ check_levels("madison", "trust", -2)
    
    $ stopAudio("music", 3, 2)

    nana "[renpy.substitute(dialogues5['E05_ELSUI_d102'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d103'])]"
    
    $ setChannelVolume("music", 5, 0.3, 0)
    $ playAudio(nanami_love_theme, "music", 5, True, 4, 0)

    show ep05_hosd1_nan12 with hpunch
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d104'])]"
    else:
        nana "[renpy.substitute(dialogues5['E05_ELSUI_d105'])]"
    
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d106'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d107'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d108'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d109'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d110'])]"
    
    show ep05_hosd1_nan13 at ken_burns_bottom_to_top
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d111'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d112'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d113'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d114'])]"
    
    show ep05_hosd1_nan14
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d115'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d116'])]"
    nana "[renpy.substitute(dialogues5['E05_ELSUI_d117'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d118'])]"

    $ show_walkthrough("ep05_hosnan_m5")
    menu:
        "Get off me right now":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d119'])]"

            $ stopAllSubchannels("music", 2)

            show ep05_hosd1_nan15 with hpunch
            $ setChannelVolume("sfx", 1, 0.3, 0)
            $ playAudio(sfx_walk_slow_f, "sfx", 1, False, 2, 2)

            nana "[renpy.substitute(dialogues5['E05_ELSUI_d120'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d121'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d122'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d123'])]"

            $ rm.update("nanami", "trust", -6)
            $ check_levels("nanami", "trust", -6)
            $ ss.add("nanami", "strike")
            $ nanami_strikes = ss.get("nanami", "strike")
            if nanami_strikes == 1:
                $ show_custom_notification("strike1")
            elif nanami_strikes == 2:
                $ show_custom_notification("strike2")
            elif nanami_strikes >= 3:
                $ show_custom_notification("strike3")
        
        "This should be the last time":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d124'])]"

            $ stopAllSubchannels("music", 2)

            show ep05_hosd1_nan17
            $ setChannelVolume("sfx", 1, 0.3, 0)
            $ playAudio(sfx_walk_slow_f, "sfx", 1, False, 2, 2)

            nana "[renpy.substitute(dialogues5['E05_ELSUI_d125'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d126'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d127'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d128'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d129'])]"

            $ rm.update("nanami", "trust", -3)
            $ check_levels("nanami", "trust", -3)
        
        "Just enjoy the moment":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d130'])]"

            show ep05_hosd1_nan16 with vpunch
            $ setChannelVolume("sfx", 1, 0.3, 0)
            $ playAudio(sfx_walk_slow_f, "sfx", 1, False, 2, 2)

            nana "[renpy.substitute(dialogues5['E05_ELSUI_d131'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d132'])]"
            mc_s "[renpy.substitute(dialogues5['E05_ELSUI_d133'])]"
            nana "[renpy.substitute(dialogues5['E05_ELSUI_d134'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELSUI_d135'])]"

            $ stopAllSubchannels("music", 2)

            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)
    
    $ stopAllSubchannels("sfx", 2)

    jump ep05_hosmadison

label ep05_hosmadison:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0

    $ setChannelVolume("amb", 3, 0.1, 0)
    $ playAudio(sfx_clinicwalla3, "amb", 3, False, 3, 3)

    show ep05_hosd1_mad01
    mad "[renpy.substitute(dialogues5['E05_MADHO_d001'])]"
    nana "[renpy.substitute(dialogues5['E05_MADHO_d002'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d003'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d004'])]"
    
    show ep05_hosd1_mad02 at ken_burns_right_to_left
    nana "[renpy.substitute(dialogues5['E05_MADHO_d005'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d006'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d007'])]"
    nana "[renpy.substitute(dialogues5['E05_MADHO_d008'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d009'])]"
    
    show ep05_hosd1_mad03
    nana "[renpy.substitute(dialogues5['E05_MADHO_d010'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d011'])]"
    if ep04_nanadad:
        nana "[renpy.substitute(dialogues5['E05_MADHO_d012'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d013'])]"
    else:
        nana "[renpy.substitute(dialogues5['E05_MADHO_d014'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d015'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d016'])]"
    
    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(madison_bad_theme, "music", 1, True, 4, 0)

    $ setChannelVolume("sfx", 1, 0.7, 0)
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)

    show ep05_hosd1_mad04 at ken_burns_left_to_right with hpunch
    if ep04_mcdrunk:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d017'])]"
    else:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d018'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d019'])]"
    
    $ show_walkthrough("ep05_hosmad_m1")
    menu:
        "Try to defuse the situation":
            hide screen walkthrough_screen
            $ ep05_confrontation_peaceful = True

            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d020'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d021'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d022'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d023'])]"

            $ rm.update("madison", "trust", 1)
            $ check_levels("madison", "trust", 1)
        
        "Put her in her place":
            hide screen walkthrough_screen
            $ ep05_confrontation_peaceful = False

            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d024'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d025'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d026'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d027'])]"

            $ rm.update("madison", "trust", -2)
            $ check_levels("madison", "trust", -2)
    
    $ setChannelVolume("sfx", 2, 0.7, 0)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)

    show ep05_hosd1_mad05 at ken_burns_right_to_left with hpunch
    mad "[renpy.substitute(dialogues5['E05_MADHO_d028'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d029'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d030'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d031'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d032'])]"
    
    show ep05_hosd1_mad06 at zoom_out
    mad "[renpy.substitute(dialogues5['E05_MADHO_d033'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d034'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d035'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d036'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d037'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d038'])]"
    
    if not ep05_confrontation_peaceful:
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d230'])]"

        show ep05_hosd1_mad07
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d039'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d040'])]"
        
        $ show_walkthrough("ep05_hosmad_m2")
        menu:
            "Make a direct threat":
                hide screen walkthrough_screen
                $ ep05_threat_direct = True

                mc_s "[renpy.substitute(dialogues5['E05_MADHO_d041'])]"
                mad "[renpy.substitute(dialogues5['E05_MADHO_d042'])]"
                mc_s "[renpy.substitute(dialogues5['E05_MADHO_d043'])]"

                $ rm.update("madison", "trust", -2)
                $ check_levels("madison", "trust", -2)
            
            "Hint at consequences":
                hide screen walkthrough_screen
                $ ep05_threat_direct = False

                mc_s "[renpy.substitute(dialogues5['E05_MADHO_d044'])]"
                mad "[renpy.substitute(dialogues5['E05_MADHO_d045'])]"
                mc_s "[renpy.substitute(dialogues5['E05_MADHO_d046'])]"
        
        if ep05_threat_direct:
            if ep04_nanadad:
                mad "[renpy.substitute(dialogues5['E05_MADHO_d047'])]"
            else:
                mad "[renpy.substitute(dialogues5['E05_MADHO_d048'])]"
        else:
            mad "[renpy.substitute(dialogues5['E05_MADHO_d049'])]"
            
        mad "[renpy.substitute(dialogues5['E05_MADHO_d050'])]"
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d051'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d052'])]"
        
        $ stopAllAudio(2.0)

        jump ep05_hospaz
        
    else:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d229'])]"

        $ stopAudio("music", 1, 2)

        scene eigengrau with slowfade
        $ setChannelVolume("amb", 2, 0.3, 0)
        $ playAudio(sfx_clinicwalla2, "amb", 2, False, 3, 0)

        show ep05_hosd1_mad08 at ken_burns_bottom_to_top
        mad "[renpy.substitute(dialogues5['E05_MADHO_d053'])]"
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d054'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d055'])]"
        mc_t "[renpy.substitute(dialogues5['E05_MADHO_d056'])]"
        
        $ setChannelVolume("sfx", 3, 0.7, 0)
        $ playAudio(sfx_bodyfall_carpet, "sfx", 3, False, 0, 0)
        
        pause 0.3

        show ep05_hosd1_mad09 with vpunch
        mad "[renpy.substitute(dialogues5['E05_MADHO_d057'])]"
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d058'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d059'])]"
        mc_t "[renpy.substitute(dialogues5['E05_MADHO_d060'])]"
    
    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(madison_sexy_theme, "music", 2, True, 4, 0)

    show ep05_hosd1_mad10 at ken_burns_bottom_to_top with slowfade
    mad "[renpy.substitute(dialogues5['E05_MADHO_d061'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d062'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d063'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d064'])]"
    
    show ep05_hosd1_mad11 at ken_burns_left_to_right
    mad "[renpy.substitute(dialogues5['E05_MADHO_d065'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d066'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d067'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d068'])]"
    
    show ep05_hosd1_mad12 at subtle_zoom_in
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d069'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d070'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d071'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d072'])]"
    
    show ep05_hosd1_mad13 at ken_burns_bottom_to_top
    mad "[renpy.substitute(dialogues5['E05_MADHO_d073'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d074'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d075'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d076'])]"
    
    show ep05_hosd1_mad14 at ken_burns_right_to_left
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d077'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d078'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d079'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d080'])]"
    
    show ep05_hosd1_mad15 at subtle_zoom_out
    mad "[renpy.substitute(dialogues5['E05_MADHO_d081'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d082'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d083'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d084'])]"
    
    show ep05_hosd1_mad43
    mad "[renpy.substitute(dialogues5['E05_MADHO_d085'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d086'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d087'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d088'])]"
    
    show ep05_hosd1_mad44
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d089'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d090'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d091'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d092'])]"
    
    show ep05_hosd1_mad16
    mad "[renpy.substitute(dialogues5['E05_MADHO_d093'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d094'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d095'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d096'])]"
    
    show ep05_hosd1_mad17 with hpunch
    mad "[renpy.substitute(dialogues5['E05_MADHO_d097'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d098'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d099'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d100'])]"
    
    show ep05_hosd1_mad45
    mad "[renpy.substitute(dialogues5['E05_MADHO_d101'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d102'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d103'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d104'])]"
    
    show ep05_hosd1_mad18
    mad "[renpy.substitute(dialogues5['E05_MADHO_d105'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d106'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d107'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d108'])]"
    
    show ep05_hosd1_mad19 at subtle_zoom_out
    mad "[renpy.substitute(dialogues5['E05_MADHO_d109'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d110'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d111'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d112'])]"
    
    show ep05_hosd1_mad20 at subtle_zoom_in
    mad "[renpy.substitute(dialogues5['E05_MADHO_d113'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d114'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d115'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d116'])]"
    
    show ep05_hosd1_mad21 at subtle_zoom_out
    mad "[renpy.substitute(dialogues5['E05_MADHO_d117'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d118'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d119'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d120'])]"
    
    show ep05_hosd1_mad22
    mad "[renpy.substitute(dialogues5['E05_MADHO_d121'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d122'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d123'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d124'])]"
    
    show ep05_hosd1_mad47
    mad "[renpy.substitute(dialogues5['E05_MADHO_d125'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d126'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d127'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d128'])]"
    
    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_madohxxx, "sfx", 4, False, 0, 0)
    
    scene eigengrau
    show ep05_hosd1_mad23 with vpunch
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d129'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d130'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d131'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d132'])]"
    
    show ep05_hosd1_mad24 at ken_burns_bottom_to_top
    mad "[renpy.substitute(dialogues5['E05_MADHO_d133'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d134'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d135'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d136'])]"
    
    show ep05_hosd1_mad25
    if ep04_nanadad:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d137'])]"
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d138'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d139'])]"
    else:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d140'])]"
        mc_s "[renpy.substitute(dialogues5['E05_MADHO_d141'])]"
        mad "[renpy.substitute(dialogues5['E05_MADHO_d142'])]"
    
    show ep05_hosd1_mad26 at ken_burns_left_to_right
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d143'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d144'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d145'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d146'])]"
    
    show ep05_hosd1_mad27
    mad "[renpy.substitute(dialogues5['E05_MADHO_d147'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d148'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d149'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d150'])]"
    
    show ep05_hosd1_mad28
    mad "[renpy.substitute(dialogues5['E05_MADHO_d151'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d152'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d153'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d154'])]"
    
    show ep05_hosd1_mad29 at subtle_zoom_out
    mad "[renpy.substitute(dialogues5['E05_MADHO_d155'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d156'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d157'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d158'])]"
    
    show ep05_hosd1_mad30 at ken_burns_corner_to_corner2
    mad "[renpy.substitute(dialogues5['E05_MADHO_d159'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d160'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d161'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d162'])]"
    
    show ep05_hosd1_mad31
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d163'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d164'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d165'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d166'])]"
    
    show ep05_hosd1_mad32 with vpunch
    mad "[renpy.substitute(dialogues5['E05_MADHO_d167'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d168'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d169'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d170'])]"
    
    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_slosh1, "sfx", 5, True, 0, 0)

    show ep05_hosd1_mad46
    mad "[renpy.substitute(dialogues5['E05_MADHO_d171'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d172'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d173'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d174'])]"
    
    $ stopAudio("sfx", 5, 2)

    show ep05_hosd1_mad33 with hpunch
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d175'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d176'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d177'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d178'])]"
    
    show ep05_hosd1_mad34 with vpunch
    mad "[renpy.substitute(dialogues5['E05_MADHO_d179'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d180'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d181'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d182'])]"
    
    show ep05_hosd1_mad35
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d183'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d184'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d185'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d186'])]"
    
    $ show_walkthrough("ep05_hosmad_m3")
    menu:
        "Finish inside her":
            hide screen walkthrough_screen
            $ ep05_finish_inside = True

            show white zorder 1.0 at ejaculation_flash
            $ setChannelVolume("sfx", 7, 0.5, 0)
            $ playAudio(sfx_cum_bigload_fast, "sfx", 7, False, 0, 0)

            show ep05_hosd1_mad36 at vpunch with flash
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d187'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d188'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d189'])]"
            mc_t "[renpy.substitute(dialogues5['E05_MADHO_d190'])]"

            $ rm.update("madison", "cor", 4)
            $ check_levels("madison", "cor", 4)
            
            show ep05_hosd1_mad37 at subtle_zoom_out
            mad "[renpy.substitute(dialogues5['E05_MADHO_d191'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d192'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d193'])]"
        
        "Pull out":
            hide screen walkthrough_screen
            $ ep05_finish_inside = False

            show white zorder 1.0 at ejaculation_flash
            $ setChannelVolume("sfx", 7, 0.5, 0)
            $ playAudio(sfx_cum_bigload_fast, "sfx", 7, False, 0, 0)

            show ep05_hosd1_mad38 at vpunch with flash
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d194'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d195'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d189'])]"
            mc_t "[renpy.substitute(dialogues5['E05_MADHO_d190'])]"

            $ rm.update("madison", "cor", 2)
            $ check_levels("madison", "cor", 2)
            
            show ep05_hosd1_mad39 at subtle_zoom_out
            mad "[renpy.substitute(dialogues5['E05_MADHO_d198'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d199'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d200'])]"
    
    $ stopAudio("music", 2, 2)

    scene eigengrau with slowfade
    show ep05_hosd1_mad40 
    mad "[renpy.substitute(dialogues5['E05_MADHO_d201'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d202'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d203'])]"

    $ setChannelVolume("amb", 8, 0.2, 0)
    $ playAudio(sfx_clinicwalla3, "amb", 8, False, 3, 3)

    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d204'])]"

    $ ss.add("madison", "blowjob")
    $ ss.add("madison", "anal")
    $ ss.add("madison", "assjob")

    show ep05_hosd1_mad41 at ken_burns_left_to_right
    mad "[renpy.substitute(dialogues5['E05_MADHO_d205'])]"
    
    $ show_walkthrough("ep05_hosmad_m4")
    menu:
        "Accept defeat":
            hide screen walkthrough_screen
            $ ep05_stance_surrender = True

            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d206'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d207'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d208'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d209'])]"

            $ rm.update("madison", "trust", 5)
            $ check_levels("madison", "trust", 5)
        
        "Challenge Madison":
            hide screen walkthrough_screen
            $ ep05_stance_surrender = False

            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d210'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d211'])]"
            mc_s "[renpy.substitute(dialogues5['E05_MADHO_d212'])]"
            mad "[renpy.substitute(dialogues5['E05_MADHO_d213'])]"

            $ rm.update("madison", "trust", -1)
            $ check_levels("madison", "trust", -1)
            $ ss.add("madison", "strike")
            $ madison_strikes = ss.get("madison", "strike")
            if madison_strikes == 1:
                $ show_custom_notification("strike1")
            elif madison_strikes == 2:
                $ show_custom_notification("strike2")
            elif madison_strikes >= 3:
                $ show_custom_notification("strike3")
    
    if ep05_stance_surrender:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d214'])]"
    else:
        mad "[renpy.substitute(dialogues5['E05_MADHO_d215'])]"
    
    mad "[renpy.substitute(dialogues5['E05_MADHO_d216'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d217'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d218'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d219'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d220'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d221'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d222'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d223'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MADHO_d224'])]"
    mad "[renpy.substitute(dialogues5['E05_MADHO_d225'])]"
    
    show ep05_hosd1_mad42 at ken_burns_corner_to_corner with slowfade
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d226'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d227'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MADHO_d228'])]"
    
    $ stopAllAudio(2.0)

    jump ep05_hospaz

label ep05_hospaz:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3

    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    
    show ep05_hosd2_paz01
    $ setChannelVolume("sfx", 1, 0.2, 0)
    $ playAudio(sfx_vcall, "sfx", 1, True, 2, 2)

    mc_t "[renpy.substitute(dialogues5['E05_PAZHO_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZHO_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZHO_d003'])]"
    
    show ep05_hosd2_paz02
    mc_t "[renpy.substitute(dialogues5['E05_PAZHO_d004'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZHO_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZHO_d006'])]"
    call screen videocall_icons("ep05_hospaz_vc")
    
label ep05_hospaz_vc:
    show ep05_hosd2_paz02 at focus_shift_sms
    pause 1.0

    $ stopAudio ("sfx", 1, 1)
    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(paz_theme, "music", 1, True, 4, 0)

    show ep05_hosd2_paz03 at scale_down, videocall_open
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d001'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d002'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d003'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d004'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d005'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d006'])]"
    
    show ep05_hosd2_paz04 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d007'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d008'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d009'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d010'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d011'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d012'])]"
    
    show ep05_hosd2_paz05 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d013'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d014'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d015'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d016'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d017'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d018'])]"
    
    show ep05_hosd2_paz06 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d019'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d020'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d021'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d022'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d023'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d024'])]"
    
    show ep05_hosd2_paz07 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d025'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d026'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d027'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d028'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d029'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d030'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d031'])]"
    
    show ep05_hosd2_paz08 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d032'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d033'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d034'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d035'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d036'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d037'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d038'])]"
    
    show ep05_hosd2_paz09 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d039'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d040'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d041'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d042'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d043'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d044'])]"
    
    show ep05_hosd2_paz10 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d045'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d046'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d047'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d048'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d049'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d050'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d051'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d052'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d053'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d054'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d055'])]"
    
    show ep05_hosd2_paz11 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d056'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d057'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d058'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d059'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d060'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d061'])]"
    
    show ep05_hosd2_paz12 at scale_down
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d062'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d063'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d064'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d065'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d066'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d067'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d068'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d069'])]"

    show ep05_hosd2_paz13 at scale_down
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d070'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d071'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d072'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d073'])]"
    mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d074'])]"
    
    $ show_walkthrough("ep05_hospaz_m1")
    menu:
        "Help her learn":
            $ ep05_paz_choice = 1
            hide screen walkthrough_screen

            show ep05_hosd2_paz14 at scale_down
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d075'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d076'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d077'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d078'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d079'])]"
            mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d080'])]"

            $ rm.update("paz", "trust", 2)
            $ check_levels("paz", "trust", 2)
            $ rm.update("paz", "cor", 4)
            $ check_levels("paz", "cor", 4)
            
            show ep05_hosd2_paz17 at scale_down
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d081'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d082'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d083'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d084'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d085'])]"
            mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d086'])]"
            
            show ep05_hosd2_paz20 at scale_down
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d087'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d088'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d089'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d090'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d091'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d092'])]"
            mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d093'])]"
            
            show ep05_hosd2_paz21 at scale_down
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d094'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d095'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d096'])]"
            mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d097'])]"
            
        "This isn't a good idea":
            $ ep05_paz_choice = 2
            hide screen walkthrough_screen

            $ stopAudio("music", 1, 2)

            show ep05_hosd2_paz15 at scale_down
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d098'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d099'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d100'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d101'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d102'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d103'])]"

            $ rm.update("paz", "cor", -2)
            $ check_levels("paz", "cor", -2)
            
            show ep05_hosd2_paz18 at scale_down
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d104'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d105'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d106'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d107'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d108'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d109'])]"
            
        "You don't need to change":
            $ ep05_paz_choice = 3
            hide screen walkthrough_screen

            show ep05_hosd2_paz16 at scale_down
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d110'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d111'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d112'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d113'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d114'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d115'])]"

            $ rm.update("paz", "trust", 2)
            $ check_levels("paz", "trust", 2)
            
            show ep05_hosd2_paz19 at scale_down
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d116'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d117'])]"
            mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d118'])]"
            pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d119'])]"
    
    show ep05_hosd2_paz22 at scale_down
    if ep05_paz_choice == 1:
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d120'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d121'])]"
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d122'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d092'])]"
    elif ep05_paz_choice == 2:
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d124'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d125'])]"
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d126'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d127'])]"
    else:
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d128'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d129'])]"
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d130'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d131'])]"
    
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d132'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d133'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d134'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d135'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d136'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d137'])]"
    pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d138'])]"
    mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d139'])]"
    
    show ep05_hosd2_paz23 at scale_down
    if ep05_paz_choice == 1:
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d140'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d141'])]"
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d142'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d143'])]"
    elif ep05_paz_choice == 2:
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d144'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d145'])]"
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d146'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d143'])]"
    else:
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d148'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d149'])]"
        pa_s "[renpy.substitute(dialogues5['E05_PAZCA_d142'])]"
        mc_s "[renpy.substitute(dialogues5['E05_PAZCA_d143'])]"

    $ stopAudio("music", 1, 2)
    $ setChannelVolume("amb", 1, 0.2, 0)
    $ playAudio(sfx_clinicwalla3, "amb", 1, True, 2, 0)


    show ep05_hosd2_paz24
    "Nurse" "[renpy.substitute(dialogues5['E05_RNDM_d001'])]"
    if ep05_paz_choice == 1:
        mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d152'])]"
    elif ep05_paz_choice == 2:
        mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d153'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d154'])]"
    
    mc_t "[renpy.substitute(dialogues5['E05_PAZCA_d155'])]"

    $ stopAllAudio(2.0)

    jump ep05_hosamber

label ep05_hosamber:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3

    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    $ setChannelVolume("amb", 2, 0.15, 0)
    $ playAudio(sfx_heart_monitor, "amb", 2, True, 2, 0)
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_clinicroom, "amb", 3, True, 2, 0)

    show ep05_hosd3_amb01 at ken_burns_right_to_left
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d001'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d002'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d003'])]"
    
    $ stopAudio("amb",1,2)
    $ stopAudio("amb",2,2)
    $ stopAudio("amb",3,2)
    $ setChannelVolume("amb", 4, 0.6, 0)
    $ playAudio(sfx_clinicrooftop, "amb", 4, True, 2, 0)
    $ setChannelVolume("amb", 5, 0.2, 0)
    $ playAudio(sfx_wind_pool, "amb", 5, True, 2, 0)

    show ep05_hosd3_amb02 with slowfade
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d004'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d005'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d006'])]"

    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(amber_sad_theme, "music", 1, True, 4, 0)

    amb "[renpy.substitute(dialogues5['E05_AMBHO_d007'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d008'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d009'])]"
    
    show ep05_hosd3_amb03 at ken_burns_corner_to_corner3 with slowfade
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d010'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d011'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d012'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d013'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d014'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d015'])]"

    show ep05_hosd3_amb04 at focus_shift with normalfade
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d016'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d017'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d018'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d019'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d020'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d021'])]"
    
    show ep05_hosd3_amb05 at ken_burns_left_to_right
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d022'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d023'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d024'])]"
    
    $ show_walkthrough("ep05_hosamb_m1")
    menu:
        "Show compassion":
            hide screen walkthrough_screen
            $ ep05_amber_compassion = True

            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d025'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d026'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d027'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d028'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d029'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d030'])]"

            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            
        "Stay detached":
            hide screen walkthrough_screen
            $ ep05_amber_compassion = False

            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d031'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d032'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d033'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d034'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d035'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d036'])]"

            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
    
    show ep05_hosd3_amb06 at ken_burns_right_to_left
    if ep05_amber_compassion:
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d037'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d038'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d039'])]"
    else:
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d040'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d041'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d042'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d043'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d044'])]"
    
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d045'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d046'])]"
    
    $ stopAudio("music", 1, 2)

    show ep05_hosd3_amb07
    if ep05_ambignore:
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d048'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d049'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d050'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d051'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d052'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d053'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d054'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d015'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d056'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d057'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d058'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d059'])]"
    else:
        mc_s  "[renpy.substitute(dialogues5['E05_AMBHO_d060'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d061'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d062'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d063'])]"
        amb "[renpy.substitute(dialogues5['E05_AMBHO_d064'])]"
        mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d065'])]"
    
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d066'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d067'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d068'])]"
    
    show ep05_hosd3_amb08
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d069'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d070'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d071'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d072'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d073'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d074'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d075'])]"
    
    show ep05_hosd3_amb09 with slowfade
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d076'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d077'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d078'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d079'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d080'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d081'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d082'])]"
    
    $ setChannelVolume("music", 9, 0.3, 0)
    $ playAudio(amber_2nd_theme, "music", 9, True, 2, 2)
    pause 1
    $ setChannelVolume("sfx", 3, 0.6, 0)
    $ playAudio(sfx_carhit, "sfx", 3, False, 0, 0)

    show ep05_hosd3_amb10 at ken_burns_corner_to_corner2 with normalfade
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d083'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d084'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d085'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d086'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d087'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d088'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d089'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d090'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d091'])]"
    
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_punch, "sfx", 1, False, 0, 0)
    pause 0.5
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)

    show ep05_hosd3_amb11 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d092'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d093'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d094'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d095'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d096'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d097'])]"
    
    $ show_walkthrough("ep05_hosamb_m2")
    menu:
        "Be romantic and gentle":
            hide screen walkthrough_screen
            $ ep05_amber_route = 1

            show ep05_hosd3_amb12
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d098'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d099'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d100'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d101'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d102'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d103'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d104'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d105'])]"

            $ rm.update("amber", "trust", 6)
            $ check_levels("amber", "trust", 6)
            
        "Be passionate and intense":
            hide screen walkthrough_screen
            $ ep05_amber_route = 2

            show ep05_hosd3_amb13
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d106'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d107'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d108'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d109'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d110'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d111'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d112'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d113'])]"

            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            $ rm.update("amber", "cor", 4)
            $ check_levels("amber", "cor", 4)
            
        "Pull away":
            hide screen walkthrough_screen
            $ ep05_amber_route = 3

            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d114'])]"

            $ stopAllSubchannels("music", 2)

            show ep05_hosd3_amb14
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d115'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d116'])]"
            mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d117'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d118'])]"
            amb "[renpy.substitute(dialogues5['E05_AMBHO_d119'])]"

            $ ss.add("amber", "strike")
            $ amber_strikes = ss.get("amber", "strike")
            if amber_strikes == 1:
                $ show_custom_notification("strike1")
            elif amber_strikes == 2:
                $ show_custom_notification("strike2")
            elif amber_strikes >= 3:
                $ show_custom_notification("strike3")
            $ rm.update("amber", "trust", -6)
            $ check_levels("amber", "trust", -6)

            $ stopAllSubchannels("sfx", 2)
            $ stopAllSubchannels("amb", 2)

            jump ep05_elidream
    
    show ep05_hosd3_amb15
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d120'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d121'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d122'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d015'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d124'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d125'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d126'])]"
    
    $ stopAllSubchannels("music", 2)

    scene eigengrau with slowfade
    show ep05_hosd3_amb16
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d127'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d128'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d129'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d130'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d131'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d132'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d133'])]"
    
    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(amber_sexy_theme2, "music", 2, True, 4, 0)
    $ setChannelVolume("amb", 4, 0.3, 2.0)
    $ setChannelVolume("amb", 5, 0.1, 2.0)

    show ep05_hosd3_amb17
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d134'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d135'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d136'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d137'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d138'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d139'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d140'])]"
    
    show ep05_hosd3_amb18 with vpunch
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d141'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d090'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d143'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d144'])]"

    
    show ep05_hosd3_amb19
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d147'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d148'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d149'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d150'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d151'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d152'])]"
    
    $ setChannelVolume("sfx", 1, 0.2, 1.0)
    $ playAudio(sfx_carhit, "sfx", 1, False)

    show ep05_hosd3_amb20 with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d153'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d154'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d155'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d156'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d157'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d158'])]"
    
    show ep05_hosd3_amb21
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d159'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d121'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d161'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d162'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d163'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d015'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d165'])]"
    
    show ep05_hosd3_amb22
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d166'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d167'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d168'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d169'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d170'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d171'])]"
    
    show ep05_hosd3_amb23 at subtle_zoom_out
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d172'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d173'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d174'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d015'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d176'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d177'])]"
    
    show ep05_hosd3_amb24
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d178'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d179'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d180'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d181'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d182'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d183'])]"
    
    show ep05_hosd3_amb25
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d184'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d185'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d186'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d187'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d188'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d189'])]"
    
    show ep05_hosd3_amb26
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d190'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d191'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d192'])]"
    
    $ setChannelVolume("sfx", 2, 0.1, 0)
    $ playAudio(sfx_gasp_female, "sfx", 2, False)

    show ep05_hosd3_amb27
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d195'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d196'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d197'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d198'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d199'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d200'])]"
    
    show ep05_hosd3_amb28
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d201'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d202'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d203'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d204'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d205'])]"
    
    $ setChannelVolume("sfx", 3, 0.1, 1.0)
    $ playAudio(sfx_moan_generic, "sfx", 3, False)

    show ep05_hosd3_amb56 at focus_shift, ken_burns_left_to_right
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d206'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d207'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d208'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d209'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d210'])]"
    
    show ep05_hosd3_amb29 with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d211'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d212'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d213'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d214'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d215'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d216'])]"
    
    $ setChannelVolume("sfx", 5, 0.3, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False)
    pause 0.5
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_sexslide1, "sfx", 4, False)
    $ setChannelVolume("sfx", 6, 1, 0)
    $ playAudio(sfx_moan_breath2, "sfx", 6, False)

    show ep05_hosd3_amb30 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d217'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d218'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d219'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d220'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d221'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d222'])]"
    
    show ep05_hosd3_amb31
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d223'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d224'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d225'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d226'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d227'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d228'])]"
    
    show ep05_hosd3_amb32 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d229'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d230'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d231'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d232'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d233'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d234'])]"
    
    $ setChannelVolume("sfx", 7, 1, 0)
    $ playAudio(sfx_moan_breath3, "sfx", 7, False)

    show ep05_hosd3_amb33 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d235'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d236'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d237'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d238'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d152'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d240'])]"
    
    scene eigengrau

    $ setChannelVolume("sfx", 4, 1.0, 0)
    $ playAudio(sfx_moan_breath, "sfx", 4, False)

    show ep05_hosd3_amb60 at focus_shift, ken_burns_corner_to_corner3
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d241'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d242'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d243'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d244'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d245'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d246'])]"
    
    show ep05_hosd3_amb34 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d247'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d248'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d249'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d250'])]"
    
    show ep05_hosd3_amb35 at subtle_zoom_out with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d253'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d254'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d255'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d256'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d257'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d258'])]"
    
    scene eigengrau

    $ setChannelVolume("sfx", 9, 0.4, 0)
    $ playAudio(sfx_panting1, "sfx", 9, False)

    show ep05_hosd3_amb61 at focus_shift, ken_burns_left_to_right
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d259'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d260'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d261'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d262'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d263'])]"
    
    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False)
    
    show ep05_hosd3_amb36 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d264'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d202'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d268'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d269'])]"
    
    show ep05_hosd3_amb37
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d270'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d271'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d272'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d273'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d274'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d275'])]"
    
    show ep05_hosd3_amb38 at ken_burns_bottom_to_top with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d276'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d277'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d278'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d279'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d280'])]"
    
    scene eigengrau

    $ setChannelVolume("sfx", 2, 0.2, 0)
    $ playAudio(sfx_moan_generic, "sfx", 2, False)

    show ep05_hosd3_amb57 at focus_shift, ken_burns_right_to_left
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d306'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d307'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d308'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d309'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d310'])]"
    
    scene eigengrau
    show ep05_hosd3_amb58 at focus_shift, ken_burns_top_to_bottom, vpunch_effect(time=0.2, offset=5, pause=0.8)
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d282'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d283'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d284'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d285'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d286'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d287'])]"
    
    
    show ep05_hosd3_amb39 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d288'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d289'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d290'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d291'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d292'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d293'])]"
    
    scene eigengrau
    show ep05_hosd3_amb59 at focus_shift, ken_burns_right_to_left, vpunch_effect(time=0.2, offset=5, pause=0.7)
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d294'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d295'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d296'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d297'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d298'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d299'])]"
    
    scene eigengrau
    show ep05_hosd3_amb40 with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d300'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d301'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d302'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d303'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d304'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d262'])]"
    
    $ setChannelVolume("sfx", 9, 0.4, 1.0)
    $ playAudio(sfx_femheavybreath, "sfx", 9, False)

    show ep05_hosd3_amb42 with vpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d311'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d312'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d313'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d314'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d315'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d316'])]"
    
    show ep05_hosd3_amb41 with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d317'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d318'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d319'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d320'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d321'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d322'])]"
    
    show ep05_hosd3_amb43 with hpunch
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d323'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d324'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d325'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d326'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d327'])]"
    
    menu:
        "Cum inside Amber":
            $ setChannelVolume("sfx", 2, 0.2, 0)
            $ playAudio(sfx_moan_orgasm_generic, "sfx", 2, False)
            
            pause 0.8
            pass

    show white zorder 1.0 at ejaculation_flash
    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_cum_bigload_fast, "sfx", 1, False)

    show ep05_hosd3_amb44 at vpunch with flash
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d328'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d329'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d330'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d331'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d332'])]"
    mc_t "[renpy.substitute(dialogues5['E05_AMBHO_d333'])]"

    $ ss.add("amber", "sex")
    $ ss.add("amber", "creampie")
    
    show ep05_hosd3_amb45
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d334'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d335'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d336'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d337'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d338'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d339'])]"
    
    $ stopAudio("music", 2, 2)
    $ stopAllSubchannels("sfx", 2)
    $ setChannelVolume("amb", 4, 0.6, 2)
    $ setChannelVolume("amb", 5, 0.2, 2)


    scene eigengrau with slowfade
    show ep05_hosd3_amb46 at ken_burns_bottom_to_top
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d340'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d341'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d342'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d343'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d344'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d345'])]"
    
    show ep05_hosd3_amb47 at ken_burns_left_to_right
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d346'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d347'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d348'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d349'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d350'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d351'])]"
    
    show ep05_hosd3_amb48
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d352'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d353'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d354'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d355'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d356'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d357'])]"
    
    show ep05_hosd3_amb49
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d358'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d359'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d360'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d361'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d362'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d363'])]"
    
    show ep05_hosd3_amb50
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d364'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d365'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d366'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d367'])]"
    
    show ep05_hosd3_amb51
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d370'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d371'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d372'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d373'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d374'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d375'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d376'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d377'])]"

    $ setChannelVolume("sfx", 3, 0.1, 0)
    $ playAudio(sfx_phone, "sfx", 3, False)
    
    show ep05_hosd3_amb52 with slowfade
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d378'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d379'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d380'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d381'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d382'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d383'])]"

    scene eigengrau with slowfade

    $ setChannelVolume("music", 3, 0.3, 0)
    $ playAudio(amber_theme, "music", 3, True, 4, 0)

    show ep05_hosd3_amb53 at ken_burns_left_to_right
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d384'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d121'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d386'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d387'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d388'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d389'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d390'])]"
    
    show ep05_hosd3_amb54
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d391'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d392'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d393'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d394'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d395'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d396'])]"
    
    show ep05_hosd3_amb55
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d397'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d135'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d399'])]"
    mc_s "[renpy.substitute(dialogues5['E05_AMBHO_d400'])]"
    amb "[renpy.substitute(dialogues5['E05_AMBHO_d401'])]"
    
    $ stopAllAudio(2.0)

    jump ep05_elidream    

label ep05_elidream:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3

    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    $ setChannelVolume("amb", 2, 0.15, 0)
    $ playAudio(sfx_heart_monitor, "amb", 2, True, 2, 0)
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_clinicroom, "amb", 3, True, 2, 0)

    show ep05_hosd3_eli20 at ken_burns_right_to_left
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d001'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d002'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d003'])]"
    
    $ stopAllSubchannels("amb", 2)

    scene eigengrau with bokeh

    $ setChannelVolume("amb", 4, 0.6, 0)
    $ playAudio(sfx_fashion, "amb", 4, True, 2, 0)
    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(photos_theme, "music", 1, True, 4, 0)

    show ep05_hosd3_eli01 at focus_shift with clouds_inverse
    "Producer" "[renpy.substitute(dialogues5['E05_ELIDR_d239'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d004'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d006'])]"
    
    $ setChannelVolume("sfx", 1, 0.3, 0)
    $ playAudio(sfx_cameras_photoshoot, "sfx", 1, False, 4, 4)

    show ep05_hosd3_eli02
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d007'])]"
    
    $ show_walkthrough("ep05_elid_m1")
    menu:
        "It's fine, Mom. I like watching you work.":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d008'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d009'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d010'])]"

            $ rm.update("elizabeth", "trust", 4)
            $ check_levels("elizabeth", "trust", 4)
        
        "It's okay. Better than being home alone.":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d011'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d012'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d013'])]"

            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
        
        "I don't mind waiting around.":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d014'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d015'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d016'])]"
    
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d017'])]"
    
    $ show_walkthrough("ep05_elid_m2")
    menu:
        "I shouldn't be looking at her like this...":
            $ ep05_guilt_points += 1
            hide screen walkthrough_screen

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d018'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d019'])]"
        
        "She looks incredible in that dress":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d020'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d021'])]"

            $ rm.update("elizabeth", "cor", 1)
            $ check_levels("elizabeth", "cor", 1)
        
        "I'll just focus on something else":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d022'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d023'])]"

            $ rm.update("elizabeth", "cor", -1)
            $ check_levels("elizabeth", "cor", -1)
    
    show ep05_hosd3_eli03
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d024'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d025'])]"
    
    $ show_walkthrough("ep05_elid_m3")
    menu:
        "I'll always be here for you, Mom.":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d026'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d027'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d028'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d029'])]"

            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
        
        "I try my best not to let you down.":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d030'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d031'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d032'])]"

            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
        
        "That's what family does.":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d033'])]"
            eli "[renpy.substitute(dialogues5['E05_ELIDR_d034'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d035'])]"
    
    show ep05_hosd3_eli04
    "Producer" "[renpy.substitute(dialogues5['E05_ELIDR_d240'])]"
    "Producer" "[renpy.substitute(dialogues5['E05_ELIDR_d241'])]"
    "Producer" "[renpy.substitute(dialogues5['E05_ELIDR_d242'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d036'])]"
    
    $ stopAudio("music", 1, 2)
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)

    scene eigengrau with slowfade

    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_hotel_lobby, "amb", 3, True, 2, 0)

    show ep05_hosd3_eli05 at focus_shift
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d037'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d038'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d039'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d040'])]"
    
    $ stopAudio("amb", 3, 2)

    scene eigengrau with slowfade

    $ setChannelVolume("amb", 4, 0.6, 0)
    $ playAudio(sfx_room_noise, "amb", 4, True, 2, 0)

    show ep05_hosd3_eli06 at ken_burns_left_to_right
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d041'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d042'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d043'])]"
    
    $ show_walkthrough("ep05_elid_m4")
    menu:
        "I should leave immediately":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d044'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d045'])]"

            $ rm.update("elizabeth", "cor", -1)
            $ check_levels("elizabeth", "cor", -1)
        
        "I should see if she's okay":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d046'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d047'])]"
        
        "I'll just pretend I didn't see anything":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d048'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d049'])]"

            $ rm.update("elizabeth", "cor", -2)
            $ check_levels("elizabeth", "cor", -2)
    
    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(elizabeth_sexy_theme, "music", 2, True, 4, 0)
    
    scene eigengrau with slowfade

    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_door_open_creak, "sfx", 1, False, 0, 0)
    $ setChannelVolume("amb", 4, 0.3, 1)

    show ep05_hosd3_eli07 at camera_zoom
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d050'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d051'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d052'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d053'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d054'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d055'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d056'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d057'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d058'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d059'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d060'])]"
    
    show ep05_hosd3_eli08 at ken_burns_corner_to_corner3
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d061'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d062'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d063'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d064'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d065'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d066'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d067'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d068'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d069'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d070'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d071'])]"
    
    $ setChannelVolume("sfx", 2, 0.8, 0)
    $ playAudio(sfx_female_hmm2, "sfx", 2, False, 2, 0)

    show ep05_hosd3_eli28 #anim
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d072'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d073'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d074'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d075'])]"
    
    show ep05_hosd3_eli09
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d076'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d077'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d078'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d079'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d080'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d081'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d082'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d083'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d084'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d085'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d086'])]"
    
    show ep05_hosd3_eli10
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d087'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d088'])]"

    $ show_walkthrough("ep05_elid_m5")
    menu:
        "I want to respond, to comfort her...":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d089'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d090'])]"

            $ rm.update("elizabeth", "cor", -1)
            $ check_levels("elizabeth", "cor", -1)
            
        "I shouldn't be hearing this...":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d091'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d092'])]"

            $ rm.update("elizabeth", "cor", 1)
            $ check_levels("elizabeth", "cor", 1)
        
        "I need to stay completely silent":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d093'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d094'])]"

            $ rm.update("elizabeth", "cor", -2)
            $ check_levels("elizabeth", "cor", -2)

    eli "[renpy.substitute(dialogues5['E05_ELIDR_d095'])]"

    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d096'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d097'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d098'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d099'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d100'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d101'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d102'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d103'])]"
    
    scene eigengrau
    show ep05_hosd3_eli24 #anim
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d104'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d105'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d106'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d107'])]"
    
    scene eigengrau

    $ setChannelVolume("sfx", 3, 0.8, 0)
    $ playAudio(sfx_inhale_fem2, "sfx", 3, False, 2, 0)

    show ep05_hosd3_eli25 #anim
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d108'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d109'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d110'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d111'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d112'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d113'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d114'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d115'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d116'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d117'])]"
    
    scene eigengrau
    show ep05_hosd3_eli27 #anim
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d118'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d119'])]"
    
    scene eigengrau
    show ep05_hosd3_eli26 #anim
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d120'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d121'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d122'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d123'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d124'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d125'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d126'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d127'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d128'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d129'])]"
    
    show ep05_hosd3_eli11 with normalfade
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d130'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d131'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d132'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d133'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d134'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d135'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d136'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d137'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d138'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d139'])]"
    
    show ep05_hosd3_eli12
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d140'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d141'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d142'])]"
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d143'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d144'])]"
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d145'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d146'])]"
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d147'])]"
    else:
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d148'])]"
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d149'])]"
    
    $ stopAudio("music", 2, 2)
    $ setChannelVolume("amb", 4, 0.6, 1)
    
    scene eigengrau with slowfade
    show ep05_hosd3_eli13
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d150'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d151'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d152'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d153'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d154'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d155'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d156'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d157'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d158'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d159'])]"
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d160'])]"
    
    # CURIOSITY PATH REWARD
    if ep05_curiosity_points >= 3:
        show ep05_hosd3_eli14
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d161'])]"
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d162'])]"
        
        if ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d163'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d164'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d165'])]"
        elif ep05_guilt_points > ep05_evasive_points:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d166'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d167'])]"
        else:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d168'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d169'])]"
        
        $ ep05_ach_final2 = True
        
    else:
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d161'])]"
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d162'])]"
        
        if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d172'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d173'])]"
        elif ep05_evasive_points > ep05_curiosity_points:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d174'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d175'])]"
        else:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d176'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d177'])]"
    
    show ep05_hosd3_eli15
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d178'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d179'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d180'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d181'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d182'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d183'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d184'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d185'])]"
    else:
        mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d186'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d187'])]"
    
    show ep05_hosd3_eli16
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d188'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d189'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d190'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d191'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d192'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d164'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d194'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d195'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d196'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d197'])]"
    
    $ stopAllSubchannels("amb", 2)

    scene eigengrau with slowfade

    $ setChannelVolume("music", 5, 0.3, 0)
    $ playAudio(elizabeth_theme, "music", 5, True, 4, 0)
    $ setChannelVolume("amb", 6, 0.4, 0)
    $ playAudio(sfx_nightclub, "amb", 6, True, 2, 0)

    show ep05_hosd3_eli17
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d198'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d199'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d200'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d201'])]"
    
    show ep05_hosd3_eli18
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d202'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d203'])]"
    
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d204'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d205'])]"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d206'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d207'])]"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d208'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d209'])]"
    else:
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d210'])]"
        mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d211'])]"
    
    # GUILT PATH REWARD
    if ep05_guilt_points >= 3:
        show ep05_hosd3_eli19
        if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d212'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d213'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d214'])]"
        elif ep05_curiosity_points > ep05_evasive_points:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d215'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d216'])]"
        else:
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d217'])]"
            mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d218'])]"
        
        eli "[renpy.substitute(dialogues5['E05_ELIDR_d219'])]"

        $ ep05_ach_final1 = True
    
    show ep05_hosd3_eli18 at focus_shift_sms
    
    $ stopAudio("music", 5, 2)
    $ stopAllSubchannels("amb", 2)

    pause 1

    scene eigengrau with clouds

    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    $ setChannelVolume("amb", 2, 0.15, 0)
    $ playAudio(sfx_heart_monitor, "amb", 2, True, 2, 0)
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_clinicroom, "amb", 3, True, 2, 0)

    show ep05_hosd3_eli21
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d220'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d221'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d222'])]"
    
    show ep05_hosd3_eli22
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d223'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d224'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d225'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d226'])]"
    mc_s "[renpy.substitute(dialogues5['E05_ELIDR_d227'])]"
    eli "[renpy.substitute(dialogues5['E05_ELIDR_d228'])]"
    
    $ setChannelVolume("sfx", 1, 0.1, 0)
    $ playAudio(sfx_phone, "sfx", 1, False, 1, 1)

    show ep05_hosd3_eli23
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d229'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d230'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d231'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d232'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d233'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d234'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d235'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d236'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d237'])]"
    mc_t "[renpy.substitute(dialogues5['E05_ELIDR_d238'])]"
    
    $ stopAllAudio(2.0)

    jump ep05_hosfinal

label ep05_hosfinal:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0

    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    
    show ep05_hosd3_mic01
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d001'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d002'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d003'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d004'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d005'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d006'])]"
    
    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(mic_theme, "music", 1, True, 4, 0)
    
    show ep05_hosd3_mic02 with hpunch
    mad "[renpy.substitute(dialogues5['E05_MICMC_d007'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d008'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d009'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d010'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d011'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d012'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d013'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d014'])]"
    
    show ep05_hosd3_mic03
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d015'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d016'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d017'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d018'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d019'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d020'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d021'])]"
    
    $ show_walkthrough("ep05_mcmic_m1")
    menu:
        "Demand the truth about her medication":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", -5)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d022'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d023'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d024'])]"
        
        "Ask for specifics about her treatment":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d025'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d026'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d027'])]"
        
        "Assert your right to know as her son":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", 5)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d028'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d029'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d030'])]"
    
    show ep05_hosd3_mic04
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d031'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d032'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d033'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d034'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d035'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d036'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d037'])]"
    
    show ep05_hosd3_mic05
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d038'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d039'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d040'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d041'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d042'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d043'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d044'])]"
    
    show ep05_hosd3_mic06
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d045'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d046'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d047'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d048'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d049'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d050'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d051'])]"
    
    $ show_walkthrough("ep05_mcmic_m2")
    menu:
        "Accuse him of hiding something":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", -8)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d052'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d053'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d054'])]"
        
        "Challenge his medical practices":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d055'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d056'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d057'])]"
        
        "Threaten to involve medical authorities":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", 8)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d058'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d059'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d060'])]"
    
    show ep05_hosd3_mic07
    mic "[renpy.substitute(dialogues5['E05_MICMC_d061'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d062'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d063'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d064'])]"

    show ep05_hosd3_mic08
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d065'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d066'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d067'])]"
    
    $ show_walkthrough("ep05_mcmic_m3")
    menu:
        "Angrily accuse him of experimenting":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", -10)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d068'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d069'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d070'])]"
        
        "Question Elizabeth's knowledge of the treatment":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d071'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d072'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d073'])]"
        
        "Point out the legal and ethical violations":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", 10)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d074'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d075'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d076'])]"
    
    show ep05_hosd3_mic09
    mic "[renpy.substitute(dialogues5['E05_MICMC_d077'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d078'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d079'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d080'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d081'])]"
    
    show ep05_hosd3_mic10
    mic "[renpy.substitute(dialogues5['E05_MICMC_d082'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d083'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d084'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d085'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d086'])]"
    
    show ep05_hosd3_mic11 at ken_burns_bottom_to_top
    mic "[renpy.substitute(dialogues5['E05_MICMC_d087'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d088'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d089'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d090'])]"
    
    show ep05_hosd3_mic12 at ken_burns_right_to_left
    mic "[renpy.substitute(dialogues5['E05_MICMC_d091'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d092'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d093'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d094'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d095'])]"
    
    $ show_walkthrough("ep05_mcmic_m4")
    menu:
        "Threaten to take matters into your own hands":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", -12)

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d096'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d097'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d098'])]"
        
        "Promise to investigate officially":
            hide screen walkthrough_screen

            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d099'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d100'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d101'])]"
        
        "Threaten to file a formal report":
            hide screen walkthrough_screen

            $ rm.update("mc", "integrity", 8)
            
            mc_s "[renpy.substitute(dialogues5['E05_MICMC_d102'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d103'])]"
            mic "[renpy.substitute(dialogues5['E05_MICMC_d104'])]"
    
    show ep05_hosd3_mic13
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d105'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d106'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d107'])]"
    
    show ep05_hosd3_mic14
    mic "[renpy.substitute(dialogues5['E05_MICMC_d108'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d109'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d110'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d111'])]"
    
    show ep05_hosd3_mic15
    mic "[renpy.substitute(dialogues5['E05_MICMC_d112'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d113'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d114'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d115'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d116'])]"
    
    show ep05_hosd3_mic16
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d117'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d118'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d119'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d120'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d121'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d122'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d123'])]"
    
    show ep05_hosd3_mic17
    mic "[renpy.substitute(dialogues5['E05_MICMC_d124'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d125'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d126'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d127'])]"
    mad "[renpy.substitute(dialogues5['E05_MICMC_d128'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d129'])]"
    
    show ep05_hosd3_mic18 at ken_burns_bottom_to_top
    mic "[renpy.substitute(dialogues5['E05_MICMC_d130'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d131'])]"
    mc_s "[renpy.substitute(dialogues5['E05_MICMC_d132'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d133'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d134'])]"
    
    show ep05_hosd3_mic19
    mic "[renpy.substitute(dialogues5['E05_MICMC_d135'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d136'])]"
    mic "[renpy.substitute(dialogues5['E05_MICMC_d137'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d138'])]"

    $ stopAudio("music", 1, 2)
    
    scene eigengrau with slowfade

    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(mc_broken_theme, "music", 2, True, 4, 0)

    show ep05_hosd3_mic20 at ken_burns_left_to_right
    mad "[renpy.substitute(dialogues5['E05_MICMC_d139'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d140'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d141'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d142'])]"
    
    show ep05_hosd3_mic21 at subtle_zoom_out
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d143'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d144'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d145'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d146'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d147'])]"
    mc_t "[renpy.substitute(dialogues5['E05_MICMC_d148'])]"
    
    $ stopAllAudio(2)

    jump ep05_end

label ep05_end:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0

    show loc_murderroom_night with slowfade
    show murderroom_location zorder 2 with dissolve
    pause 4
    hide murderroom_location with dissolve

    $ setChannelVolume("amb", 1, 0.5, 0)
    $ playAudio(sfx_factory, "amb", 1, True, 2, 0)
    $ setChannelVolume("music", 1, 0.5, 0)
    $ playAudio(antonella_horror_theme, "music", 1, True, 4, 0)

    show ep05_end01 at ken_burns_bottom_to_top
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d002'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d003'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d001'])]"
    
    show ep05_end02
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d004'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d005'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d002'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d006'])]"
    
    show ep05_end03
    surg "[renpy.substitute(dialogues5['E05_RNDM_d044'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d003'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d007'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d008'])]"
    
    show ep05_end04
    surg "[renpy.substitute(dialogues5['E05_ENDAC_d004'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d009'])]"
    surg "[renpy.substitute(dialogues5['E05_ENDAC_d005'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d010'])]"
    
    show ep05_end05
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d006'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d011'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d012'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d007'])]"
    
    show ep05_end06
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d008'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d013'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d009'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d014'])]"
    
    show ep05_end07
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d010'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d015'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d011'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d016'])]"
    
    show ep05_end08
    surg "[renpy.substitute(dialogues5['E05_RNDM_d017'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d012'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d018'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d019'])]"
    
    show ep05_end09
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d020'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d021'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d022'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d013'])]"
    
    scene eigengrau with slowfade

    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)
    $ setChannelVolume("sfx", 3, 0.5, 0)
    $ playAudio(sfx_blood_splash, "sfx", 3, False, 0, 0)

    show ep05_end10 at ken_burns_corner_to_corner3
    surg "[renpy.substitute(dialogues5['E05_RNDM_d023'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d014'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d024'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d025'])]"
    
    show ep05_end11
    surg "[renpy.substitute(dialogues5['E05_RNDM_d026'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d015'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d027'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d016'])]"
    
    show ep05_end12
    surg "[renpy.substitute(dialogues5['E05_RNDM_d028'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d017'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d029'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d018'])]"
    
    $ setChannelVolume("amb", 1, 0, 2)

    show ep05_end13 with slowfade
    $ setChannelVolume("sfx", 9, 1, 0)
    $ playAudio(sfx_heartbeatslow, "sfx", 9, True, 0, 0)

    anto "[renpy.substitute(dialogues5['E05_ENDAC_d019'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d030'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d020'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d021'])]"
    
    show ep05_end14
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d031'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d022'])]"
    "Unknown Woman" "[renpy.substitute(dialogues5['E05_RNDM_d032'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d023'])]"
    $ stopAudio("sfx", 9, 0)
    
    scene eigengrau with slowfade

    $ setChannelVolume("sfx", 4, 0.5, 0)
    $ playAudio(sfx_knife_jab, "sfx", 4, False, 0, 0)
    $ setChannelVolume("amb", 1, 0.5, 0)

    show ep05_end15
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d024'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d033'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d025'])]"
    surg "[renpy.substitute(dialogues5['E05_RNDM_d034'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d026'])]"
    
    $ stopAudio("music", 1, 2)
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)

    scene eigengrau with slowfade

    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(yakuza_theme, "music", 2, True, 4, 0)
    $ setChannelVolume("amb", 2, 0.3, 0)
    $ playAudio(sfx_eveningtraffic, "amb", 2, True, 2, 0)

    show ep05_end16 at ken_burns_left_to_right
    hir "[renpy.substitute(dialogues5['E05_RNDM_d035'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d027'])]"
    hir "[renpy.substitute(dialogues5['E05_RNDM_d036'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d028'])]"
    
    show ep05_end17
    hir "[renpy.substitute(dialogues5['E05_RNDM_d037'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d029'])]"
    hir "[renpy.substitute(dialogues5['E05_RNDM_d038'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d030'])]"
    
    show ep05_end18
    hir "[renpy.substitute(dialogues5['E05_RNDM_d039'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d031'])]"
    hir "[renpy.substitute(dialogues5['E05_RNDM_d040'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d032'])]"
    
    show ep05_end19
    hir "[renpy.substitute(dialogues5['E05_RNDM_d041'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d033'])]"
    hir "[renpy.substitute(dialogues5['E05_RNDM_d042'])]"
    anto "[renpy.substitute(dialogues5['E05_ENDAC_d034'])]"
    hir "[renpy.substitute(dialogues5['E05_RNDM_d043'])]"
    
    $ stopAudio("music", 2, 2)
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)

    scene eigengrau with slowfade

    show loc_templeasak_night with slowfade
    show asakusa_location zorder 2 with dissolve
    pause 4
    hide asakusa_location with dissolve

    $ setChannelVolume("music", 3, 0.6, 0)
    $ playAudio(antonella_singing_act1, "music", 3, True, 4, 0)
    $ setChannelVolume("amb", 3, 0.3, 0)
    $ playAudio(sfx_temple_outside, "amb", 3, True, 2, 0)

    show ep05_end20 at subtle_zoom_out
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d035'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d036'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d037'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d038'])]"
    
    show ep05_end21
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d039'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d040'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d041'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d042'])]"
    
    show ep05_end22 at ken_burns_top_to_bottom
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d043'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d044'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d045'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d046'])]"
    
    show ep05_end23 at ken_burns_bottom_to_top with slowfade
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d047'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d048'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d049'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d050'])]"
    
    show ep05_end24 
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d051'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d052'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d053'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d054'])]"
    
    show ep05_end25 at ken_burns_right_to_left
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d055'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d056'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d057'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d058'])]"
    
    show ep05_end26 at subtle_zoom_out with smoke
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d059'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d060'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d061'])]"
    anto_t "[renpy.substitute(dialogues5['E05_ENDAC_d062'])]"
    
    hide screen stats_button
    hide screen walkthrough_icon
    
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)

    jump act1_ending

label act1_ending:
    scene eigengrau with rose

    show act1_ending_bg at slow_reveal zorder 1

    pause 2.0

    show sakura_movie zorder 2

    if htl_episodes == 5.3:
        $ show_custom_notification("save_tip")
    else:
        pass

    pause 6.0

    show the_end_text zorder 3 with dissolve:
        alpha 0.0
        zoom 0.8
        yoffset 30
        linear 3.0 alpha 1.0 zoom 1.0 yoffset 0
    
    pause 4.0
    
    show of_text zorder 3 with dissolve:
        alpha 0.0
        xoffset -50
        linear 2.0 alpha 1.0 xoffset 0
    
    pause 2.5
    
    show act_one_text zorder 3 with dissolve:
        alpha 0.0
        zoom 0.7
        linear 2.5 alpha 1.0 zoom 1.0
    
    pause 4.0

    $ renpy.call_screen("forced_pause")
    
    hide act_one_text with dissolve
    hide of_text with dissolve
    hide the_end_text with dissolve
    
    pause 1.5
    
    #-- End Episode 5
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
    pause 2.0
    if htl_episodes == 5.3:
        return
    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep05_title