## screen_achievements.rpy
## Achievement System for Ren'Py - Complete English Version
## 
## How to use:
## The achievement system automatically tracks player progress and displays unlocked achievements.
## Achievements are checked on every interaction through the SetAchievements() function.
## 
## To open the achievements screen from anywhere in your game:
## textbutton "Achievements" action ShowMenu("achievements")
## 
## The achievement system uses persistent data to maintain progress across saves.
## All achievements are displayed in a grid organized by ACTs (episodes).
##
## Achievement Notification System:
## When an achievement is unlocked, a notification automatically appears for 12 seconds.
## Players can click on unlocked achievements to view full-screen details.
##
## Adding New Achievements:
## 1. Add persistent variables for the new achievement and its notification state
## 2. Add achievement data to the achievement_data dictionary
## 3. Add the unlock condition to achievement_conditions list
## 4. Ensure required achievement images exist in achievements/ directory

################################################################################
## INITIALIZATION
################################################################################

init -1:
    ## Persistent Variables - Achievement States
    default persistent.ep01_ach1 = False
    default persistent.ep01_ach2 = False
    default persistent.ep01_ach3 = False
    default persistent.ep01_ach4 = False
    default persistent.ep01_ach5 = False

    default persistent.ep02_ach1 = False
    default persistent.ep02_ach2 = False
    default persistent.ep02_ach3 = False

    default persistent.ep03_ach1 = False
    default persistent.ep03_ach2 = False
    default persistent.ep03_ach3 = False

    default persistent.ep04_ach1 = False
    default persistent.ep04_ach2 = False
    default persistent.ep04_ach3 = False
    default persistent.ep04_ach4 = False
    default persistent.ep04_ach6 = False
    default persistent.ep04_ach7 = False
    default persistent.ep04_ach8 = False
    default persistent.ep04_ach9 = False

    default persistent.ep05_ach1 = False
    default persistent.ep05_ach2 = False
    default persistent.ep05_ach3 = False
    default persistent.ep05_ach4 = False
    default persistent.ep05_ach5 = False
    default persistent.ep05_ach6 = False

    ## Notification Variables - Track if notification was shown
    default persistent.ep01_ach1_notified = False
    default persistent.ep01_ach2_notified = False
    default persistent.ep01_ach3_notified = False
    default persistent.ep01_ach4_notified = False
    default persistent.ep01_ach5_notified = False

    default persistent.ep02_ach1_notified = False
    default persistent.ep02_ach2_notified = False
    default persistent.ep02_ach3_notified = False

    default persistent.ep03_ach1_notified = False
    default persistent.ep03_ach2_notified = False
    default persistent.ep03_ach3_notified = False

    default persistent.ep04_ach1_notified = False
    default persistent.ep04_ach2_notified = False
    default persistent.ep04_ach3_notified = False
    default persistent.ep04_ach4_notified = False
    default persistent.ep04_ach5_notified = False
    default persistent.ep04_ach6_notified = False
    default persistent.ep04_ach7_notified = False
    default persistent.ep04_ach8_notified = False

    default persistent.ep05_ach1_notified = False
    default persistent.ep05_ach2_notified = False
    default persistent.ep05_ach3_notified = False
    default persistent.ep05_ach4_notified = False
    default persistent.ep05_ach5_notified = False
    default persistent.ep05_ach6_notified = False

