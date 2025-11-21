init python:
    wt_data_ep06 = {
        # Opening sequences - MC character/philosophy choices (no stat impact)
        "ep06_opening_menu1": {
            "mc": create_wt_text([
                {"option_num": 0, "char_name": "These choices shape MC's", "extra_text": "mindset but don't affect stats directly"}
            ])
        },

        "ep06_crimescene_menu1": {
            "mc": create_wt_text([
                {"option_num": 0, "char_name": "Character development", "extra_text": "choice - influences how MC approaches the case"}
            ])
        },

        "ep06_crimescene_menu2": {
            "mc": create_wt_text([
                {"option_num": 0, "char_name": "Defines MC's moral", "extra_text": "perspective on justice and criminals"}
            ])
        },

        # Amber morning scene - Path selection
        "ep06_morn_amb_menu1": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "extra_text": "CORRUPTION PATH (Requires: No strikes & Corruption ≥25)"
                },
                {"option_num": 2, "char_name": "Amber", "extra_text": "No stat changes"},
                {"option_num": 3, "char_name": "Amber", "points": 2, "type": "Love"},
                {
                    "option_num": 4,
                    "char_name": "Amber",
                    "extra_text": "REJECTION - You will get a strike! Path ends"
                }
            ])
        },

        "ep06_morn_amb_menu2": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "extra_text": "LOVE PATH (Requires: No strikes & Love ≥40)"
                },
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "extra_text": "NEUTRAL PATH - Leads to standard intimate scene"
                },
                {
                    "option_num": 3,
                    "char_name": "Amber",
                    "points": 2,
                    "type": "Corruption",
                    "extra_text": "NEUTRAL PATH with corruption boost"
                }
            ])
        },

        # Neutral path choices
        "ep06_amb_neutral_menu1": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": 2, "type": "Corruption"},
                {
                    "option_num": 3,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Corruption",
                    "additional_effects": [
                        {"points": 1, "type": "Love"}
                    ]
                }
            ])
        },

        "ep06_amb_neutral_sexmenu": {
            "amber": create_wt_text([
                {
                    "option_num": 0,
                    "char_name": "Sex scene choices",
                    "extra_text": "Choose all options to see complete content"
                }
            ])
        },

        "ep06_amb_neutral_menu2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": 2, "type": "Corruption"},
                {
                    "option_num": 3,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Corruption",
                    "additional_effects": [
                        {"points": 1, "type": "Love"}
                    ]
                }
            ])
        },

        "ep06_amb_neutral_postclimax": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Corruption",
                    "additional_effects": [
                        {"points": 1, "type": "Love"}
                    ]
                },
                {"option_num": 3, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        # Corruption path choices
        "ep06_amb_cor_sexmenu": {
            "amber": create_wt_text([
                {
                    "option_num": 0,
                    "char_name": "Corruption sex scenes",
                    "extra_text": "Choose all 4 options to unlock final scene"
                }
            ])
        },

        "ep06_amb_cor_climax": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Corruption"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Corruption",
                    "additional_effects": [
                        {"points": 1, "type": "Love"}
                    ]
                },
                {"option_num": 3, "char_name": "Amber", "points": 2, "type": "Love"}
            ])
        },

        "ep06_amb_cor_postclimax": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Corruption",
                    "additional_effects": [
                        {"points": 1, "type": "Love"}
                    ]
                },
                {"option_num": 3, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        # Love path choices
        "ep06_amb_love_sexmenu": {
            "amber": create_wt_text([
                {
                    "option_num": 0,
                    "char_name": "Love sex scenes",
                    "extra_text": "Choose all 3 options to unlock final scene"
                }
            ])
        },

        "ep06_amb_love_climax": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "points": 10,
                    "type": "Love",
                    "extra_text": "MILESTONE CHOICE"
                },
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 7,
                    "type": "Love",
                    "extra_text": "MILESTONE CHOICE"
                },
                {
                    "option_num": 3,
                    "char_name": "Amber",
                    "points": 5,
                    "type": "Love",
                    "extra_text": "MILESTONE CHOICE"
                }
            ])
        },

        "ep06_amb_love_postclimax": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 3, "char_name": "Amber", "points": 1, "type": "Love"}
            ])
        },

        # Madison train game - Round 1 (True path)
        "ep06_mad_train_r1_true": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        "ep06_mad_train_r1_false": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        # Madison train game - Round 2 (True path)
        "ep06_mad_train_r2_true": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        "ep06_mad_train_r2_false": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        # Madison train game - MC questions Round 2
        "ep06_mad_train_r2_mc_true": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "Neutral question - no cost"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Costs 1 advantage point"}
            ])
        },

        "ep06_mad_train_r2_mc_false": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "Neutral question - no cost"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Costs 1 advantage point"}
            ])
        },

        # Madison train game - Round 3
        "ep06_mad_train_r3_true": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        "ep06_mad_train_r3_false": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        # Madison train game - Round 4
        "ep06_mad_train_r4_true": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        "ep06_mad_train_r4_false": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        # Madison train game - MC questions Round 4
        "ep06_mad_train_r4_mc_true": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "Neutral question - no cost"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Costs 2 advantage points - Deep question"}
            ])
        },

        "ep06_mad_train_r4_mc_false": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "Neutral question - no cost"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Costs 2 advantage points - Deep question"}
            ])
        },

        # Madison train game - Round 5
        "ep06_mad_train_r5_true": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        "ep06_mad_train_r5_false": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% chance Madison detects your lie"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% chance Madison detects your lie"}
            ])
        },

        # Madison train game - Round 6 FINAL (path selection)
        "ep06_mad_train_r6_final_true": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "LOVE PATH - Romantic approach"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "CORRUPTION PATH - Direct/sexual"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "NEUTRAL PATH - Rejection"}
            ])
        },

        "ep06_mad_train_r6_final_false": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "LOVE PATH - Dynamic changed"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "CORRUPTION PATH - Depends on situation"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "NEUTRAL PATH - Rejection"}
            ])
        },

        # Madison train game - MC final question Round 6
        "ep06_mad_train_r6_mc_true": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "Neutral question - no cost"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Costs 1 advantage point - Heavy question"}
            ])
        },

        "ep06_mad_train_r6_mc_false": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "Neutral question - no cost"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Costs 1 advantage point - Heavy question"}
            ])
        },

        # Final decision - Madison studio
        "ep06_madison_studio_final": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Accept Madison's invitation - continues scenes"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Reject Madison - skips studio content"}
            ])
        }
    }

    # Update main walkthrough data with Episode 6 content
    walkthrough_data.update(wt_data_ep06)
