default sawpic_ep03_sms1 = False

image thumb_ep03_sms1:
    "sms/thumb_ep03_sms1.png" 
    yoffset -5
    
image ep03_sms1 = Composite(
    (1920,1080),
    (0,0), AlphaMask("sms/ep03_06_12.avif", "gui/masksms_h.png"),
    (0,0), "gui/bordersms_h.png"
)

screen picview_ep03_sms1:
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
        add "ep03_sms1"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep03_sms1"), SetVariable("sawpic_ep03_sms1", True)]
            style "igm_button"
            focus_mask None

#-- ISA SMS
label ep03_sms01:
    nvl clear
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(isabella_theme, "music", 1, True, 2, 0)
    show ep03_antoback02 with slowfade
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d001'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d002'])]"
    if not smstip_seen:
        $ show_custom_notification("sms_tip")
        $ smstip_seen = True
    else:
        pass
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d003'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d004'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d005'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d006'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d007'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d008'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d009'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d010'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d011'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d012'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d013'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d014'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d015'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d016'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d017'])]"
    if not smstip2_seen:
        $ show_custom_notification("sms_tip2")
        $ smstip2_seen = True
    else:
        pass
    if sawpic_ep03_sms1: #FORCE PICTURE SHOULD BE ALWAYS AFTER THE THUMBNAIL.
        pass
    else:
        show screen picview_ep03_sms1
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d018'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d019'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d020'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d021'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d022'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d023'])]"
    isa_nvl "[renpy.substitute(dialogues3['E03ISASMS_d024'])]"
    mc_nvl "[renpy.substitute(dialogues3['E03ISASMS_d025'])]"
    $ stopAllSubchannels(channel="music", fadeout=2)
    hide ep03_antoback02
    show ep03_antoback01
    mc_t "[renpy.substitute(dialogues3['E03ISASMS_d026'])]"
    mc_t "[renpy.substitute(dialogues3['E03ISASMS_d027'])]"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_boxes
#-- TOTAL POINTS AVAILABLE:
    


