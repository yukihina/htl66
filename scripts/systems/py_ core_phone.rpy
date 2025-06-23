## py_core_phone.rpy
## Phone Conversation System for Ren'Py - Complete English Version
## 
## How to use:
## This script implements a phone conversation system using NVL mode to display
## text messages and conversations in a mobile phone interface.
## 
## To start a phone conversation:
## $ nvl_mode = "phone"
## nvl clear
## character "Message text here"
## 
## The system automatically:
## - Displays messages in phone-style bubbles with character avatars
## - Plays appropriate send/receive sound effects
## - Handles different character color schemes and layouts
## - Supports narrator messages for scene descriptions
## - Manages message animations and transitions
##
## Phone Interface Features:
## - Realistic phone UI with message bubbles
## - Character-specific colors and profile pictures
## - Send/receive sound effects with timing
## - Smooth message appearance animations
## - Scrollable conversation history
## - Support for long conversations
##
## Character Support:
## - Main character (MC) messages appear on the right
## - Other character messages appear on the left
## - Automatic profile picture assignment
## - Character-specific color schemes
## - Narrator messages for scene transitions

################################################################################
## INITIALIZATION
################################################################################

## Enable phone conversation mode
define nvl_mode = "phone"

init -2 python:
    ############################################################################
    ## PHONE SYSTEM CONFIGURATION
    ############################################################################
    
    # Phone positioning configuration
    phone_position_x = 0.3
    phone_position_y = 0.5
    
    ############################################################################
    ## PHONE SOUND EFFECT FUNCTIONS
    ############################################################################
    
    def Phone_ReceiveSound(event, interact=True, **kwargs):
        """
        Play sound effect when receiving a message
        
        Args:
            event: Ren'Py event type
            interact: Whether interaction is allowed
            **kwargs: Additional arguments
        """
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.opus")

    def Phone_SendSound(event, interact=True, **kwargs):
        """
        Play sound effect when sending a message
        
        Args:
            event: Ren'Py event type
            interact: Whether interaction is allowed
            **kwargs: Additional arguments
        """
        if event == "show_done":
            renpy.sound.play("audio/SendText.opus")

    def print_bonjour():
        """Debug function for testing purposes"""
        print("bonjour")
    
    # Register sound functions globally
    globals()['Phone_ReceiveSound'] = Phone_ReceiveSound
    globals()['Phone_SendSound'] = Phone_SendSound

    ############################################################################
    ## CHARACTER PROFILE CONFIGURATION
    ############################################################################
    
    # Character profile picture mapping (excluding MC since mc_name isn't defined yet)
    character_profiles = {
        "Antonella": "gui/profile_pic_anto.png",
        "Isabella": "gui/profile_pic_isa.png",
        "Amber": "gui/profile_pic_amb.png",
        "Madison": "gui/profile_pic_mad.png",
        "Paz": "gui/profile_pic_paz.png",
        "Nanami": "gui/profile_pic_nana.png",
        "Kanae": "gui/profile_pic_kan.png",
        "Mom": "gui/profile_pic_eli.png",
        "Elizabeth": "gui/profile_pic_eli.png",
        "Arlette": "gui/profile_pic_arl.png"
    }
    
    # Character name color schemes
    character_name_colors = {
        "Antonella": "#ff4d4d",
        "Isabella": "#00b7eb",
        "Amber": "#FF3333",
        "Madison": "#ff5349",
        "Paz": "#7f7fc5",
        "Nanami": "#FFB6C1",
        "Kanae": "#33ffff",
        "Mom": "#DBB2D1",
        "Elizabeth": "#da86c5",
        "Arlette": "#ffa69e"
    }
    
    # Character text color schemes (excluding MC since mc_name isn't defined yet)
    character_text_colors = {
        "Antonella": "#ffdbdb",
        "Isabella": "#b9f2ff",
        "Amber": "#ff9090",
        "Madison": "#ffc0bc",
        "Paz": "#cbcbf2",
        "Nanami": "#facbd2",
        "Kanae": "#b2ffff",
        "Arlette": "#faf3dd"
    }
    
    ############################################################################
    ## PHONE HELPER FUNCTIONS
    ############################################################################
    
    def get_character_profile(character_name):
        """Get profile picture for a character"""
        # Handle MC case dynamically since mc_name isn't available at init time
        if hasattr(store, 'mc_name') and character_name == mc_name:
            return "gui/profile_pic_mc.png"
        return character_profiles.get(character_name, "gui/phone_received_icon.png")
    
    def get_character_name_color(character_name):
        """Get name color for a character"""
        return character_name_colors.get(character_name, "#000")
    
    def get_character_text_color(character_name):
        """Get text color for a character"""
        # Handle MC case dynamically since mc_name isn't available at init time
        if hasattr(store, 'mc_name') and character_name == mc_name:
            return "#FFD119"
        return character_text_colors.get(character_name, "#000")
    
    def is_mc_message(character_name):
        """Check if message is from main character"""
        return hasattr(store, 'mc_name') and character_name == mc_name
    
    def get_message_frame(character_name):
        """Get appropriate message frame based on sender"""
        if is_mc_message(character_name):
            return "gui/phone_send_frame.png"
        else:
            return "gui/phone_received_frame.png"

