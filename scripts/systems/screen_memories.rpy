## screen_memories.rpy
## Memories Gallery System - Complete English Version
## 
## How to use:
## To open the memories gallery from anywhere in your game:
## textbutton "Memories" action ShowMenu("memories_gallery")
## 
## The memories system provides:
## 1. Organized memory collections by episodes/acts
## 2. Progressive unlock system based on game progress
## 3. Image viewing with sequential navigation
## 4. Automatic state persistence across sessions
## 5. ACT-based organization for easy navigation
##
## Memory Management:
## Memories are automatically unlocked through game progression
## Players can view unlocked memories in sequential order
## Each memory contains multiple images that advance on click
## State is preserved between sessions using persistent data

################################################################################
## INITIALIZATION
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
    
    # Ensure persistent variables exist
    if not hasattr(persistent, 'unlocked_memories'):
        persistent.unlocked_memories = {}
    
    ############################################################################
    ## MEMORY DATA CONFIGURATION
    ############################################################################
    
    # List of all memory IDs organized by release order
    all_memories = [
        "m_ep01_library",
        "m_ep01_clothes", 
        "m_ep01_home",
        "m_ep01_laundry",
        "m_ep01_confession",
        # Add new memory IDs here following the same pattern
    ]
    
    # Memory definitions with metadata and image sequences
    memories_dict = {
        "m_ep01_library": {
            "name": "Meeting Antonella at library",
            "thumbnail_idle": "memories/m_ep01_library_thumb_idle.png",
            "thumbnail_hover": "memories/m_ep01_library_thumb_hover.png", 
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
            "name": "Goth woman in the store",
            "thumbnail_idle": "memories/m_ep01_clothes_thumb_idle.png",
            "thumbnail_hover": "memories/m_ep01_clothes_thumb_hover.png",
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
            "name": "Amber at home",
            "thumbnail_idle": "memories/m_ep01_home_thumb_idle.png",
            "thumbnail_hover": "memories/m_ep01_home_thumb_hover.png",
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
            "name": "Amber at the laundry",
            "thumbnail_idle": "memories/m_ep01_laundry_thumb_idle.png", 
            "thumbnail_hover": "memories/m_ep01_laundry_thumb_hover.png",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_amberfail02",
                "ep01_amberfail03",
                "ep01_amberfail04",
                "ep01_amberfail05"
            ]
        },
        "m_ep01_confession": {
            "name": "Amber's confession",
            "thumbnail_idle": "memories/m_ep01_confession_thumb_idle.png",
            "thumbnail_hover": "memories/m_ep01_confession_thumb_hover.png",
            "thumbnail_locked": "gui/thumb_locked.png",
            "images": [
                "ep01_amberconfess02",
                "ep01_amberconfess09", 
                "ep01_amberconfess10"
            ]
        }
        # Add new memory dictionaries here following the same pattern
    }
    
    ############################################################################
    ## MEMORY MANAGEMENT FUNCTIONS
    ############################################################################
    
    def unlock_memory(memory_id):
        """Unlock a specific memory and show notification"""
        if not hasattr(persistent, 'unlocked_memories'):
            persistent.unlocked_memories = {}
        
        # Only unlock if not already unlocked to avoid spam
        if not persistent.unlocked_memories.get(memory_id, False):
            persistent.unlocked_memories[memory_id] = True
            # Show unlock notification
            show_memory_unlock_notification(memory_id)
    
    def is_memory_unlocked(memory_id):
        """Check if a specific memory is unlocked"""
        if not hasattr(persistent, 'unlocked_memories'):
            persistent.unlocked_memories = {}
        return persistent.unlocked_memories.get(memory_id, False)
    
    def get_unlocked_memories_count():
        """Get total count of unlocked memories"""
        if not hasattr(persistent, 'unlocked_memories'):
            return 0
        return sum(1 for unlocked in persistent.unlocked_memories.values() if unlocked)
    
    def reset_all_memories():
        """Reset all memory unlock status (debug function)"""
        if hasattr(persistent, 'unlocked_memories'):
            persistent.unlocked_memories = {}
        memories_state.current_image_index = {}
    
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
    ## NOTIFICATION SYSTEM
    ############################################################################
    
    def show_memory_unlock_notification(memory_id):
        """Show memory unlock notification"""
        if memory_id in memories_dict:
            renpy.show_screen("memory_unlock_notification", memory_id=memory_id)

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
## MEMORY UNLOCK NOTIFICATION SCREEN
################################################################################

