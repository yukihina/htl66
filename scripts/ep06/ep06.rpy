label ep06_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ persistent.act2_play = True
    $ renpy.block_rollback()
    $ renpy.save_persistent()
    jump ep06_intro


label ep06_intro:
    scene eigengrau with clouds_inverse
    show location_tmpd_m with slowfade
    show tmpd_location zorder 2 with dissolve
    pause 4
    hide tmpd_location with dissolve
    jump ep06_ope


label ep06_ope:
    scene eigengrau
    show ep06_opening01
    mc_t "First day."
    mc_t "Nothing in the house is safe to say out loud anymore."

    show ep06_opening02
    mc_t "The badge weighs nothing."
    mc_t "Three months since the hospital."
    
    show ep06_opening03
    mc_t "Mother's wrists. Gauze. Pulse."
    mc_t "Three months of visiting hours."

    show ep06_opening04
    mc_t "She's awake now. Talking. Smiling at the nurses."
    mc_t "That smile. I know that smile."

    show ep06_opening05
    mc_t "Michael calls it 'remarkable progress.'"
    mc_t "Michael says a lot of things."

    show ep06_opening06
    wat "Ah. Inspector..."
    wat "...Crawford-san. Yes."
    wat "Sit, sit. Coffee?"
    mc_s "I'm fine, thank you."
    wat "The transfer paperwork mentioned Osaka."
    wat "Quite a commendation record."

    show ep06_opening07
    wat "Before the... incident."
    mc_s "I've recovered."

    show ep06_opening08
    wat "Of course, of course."
    wat "Crawford. That's... English?"
    mc_s "My father's name."
    wat "I see."

    show ep06_opening09
    wat "Detective Yamamoto. Found dead last night. Professional execution - three shots, precise spacing. Very... un-Japanese in its directness."
    mc_t "Foreign killer. Foreign detective. He's already building a file with me."
    mc_s "Yakuza work?"
    wat "That's what you'll determine."
    wat "Detective Inspector Sato from Organized Crime requested you specifically."
    mc_s "Why me?"
    wat "Osaka connections, perhaps."
    wat "Sato believes your... **background**... provides unique perspective."
    wat "Yakuza clans are traditional. Conservative. They don't adapt well to..."
    wat "...modern Tokyo's 'diversity'."

    show ep06_opening10
    mc_t "Diversity. That's what we're calling it now."
    wat "Of course, **we** value all contributions to the department."

    menu:
        "I'll do this right.":
            mc_t "I'll investigate thoroughly. Professional standards still matter."
        "I wasn't ready for this.":
            mc_t "Three months wasn't enough recovery time for this kind of case."
        "Perfect. Time for payback.":
            mc_t "Good. I've got unfinished business with those bastards anyway."

    show ep06_opening11
    wat "He's at the scene. Don't keep him waiting."

    show ep06_opening12
    mc_t "Osaka. It follows me like a bullet I can never hear coming."
    jump ep06_operative


label ep06_operative:
    scene eigengrau with clouds_inverse
    show days_before
    pause 3
    show location_kabuchikotower_n with slowfade
    show kabukicho_night zorder 2 with dissolve
    pause 4
    hide kabukicho_night with dissolve
    jump ep06_shadow


