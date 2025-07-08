init python:
    wt_data_ep05 = {
        # PART 1
        "ep05_ambcofmenu": {
            "amber": create_wt_text([
                {"option_num": 0, "char_name": "Important!", "extra_text": "A strike or clash with Amber gave you this rare scene... Chances to mend are few"},
                {"option_num": 1, "char_name": "Amber", "points": 4, "type": "Love", "extra_text": "Erases a strike"},
                {"option_num": 2, "char_name": "Amber", "points": -10, "type": "Love"}
            ])
        },

        "ep05_ambsexmenu": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 4, "type": "Corruption"},
                {"option_num": 2, "char_name": "Amber", "points": -4, "type": "Corruption"}
            ])
        },

        "ep05_isacheckmenu": {
            "isabella": create_wt_text([
                {"option_num": 1, "char_name": "Isabella", "points": 2, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Isabella",
                    "points": 4,
                    "type": "Love",
                    "additional_effects": [
                        {"points": -1, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 3,
                    "char_name": "Isabella",
                    "points": -1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep05_isacheckmenu2": {
            "isabella": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Isabella",
                    "points": 4,
                    "type": "Love",
                    "additional_effects": [
                        {"points": -1, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 2,
                    "char_name": "Isabella",
                    "points": -1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep05_isacheckmenu3": {
            "isabella": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Isabella",
                    "points": 4,
                    "type": "Love",
                    "additional_effects": [
                        {"points": -1, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 2,
                    "char_name": "Isabella",
                    "points": -1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep05_isacheckmenu4": {
            "isabella": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Isabella",
                    "points": 4,
                    "type": "Love",
                    "additional_effects": [
                        {"points": -1, "type": "Corruption"}
                    ]
                },
                {
                    "option_num": 2,
                    "char_name": "Isabella",
                    "points": -1,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                }
            ])
        },

        "ep05_2nd_elipst": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": -2, "type": "Love"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Love"}
            ])
        },

        "ep05_2nd_elipst2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": -2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Corruption"}
            ])
        },

        "ep05_2nd_elipst3": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -2, "type": "Love"}
            ])
        },

        "ep05_2nd_elipst4": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "extra_text": "Amber will witness this scene, becoming suspicious of Elizabeth's behavior toward you"},
                {"option_num": 2, "char_name": "Amber", "extra_text": "You'll reject this before Amber arrives. She won't see what Elizabeth was trying to do"}
            ])
        },

        "ep05_2nd_elishow": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Elizabeth", "extra_text": "Neutral response. No changes to Elizabeth's love/trust"},
                {"option_num": 3, "char_name": "Elizabeth", "points": 2, "type": "Corruption"}
            ])
        },

        "ep05_2nd_elishow2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Elizabeth", "extra_text": "Neutral response. No changes to Elizabeth's love/trust"},
                {"option_num": 3, "char_name": "Elizabeth", "points": 2, "type": "Corruption"}
            ])
        },

        "ep05_2nd_paz": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+10 Integrity to Darkness"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "+10 Integrity to Light"}
            ])
        },

        "ep05_2nd_mnbath": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "extra_text": "Observe from hiding to gather information about Madison's behavior"},
                {"option_num": 2, "char_name": "Nanami", "extra_text": "Confront Madison directly, but risk being dismissed before seeing her true intentions"}
            ])
        },

        "ep05_2nd_mnbath2": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "extra_text": "Secretly observe to see Madison's true intentions with Nanami"},
                {"option_num": 2, "char_name": "Nanami", "extra_text": "Step in and confront Madison about her manipulative behavior"}
            ])
        },

        "ep05_2nd_mnbath3": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": -10, "type": "Love",  "extra_text": "You will get a strike!"},
                {"option_num": 2, "char_name": "Nanami", "points": 10, "type": "Love"}
            ])
        },

        "ep05_hosnan_m1": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": -1, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": 1, "type": "Love"}
            ])
        },

        "ep05_hosnan_m2": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": 6, "type": "Love"},
                {"option_num": 2, "char_name": "Nanami", "points": -6, "type": "Love"}
            ])
        },

        "ep05_hosnan_m3": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": -2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Nanami", "points": 2, "type": "Corruption"}
            ])
        },

        "ep05_hosnan_m4": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": -2, "type": "Love"}
            ])
        },

        "ep05_hosnan_m5": {
            "nanami": create_wt_text([
                {"option_num": 1, "char_name": "Nanami", "points": -6, "type": "Love",  "extra_text": "You will get a strike!"},
                {"option_num": 2, "char_name": "Nanami", "points": -3, "type": "Love"},
                {"option_num": 3, "char_name": "Nanami", "points": 3, "type": "Love"}
            ])
        },

        "ep05_hosmad_m1": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 1, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": -2, "type": "Love",  "extra_text": "You will skip sex scenes!"}
            ])
        },

        "ep05_hosmad_m2": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": -2, "type": "Love"}
            ])
        },

        "ep05_hosmad_m3": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 4, "type": "Corruption"},
                {"option_num": 2, "char_name": "Madison", "points": 2, "type": "Corruption"}
            ])
        },

        "ep05_hosmad_m4": {
            "madison": create_wt_text([
                {"option_num": 1, "char_name": "Madison", "points": 5, "type": "Love"},
                {"option_num": 2, "char_name": "Madison", "points": -1, "type": "Love",  "extra_text": "You will get a strike!"}
            ])
        },

        "ep05_hospaz_m1": {
            "paz": create_wt_text([
                {
                    "option_num": 1,
                    "char_name": "Paz",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                },
                {"option_num": 2, "char_name": "Paz", "points": -2, "type": "Corruption"},
                {"option_num": 3, "char_name": "Paz", "points": 2, "type": "Love"}
            ])
        },

        "ep05_hosamb_m1": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Amber", "points": -2, "type": "Love"}
            ])
        },

        "ep05_hosamb_m2": {
            "amber": create_wt_text([
                {"option_num": 1, "char_name": "Amber", "points": 6, "type": "Love"},
                {
                    "option_num": 2,
                    "char_name": "Amber",
                    "points": 2,
                    "type": "Love",
                    "additional_effects": [
                        {"points": 4, "type": "Corruption"}
                    ]
                },
                {"option_num": 3, "char_name": "Amber", "points": -6, "type": "Love",  "extra_text": "You will get a strike and skip sex scenes!"}
            ])
        },

        "ep05_elid_m1": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 4, "type": "Love"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 2, "type": "Love"},
                {"option_num": 3, "char_name": "Elizabeth", "extra_text": "It won't change any score"}
            ])
        },

        "ep05_elid_m2": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "extra_text": "It won't change any score"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 1, "type": "Corruption"},
                {"option_num": 3, "char_name": "Elizabeth", "points": -1, "type": "Corruption"}
            ])
        },

        "ep05_elid_m3": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 1, "type": "Love"},
                {"option_num": 3, "char_name": "Elizabeth", "extra_text": "It won't change any score"}
            ])
        },

        "ep05_elid_m4": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": -1, "type": "Corruption"},
                {"option_num": 2, "char_name": "Elizabeth", "extra_text": "It won't change any score"},
                {"option_num": 3, "char_name": "Elizabeth", "points": -2, "type": "Corruption"}
            ])
        },

        "ep05_elid_m5": {
            "elizabeth": create_wt_text([
                {"option_num": 1, "char_name": "Elizabeth", "points": -1, "type": "Corruption"},
                {"option_num": 2, "char_name": "Elizabeth", "points": 1, "type": "Corruption"},
                {"option_num": 3, "char_name": "Elizabeth", "points": -2, "type": "Corruption"}
            ])
        },

        "ep05_mcmic_m1": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+5 Integrity to Darkness"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "It won't change any score"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+5 Integrity to Light"}
            ])
        },

        "ep05_mcmic_m2": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+8 Integrity to Darkness"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "It won't change any score"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+8 Integrity to Light"}
            ])
        },

        "ep05_mcmic_m3": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+10 Integrity to Darkness"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "It won't change any score"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+10 Integrity to Light"}
            ])
        },

        "ep05_mcmic_m4": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+12 Integrity to Darkness"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "It won't change any score"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+8 Integrity to Light"}
            ])
        },

#------end of wt data
    }

    # Update main walkthrough data with Episode 5 content
    walkthrough_data.update(wt_data_ep05)