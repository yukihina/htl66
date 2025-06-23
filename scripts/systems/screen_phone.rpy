## screen_phone.rpy
## Phone Notification System - Complete English Version
## 
## How to use:
## To show SMS notification:
## show screen phone_icons("label_name")
## 
## To show video call notification:
## show screen videocall_icons("label_name")
## 
## To show menu buttons:
## show screen menu_button("Option 1", "label1", "Option 2", "label2", ...)
##
## Phone Notification Features:
## The phone system provides:
## 1. Animated SMS notification with shake effect
## 2. Video call notification display
## 3. Interactive menu system with custom options
## 4. Open/Close actions for user interaction
## 5. Modal overlays with vignette backgrounds
##
## User Interaction:
## Players can choose to open notifications (jumps to specified label)
## or close them (returns to previous screen)

################################################################################
## INITIALIZATION
################################################################################

init python:
    # Phone system state class
    class PhoneState:
        def __init__(self):
            self.current_notification = None
            self.notification_active = False
            self.menu_options = []
            self.background_alpha = 0.45
    
    # Create global phone state instance
    if not hasattr(store, 'phone_state'):
        phone_state = PhoneState()
    
    ############################################################################
    ## PHONE NOTIFICATION MANAGEMENT
    ############################################################################
    
    def set_phone_notification(notification_type):
        """Set the current active notification type"""
        phone_state.current_notification = notification_type
        phone_state.notification_active = True
    
    def clear_phone_notification():
        """Clear the current notification"""
        phone_state.current_notification = None
        phone_state.notification_active = False
    
    def is_phone_notification_active():
        """Check if any phone notification is currently active"""
        return phone_state.notification_active
    
    ############################################################################
    ## MENU SYSTEM HELPERS
    ############################################################################
    
    def create_menu_options(*args):
        """Create menu options from paired arguments (text, label)"""
        options = []
        for i in range(0, len(args), 2):
            if i + 1 < len(args):
                option_text = args[i]
                option_label = args[i + 1]
                options.append((option_text, option_label))
        return options
    
    def get_menu_option_count(args):
        """Get the number of menu options from arguments"""
        return len(args) // 2
    
    ############################################################################
    ## PHONE INTERACTION ACTIONS
    ############################################################################
    
    def phone_open_action(jump_to_label):
        """Action for opening a phone notification"""
        clear_phone_notification()
        renpy.jump(jump_to_label)
    
    def phone_close_action():
        """Action for closing a phone notification"""
        clear_phone_notification()
        renpy.call_screen_return()
    
    def menu_jump_action(label_name):
        """Action for menu button selection"""
        renpy.jump(label_name)

################################################################################
## PHONE ANIMATION TRANSFORMS
################################################################################

## SMS icon shake animation - creates attention-grabbing movement
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

## Phone button alpha animation - provides visual feedback on hover
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

################################################################################
## SMS NOTIFICATION SCREEN
################################################################################

screen phone_icons(jump_to):
    ## Modal overlay to prevent interaction with background
    modal True
    
    ## Set notification state when screen is shown
    on "show" action Function(set_phone_notification, "sms")
    on "hide" action Function(clear_phone_notification)
    
    ## Vignette background overlay
    add "vignette" at igm_appear_bg alpha phone_state.background_alpha
    
    ## Main notification display frame
    frame at igm_appear_fg:
        ## SMS icon with shake animation
        vbox:
            xalign 0.5
            yalign 0.35
            add "gui/phone_sms.png" at phone_sms_icon yalign 0.5 xalign 0.5
        
        ## Action buttons (Open/Close)
        hbox:
            spacing 80
            xalign 0.5
            yalign 0.5
            
            ## Open notification button
            imagebutton:
                idle "gui/open_off.png"
                hover "gui/open_on.png"
                action [Hide("phone_icons"), Jump(jump_to)]
                at phone_icon_alpha
            
            ## Close notification button
            imagebutton:
                idle "gui/close_off.png"
                hover "gui/close_on.png"
                action [Hide("phone_icons"), Return()]
                at phone_icon_alpha

################################################################################
## VIDEO CALL NOTIFICATION SCREEN
################################################################################