label ep06_shadow:
    scene eigengrau
    show ep06_shadowdir01
    hir "The Osaka detective."
    hir "He's in Tokyo now."
    anto "I know."
    hir "Stationary. Predictable. Comfortable."
    hir "Three months of watching him settle in. Build routines."
    hir "Now he's vulnerable."

    show ep06_shadowdir02
    hir "Yamamoto. Asagaya, Suginami-ku."
    hir "Second floor. Apartment 204."
    anto "Security?"

    show ep06_shadowdir03
    hir "None. Lives alone. Works late Thursdays."
    hir "Returns home past midnight. Drunk, usually. Keys in left pocket."
    anto "Why him?"

    show ep06_shadowdir04
    hir "He's connecting dots. Osaka to Tokyo. Surgical modifications, territory shifts, missing women."
    hir "Last week he requested files on Kudo-kai specifically."

    show ep06_shadowdir05
    hir "Smart detective. Dangerous detective."
    hir "You play chess, Antonella?"

    show ep06_shadowdir06
    anto "No."
    hir "You should learn."
    hir "Chess teaches you how to win wars."

    show ep06_shadowdir07
    hir "You don't attack the king directly. Too obvious. Too defended."
    hir "You remove his pieces. One by one."
    hir "First the knights. Then the bishops. Then the rooks."
    hir "When the king is alone and blind..."

    show ep06_shadowdir08
    hir "...he falls without a fight."
    hir "Yamamoto is a knight. Intelligent. Mobile. Dangerous."
    anto "And after the knight falls?"
    hir "The board shifts. Tokyo Metropolitan loses its best investigator."

    show ep06_shadowdir09
    hir "Yamaguchi-gumi, Sumiyoshi-kai, Inagawa-kai, all the old families - they think this is random violence. Gang war."
    hir "They don't see the pattern. They don't see me moving pieces."

    show ep06_shadowdir10
    anto "And after Yamamoto?"
    hir "Other pieces. Bishops, rooks."
    hir "The game takes time, Antonella. Patience."
    anto "I'm patient."
    anto "The more pieces removed, the clearer the board becomes."
    hir "Exactly. Your precision makes this possible."
    anto "Then I won't disappoint you."

    show ep06_shadowdir11
    hir "Thursday night. Apartment 204. Three shots."
    anto "Professional spacing."
    hir "Obvious yakuza signature. Impossible to trace to Kudo-kai."

    show ep06_shadowdir12
    anto "Thursday night. Apartment 204."
    anto "Three shots. Professional spacing."
    anto "The knight falls."

    show ep06_shadowdir13
    anto "The board shifts."
    jump ep06_executiontitle


label ep06_executiontitle:
    scene eigengrau with clouds_inverse
    show location_asagaya_n with slowfade
    show asagaya zorder 2 with dissolve
    pause 4
    hide asagaya with dissolve
    jump ep06_execution


label ep06_execution:
    scene eigengrau
    show ep06_execution01
    yam_t "Seventeen women. Seventeen families asking when I'll find answers."
    yam_t "Surgical chest incisions. Professional precision. Osaka to Tokyo - someone's expanding operations."

    show ep06_execution02
    yam_t "11:43 PM. Miyuki called three hours ago. Sounded tired. I told her two more days in Tokyo."
    yam_t "Lied. Probably four more days. Maybe five."
    yam_t "But I'm close. The connection between Osaka and Tokyo - it's here somewhere in these files."

    show ep06_execution03
    yam_t "11:47 PM."
    yam_t "Three knocks. Polite. Soft."
    yam_t "Neighbor? Building manager?"
    yam_t "This late?"

    show ep06_execution04
    yam_t "Delivery driver."

    show ep06_execution05
    yam_t "Young."

    show ep06_execution06
    yam_t "European features: Black hair, pale, blue eyes with glasses."

    show ep06_execution07
    yam_t "Curves straining fabric. Wrong size. Abdomen scar visible. Work accident, maybe."

    show ep06_execution08
    yam_t "Late shift worker. Probably part-time student."
    yam_t "Delivery for Yamamoto-san. Signature required."
    yam_t "Light accent. Foreign worker."
    yam_t "Wrong apartment probably. Common mistake with Japanese names."

    show ep06_execution09
    yam "I think you have the wrong—"
    anto "Yamamoto-san? Detective Yamamoto Koji?"
    yam "...Yes?"
    yam_t "She knows I'm a detective. How?"
    yam_t "Sender must have specified. Precinct sometimes sends-"

    show ep06_execution10
    yam_t "European."

    show ep06_execution11
    yam_t "Osaka."

    show ep06_execution12
    yam_t "Miyuk—"

    show ep06_execution13
    anto_t "Professional spacing."
    anto_t "The knight falls."

    show ep06_execution14
    anto_t "Wedding ring on his finger."
    anto_t "Doesn't matter."
    anto_t "Package. Take it."
    anto_t "Thirty seconds. Exit clean."
    jump ep06_crimescene


