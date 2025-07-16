## screen_memories.rpy - COMPLETE INTEGRATION WITH NOTIFICATION POSITIONING
## 
## SOLUTION: Memory notifications now use the existing notification queue and positioning system
## This prevents overlapping and ensures proper stacking behavior

################################################################################
## INITIALIZATION - FIXED
################################################################################

init python:
    # Memories system state class
    class MemoriesState:
        def __init__(self):
            self.current_memory = None
            self.current_image_index = {}
            self.viewing_mode = False
            self.selected_act = 1
            self.notification_duration = 5.0
    
    # Create global memories state instance
    if not hasattr(store, 'memories_state'):
        memories_state = MemoriesState()

# CRITICAL FIX: Use default statement for persistent data initialization
default persistent.unlocked_memories = {}

init python:
    ############################################################################
    ## MEMORY DATA CONFIGURATION - SHORTENED NAMES FOR NOTIFICATIONS
    ############################################################################
    
    # List of all memory IDs organized by release order
    all_memories = [
        # EP01 Memories
        "m_ep01_library",
        "m_ep01_clothes",
        "m_ep01_home",
        "m_ep01_laundry",
        "m_ep01_confession",
        # EP02 Memories
        "m_ep02_friend",
        "m_ep02_reunion",
        "m_ep02_hangover",
        "m_ep02_friendship",
        "m_ep02_hotel",
        "m_ep02_revelation",
        "m_ep02_kitchen",
        # EP03 Memories
        "m_ep03_talk",
        "m_ep03_night",
        "m_ep03_green",
        "m_ep03_tv",
        # Add new memory IDs here following the same pattern
    ]
    
    # Memory definitions with SHORTENED NAMES for notification compatibility
    memories_dict = {
        # ===== EP01 MEMORIES =====
        "m_ep01_library": {
            "name": "Library Meeting",  # Was: "Meeting Antonella at library"
            "thumbnail_idle": "memories/m_ep01_library_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep01_library_thumb_hover.webp", 
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_3rddream01",
                "ep01_3rddream02",
                "ep01_3rddream03",
                "ep01_3rddream05",
                "ep01_3rddream07",
                "ep01_3rddream09"
            ]
        },
        "m_ep01_clothes": {
            "name": "Goth Girl",  # Was: "Goth woman in the store"
            "thumbnail_idle": "memories/m_ep01_clothes_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep01_clothes_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_clothing04",
                "ep01_clothing05",
                "ep01_clothing06",
                "ep01_clothing07",
                "ep01_clothing08"
            ]
        },
        "m_ep01_home": {
            "name": "Home Sweet Home",  # Was: "Amber at home"
            "thumbnail_idle": "memories/m_ep01_home_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep01_home_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_home02",
                "ep01_home04",
                "ep01_home06",
                "ep01_home07",
                "ep01_home08",
                "ep01_home09",
                "ep01_home12"
            ]
        },
        "m_ep01_laundry": {
            "name": "Laundry Day",  # Was: "Amber at the laundry"
            "thumbnail_idle": "memories/m_ep01_laundry_thumb_idle.webp", 
            "thumbnail_hover": "memories/m_ep01_laundry_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_amberfail02",
                "ep01_amberfail03",
                "ep01_amberfail04",
                "ep01_amberfail05"
            ]
        },
        "m_ep01_confession": {
            "name": "Heart to Heart",  # Was: "Amber's confession"
            "thumbnail_idle": "memories/m_ep01_confession_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep01_confession_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_amberconfess02",
                "ep01_amberconfess09",
                "ep01_amberconfess10"
            ]
        },
        # ===== EP02 MEMORIES =====
        "m_ep02_friend": {
            "name": "Old Friend",  # Was: "Reconnecting with a Friend"
            "thumbnail_idle": "memories/m_ep02_friend_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep02_friend_thumb_hover.webp", 
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_booze09",
                "ep02_booze11",
                "ep02_booze12",
                "ep02_booze13",
                "ep02_booze15",
                "ep02_booze16"
            ]
        },
        "m_ep02_reunion": {
            "name": "Surprise Reunion",  # Was: "Unexpected Reunion"
            "thumbnail_idle": "memories/m_ep02_reunion_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep02_reunion_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_whore09",
                "ep02_whore10",
                "ep02_whore13",
                "ep02_whore15",
                "ep02_whore16",
                "ep02_whore18",
                "ep02_whore19",
                "ep02_whore20",
                "ep02_whore21",
                "ep02_whore22"
            ]
        },
        "m_ep02_hangover": {
            "name": "Morning After",  # Was: "Morning After Hangover"
            "thumbnail_idle": "memories/m_ep02_hangover_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep02_hangover_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_nxtbooze06",
                "ep02_nxtbooze07",
                "ep02_nxtbooze08"
            ]
        },
        "m_ep02_friendship": {
            "name": "Friendship Test",  # Was: "Testing Friendship Bonds"
            "thumbnail_idle": "memories/m_ep02_friendship_thumb_idle.webp", 
            "thumbnail_hover": "memories/m_ep02_friendship_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_friends03",
                "ep02_friends04",
                "ep02_friends05",
                "ep02_friends06",
                "ep02_friends07",
                "ep02_friends08",
                "ep02_friends09",
                "ep02_friends10",
                "ep02_friends11"
            ]
        },
        "m_ep02_hotel": {
            "name": "Hotel Night",  # Was: "Hotel Encounter"
            "thumbnail_idle": "memories/m_ep02_hotel_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep02_hotel_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_arlehotel20",
                "ep02_arlehotel21",
                "ep02_arlehotel22",
                "ep02_arlehotel23"
            ]
        },
        "m_ep02_revelation": {
            "name": "Big Secret",  # Was: "Shocking Revelation"
            "thumbnail_idle": "memories/m_ep02_revelation_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep02_revelation_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_escort01",
                "ep02_escort05",
                "ep02_escort08"
            ]
        },
        "m_ep02_kitchen": {
            "name": "Kitchen Drama",  # Was: "Kitchen Confrontation"
            "thumbnail_idle": "memories/m_ep02_kitchen_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep02_kitchen_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep02_arledeath01",
                "ep02_arledeath02",
                "ep02_arledeath03",
                "ep02_arledeath04",
                "ep02_arledeath05"
            ]
        },
        # ===== EP03 MEMORIES =====
        "m_ep03_talk": {
            "name": "Deep Talk",  # Was: "Important Talk"
            "thumbnail_idle": "memories/m_ep03_talk_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep03_talk_thumb_hover.webp", 
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep03_ambertalk07",
                "ep03_ambertalk08",
                "ep03_ambertalk09",
                "ep03_ambertalk10",
                "ep03_ambertalk33",
                "ep03_ambertalk38",
                "ep03_ambertalk49"
            ]
        },
        "m_ep03_night": {
            "name": "Special Night",  # Was: "Intimate Night"
            "thumbnail_idle": "memories/m_ep03_night_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep03_night_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep03_ambernight18",
                "ep03_ambernight19",
                "ep03_afterpool01",
                "ep03_afterpool02",
                "ep03_afterpool05",
                "ep03_afterpool06",
                "ep03_afterpool07",
                "ep03_afterpool08",
                "ep03_afterpool09",
                "ep03_afterpool10",
                "ep03_afterpool11",
                "ep03_afterpool12",
                "ep03_afterpool13",
                "ep03_afterpool14",
                "ep03_afterpool15",
                "ep03_afterpool16"
            ]
        },
        "m_ep03_green": {
            "name": "Green Scene",  # Was: "Green Moment"
            "thumbnail_idle": "memories/m_ep03_green_thumb_idle.webp",
            "thumbnail_hover": "memories/m_ep03_green_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep03_caught3",
                "ep03_caught4",
                "ep03_caught5",
                "ep03_caught6",
                "ep03_caught7"
            ]
        },
        "m_ep03_tv": {
            "name": "TV Room Chat",  # Was: "TV Room Discussion"
            "thumbnail_idle": "memories/m_ep03_tv_thumb_idle.webp", 
            "thumbnail_hover": "memories/m_ep03_tv_thumb_hover.webp",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep03_madtalk03",
                "ep03_madtalk04",
                "ep03_madtalk05",
                "ep03_madtalk06",
                "ep03_madtalk07",
                "ep03_madtalk08",
                "ep03_madtalk09",
                "ep03_madtalk10",
                "ep03_madtalk11",
                "ep03_madtalk12"
            ]
        }
    }
    
    ############################################################################
    ## MEMORY MANAGEMENT FUNCTIONS - COMPLETELY FIXED
    ############################################################################
    
    def unlock_memory(memory_id):
        """Unlock a specific memory and show notification"""
        # CRITICAL FIX: Ensure persistent.unlocked_memories is always a dict
        if persistent.unlocked_memories is None:
            persistent.unlocked_memories = {}
        
        # Only unlock if not already unlocked to avoid spam
        if not persistent.unlocked_memories.get(memory_id, False):
            persistent.unlocked_memories[memory_id] = True
            # Show unlock notification using INTEGRATED positioning system
            show_memory_unlock_notification(memory_id)
    
    def is_memory_unlocked(memory_id):
        """Check if a specific memory is unlocked"""
        # CRITICAL FIX: Ensure persistent.unlocked_memories is always a dict
        if persistent.unlocked_memories is None:
            persistent.unlocked_memories = {}
        return persistent.unlocked_memories.get(memory_id, False)
    
    def get_unlocked_memories_count():
        """Get total count of unlocked memories"""
        # CRITICAL FIX: Ensure persistent.unlocked_memories is always a dict
        if persistent.unlocked_memories is None:
            persistent.unlocked_memories = {}
            return 0
        return sum(1 for unlocked in persistent.unlocked_memories.values() if unlocked)
    
    def reset_all_memories():
        """Reset all memory unlock status (debug function)"""
        persistent.unlocked_memories = {}
        memories_state.current_image_index = {}
        renpy.save_persistent()
    
    ############################################################################
    ## MEMORY VIEWING FUNCTIONS
    ############################################################################
    
    def start_memory_viewing(memory_id):
        """Initialize memory viewing session"""
        if memory_id not in memories_dict:
            return False
        
        if not is_memory_unlocked(memory_id):
            return False
            
        memories_state.current_memory = memory_id
        memories_state.current_image_index[memory_id] = 0
        memories_state.viewing_mode = True
        return True
    
    def advance_memory_image(memory_id):
        """Advance to next image in memory sequence"""
        if memory_id not in memories_dict:
            return
            
        memory = memories_dict[memory_id]
        current_index = memories_state.current_image_index.get(memory_id, 0)
        
        # Advance to next image
        current_index += 1
        
        # Check if we've reached the end
        if current_index >= len(memory["images"]):
            # Reset index and return to gallery
            memories_state.current_image_index[memory_id] = 0
            memories_state.viewing_mode = False
            memories_state.current_memory = None
            renpy.hide_screen("memory_viewer")
            renpy.show_screen("memories_gallery")
        else:
            # Update index and continue viewing
            memories_state.current_image_index[memory_id] = current_index
            renpy.restart_interaction()
    
    def get_current_memory_image(memory_id):
        """Get current image for a memory"""
        if memory_id not in memories_dict:
            return None
            
        memory = memories_dict[memory_id]
        current_index = memories_state.current_image_index.get(memory_id, 0)
        
        if current_index < len(memory["images"]):
            return memory["images"][current_index]
        return None
    
    def get_memory_progress(memory_id):
        """Get viewing progress for a memory (current/total)"""
        if memory_id not in memories_dict:
            return (0, 0)
            
        memory = memories_dict[memory_id]
        current_index = memories_state.current_image_index.get(memory_id, 0)
        total_images = len(memory["images"])
        
        return (current_index + 1, total_images)
    
    ############################################################################
    ## MEMORY ORGANIZATION HELPERS
    ############################################################################
    
    def get_memories_by_act(act_number):
        """Get all memories for a specific ACT"""
        act_memories = []
        
        for memory_id in all_memories:
            # ACT 1: ep01-ep05
            if act_number == 1 and any(ep in memory_id for ep in ["ep01", "ep02", "ep03", "ep04", "ep05"]):
                act_memories.append(memory_id)
            # ACT 2: ep06-ep10 
            elif act_number == 2 and any(ep in memory_id for ep in ["ep06", "ep07", "ep08", "ep09", "ep10"]):
                act_memories.append(memory_id)
            # ACT 3: ep11-ep15
            elif act_number == 3 and any(ep in memory_id for ep in ["ep11", "ep12", "ep13", "ep14", "ep15"]):
                act_memories.append(memory_id)
            # ACT 4: ep16-ep20
            elif act_number == 4 and any(ep in memory_id for ep in ["ep16", "ep17", "ep18", "ep19", "ep20"]):
                act_memories.append(memory_id)
        
        return act_memories
    
    def organize_memories_in_rows(memory_list, columns=3):
        """Organize memories into rows for grid display"""
        rows = []
        current_row = []
        
        for memory_id in memory_list:
            current_row.append(memory_id)
            if len(current_row) == columns:
                rows.append(current_row)
                current_row = []
        
        # Add last row if it has items
        if current_row:
            rows.append(current_row)
        
        return rows
    
    def get_memory_thumbnail(memory_id, unlocked=True):
        """Get appropriate thumbnail based on unlock status"""
        if memory_id not in memories_dict:
            return "gui/thumb_locked.png"
            
        memory = memories_dict[memory_id]
        
        if unlocked:
            return memory["thumbnail_idle"]
        else:
            return memory["thumbnail_locked"]
    
    ############################################################################
    ## NOTIFICATION SYSTEM - FULLY INTEGRATED POSITIONING
    ############################################################################
    
    def show_memory_unlock_notification(memory_id):
        """Show memory unlock notification integrated with existing notification positioning"""
        if memory_id in memories_dict:
            memory = memories_dict[memory_id]
            
            # Create notification in the EXACT same format as existing notifications
            memory_notification = {
                "title": memory["name"].upper(),
                "message": "New memory unlocked!",
                "icon": "memory",
                "type": "memory"  # Special type for styling
            }
            
            # Ensure active_notifications exists (it should from screen_notifications.rpy)
            if 'active_notifications' not in globals():
                globals()['active_notifications'] = []
            
            # Get notification counter if available
            if hasattr(store, 'notification_state') and hasattr(notification_state, 'notification_counter'):
                notification_state.notification_counter += 1
                memory_notification["unique_id"] = notification_state.notification_counter
            else:
                # Fallback unique ID
                memory_notification["unique_id"] = len(active_notifications) + 1
            
            # Add to the EXISTING active_notifications queue
            active_notifications.append(memory_notification)
            
            # Enforce existing notification limits (should match screen_notifications.rpy)
            max_notifications = 2
            if hasattr(store, 'notification_state') and hasattr(notification_state, 'max_notifications'):
                max_notifications = notification_state.max_notifications
            
            while len(active_notifications) > max_notifications:
                active_notifications.pop(0)
            
            # Also add to notification_state if it exists
            if hasattr(store, 'notification_state') and hasattr(notification_state, 'active_notifications'):
                notification_state.active_notifications.append(memory_notification)
                while len(notification_state.active_notifications) > notification_state.max_notifications:
                    notification_state.active_notifications.pop(0)
            
            # Show using the EXISTING notification system (from screen_notifications.rpy)
            layer_name = "notifications"
            if hasattr(store, 'notification_state') and hasattr(notification_state, 'notification_layer'):
                layer_name = notification_state.notification_layer
            
            # Use the existing screen from screen_notifications.rpy
            renpy.show_screen("transition_immune_notifications", _layer=layer_name)
            renpy.restart_interaction()