################################################################################
## TRANSFORMS AND ANIMATIONS
################################################################################

init:
    ## Phone positioning transform
    transform phone_transform(pXalign=0.5, pYalign=0.5):
        xcenter pXalign
        yalign pYalign

    ## Phone appearance animation (for single message conversations)
    transform phone_appear(pXalign=0.5, pYalign=0.5):
        xcenter pXalign
        yalign pYalign
        on show:
            yoffset 1080
            easein_back 1.0 yoffset 0
    
    ## Message appearance animation with direction
    transform message_appear(pDirection):
        alpha 0.0
        xoffset 50 * pDirection
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            easein_back 0.5 xoffset 0

    ## Profile icon appearance animation
    transform message_appear_icon():
        zoom 0.0
        easein_back 0.5 zoom 1.0

    ## Narrator message animation
    transform message_narrator:
        alpha 0.0
        yoffset -50
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            easein_back 0.5 yoffset 0

################################################################################
## PHONE CONVERSATION SCREENS
################################################################################

## Main phone dialogue container screen
screen PhoneDialogue(dialogue, items=None):
    style_prefix "phoneFrame"
    
    frame at phone_transform(phone_position_x, phone_position_y):
        # Special animation for single message conversations
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        
        viewport:
            draggable True
            mousewheel True
            yinitial 1.0
            
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100

## Phone text rendering screen
screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    
    for id_d, d in enumerate(dialogue):
        # Handle narrator messages (scene descriptions)
        if d.who == None:
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
        
        # Handle character messages
        else:
            $ message_frame = get_message_frame(d.who)

            hbox:
                spacing 10
                
                # Reverse layout for MC messages (appear on right)
                if is_mc_message(d.who):
                    box_reverse True
                
                # Show profile icon for first message from each character
                if previous_d_who != d.who:
                    $ message_icon = get_character_profile(d.who)

                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    
                    # Show character name for non-MC first messages
                    if not is_mc_message(d.who) and previous_d_who != d.who:
                        text d.who:
                            color get_character_name_color(d.who)
                    
                    # Message bubble frame
                    frame:
                        padding (20,20)
                        background Frame(message_frame, 23,23,23,23)
                        xsize 350
                        
                        # Animation for current message
                        if d.current:
                            if is_mc_message(d.who):
                                at message_appear(1)
                            else:
                                at message_appear(-1)
                        
                        # Message text with character-specific styling
                        text d.what:
                            pos (0,0)
                            xsize 350
                            slow_cps False
                            color get_character_text_color(d.who)
                            
                            # Special positioning for MC messages
                            if is_mc_message(d.who):
                                text_align 1.0
                                xpos -580
                            
                            id d.what_id
                        
        $ previous_d_who = d.who