label ep06_crimescene:
    scene eigengrau
    show ep06_crimescene01
    mc_t "First day back. First crime scene in three months."

    show ep06_crimescene02
    mc_t "The last crime scene I was at, I was the one bleeding."

    show ep06_crimescene03
    mc_t "Second floor. Apartment 204."
    mc_t "Three evidence markers. Must be the shell casings."
    mc_t "Gray-haired man by the bullets. Wire-rim glasses. That's Detective Inspector Sato."

    show ep06_crimescene04
    tak "Inspector Crawford? [mc_name]?. I'm..."
    mc_s "Detective Inspector Sato."
    tak "Just Takeo. Look at these casings."
    tak "Nine millimeter. Professional grade ammunition."
    tak "Three shots. Chest, chest, head."
    tak "The shooter knew exactly what they were doing."
    mc_t "No handshake. No pleasantries. Straight to the evidence."
    mc_t "My kind of cop."
    mc_s "Professional hit?"
    tak "Yes. But look at the arrangement."
    tak "Triangular pattern. Even spacing between each casing."
    tak "Someone positioned these after firing. Why?"
    mc_s "Signature?"
    tak "Or they were following very specific instructions."
    tak "Three shots. Three decisions. Three certainties."
    tak "Come. I'll show you where he fell."

    show ep06_crimescene05
    tak "Yamamoto Koji. Forty-two years old. Fifteen-year veteran. Organized Crime Division."
    tak "Very careful. Very paranoid. Investigating yakuza operations."
    tak "He opened his door late at night to a stranger."

    show ep06_crimescene06
    mc_t "Yamamoto... I saw his personnel file this morning."
    mc_t "Married. Two kids, studying overseas. From Osaka originally."

    show ep06_crimescene07
    tak "The question is why. Why would a paranoid detective investigating dangerous criminals open his door after midnight?"
    mc_s "He saw someone through the peephole who didn't look threatening."
    tak "Exactly. Someone who fit a safe profile."
    tak "Delivery worker. Building maintenance. Perhaps a woman."
    tak "Someone he dismissed as harmless."
    mc_t "I would have opened the door too."
    mc_t "That's the scary part."

    show ep06_crimescene08
    tak "You know why Captain Watanabe assigned you to this case?"
    mc_s "My experience with yakuza organizational patterns in Osaka."
    tak "Partially. Also because neither of us belongs here."
    tak "The department doesn't trust you because you're a gaijin. They don't trust me because I don't follow their rules."
    tak "That makes us useful for cases like this."
    mc_t "Useful. That's one way to put it."
    mc_t "Expendable is another."

    show ep06_crimescene09
    tak "What do you see?"
    mc_t "Nine millimeter casings. Three of them."
    mc_t "Arranged in a perfect triangle. Someone took time to do this."
    mc_t "Fuck! My wound aches. The scar tissue pulls when I crouch like this."
    mc_s "Controlled shooting. No panic. The triangular arrangement suggests the killer stayed calm after firing."
    tak "Yes. Professional methodology."
    tak "But I want to know something else, Inspector Crawford."

    show ep06_crimescene10
    tak "What kind of person kills a police officer, then stays at the crime scene to arrange shell casings in a geometric pattern?"
    mc_s "That depends on how you look at it."

    menu:
        "They believed in justice.":
            mc_s "Someone who believes they're serving a higher purpose. Justice, even if it's wrong."
        "Just following orders.":
            mc_s "Someone doing a job. Following orders. No emotion involved."
        "They enjoyed the kill.":
            mc_s "Someone who enjoys it. The killing and the art of it."

    tak "We're hunting someone very dangerous."
    tak "Come. Look at the victim's position."

    show ep06_crimescene11
    mc_t "Blood. Dried now. Dark brown against the cheap vinyl."
    mc_t "Yamamoto bled out here. On this floor. Alone."
    mc_t "The smell is still here. Copper and cleaning chemicals."
    tak "No defensive wounds. No signs of struggle."
    tak "The first shot hit him in the chest while he was standing, facing the door."
    tak "Never tried to block."
    mc_s "He didn't have time to react."
    tak "Or he didn't recognize the threat until it was too late."
    tak "Look at the blood spatter. First shot, he's standing. Second shot, he's falling backward."
    tak "Third shot hit his head while he was already going down."
    tak "All three shots within seconds. The shooter fired rapidly."
    mc_s "Speed over precision. They wanted to finish before he could scream."
    tak "Yes. Now come look at what Yamamoto was working on when he died."

    show ep06_crimescene12
    mc_t "The outline looks too small. Bodies always look smaller after death."
    mc_t "Yamamoto had a family. A wife in Osaka. Kids."
    mc_t "Now he's just chalk and dried blood."
    tak "Time of death was probably around 11:52 PM according to the preliminary coroner's report."
    tak "A neighbor reported hearing what sounded like firecrackers at 11:47 PM."
    tak "Five-minute response delay from sound to death."
    mc_s "Fast kill. Professional execution."
    tak "Yes. But execution implies punishment. Judgment."
    tak "Was Yamamoto being punished? Or was he simply eliminated because he knew too much?"
    mc_s "What was he investigating exactly?"
    tak "That's what I want to show you."

    show ep06_crimescene13
    tak "Yamamoto was investigating a series of murders. Seventeen women over three months."
    tak "All found with post-mortem surgical incisions in the same location."
    tak "Breast tissue removed. Look at these photographs."

    show ep06_crimescene14
    mc_t "Bodies. Female. Surgical cuts."

    call screen confirm(
        message="Gore content ahead. Continue?",
        yes_action=SetVariable("e6_gore", True),
        no_action=SetVariable("e6_gore", False)
    )

    if e6_gore:
        show ep06_crimescene15
        tak "Three months ago. First victim. Look at the surgical incision."
        mc_t "Clean at first..."
        mc_t "Precise. Professional medical work."

        show ep06_crimescene16
        tak "Two months ago. Third victim."
        mc_t "Then rougher..."
        mc_t "Less careful."

        show ep06_crimescene17
        tak "Last week. Most recent victim."
        mc_t "Then butchered."
        mc_t "Hack job. Whoever did this was either in a hurry or didn't care anymore."
        mc_s "The quality degraded. Surgical precision to crude butchery."
        mc_t "I've seen bodies before. But these..."

    else:
        tak "Three months ago. First victim. Look at the surgical incision."
        mc_t "Clean cut. Precise. Professional medical work."
        tak "Two months ago. Third victim."
        mc_t "Rougher. Less careful."
        tak "Last week. Most recent victim."
        mc_t "Butchered. Hack job. Whoever did this was either in a hurry or didn't care anymore."
        mc_s "The quality degraded. Surgical precision to crude butchery."
        mc_t "I've seen bodies before. But these..."

    show ep06_crimescene18
    mc_s "You think it's organ harvesting?"
    tak "That's what I thought initially. But breast tissue has no black market value."
    tak "No transplant demand. No medical use."
    tak "So why remove it?"
    mc_s "Something inside the tissue. The implants."
    tak "Yes. Modified silicone implants with sealed compartments."
    tak "These women were human cargo vessels. Contraband surgically implanted in their bodies."
    tak "Harder to detect than swallowing packages. More permanent. More reliable."
    mc_s "Seventeen women. Osaka to Tokyo."
    mc_s "Someone's expanding their smuggling operation."
    tak "That's what Yamamoto discovered. The connection between Osaka and Tokyo."
    tak "The expansion pattern. The surgical modifications."
    mc_t "Osaka. Always Osaka."
    mc_s "But something doesn't make sense."
    mc_s "If these women were valuable cargo vessels, why kill them? Why not extract the contraband and use them again?"
    tak "That's the question that got Yamamoto killed."
    tak "He was investigating why the organization started murdering their own mules."
    tak "Look at this timeline."

    show ep06_crimescene19
    tak "Something changed in the operation."
    tak "More volume. Less time. More pressure."
    tak "Or perhaps the person in charge is losing control."
    mc_s "Yamamoto noticed this pattern. Connected the degradation to the Osaka-Tokyo expansion."
    tak "Yes. And that connection threatened someone important enough to order a police officer's assassination."
    tak "Someone with resources. Organization. Professional killers."
    tak "But here's what troubles me most, [mc_name]."
    mc_t "He's testing me. Seeing how I think."
    tak "We have seventeen dead women who were valuable assets."
    tak "We have degrading operational quality suggesting organizational stress."
    tak "We have a detective murdered for discovering the connection."
    mc_s "And we have a killer who arranges shell casings in triangles."
    tak "Yes. So tell me. What kind of organization are we dealing with?"
    tak "Not tactically. Not structurally."
    tak "Morally. What kind of people do this?"

    menu:
        "Stop them legally.":
            mc_s "People who've lost sight of any moral line. They need to be stopped through proper legal process."

        "Just catch them.":
            mc_s "Criminals doing criminal things. The brutality doesn't matter. What matters is catching them."

        "They deserve everything.":
            mc_s "Monsters. The kind who deserve whatever happens to them when we find them."
    
    tak "I wanted to hear your answer."
    tak "Because the way we see them determines how we hunt them."

    show ep06_crimescene20
    tak "The autopsy results will be ready this afternoon."
    tak "Dr. Hatanaka from forensics. The body will tell us what the crime scene cannot."
    tak "Ballistics. Trajectory. Exact time of death."
    tak "Until then, we have three shell casings arranged in a triangle."
    tak "Three rapid shots."
    tak "Seventeen dead women with modified implants."
    tak "And one central question: why kill your own cargo vessels?"
    mc_s "Where do we start?"
    tak "We start with the autopsy. Then we start asking questions."
    tak "Yamamoto asked the right questions and died for it."
    tak "We'll ask the same questions."
    tak "But perhaps we'll be more careful about who hears the answers."
    mc_t "Careful. Right."
    mc_t "Because the person who killed Yamamoto is still out there."
    mc_t "Calm enough to arrange shell casings after murder."
    mc_t "Professional enough to kill a cop and walk away."
    jump ep06_mornintro