################################################################################
## MEMORIES GALLERY SCREEN
################################################################################

screen memories_gallery():
    tag menu
    default current_act = 1  # Default to ACT 1
    
    use game_menu(_("Memories"), scroll="viewport"):
        style_prefix "memories"
    
    ## Main menu title image
    if main_menu:
        add "gui/mmtitle_extras_mg.png" ypos 151 xpos 1100 at igm_appear_fg
    else:
        null
    
    ## ACT selection submenu
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
            
            ## ACT 3 Button
            button at igm_appear_fg2:
                text "ACT 3" style "act_button_text"
                selected current_act == 3
                action SetScreenVariable("current_act", 3)
            
            ## ACT 4 Button
            button at igm_appear_fg2:
                text "ACT 4" style "act_button_text"
                selected current_act == 4
                action SetScreenVariable("current_act", 4)
    
    ## Memories grid viewport
    viewport:
        xsize 1260
        ysize 512
        xpos 331
        ypos 270
        scrollbars "vertical"
        mousewheel True
        
        ## Generate memories layout for current ACT
        python:
            # Get memories for the current ACT
            act_memories = get_memories_by_act(current_act)
            
            # Organize memories in rows of 3
            memory_rows = organize_memories_in_rows(act_memories, 3)
        
        vbox:
            spacing 90
            
            ## Display memory rows
            for row in memory_rows:
                hbox:
                    spacing 90
                    
                    ## Display each memory in the row
                    for memory_id in row:
                        $ memory = memories_dict[memory_id]
                        $ unlocked = is_memory_unlocked(memory_id)
                        
                        frame:
                            background "gui/rectangle.png" at igm_appear_fg
                            xsize 345
                            ysize 194
                            
                            ## Memory thumbnail button
                            if unlocked:
                                imagebutton:
                                    idle memory["thumbnail_idle"] at hover_alpha
                                    hover memory["thumbnail_hover"]
                                    action ShowMenu("memory_viewer", memory_id)
                                    focus_mask True
                            else:
                                imagebutton:
                                    idle memory["thumbnail_locked"] at hover_alpha
                                    action NullAction()
                                    focus_mask True
                            
                            ## Memory name text
                            text "[memory['name'].upper()]":
                                xalign 0.5
                                yalign 0.5
                                size 20
                                color "#F7F7F7"
                                outlines [(2, "#16161D", 0, 0)]
                    
                    ## Fill empty spaces in the last row
                    if len(row) < 3:
                        $ empty_spaces = 3 - len(row)
                        for i in range(empty_spaces):
                            null width 345

