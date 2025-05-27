define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation

init -2 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.opus")

    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.opus")

    def print_bonjour():
        print("bonjour")

    
    globals()['Phone_ReceiveSound'] = Phone_ReceiveSound
    globals()['Phone_SendSound'] = Phone_SendSound

transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign
    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0
    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0
    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:
                    xpos -335
                    ypos 0.0
                    xsize 350
                    text_align 0.5
                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == mc_name:
                $ message_frame = "gui/phone_send_frame.png"
            else:
                $ message_frame = "gui/phone_received_frame.png"

            hbox:
                spacing 10
                if d.who == mc_name:
                    box_reverse True
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == mc_name:
                        $ message_icon = "gui/profile_pic_mc.png"
                    elif d.who == "Antonella":
                        $ message_icon = "gui/profile_pic_anto.png"
                    elif d.who == "Isabella":
                        $ message_icon = "gui/profile_pic_isa.png"
                    elif d.who == "Amber":
                        $ message_icon = "gui/profile_pic_amb.png"
                    elif d.who == "Madison":
                        $ message_icon = "gui/profile_pic_mad.png"
                    elif d.who == "Paz":
                        $ message_icon = "gui/profile_pic_paz.png"
                    elif d.who == "Nanami":
                        $ message_icon = "gui/profile_pic_nana.png"
                    elif d.who == "Kanae":
                        $ message_icon = "gui/profile_pic_kan.png"
                    elif d.who == "Mom":
                        $ message_icon = "gui/profile_pic_eli.png"
                    elif d.who == "Elizabeth":
                        $ message_icon = "gui/profile_pic_eli.png"
                    elif d.who == "Arlette":
                        $ message_icon = "gui/profile_pic_arl.png"
                    else:
                        $ message_icon = "gui/phone_received_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                        
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != mc_name and previous_d_who != d.who:
                        text d.who:#CHAR NAME COLOR
                            if d.who == "Antonella":
                                color "#ff4d4d"
                            elif d.who == "Isabella":
                                color "#00b7eb"
                            elif d.who == "Amber":
                                color "#FF3333"
                            elif d.who == "Madison":
                                color "#ff5349"
                            elif d.who == "Paz":
                                color "#7f7fc5"
                            elif d.who == "Nanami":
                                color "#FFB6C1"
                            elif d.who == "Kanae":
                                color "#33ffff"
                            elif d.who == "Mom":
                                color "#DBB2D1"
                            elif d.who == "Elizabeth":
                                color "#da86c5"
                            elif d.who == "Arlette":
                                color "#ffa69e"
                            else:
                                color "#000"
                    

                    frame:
                        padding (20,20)
                        background Frame(message_frame, 23,23,23,23)
                        xsize 350
                        if d.current:
                            if d.who == mc_name:
                                at message_appear(1)
                            else:
                                at message_appear(-1)
                        
                        
                        text d.what:
                            pos (0,0)
                            xsize 350
                            slow_cps False
                            if d.who == mc_name:#CHAR TEXT COLOR
                                color "#FFD119" 
                                text_align 1.0
                                xpos -580
                            elif d.who == "Antonella":
                                color "#ffdbdb"
                            elif d.who == "Isabella":
                                color "#b9f2ff"
                            elif d.who == "Amber":
                                color "#ff9090"
                            elif d.who == "Madison":
                                color "#ffc0bc"
                            elif d.who == "Paz":
                                color "#cbcbf2"
                            elif d.who == "Nanami":
                                color "#facbd2"
                            elif d.who == "Kanae":
                                color "#b2ffff"
                            elif d.who == "Arlette":
                                color "#faf3dd"
                            else:
                                color "#000"  
                            id d.what_id
                        
        $ previous_d_who = d.who
                    



style phoneFrame is default

style phoneFrame_frame:
    background Transform("gui/phone_bg.png", xcenter=0.5,yalign=0.5)
    #foreground Transform("phone_foreground.png", xcenter=0.5,yalign=0.5)
    ysize 780
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset 9

style phoneFrame_vbox:
    spacing 10
    xfill True

return