init python:
    wt_data_ep06 = {
        # MC Case Investigation Choices
        "ep06_case_attitude_menu": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+1 Integrity to Light"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Neutral response, no integrity change"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+1 Integrity to Darkness"}
            ])
        },

        "ep06_killer_profile_menu": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Neutral response, no integrity change"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness"}
            ])
        },

        "ep06_criminal_vision_menu": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "Neutral response, no integrity change"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness"}
            ])
        },

        # Amber Morning Scenes
        "ep06_amber_first_decision_menu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "extra_text": "Corruption path (requires high corruption with Amber and a good relationship)"
                },
                {"option_num": 2, "char_name": "Amber", "extra_text": "Playful response, no stat changes"},
                {"option_num": 3, "char_name": "Amber", "points": 2, "type": "Love"},
                {
                    "option_num": 4,
                    "char_name": "Amber",
                    "extra_text": "You will get a strike! Too many strikes will severely damage your relationship"
                }
            ])
        },

        "ep06_amber_intimacy_response_menu": {
            "amber": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Amber",
                    "extra_text": "Love path (requires high trust with Amber and a good relationship)"
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
                {"option_num": 0, "char_name": "All options", "extra_text": "unlock different sex scenes with Amber. Explore all to see everything"}
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
                {"option_num": 0, "char_name": "All options", "extra_text": "unlock different sex scenes with Amber. Explore all to see everything"}
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
                {"option_num": 0, "char_name": "All options", "extra_text": "unlock different intimate scenes with Amber. Explore all to see everything"}
            ])
        },

        "ep06_amber_love_declaration_menu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 10, "type": "Love", "extra_text": "Very important choice! Highest love gain"},
                {"option_num": 2, "char_name": "Amber", "points": 7, "type": "Love"},
                {"option_num": 3, "char_name": "Amber", "points": 5, "type": "Love"}
            ])
        },

        # Madison Camera Scene - Round 1
        "ep06_madison_deepq_round1_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Lie Detection", "extra_text": "Lies give Advantage pts if undetected. Use Advantage to ask deeper questions"},
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_response_round1_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        # Madison Camera Scene - Round 2
        "ep06_madison_deepq_round2_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Lie Detection", "extra_text": "Lies give Advantage pts if undetected. Use Advantage to ask deeper questions"},
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_response_round2_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        # Madison Camera Scene - Round 3 (Peaceful path from Episode 5)
        "ep06_madison_deepq_round3_true_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Lie Detection", "extra_text": "Lies give Advantage pts if undetected. Use Advantage to ask deeper questions"},
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        # Madison Camera Scene - Round 3 (Conflict path from Episode 5)
        "ep06_madison_deepq_round3_false_menu": {
            "madison": create_wt_text([
                {"option_num": 0, "char_name": "Lie Detection", "extra_text": "Lies give Advantage pts if undetected. Use Advantage to ask deeper questions"},
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_response_round3_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_response_round3_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_nanami_knows_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_why_left_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Corruption", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "points": 2, "type": "Corruption", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        # Madison Camera Scene - Round 4
        "ep06_madison_deepq_round4_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Safe question to ask"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Deeper question, costs points to ask"}
            ])
        },

        "ep06_madison_deepq_round4_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Safe question to ask"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "More personal question, costs points to ask"}
            ])
        },

        # Madison Camera Scene - Round 5
        "ep06_madison_response_round5_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "+Advantage if undetected (30%)"}
            ])
        },

        "ep06_madison_response_round5_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Truth - no Advantage"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "+Advantage if undetected (50%)"},
                {"option_num": 3, "char_name": "Madison", "extra_text": "+Advantage if undetected (30%)"}
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
                    "extra_text": "Very important! Opens romantic path with Madison"
                },
                {
                    "option_num": 2,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Corruption",
                    "extra_text": "Very important! Opens corruption path with Madison"
                },
                {"option_num": 3, "char_name": "Madison", "extra_text": "Will decline Madison's advances"}
            ])
        },

        "ep06_madison_critical_false_menu": {
            "madison": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Love",
                    "extra_text": "Very important! Opens romantic path with Madison"
                },
                {
                    "option_num": 2,
                    "char_name": "Madison",
                    "points": 10,
                    "type": "Corruption",
                    "extra_text": "Very important! Opens corruption path with Madison"
                },
                {"option_num": 3, "char_name": "Madison", "extra_text": "Will decline Madison's advances"}
            ])
        },

        # Madison Camera Scene - Round 6 (Final Round)
        "ep06_madison_finalq_round6_true_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "General question, free to ask"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "More personal question, costs a point to ask"}
            ])
        },

        "ep06_madison_finalq_round6_false_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Simple question, no cost"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Deeper question, requires a point to ask"}
            ])
        },

        # Madison Studio - Final Decision
        "ep06_madison_studio_decision_menu": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "extra_text": "Accept her invitation and go to her studio"},
                {"option_num": 2, "char_name": "Madison", "extra_text": "Decline her invitation. This will significantly affect your relationship"}
            ])
        }
    }

    # Update main walkthrough data with Episode 6 content
    walkthrough_data.update(wt_data_ep06)