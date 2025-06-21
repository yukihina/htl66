## screen_replay.rpy
## Replay gallery system - Add replay scenes here when ready

## Replay Data Configuration
## To add replays, modify these lists and dictionaries

default persistent.unlocked_replays = {}

## List of all replay IDs - ADD NEW REPLAYS HERE
define all_replays = [
    # Example format:
    # "replay_beach_scene",
    # "replay_confession_scene",
    # "replay_date_scene",
]

## Replay definitions - ADD NEW REPLAY DATA HERE
define replays_dict = {
    # Example format:
    # "replay_beach_scene": {
    #     "name": "Beach Scene",
    #     "thumbnail": "images/replays/beach_thumb.png",
    #     "thumbnail_locked": "images/replays/thumb_locked.png",
    #     "label": "beach_scene_replay",  # The label to jump to
    #     "description": "A romantic day at the beach"
    # },
}

## Replay System Functions
init python:
    ## Function to unlock a replay
    def unlock_replay(replay_id):
        if not hasattr(persistent, 'unlocked_replays'):
            persistent.unlocked_replays = {}
        persistent.unlocked_replays[replay_id] = True
        # Optional: Show notification
        renpy.show_screen("replay_unlock_notification", replay_id=replay_id)
    
    ## Function to start a replay
    def start_replay(replay_label):
        # Store current game state
        renpy.call_in_new_context(replay_label)

## Replay Gallery Screen - Currently under construction
screen replay_gallery():
    tag menu
    
    use game_menu(_("Replay Gallery"), scroll="viewport"):
        style_prefix "replay"
    
    if main_menu:
        add "gui/mmtitle_extras_rg.png" ypos 151 xpos 1180 at igm_appear_fg
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
    
    ## Under construction message
    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5
        
        #add "gui/under_construction.png" xalign 0.5 at igm_appear_fg
        text "REPLAY GALLERY - UNDER CONSTRUCTION" size 30 style "replay_wip_text" at igm_appear_fg xalign 0.5
        text "This feature will be available in a future update" size 20 style "replay_info_text" at igm_appear_fg xalign 0.5
    
    ## Placeholder for future replay grid
    ## When ready, uncomment and modify this section:
    # """
    # viewport:
    #     xsize 1260
    #     ysize 512
    #     xpos 331
    #     ypos 270
    #     scrollbars "vertical"
    #     mousewheel True
        
    #     python:
    #         # Organize replays in rows of 3
    #         rows = []
    #         current_row = []
            
    #         for replay_id in all_replays:
    #             current_row.append(replay_id)
    #             if len(current_row) == 3:
    #                 rows.append(current_row)
    #                 current_row = []
            
    #         if current_row:
    #             rows.append(current_row)
        
    #     vbox:
    #         spacing 90
            
    #         for row in rows:
    #             hbox:
    #                 spacing 90
                    
    #                 for replay_id in row:
    #                     $ replay = replays_dict[replay_id]
    #                     $ unlocked = persistent.unlocked_replays.get(replay_id, False)
                        
    #                     frame:
    #                         background "gui/rectangle.png" at igm_appear_fg
    #                         xsize 345
    #                         ysize 194
                            
    #                         vbox:
    #                             spacing 5
                                
    #                             if unlocked:
    #                                 imagebutton:
    #                                     idle replay["thumbnail"] at hover_alpha
    #                                     hover replay["thumbnail"]
    #                                     action Function(start_replay, replay["label"])
    #                                     focus_mask True
    #                             else:
    #                                 add replay["thumbnail_locked"] at hover_alpha
                                
    #                             text "[replay['name']]" xalign 0.5 style "replay_name_text"
    #                             if unlocked:
    #                                 text "[replay['description']]" xalign 0.5 style "replay_desc_text"
    #                             else:
    #                                 text "???" xalign 0.5 style "replay_desc_text"
                    
    #                 # Fill empty spaces
    #                 if len(row) < 3:
    #                     $ empty_spaces = 3 - len(row)
    #                     for i in range(empty_spaces):
    #                         null width 345
    # """

## Replay unlock notification
screen replay_unlock_notification(replay_id):
    zorder 100
    
    $ replay = replays_dict.get(replay_id, {"name": "Unknown Replay"})
    
    frame:
        at notification_appear
        add "gui/message_bg.png" xpos 1380 ypos 625
        add "gui/icon_replay.png" xpos 1408 ypos 654
        
        vbox:
            xpos 1561 ypos 646
            spacing 3
            text "[replay['name'].upper()]" style "replay_notification_title"
            text _("New replay unlocked!") style "replay_notification_text"
    
    timer 5.0 action Hide("replay_unlock_notification")

## Example replay labels - ADD YOUR REPLAY SCENES HERE
## These would go in your script files, not here
# """
# label beach_scene_replay:
#     # Set up the scene for replay
#     scene beach_background
#     show character happy
    
#     "This is the beach scene replay."
    
#     # Your scene content here
    
#     # End replay and return to gallery
#     $ renpy.end_replay()
#     return

# label confession_scene_replay:
#     # Set up the scene
#     scene school_rooftop
#     show character blush
    
#     "This is the confession scene replay."
    
#     # Your scene content here
    
#     $ renpy.end_replay()
#     return
# """

## Replay-specific styles
style replay_wip_text:
    kerning 0
    size 30
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    outlines [(1, "#56555a", 0, 0)]

style replay_info_text:
    kerning 0
    size 20
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#a59f96"

style replay_name_text:
    kerning 0
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#F7F7F7"
    outlines [(2, "#16161D", 0, 0)]

style replay_desc_text:
    kerning 0
    size 14
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#a59f96"
    xmaximum 335

style replay_notification_title:
    size 26
    font "fonts/UbuntuTitling-Bold.ttf"
    outlines [(1, "#198c5f", 0, 0)]
    color "#27dc95"

style replay_notification_text:
    size 18
    font "fonts/UbuntuTitling-Bold.ttf"
    color "#34323d"
    xmaximum 280
    kerning -1
    yoffset -8