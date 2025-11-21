init python:
    wt_data_ep06 = {
        # MC Case Investigation Choices
        "ep06_case_attitude_menu": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+1 Integrity to Light"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+1 Integrity to Darkness"}
            ])
        },

        "ep06_killer_profile_menu": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness"}
            ])
        },

        "ep06_criminal_vision_menu": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness"}
            ])
        },

        # Amber Morning Scenes
        "ep06_amber_first_decision_menu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "extra_text": "Corruption path (requires Amber cor >= 25 and no strikes)"
                },
                {"option_num": 3, "char_name": "Amber", "points": 2, "type": "Love"},
                {
                    "option_num": 4,
                    "char_name": "Amber",
                    "extra_text": "Gives you a strike! (3 strikes = game over)"
                }
            ])
        },

        "ep06_amber_intimacy_response_menu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "extra_text": "Love path (requires Amber trust >= 40 and no strikes)"
                },
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "extra_text": "Neutral path - continues to neutral scenes"
                },
                {"option_num": 3, "char_name": "Amber", "points": 2, "type": "Corruption"}
            ])
        },

        "ep06_amber_sex_neutral_talk_menu": {
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

        "ep06_mornwithamber_neutral_sexmenu": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "All options", "extra_text": "unlock different sex scenes. Choose all to see everything"}
            ])
        },

        "ep06_amber_neutral_climax_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": 2, "type": "Corruption"},
                {"option_num": 3, "char_name": "Amber", "points": 1, "type": "Corruption"}
            ])
        },

        "ep06_amber_corruption_postclim_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 1, "type": "Corruption"}
                    ]
                },
                {"option_num": 3, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        "ep06_amber_love_postclim_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 3, "char_name": "Amber", "points": 1, "type": "Love"}
            ])
        },

        "ep06_amber_neutral_postclim_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 3, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 1, "type": "Corruption"}
                    ]
                },
                {"option_num": 3, "char_name": "Amber", "points": -1, "type": "Love"}
            ])
        },

        "ep06_mornwithamber_corruption_sexmenu": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "All options", "extra_text": "unlock different sex scenes. Choose all to see everything"}
            ])
        },

        "ep06_amber_corruption_sex_menu": {
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

        "ep06_mornwithamber_love_sexmenu": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "All options", "extra_text": "unlock different sex scenes. Choose all to see everything"}
            ])
        },

        "ep06_amber_love_declaration_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 10, "type": "Love", "extra_text": "MILESTONE DECISION"},
                {"option_num": 2, "char_name": "Amber", "points": 7, "type": "Love"},
                {"option_num": 3, "char_name": "Amber", "points": 5, "type": "Love"}
            ])
        },

        # Madison Camera Scene - Round 1
        "ep06_madison_deepq_round1_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Both options", "extra_text": "cost 2 advantage points (requires ep06_mc_advantage_points >= 2)"}
            ])
        },

        "ep06_madison_response_round1_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "70% lie detection"}
            ])
        },

        # Madison Camera Scene - Round 2
        "ep06_madison_deepq_round2_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Both options", "extra_text": "cost 2 advantage points (requires ep06_mc_advantage_points >= 2)"}
            ])
        },

        "ep06_madison_response_round2_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "70% lie detection"}
            ])
        },

        # Madison Camera Scene - Round 3 (TRUE PATH - ep05_confrontation_peaceful == True)
        "ep06_madison_deepq_round3_true_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Both options", "extra_text": "cost 2 advantage points (requires ep06_mc_advantage_points >= 2)"}
            ])
        },

        # Madison Camera Scene - Round 3 (FALSE PATH - ep05_confrontation_peaceful == False)
        "ep06_madison_deepq_round3_false_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Both options", "extra_text": "cost 2 advantage points (requires ep06_mc_advantage_points >= 2)"}
            ])
        },

        "ep06_madison_response_round3_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "70% lie detection"}
            ])
        },

        "ep06_madison_response_round3_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "70% lie detection"}
            ])
        },

        "ep06_madison_nanami_knows_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "70% lie detection"}
            ])
        },

        "ep06_madison_why_left_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "70% lie detection"}
            ])
        },

        # Madison Camera Scene - Round 4
        "ep06_madison_deepq_round4_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Free question - no cost"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Costs 2 advantage points"}
            ])
        },

        "ep06_madison_deepq_round4_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Free question - no cost"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Costs 2 advantage points"}
            ])
        },

        # Madison Camera Scene - Round 5
        "ep06_madison_response_round5_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% lie detection"}
            ])
        },

        "ep06_madison_response_round5_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Honest answer - no lie detection"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "50% lie detection"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "70% lie detection"}
            ])
        },

        # Madison Camera Scene - CRITICAL DECISIONS
        "ep06_madison_critical_true_menu": {
            "madison": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Love",
                    "extra_text": "MILESTONE - Activates LOVE route with Madison"
                },
                {
                    "option_num": 2,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Corruption",
                    "extra_text": "MILESTONE - Activates CORRUPTION route with Madison"
                },
                {"option_num": 3, "char_name": "Madison", "extra_text": "Reject Madison - no stats gained"}
            ])
        },

        "ep06_madison_critical_false_menu": {
            "madison": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Love",
                    "extra_text": "MILESTONE - Activates LOVE route with Madison"
                },
                {
                    "option_num": 2,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Corruption",
                    "extra_text": "MILESTONE - Activates CORRUPTION route with Madison"
                },
                {"option_num": 3, "char_name": "Madison", "extra_text": "Reject Madison - no stats gained"}
            ])
        },

        # Madison Camera Scene - Round 6 (Final Round)
        "ep06_madison_finalq_round6_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Free question - no cost"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Costs 1 advantage point"}
            ])
        },

        "ep06_madison_finalq_round6_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Free question - no cost"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Costs 1 advantage point"}
            ])
        },

        # Madison Studio - Final Decision
        "ep06_madison_studio_decision_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Accept - go to Madison's studio"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Reject - decline Madison's invitation"}
            ])
        }
    }

    # Update main walkthrough data with Episode 6 content
    walkthrough_data.update(wt_data_ep06)
