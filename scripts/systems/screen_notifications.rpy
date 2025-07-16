## screen_notifications.rpy - COMPLETE FIX FOR TRANSITION ISSUES
## Custom Layer Solution - Notifications persist through ALL transitions
## 
## SOLUTION EXPLANATION:
## The root cause is that Ren'Py transitions like Fade() affect ALL layers by default,
## including the 'screens' layer where notifications normally appear. 
## 
## This fix creates a dedicated 'notifications' layer that sits above everything
## and is excluded from scene transitions, ensuring notifications never disappear.

################################################################################
## CUSTOM LAYER SETUP - MODIFY YOUR EXISTING options.rpy
################################################################################

## CRITICAL: MODIFY your existing config.layers in options.rpy
## 
## CHANGE THIS LINE IN options.rpy:
## define config.layers = ['master', 'background', 'texture', 'middle', 'forward', 'transient', 'screens', 'overlay', 'states']
##
## TO THIS:
## define config.layers = ['master', 'background', 'texture', 'middle', 'forward', 'transient', 'screens', 'overlay', 'states', 'notifications']
##
## (Just add 'notifications' at the end)

#init -1:
    # Configure layer properties to ensure notifications stay visible
    # Only add this if you want overlay behavior for notifications
    # define config.overlay_layers = ['overlay', 'notifications']

################################################################################
## INITIALIZATION
################################################################################

init -1 python:
    # Import required modules
    import random
    
    # Notification tracking variables
    if "smstip_seen" not in globals():
        smstip_seen = False
    if "smstip2_seen" not in globals():
        smstip2_seen = False