screen videocall_icons(jump_to):
    ## Modal overlay to prevent interaction with background
    modal True
    
    ## Set notification state when screen is shown
    on "show" action Function(set_phone_notification, "videocall")
    on "hide" action Function(clear_phone_notification)
    
    ## Vignette background overlay
    add "vignette" at igm_appear_bg alpha phone_state.background_alpha
    
    ## Main notification display frame
    frame at igm_appear_fg:
        ## Video call icon with shake animation
        vbox:
            xalign 0.5
            yalign 0.35
            add "gui/phone_vc.png" at phone_sms_icon yalign 0.5 xalign 0.5
        
        ## Action buttons (Open only - no close for urgent calls)
        hbox:
            spacing 80
            xalign 0.5
            yalign 0.5
            
            ## Open video call button
            imagebutton:
                idle "gui/open_off.png"
                hover "gui/open_on.png"
                action [Hide("videocall_icons"), Jump(jump_to)]
                at phone_icon_alpha

################################################################################
## INTERACTIVE MENU SYSTEM SCREEN
################################################################################

screen menu_button(*args):
    ## Modal overlay to prevent interaction with background
    modal True
    
    ## Set notification state when screen is shown
    on "show" action Function(set_phone_notification, "menu")
    on "hide" action Function(clear_phone_notification)
    
    ## Background warning/attention graphic
    frame:
        add "achtung" at igm_appear_fg:
            align (0.07, 0.4)
        
        ## Main menu content area
        xpos 800
        yalign 0.5
        
        ## Menu options container
        vbox:
            style_prefix "choice"
            
            ## Generate menu buttons from paired arguments
            for i in range(0, len(args), 2):
                if i + 1 < len(args):
                    $ option_text = args[i]
                    $ option_label = args[i + 1]
                    
                    textbutton "[option_text]":
                        action [Hide("menu_button"), Jump(option_label)]
                        at igm_appear_fg2

################################################################################
## PHONE NOTIFICATION STYLES
################################################################################

## Base phone notification frame style
style phone_frame:
    background None
    xfill False
    yfill False

## Phone notification text styles
style phone_notification_text:
    kerning 0
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#ffffff"
    text_align 0.5
    xalign 0.5

## Phone button styles
style phone_button:
    background None
    hover_background None

style phone_button_text:
    kerning 0
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#ffffff"
    hover_color "#27dc95"
    text_align 0.5

## Menu choice button styles (extends existing choice style)
style choice_button:
    xalign 0.0
    background None

style choice_text:
    kerning 0
    size 22
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    hover_color "#27dc95"

################################################################################
## ADVANCED PHONE FEATURES
################################################################################

## Phone notification queue system for multiple notifications
init python:
    class PhoneNotificationQueue:
        def __init__(self):
            self.queue = []
            self.current_index = 0
        
        def add_notification(self, notification_type, jump_label):
            """Add notification to queue"""
            self.queue.append((notification_type, jump_label))
        
        def get_next_notification(self):
            """Get next notification from queue"""
            if self.queue and self.current_index < len(self.queue):
                notification = self.queue[self.current_index]
                self.current_index += 1
                return notification
            return None
        
        def clear_queue(self):
            """Clear all notifications from queue"""
            self.queue = []
            self.current_index = 0
        
        def has_notifications(self):
            """Check if there are pending notifications"""
            return len(self.queue) > self.current_index
    
    # Create global notification queue
    if not hasattr(store, 'phone_notifications'):
        phone_notifications = PhoneNotificationQueue()
    
    ############################################################################
    ## NOTIFICATION QUEUE MANAGEMENT
    ############################################################################
    
    def queue_sms_notification(jump_label):
        """Add SMS notification to queue"""
        phone_notifications.add_notification("sms", jump_label)
    
    def queue_videocall_notification(jump_label):
        """Add video call notification to queue"""
        phone_notifications.add_notification("videocall", jump_label)
    
    def show_next_notification():
        """Show next notification from queue"""
        notification = phone_notifications.get_next_notification()
        if notification:
            notification_type, jump_label = notification
            if notification_type == "sms":
                renpy.show_screen("phone_icons", jump_label)
            elif notification_type == "videocall":
                renpy.show_screen("videocall_icons", jump_label)
    
    def clear_all_notifications():
        """Clear all pending notifications"""
        phone_notifications.clear_queue()
        clear_phone_notification()

################################################################################
## HELPER SCREENS FOR EASY INTEGRATION
################################################################################

## Quick SMS notification helper
screen quick_sms(message, jump_to):
    modal True
    
    frame:
        xalign 0.5
        yalign 0.3
        background "gui/phone_notification_bg.png"
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "New Message" style "phone_notification_text"
            text "[message]" style "phone_notification_text" size 18
            
            hbox:
                spacing 40
                xalign 0.5
                
                textbutton "Read":
                    style "phone_button"
                    action [Hide("quick_sms"), Jump(jump_to)]
                
                textbutton "Dismiss":
                    style "phone_button"
                    action Hide("quick_sms")