label ep06_mornintro:
    scene eigengrau with clouds_inverse
    show location_denenchofu_m with slowfade
    show home_location zorder 2 with dissolve
    pause 4
    hide home_location with dissolve
    jump ep06_mornwithamber


label ep06_mornwithamber:
    scene eigengrau
    show ep06_ambermorn01
    pause

    show ep06_ambermorn02
    mc_s "Shit..."

    show ep06_ambermorn03
    amb "No."
    mc_s "Amber, I have—"
    mc_t "That look. Fuck."
    amb "I said no. You're not going anywhere."

    show ep06_ambermorn04
    amb "Haah..."

    show ep06_ambermorn05
    mc_s "The case—"
    amb "Shut up and feel this."
    mc_t "I should stop. I can't. God, I can't."

    menu:
        "Show me." if amber_strikes == 0 and rm.get("amber", "cor") >= 10:
            mc_s "Show me what you were doing."

            $ e6_amber_path = "corruption"
            jump ep06_mornwithamber_corruption
        
        "You're impossible.":
            mc_s "You're impossible."

        "I missed this.":
            mc_s "I missed this too."
            
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            
        "Not now.":
            mc_s "I can't. Not now."

            $ e6_amber_path = "rejection"
            $ ss.add("amber", "strike")
            $ amber_strikes = ss.get("amber", "strike")
            if amber_strikes == 1:
                $ show_custom_notification("strike1")
            elif amber_strikes == 2:
                $ show_custom_notification("strike2")
            elif nanami_strikes >= 3:
                $ show_custom_notification("strike3")
            jump ep06_mornwithamber_rejection

    show ep06_ambermorn06
    amb "This scar..."
    mc_s "What about it?"

    show ep06_ambermorn07
    amb "It's so fucking hot."
    mc_t "She sees the worst parts and wants them."

    menu:
        "You see me." if amber_strikes == 0 and rm.get("amber", "trust") >= 33:
            mc_s "You've always seen me."

            $ e6_amber_path = "love"
            jump ep06_mornwithamber_love

        "You like broken things?":
            mc_s "You like broken things?"

            $ e6_amber_path = "neutral"
            jump ep06_mornwithamber_neutral

        "Like the view?":
            mc_s "Like what you see?"

            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)
            $ e6_amber_path = "neutral"
            jump ep06_mornwithamber_neutral



