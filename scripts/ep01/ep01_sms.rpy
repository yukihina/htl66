default sawpic_ep01_sms5 = False
default sawpic_ep01_sms4 = False
default sawpic_ep01_sms6 = False

transform sms_thumb_t:
    on show:
        subpixel True
        alpha 0.65
    on hover:
        subpixel True
        ease 0.5 alpha 1.0
    on idle:
        subpixel True
        ease 0.5 alpha 0.65

image thumb_ep01_sms4:
    "sms/thumb_ep01_sms4.png" 
    yoffset -5

image thumb_ep01_sms5:
    "sms/thumb_ep01_sms5.png" 
    yoffset -5 

image thumb_ep01_sms6:
    "sms/thumb_ep01_sms6.png" 
    yoffset -5
    
image ep01_sms4 = Composite(
    (1080,1920),
    (0,0), AlphaMask("sms/ep01_sms4.avif", "gui/masksms_v.png"),
    (0,0), "gui/bordersms_v.png"
)

image ep01_sms5 = Composite(
    (1080,1920),
    (0,0), AlphaMask("sms/ep01_sms5.avif", "gui/masksms_v.png"),
    (0,0), "gui/bordersms_v.png"
)

image ep01_sms6 = Composite(
    (1920,1080),
    (0,0), AlphaMask("sms/ep01_sms6.avif", "gui/masksms_h.png"),
    (0,0), "gui/bordersms_h.png"
)

screen picview_ep01_sms4:
    add "black" at igm_appear_bg alpha 0.5
    add "vignette" at igm_appear_bg alpha 0.5
    modal True
    
    viewport at igm_appear_fg2:
        xsize 1018
        ysize 1018
        xpos 860
        ypos 20
        draggable True
        mousewheel True
        arrowkeys True
        add "ep01_sms4"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep01_sms4"), SetVariable("sawpic_ep01_sms4", True)]
            style "igm_button"
            focus_mask None


screen picview_ep01_sms5:
    add "black" at igm_appear_bg alpha 0.5
    add "vignette" at igm_appear_bg alpha 0.5
    modal True
    viewport at igm_appear_fg:
        xsize 1018
        ysize 1018
        xpos 860
        ypos 20
        draggable True
        mousewheel True
        arrowkeys True
        add "ep01_sms5"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep01_sms5"), SetVariable("sawpic_ep01_sms5", True)]
            style "igm_button"
            focus_mask None

screen picview_ep01_sms6:
    add "black" at igm_appear_bg alpha 0.5
    add "vignette" at igm_appear_bg alpha 0.5
    modal True
    
    viewport at igm_appear_fg2:
        xsize 1018
        ysize 1018
        xpos 860
        ypos 20
        draggable True
        mousewheel True
        arrowkeys True
        add "ep01_sms6"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep01_sms6"), SetVariable("sawpic_ep01_sms6", True)]
            style "igm_button"
            focus_mask None

#-- PAZ SMS
label ep01_sms01:
    nvl clear
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    show ep01_3rddream20 with slowfade
    mc_t "[renpy.substitute(dialogues['E01S04_d077'])]"
    show ep01_3rddream21
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d001'])]"
    if not smstip_seen:
        $ show_custom_notification("sms_tip")
        $ smstip_seen = True
    else:
        pass
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d002'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d003'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d004'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d005'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d006'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d007'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d008'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d009'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d010'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d011'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d012'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d013'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d014'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d015'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d016'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d017'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d018'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d019'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d020'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d021'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d022'])]"
    if not smstip2_seen:
        $ show_custom_notification("sms_tip2")
        $ smstip2_seen = True
    else:
        pass
    if sawpic_ep01_sms5: #FORCE PICTURE SHOULD BE ALWAYS AFTER THE THUMBNAIL.
        pass
    else:
        show screen picview_ep01_sms5
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d023'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d024'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d025'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS1_d026'])]"
    #MENU
    $ show_walkthrough("ep01_sms01_wt1")
    show screen menu_button ("Joke about it", "ep01_sms01_joke", "Get serious", "ep01_sms01_serious") #MENU SHOULD BE ALWAYS WITH A DIALOGUE AFTER.
    paz_nvl "[renpy.substitute(dialogues['E01SMS1_d027'])]"    