init python:
    # Enhanced notification system state class
    class NotificationState:
        def __init__(self):
            self.active_notifications = []
            self.max_notifications = 2
            self.notification_duration = 10.0
            self.animation_delay = 0.5
            self.positioning = {
                "height": 130,
                "spacing": 20,
                "base_x": 1380,
                "base_y": 625
            }
            # Use dedicated notification layer
            self.notification_layer = "notifications"
            self.notification_counter = 0
    
    # Create global notification state instance
    if not hasattr(store, 'notification_state'):
        notification_state = NotificationState()
    
    # Legacy support for existing code
    if "active_notifications" not in globals():
        active_notifications = []
    
    ############################################################################
    ## NOTIFICATION CONTENT DATABASE (unchanged)
    ############################################################################
    
    custom_notifications = {
        # General tips and information
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
        
        # Strike system notifications
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
        
        # Corruption level notifications
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
        
        # Trust/Love level notifications
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
    
    ############################################################################
    ## ENHANCED NOTIFICATION MANAGEMENT FUNCTIONS
    ############################################################################
    
    def show_custom_notification(notification_id, **kwargs):
        """Show a custom notification with transition immunity"""
        global active_notifications
        
        # Validate notification exists
        if notification_id not in custom_notifications:
            return
        
        # Create notification copy
        notification = custom_notifications[notification_id].copy()
        notification_state.notification_counter += 1
        notification["unique_id"] = notification_state.notification_counter
        
        # Handle random message selection
        if isinstance(notification["message"], list):
            notification["message"] = random.choice(notification["message"])
        
        # Apply formatting
        if kwargs:
            notification["message"] = notification["message"].format(**kwargs)
        
        # Add to queue
        add_notification_to_queue(notification)
        
        # Show on dedicated layer
        show_notification_on_custom_layer()
    
    def add_notification_to_queue(notification):
        """Add notification to queue with limits"""
        global active_notifications
        
        active_notifications.append(notification)
        notification_state.active_notifications.append(notification)
        
        # Enforce limits
        while len(active_notifications) > notification_state.max_notifications:
            active_notifications.pop(0)
        while len(notification_state.active_notifications) > notification_state.max_notifications:
            notification_state.active_notifications.pop(0)
    
    def show_notification_on_custom_layer():
        """Display notifications on the dedicated layer"""
        # Show screen on notifications layer - immune to scene transitions
        renpy.show_screen("transition_immune_notifications", 
                         _layer=notification_state.notification_layer)
        renpy.restart_interaction()
    
    def clear_notifications():
        """Clear all notifications"""
        global active_notifications
        active_notifications = []
        notification_state.active_notifications = []
        renpy.hide_screen("transition_immune_notifications", 
                         layer=notification_state.notification_layer)
    
    def clear_specific_notification(index):
        """Clear specific notification by index"""
        global active_notifications
        if 0 <= index < len(active_notifications):
            active_notifications.pop(index)
        if 0 <= index < len(notification_state.active_notifications):
            notification_state.active_notifications.pop(index)
        
        # Hide if no notifications remain
        if not active_notifications:
            renpy.hide_screen("transition_immune_notifications", 
                             layer=notification_state.notification_layer)
    
    ############################################################################
    ## NOTIFICATION CONTENT HELPERS (unchanged)
    ############################################################################
    
    def get_notification_template(notification_id):
        return custom_notifications.get(notification_id, None)
    
    def add_notification_template(notification_id, title, message, icon="info"):
        custom_notifications[notification_id] = {
            "title": title,
            "message": message,
            "icon": icon
        }
    
    def is_message_short(message, threshold=100):
        return len(message) < threshold
    
    def get_notification_position(index):
        pos = notification_state.positioning
        y_offset = index * (pos["height"] + pos["spacing"])
        return pos["base_x"], pos["base_y"] - y_offset
    
    ############################################################################
    ## SPECIALIZED NOTIFICATION FUNCTIONS (unchanged)
    ############################################################################
    
    def show_corruption_notification(character_name, change_type, level=None):
        if change_type == "increase":
            show_custom_notification("corruption_increase", char=character_name)
        elif change_type == "decrease":
            show_custom_notification("corruption_decrease", char=character_name)
        elif change_type == "level_up" and level:
            show_custom_notification("corruption_level_up", char=character_name, level=level)
        elif change_type == "level_down" and level:
            show_custom_notification("corruption_level_down", char=character_name, level=level)
    
    def show_trust_notification(character_name, change_type, level=None):
        if change_type == "increase":
            show_custom_notification("trust_increase", char=character_name)
        elif change_type == "decrease":
            show_custom_notification("trust_decrease", char=character_name)
        elif change_type == "level_up" and level:
            show_custom_notification("trust_level_up", char=character_name, level=level)
        elif change_type == "level_down" and level:
            show_custom_notification("trust_level_down", char=character_name, level=level)
    
    def show_strike_notification(strike_count):
        if strike_count == 1:
            show_custom_notification("strike1")
        elif strike_count == 2:
            show_custom_notification("strike2")
        elif strike_count >= 3:
            show_custom_notification("strike3")
    
    def show_tip_notification(tip_type):
        if tip_type == "sms" and not smstip_seen:
            show_custom_notification("sms_tip")
            globals()["smstip_seen"] = True
        elif tip_type == "sms2" and not smstip2_seen:
            show_custom_notification("sms_tip2")
            globals()["smstip2_seen"] = True
        elif tip_type in ["start", "wt", "multicam", "save"]:
            show_custom_notification(tip_type + "_tip")

################################################################################
## TRANSITION-IMMUNE NOTIFICATION ANIMATIONS
################################################################################

transform notification_appear_immune(i):
    # Animation completely immune to scene transitions
    xalign 1.0
    xoffset 500
    alpha 1.0
    
    # Staggered entrance
    pause (notification_state.animation_delay * i)
    
    # Smooth slide in
    easein 0.5 xoffset 0
    
    # Display duration
    pause 4.0
    
    # Natural exit
    easeout 0.5 xoffset 600 alpha 0.0

################################################################################
## TRANSITION-IMMUNE NOTIFICATION SCREEN
################################################################################

screen transition_immune_notifications():
    # CRITICAL: This screen is shown on the notifications layer
    # which is excluded from scene transitions
    
    # No zorder needed - layer position handles priority
    
    # Get positioning parameters
    $ notif_height = notification_state.positioning["height"]
    $ notif_spacing = notification_state.positioning["spacing"]
    $ base_x = notification_state.positioning["base_x"]
    $ base_y = notification_state.positioning["base_y"]
    
    # Display each notification
    for i, notif in enumerate(active_notifications):
        $ this_x, this_y = get_notification_position(i)
        $ message_length = len(notif["message"])
        $ is_short_message = is_message_short(notif["message"])
        $ unique_id = notif.get("unique_id", i)
        
        ## Notification frame - completely immune to transitions
        frame:
            id "notification_{}".format(unique_id)
            at notification_appear_immune(i)
            
            ## Background image
            add "gui/message_bg.png" xpos this_x ypos this_y
            
            ## Icon
            add "gui/icon_[notif.get('icon', 'info')].png" xpos (this_x + 28) ypos (this_y + 29)
            
            ## Text content frame
            frame:
                background None
                xsize 280
                ysize 90
                xpos (this_x + 181)
                ypos (this_y + 21)
                
                vbox:
                    if is_short_message:
                        yalign 0.5
                    else:
                        ypos 5
                    spacing 5
                    
                    ## Title - different styles for memory vs regular notifications
                    if notif.get("type") == "memory":
                        text _(notif["title"]).upper() style "memory_notification_title"
                    else:
                        text _(notif["title"]).upper() style "notification_title"

                    ## Message - different styles for memory vs regular notifications  
                    if notif.get("type") == "memory":
                        text notif["message"] style "memory_notification_text"
                    else:
                        text notif["message"] style "notification_text"
    
    # Auto-clear timer
    timer notification_state.notification_duration action Function(clear_notifications)

################################################################################
## LEGACY COMPATIBILITY SCREEN
################################################################################

screen custom_notifications_screen():
    # Redirect to new transition-immune screen for backward compatibility
    use transition_immune_notifications

################################################################################
## NOTIFICATION STYLES (unchanged)
################################################################################

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

## NOTE: Enhanced transitions are no longer needed here!
## All transitions in def_transitions.rpy now automatically exclude the notifications layer.

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## COMPLETE SETUP INSTRUCTIONS:
##
## 1. MODIFY options.rpy (CRITICAL):
##    Find this existing line in your options.rpy:
##    define config.layers = ['master', 'background', 'texture', 'middle', 'forward', 'transient', 'screens', 'overlay', 'states']
##    
##    Change it to:
##    define config.layers = ['master', 'background', 'texture', 'middle', 'forward', 'transient', 'screens', 'overlay', 'states', 'notifications']
##    
##    (Just add 'notifications' at the end to preserve all your existing layers)
##
## 2. REPLACE def_transitions.rpy:
##    Replace your entire def_transitions.rpy file with the modified version
##    This automatically makes ALL transitions exclude the notifications layer
##
## 3. REPLACE screen_notifications.rpy:
##    Replace your screen_notifications.rpy with this code
##
## 4. USAGE (no changes required to existing code):
##    $ show_custom_notification("corruption_increase", char="Elizabeth")
##    $ show_corruption_notification("Amber", "level_up", level=3)
##    scene new_background with slowfade  # Notifications stay visible!
##    
##    ALL your existing transitions work automatically: slowfade, normalfade, circlewipe, etc.
##
## HOW THE FIX WORKS:
##
## 1. CUSTOM LAYER SOLUTION:
##    - Creates dedicated 'notifications' layer above all others
##    - ALL existing transitions automatically exclude this layer
##    - Notification layer is completely immune to scene transitions
##    - No more disappearing notifications during any transition
##
## 2. AUTOMATIC TRANSITION EXCLUSION:
##    - def_transitions.rpy modified to use create_layer_transition() helper
##    - All transitions (slowfade, normalfade, circlewipe, etc.) automatically exclude 'notifications'
##    - Your existing code works exactly the same
##    - Clean separation of concerns - no transition code in notification files
##
## 3. ZERO CODE CHANGES REQUIRED:
##    - All existing script files work without modification
##    - scene bg with slowfade automatically preserves notifications
##    - Future transitions inherit notification immunity automatically
##    - Elegant, maintenance-free solution
##
## TESTING:
## Try this sequence to verify the fix:
## $ show_custom_notification("trust_level_up", char="Amber", level=3)
## scene eigengrau with slowfade
## 
## Expected result:
## ✅ Notification stays visible during entire slowfade transition
## ✅ No disappearing/reappearing behavior
## ✅ Smooth, uninterrupted notification animation
## ✅ Works with ALL transitions (slowfade, normalfade, etc.)
##
## TROUBLESHOOTING:
## - If notifications still disappear: Ensure you modified config.layers in options.rpy correctly
## - If transitions don't work: Verify you replaced def_transitions.rpy completely
## - If error occurs: Check that all required image assets exist in images/wipes/ folder
## - If positioning is wrong: Adjust notification_state.positioning values
## - If other layers break: Verify you kept all existing layers and only added 'notifications'
##
## This solution provides complete immunity to transition interference!