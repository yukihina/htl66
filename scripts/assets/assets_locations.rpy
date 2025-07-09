## assets_locations.rpy
## Location Assets System - Complete English Version
## 
## This file contains all location-related text images and templates
## for scene transitions and location displays throughout the game.
## 
## Usage:
## To display a location:
## show osaka_location zorder 2 with dissolve
## pause 2
## hide osaka_location with dissolve

################################################################################
## INITIALIZATION
################################################################################

init:
    ############################################################################
    ## TIME TRANSITION TEXTS
    ############################################################################
    
    # Time progression indicators for scene transitions
    image minutes = Text("Minutes later...", style="minutes")
    image hours = Text("Hours later...", style="minutes")
    image week = Text("1 Week later...", style="minutes")
    image days = Text("Some days later...", style="minutes")
    
    ############################################################################
    ## OSAKA LOCATIONS
    ############################################################################
    
    # Osaka area location text displays
    image osaka_location = Text("Shin-Imamiya, Osaka", style="location")
    image tobita_location = Text("Tobita Sinchi, Osaka", style="location")
    image doton_location = Text("Dōtonbori, Osaka", style="location")
    image kama_location = Text("Kamagasaki, Osaka", style="location")
    image taniwa_location = Text("Taniwa Beach, Osaka", style="location")
    
    ############################################################################
    ## TOKYO LOCATIONS
    ############################################################################
    
    # Tokyo area location text displays
    image asakusa_location = Text("Asakusa area, Taito ward, Tokyo", style="location")
    image nana_location = Text("Kita-senju, Adachi Ward, Tokyo", style="location")
    image home_location = Text("Den-en-chōfu, Ōta ward, Tokyo", style="location")
    image outside_home_for_work = Text("Futako-Tamagawa area, Ōta ward, Tokyo", style="location")
    image work_location = Text("Kasumigaseki area, Chiyoda ward, Tokyo", style="location")
    image shibuya_location = Text("Shibuya Crossing, Shibuya City, Tokyo", style="location")
    image hospital_location = Text("Minami-Azabu area, Minato ward, Tokyo", style="location")
    image murderroom_location = Text("Ōi Futo area, Shinagawa ward, Tokyo", style="location")
    
    ############################################################################
    ## LOCATION BACKGROUND IMAGES (COMMENTED OUT)
    ############################################################################
    
    # Uncomment and modify these as needed for your scenes
    # These are placeholders for actual location background images
    
    # Michael's house - Front door at night
    # image ep06_mcnightie01 = "scene6_location"
    
    # Tokyo Police Department - Front door during day
    # image ep06_mornwork08 = "ep6_s3_p2_sub03_a03"
    
    # Tokyo outside MC house - Aerial view in morning
    # image ep06_mornwork04 = "ep6_s3_p2_sub01"
    
    # Kanae's house - Front view during day
    # image ep05_02_nanahouse01 = "ep5_panel04_01_1"
    
    # Shibuya - Aerial view during day
    # image ep06_shibuya = "shibuya"

################################################################################
## LOCATION DISPLAY TEMPLATES
################################################################################

## Standard template for displaying location text
## Copy this template and modify the location name as needed:
##
## show [location_name]_location zorder 2 with dissolve
## pause 2
## hide [location_name]_location with dissolve
##
## Example usage:
## show osaka_location zorder 2 with dissolve
## pause 2
## hide osaka_location with dissolve

################################################################################
## INTEGRATION INSTRUCTIONS
################################################################################

## How to use location assets in your scenes:
##
## 1. For time transitions:
##    show minutes with dissolve
##    pause 1.5
##    hide minutes with dissolve
##
## 2. For location displays:
##    show tokyo_location zorder 2 with dissolve
##    pause 2
##    hide tokyo_location with dissolve
##
## 3. To add new locations:
##    - Add a new image definition in the appropriate section
##    - Use the Text() function with the "location" style
##    - Follow the naming convention: [area_name]_location
##
## 4. Location text styling:
##    - Time transitions use "minutes" style
##    - Locations use "location" style
##    - Define these styles in your gui.rpy or screens.rpy
##
## 5. Best practices:
##    - Always use zorder 2 for location text to ensure visibility
##    - Use appropriate transitions (dissolve recommended)
##    - Keep pause duration between 1.5-3 seconds for readability
##    - Group related locations (Osaka, Tokyo, etc.) for organization