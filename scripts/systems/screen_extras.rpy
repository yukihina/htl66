screen extras():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("extras"), scroll="viewport"):

        style_prefix "about"

    if main_menu:
        add "gui/mmtitle_extras.png" ypos 151 xpos 1358 at igm_appear_fg
    else:
        null
    vbox:
        xsize 1250
        yalign 0.5
        xalign 0.5
        text _("Work in progress") at igm_appear_fg style "about_txt" xalign 0.5


style about_txt is text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    #outlines [ (2, "#321414", 0, 0) ]
    color "#34323d"

style about_label is about_txt
style about_label_text is about_txt
style about_text is about_txt
