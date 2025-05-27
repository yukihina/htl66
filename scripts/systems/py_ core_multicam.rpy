# Documentation for the Ren'Py Multi-Camera View System
# -----------------------------------------------------

# Purpose:
# This script implements a multi-camera view system, allowing players to switch
# between different perspectives or angles of the same scene.

# Main Components:
# 1. Global Variables:
#    - CurrentImages: List of available images for the current scene.
#    - ActiveImage: Currently displayed image.

# 2. Functions:
#    - ChangeView(image_name): Switches to a specified view.
#    - AddView(*images): Adds new views to the current scene.

# 3. camera_view Screen:
#    - Displays camera selection buttons when multiple views are available.

# Detailed Usage:
# 1. Setting Up a Multi-View Scene:
#    $ AddView("view1.jpg", "view2.jpg", "view3.jpg")
#    show screen camera_view

# 2. Changing Views in Script:
#    $ ChangeView("view2.jpg")

# 3. Player Interaction:
#    Players can click on the camera buttons to switch views.

# Connections to Other Files:
# - This system can be used in any script file where multiple scene perspectives are desired.
# - It interacts with the game's image assets, which should be defined in your images.rpy or equivalent.

# Maintenance and Expansion:
# - When adding new multi-view scenes, ensure all perspective images are properly defined.
# - Consider expanding the system to handle transitions between views or to support more than just images (e.g., animations).

# Note for Novices:
# - The '*' in AddView(*images) allows for any number of images to be added.
# - The camera_view screen is automatically hidden when there's only one view available.

# Remember: While multiple views can enhance player engagement, overuse might disrupt 
# the narrative flow. Use this feature judiciously to highlight important scenes or provide 
# additional context when necessary.

init python:
    # Global variables
    global CurrentImages
    global ActiveImage
    CurrentImages = []
    ActiveImage = None

    # Function to change the scene
    def ChangeView(image_name):
        global ActiveImage
        if image_name in CurrentImages and ActiveImage != image_name:
            renpy.hide(ActiveImage)
            renpy.show(image_name)
            renpy.transition(Dissolve(0.5))  
            ActiveImage = image_name

    # Function to add images to the scene
    def AddView(*images):
        global CurrentImages, ActiveImage
        # Clear the CurrentImages list and reset ActiveImage
        CurrentImages = []
        ActiveImage = None
        CurrentImages.extend(images)
        if not ActiveImage:
            ActiveImage = images[0]
            renpy.show(ActiveImage)
            renpy.transition(Dissolve(0.5)) 

screen camera_view():
    if len(CurrentImages) > 1:
        frame at igm_appear_bg:
            xpos 358
            ypos 777
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

# Example usage
# label start:
#     # Add views
#     $ AddView("view1.jpg", "view2.jpg", "view3.jpg")

#     # Show the camera buttons
#     show screen camera_view

#     # Game dialogues and logic
#     "You can change the camera view by clicking on the circular buttons at the top right."
#     ...