init python:
    ############################################################################
    ## ACHIEVEMENT DATA DICTIONARY
    ############################################################################
    
    achievement_data = {
        "ach_ep01_isabella": {
            "title": "Beginnings",
            "text": "Your story unfolds as you rekindle your connection with Isabella. The journey starts here.",
            "persistent_var": "ep01_ach1",
            "notified_var": "ep01_ach1_notified",
            "thumb_on": "achievements/ach_ep01_isabella_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep01_isabella_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep01_isabella_thumb_off.webp"
        },
        "ach_ep01_antonella2": {
            "title": "The Grand Prize",
            "text": "Through wit and charm, you've led Antonella to a stunning defeat. Savor your triumph.",
            "persistent_var": "ep01_ach2",
            "notified_var": "ep01_ach2_notified",
            "thumb_on": "achievements/ach_ep01_antonella2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep01_antonella2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep01_antonella2_thumb_off.webp"
        },
        "ach_ep01_amber2": {
            "title": "Forbidden Love",
            "text": "Amber bares her heart, confessing her deep affection for you. Despite the odds, you choose to embrace her love.",
            "persistent_var": "ep01_ach3",
            "notified_var": "ep01_ach3_notified",
            "thumb_on": "achievements/ach_ep01_amber2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep01_amber2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep01_amber2_thumb_off.webp"
        },
        "ach_ep01_amber": {
            "title": "Turning Point",
            "text": "In a pivotal decision, you chose to share your first time with Amber, creating an unforgettable memory.",
            "persistent_var": "ep01_ach4",
            "notified_var": "ep01_ach4_notified",
            "thumb_on": "achievements/ach_ep01_amber_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep01_amber_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep01_amber_thumb_off.webp"
        },
        "ach_ep01_antonella": {
            "title": "Timeless Bond",
            "text": "Antonella's special day didn't go unnoticed. Your thoughtfulness will be forever cherished.",
            "persistent_var": "ep01_ach5",
            "notified_var": "ep01_ach5_notified",
            "thumb_on": "achievements/ach_ep01_antonella_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep01_antonella_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep01_antonella_thumb_off.webp"
        },
        "ach_ep02_paz": {
            "title": "Opening Old Doors",
            "text": "Reconnecting with Paz, your old bestie, sparks nostalgia. Could this lead to something more?",
            "persistent_var": "ep02_ach1",
            "notified_var": "ep02_ach1_notified",
            "thumb_on": "achievements/ach_ep02_paz_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep02_paz_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep02_paz_thumb_off.webp"
        },
        "ach_ep02_arlette": {
            "title": "New Love Found",
            "text": "Arlette enters your life, bringing the promise of a new romantic adventure.",
            "persistent_var": "ep02_ach2",
            "notified_var": "ep02_ach2_notified",
            "thumb_on": "achievements/ach_ep02_arlette_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep02_arlette_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep02_arlette_thumb_off.webp"
        },
        "ach_ep02_rina": {
            "title": "Payback Time",
            "text": "Fueled by past grievances, you chose the path of retribution. Rina learns that payback can be oh so sweet.",
            "persistent_var": "ep02_ach3",
            "notified_var": "ep02_ach3_notified",
            "thumb_on": "achievements/ach_ep02_rina_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep02_rina_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep02_rina_thumb_off.webp"
        },
        "ach_ep03_amber2": {
            "title": "Silken Secrets",
            "text": "Reconnecting with Amber has given you a tempting glimpse of her body. Trust pays off.",
            "persistent_var": "ep03_ach1",
            "notified_var": "ep03_ach1_notified",
            "thumb_on": "achievements/ach_ep03_amber2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep03_amber2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep03_amber2_thumb_off.webp"
        },
        "ach_ep03_amber1": {
            "title": "Passion's Price",
            "text": "Amber's captivating body is revealed to you, but at the cost of her trust.",
            "persistent_var": "ep03_ach2",
            "notified_var": "ep03_ach2_notified",
            "thumb_on": "achievements/ach_ep03_amber1_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep03_amber1_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep03_amber1_thumb_off.webp"
        },
        "ach_ep03_madison": {
            "title": "Prophecy Fulfilled",
            "text": "Madison's warnings prove true. There's no escaping her watchful gaze.",
            "persistent_var": "ep03_ach3",
            "notified_var": "ep03_ach3_notified",
            "thumb_on": "achievements/ach_ep03_madison_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep03_madison_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep03_madison_thumb_off.webp"
        },
        "ach_ep04_nanami1": {
            "title": "Innocent Exposure",
            "text": "Your persuasive charm leads Nanami to an unexpectedly revealing wardrobe choice.",
            "persistent_var": "ep04_ach1",
            "notified_var": "ep04_ach1_notified",
            "thumb_on": "achievements/ach_ep04_nanami1_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_nanami1_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_nanami1_thumb_off.webp"
        },
        "ach_ep04_nanami2": {
            "title": "Gothic Transformation",
            "text": "A series of cunning suggestions results in Nanami's dramatic style change.",
            "persistent_var": "ep04_ach2",
            "notified_var": "ep04_ach2_notified",
            "thumb_on": "achievements/ach_ep04_nanami2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_nanami2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_nanami2_thumb_off.webp"
        },
        "ach_ep04_madison": {
            "title": "Madison's Ally",
            "text": "You choose to align with Madison's interests, despite potential consequences for others.",
            "persistent_var": "ep04_ach3",
            "notified_var": "ep04_ach3_notified",
            "thumb_on": "achievements/ach_ep04_madison_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_madison_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_madison_thumb_off.webp"
        },
        "ach_ep04_isabella": {
            "title": "Complicated Affection",
            "text": "A moment of conflicted emotions leads to a boundary-crossing interaction with Isabella.",
            "persistent_var": "ep04_ach4",
            "notified_var": "ep04_ach4_notified",
            "thumb_on": "achievements/ach_ep04_isabella_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_isabella_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_isabella_thumb_off.webp"
        },
        "ach_ep04_isabella2": {
            "title": "Dream Walker",
            "text": "Your subconscious revealed desires better left unspoken about Isabella.",
            "persistent_var": "ep04_ach5",
            "notified_var": "ep04_ach5_notified",
            "thumb_on": "achievements/ach_ep04_isabella2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_isabella2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_isabella2_thumb_off.webp"
        },
        "ach_ep04_amber": {
            "title": "Midnight Snack",
            "text": "When Amber made an appetizing suggestion, you didn't hesitate to dig in.",
            "persistent_var": "ep04_ach6",
            "notified_var": "ep04_ach6_notified",
            "thumb_on": "achievements/ach_ep04_amber_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_amber_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_amber_thumb_off.webp"
        },
        "ach_ep04_madison2": {
            "title": "Good Boy's Reward",
            "text": "Following Madison's every command paid off in the most teasing way possible.",
            "persistent_var": "ep04_ach7",
            "notified_var": "ep04_ach7_notified",
            "thumb_on": "achievements/ach_ep04_madison2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_madison2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_madison2_thumb_off.webp"
        },
        "ach_ep04_elizabeth": {
            "title": "Midnight Care",
            "text": "A moment of conflicted emotions leads to a boundary-crossing interaction with Isabella.",
            "persistent_var": "ep04_ach8",
            "notified_var": "ep04_ach8_notified",
            "thumb_on": "achievements/ach_ep04_elizabeth_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep04_elizabeth_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep04_elizabeth_thumb_off.webp"
        },
        "ach_ep05_isabella": {
            "title": "Corrupted Cosplay",
            "text": "Isabella's Commander White costume takes a seductive turn under your influence.",
            "persistent_var": "ep05_ach1",
            "notified_var": "ep05_ach1_notified",
            "thumb_on": "achievements/ach_ep05_isabella_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep05_isabella_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep05_isabella_thumb_off.webp"
        },
        "ach_ep05_isabella2": {
            "title": "Pure Cosplayer",
            "text": "Isabella joyfully embodies Commander White, her innocent passion for cosplay intact.",
            "persistent_var": "ep05_ach2",
            "notified_var": "ep05_ach2_notified",
            "thumb_on": "achievements/ach_ep05_isabella2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep05_isabella2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep05_isabella2_thumb_off.webp"
        },
        "ach_ep05_ambeli": {
            "title": "Forbidden Triangle",
            "text": "Amber discovered Elizabeth's desires, forever changing her relationship.",
            "persistent_var": "ep05_ach3",
            "notified_var": "ep05_ach3_notified",
            "thumb_on": "achievements/ach_ep05_ambeli_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep05_ambeli_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep05_ambeli_thumb_off.webp"
        },
        "ach_ep05_nanamad": {
            "title": "Seductive Betrayal",
            "text": "Your actions allowed Madison to claim Nanami's trust, leaving you with only regrets and lost opportunities.",
            "persistent_var": "ep05_ach4",
            "notified_var": "ep05_ach4_notified",
            "thumb_on": "achievements/ach_ep05_nanamad_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep05_nanamad_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep05_nanamad_thumb_off.webp"
        },
        "ach_ep05_final1": {
            "title": "Conflicted Desires",
            "text": "The weight of forbidden attraction battles against your conscience. In the forest's embrace, temptation whispers what morality forbids.",
            "persistent_var": "ep05_ach5",
            "notified_var": "ep05_ach5_notified",
            "thumb_on": "achievements/ach_ep05_final1_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep05_final1_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep05_final1_thumb_off.webp"
        },
        "ach_ep05_final2": {
            "title": "Uninhibited Exploration",
            "text": "Your curiosity knows no bounds, leading you to embrace desires without shame. In tranquil waters, true feelings surface naturally.",
            "persistent_var": "ep05_ach6",
            "notified_var": "ep05_ach6_notified",
            "thumb_on": "achievements/ach_ep05_final2_thumb_on.webp",
            "thumb_on_hover": "achievements/ach_ep05_final2_thumb_onh.webp",
            "thumb_off": "achievements/ach_ep05_final2_thumb_off.webp"
}
    }

    ############################################################################
    ## ACHIEVEMENT CONDITION HELPER FUNCTIONS
    ############################################################################
    
    def create_achievement_condition(condition_func, persistent_var, notified_var, achievement_key):
        """Helper function to create achievement condition objects"""
        return {
            "condition": condition_func,
            "persistent_var": persistent_var,
            "notified_var": notified_var,
            "achievement_key": achievement_key
        }
    
    ############################################################################
    ## ACHIEVEMENT CONDITIONS LIST
    ############################################################################
    
    # List of achievements with their unlock conditions
    achievement_conditions = [
        create_achievement_condition(
            lambda: rm.get("isabella", "knows"),
            "ep01_ach1",
            "ep01_ach1_notified",
            "ach_ep01_isabella"
        ),
        create_achievement_condition(
            lambda: ep01_bestprize,
            "ep01_ach2",
            "ep01_ach2_notified",
            "ach_ep01_antonella2"
        ),
        create_achievement_condition(
            lambda: ep01_amblove,
            "ep01_ach3",
            "ep01_ach3_notified",
            "ach_ep01_amber2"
        ),
        create_achievement_condition(
            lambda: ep01_first,
            "ep01_ach4",
            "ep01_ach4_notified",
            "ach_ep01_amber"
        ),
        create_achievement_condition(
            lambda: ep01_antobday,
            "ep01_ach5",
            "ep01_ach5_notified",
            "ach_ep01_antonella"
        ),
        create_achievement_condition(
            lambda: rm.get("paz", "knows"),
            "ep02_ach1",
            "ep02_ach1_notified",
            "ach_ep02_paz"
        ),
        create_achievement_condition(
            lambda: rm.get("arlette", "knows"),
            "ep02_ach2",
            "ep02_ach2_notified",
            "ach_ep02_arlette"
        ),
        create_achievement_condition(
            lambda: ep02_hitrina,
            "ep02_ach3",
            "ep02_ach3_notified",
            "ach_ep02_rina"
        ),
        create_achievement_condition(
            lambda: ep03_ambersex_l,
            "ep03_ach1",
            "ep03_ach1_notified",
            "ach_ep03_amber2"
        ),
        create_achievement_condition(
            lambda: ep03_ambersex_c,
            "ep03_ach2",
            "ep03_ach2_notified",
            "ach_ep03_amber1"
        ),
        create_achievement_condition(
            lambda: ep03_madcaught,
            "ep03_ach3",
            "ep03_ach3_notified",
            "ach_ep03_madison"
        ),
        create_achievement_condition(
            lambda: ep04_ach_nanabikini,
            "ep04_ach1",
            "ep04_ach1_notified",
            "ach_ep04_nanami1"
        ),
        create_achievement_condition(
            lambda: ep04_ach_nanagoth,
            "ep04_ach2",
            "ep04_ach2_notified",
            "ach_ep04_nanami2"
        ),
        create_achievement_condition(
            lambda: ep03_madtalk and ep04_ach_madison,
            "ep04_ach3",
            "ep04_ach3_notified",
            "ach_ep04_madison"
        ),
        create_achievement_condition(
            lambda: ep03_isahug and ep04_ach_isabella,
            "ep04_ach4",
            "ep04_ach4_notified",
            "ach_ep04_isabella"
        ),
        create_achievement_condition(
            lambda: ep04_mcdrunk and ep04_ach_isabella2,
            "ep04_ach5",
            "ep04_ach5_notified",
            "ach_ep04_isabella2"
        ),
        create_achievement_condition(
            lambda: ep04_ambnight_cum == 2 and ep04_ach_amber,
            "ep04_ach6",
            "ep04_ach6_notified",
            "ach_ep04_amber"
        ),
        create_achievement_condition(
            lambda: ep04_madpath == 2 and ep04_ach_madison2,
            "ep04_ach7",
            "ep04_ach7_notified",
            "ach_ep04_madison2"
        ),
        create_achievement_condition(
            lambda: ep04_elistay and ep04_ach_elizabeth,
            "ep04_ach8",
            "ep04_ach8_notified",
            "ach_ep04_elizabeth"
        ),
        create_achievement_condition(
            lambda: ep05_isacosplay == 4 and ep05_ach_isaintro,
            "ep05_ach2",
            "ep05_ach2_notified",
            "ach_ep05_isabella2"
        ),
        create_achievement_condition(
            lambda: ep05_isacosplay == -4 and ep05_ach_isaintro,
            "ep05_ach1",
            "ep05_ach1_notified",
            "ach_ep05_isabella"
        ),
        create_achievement_condition(
            lambda: ep05_ambersus_eli and ep05_ach_ambvseli,
            "ep05_ach3",
            "ep05_ach3_notified",
            "ach_ep05_ambeli"
        ),
        create_achievement_condition(
            lambda: ss.get("nanami", "strike") == 1 and ep05_ach_nanastrike,
            "ep05_ach4",
            "ep05_ach4_notified",
            "ach_ep05_nanamad"
        ),
        create_achievement_condition(
            lambda: ep05_guilt_points >= 3 and ep05_ach_final1,
            "ep05_ach5",
            "ep05_ach5_notified",
            "ach_ep05_final1"
        ),
        create_achievement_condition(
            lambda: ep05_curiosity_points >= 3 and ep05_ach_final2,
            "ep05_ach6",
            "ep05_ach6_notified",
            "ach_ep05_final2"
        )
    ]

    ############################################################################
    ## ACHIEVEMENT PROCESSING FUNCTIONS
    ############################################################################

    def SetAchievements():
        """Main function to check and unlock achievements"""
        for ach in achievement_conditions:
            if ach["condition"]() and not getattr(persistent, ach["persistent_var"]):
                setattr(persistent, ach["persistent_var"], True)
                if not getattr(persistent, ach["notified_var"]):
                    setattr(persistent, ach["notified_var"], True)
                    renpy.show_screen("achievement_notification", achievement_key=ach["achievement_key"])
        return

    def execute_SetAchievements():
        """Wrapper function for interaction callback"""
        SetAchievements()

    # Register the achievement checker to run on every interaction
    config.interact_callbacks.append(execute_SetAchievements)

    ############################################################################
    ## ACT FILTERING HELPER FUNCTIONS
    ############################################################################
    
    def get_achievements_for_act(act_number):
        """Get achievements filtered by ACT number"""
        act_achievements = []
        for ach_key, ach in achievement_data.items():
            # ACT 1: ep01-ep05
            if act_number == 1 and any(ep in ach_key for ep in ["ep01", "ep02", "ep03", "ep04", "ep05"]):
                act_achievements.append((ach_key, ach))
            # ACT 2: ep06-ep10 (for future use)
            elif act_number == 2 and any(ep in ach_key for ep in ["ep06", "ep07", "ep08", "ep09", "ep10"]):
                act_achievements.append((ach_key, ach))
            # ACT 3: ep11-ep15 (for future use)
            elif act_number == 3 and any(ep in ach_key for ep in ["ep11", "ep12", "ep13", "ep14", "ep15"]):
                act_achievements.append((ach_key, ach))
            # ACT 4: ep16-ep20 (for future use)
            elif act_number == 4 and any(ep in ach_key for ep in ["ep16", "ep17", "ep18", "ep19", "ep20"]):
                act_achievements.append((ach_key, ach))
                
        return act_achievements
    
    def organize_achievements_in_rows(achievements_list, items_per_row=3):
        """Organize achievements into rows for display"""
        rows = []
        current_row = []
        
        for item in achievements_list:
            current_row.append(item)
            if len(current_row) == items_per_row:
                rows.append(current_row)
                current_row = []
                
        # Add remaining items as last row
        if current_row:
            rows.append(current_row)
            
        return rows

