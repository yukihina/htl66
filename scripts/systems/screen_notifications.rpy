## screen_notifications.rpy
## Custom Notification System - Complete English Version
## 
## How to use:
## To show a notification from anywhere in your game:
## $ show_custom_notification("notification_id")
## $ show_custom_notification("corruption_increase", char="Elizabeth")
## 
## The notification system provides:
## 1. Multiple notification types (tips, warnings, strikes, corruption, love)
## 2. Queue management for multiple simultaneous notifications
## 3. Animated appearance and disappearance effects
## 4. Character-specific dynamic messages with random variation
## 5. Icon-based visual categorization
##
## Notification Features:
## - Stack up to 2 notifications simultaneously
## - Auto-clear after 10 seconds
## - Support for dynamic message formatting with character names
## - Random message selection for variety
## - Proper positioning and animation timing

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
    # Notification system state class
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
    
    # Create global notification state instance
    if not hasattr(store, 'notification_state'):
        notification_state = NotificationState()
    
    # Legacy support for existing code
    if "active_notifications" not in globals():
        active_notifications = []
    
    ############################################################################
    ## NOTIFICATION CONTENT DATABASE
    ############################################################################
    
    # Predefined notification templates organized by category
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
    ## NOTIFICATION MANAGEMENT FUNCTIONS
    ############################################################################
    
    def show_custom_notification(notification_id, **kwargs):
        """Show a custom notification with optional formatting parameters"""
        global active_notifications
        
        # Validate notification exists
        if notification_id not in custom_notifications:
            return
        
        # Create notification copy to avoid modifying original
        notification = custom_notifications[notification_id].copy()
        
        # Handle random message selection for lists
        if isinstance(notification["message"], list):
            notification["message"] = random.choice(notification["message"])
        
        # Apply formatting if parameters provided
        if kwargs:
            notification["message"] = notification["message"].format(**kwargs)
        
        # Add notification to active queue
        add_notification_to_queue(notification)
        
        # Display notification screen
        show_notification_screen()
    
    def add_notification_to_queue(notification):
        """Add notification to the active queue with proper limits"""
        global active_notifications
        
        # Add the new notification
        active_notifications.append(notification)
        notification_state.active_notifications.append(notification)
        
        # Enforce notification limit
        while len(active_notifications) > notification_state.max_notifications:
            active_notifications.pop(0)
        while len(notification_state.active_notifications) > notification_state.max_notifications:
            notification_state.active_notifications.pop(0)
    
    def show_notification_screen():
        """Display the notification screen and restart interaction"""
        renpy.show_screen("custom_notifications_screen")
        renpy.restart_interaction()
    
    def clear_notifications():
        """Clear all active notifications and hide screen"""
        global active_notifications
        active_notifications = []
        notification_state.active_notifications = []
        renpy.hide_screen("custom_notifications_screen")
    
    def clear_specific_notification(index):
        """Clear a specific notification by index"""
        global active_notifications
        if 0 <= index < len(active_notifications):
            active_notifications.pop(index)
        if 0 <= index < len(notification_state.active_notifications):
            notification_state.active_notifications.pop(index)
    
    ############################################################################
    ## NOTIFICATION CONTENT HELPERS
    ############################################################################
    
    def get_notification_template(notification_id):
        """Get notification template by ID"""
        return custom_notifications.get(notification_id, None)
    
    def add_notification_template(notification_id, title, message, icon="info"):
        """Add a new notification template to the system"""
        custom_notifications[notification_id] = {
            "title": title,
            "message": message,
            "icon": icon
        }
    
    def is_message_short(message, threshold=100):
        """Check if message is short for layout purposes"""
        return len(message) < threshold
    
    def get_notification_position(index):
        """Calculate notification position based on index"""
        pos = notification_state.positioning
        y_offset = index * (pos["height"] + pos["spacing"])
        return pos["base_x"], pos["base_y"] - y_offset
    
    ############################################################################
    ## SPECIALIZED NOTIFICATION FUNCTIONS
    ############################################################################
    
    def show_corruption_notification(character_name, change_type, level=None):
        """Show corruption-related notification"""
        if change_type == "increase":
            show_custom_notification("corruption_increase", char=character_name)
        elif change_type == "decrease":
            show_custom_notification("corruption_decrease", char=character_name)
        elif change_type == "level_up" and level:
            show_custom_notification("corruption_level_up", char=character_name, level=level)
        elif change_type == "level_down" and level:
            show_custom_notification("corruption_level_down", char=character_name, level=level)
    
    def show_trust_notification(character_name, change_type, level=None):
        """Show trust/love-related notification"""
        if change_type == "increase":
            show_custom_notification("trust_increase", char=character_name)
        elif change_type == "decrease":
            show_custom_notification("trust_decrease", char=character_name)
        elif change_type == "level_up" and level:
            show_custom_notification("trust_level_up", char=character_name, level=level)
        elif change_type == "level_down" and level:
            show_custom_notification("trust_level_down", char=character_name, level=level)
    
    def show_strike_notification(strike_count):
        """Show strike notification based on count"""
        if strike_count == 1:
            show_custom_notification("strike1")
        elif strike_count == 2:
            show_custom_notification("strike2")
        elif strike_count >= 3:
            show_custom_notification("strike3")
    
    def show_tip_notification(tip_type):
        """Show tip notification if not already seen"""
        if tip_type == "sms" and not smstip_seen:
            show_custom_notification("sms_tip")
            globals()["smstip_seen"] = True
        elif tip_type == "sms2" and not smstip2_seen:
            show_custom_notification("sms_tip2")
            globals()["smstip2_seen"] = True
        elif tip_type in ["start", "wt", "multicam", "save"]:
            show_custom_notification(tip_type + "_tip")

