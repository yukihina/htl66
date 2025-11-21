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
    isa_nvl "Hey there, [daddy_r]! It's Isabella! {outlinecolor=#ffffff00}😊"
    isa_nvl "I've been thinking about you all day! {outlinecolor=#ffffff00}💭💕"
    if not smstip_seen:
        $ show_custom_notification("sms_tip")
        $ smstip_seen = True

    isa_nvl "Did you miss me yet? {outlinecolor=#ffffff00}🥺{/outlinecolor}"
    mc_nvl "Yeah... A lot."

    # Showing affection to Isabella
    $ rm.update("isabella", "trust", 1)
    $ check_levels("isabella", "trust", 1)

    isa_nvl "Ahhh!! That's so sweet!! {outlinecolor=#ffffff00}😍😍{/outlinecolor}"
    isa_nvl "I miss you too, [daddy_r]. I wish we could spend more time together. {outlinecolor=#ffffff00}👨‍👧💞{/outlinecolor}"
    isa_nvl "I'm with [gra_r] and [aun_r] Madison right now! {outlinecolor=#ffffff00}👵👧{/outlinecolor}"
    mc_nvl "Ok cool..."
    mc_nvl "You need something from me?"
    mc_nvl "I'm kinda busy at the moment."
    isa_nvl "Well... uhm. Not really. I just wanted to tell you hi. {outlinecolor=#ffffff00}😊{/outlinecolor}"
    mc_nvl "Tell them hello too then."
    mc_nvl "I gotta go now. Talk to you later."
    isa_nvl "Gotcha! I will send you some picture of me doing the photoshoot. Like a present for you {outlinecolor=#ffffff00}📷🎁{/outlinecolor}"
    mc_nvl "Sure, looking forward to it."
    mc_nvl "Just don't send too many. My phone's storage is almost full."
    isa_nvl "{a=show:picview_ep03_sms1}{image=thumb_ep03_sms1}"
    if not smstip2_seen:
        $ show_custom_notification("sms_tip2")
        $ smstip2_seen = True
    # FORCE PICTURE SHOULD BE ALWAYS AFTER THE THUMBNAIL.
    if not sawpic_ep03_sms1:
        show screen picview_ep03_sms1

    isa_nvl "Alright, [daddy_r]! Love you! Bye!! {outlinecolor=#ffffff00}😘💕{/outlinecolor}"
    isa_nvl "I hope you like the picture. I picked the best one just for you! {outlinecolor=#ffffff00}😊👌{/outlinecolor}"
    isa_nvl "Oh! Don't forget to check the boxes from Osaka! {outlinecolor=#ffffff00}📦👀"
    isa_nvl "I packed some special surprises for you in there! {outlinecolor=#ffffff00}😉🎉"
    mc_nvl "Got it! Will do."
    mc_nvl "Thanks for the reminder. I'll check them later."
    isa_nvl "Okay, [daddy_r]. I hope you like what I picked out for you. I put a lot of thought into it. {outlinecolor=#ffffff00}🤗💖{/outlinecolor}"
    mc_nvl "I'm sure I will. Thanks, kid."

    $ stopAllSubchannels(channel="music", fadeout=2)

    hide ep03_antoback02
    show ep03_antoback01
    mc_t "Thanks, kid? Seriously? That's all I could say? Am I that bad at expressing my feelings towards my [dau_r_low]?"
    mc_t "She deserves better than me, doesn't she? Anyway, let's check those boxes..."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_boxes


#-- TOTAL POINTS AVAILABLE:
    #ISABELLA TRUST: +1