label ep01_sms01_joke:
    $ rm.update("paz", "trust", 2)
    $ check_levels("paz", "trust", 2)
    hide screen walkthrough_screen
    mc_nvl "[renpy.substitute(dialogues['E01SMS2_d001'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d002'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS2_d003'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d004'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d005'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d006'])]"
    if sawpic_ep01_sms4:
        pass
    else:
        show screen picview_ep01_sms4
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d007'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS2_d008'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d009'])]"
    #MENU
    $ show_walkthrough("ep01_sms01_wt2")
    show screen menu_button ("Say sorry", "ep01_sms01_sorry", "Flirt", "ep01_sms01_flirt")
    paz_nvl "[renpy.substitute(dialogues['E01SMS2_d010'])]"
    
label ep01_sms01_flirt:
    $ rm.update("paz", "trust", 2)
    $ check_levels("paz", "trust", 2)
    hide screen walkthrough_screen
    mc_nvl "[renpy.substitute(dialogues['E01SMS3_d001'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS3_d002'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d003'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d004'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS3_d005'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d006'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d007'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS3_d008'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d009'])]"
    $ rm.update("paz", "cor", 1)
    $ check_levels("paz", "cor", 1)
    if sawpic_ep01_sms6:
        pass
    else:
        show screen picview_ep01_sms6
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d010'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d011'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS3_d012'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS3_d013'])]"
    jump ep01_smslater

label ep01_sms01_sorry:
    $ rm.update("paz", "trust", 1)
    $ check_levels("paz", "trust", 1)
    hide screen walkthrough_screen
    mc_nvl "[renpy.substitute(dialogues['E01SMS4_d001'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS4_d002'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS4_d003'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS4_d004'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS4_d005'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS4_d006'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS4_d007'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS4_d008'])]"
    jump ep01_smslater

label ep01_sms01_serious:
    $ rm.update("paz", "trust", 1)
    $ check_levels("paz", "trust", 1)
    hide screen walkthrough_screen
    mc_nvl "[renpy.substitute(dialogues['E01SMS5_d001'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d002'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d003'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d004'])]"
    if sawpic_ep01_sms4:
        pass
    else:
        show screen picview_ep01_sms4
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d005'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS5_d006'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d007'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS5_d008'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d009'])]"
    paz_nvl "[renpy.substitute(dialogues['E01SMS5_d010'])]"
    jump ep01_smslater

#-- ELIZABETH SMS
label ep01_sms02:
    nvl clear
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    show ep01_pregame35 with slowfade
    mc_t "[renpy.substitute(dialogues['E01SMS6_d001'])]"
    mc_t "[renpy.substitute(dialogues['E01SMS6_d002'])]"
    show ep01_pregame36
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d003'])]"
    if not smstip_seen:
        $ show_custom_notification("sms_tip")
        $ smstip_seen = True
    else:
        pass
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d004'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d005'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d006'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d007'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d008'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d009'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d010'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d011'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d012'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d013'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d014'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d015'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d016'])]"
    eli_nvl "[renpy.substitute(dialogues['E01SMS6_d017'])]"
    mc_nvl "[renpy.substitute(dialogues['E01SMS6_d018'])]"
    pause 0.1
    mc_t "[renpy.substitute(dialogues['E01S05_d159'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d160'])]"
    mc_t "[renpy.substitute(dialogues['E01S05_d161'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_pregame2

#-- TOTAL POINTS AVAILABLE:
    #PAZ TRUST: +2 OR +1
    #PAZ TRUST: +1
    #PAZ COR: +1
