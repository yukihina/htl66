# Documentation for the Ren'Py Custom Notification System
# -------------------------------------------------------

# Purpose:
# This script implements a custom notification system to display important
# information to the player during gameplay.

# Main Components:
# 1. custom_notifications Dictionary:
#    - Stores predefined notifications with titles and messages.

# 2. show_custom_notification Function:
#    - Triggers the display of a specific notification.

# 3. custom_notification Screen:
#    - Defines the visual layout and behavior of notifications.

# Detailed Usage:
# 1. Displaying a Notification:
#    $ show_custom_notification("notification_id")
#    Example: $ show_custom_notification("start_tip")

# 2. Adding New Notifications:
#    Add new entries to the custom_notifications dictionary:
#    "new_notification_id": {
#        "title": "Notification Title",
#        "message": "Notification message content."
#    }

# 3. Customizing Notification Appearance:
#    Modify the custom_notification screen to change the visual style of notifications.

# Connections to Other Files:
# - This system can be called from any script file where notifications are needed.
# - It uses styles and images defined in gui.rpy and screens.rpy.

# Maintenance and Expansion:
# - When adding new types of notifications, ensure they are added to the custom_notifications dictionary.
# - Consider adding parameters for notification duration or priority if needed.

# Note for Novices:
# - The 'zorder' property in the screen definition determines the layer on which the notification appears.
# - The 'at' statement in the frame applies the custom_notification_appear transform for animation.

# Remember: While notifications can provide useful information to players, overuse can 
# become distracting. Use them sparingly for important game events or tips.

default smstip_seen = False
default smstip2_seen = False


init -1 python:
    import random

    custom_notifications = {
        "start_tip": {
            "title": "Tip!",
            "message": "Don't forget to check the 'Help' section - learn the icons and game mechanics!",
            "icon": "info"
        },
        "wt_tip": {
            "title": "Remember!",
            "message": "Activate the Walkthrough on the ASSIST icon in the top left!",
            "icon": "info"
        },
        "sms_tip": {
            "title": "Attention!",
            "message": "If you get a photo, you can open it as many times as you want once it's closed.",
            "icon": "info"
        },
        "sms_tip2": {
            "title": "Tip!",
            "message": "Use your mouse wheel to click and move the photo around.",
            "icon": "info"
        },
        "multicam_tip": {
            "title": "Remember!",
            "message": "Switch camera views by clicking the circles next to your name.",
            "icon": "info"
        },
        "save_tip": {
            "title": "Warning!",
            "message": "You're near the end of this update - recommend saving your progress.",
            "icon": "info"
        },
        "bugfix": {
            "title": "Update Info",
            "message": "Bugfix applied, some values have been patched.",
            "icon": "info"
        },
        "strike1": {
            "title": "What did you do?!",
            "message": "You've got one strike. Two more, and she'll be out of your life for good.",
            "icon": "strike"
        },
        "strike2": {
            "title": "Be Careful!",
            "message": "You've got two strikes. One more, and she'll be out of your life for good.",
            "icon": "strike"
        },
        "strike3": {
            "title": "The End",
            "message": "She's out of your life for good. I'm sorry.",
            "icon": "strike"
        },
        # Corruption notifications
        "corruption_level_up": {
            "title": "Corruption Level Up!",
            "message": "{char}'s corruption is now at level {level}!",
            "icon": "corr"
        },
        "corruption_increase": {
            "title": "Corruption Increasing",
            "message": [
                "{char} is becoming more flirtatious...",
                "{char}'s sexy side is emerging...",
                "{char} is embracing her naughty nature...",
                "{char} feels more uninhibited...",
                "{char} is losing her innocence..."
            ],
            "icon": "corr"
        },
        "corruption_level_down": {
            "title": "Corruption Decreased",
            "message": "{char}'s corruption has dropped to level {level}",
            "icon": "corr"
        },
        "corruption_decrease": {
            "title": "Corruption Fading",
            "message": [
                "{char} is regaining her purity...",
                "{char} is becoming more modest...",
                "{char} feels less corrupted...",
                "{char} is rediscovering her virtuous side...",
                "{char}'s naughty tendencies are waning..."
            ],
            "icon": "corr"
        },
        
        # Trust/Love notifications
        "trust_level_up": {
            "title": "Love Level Up!",
            "message": "{char} has reached love level {level}!",
            "icon": "love"
        },
        "trust_increase": {
            "title": "Love Growing",
            "message": [
                "{char}'s love for you is increasing...",
                "{char} feels closer to you...",
                "{char}'s affection is blossoming...",
                "{char} is opening her heart to you...",
                "{char} trusts you more..."
            ],
            "icon": "love"
        },
        "trust_level_down": {
            "title": "Love Decreased",
            "message": "{char}'s love has dropped to level {level}",
            "icon": "love"
        },
        "trust_decrease": {
            "title": "Love Fading",
            "message": [
                "{char}'s love for you is decreasing...",
                "{char} seems less enamored...",
                "{char} is feeling distant...",
                "{char}'s affection is waning...",
                "{char}'s love is fading..."
            ],
            "icon": "love"
        }
    }


    
    if "active_notifications" not in globals():
        active_notifications = []

    def show_custom_notification(notification_id, **kwargs):
        global active_notifications
        
        if notification_id not in custom_notifications:
            return
        
        notification = custom_notifications[notification_id].copy()

        if isinstance(notification["message"], list):
            notification["message"] = random.choice(notification["message"])
            
        if kwargs:
            notification["message"] = notification["message"].format(**kwargs)

        # Add the new notification
        active_notifications.append(notification)

        # Enforce a limit of 2 notifications at once
        while len(active_notifications) > 2:
            active_notifications.pop(0)

        renpy.show_screen("custom_notifications_screen")
        renpy.restart_interaction()



