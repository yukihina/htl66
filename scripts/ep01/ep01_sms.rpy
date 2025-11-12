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
    mc_t "Oh, a new message... Who is it?"

    show ep01_3rddream21
    paz_nvl "Hey, I'm really sorry about what I said the other day {outlinecolor=#ffffff00}😞{/outlinecolor}"
    if not smstip_seen:
        $ show_custom_notification("sms_tip")
        $ smstip_seen = True

    paz_nvl "And my bad for not coming to see you at the hospital again..."
    paz_nvl "I've just been swamped with stuff {outlinecolor=#ffffff00}😓{/outlinecolor}"
    mc_nvl "No worries, it's all good {outlinecolor=#ffffff00}👌{/outlinecolor}"
    paz_nvl "If there's any way I can make it up to you, just say the word! {outlinecolor=#ffffff00}🙌{/outlinecolor}"
    paz_nvl "So, how're you holding up? Feeling any better?"
    mc_nvl "Yeah, a lot better than yesterday..."
    mc_nvl "The meds they gave me really helped with the pain."
    paz_nvl "That's great to hear!"
    paz_nvl "You know... after what happened to you, I've been going through some serious shit with the higher-ups..."
    paz_nvl "You really left me in a tight spot, man {outlinecolor=#ffffff00}😅😅😅{/outlinecolor}"
    mc_nvl "Yeah, I know. I'm sorry about that."
    paz_nvl "I get it..."
    paz_nvl "You had your reasons... {outlinecolor=#ffffff00}😓{/outlinecolor}"
    paz_nvl "Anyway, we managed to bust some of the guys involved thanks to the info you gave us."
    mc_nvl "Look, Paz... I'm feeling pretty out of it right now and still not okay..."
    mc_nvl "So I might not be able to follow the whole story."
    mc_nvl "Maybe we can catch up another time when I'm more with it?"
    paz_nvl "Yeah, no worries at all! {outlinecolor=#ffffff00}😊😊{/outlinecolor}"
    paz_nvl "But hey, if there's anything I can do for you, just holler."
    mc_nvl "Thanks for having my back, Paz. I appreciate it."
    paz_nvl "{a=show:picview_ep01_sms5}{image=thumb_ep01_sms5}{/a}"
    if not smstip2_seen:
        $ show_custom_notification("sms_tip2")
        $ smstip2_seen = True
    # FORCE PICTURE SHOULD BE ALWAYS AFTER THE THUMBNAIL.
    if not sawpic_ep01_sms5:
        show screen picview_ep01_sms5

    paz_nvl "Here's a little something to cheer you up!! {outlinecolor=#ffffff00}❤{/outlinecolor}"
    paz_nvl "Oh, fuck! Wrong pic!!! Just ignore that!! {outlinecolor=#ffffff00}🙈 🙈 🙈{/outlinecolor}"
    mc_nvl "lol For real? {outlinecolor=#ffffff00}😂{/outlinecolor}"
    mc_nvl "Damn, Paz... That... {outlinecolor=#ffffff00}😳{/outlinecolor}"
    #MENU
    $ show_walkthrough("ep01_sms01_wt1")
    # MENU SHOULD BE ALWAYS WITH A DIALOGUE AFTER.
    show screen menu_button ("Joke about it", "ep01_sms01_joke", "Get serious", "ep01_sms01_serious")

    paz_nvl "It's an old pic, don't even worry about it! {outlinecolor=#ffffff00}😬 😬{/outlinecolor}"    




label ep01_sms01_joke:
    $ rm.update("paz", "trust", 2)
    $ check_levels("paz", "trust", 2)

    hide screen walkthrough_screen

    mc_nvl "So who're you sending these sexy pics to, huh? ^^"
    paz_nvl "They weren't meant for anyone, alright?!"
    mc_nvl "Seriously?"
    paz_nvl "Yeah, just some vacation shots."
    paz_nvl "My bad, I really meant to send you a different one."
    paz_nvl "{a=show:picview_ep01_sms4}{image=thumb_ep01_sms4}"
    if not sawpic_ep01_sms4:
        show screen picview_ep01_sms4

    paz_nvl "This one's way more PG... {outlinecolor=#ffffff00}😇{/outlinecolor}"
    mc_nvl "Heh, come on. It was actually pretty nice to see lol"
    paz_nvl "{outlinecolor=#ffffff00}😵‍💫{/outlinecolor}"
    #MENU
    $ show_walkthrough("ep01_sms01_wt2")
    show screen menu_button ("Say sorry", "ep01_sms01_sorry", "Flirt", "ep01_sms01_flirt")

    paz_nvl "[mc_name]! You perv! {outlinecolor=#ffffff00}😒😒😒{/outlinecolor}"