################################################################################
## TRANSFORMS AND ANIMATIONS
################################################################################

init:
    ## Hover effect that changes opacity
    transform hover_alpha:
        alpha 0.8
        on hover:
            linear 0.2 alpha 1.0
        on idle:
            linear 0.2 alpha 0.8

    ## Fade-in effect for achievement notifications
    transform notification_appear:
        alpha 0.0
        pause 1
        ease 0.5 alpha 1.0
        on show:
            alpha 0.0
            pause 2
            ease 0.5 alpha 1.0
        on hide:
            alpha 1.0
            ease 0.5 alpha 0.0

################################################################################
## ACHIEVEMENT SCREENS
################################################################################

## Achievement Notification Screen
screen achievement_notification(achievement_key=None):
    zorder 100

    frame:
        at notification_appear
        add "gui/message_bg.png" xpos 1380 ypos 625
        add "gui/icon_achiev.png" xpos 1408 ypos 654

        vbox:
            xpos 1561 ypos 646
            spacing 3
            if achievement_key:
                text "[achievement_data[achievement_key]['title'].upper()]" style "achievements_title"
            else:
                text _("Congratulations!").upper() style "achievements_title"
            
            text _("You have unlocked a new achievement!") style "achievements_text"

    timer 12 action Hide("achievement_notification")

