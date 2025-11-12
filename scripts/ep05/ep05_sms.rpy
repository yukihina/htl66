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
    mc_nvl "Hey... u ok after that attack?"
    paz_nvl "Hey, yea I'm fine. Nothing serious {outlinecolor=#ffffff00}👍{/outlinecolor}"
    paz_nvl "Bitch caught me off guard but I gave back 2x harder {outlinecolor=#ffffff00}💪{/outlinecolor}"
    mc_nvl "Good. Sorry I couldn't be there…"
    mc_nvl "Stuck w/ [fm_r_low] bs when I should be helping"
    paz_nvl "Lol don't sweat it—if u were here u'd prob get shot AGAIN {outlinecolor=#ffffff00}😂{/outlinecolor}"
    paz_nvl "Btw guess what? Still have ur uniform from that day—the one w/ bloodstains + bullet hole"
    paz_nvl "Always getting urself into trouble smh"
    mc_nvl "U kept it? Kinda morbid, Paz... {outlinecolor=#ffffff00}🤨{/outlinecolor}"
    paz_nvl "{a=show:picview_ep05_sms01}{image=thumb_ep05_sms01}"
    mc_nvl "Didn't take u for the souvenir type"
    paz_nvl "Can't wash it. Reminder to stay alert ya know? Not morbid—lucky charm {outlinecolor=#ffffff00}🍀{/outlinecolor}"
    paz_nvl "Almost lost u that day. Not happening again."
    mc_nvl "Strange but whatever works for u..."
    mc_nvl "Still wish I was there. Hate being useless"
    mc_nvl "Wait—u got a phone now? Thought u were still on that ancient desktop app"
    mc_nvl "The one u swore was 'unhackable' {outlinecolor=#ffffff00}🙄{/outlinecolor}"
    paz_nvl "{a=show:picview_ep05_sms02}{image=thumb_ep05_sms02}"
    paz_nvl "Yea got new one. Hang on, gonna call u"
    paz_nvl "Found smth in ur apt. Need to show u ASAP {outlinecolor=#ffffff00}👀{/outlinecolor}"

    jump ep05_smspaz_call


