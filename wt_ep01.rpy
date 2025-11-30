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
                {"option_num": 1, "char_name": "Antonella", "points": 1, "type": "Love", "extra_text": "Sets ep01_hug = True (unlocks special dialogue later)"}  # Base 3 × 0.25 = 1 (rounded)
            ])
        },

        "ep01_clothing_menu": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": -1, "type": "Love", "extra_text": "Sets ep01_gothgirl = True"}  # Base -3 × 0.25 = -1 (rounded)
            ])
        },

        # Park scene choices
        "ep01_thepark_menu1": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love", "extra_text": "Sets ep01_park = 2 (chose Amber path)"},
                {"option_num": 2, "char_name": "Antonella", "extra_text": "Sets ep01_park = 1 (chose Antonella path). Affects later branching"}
            ])
        },

        "ep01_thepark_menu2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love", "extra_text": "Sets ep01_lieamber = True. Changes home scene dialogue significantly"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love", "extra_text": "Telling the truth. Amber gets very angry"}
            ])
        },

        "ep01_thepark_menu3": {
            "antonella": create_wt_text([
                {"option_num": 1, "char_name": "Antonella", "points": -1, "type": "Love", "extra_text": "Sets ep01_losttrust = True. CRITICAL: Calling her feelings 'trivial' is devastating!"}  # Base -5 × 0.25 = -1 (rounded)
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
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Corruption", "extra_text": "Sets ep01_elimemories = True"},  # Base 2 × 1.0 = 2
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Love"}  # Base 1 × 2.0 = 2
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
                {"option_num": 1, "char_name": "Amber", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        "ep01_amberconfess_menu2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "extra_text": "Sets ep01_amblove = True (accepted Amber's feelings). Will skip Elizabeth's scene"}
            ]),
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "Rejected Amber's confession. Will skip Amber's scene"}
            ])
        },

        "ep01_amberconfess_menu2b": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "extra_text": "Sets ep01_amblove = True (accepted Amber's feelings). Elizabeth scene already seen"}
            ]),
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "Rejected Amber's confession. Will skip Amber's scene"}
            ])
        },

        "ep01_amberconfess_menu3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Corruption", "extra_text": "Sets ep01_first = True. Leads to losing virginity (both). Will be important for episode 3"}  # Base 3 × 1.5 = 5 (rounded)
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
                {"option_num": 1, "char_name": "Antonella", "extra_text": "Sets ep01_antobday = True (remembered her birthday). Explains necklace connection. Opens Antonella's birthday flashback"},
                {"option_num": 2, "char_name": "Antonella", "extra_text": "Will skip Antonella's birthday scene"}
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
                {"option_num": 2, "char_name": "Paz", "points": 2, "type": "Corruption"}  # Base 2 × 1.0 = 2
            ])
        },

        # Minigame correct answers
        # ACHIEVEMENT TIP: Answer all 6 questions correctly (MC doesn't lose clothes) to unlock ep01_bestprize = True
        "ep01_game_menu1": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Answer", "extra_text": "is \"Ask about an Argentine writer\". For achievement: win all 6 rounds perfectly"}
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