## --- Notification Styles
style notification_title is achievements_title:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [(1, "#198c5f", 0, 0)]
    color "#27dc95"
    xalign 0.0
    line_spacing 0

style notification_text is achievements_text:
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xmaximum 280
    kerning -1
    line_spacing 0
    
## --- Screen Definition
screen custom_notifications_screen():
    zorder 100

    # Set parameters for stacking
    $ notif_height = 130  # height of each notification background
    $ notif_spacing = 20  # spacing between notifications
    $ base_x = 1380       # base X position for the first notification
    $ base_y = 625        # base Y position for the first notification

    # Iterate over the active_notifications list
    for i, notif in enumerate(active_notifications):
        $ this_y = base_y - i * (notif_height + notif_spacing)
        $ message_length = len(notif["message"])
        $ is_short_message = message_length < 100

        frame:
            at custom_notification_appear(i)
            add "gui/message_bg.png" xpos base_x ypos this_y
            add "gui/icon_[notif.get('icon', 'info')].png" xpos (base_x + 28) ypos (this_y + 29)

            frame:
                background None
                xsize 280
                ysize 90
                xpos (base_x + 181)
                ypos (this_y + 21)

                vbox:
                    if is_short_message:
                        yalign 0.5
                    else:
                        ypos 5
                    spacing 5
                    text _(notif["title"]).upper() style "notification_title"
                    text notif["message"] style "notification_text"

    # A timer to clear all notifications after 10 seconds
    timer 10 action Function(clear_notifications)

init python:
    def clear_notifications():
        global active_notifications
        active_notifications = []
        renpy.hide_screen("custom_notifications_screen")

transform custom_notification_appear(i):
    # Add a slight delay for each subsequent notification
    xalign 1.0
    xoffset 500
    pause 0.5 * i  # Each subsequent notification waits an additional 0.5s
    easein 0.5 xoffset 0
    pause 4
    easeout 0.5 xoffset 600


# $ show_custom_notification("start_tip")