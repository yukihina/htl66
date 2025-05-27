transform phone_sms_icon:
    subpixel True
    ease 0.1 xoffset 24
    ease 0.1 xoffset 0
    ease 0.08 xoffset -20
    ease 0.08 xoffset 0
    ease 0.06 xoffset 16
    ease 0.06 xoffset 0
    ease 0.04 xoffset -12
    ease 0.04 xoffset 0
    ease 0.02 xoffset 8
    ease 0.02 xoffset 0
    ease 0.01 xoffset -4
    ease 0.01 xoffset 0
    linear 0.5 xoffset 0
    repeat


transform phone_icon_alpha:
    on show:
        subpixel True
        alpha 0.65
    on hover:
        subpixel True
        ease 0.5 alpha 1.0
    on idle:
        subpixel True
        ease 0.5 alpha 0.65


screen phone_icons(jump_to):
    add "vignette" at igm_appear_bg alpha 0.45
    frame at igm_appear_fg:
        vbox:
            xalign 0.5
            yalign 0.35
            add "gui/phone_sms.png" at phone_sms_icon yalign 0.5 xalign 0.5
            #add AnimatedWave("gui/phone_sms.png", wave_amplitude=20, wave_frequency=0.1, wave_speed=5)
        hbox:
            spacing 80
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "gui/open_off.png"
                hover "gui/open_on.png"
                action [Hide("phone_icons"), Jump(jump_to)]
                at phone_icon_alpha
            imagebutton:
                idle "gui/close_off.png"
                hover "gui/close_on.png"
                action [Hide("phone_icons"), Return()]
                at phone_icon_alpha

screen videocall_icons(jump_to):
    add "vignette" at igm_appear_bg alpha 0.45
    frame at igm_appear_fg:
        vbox:
            xalign 0.5
            yalign 0.35
            add "gui/phone_vc.png" at phone_sms_icon yalign 0.5 xalign 0.5
        hbox:
            spacing 80
            xalign 0.5
            yalign 0.5
            imagebutton:
                idle "gui/open_off.png"
                hover "gui/open_on.png"
                action [Hide("phone_icons"), Jump(jump_to)]
                at phone_icon_alpha


screen menu_button(*args):
    modal True    
    frame:
        add "achtung" at igm_appear_fg:
                align (0.07, 0.4)
        xpos 800
        yalign 0.5
        vbox:
            style_prefix "choice"
            for i in range(0, len(args), 2):
                $ option_text = args[i]
                $ option_label = args[i+1]
                textbutton "[option_text]" action [Hide("menu_button"), Jump(option_label)] at igm_appear_fg2