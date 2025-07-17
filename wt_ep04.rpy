init python:
    wt_data_ep04 = {
        # Nanami initial choices
        "ep04_nana_m1": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "extra_text": "wears a bikini"},
                {"option_num": 2, "char_name": "Nanami", "extra_text": "wears a towel"}
            ])
        },

        "ep04_nana_m2": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "extra_text": "Reveals more of Nanami"},
                {"option_num": 2, "char_name": "Nanami", "extra_text": "No additional pictures of Nanami"}
            ])
        },

        "ep04_nana_m3": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 12, "type": "Love"},
                {"option_num": 2, "char_name": "Nanami", "points": -5, "type": "Love"}
            ])
        },

        # SMS sequences
        "ep04_ambsms_m1": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 5, "type": "Corruption"},
                {"option_num": 2, "char_name": "Nanami", "points": 12, "type": "Love"}
            ])
        },

        "ep04_ambsms_m2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -5, "type": "Love"}
            ])
        },

        "ep04_ambsms_m3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Corruption", "extra_text": "Shows more pictures of Amber"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "No additional pictures of Amber"}
            ])
        },

        "ep04_ambsms_m4": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Corruption", "extra_text": "Shows more pictures of Amber"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "No additional pictures of Amber"}
            ])
        },

        "ep04_ambsms_m5": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "Depending on your personal taste, you can choose any", "extra_text": "option"}
            ])
        },

        "ep04_ambsms_m6": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Corruption", "extra_text": "Shows more pictures of Amber"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "No additional pictures of Amber"}
            ])
        },

        "ep04_ambsms_m7": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 5, "type": "Corruption"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "This will close the communication with Amber"}
            ])
        },

        "ep04_nanamad_1": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 12, "type": "Love", "extra_text": "You will side with Nanami"}
            ]),
            "madison": create_wt_text([
                {"option_num": 2, "char_name": "Madison", "points": 5, "type": "Love", "extra_text": "You will side with Madison"}
            ])
        },

        # Minigame hints
        "ep04_ambsms_m8": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "You need to score 6 to get all of Amber's prizes", "extra_text": "\nOption 1 or 2: +2 points\nOption 3 or 4: +1 point"}
            ])
        },

        "ep04_ambsms_m9": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Option 2 or 3", "extra_text": "+2 points\nOption 1 or 4: +1 point"}
            ])
        },

        "ep04_ambsms_m10": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Option 1 or 4", "extra_text": "+2 points\nOption 2 or 3: +1 point"}
            ])
        },

        "ep04_ambsms_m11": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Depending on your personal taste, you can choose any option", "extra_text": "but pick Amber's face first if you wanna see every picture"}
            ])
        },

        # Isabella choices
        "ep04_isa_m1": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 5, "type": "Love"},
                {"option_num": 2, "char_name": "Isabella", "points": -2, "type": "Love"}
            ])
        },

        "ep04_isa_m2": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Isabella", "points": -2, "type": "Love"}
            ])
        },

        "ep04_isa_m3": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 2, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Isabella",
                    "points": 5,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 5, "type": "Corruption"}
                    ]
                }
            ])
        },

        # Paz choices
        "ep04_pazsms_m1": {
            "paz": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Paz",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 5, "type": "Corruption"}
                    ],
                    "extra_text": "Paz won't be wearing any underwear"
                },
                {"option_num": 2, "char_name": "Paz", "points": 2, "type": "Love"}
            ])
        },

        "ep04_pazsms_m2_p1": {
            "paz": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Paz",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 5, "type": "Corruption"}
                    ]
                },
                {"option_num": 2, "char_name": "Paz", "points": -5, "type": "Love"}
            ])
        },

        "ep04_pazsms_m2_p2": {
            "paz": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Paz",
                    "points": 3,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 1, "type": "Corruption"}
                    ]
                },
                {"option_num": 2, "char_name": "Paz", "points": -5, "type": "Love"}
            ])
        },

        "ep04_pazsms_m3": {
            "paz": create_wt_text([
                {"option_num": 0, "char_name": "Depending on your personal taste, you can choose any", "extra_text": "option"}
            ])
        },

        # Character meeting sequences
        "ep04_nanameetmenu": {
            "nanami": create_wt_text([
                {
                    "option_num": 1, 
                    "char_name": "Nanami", 
                    "points": 2, 
                    "type": "Corruption", 
                    "extra_text": "Branches to Elizabeth or Isabella"
                },
                {
                    "option_num": 2, 
                    "char_name": "Nanami", 
                    "points": 6, 
                    "type": "Love", 
                    "extra_text": "Direct path to Isabella"
                }
            ])
        },

        "ep04_nanamilkmenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Nanami", "points": 1, "type": "Love"}
            ])
        },

        "ep04_nanaaskismenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 2, "type": "Corruption"}
            ])
        },

        "ep04_nanaboozmenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 1, "type": "Corruption", "extra_text": "This path blocks Isabella's scenes but opens the others"},
                {"option_num": 2, "char_name": "Nanami", "extra_text": "This path only leads to Isabella's dream subscene"}
            ])
        },

        "ep04_nanadrumcmenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Nanami", "extra_text": "This path only leads to Elizabeth scene"}
            ])
        },

        "ep04_nanadrumcmenu_2": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Nanami", "points": 6, "type": "Love"}
            ])
        },

        "ep04_nanadruawaksmenu": {
            "nanami": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "is fine, it will depend on what you want to do with Nanami"}
            ])
        },

        "ep04_nanasucpathmenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Nanami", "points": 3, "type": "Love", "extra_text": "This path only leads to Elizabeth scene"}
            ])
        },

        "ep04_nanaleavemenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 3, "type": "Love", "extra_text": "This path locks you out of the Madison scenes"},
                {"option_num": 2, "char_name": "Nanami", "points": -3, "type": "Love"}
            ])
        },

        "ep04_nanaleave2menu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 3, "type": "Love", "extra_text": "This path locks you out of the Madison scenes"},
                {"option_num": 2, "char_name": "Nanami", "points": -3, "type": "Love"}
            ])
        },

        "ep04_nanalehallmenu": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Nanami", "points": -6, "type": "Love", "extra_text": "This path locks you out of the Elizabeth and Amber scenes"}
            ])
        },

        "ep04_ambhallmenu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "extra_text": "This path leads to Elizabeth scenes"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "This path leads to Madison scenes"}
            ])
        },

        "ep04_ambroommenu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": -2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": -2, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep04_ambroommenu_2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "extra_text": "This path leads to Elizabeth scenes"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "This path leads to Madison scenes"}
            ])
        },

        "ep04_ambbjmenu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "points": -2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 1, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep04_ambendmenu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "extra_text": "This path leads to Elizabeth scenes"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "This path leads to Madison scenes"}
            ])
        },

        "ep04_madmcmenu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": -1, "type": "Love"}
            ])
        },

        "ep04_madmassmenu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": -1, "type": "Love"}
            ])
        },

        "ep04_madrewamenu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": -1, "type": "Love"}
            ])
        },

        "ep04_madajmenu": {
            "madison": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Madison",
                    "points": 1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}
                    ]
                },
                {"option_num": 2, "char_name": "Madison", "points": -1, "type": "Love"}
            ])
        },

        "ep04_madajmenu_2": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 3, "type": "Corruption"},
                {"option_num": 2, "char_name": "Madison", "points": -1, "type": "Love"}
            ])
        },

        "ep04_madajmenu_3": {
            "madison": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Madison",
                    "points": -2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 2,
                    "char_name": "Madison",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                },
            ])
        },

        "ep04_elimeetmenu": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Elizabeth", "points": -2, "type": "Love"}
            ])
        },

        "ep04_elimeetmenu_2": {
            "elizabeth": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Elizabeth",
                    "points": -1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}
                    ]
                },
                {"option_num": 2, "char_name": "Elizabeth", "points": 4, "type": "Love"}
            ])
        },

        "ep04_elimeetmenu_3": {
            "elizabeth": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Elizabeth",
                    "points": 4,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 2, "type": "Corruption"}
                    ]
                },
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Love"},
                {"option_num": 3, "char_name": "Elizabeth", "points": -4, "type": "Love"}
            ])
        },

        "ep04_eligolmenu": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Love", "extra_text": "Warning: Pissing content"}
            ])
        },

        "ep04_isamcmenu": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Isabella", "points": -2, "type": "Love"}
            ])
        },

        "ep04_isanobramenu": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Isabella", "points": 1, "type": "Love"}
            ])
        },

        "ep04_nanagamesmenu": {
            "minigames": create_wt_text([
                {"option_num": 0, "char_name": "Correct Order", "extra_text": "is: mouth, neck, shoulders and breasts"}
            ])
        }
    }

    # Update main walkthrough data with Episode 4 content
    walkthrough_data.update(wt_data_ep04)