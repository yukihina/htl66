init python:
    # Episode 1 walkthrough data using the improved helper function
    wt_data_ep01 = {
        # Dream sequence choices
        "ep01_dream1_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": 1, "type": "Love"},  # Base 3 × 0.25 = 1 (rounded)
                {"option_num": 2, "char_name": "Antonella", "points": 1, "type": "Love"}   # Base 5 × 0.25 = 1 (rounded)
            ])
        },

        "ep01_2nddream_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": 1, "type": "Love"},  # Base 5 × 0.25 = 1 (rounded)
                {"option_num": 2, "char_name": "Antonella", "points": 1, "type": "Love"}   # Base 3 × 0.25 = 1 (rounded)
            ])
        },

        # Pre-game choices
        "ep01_pregame_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": 1, "type": "Love", "extra_text": "This tender moment will unlock special dialogue later"}  # Base 3 × 0.25 = 1 (rounded)
            ])
        },

        "ep01_clothing_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": -1, "type": "Love", "extra_text": "Ditching Antonella to flirt with another girl will hurt her feelings"}  # Base -3 × 0.25 = -1 (rounded)
            ])
        },

        # Park scene choices
        "ep01_thepark_menu1": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love", "extra_text": "Side with Amber. This choice affects later scenes"},
                {"option_num": 2, "char_name": "Antonella", "extra_text": "Stay with Antonella. This choice affects later scenes"}
            ])
        },

        "ep01_thepark_menu2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love", "extra_text": "Lie to Amber about Antonella. This will significantly change dialogue at home"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love", "extra_text": "Tell Amber the truth. She will get very angry"}
            ])
        },

        "ep01_thepark_menu3": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": -1, "type": "Love", "extra_text": "CRITICAL: Calling her feelings 'trivial' is devastating! You will lose her trust"}  # Base -5 × 0.25 = -1 (rounded)
            ])
        },

        # Home scene choices
        "ep01_home_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        # Elizabeth dress scenes
        "ep01_elidress_menu": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Corruption", "extra_text": "Play along with her suggestive teasing"},  # Base 2 × 1.0 = 2
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Love", "extra_text": "Establish healthy boundaries"}  # Base 1 × 2.0 = 2
            ])
        },

        "ep01_elidress_menu2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 1, "type": "Corruption"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Love"}  # Elizabeth trust: 1 × 2.0 = 2
            ])
        },

        # Amber confession scenes
        "ep01_amberconfess_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love", "extra_text": "Stay to hear Amber's confession. Required to access romantic scenes"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        "ep01_amberconfess_menu2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "extra_text": "Accept Amber's romantic feelings. Will skip Elizabeth's scene and open Amber's intimate scene. ACHIEVEMENT: Unlocks 'Forbidden Love'"}
            ]),
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "Reject Amber's confession. Will skip Amber's intimate scene"}
            ])
        },

        "ep01_amberconfess_menu2b": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "extra_text": "Accept Amber's romantic feelings. Opens Amber's intimate scene. ACHIEVEMENT: Unlocks 'Forbidden Love'"}
            ]),
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "Reject Amber's confession. Will skip Amber's intimate scene"}
            ])
        },

        "ep01_amberconfess_menu3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Corruption", "extra_text": "Allow her to continue. Both of you will lose your virginity. This choice will be important in episode 3. ACHIEVEMENT: Unlocks 'Turning Point'"}  # Base 3 × 1.5 = 5 (rounded)
            ])
        },

        # Isabella and Antonella scenes
        "ep01_antobd04_menu1": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 1, "type": "Love"}
            ])
        },

        "ep01_antobd_menu2": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "extra_text": "Look at the girl. This opens Antonella's birthday flashback and explains the necklace connection. ACHIEVEMENT: Unlocks 'Timeless Bond'"},
                {"option_num": 2, "char_name": "Antonella", "extra_text": "Don't look at her. Will skip Antonella's birthday flashback"}
            ])
        },

        # Post-game choices
        "ep01_postgame_menu": {
            "antonella": create_wt_text([
                {"option_num": 2, "char_name": "Antonella", "extra_text": "Will skip Antonella's scene"}
            ])
        },

        # SMS conversation choices
        "ep01_sms01_wt1": {
            "paz": create_wt_text([
                {"option_num": 1, "char_name": "Paz", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Paz", "points": 1, "type": "Love"}
            ])
        },

        "ep01_sms01_wt2": {
            "paz": create_wt_text([
                {"option_num": 1, "char_name": "Paz", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Paz", "points": 2, "type": "Corruption", "extra_text": "Flirt back to receive an extra spicy photo"}  # Base 2 × 1.0 = 2
            ])
        },

        # Minigame correct answers
        "ep01_game_menu1": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Ask about an Argentine writer\". ACHIEVEMENT: Answer all 6 correctly to unlock 'The Grand Prize'"}
            ])
        },

        "ep01_game_menu2": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Niccolò Machiavelli\""}
            ])
        },

        "ep01_game_menu3": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Demian\""}
            ])
        },

        "ep01_game_menu4": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Vladimir Nabokov\""}
            ])
        },

        "ep01_game_menu5": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Something about Agatha Christie\""}
            ])
        },

        "ep01_game_menu6": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"The Epic of Gilgamesh\""}
            ])
        },

        # Miscellaneous choices
        "ep01_home_menu2": {
            "elizabeth": create_wt_text([
                {"option_num": 0, "char_name": "The best order to play is to choose Option 1", "extra_text": "first"}
            ])
        },

        "ep01_train_menu": {
            "isabella": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "is fine, it depends on what you want to reply"}
            ])
        },

        "ep01_antodemo_menu": {
            "antonella": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "is fine, it depends on what you want to reply"}
            ])
        },

        "ep01_antolib_menu": {
            "antonella": create_wt_text([
                {"option_num": 2, "char_name": "Option 2", "extra_text": "Will reveal another part of Antonella's body to you"}
            ])
        },

        "ep01_antochangeclothes_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Option 1", "extra_text": "Will reveal Antonella's sexy ass to you"}
            ])
        },

        "ep01_elibathdress_menu": {
            "elizabeth": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "is fine, it depends on what you want to reply. Either way, Elizabeth won't listen to your advice"}
            ])
        }
    }

    # Update main walkthrough data with Episode 1 content
    walkthrough_data.update(wt_data_ep01)