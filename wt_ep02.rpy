init python:
    # Episode 2 walkthrough data using the improved helper function
    wt_data_ep02 = {
        # Initial Paz Fight Scene
        "ep02_mc_paz_fight_menu1": {
            "paz": create_wt_text([
                {"option_num": 1, "char_name": "Paz", "points": 2, "type": "Love"}  # Paz trust: 2 × 1.0 = 2
            ])
        },

        # Whore Scene Choice
        "ep02_whore_menu1": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+1 Integrity to Light"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "+1 Integrity to Darkness"}
            ])
        },

        # Arlette Host Scene
        "ep02_arlehost_menu1": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Love"}  # Arlette trust: 1 × 1.5 = 2
            ])
        },

        # Arlette Hotel Scenes
        "ep02_arlehotel_menu1": {
            "arlette": create_wt_text([
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Corruption"},  # Arlette cor: 1 × 1.5 = 2
                {"option_num": 3, "char_name": "Arlette", "points": 2, "type": "Corruption"}  # Arlette cor: 1 × 1.5 = 2
            ])
        },

        "ep02_arlehotel_menu2": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Corruption"}  # Arlette cor: 1 × 1.5 = 2
            ])
        },

        "ep02_arlehotel_menu3": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Corruption"},  # Arlette cor: 1 × 1.5 = 2
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Corruption"},
                {"option_num": 3, "char_name": "Arlette", "points": 2, "type": "Love"}  # Arlette trust: 1 × 1.5 = 2
            ])
        },

        # Arlette Sex Scenes
        "ep02_arlesex_menu1": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 5, "type": "Corruption", "extra_text": "Agree to anal sex with Arlette. Denying will skip the intimate scene"}
            ])
        },

        "ep02_arlesex_menu2": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Corruption"},  # Arlette cor: 1 × 1.5 = 2
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Love"}  # Arlette trust: 1 × 1.5 = 2
            ])
        },

        "ep02_arlesex_menu3": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Love"}  # Arlette trust: 1 × 1.5 = 2
            ])
        },

        "ep02_arlesex_menu4": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Corruption"},  # Arlette cor: 1 × 1.5 = 2
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Love"}
            ])
        },

        "ep02_arlesex_menu5": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Corruption"},
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Corruption"}  # Arlette cor: 1 × 1.5 = 2
            ])
        },

        # Revenge Choices
        "ep02_revenge_menu1": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+5 Integrity to Light. Walk away peacefully, avoiding the shootout"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "+5 Integrity to Darkness. Attack Hideo and trigger an intense shootout scene"}
            ])
        },

        "ep02_revenge_menu2": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness. ACHIEVEMENT: Unlocks 'Payback Time'"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"}
            ])
        },

        # Aftermath Scenes
        "ep02_aftermath_menu1": {
            "paz": create_wt_text([
                {"option_num": 1, "char_name": "Paz", "points": 2, "type": "Love"},
                {"option_num": 2, "char_name": "Paz", "points": 1, "type": "Love"}
            ])
        },

        "ep02_aftermath_menu2": {
            "paz": create_wt_text([
                {"option_num": 1, "char_name": "Paz", "points": 2, "type": "Love"},  # Paz trust: 2 × 1.0 = 2
                {"option_num": 2, "char_name": "Paz", "points": -2, "type": "Love"}  # Paz trust: -2 × 1.0 = -2
            ])
        },

        "ep02_aftermath_menu3": {
            "mc": create_wt_text([
                {"option_num": 1, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"},
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness"}
            ])
        },

        # Breakup Scene
        "ep02_breakup_menu1": {
            "arlette": create_wt_text([
                {"option_num": 1, "char_name": "Arlette", "points": 2, "type": "Love"},  # Arlette trust: 1 × 1.5 = 2
                {"option_num": 2, "char_name": "Arlette", "points": 2, "type": "Love"}  # Arlette trust: 1 × 1.5 = 2
            ]),
            "mc": create_wt_text([
                {"option_num": 2, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Light"},
                {"option_num": 3, "char_name": "[mc_name]", "extra_text": "+2 Integrity to Darkness"}
            ])
        },

        # Free Choice Scenes
        "ep02_pazmctits_menu": {
            "paz": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "is fine, it depends on what you want to reply"}
            ])
        },

        "ep02_sexwhorescene_menu": {
            "mc": create_wt_text([
                {"option_num": 0, "char_name": "Any option", "extra_text": "works, it's just about who you wanna have sex with"}
            ])
        }
    }

    # Update main walkthrough data with Episode 2 content
    walkthrough_data.update(wt_data_ep02)