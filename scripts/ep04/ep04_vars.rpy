# Documentation for Ren'Py Variable Management in Episodic Games
# ------------------------------------------------------------

# Purpose:
# This guide outlines best practices for managing variables in episodic Ren'Py games,
# ensuring compatibility with existing save games while improving code readability
# and maintainability for future episodes.

# Main Components:
# 1. Variable Naming Conventions
# 2. Variable Types and Usage
# 3. Achievement Tracking
# 4. Scene Management
# 5. Character Relationship Tracking

# Detailed Usage:

# 1. Variable Naming Conventions:
#    - Use 'epXX_' prefix for all variables related to a specific episode (e.g., ep05_)
#    - Group related variables with additional prefixes (e.g., ep05_nanami_)
#    - Use clear, descriptive names (e.g., ep05_nanami_trust instead of ep05_nt)

# 2. Variable Types and Usage:
#    a. Boolean flags:
#       Use for simple yes/no conditions
#       Example in epXX_vars.rpy:
#  default ep05_nanami_kissed = False

#       Example in epXX.rpy:
#  if ep05_nanami_kissed:
#      "Nanami blushes, remembering your kiss."

#    b. Integer counters:
#       Use for tracking multiple states or counting events
#       Example in epXX_vars.rpy:
#  default ep05_amber_photos_seen = 0

#       Example in epXX.rpy:
#  $ ep05_amber_photos_seen += 1
#  if ep05_amber_photos_seen == 3:
#      "You've seen all of Amber's photos."

#    c. Dictionaries:
#       Use for grouping related boolean flags or for more complex state tracking
#       Example in epXX_vars.rpy:
#  default ep05_character_trust = {
#      "nanami": 0,
#      "amber": 0,
#      "isabella": 0
#  }

#       Example in epXX.rpy:
#  $ ep05_character_trust["nanami"] += 5
#  if ep05_character_trust["nanami"] > 50:
#      "Nanami seems to trust you more now."

#    d. Lists:
#       Use for tracking multiple choices or events
#       Example in epXX_vars.rpy:
#  default ep05_party_attendees = []

#       Example in epXX.rpy:
#  $ ep05_party_attendees.append("nanami")
#  if "nanami" in ep05_party_attendees and "amber" in ep05_party_attendees:
#      "Both Nanami and Amber came to your party!"

# 3. Achievement Tracking:
#    Use a dictionary to track achievements
#    Example in epXX_vars.rpy:
#  default ep05_achievements = {
#      "nanami_romance": False,
#      "amber_photos": False,
#      "isabella_friend": False
#  }

#    Example in epXX.rpy:
#  if ep05_nanami_trust > 75:
#      $ ep05_achievements["nanami_romance"] = True
#      $ show_achievement("Nanami's Heart")

# 4. Scene Management:
#    Use integer variables for branching scenes
#    Example in epXX_vars.rpy:
#  default ep05_beach_scene = 0  # 0: not visited, 1: fun day, 2: dramatic event

#    Example in epXX.rpy:
#  label ep05_beach:
#      menu:
#          "Go swimming":
#              $ ep05_beach_scene = 1
#          "Stay on the shore":
#              $ ep05_beach_scene = 2

#      if ep05_beach_scene == 1:
#          "You had a fun day swimming."
#      elif ep05_beach_scene == 2:
#          "You witnessed a dramatic event on the shore."

# 5. Character Relationship Tracking:
#    Use dictionaries for complex relationship tracking
#    Example in epXX_vars.rpy:
#  default ep05_relationships = {
#      "nanami": {"trust": 0, "romance": 0},
#      "amber": {"trust": 0, "romance": 0},
#      "isabella": {"trust": 0, "romance": 0}
#  }

#    Example in epXX.rpy:
#  $ ep05_relationships["nanami"]["trust"] += 5
#  if ep05_relationships["nanami"]["trust"] > 50:
#      $ ep05_relationships["nanami"]["romance"] += 1

