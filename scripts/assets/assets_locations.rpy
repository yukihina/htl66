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
    image days_before = Text("Some days earlier...", style="minutes")
    
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
    image home_location = Text("Den-en-chōfu residential area, Ōta, Tokyo", style="location")
    image outside_home_for_work = Text("Futako-Tamagawa area, Ōta ward, Tokyo", style="location")
    image tmpd_location = Text("Tokyo Metropolitan Police Department\nKasumigaseki, Tokyo", style="location")
    image shibuya_location = Text("Shibuya Crossing, Shibuya City, Tokyo", style="location")
    image hospital_location = Text("Minami-Azabu area, Minato ward, Tokyo", style="location")
    image murderroom_location = Text("Ōi Futo area, Shinagawa ward, Tokyo", style="location")
    image kabukicho_night = Text("Tokyu Kabukicho Tower\nShinjuku, Tokyo", style="location")
    image asagaya = Text("Weekly Mansion - Asagaya\nSuginami, Tokyo", style="location")
    
    ############################################################################
    ## LOCATION BACKGROUND VIDEOS (WEBM)
    ############################################################################

    # Location background videos - Play once and freeze on last frame
    # These replace static images with animated webm videos for enhanced visuals
    # Use these with the corresponding location text overlays (defined above)

    # Tokyo Locations - Morning versions
    image location_tmpd_m = Movie(play="images/locations/location_tmpd_m.webm", loop=False, keep_last_frame=True)
    image location_denenchofu_m = Movie(play="images/locations/location_denenchofu_m.webm", loop=False, keep_last_frame=True)

    # Tokyo Locations - Night versions
    image location_asagaya_n = Movie(play="images/locations/location_asagaya_n.webm", loop=False, keep_last_frame=True)
    image location_kabuchikotower_n = Movie(play="images/locations/location_kabuchikotower_n.webm", loop=False, keep_last_frame=True)

    ############################################################################
    ## LOCATION BACKGROUND IMAGES (COMMENTED OUT - LEGACY)
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

## Standard template for displaying location text only
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
## LOCATION VIDEO DISPLAY TEMPLATES
################################################################################

## Template for displaying location videos with text overlay
## The video plays in the background while the text appears on top
##
## Basic structure:
## 1. Set background (eigengrau or similar)
## 2. Show video (it will play once and freeze on last frame)
## 3. Show location text overlay with zorder 2
## 4. Pause to let player read
## 5. Hide text first, then video
##
## Example usage - Morning at Den-en-chōfu (home):
##
##     scene eigengrau with clouds_inverse
##     show location_denenchofu_m with slowfade
##     show home_location zorder 2 with dissolve
##     pause 4
##     hide home_location with dissolve
##     hide location_denenchofu_m
##
## Example usage - Night at Asagaya:
##
##     scene eigengrau with clouds_inverse
##     show location_asagaya_n with slowfade
##     show asakusa_location zorder 2 with dissolve
##     pause 4
##     hide asakusa_location with dissolve
##     hide location_asagaya_n
##
## Example usage - Morning at Tokyo Metro Police Department:
##
##     scene eigengrau with clouds_inverse
##     show location_tmpd_m with slowfade
##     show work_location zorder 2 with dissolve
##     pause 4
##     hide work_location with dissolve
##     hide location_tmpd_m
##
## Note: Videos are configured with loop=False and keep_last_frame=True,
## so they will play once and stay visible on the last frame until hidden

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
## 2. For location displays (text only):
##    show tokyo_location zorder 2 with dissolve
##    pause 2
##    hide tokyo_location with dissolve
##
## 3. For location displays with video backgrounds:
##    scene eigengrau with clouds_inverse
##    show location_denenchofu_m with slowfade
##    show home_location zorder 2 with dissolve
##    pause 4
##    hide home_location with dissolve
##    hide location_denenchofu_m
##
## 4. To add new location videos:
##    - Place your .webm file in images/locations/
##    - Add a Movie() definition in the "LOCATION BACKGROUND VIDEOS" section
##    - Use loop=False and keep_last_frame=True for non-looping videos
##    - Follow naming convention: location_[name]_[time] (e.g., location_shibuya_n)
##      where [time] can be: m (morning), a (afternoon), n (night), e (evening)
##
## 5. To add new location text overlays:
##    - Add a new image definition in the appropriate section (OSAKA/TOKYO)
##    - Use the Text() function with the "location" style
##    - Follow the naming convention: [area_name]_location
##
## 6. Location text styling:
##    - Time transitions use "minutes" style
##    - Locations use "location" style
##    - Define these styles in your gui.rpy or screens.rpy
##
## 7. Best practices:
##    - Always use zorder 2 for location text to ensure visibility over videos
##    - Use slowfade for videos, dissolve for text overlays
##    - Keep pause duration between 3-5 seconds for video locations
##    - Hide text before hiding the video for smoother transitions
##    - Videos will auto-freeze on last frame, no need to worry about timing
##
## 8. Savegame compatibility:
##    - All existing text location definitions (osaka_location, home_location, etc.)
##      are maintained for backward compatibility
##    - Video backgrounds are NEW additions and won't affect old saves
##    - You can mix old static backgrounds with new video backgrounds