## Achievement Detail Screen
screen achievement_screen(achievement_key):
    modal True

    default zoom_level = 1.0

    viewport:
        at notification_appear
        xsize 1920
        ysize 1080
        xpos 0
        ypos 0
        draggable True
        mousewheel True
        add "achievements/[achievement_key].avif" zoom zoom_level

    frame:
        at notification_appear
        xpos 0
        ypos 0
        add "gui/message_bg.png" xpos 1380 ypos 878
        add "gui/icon_achiev.png" xpos 1398 ypos 915

        vbox:
            xpos 1562
            ypos 901
            spacing 10
            text "[achievement_data[achievement_key]['title'].upper()]" style "achievements_title"
            text "[achievement_data[achievement_key]['text']]" style "achievements_text"

    imagebutton:
        xalign 0.99
        yalign 0.03
        idle "gui/btn_close_off.png" at hover_alpha, notification_appear
        hover "gui/btn_close_off.png"
        hover_offset (0, -2)
        action Hide("achievement_screen")
        style "igm_button"
        focus_mask None

    key "mousedown_4" action SetScreenVariable("zoom_level", min(1.25, zoom_level + 0.05))
    key "mousedown_5" action SetScreenVariable("zoom_level", max(1.0, zoom_level - 0.05))

## Main Achievements Grid Screen
screen achievements():
    tag menu
    default current_act = 1  # Default, show ACT 1

    use game_menu(("Achievements"), scroll="viewport"):
        style_prefix "achievements"

    if main_menu:
        add "gui/mmtitle_achi.png" ypos 146 xpos 1177 at notification_appear
    else:
        null
    
    ## ACT Selection Menu
    frame:
        xsize 1260
        ysize 50
        xpos 714
        ypos 791
        
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            ## ACT 1 Button (active by default)
            button at igm_appear_fg2:
                text "ACT 1" style "act_button_text"
                selected current_act == 1
                action SetScreenVariable("current_act", 1)
                
            ## ACT 2 Button
            button at igm_appear_fg2:
                text "ACT 2" style "act_button_text"
                selected current_act == 2
                action SetScreenVariable("current_act", 2)
            
            ## ACT 3 Button (disabled)
            button at igm_appear_fg2:
                text "ACT 3" style "act_button_text"
                selected current_act == 3
                action SetScreenVariable("current_act", 3)
                
            ## ACT 4 Button (disabled)
            button at igm_appear_fg2:
                text "ACT 4" style "act_button_text"
                selected current_act == 4
                action SetScreenVariable("current_act", 4)

    ## Achievement Grid Display
    $ act_achievements = get_achievements_for_act(current_act)
    $ achievement_rows = organize_achievements_in_rows(act_achievements, 3)
    
    viewport:
        xsize 1260
        ysize 512
        xpos 331
        ypos 270
        scrollbars "vertical"
        mousewheel True

        vbox:
            spacing 90
            
            for row in achievement_rows:
                hbox:
                    spacing 90
                    
                    for ach_key, ach in row:
                        frame:
                            background "gui/rectangle.png" at notification_appear
                            xsize 345
                            ysize 194
                            if getattr(persistent, ach['persistent_var']):
                                imagebutton:
                                    idle ach['thumb_on'] at hover_alpha
                                    hover ach['thumb_on_hover']
                                    action Show("achievement_screen", achievement_key=ach_key)
                            else:
                                imagebutton:
                                    idle ach['thumb_off'] at hover_alpha
                                    action NullAction()
                            text "[ach['title'].upper()]":
                                xalign 0.5
                                yalign 0.5
                                size 20
                                color "#F7F7F7"
                                outlines [(2, "#16161D", 0, 0)]
                    
                    ## Fill empty spaces in the last row if needed
                    if len(row) < 3:
                        $ empty_spaces = 3 - len(row)
                        for i in range(empty_spaces):
                            null width 345