################################################################################
## MEMORY VIEWER SCREEN
################################################################################

screen memory_viewer(memory_id):
    tag menu
    modal True
    
    ## Validate memory exists and is unlocked
    if memory_id not in memories_dict or not is_memory_unlocked(memory_id):
        ## Return to gallery if invalid
        timer 0.1 action ShowMenu("memories_gallery")
    else:
        ## Get memory data and current image
        $ memory = memories_dict[memory_id]
        $ current_image = get_current_memory_image(memory_id)
        $ current_progress, total_images = get_memory_progress(memory_id)
        
        ## Black background
        add "#000"
        
        ## Current memory image
        if current_image:
            add current_image xalign 0.5 yalign 0.5 fit "contain" at igm_appear_fg2
        
        ## Click area to advance to next image
        button:
            xfill True
            yfill True
            background None
            action Function(advance_memory_image, memory_id)
            style "memory_advance_button"
        
        ## Close button
        imagebutton:
            xalign 0.99
            yalign 0.03
            idle "gui/btn_close_off.png" at hover_alpha, igm_appear_fg
            hover "gui/btn_close_off.png"
            hover_offset (0, -2)
            action [Hide("memory_viewer"), ShowMenu("memories_gallery")]
            style "igm_button"
            focus_mask None
        
        ## Progress indicator
        frame:
            background None
            xalign 0.02
            yalign 0.03
            text "[current_progress]/[total_images]" size 18 color "#F7F7F7" outlines [(2, "#000000", 0, 0)]
        
        ## Instructions
        frame:
            background None
            xalign 0.5
            yalign 0.95
            text _("Click to continue") size 20 color "#F7F7F7" outlines [(2, "#000000", 0, 0)]

