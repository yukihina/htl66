init python:
    wt_data_ep03 = {
        # Isabella hug choice
        "ep03_isahug_menu": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Isabella", "points": 1, "type": "Love"}
            ])
        },
        
        # Madison interaction choice
        "ep03_maddie_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 10, "type": "Love"}
            ])
        },
        
        # Amber scenes choices
        "ep03_ambertits_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Amber", "points": 2, "type": "Love"}
            ])
        },
        
        "ep03_amberfeels_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -5, "type": "Love"}
            ])
        },
        
        "ep03_amberstop_menu": {
            "amber": create_wt_text([
                {"option_num": 2, "char_name": "Amber", "extra_text": "will skip several scenes involving Amber"}
            ])
        },
        
        "ep03_amberconvinc_menu": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "Both options", "extra_text": "will convince Amber.\nThey only affect the renderings and dialogues"}
            ])
        },
        
        "ep03_amberstaygo_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -3, "type": "Love", "extra_text": "and will skip several scenes with her"}
            ])
        },
        
        "ep03_amberinvpool_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -5, "type": "Love", "extra_text": "and significantly damages your relationship with her"}
            ])
        },
        
        # Madison scenes choices
        "ep03_maddiebod_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Corruption"}
            ])
        },
        
        "ep03_maddieass_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 6, "type": "Corruption"}  # Madison cor: 3 × 2.0 = 6
            ])
        },
        
        # Amber room and sleep scenes
        "ep03_amberroom_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Love", "extra_text": "ACHIEVEMENT: Get the sweater. If you have sex with Amber later, unlocks 'Silken Secrets'"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": -2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 5, "type": "Corruption"}
                    ],
                    "extra_text": "ACHIEVEMENT: Bring only underwear. If you have sex with Amber later, unlocks 'Passion's Price'"
                }
            ])
        },

        "ep03_ambersleep_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love", "extra_text": "This choice opens Amber's intimate scenes and possible achievements"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "will skip several sex scenes involving Amber and block achievements"}
            ])
        },
        
        "ep03_ambersleep_menu2": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "will result in Madison catching you in the act. ACHIEVEMENT: Unlocks 'Prophecy Fulfilled'"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "will protect you from Madison catching you in the act"}
            ])
        },
        
        "ep03_ambersleep_menu3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "extra_text": "will get you into Amber sex scenes (Only recommended if you've had your first time with her)"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "will skip sex scenes involving Amber"}
            ])
        },
        
        # Amber sex scene choices
        "ep03_ambersex_menu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "points": -5,
                    "type": "Love",
                    "additional_effects": [
                        {"points": -2, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 5, "type": "Corruption"}
                    ]
                }
            ])
        },
        
        "ep03_ambersex_menu2": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "is fine, it will depend on what you want to do with what Amber suggests"}
            ])
        },
        
        "ep03_ambersex_menu3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": -5, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 5,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}  # Amber cor: 1 × 1.5 = 2
                    ]
                }
            ])
        },
        
        "ep03_ambersex_menu4": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": -5, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 5,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}  # Amber cor: 1 × 1.5 = 2
                    ]
                }
            ])
        }
    }

    # Update the main walkthrough data with Episode 3 content
    walkthrough_data.update(wt_data_ep03)
