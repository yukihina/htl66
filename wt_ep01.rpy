init python:
    # Episode 1 walkthrough data using the improved helper function
    wt_data_ep01 = {
        # Dream sequence choices
        "ep01_dream1_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Antonella", "points": 2, "type": "Love"}
            ])
        },

        "ep01_2nddream_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Antonella", "points": 1, "type": "Love"}
            ])
        },

        # Pre-game choices
        "ep01_pregame_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": 1, "type": "Love"}
            ])
        },

        "ep01_clothing_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": -1, "type": "Love"}
            ])
        },

        # Park scene choices
        "ep01_thepark_menu1": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love"}
            ])
        },

        "ep01_thepark_menu2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        "ep01_thepark_menu3": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": -5, "type": "Love"}
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
                {
                    "option_num": 1,
                    "char_name": "Elizabeth",
                    "points": 1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 1, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep01_elidress_menu2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 1, "type": "Corruption"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 1, "type": "Love"}
            ])
        },

        # Amber confession scenes
        "ep01_amberconfess_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        "ep01_amberconfess_menu2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "extra_text": "Will skip Elizabeth's scene"}
            ]),
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "Will skip Amber's scene"}
            ])
        },

        "ep01_amberconfess_menu2b": {
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "Will skip Amber's scene"}
            ])
        },

        "ep01_amberconfess_menu3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Corruption", "extra_text": "(Will be important for episode 3)"}
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
                {"option_num": 2, "char_name": "Antonella", "extra_text": "Will skip Antonella's scene"}
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
                {
                    "option_num": 2,
                    "char_name": "Paz",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 1, "type": "Corruption"}
                    ]
                }
            ])
        },

        # Minigame correct answers
        "ep01_game_menu1": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Ask about an Argentine writer\""}
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