################################################################################
## MEMORY SYSTEM STYLES - FOR USE IN EXISTING NOTIFICATION SCREEN
################################################################################

## Memory notification styles - IMPROVED KERNING
## These will be used by the existing transition_immune_notifications screen
style memory_notification_title:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [(1, "#198c5f", 0, 0)]
    color "#27dc95"
    kerning -2  # Better letter spacing like other notifications
    line_spacing 0
    xalign 0.0

style memory_notification_text:
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xmaximum 280
    kerning -1
    yoffset -8
    line_spacing 0

## Memory viewer styles
style memory_advance_button:
    background None
    hover_background None
    focus_mask None

## ACT button styles (shared with other systems)
style act_button_text:
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    outlines [(1, "#198c5f", 0, 0)]

## Memory gallery styles
style memories_title_text:
    kerning 0
    size 30
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    outlines [(1, "#56555a", 0, 0)]

style memories_info_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#a59f96"

################################################################################
## ANIMATION TRANSFORMS
################################################################################

## Hover effect for memory thumbnails
transform hover_alpha:
    alpha 0.8
    on hover:
        linear 0.2 alpha 1.0
    on idle:
        linear 0.2 alpha 0.8

## Notification appearance animation - CONSISTENT WITH NOTIFICATION SYSTEM
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
## INTEGRATION NOTES
################################################################################

## IMPORTANT: This memory system now uses the existing notification queue from screen_notifications.rpy
## 
## Memory notifications will:
## ✅ Use the existing active_notifications array
## ✅ Follow the same positioning logic (no overlapping)
## ✅ Stack properly above/below other notifications 
## ✅ Use the existing notification layer system
## ✅ Have proper spacing and limits
##
## You also need to modify your screen_notifications.rpy file to handle memory notification styling.
## 
## In the transition_immune_notifications screen, find this section:
##
##                     ## Title
##                     text _(notif["title"]).upper() style "notification_title"
##                     
##                     ## Message
##                     text notif["message"] style "notification_text"
##
## And replace it with:
##
##                     ## Title - different styles for memory vs regular notifications
##                     if notif.get("type") == "memory":
##                         text _(notif["title"]).upper() style "memory_notification_title"
##                     else:
##                         text _(notif["title"]).upper() style "notification_title"
##                     
##                     ## Message - different styles for memory vs regular notifications  
##                     if notif.get("type") == "memory":
##                         text notif["message"] style "memory_notification_text"
##                     else:
##                         text notif["message"] style "notification_text"
##
## This ensures memory notifications use the correct styling while maintaining proper positioning.