################################################################################
## ACHIEVEMENT STYLES
################################################################################

style achievements_title:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [(1, "#198c5f", 0, 0)]
    color "#27dc95"

style achievements_text:
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xmaximum 280
    kerning -1
    yoffset -8

style act_button_text:
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF" 
    outlines [(1, "#198c5f", 0, 0)]
    
style act_button_text_disabled:
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#606060"  # Gray color for disabled buttons
    outlines [(1, "#303030", 0, 0)]

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this achievement system in your game:
## 
## 1. In your extras screen or main menu, add a button like this:
##    textbutton "Achievements" action ShowMenu("achievements")
##
## 2. The achievement system will automatically:
##    - Track player progress through game variables
##    - Show notifications when achievements are unlocked
##    - Save achievement progress in persistent data
##    - Display achievements organized by ACTs
##
## 3. To add new achievements:
##    - Add persistent variables for the achievement and notification
##    - Add achievement data to the achievement_data dictionary
##    - Add the unlock condition to achievement_conditions list
##    - Ensure required achievement images exist
##
## 4. Required assets:
##    - Achievement thumbnail images (on, off, hover states)
##    - Full achievement images for detail view
##    - GUI elements (message_bg.png, icon_achiev.png, etc.)
##
## 5. The system is compatible with existing save games and will not
##    interfere with other game systems
##
## Example extras screen integration:
## screen extras():
##     tag menu
##     use game_menu(_("Extras")):
##         vbox:
##             textbutton "Achievements" action ShowMenu("achievements")
##             textbutton "Gallery" action ShowMenu("gallery")
##             # etc...
##
## Achievement images should be organized as:
## achievements/
##   ├── ach_ep01_isabella.avif (full image)
##   ├── ach_ep01_isabella_thumb_on.webp
##   ├── ach_ep01_isabella_thumb_onh.webp (hover)
##   └── ach_ep01_isabella_thumb_off.webp