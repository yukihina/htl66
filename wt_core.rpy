init python:
    walkthrough_all = False
    walkthrough_li = set()
    walkthrough_enabled = False

    def select_all():
        global walkthrough_li
        walkthrough_li = {"amber", "antonella", "arlette", "elizabeth", "isabella", "kanae", "madison", "nanami", "mc", "minigames"}
    def deselect_all():
        global walkthrough_li
        walkthrough_li = set()
    def update_walkthrough_enabled():
        global walkthrough_enabled
        walkthrough_enabled = walkthrough_all or bool(walkthrough_li)

    def create_wt_text(options):
        
        # Generate formatted walkthrough text from simplified option dictionaries.
        
        # Args:
        #     options: List of dictionaries containing:
        #         - option_num: Option number (0 for generic text)
        #         - char_name: Character name
        #         - points: Main effect points value
        #         - type: Effect type ("Love" or "Corruption")
        #         - additional_effects: List of additional point effects
        #         - extra_text: Plain text to append
        
        def format_points_effect(points, effect_type):
            # Format points and effect type with proper colors and emoji
            prefix = "+" if points > 0 else ""
            color = "00ff00" if points > 0 else "ff0000"
            
            if effect_type == "Love":
                return f"{{color=#" + color + f"}}{prefix}{points}{{/color}} {{color=#ff5c5c}}{effect_type} {{outlinecolor=#ffffff00}}❤️{{/outlinecolor}}{{/color}}"
            else:
                return f"{{color=#" + color + f"}}{prefix}{points}{{/color}} {{color=#a86c88}}{effect_type} {{outlinecolor=#ffffff00}}😈{{/outlinecolor}}{{/color}}"

        formatted_text = ""
        for opt in options:
            # Handle option number and character name
            if 'option_num' in opt:
                if opt['option_num'] == 0:
                    formatted_text += f"{{color=#27dc95}}{opt['char_name']}{{/color}} "
                else:
                    formatted_text += f"{{color=#27dc95}}Option {opt['option_num']}:{{/color}} "
                    formatted_text += f"{{color=#ffcc01}}{opt['char_name']}{{/color}} "

            # Add main effect if present
            if 'points' in opt and 'type' in opt:
                formatted_text += format_points_effect(opt['points'], opt['type'])

            # Add any additional effects
            if 'additional_effects' in opt:
                for effect in opt['additional_effects']:
                    formatted_text += " and " + format_points_effect(effect['points'], effect['type'])

            # Add plain extra text if present
            if 'extra_text' in opt:
                formatted_text += " " + opt['extra_text']

            # Add newline if not the last option
            if opt != options[-1]:
                formatted_text += "\n"

        return formatted_text    

screen walkthrough_screen(message):
    add "gui/speech_bubble_att.png" at igm_appear_bg xpos 1314 ypos 166
    add "gui/speech_bubble.png" at igm_appear_bg xpos 1379 ypos 151
    
    frame:
        xpos 1399
        ypos 161
        xsize 367
        ysize 65
        background None
        
        vbox:
            align (0.5, 0.5)  # This centers the content both horizontally and vertically
            text message:
                at igm_appear_fg
                style "wt_tip"
                align (0.5, 0.5)  # This ensures the text itself is centered within the vbox
                text_align 0 # This centers the text content

screen walkthrough_options():
    modal True
    zorder 200
    add "gui/wt_bg.png" at igm_appear, heartbeat(0.99,1.0,1) xpos 488 ypos 54
    add "gui/wt_pop.png" at igm_appear_fg xpos 713 ypos 202
    text "assist manager".upper() at igm_appear_fg2 xpos 949 ypos 622 style "wt_label"
    imagebutton at igm_appear:
            xpos 1170
            ypos 232
            idle "gui/wt_btn_close_off.png"
            hover "gui/wt_btn_close.png"
            hover_offset (0, -2)
            action Hide("walkthrough_options")
            style "igm_button"
            focus_mask None
    hbox:
        xpos 800
        ypos 300
        spacing 100
        
        vbox:
            spacing 27
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [If(walkthrough_all, Function(deselect_all), Function(select_all)), ToggleVariable("walkthrough_all"), Function(update_walkthrough_enabled)]
                    selected walkthrough_all
                text "All" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "amber"), Function(update_walkthrough_enabled)]
                    selected "amber" in walkthrough_li
                text "Amber" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "antonella"), Function(update_walkthrough_enabled)]
                    selected "antonella" in walkthrough_li
                text "Antonella" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "arlette"), Function(update_walkthrough_enabled)]
                    selected "arlette" in walkthrough_li
                text "Arlette" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "elizabeth"), Function(update_walkthrough_enabled)]
                    selected "elizabeth" in walkthrough_li
                text "Elizabeth" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "isabella"), Function(update_walkthrough_enabled)]
                    selected "isabella" in walkthrough_li
                text "Isabella" style "wt_txt" at igm_appear_fg2
        
        vbox:
            spacing 27
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "kanae"), Function(update_walkthrough_enabled)]
                    selected "kanae" in walkthrough_li
                text "Kanae" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "madison"), Function(update_walkthrough_enabled)]
                    selected "madison" in walkthrough_li
                text "Madison" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "nanami"), Function(update_walkthrough_enabled)]
                    selected "nanami" in walkthrough_li
                text "Nanami" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "mc"), Function(update_walkthrough_enabled)]
                    selected "mc" in walkthrough_li
                text "MC" style "wt_txt" at igm_appear_fg2
            
            hbox:
                xalign 0
                yalign 0.5
                spacing 15
                imagebutton at igm_appear:
                    yalign 0.5
                    idle "wt_check_off"
                    hover "wt_check_on"
                    selected_idle "wt_check_on"
                    selected_hover "wt_check_on"
                    action [SetVariable("walkthrough_all", False), ToggleSetMembership(walkthrough_li, "minigames"), Function(update_walkthrough_enabled)]
                    selected "minigames" in walkthrough_li
                text "Minigames" style "wt_txt" at igm_appear_fg2

image wt_check_on:
    "gui/checkbox_square_on.png"
    zoom 0.5

image wt_check_off:
    "gui/checkbox_square_off.png"
    zoom 0.5

style wt_label is text:
    kerning 0
    size 36
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"

style wt_txt is text:
    kerning 0
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#3f3c38"

style wt_tip is text:
    kerning 0
    size 16
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#e4dace"
    outlines [(1, "#00000065", 0, 0)]
    text_align 0.0
    line_spacing 2

init python:
    walkthrough_data = {}
