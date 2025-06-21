## screen_memories.rpy
## Memories gallery system - Add new memories here

## Memory Data Configuration
## To add new memories, modify these lists and dictionaries

default persistent.unlocked_memories = {}

## List of all memory IDs - ADD NEW MEMORIES HERE
define all_memories = [
    "m_ep01_library",
    "m_ep01_clothes",
    "m_ep01_home",
    "m_ep01_laundry",
    "m_ep01_confession",
    # Add new memory IDs here
]

## Memory definitions - ADD NEW MEMORY DATA HERE
define memories_dict = {
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

## Memory System Functions
init python:
    ## Dictionary to store current image index for each memory
    _memory_current_index = {}
    
    ## Function to advance memory image
    def advance_memory_image(memory_id):
        memory = memories_dict[memory_id]
        current_index = _memory_current_index.get(memory_id, 0)
        
        ## Advance to next image
        current_index += 1
        
        ## If we've reached the end, return to memories gallery
        if current_index >= len(memory["images"]):
            _memory_current_index[memory_id] = 0
            renpy.hide_screen("memory_viewer")
            renpy.show_screen("memories_gallery")
        else:
            _memory_current_index[memory_id] = current_index
            renpy.restart_interaction()
    
    ## Function to unlock a memory
    def unlock_memory(memory_id):
        if not hasattr(persistent, 'unlocked_memories'):
            persistent.unlocked_memories = {}
        persistent.unlocked_memories[memory_id] = True
        # Optional: Show notification
        renpy.show_screen("memory_unlock_notification", memory_id=memory_id)

## Memories Gallery Screen
screen memories_gallery():
    tag menu
    default current_act = 1  # Default, show ACT 1
    
    use game_menu(_("Memories"), scroll="viewport"):
        style_prefix "memories"
    
    if main_menu:
        add "gui/mmtitle_extras_mg.png" ypos 151 xpos 1100 at igm_appear_fg
    else:
        null
    
    ## Back to Extras button
    # imagebutton at igm_appear:
    #     xpos 332
    #     ypos 824
    #     idle "gui/back_to_extras_off.png"
    #     hover "gui/back_to_extras_on.png"
    #     action ShowMenu("extras")
    #     style "igm_button"
    #     focus_mask None
    
    ## ACT Submenu
    frame:
        xsize 1260
        ysize 50
        xpos 714
        ypos 791
        
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            # ACT 1 Button (active by default)
            button at igm_appear_fg2:
                text "ACT 1" style "act_button_text"
                selected current_act == 1
                action SetScreenVariable("current_act", 1)
                
            # ACT 2 Button
            button at igm_appear_fg2:
                text "ACT 2" style "act_button_text"
                selected current_act == 2
                action SetScreenVariable("current_act", 2)
            
            # ACT 3 Button
            button at igm_appear_fg2:
                text "ACT 3" style "act_button_text"
                selected current_act == 3
                action SetScreenVariable("current_act", 3)
                
            # ACT 4 Button
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
        
        python:
            # Filter memories for the current ACT
            act_memories = []
            for memory_id in all_memories:
                # ACT 1: ep01-ep05
                if current_act == 1 and any(ep in memory_id for ep in ["ep01", "ep02", "ep03", "ep04", "ep05"]):
                    act_memories.append(memory_id)
                # ACT 2: ep06-ep10
                elif current_act == 2 and any(ep in memory_id for ep in ["ep06", "ep07", "ep08", "ep09", "ep10"]):
                    act_memories.append(memory_id)
                # ACT 3: ep11-ep15
                elif current_act == 3 and any(ep in memory_id for ep in ["ep11", "ep12", "ep13", "ep14", "ep15"]):
                    act_memories.append(memory_id)
                # ACT 4: ep16-ep20
                elif current_act == 4 and any(ep in memory_id for ep in ["ep16", "ep17", "ep18", "ep19", "ep20"]):
                    act_memories.append(memory_id)
            
            # Organize memories in rows of 3
            rows = []
            current_row = []
            
            for memory_id in act_memories:
                current_row.append(memory_id)
                if len(current_row) == 3:
                    rows.append(current_row)
                    current_row = []
            
            # Add last row if it has items
            if current_row:
                rows.append(current_row)
        
        vbox:
            spacing 90
            
            for row in rows:
                hbox:
                    spacing 90
                    
                    for memory_id in row:
                        $ memory = memories_dict[memory_id]
                        $ unlocked = persistent.unlocked_memories.get(memory_id, False)
                        
                        frame:
                            background "gui/rectangle.png" at igm_appear_fg
                            xsize 345
                            ysize 194
                            
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
                            
                            text "[memory['name'].upper()]":
                                xalign 0.5
                                yalign 0.5
                                size 20
                                color "#F7F7F7"
                                outlines [(2, "#16161D", 0, 0)]
                    
                    # Fill empty spaces in the last row
                    if len(row) < 3:
                        $ empty_spaces = 3 - len(row)
                        for i in range(empty_spaces):
                            null width 345

## Memory Viewer Screen
screen memory_viewer(memory_id):
    tag menu
    modal True
    
    $ memory = memories_dict[memory_id]
    $ current_image_index = _memory_current_index.get(memory_id, 0)
    $ current_image = memory["images"][current_image_index]
    
    ## Background
    add "#000"
    
    ## Current memory image
    add current_image xalign 0.5 yalign 0.5 fit "contain" at igm_appear_fg2
    
    ## Click area to advance
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
    
    ## Instructions
    frame:
        background None
        xalign 0.5
        yalign 0.95
        text _("Click to continue") size 20 color "#F7F7F7" outlines [(2, "#000000", 0, 0)]

## Memory unlock notification
screen memory_unlock_notification(memory_id):
    zorder 100
    
    $ memory = memories_dict[memory_id]
    
    frame:
        at notification_appear
        add "gui/message_bg.png" xpos 1380 ypos 625
        add "gui/icon_memory.png" xpos 1408 ypos 654
        
        vbox:
            xpos 1561 ypos 646
            spacing 3
            text "[memory['name'].upper()]" style "memory_notification_title"
            text _("New memory unlocked!") style "memory_notification_text"
    
    timer 5.0 action Hide("memory_unlock_notification")

## Memory-specific styles
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

style memory_advance_button:
    background None
    hover_background None
    focus_mask None

## ACT button styles (reused from achievements)
style act_button_text:
    size 24
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#27dc95"
    hover_color "#FFFFFF"
    selected_color "#FFFFFF" 
    outlines [(1, "#198c5f", 0, 0)]