label ep06_mornwithamber_neutral:
    show ep06_ambermorn08
    amb "God... wait—"
    mc_s "Too much?"
    amb "No. Just... slow at first."
    mc_s "Like this?"
    amb "Yeah. Fuck, yeah. Now don't stop."

    show ep06_ambermorn09
    amb "Mmm..."
    mc_t "Say it. She needs to hear it."
    amb "Tell me..."

    menu:
        "I love you.":
            mc_s "I love you, Amber."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "Fucking perfect.":
            mc_s "Your pussy's perfect."
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)

        "Only you.":
            mc_s "No one else compares."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)

    show ep06_ambermorn10
    amb "Look at me."
    mc_s "I am."
    amb "No one else gets this."

    show ep06_ambermorn11
    amb "You watching?"
    mc_s "Can't look away."
    amb "Good. Now what do you want? And don't say 'whatever you want'—that's such a cop-out."
    mc_s "Since when do you give me choices?"
    amb "Since I'm feeling generous. Don't waste it."


label ep06_mornwithamber_neutral_sexmenu:
    menu:
        amb "Tell me what you want..."
        "Come here." if not e6_amber_neutral_blowjob_seen:
            mc_s "Come here."
            $ e6_amber_neutral_blowjob_seen = True
            jump ep06_mornwithamber_neutral_blowj
        
        "Let me see all of you." if not e6_amber_neutral_boobjob_seen:
            mc_s "Let me see all of you."
            $ e6_amber_neutral_boobjob_seen = True
            jump ep06_mornwithamber_neutralboobj
        
        "Keep going." if e6_amber_neutral_blowjob_seen and e6_amber_neutral_boobjob_seen:
            mc_s "Keep going."
            jump ep06_mornwithamber_neutral_continue