screen memory_unlock_notification(memory_id):
    zorder 100
    
    ## Get memory data for notification
    $ memory = memories_dict.get(memory_id, {"name": "Unknown Memory"})
    
    frame:
        at notification_appear
        add "gui/message_bg.png" xpos 1380 ypos 625
        add "gui/icon_memory.png" xpos 1408 ypos 654
        
        vbox:
            xpos 1561 ypos 646
            spacing 3
            text "[memory['name'].upper()]" style "memory_notification_title"
            text _("New memory unlocked!") style "memory_notification_text"
    
    ## Auto-hide notification after duration
    timer memories_state.notification_duration action Hide("memory_unlock_notification")

################################################################################
## MEMORY SYSTEM STYLES
################################################################################

## Memory notification styles
style memory_notification_title:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [(1, "#198c5f", 0, 0)]
    color "#27dc95"

style memory_notification_text:
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xmaximum 280
    kerning -1
    yoffset -8

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

## Notification appearance animation
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
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this memories system in your game:
##
## 1. BASIC MEMORY UNLOCKING:
##    $ unlock_memory("m_ep01_library")
##    - Unlocks a specific memory and shows notification
##    - Only unlocks if not already unlocked to avoid spam
##
## 2. OPENING THE MEMORIES GALLERY:
##    textbutton "Memories" action ShowMenu("memories_gallery")
##    - Opens the memories gallery with ACT navigation
##    - Players can browse unlocked memories by episodes/acts
##
## 3. ADDING NEW MEMORIES:
##    a) Add memory ID to all_memories list:
##       "m_ep02_new_memory"
##    
##    b) Add memory definition to memories_dict:
##       "m_ep02_new_memory": {
##           "name": "Memory Name",
##           "thumbnail_idle": "memories/new_memory_thumb_idle.png",
##           "thumbnail_hover": "memories/new_memory_thumb_hover.png", 
##           "thumbnail_locked": "gui/thumb_locked.png",
##           "images": ["image1", "image2", "image3"]
##       }
##
## 4. CHECKING MEMORY STATUS:
##    $ is_unlocked = is_memory_unlocked("m_ep01_library")
##    $ total_unlocked = get_unlocked_memories_count()
##    - Check unlock status and get statistics
##
## 5. MEMORY VIEWING FEATURES:
##    - Sequential image viewing with click-to-advance
##    - Progress indicator showing current/total images
##    - Automatic return to gallery when sequence ends
##    - Persistent state across game sessions
##
## 6. Required assets:
##    - Memory thumbnails: memories/[memory_id]_thumb_idle.png, _thumb_hover.png
##    - Locked thumbnail: gui/thumb_locked.png
##    - UI elements: gui/message_bg.png, gui/icon_memory.png, gui/rectangle.png
##    - Memory images: Referenced in memories_dict["images"] arrays
##    - Navigation assets: gui/btn_close_off.png, gui/mmtitle_extras_mg.png
##
## 7. Memory organization:
##    - Memories are organized by ACT (episodes 1-5, 6-10, 11-15, 16-20)
##    - Grid layout with 3 memories per row
##    - Locked memories show placeholder thumbnail
##    - Unlocked memories show hover effects and are clickable
##
## USAGE EXAMPLES:
##
## Example 1 - Unlock memory during story:
## label important_scene:
##     "This moment will be remembered forever."
##     $ unlock_memory("m_ep01_confession")
##     # Continue with story...
##
## Example 2 - Conditional memory unlocking:
## label scene_end:
##     if amber_route_active:
##         $ unlock_memory("m_ep01_amber_scene")
##     elif elizabeth_route_active:
##         $ unlock_memory("m_ep01_elizabeth_scene")
##
## Example 3 - Check progress for achievements:
## label check_completion:
##     $ unlocked_count = get_unlocked_memories_count()
##     if unlocked_count >= 10:
##         "Achievement unlocked: Memory Collector!"
##
## Example 4 - Integration in extras menu:
## screen extras():
##     textbutton "Memories" action ShowMenu("memories_gallery")
##     textbutton "Music Player" action ShowMenu("music_player")
##
## TROUBLESHOOTING:
## - If memories don't unlock: Check that memory ID exists in memories_dict
## - If thumbnails don't show: Verify image paths are correct
## - If navigation fails: Ensure ACT organization logic matches your episodes
## - If notifications don't appear: Check icon_memory.png exists
## - If images don't display: Verify all image names in memories_dict are valid
##
## CUSTOMIZATION:
## - Modify get_memories_by_act() to change episode organization
## - Adjust notification_duration in MemoriesState for different timing
## - Change grid layout by modifying organize_memories_in_rows() columns parameter
## - Add new ACTs by extending the ACT button logic and organization function
## - Customize thumbnails and locked states through memories_dict definitions
##
## ADVANCED FEATURES:
## - Progress tracking with current/total image indicators
## - Persistent unlock state across game sessions
## - Notification system for new unlocks
## - ACT-based organization for easy navigation
## - Click-to-advance viewing with automatic progression
## - Hover effects and visual feedback
## - Modal viewing with proper screen management