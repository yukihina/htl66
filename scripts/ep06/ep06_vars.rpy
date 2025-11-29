
init:

    # AMBER TRACKING
    default e6_amber_path = "none"  # "love", "corruption", "neutral"
    default e6_amber_neutral_blowjob_seen = False
    default e6_amber_neutral_boobjob_seen = False
    default e6_amber_cor_blowjob_seen = False
    default e6_amber_cor_boobjob_seen = False
    default e6_amber_cor_assjob_seen = False
    default e6_amber_cor_footjob_seen = False
    default e6_amber_love_worship_seen = False
    default e6_amber_love_oral_seen = False
    default e6_amber_love_assjob_seen = False

    # MADISON TRAIN GAME
    default ep06_mc_lies_detected = 0
    default ep06_mc_advantage_points = 0
    default ep06_madison_path = "none"  # "love", "corruption", "neutral"
    
    # SCENE TRACKING
    default e6_gore = False

    # ACHIEVEMENTS
    default ep06_ach_amblove = False # Achievement for Amber love path
    default ep06_ach_ambcor = False # Achievement for Amber corruption path

init python:
    def ep06_detect_lie(detection_chance):
        """
        Helper function for Madison train game lie detection.

        Args:
            detection_chance (int): Percentage chance of detection (0-100)
                                   50 = Partial Truth
                                   70 = Lie

        Returns:
            None - Increments lie counter if detected, or grants advantage point if not.
                   Successfully deceiving Madison gives MC an advantage in later interactions.
        """
        import renpy.exports as renpy

        # Roll for detection
        if renpy.random.randint(1, 100) <= detection_chance:
            # Madison detected the lie
            store.ep06_mc_lies_detected += 1
        else:
            # MC successfully deceived Madison, gains advantage
            store.ep06_mc_advantage_points += 1