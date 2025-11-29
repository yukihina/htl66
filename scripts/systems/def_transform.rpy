init -1:
    # Basic Opacity Effects
    # ====================

    # Reduces opacity to 50%
    transform alpha_50:
        alpha 0.5

    # Gradually increases opacity from 0 to 100%
    transform fade_in:
        alpha 0.0
        linear 1.0 alpha 1.0

    # Gradually decreases opacity from 100% to 0
    transform fade_out:
        alpha 1.0
        linear 1.0 alpha 0.0
    
    # Creates a flickering neon light effect
    transform neon_flicker:
        alpha 0.0
        linear 0.05 alpha 1.0
        pause 0.5
        linear 0.05 alpha 0.0
        pause 0.1
        linear 0.05 alpha 1.0
        pause 0.5
        linear 0.05 alpha 0.0
        pause 0.1
        linear 0.05 alpha 1.0
        pause 1.0
        linear 0.05 alpha 0.0
        pause 0.2
        linear 0.05 alpha 1.0
        pause 0.7
        repeat

    # In-game Menu Animations
    # =======================
    # Quickly fades in menu elements with minimal delay
    transform igm_appear_nowait:
        alpha 0.0
        pause 0.02  # Reduced from 0.05
        ease 0.25 alpha 1.0  # Reduced from 0.5
        on show:
            alpha 0.0
            pause 0.02
            ease 0.25 alpha 1.0
        on hide:
            alpha 1.0
            ease 0.25 alpha 0.0

    # Fades in background elements with shortened delay
    transform igm_appear_bg:
        alpha 0.0
        pause 0.15  # Reduced from 0.35
        ease 0.25 alpha 1.0  # Reduced from 0.5
        on show:
            alpha 0.0
            pause 0.15
            ease 0.25 alpha 1.0
        on hide:
            alpha 1.0
            ease 0.25 alpha 0.0

    # Standard fade in with reduced timing
    transform igm_appear:
        alpha 0.0
        pause 0.25  # Reduced from 0.5
        ease 0.25 alpha 1.0  # Reduced from 0.5
        on show:
            alpha 0.0
            pause 0.25
            ease 0.25 alpha 1.0
        on hide:
            alpha 1.0
            ease 0.25 alpha 0.0

    # Fades in foreground elements with optimized delay
    transform igm_appear_fg:
        alpha 0.0
        pause 0.35  # Reduced from 0.65
        ease 0.25 alpha 1.0  # Reduced from 0.5
        on show:
            alpha 0.0
            pause 0.35
            ease 0.25 alpha 1.0
        on hide:
            alpha 1.0
            ease 0.25 alpha 0.0
        
    # Fades in foreground elements with shortened final delay
    transform igm_appear_fg2:
        alpha 0.0
        pause 0.45  # Reduced from 0.9
        ease 0.25 alpha 1.0  # Reduced from 0.5
        on show:
            alpha 0.0
            pause 0.45
            ease 0.25 alpha 1.0
        on hide:
            alpha 1.0
            ease 0.25 alpha 0.0
    
    # Movement Effects
    # ================

    # Creates a vertical shaking effect
    transform vpunch_effect(time=0.3, offset=10, pause=1):
        ease time/4 yoffset -offset
        ease time/4 yoffset offset
        ease time/4 yoffset -offset
        ease time/4 yoffset 0
        pause pause
        repeat

    # Creates a horizontal shaking effect
    transform hpunch_effect(time=0.3, offset=10, pause=1):
        ease time/4 xoffset -offset
        ease time/4 xoffset offset
        ease time/4 xoffset -offset
        ease time/4 xoffset 0
        pause pause
        repeat

    # Creates a bouncing effect
    transform bounce:
        subpixel True
        xalign 0.5
        yalign 0.5
        zoom 0.1
        alpha 0.0
        ease 0.5 zoom 1.0 alpha 1.0
        ease 0.2 xzoom 1.2 yzoom 0.8
        ease 0.2 xzoom 0.9 yzoom 1.1
        ease 0.2 xzoom 1.1 yzoom 0.9
        ease 0.2 xzoom 0.95 yzoom 1.05
        ease 0.2 xzoom 1.05 yzoom 0.95
        ease 0.2 xzoom 1.0 yzoom 1.0

    # Creates a dizzy, swirling effect
    transform dizzyness:
        subpixel True
        zoom 1.05
        anchor(.5, .5)
        pos(.5, .5)
        on show:
            parallel:
                linear 2.5 xalign 0.6 yalign 0.5
                linear 2.5 xalign 0.6 yalign 0.6
                linear 2.5 xalign 0.4  yalign 0.6
                linear 2.5 xalign 0.4  yalign 0.4
            repeat
    
    # Creates a pulsing, heartbeat-like effect
    transform heartbeat(a=0.975, b=1.0, x=0.8):
        alpha x
        subpixel True
        zoom a
        ease 1 zoom b
        ease 1 zoom a
        repeat

    # Creates a swaying effect
    transform sway:
        linear 0.3 xoffset 20
        linear 0.3 xoffset -20
        linear 0.3 xoffset 0
        choice:
            pause 1.085
        choice:
            pause 2.8
        choice:
            pause 3.5
        repeat

    # Creates a subtle pulsing effect
    transform concentrate:
        subpixel True
        truecenter
        zoom 1.0
        ease 10 zoom 1.05
        ease 10 zoom 1.0
        repeat

    # Zoom Effects
    # ============
    
    # 10% smaller
    transform scale_down:
        subpixel True
        truecenter
        zoom 0.95

    # Gradually zooms in
    transform zoom_in:
        subpixel True
        truecenter
        zoom 1.0
        easein 0.5 zoom 1.05
        ease 1.0 zoom 1.2
        ease 2.0 zoom 1.15
        easein 6.5 zoom 1.2
        ease 2.0 zoom 1.0

    # Gradually zooms out
    transform zoom_out:
        subpixel True
        truecenter
        zoom 1.2
        ease 10 zoom 1.0

    # Creates a camera-like zoom effect
    transform camera_zoom:
        subpixel True
        truecenter
        zoom 1.0
        ease 2.0 zoom 1.1
        pause 2.0
        ease 2.0 zoom 1.0

    # Creates a quick, dramatic zoom effect
    transform dramatic_zoom:
        subpixel True
        align (0.5, 0.5)
        zoom 1.0
        ease 1.5 zoom 1.3

    # Ken Burns Effects
    # =================

    # Pans from left to right
    transform ken_burns_left_to_right:
        subpixel True
        align (0.0, 0.5)
        zoom 1.05
        linear 10.0 align (1.0, 0.5)

    # Pans from right to left
    transform ken_burns_right_to_left:
        subpixel True
        align (1.0, 0.5)
        zoom 1.05
        linear 10.0 align (0.0, 0.5)

    # Pans from top to bottom
    transform ken_burns_top_to_bottom:
        subpixel True
        align (0.5, 0.0)
        zoom 1.05
        linear 10.0 align (0.5, 1.0)

    # Pans from bottom to top
    transform ken_burns_bottom_to_top:
        subpixel True
        align (0.5, 1.0)
        zoom 1.05
        linear 10.0 align (0.5, 0.0)

    # Pans from top-left to bottom-right
    transform ken_burns_corner_to_corner:
        subpixel True
        align (0.0, 0.0)
        zoom 1.1
        linear 15.0 align (1.0, 1.0)

    # Pans from top-right to bottom-left
    transform ken_burns_corner_to_corner2:
        subpixel True
        align (1.0, 0.0)
        zoom 1.1
        linear 15.0 align (0.0, 1.0)

    # Pans from bottom-left to top-right
    transform ken_burns_corner_to_corner3:
        subpixel True
        align (0.0, 1.0)
        zoom 1.1
        linear 15.0 align (1.0, 0.0)

    # Pans from bottom-right to top-left
    transform ken_burns_corner_to_corner4:
        subpixel True
        align (1.0, 1.0)
        zoom 1.1
        linear 15.0 align (0.0, 0.0)

    # Subtle Effects
    # ==============

    # Creates a subtle zoom in effect
    transform subtle_zoom_in:
        subpixel True
        align (0.5, 0.5)
        zoom 1.0
        ease 5.0 zoom 1.1

    # Creates a subtle zoom out effect
    transform subtle_zoom_out:
        subpixel True
        align (0.5, 0.5)
        zoom 1.1
        ease 5.0 zoom 1.0

    # Creates a shaking effect for impacts
    transform impact_shake:
        subpixel True
        align (0.5, 0.5)
        xoffset 0
        ease 0.02 xoffset 20
        ease 0.02 xoffset -15
        ease 0.02 xoffset 10
        ease 0.02 xoffset -5
        ease 0.02 xoffset 0
        repeat 3

    # Creates a pulsing blur effect for focus
    transform focus_pulse:
        subpixel True
        align (0.5, 0.5)
        blur 0
        ease 2.0 blur 10
        ease 2.0 blur 0
        repeat

    # Creates a pulsing blur effect for focus for menus
    transform focus_pulse_menu:
        subpixel True
        align (0.5, 0.5)
        blur 10 alpha 0.7
        ease 2.0 blur 10 alpha 0.5
        ease 2.0 blur 10 alpha 0.7
        repeat
   
    # Combined Effects
    # ===============

    # Combines zoom and blur for a dramatic focus effect
    transform dramatic_focus:
        subpixel True
        align (0.5, 0.5)
        zoom 1.0
        parallel:
            ease 3.0 zoom 1.15
        parallel:
            blur 0
            ease 1.5 blur 10
            ease 1.5 blur 0
    
    transform dramatic_focus_out:
        subpixel True
        align (0.5, 0.5)
        zoom 1.15
        parallel:
            ease 5.0 zoom 1.0
        parallel:
            blur 10
            ease 5.0 blur 0

    # Slowly reveals an image while zooming out
    transform slow_reveal:
        subpixel True
        align (0.0, 0.5)
        zoom 1.1
        parallel:
            linear 15.0 align (1.0, 0.5)
        parallel:
            ease 5.0 zoom 1.0
            
    # Shifts focus by changing blur
    transform focus_shift:
        subpixel True
        align (0.5, 0.5)
        blur 10
        pause 0.5
        linear 1.0 blur 0

    transform focus_shift_sms:
        block:
            subpixel True
            align (0.5, 0.5)
            linear 1.0 blur 10

    # Creates a dramatic realization effect with zoom and blur
    transform dramatic_realization:
        subpixel True
        align (0.5, 0.5)
        zoom 1.0
        blur 0
        parallel:
            ease 1.5 zoom 1.3
            ease 5.0 zoom 1.0
        parallel:
            linear 0.5 blur 10
            linear 1.0 blur 0

    # Simulates an action sequence with zoom, rotation, and shaking
    transform action_sequence:
        subpixel True
        align (0.5, 0.5)
        zoom 1.0
        rotate 0
        parallel:
            ease 0.5 zoom 1.2
        parallel:
            ease 0.5 rotate -5
        parallel:
            ease 0.02 xoffset 20
            ease 0.02 xoffset -15
            ease 0.02 xoffset 10
            ease 0.02 xoffset -5
            ease 0.02 xoffset 0
            repeat 2

    # Creates a flashback effect with panning and blurring
    transform emotional_flashback:
        subpixel True
        align (0.0, 0.0)
        zoom 1.1
        blur 0
        parallel:
            linear 10.0 align (1.0, 1.0)
        parallel:
            linear 3.0 blur 5
            linear 3.0 blur 0
            repeat
            
    # Simulates a camera snapshot effect
    transform photo_effect:
        subpixel True
        align (0.5, 0.5)
        zoom 1.1
        ease 0.2 xoffset 5 yoffset -5
        ease 0.2 xoffset -3 yoffset 3
        ease 0.05 zoom 1.09
        ease 0.05 zoom 1.1
        ease 0.3 xoffset 0 yoffset 0

    # Creates a white flash effect for photos
    image photo_flash:
        Solid("#FFFFFF")
        alpha 0.0
        linear 0.1 alpha 0.8
        linear 0.1 alpha 0.0

    # Creates a subtle breathing effect
    transform subtle_breathing:
        subpixel True
        align (0.5, 0.5)
        zoom 1.1
        ease 2.0 yoffset -10
        ease 2.0 yoffset 0
        repeat

    # Special Effects
    # ==============

    # Creates a flashing effect for ejaculation scenes
    transform ejaculation_flash:
        alpha 0.0
        linear 0.2 alpha 0.2
        linear 0.2 alpha 0.4
        linear 0.2 alpha 0.6
        linear 0.2 alpha 0.8
        linear 0.1 alpha 1.0
        linear 0.1 alpha 0.8
        linear 0.1 alpha 1.0
        linear 0.1 alpha 0.8
        linear 0.1 alpha 1.0
        linear 0.1 alpha 0.8
        linear 0.1 alpha 1.0
        linear 0.2 alpha 0.6
        linear 0.2 alpha 0.4
        linear 0.2 alpha 0.2
        linear 0.2 alpha 0.0

    # Simulates a point-of-view dying effect
    transform pov_die:
        alpha 0.0
        easein 1.0 alpha 1.0
        easeout 1.0 alpha 0.0
        easein 1.0 alpha 0.8
        easeout 1.0 alpha 0.0
        easein 1.0 alpha 0.6
        easeout 1.0 alpha 0.0
        easein 1.0 alpha 0.4
        easeout 1.0 alpha 0.0
        repeat

    # Creates a slow panning effect
    transform slow_pan:
        yalign 0.0
        linear 20.0 yalign 1.0
        pause 2.0
        linear 20.0 yalign 0.0
        repeat

    transform videocall_open:
        alpha 0.0
        xoffset -300
        linear 0.2:
            alpha 1.0
            zoom 1.0
            xoffset 0
        ease 0.2:
            zoom 1.05
        ease 0.2:
            zoom 1.0

    # Blood overlay that slowly covers the screen (James Bond style)
    # This creates the iconic blood dripping down effect
    transform blood_cover:
        subpixel True
        alpha 0.0
        yalign -1.0  # Start above screen
        zoom 1.0
        # Flash impact
        parallel:
            ease 0.1 alpha 1.0  # Quick fade in
            pause 0.2
            ease 0.7 alpha 0.9  # Slight fade as it drips
        # Drip down motion
        parallel:
            pause 0.05
            ease 0.8 yalign 0.0  # Smooth drip down to cover screen