label ep06_mornwithamber_neutral_blowj:
    show ep06_ambermorn12
    mc_s "Open your mouth."
    amb "Mmm..."
    amb "I want to taste us."

    show ep06_anim01
    mc_s "That's it..."
    amb "Mmph..."

    show ep06_anim02
    mc_s "Just like that..."
    amb "Mmm..."

    show ep06_ambermorn13
    amb "More?"
    mc_t "If she keeps going, I'll lose it."
    mc_s "Enough. Get up here."
    jump ep06_mornwithamber_neutral_sexmenu


label ep06_mornwithamber_neutralboobj:
    show ep06_ambermorn14
    amb "Shh..."

    show ep06_ambermorn15
    mc_s "Look at you..."
    amb "Use them."

    show ep06_anim03
    amb "Mmm..."

    show ep06_anim04
    mc_s "Fuck..."

    show ep06_ambermorn16
    mc_s "Amber, I'm—"
    amb "Not yet."
    jump ep06_mornwithamber_neutral_sexmenu


label ep06_mornwithamber_neutral_continue:
    show ep06_ambermorn17
    amb "You know why this works?"
    mc_s "Why?"
    amb "Because I know your darkness, [mc_name]."
    mc_s "And you're insane."
    amb "We both are."
    mc_t "God, she's right. We're both fucking insane."

    menu:
        "Only you get me.":
            mc_s "You're the only one who understands."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "Take it all.":
            mc_s "Then take all of it."
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)

        "Broken together.":
            mc_s "Maybe we're both exactly as fucked up as we need to be."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

    show ep06_ambermorn18
    pause
    show ep06_ambermorn19
    pause
    show ep06_ambermorn20
    pause
    show ep06_ambermorn21
    pause
    show ep06_ambermorn22
    pause
    show ep06_ambermorn23
    pause
    show ep06_ambermorn24
    pause
    show ep06_ambermorn25
    pause
    show ep06_ambermorn26
    pause
    show ep06_ambermorn27
    pause
    show ep06_ambermorn28
    pause
    show ep06_ambermorn29
    pause
    show ep06_ambermorn30
    pause
    show ep06_ambermorn31
    pause
    show ep06_ambermorn32
    pause
    show ep06_ambermorn33
    pause
    show ep06_ambermorn34
    pause
    show ep06_ambermorn35
    pause
    show ep06_ambermorn36
    pause
    show ep06_ambermorn37
    pause
    show ep06_ambermorn38
    pause
    show ep06_ambermorn39
    pause
    show ep06_ambermorn40
    pause
    show ep06_ambermorn41
    pause
    show ep06_ambermorn42
    pause
    show ep06_ambermorn43
    pause
    show ep06_ambermorn44
    pause
    show ep06_ambermorn45
    pause
    show ep06_ambermorn46
    pause
    show ep06_ambermorn47
    pause
    show ep06_ambermorn48
    pause
    show ep06_ambermorn49
    pause
    show ep06_ambermorn50
    pause
    show ep06_ambermorn51
    pause
    show ep06_ambermorn52
    pause
    show ep06_ambermorn53
    pause
    show ep06_ambermorn54
    pause
    show ep06_ambermorn55
    pause
    show ep06_ambermorn56
    pause
    show ep06_ambermorn57
    pause
    show ep06_ambermorn58
    pause
    show ep06_ambermorn59
    pause
    show ep06_ambermorn60
    pause
    show ep06_ambermorn61
    pause
    show ep06_ambermorn62
    pause
    show ep06_ambermorn63
    pause
    show ep06_ambermorn64
    pause
    show ep06_ambermorn65
    pause
    show ep06_ambermorn66
    pause
    show ep06_ambermorn67
    pause
    show ep06_ambermorn68
    pause
    show ep06_ambermorn69
    pause
    show ep06_ambermorn70
    pause
    show ep06_ambermorn71
    pause
    show ep06_ambermorn72
    pause
    show ep06_ambermorn73
    pause
    show ep06_ambermorn74
    pause
    show ep06_ambermorn75
    pause
    show ep06_ambermorn76
    pause
    show ep06_ambermorn77
    pause
    show ep06_ambermorn78
    pause
    show ep06_ambermorn79
    pause
    show ep06_ambermorn80
    pause