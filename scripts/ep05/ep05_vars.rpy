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
    # AMBER INTERACTIONS
    default ep05_ambignore = False # Does Amber ignore MC because she's mad?
    default ep05_ambersus_eli = False #Does Amber in the past suspects on Elizabeth and MC relatioship?
    default ep05_amber_route = 0 # 1 = Romantic and gentle / 2 = Rough and passionate / 3 = Reject her

    # ISABELLA INTERACTIONS
    default ep05_isacosplay = 0 # Negative (-4) = Corruption Achievement / Positive = Love Achievement (+4)

    # MADISON INTERACTIONS
    default ep05_confrontation_peaceful = False #Did MC confronted Madison peacefully?
    default ep05_threat_direct = False #Did MC threatened Madison directly?
    default ep05_stance_surrender = False #Did MC surrendered to Madison?

    # NANAMI INTERACTIONS
    default ep05_mc_blame_madison = False #Did MC blame Madison because she said Nanami should strip to boys when drunk
    default ep05_mc_takes_responsibility = False #Did MC take responsibility on drunk night @ episode 4
    default ep05_nanami_sex_education = False #Did MC gave sex ed to Nanami?
    default ep05_madison_is_bad = False #Did MC said Madison is bad influence?

    # PAZ INTERACTION
    default ep05_paz_choice = 0 # 0 = No choice, 1 = help her, 2 = reject her, 3 = accept her

    # SCENE TRACKING
    default look_down_seen = False  # Track if player has seen lower view
    default look_middle_seen = False  # Track if player has seen middle view
    default look_up_seen = False  # Track if player has seen upper view
    default ep05_mcthinksex = False # Tracks if player makes naughty advances to Elizabeth
    default ep05_mnwait = False #Did MC waited to enter the bath and got caught by Madison?
    default ep05_mntouch = False #Did MC groped Nanami in the bath following Madison's orders?
    default ep05_bath_path = None #Elizabeth path shower scene
    default ep05_integrity_choice = None
    default ep05_mnvoy = None #Nanami voyeur path
    default ep05_finish_inside = False #Did MC finish inside Madison?
    default ep05_guilt_points = 0
    default ep05_curiosity_points = 0
    default ep05_evasive_points = 0

    # ACHIEVEMENTS
    default ep05_ach_isaintro = False # Achievement for Isabella part 1
    default ep05_ach_ambvseli = False # Achievement for Amber vs Elizabeth
    default ep05_ach_novseli = False # Achievement for Elizabeth on the dark (no amber vs elizabeth)
    default ep05_ach_nanastrike = False #Achievement for Nanami strike achiev
    default ep05_ach_final1 = False # Achievement for Elizabeth final
    default ep05_ach_final2 = False # Achievement for Elizabeth final 2