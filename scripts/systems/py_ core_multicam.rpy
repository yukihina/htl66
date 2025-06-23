## py_core_multicam.rpy
## Multi-Camera View System for Ren'Py - Complete English Version
## 
## How to use:
## This script implements a multi-camera view system, allowing players to switch
## between different perspectives or angles of the same scene.
## 
## To set up a multi-view scene:
## $ AddView("view1.jpg", "view2.jpg", "view3.jpg")
## show screen camera_view
## 
## The system automatically:
## - Creates camera selection buttons when multiple views are available
## - Handles smooth transitions between different perspectives
## - Manages active view state and UI visibility
## - Provides interactive camera switching with visual feedback
##
## Multi-Camera Features:
## - Support for unlimited camera angles per scene
## - Smooth dissolve transitions between views
## - Visual button states (idle, hover, selected)
## - Automatic UI management (shows/hides based on view count)
## - Memory efficient view switching
##
## Scene Management:
## - AddView() function to register available camera angles
## - ChangeView() function for programmatic view switching
## - Automatic cleanup and state management
## - Support for dynamic view addition during scenes

################################################################################
## INITIALIZATION
################################################################################

init python:
    ############################################################################
    ## GLOBAL CAMERA SYSTEM VARIABLES
    ############################################################################
    
    # Global variables for camera system state
    global CurrentImages
    global ActiveImage
    CurrentImages = []
    ActiveImage = None
    
    ############################################################################
    ## CAMERA VIEW MANAGEMENT FUNCTIONS
    ############################################################################
    
    def ChangeView(image_name):
        """
        Switch to a specified camera view with smooth transition
        
        Args:
            image_name (str): Name of the image/view to switch to
        """
        global ActiveImage
        
        # Only change if the image exists in current views and isn't already active
        if image_name in CurrentImages and ActiveImage != image_name:
            # Hide the current active image
            if ActiveImage:
                renpy.hide(ActiveImage)
            
            # Show the new image
            renpy.show(image_name)
            renpy.transition(Dissolve(0.5))
            
            # Update active state
            ActiveImage = image_name
    
    def AddView(*images):
        """
        Add new camera views to the current scene
        
        Args:
            *images: Variable number of image names to add as camera views
        """
        global CurrentImages, ActiveImage
        
        # Clear previous views and reset state
        CurrentImages = []
        ActiveImage = None
        
        # Add all provided images to the current views list
        CurrentImages.extend(images)
        
        # Auto-activate the first view if no active view is set
        if not ActiveImage and images:
            ActiveImage = images[0]
            renpy.show(ActiveImage)
            renpy.transition(Dissolve(0.5))
    
    ############################################################################
    ## CAMERA SYSTEM HELPER FUNCTIONS
    ############################################################################
    
    def GetCurrentViewCount():
        """Get the number of available camera views"""
        return len(CurrentImages)
    
    def GetActiveView():
        """Get the currently active camera view"""
        return ActiveImage
    
    def HasMultipleViews():
        """Check if multiple camera views are available"""
        return len(CurrentImages) > 1
    
    def ClearAllViews():
        """Clear all camera views and reset the system"""
        global CurrentImages, ActiveImage
        
        if ActiveImage:
            renpy.hide(ActiveImage)
        
        CurrentImages = []
        ActiveImage = None
    
    def IsValidView(image_name):
        """Check if an image name is a valid camera view"""
        return image_name in CurrentImages
    
    def GetViewIndex(image_name):
        """Get the index of a specific view in the current views list"""
        try:
            return CurrentImages.index(image_name)
        except ValueError:
            return -1
    
    def GetNextView():
        """Get the next camera view in sequence"""
        if not CurrentImages or not ActiveImage:
            return None
        
        current_index = GetViewIndex(ActiveImage)
        if current_index == -1:
            return None
        
        next_index = (current_index + 1) % len(CurrentImages)
        return CurrentImages[next_index]
    
    def GetPreviousView():
        """Get the previous camera view in sequence"""
        if not CurrentImages or not ActiveImage:
            return None
        
        current_index = GetViewIndex(ActiveImage)
        if current_index == -1:
            return None
        
        prev_index = (current_index - 1) % len(CurrentImages)
        return CurrentImages[prev_index]
    
    ############################################################################
    ## PROGRAMMATIC VIEW SWITCHING
    ############################################################################
    
    def SwitchToNextView():
        """Switch to the next camera view in sequence"""
        next_view = GetNextView()
        if next_view:
            ChangeView(next_view)
    
    def SwitchToPreviousView():
        """Switch to the previous camera view in sequence"""
        prev_view = GetPreviousView()
        if prev_view:
            ChangeView(prev_view)
    
    def SwitchToViewByIndex(index):
        """Switch to a camera view by its index"""
        if 0 <= index < len(CurrentImages):
            ChangeView(CurrentImages[index])