# Best Practices:
# 1. Maintain backwards compatibility: Don't change existing variable structures.
# 2. Use comments to explain the purpose and possible values of variables.
# 3. Group related variables together in the epXX_vars.rpy file.
# 4. Use functions for complex operations on variables.
# 5. Keep variable names consistent across episodes.
# 6. Use type hints in comments for clarity (e.g., # int: 0-100).

# Remember: Consistency is key. Once you establish a pattern, stick to it across episodes.
# Always test thoroughly with existing save games when implementing new variable structures.

init:
        # NANAMI INTERACTIONS
        default ep04_nanpath = 0 # Nanami pool path: 1 is bikini / 2 is goth clothes
        default ep04_nanadad = False # Did MC accept to be Nanami's Daddy?
        default ep04_nanaskimpy = False
        default ep04_nanakiss = False # Did MC give her first kiss to Nanami?
        default ep04_refusednanakiss = False #Did MC refused a kiss of Nanami?
        default ep04_mcdrunk = False #Did MC drink beer with Nanami?
        default ep04_mcmilk = False #Did MC drink milk with Nanami?
        default ep04_nanastay = False #Did Nanami stay at MC's bed sleeping?
        default ep04_nanagame = 0
        default ep04_neck_completed = False
        default ep04_shoulders_completed = False
        default ep04_mouth_completed = False
        default ep04_breasts_completed = False
        default ep04_nanakiss_breasts = False #Did MC went to her breast or pussy only?


        # AMBER INTERACTIONS
        default ep04_ambpath = 0 # SMS Amber scene: 1 is sexy clothing / 2 is cosplay
        default ep04_amberno = False # SMS Amber deny everything
        default ep04_ambgame = 0 # SMS Amber game
        default ep04_ambpicsseen = 0 # Number of Amber pics seen on SMS game
        default ep04_seenface = False # Did MC see Amber's face pic?
        default ep04_seentits = False # Did MC see Amber's tits pic?
        default ep04_seenass = False # Did MC see Amber's ass pic?
        default ep04_seenfeet = False # Did MC see Amber's feet pic?
        default ep04_ambnight_cum = 0 # Warn Cum on Amber (1 = face / 2 = tits)
        default ep04_mc_amber_dumb = False #Did MC was being dumb around Amber and got kicked out?

        # MADISON INTERACTIONS
        default ep04_madpath = 0 # Madison caught scene path: 1 is defend Nanami / 2 is agree with Madison
        default ep04_madnight = 0 # (1 = MC doesnt massage her | 2 = MC ONLY massages her with panties | 3 = MC ONLY massages with and without panties  | 4 = MC assjob)
        default ep04_madstory = False #Did MC heard Madison story?
        default ep04_madnanastory = False #Did MC heard Madison-Nanami story?

        # ISABELLA INTERACTIONS
        default ep04_isatruth = False # Did MC tell her the truth about the pool?
        default ep04_isabellakiss = False # Did MC give her first kiss to Isabella?

        # PAZ INTERACTIONS
        default ep04_pazpath = 0 # SMS Paz scene: 1 no underwear / 2 is with underwear
        default ep04_pazred = False
        default ep04_pazgreen = False

        # ELIZABETH INTERACTIONS
        default ep04_elistay = False #Did MC stay with Elizabeth while she was in the bathroom?
        default ep04_elilook = False #Did MC looked her pee?

        # MC INTERACTIONS
        default ep04_afternanami = 0 # 0 = None / 1= After Nanami / 2 = After Amber rejection / 3 = After Amber talk / 4 = After Amber sex

        # ACHIEVEMENTS
        default ep04_ach_nanabikini = False
        default ep04_ach_nanagoth = False
        default ep04_ach_madison = False
        default ep04_ach_madison2 = False
        default ep04_ach_isabella = False
        default ep04_ach_isabella2 = False
        default ep04_ach_elizabeth = False
        default ep04_ach_amber = False