################################################################################
## PHONE INTERFACE STYLES
################################################################################

## Base phone frame style
style phoneFrame is default

## Phone frame background and dimensions
style phoneFrame_frame:
    background Transform("gui/phone_bg.png", xcenter=0.5, yalign=0.5)
    ysize 780
    xsize 495

## Phone viewport styling
style phoneFrame_viewport:
    yfill True
    xfill True
    yoffset 9

## Phone message container styling
style phoneFrame_vbox:
    spacing 10
    xfill True

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this phone conversation system in your game:
## 
## 1. Starting a phone conversation:
##    $ nvl_mode = "phone"
##    nvl clear
##    character "Hello! How are you?"
##    mc "I'm doing well, thanks for asking."
##
## 2. The system will automatically:
##    - Display messages in phone-style bubbles
##    - Play appropriate send/receive sound effects
##    - Show character profile pictures for first messages
##    - Apply character-specific color schemes
##    - Handle message animations and transitions
##
## 3. Adding narrator messages (scene descriptions):
##    nvl clear
##    "The phone buzzes with a new message."
##    character "Are you free tonight?"
##
## 4. Ending phone conversations:
##    nvl clear
##    $ nvl_mode = "normal"  # Return to normal NVL mode
##
## 5. Required assets:
##    - Phone background: gui/phone_bg.png
##    - Message frames: gui/phone_send_frame.png, gui/phone_received_frame.png
##    - Profile pictures: gui/profile_pic_*.png for each character
##    - Sound effects: audio/ReceiveText.opus, audio/SendText.opus
##    - Default received icon: gui/phone_received_icon.png
##
## 6. Character configuration:
##    - Add new characters to character_profiles dictionary
##    - Set character colors in character_name_colors and character_text_colors
##    - Ensure profile pictures exist for all characters
##
## Example phone conversation:
## label phone_amber:
##     $ nvl_mode = "phone"
##     nvl clear
##     
##     "Your phone buzzes with a new message from Amber."
##     
##     amber "Hey, are you free tonight?"
##     mc "Yeah, what's up?"
##     amber "Want to grab dinner? I know a great place."
##     mc "Sounds perfect! What time?"
##     amber "How about 7 PM? I'll pick you up."
##     mc "See you then! 😊"
##     
##     nvl clear
##     $ nvl_mode = "normal"
##     
##     "You put your phone away, looking forward to the evening."
##
## Asset organization:
## gui/
##   ├── phone_bg.png (phone interface background)
##   ├── phone_send_frame.png (MC message bubble)
##   ├── phone_received_frame.png (other character message bubble)
##   ├── phone_received_icon.png (default profile icon)
##   ├── profile_pic_mc.png (MC profile picture)
##   ├── profile_pic_amb.png (Amber profile picture)
##   └── profile_pic_*.png (other character profiles)
##
## audio/
##   ├── ReceiveText.opus (incoming message sound)
##   └── SendText.opus (outgoing message sound)
##
## Performance considerations:
## - Phone mode uses NVL system efficiently
## - Animations are optimized for smooth playback
## - Profile pictures are cached automatically
## - Sound effects are played only when appropriate
##
## Customization options:
## - Adjust phone_position_x and phone_position_y for different screen positions
## - Modify character color schemes in the configuration dictionaries
## - Change message frame designs by updating frame images
## - Adjust animation timing in the transform definitions
##
## Best practices:
## - Always clear NVL history before starting new phone conversations
## - Use narrator messages to provide context and scene transitions
## - Keep message lengths reasonable for mobile-style display
## - Test phone conversations on different screen sizes
## - Ensure all character profile pictures are consistent in style and size
##
## Troubleshooting:
## - If sounds don't play: Check that audio files exist and are properly formatted
## - If profile pictures don't show: Verify file paths in character_profiles dictionary
## - If colors look wrong: Check character color configuration dictionaries
## - If layout breaks: Ensure phone background image dimensions are correct