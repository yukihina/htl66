default sawpic_ep05_sms01 = False
default sawpic_ep05_sms02 = False
default sawpic_ep05_sms03 = False
default sawpic_ep05_sms04 = False

image thumb_ep05_sms01:
    "sms/thumb_ep05_sms01.png"
    yoffset -5

image thumb_ep05_sms02:
    "sms/thumb_ep05_sms02.png"
    yoffset -5

image thumb_ep05_sms03:
    "sms/thumb_ep05_sms03.png"
    yoffset -5

image thumb_ep05_sms04:
    "sms/thumb_ep05_sms04.png"
    yoffset -5
    
image ep05_sms01 = Composite(
    (1080,1920),
    (0,0), AlphaMask("sms/paz_message_04.avif", "gui/masksms_v.png"),
    (0,0), "gui/bordersms_v.png"
)

image ep05_sms02 = Composite(
    (1080,1920),
    (0,0), AlphaMask("sms/paz_message_05.avif", "gui/masksms_v.png"),
    (0,0), "gui/bordersms_v.png"
)

image ep05_sms03 = Composite(
    (1920,1080),
    (0,0), AlphaMask("sms/smspaz_mchome1.avif", "gui/masksms_h.png"),
    (0,0), "gui/bordersms_h.png"
)

image ep05_sms04 = Composite(
    (1920,1080),
    (0,0), AlphaMask("sms/smspaz_mchome2.avif", "gui/masksms_h.png"),
    (0,0), "gui/bordersms_h.png"
)

screen picview_ep05_sms01:
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
        add "ep05_sms01"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep05_sms01"), SetVariable("sawpic_ep05_sms01", True)]
            style "igm_button"
            focus_mask None


screen picview_ep05_sms02:
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
        add "ep05_sms02"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep05_sms02"), SetVariable("sawpic_ep05_sms02", True)]
            style "igm_button"
            focus_mask None


screen picview_ep05_sms03:
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
        add "ep05_sms03"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep05_sms03"), SetVariable("sawpic_ep05_sms03", True)]
            style "igm_button"
            focus_mask None


screen picview_ep05_sms04:
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
        add "ep05_sms04"
    imagebutton at igm_appear_fg2:
            xpos 881
            ypos 45
            idle "gui/btn_close_off.png"
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("picview_ep05_sms04"), SetVariable("sawpic_ep05_sms04", True)]
            style "igm_button"
            focus_mask None
#-- PAZ SMS
label ep05_smspaz_phone:
    nvl clear
    show ep05_smspz03_bg
    pause 1
    hide ep05_smspz03
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d001'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d002'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d003'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d004'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d005'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d006'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d007'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d008'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d009'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d010'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d011'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d012'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d013'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d014'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d015'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d016'])]"
    mc_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d017'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d018'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d019'])]"
    paz_nvl "[renpy.substitute(dialogues5['E05PZSMSS_d020'])]"
    jump ep05_smspaz_call