## Quick video call helper
screen quick_videocall(caller_name, jump_to):
    modal True
    
    frame:
        xalign 0.5
        yalign 0.3
        background "gui/phone_notification_bg.png"
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "Incoming Video Call" style "phone_notification_text"
            text "From: [caller_name]" style "phone_notification_text" size 18
            
            hbox:
                spacing 40
                xalign 0.5
                
                textbutton "Answer":
                    style "phone_button"
                    action [Hide("quick_videocall"), Jump(jump_to)]
                
                textbutton "Decline":
                    style "phone_button"
                    action Hide("quick_videocall")

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this phone notification system in your game:
##
## 1. BASIC SMS NOTIFICATION:
##    show screen phone_icons("sms_conversation_label")
##    - Shows animated SMS icon with open/close options
##    - Player can open to jump to specified label or close to return
##
## 2. VIDEO CALL NOTIFICATION:
##    show screen videocall_icons("videocall_scene_label")
##    - Shows video call icon with open option
##    - Player opens call to jump to specified label
##
## 3. INTERACTIVE MENU:
##    show screen menu_button("Option 1", "label1", "Option 2", "label2", "Option 3", "label3")
##    - Shows menu with custom options
##    - Each option jumps to its corresponding label
##
## 4. QUICK NOTIFICATIONS (simplified versions):
##    show screen quick_sms("Hey, how are you?", "sms_label")
##    show screen quick_videocall("Elizabeth", "videocall_label")
##
## 5. NOTIFICATION QUEUE SYSTEM:
##    $ queue_sms_notification("sms_label1")
##    $ queue_videocall_notification("call_label")
##    $ show_next_notification()  # Shows first notification in queue
##
## 6. Required assets:
##    - GUI images: gui/phone_sms.png, gui/phone_vc.png
##    - Button images: gui/open_off.png, gui/open_on.png, gui/close_off.png, gui/close_on.png
##    - Background images: vignette, achtung, gui/phone_notification_bg.png
##    - Transform definitions: igm_appear_bg, igm_appear_fg, igm_appear_fg2
##
## 7. Screen management:
##    - All phone screens are modal to prevent background interaction
##    - Automatic state management tracks active notifications
##    - Queue system allows multiple pending notifications
##
## USAGE EXAMPLES:
##
## Example 1 - Simple SMS in your story:
## label story_scene:
##     "You're walking down the street when your phone buzzes."
##     show screen phone_icons("read_sms")
##     return
##
## label read_sms:
##     "You check your phone and see a message from Elizabeth."
##     # Continue with SMS conversation...
##
## Example 2 - Video call during gameplay:
## label gameplay_scene:
##     "Suddenly, your phone rings with a video call."
##     show screen videocall_icons("elizabeth_calls")
##     return
##
## label elizabeth_calls:
##     scene black with fade
##     "You answer the video call."
##     # Continue with video call scene...
##
## Example 3 - Decision menu:
## label choice_point:
##     "Your phone shows multiple options."
##     show screen menu_button("Call Elizabeth", "call_elizabeth", "Text Amber", "text_amber", "Ignore Phone", "ignore_phone")
##     return
##
## Example 4 - Notification queue:
## label busy_day:
##     "It's a busy day and your phone keeps buzzing."
##     $ queue_sms_notification("morning_text")
##     $ queue_videocall_notification("lunch_call")
##     $ queue_sms_notification("evening_text")
##     $ show_next_notification()  # Shows morning_text first
##     return
##
## TROUBLESHOOTING:
## - If animations don't work: Check that igm_appear transforms are defined
## - If buttons don't respond: Ensure modal True is set on screens
## - If images don't show: Verify all GUI assets exist in gui/ folder
## - If jumps don't work: Check that target labels exist in your script
##
## CUSTOMIZATION:
## - Modify phone_state.background_alpha to change overlay darkness
## - Adjust transform timing in phone_sms_icon for different shake speeds
## - Change button spacing and positioning by modifying hbox/vbox properties
## - Add sound effects by including play sound commands in screen actions
##
## ADVANCED FEATURES:
## - Notification queue system for managing multiple alerts
## - Quick notification helpers for simple message/call displays
## - State management tracks active notifications across screens
## - Extensible design allows easy addition of new notification types