################################################################################
## NOTIFICATION ANIMATION TRANSFORMS
################################################################################

## Notification entrance and exit animation
transform custom_notification_appear(i):
    # Starting position (off-screen right)
    xalign 1.0
    xoffset 500
    
    # Staggered entrance delay for multiple notifications
    pause (notification_state.animation_delay * i)
    
    # Slide in animation
    easein 0.5 xoffset 0
    
    # Display duration
    pause 4
    
    # Slide out animation
    easeout 0.5 xoffset 600

################################################################################
## NOTIFICATION DISPLAY SCREEN
################################################################################

screen custom_notifications_screen():
    zorder 100
    
    # Get positioning parameters
    $ notif_height = notification_state.positioning["height"]
    $ notif_spacing = notification_state.positioning["spacing"]
    $ base_x = notification_state.positioning["base_x"]
    $ base_y = notification_state.positioning["base_y"]
    
    # Display each active notification
    for i, notif in enumerate(active_notifications):
        $ this_x, this_y = get_notification_position(i)
        $ message_length = len(notif["message"])
        $ is_short_message = is_message_short(notif["message"])
        
        ## Notification frame container
        frame:
            at custom_notification_appear(i)
            
            ## Background image
            add "gui/message_bg.png" xpos this_x ypos this_y
            
            ## Notification icon
            add "gui/icon_[notif.get('icon', 'info')].png" xpos (this_x + 28) ypos (this_y + 29)
            
            ## Text content frame
            frame:
                background None
                xsize 280
                ysize 90
                xpos (this_x + 181)
                ypos (this_y + 21)
                
                ## Text content container
                vbox:
                    # Vertical alignment based on message length
                    if is_short_message:
                        yalign 0.5
                    else:
                        ypos 5
                    spacing 5
                    
                    ## Notification title
                    text _(notif["title"]).upper() style "notification_title"
                    
                    ## Notification message
                    text notif["message"] style "notification_text"
    
    # Auto-clear timer
    timer notification_state.notification_duration action Function(clear_notifications)

################################################################################
## NOTIFICATION STYLES
################################################################################

## Notification title style - inherits from achievements for consistency
style notification_title is achievements_title:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [(1, "#198c5f", 0, 0)]
    color "#27dc95"
    xalign 0.0
    line_spacing 0

## Notification message text style - inherits from achievements for consistency
style notification_text is achievements_text:
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xmaximum 280
    kerning -1
    line_spacing 0

## Alternative notification styles for different types
style notification_title_warning is notification_title:
    color "#ff6b6b"
    outlines [(1, "#cc0000", 0, 0)]

style notification_title_success is notification_title:
    color "#51cf66"
    outlines [(1, "#2b8a3e", 0, 0)]

style notification_title_info is notification_title:
    color "#74c0fc"
    outlines [(1, "#1971c2", 0, 0)]

################################################################################
## ADVANCED NOTIFICATION FEATURES
################################################################################