label ep01_sms01_flirt:
    $ rm.update("paz", "trust", 2)
    $ check_levels("paz", "trust", 2)

    hide screen walkthrough_screen

    mc_nvl "hehe, guilty as charged."
    mc_nvl "Well, at least it's helping my fever go down already {outlinecolor=#ffffff00}😉{/outlinecolor}"
    paz_nvl "Dumbass... {outlinecolor=#ffffff00}😂😂{/outlinecolor}"
    paz_nvl "Anyway, I gotta bounce{outlinecolor=#ffffff00}👋{/outlinecolor}"
    mc_nvl "Yes, Ma'am!"
    paz_nvl "Hahaha {outlinecolor=#ffffff00}🤣{/outlinecolor}"
    paz_nvl "But for real... get better soon, ok? {outlinecolor=#ffffff00}😊{/outlinecolor}"
    mc_nvl "Whoa, hey now..."
    paz_nvl "{a=show:picview_ep01_sms6}{image=thumb_ep01_sms6}"

    $ rm.update("paz", "cor", 1)
    $ check_levels("paz", "cor", 1)
    if not sawpic_ep01_sms6:
        show screen picview_ep01_sms6

    paz_nvl "Consider this a little present... {outlinecolor=#ffffff00}😉{/outlinecolor}"
    paz_nvl "Oh! And... Take care of yourself, alright?"
    mc_nvl "Don't worry, I'll do my best lol"
    paz_nvl "{outlinecolor=#ffffff00}❤{/outlinecolor}"

    jump ep01_smslater




label ep01_sms01_sorry:
    $ rm.update("paz", "trust", 1)
    $ check_levels("paz", "trust", 1)

    hide screen walkthrough_screen

    mc_nvl "Sorry, I didn't mean it like that. My bad... {outlinecolor=#ffffff00}😔{/outlinecolor}"
    paz_nvl "Mhm... {outlinecolor=#ffffff00}😒{/outlinecolor}"
    paz_nvl "Please delete that picture now!"
    mc_nvl "Sure thing. {outlinecolor=#ffffff00}👍{/outlinecolor}"
    paz_nvl "Anyway, I gotta bounce{outlinecolor=#ffffff00}👋{/outlinecolor}"
    paz_nvl "Get better soon, ok? {outlinecolor=#ffffff00}😊{/outlinecolor}"
    mc_nvl "Yes, Ma'am!"
    paz_nvl "{outlinecolor=#ffffff00}❤{/outlinecolor}"

    jump ep01_smslater




label ep01_sms01_serious:
    $ rm.update("paz", "trust", 1)
    $ check_levels("paz", "trust", 1)

    hide screen walkthrough_screen

    mc_nvl "Hey, be careful with those kinds of pics..."
    paz_nvl "Ugh, yeah, I know... {outlinecolor=#ffffff00}😞{/outlinecolor}"
    paz_nvl "Anyways! What I meant to send was this one! {outlinecolor=#ffffff00}😊{/outlinecolor}"
    paz_nvl "{a=show:picview_ep01_sms4}{image=thumb_ep01_sms4}"
    if not sawpic_ep01_sms4:
        show screen picview_ep01_sms4

    paz_nvl "I miss having you as my partner! {outlinecolor=#ffffff00}😞🙏{/outlinecolor}"
    mc_nvl "Wow, I wasn't expecting that..."
    paz_nvl "How about we grab a drink when I see you next? {outlinecolor=#ffffff00}🍻🍻{/outlinecolor}"
    mc_nvl "Sounds like a plan! And hey... Thanks for looking out for me so far."
    paz_nvl "No worries, that's what friends are for {outlinecolor=#ffffff00}😊{/outlinecolor}"
    paz_nvl "I gotta run now. Let's catch up later! {outlinecolor=#ffffff00}👋{/outlinecolor}"

    jump ep01_smslater


#-- ELIZABETH SMS




label ep01_sms02:
    nvl clear
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)

    show ep01_pregame35 with slowfade
    mc_t "Let's check who it's from."
    mc_t "Oh..it's [mo_r]."

    show ep01_pregame36
    eli_nvl "Hey sweetie, how's the trip going? You getting close to home yet?"
    if not smstip_seen:
        $ show_custom_notification("sms_tip")
        $ smstip_seen = True

    mc_nvl "Yeah, we're hopping on some local transport now.."
    mc_nvl "So I'd say we're about halfway there."
    mc_nvl "{outlinecolor=#ffffff00}🤷‍♂️🤷‍♂️🤷‍♂️{/outlinecolor}"
    eli_nvl "Ooh, you must be somewhere around Shizuoka by now, right?"
    eli_nvl "That reminds me, did you grab some lunch, honey?"
    eli_nvl "I can whip something up for you if you want {outlinecolor=#ffffff00}😊 😊{/outlinecolor}"
    mc_nvl "Nah, it's cool. I'm not really feeling hungry yet."
    mc_nvl "Still a bit groggy from the meds, you know?"
    eli_nvl "Aww, well, just be careful, okay? {outlinecolor=#ffffff00}🙏🙏{/outlinecolor}"
    eli_nvl "Once that medicine wears off, you'll be starving like a bear! {outlinecolor=#ffffff00}🐻{/outlinecolor}"
    mc_nvl "Yeah, yeah, don't worry about it..."
    eli_nvl "Alright, I'll let you catch some rest then. {outlinecolor=#ffffff00}😇{/outlinecolor}"
    eli_nvl "I'm so excited to see you again, darling! It's been way too long! {outlinecolor=#ffffff00}🤗{/outlinecolor}"
    eli_nvl "Text me later, 'kay sweetie? {outlinecolor=#ffffff00}😘{/outlinecolor}"
    mc_nvl "Sure thing. Catch you later."
    pause 0.1
    mc_t "I..."
    mc_t "I just wanna see HER again..."
    mc_t ". . ."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_pregame2


#-- TOTAL POINTS AVAILABLE:
    #PAZ TRUST: +2 OR +1
    #PAZ TRUST: +1
    #PAZ COR: +1