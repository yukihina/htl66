# Documentation for the Ren'Py Random Menu Generation Script
# ----------------------------------------------------------

# Purpose:
# This script provides functionality to create randomized choice menus in the game.
# It allows for dynamic and varied player choices, enhancing replayability and
# adapting to different game states.

# Main Components:
# 1. random_menu Function:
#    - Generates a randomized menu based on provided options and conditions.

# Detailed Usage:
# random_menu(character, character_dialogue, prompt, options)
# 
# Parameters:
# - character: The speaking character (optional)
# - character_dialogue: Dialogue before the menu (optional)
# - prompt: A question or statement for the menu (optional)
# - options: List of tuples (condition, label, action)

# Example Usage:
# $ choice = random_menu(
#     mc, "What should I do?", None,
#     [
#         (True, "Go to the park", "label_park"),
#         (has_money, "Buy a gift", "label_gift"),
#         (is_night, "Go to sleep", "label_sleep")
#     ]
# )
# jump expression choice

# Connections to Other Files:
# - This function can be called from any script file where player choices are presented.
# - It interacts with the game's state variables to determine which options are available.

# Maintenance and Expansion:
# - When adding new types of choices, ensure they follow the (condition, label, action) format.
# - Consider adding new parameters if additional functionality is needed (e.g., menu styling).

# Note for Novices:
# - The 'condition' in each option determines if that choice is available.
# - 'label' is the text shown to the player for each choice.
# - 'action' is typically a label name to jump to when the choice is selected.

# Remember: Random menus can greatly enhance replayability but ensure that all possible
# combinations make sense in the context of your story. Test thoroughly to avoid
# inconsistencies in the narrative flow.

init python:

    def random_menu(character=None, character_dialogue=None, prompt=None, options=[]):
        shuffled_options = list(options)
        renpy.random.shuffle(shuffled_options)
        menu_items = [
            (label, action)
            for condition, label, action in shuffled_options
            if condition
        ]
        if prompt is not None:
            menu_items.insert(0, (prompt, None))
        if character and character_dialogue:
            renpy.say(character, character_dialogue)
        return renpy.display_menu(menu_items)



# =====================
# RANDOM MENU USAGE TEMPLATES
# =====================

# The following are example templates on how to use the random_menu function in various scenarios.
# Remember to replace placeholders with appropriate values for your game.

# ------ CONDITIONAL MENU OPTIONS ------
# You can use conditions to determine whether a menu option appears.

# Define your conditions (e.g., if a certain event has been seen or not)
# has_seen_event = True  # or False

# $ action_variable_name = random_menu(
#     None, None, None,
#     [
#         (True, "Always available option", "label_name_1"),
#         (has_seen_event, "Option available after a certain event", "label_name_2"),
#         (not has_seen_event, "Option available before a certain event", "label_name_3"),
#     ]
# )
# jump action_variable_name

# ------ MENU WITHOUT A PROMPT ------
# If you don't want a prompt, use None as the first argument.

# $ action_variable_name = random_menu(
#     None, None, None,
#     [
#         (True, "Option Text 1", "label_name_1"),
#         (True, "Option Text 2", "label_name_2"),
#     ]
# )
# jump action_variable_name


# =====================
# RANDOM MENU TEMPLATE WITH CHARACTER DIALOGUE
# =====================

# This template allows you to create a randomized menu, 
# and depending on the choice made, a character can say something 
# before transitioning to the corresponding label.

# Usage:
# 1. Replace `menu_action_variable` with a unique variable name.
# 2. Replace the menu options and corresponding labels.
# 3. Replace `character_name` with the name of your character and the dialogue.
# 4. Add more conditions as needed.

# $ menu_action_variable = random_menu(
#     character_name,  # The character who speaks before the menu. If none, use None.
#     "Character's dialogue before the menu (optional). If none, use None.",
#     None,  # You can add a prompt here if needed.
#     [
#         # Add or modify these tuples for your menu options.
#         (True, "Option Text 1", "label_name_1"),
#         (True, "Option Text 2", "label_name_2"),
#         (True, "Option Text 3", "label_name_3"),
#     ]
# )

# Replace `response_character_name` with your character's name or variable for the response.
# if menu_action_variable == "label_name_1":
#     response_character_name "Dialogue for Option 1"
#     jump label_name_1
# elif menu_action_variable == "label_name_2":
#     response_character_name "Dialogue for Option 2"
#     jump label_name_2
# elif menu_action_variable == "label_name_3":
#     response_character_name "Dialogue for Option 3"
#     jump label_name_3

# Add more conditions as needed for additional options.