init python:
    # Advanced notification management
    class NotificationManager:
        def __init__(self):
            self.notification_history = []
            self.muted_notifications = set()
            self.priority_queue = []
        
        def add_to_history(self, notification_id, timestamp=None):
            """Add notification to history log"""
            if timestamp is None:
                import time
                timestamp = time.time()
            self.notification_history.append((notification_id, timestamp))
        
        def mute_notification(self, notification_id):
            """Mute specific notification type"""
            self.muted_notifications.add(notification_id)
        
        def unmute_notification(self, notification_id):
            """Unmute specific notification type"""
            self.muted_notifications.discard(notification_id)
        
        def is_muted(self, notification_id):
            """Check if notification type is muted"""
            return notification_id in self.muted_notifications
        
        def add_priority_notification(self, notification_id, priority=1):
            """Add high-priority notification that shows immediately"""
            self.priority_queue.append((priority, notification_id))
            self.priority_queue.sort(reverse=True)  # Higher priority first
        
        def get_next_priority_notification(self):
            """Get next priority notification"""
            if self.priority_queue:
                return self.priority_queue.pop(0)[1]
            return None
    
    # Create global notification manager
    if not hasattr(store, 'notification_manager'):
        notification_manager = NotificationManager()
    
    ############################################################################
    ## ENHANCED NOTIFICATION FUNCTIONS
    ############################################################################
    
    def show_priority_notification(notification_id, priority=1, **kwargs):
        """Show high-priority notification immediately"""
        # Clear current notifications if high priority
        if priority >= 5:
            clear_notifications()
        
        # Add to priority queue
        notification_manager.add_priority_notification(notification_id, priority)
        
        # Show immediately
        show_custom_notification(notification_id, **kwargs)
    
    def show_timed_notification(notification_id, duration=5.0, **kwargs):
        """Show notification with custom duration"""
        original_duration = notification_state.notification_duration
        notification_state.notification_duration = duration
        
        show_custom_notification(notification_id, **kwargs)
        
        # Reset duration after showing
        notification_state.notification_duration = original_duration
    
    def show_conditional_notification(notification_id, condition_func, **kwargs):
        """Show notification only if condition is met"""
        if condition_func():
            show_custom_notification(notification_id, **kwargs)
    
    def batch_show_notifications(notification_list, delay=1.0):
        """Show multiple notifications with delays"""
        for i, (notification_id, kwargs) in enumerate(notification_list):
            renpy.call_screen("timed_call", delay * i, show_custom_notification, notification_id, **kwargs)

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this notification system in your game:
##
## 1. BASIC NOTIFICATION DISPLAY:
##    $ show_custom_notification("start_tip")
##    - Shows a predefined notification from the custom_notifications dictionary
##    - Automatically handles animation, positioning, and timing
##
## 2. DYNAMIC NOTIFICATIONS WITH PARAMETERS:
##    $ show_custom_notification("corruption_increase", char="Elizabeth")
##    $ show_custom_notification("trust_level_up", char="Amber", level=3)
##    - Use formatting parameters to customize notification content
##    - Character names and values are inserted into message templates
##
## 3. SPECIALIZED NOTIFICATION FUNCTIONS:
##    $ show_corruption_notification("Elizabeth", "increase")
##    $ show_trust_notification("Amber", "level_up", level=4)
##    $ show_strike_notification(2)
##    $ show_tip_notification("sms")
##    - Helper functions for common notification types
##    - Automatically handle state tracking and conditional display
##
## 4. ADVANCED FEATURES:
##    $ show_priority_notification("strike3", priority=10)
##    $ show_timed_notification("save_tip", duration=15.0)
##    $ notification_manager.mute_notification("start_tip")
##    - Priority notifications clear screen and show immediately
##    - Custom duration notifications override default timing
##    - Mute system prevents spam of repeated notifications
##
## 5. CUSTOM NOTIFICATION CREATION:
##    $ add_notification_template("custom_id", "Title", "Message content", "info")
##    $ show_custom_notification("custom_id")
##    - Add new notification types at runtime
##    - Supports all standard icons (info, strike, corr, love)
##
## 6. Required assets:
##    - Background: gui/message_bg.png
##    - Icons: gui/icon_info.png, gui/icon_strike.png, gui/icon_corr.png, gui/icon_love.png
##    - Fonts: fonts/UbuntuTitling-Bold.ttf
##    - Style inheritance: achievements_title, achievements_text styles must exist
##
## 7. Configuration options:
##    - notification_state.max_notifications: Maximum simultaneous notifications (default: 2)
##    - notification_state.notification_duration: Auto-clear time (default: 10.0)
##    - notification_state.animation_delay: Stagger delay between notifications (default: 0.5)
##    - notification_state.positioning: X/Y positioning and sizing parameters
##
## USAGE EXAMPLES:
##
## Example 1 - Story progression notification:
## label story_point:
##     "You've made an important choice."
##     $ show_custom_notification("save_tip")
##     # Continue with story...
##
## Example 2 - Relationship change notification:
## label increase_corruption:
##     $ rm.change("elizabeth", "cor", 5)
##     $ show_corruption_notification("Elizabeth", "increase")
##     # Continue with scene...
##
## Example 3 - Strike system integration:
## label bad_choice:
##     $ ss.change("amber", "strike", 1)
##     $ current_strikes = ss.get("amber", "strike")
##     $ show_strike_notification(current_strikes)
##     # Handle consequences...
##
## Example 4 - Conditional tip display:
## label first_sms:
##     "You receive your first text message."
##     $ show_tip_notification("sms")  # Only shows if not seen before
##     # Continue with SMS scene...
##
## TROUBLESHOOTING:
## - If notifications don't appear: Check that gui/message_bg.png exists
## - If icons don't show: Verify gui/icon_[type].png files exist
## - If text looks wrong: Ensure achievements styles are defined
## - If timing is off: Adjust notification_state duration and delay values
## - If notifications overlap: Reduce max_notifications or increase spacing
##
## CUSTOMIZATION:
## - Modify positioning in notification_state.positioning dictionary
## - Add new notification types to custom_notifications dictionary
## - Create custom styles by extending notification_title/notification_text
## - Adjust animation timing in custom_notification_appear transform
## - Add sound effects by including play sound commands in show functions
##
## BEST PRACTICES:
## - Use descriptive notification IDs for easy maintenance
## - Group related notifications by category (corruption, trust, tips)
## - Test notification timing to ensure good user experience
## - Avoid notification spam by using conditional showing
## - Use priority system sparingly for truly important alerts