################################################################################
## CAMERA VIEW SCREEN
################################################################################

## Camera selection interface - only shown when multiple views are available
screen camera_view():
    # Only display camera buttons when multiple views are available
    if HasMultipleViews():
        frame at igm_appear_bg:
            xpos 358
            ypos 777
            padding (6, 6)
            
            has hbox:
                spacing 5
            
            # Create a button for each available camera view
            for img in CurrentImages:
                imagebutton:
                    idle "gui/button/cam_off.png"
                    hover "gui/button/cam_hover.png"
                    selected_idle "gui/button/cam_active.png"
                    selected_hover "gui/button/cam_active_hover.png"
                    selected (ActiveImage == img)
                    action Function(ChangeView, img)
                    xsize 22
                    ysize 22

## Advanced camera view screen with additional controls (optional)
screen camera_view_advanced():
    if HasMultipleViews():
        vbox:
            xalign 1.0
            yalign 0.0
            xoffset -20
            yoffset 20
            spacing 10
            
            ## Main camera selection
            frame:
                padding (6, 6)
                has hbox:
                    spacing 5
                
                for img in CurrentImages:
                    imagebutton:
                        idle "gui/button/cam_off.png"
                        hover "gui/button/cam_hover.png"
                        selected_idle "gui/button/cam_active.png"
                        selected_hover "gui/button/cam_active_hover.png"
                        selected (ActiveImage == img)
                        action Function(ChangeView, img)
                        xsize 22
                        ysize 22
            
            ## Navigation controls
            hbox:
                spacing 5
                
                # Previous view button
                imagebutton:
                    idle "gui/button/prev_off.png"
                    hover "gui/button/prev_on.png"
                    action Function(SwitchToPreviousView)
                    xsize 20
                    ysize 20
                
                # Next view button
                imagebutton:
                    idle "gui/button/next_off.png"
                    hover "gui/button/next_on.png"
                    action Function(SwitchToNextView)
                    xsize 20
                    ysize 20

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to integrate this multi-camera system in your game:
## 
## 1. Setting up a multi-view scene:
##    $ AddView("bedroom_angle1", "bedroom_angle2", "bedroom_angle3")
##    show screen camera_view
##
## 2. The system will automatically:
##    - Show camera selection buttons when multiple views are available
##    - Handle smooth transitions between different perspectives
##    - Manage active view state and button selection states
##    - Hide camera UI when only one view is available
##
## 3. Changing views programmatically:
##    $ ChangeView("bedroom_angle2")
##    $ SwitchToNextView()
##    $ SwitchToPreviousView()
##
## 4. Advanced usage with navigation:
##    show screen camera_view_advanced
##    # Provides next/previous buttons in addition to direct selection
##
## 5. Required assets:
##    - Camera button images (cam_off.png, cam_hover.png, etc.)
##    - Optional navigation button images (prev_off.png, next_on.png, etc.)
##    - All camera view images referenced in AddView()
##
## 6. Helper functions for advanced control:
##    $ current_count = GetCurrentViewCount()
##    $ active_view = GetActiveView()
##    $ has_multiple = HasMultipleViews()
##
## Example scene implementation:
## label bedroom_scene:
##     scene bedroom_default
##     
##     # Set up multiple camera angles
##     $ AddView("bedroom_wide", "bedroom_close", "bedroom_side")
##     show screen camera_view
##     
##     "You can change the camera view by clicking the buttons."
##     
##     # Story continues with multiple viewing angles available
##     "The room looks different from each angle."
##     
##     # Hide camera interface when scene ends
##     hide screen camera_view
##     $ ClearAllViews()
##
## Asset organization:
## gui/button/
##   ├── cam_off.png (idle state)
##   ├── cam_hover.png (hover state)
##   ├── cam_active.png (selected idle)
##   ├── cam_active_hover.png (selected hover)
##   ├── prev_off.png (navigation - optional)
##   ├── prev_on.png (navigation - optional)
##   ├── next_off.png (navigation - optional)
##   └── next_on.png (navigation - optional)
##
## images/scenes/
##   ├── bedroom_wide.jpg
##   ├── bedroom_close.jpg
##   └── bedroom_side.jpg
##
## Performance considerations:
## - Views are only loaded when displayed (memory efficient)
## - Transitions use optimized dissolve effects
## - Camera UI automatically manages visibility
## - State management prevents unnecessary operations
##
## Best practices:
## - Limit to 2-5 camera angles per scene to avoid UI clutter
## - Use consistent naming conventions for related views
## - Clear views when transitioning between different scenes
## - Test camera switching in various game contexts
## - Ensure all referenced images exist before using AddView()
##
## Troubleshooting:
## - If buttons don't appear: Check that AddView() was called with multiple images
## - If transitions are choppy: Ensure images are properly optimized
## - If views don't switch: Verify image names match exactly with AddView() parameters
## - If state persists: Use ClearAllViews() when changing scenes