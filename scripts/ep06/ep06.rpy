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
    $ ss.add("amber", "blowjob")
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
    $ ss.add("amber", "titjob")
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
    $ ss.add("amber", "sex")
    amb "Yes..."
    mc_s "Like this?"
    amb "Don't stop."

    show ep06_anim06
    amb "Fuck... fuck... fuck..."

    show ep06_anim05
    amb "Ah... ah... ah..."

    show ep06_ambermorn19
    amb "Inside... I want—"
    mc_s "We don't have to—"
    amb "I want to. Please."
    mc_s "Tell me if—"
    amb "I will. Now fuck me."

    show ep06_ambermorn20
    $ ss.add("amber", "creampie")
    amb "Mmm..."
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_postclimax:
    show ep06_ambermorn21
    if e6_amber_path == "corruption":
        amb "You think I'm fucked up?"
        mc_s "For wanting that?"
        amb "For needing it."
        amb "Every time... I worry you'll see me different."
        mc_s "I see you exactly as you are."
        amb "And that doesn't scare you?"
        
        menu:
            "You don't scare me.":
                mc_s "Nothing about you scares me."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "We fit perfectly.":
                mc_s "We're both exactly what we need to be."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                $ rm.update("amber", "cor", 2)
                $ check_levels("amber", "cor", 2)

            "Stop overthinking.":
                mc_s "You think too much."
                $ rm.update("amber", "trust", -1)
                $ check_levels("amber", "trust", -1)
        
        jump ep06_mornwithamber_ending

    elif e6_amber_path == "love":
        amb "I'm scared."
        mc_s "Of what?"
        amb "Losing this."
        mc_s "You won't."
        amb "How do you know?"
        mc_s "Because I choose you. Every day."
        amb "Even when I'm..."
        mc_s "Especially then."

        menu:
            "I mean it.":
                mc_s "I know exactly what I'm saying."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "Test me.":
                mc_s "Try me. Test it. I'm still here."
                $ rm.update("amber", "trust", 2)
                $ check_levels("amber", "trust", 2)

            "Help me understand.":
                mc_s "Then tell me. Help me understand."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
        
        jump ep06_mornwithamber_ending

    elif e6_amber_path == "neutral":
        amb "You remember... when I cut and dyed my hair?" 
        
        show ep06_ambermorn22
        mc_s "Yeah."
        mc_t "I still remember she looked like a boy."
        amb "You said I looked like a warrior."
        mc_s "You did."

        show ep06_ambermorn23
        amb "No one else said that. I mean... everyone else just looked at me like I'd—like I'd ruined something."

        menu:
            "Perfect to me.":
                mc_s "You've always been perfect to me."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "Warriors together.":
                mc_s "We're both warriors now."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                $ rm.update("amber", "cor", 2)
                $ check_levels("amber", "cor", 2)

            "Time to go.":
                mc_s "We should get ready."
                $ rm.update("amber", "trust", -1)
                $ check_levels("amber", "trust", -1)
        
        jump ep06_mornwithamber_ending


label ep06_mornwithamber_ending:
    show ep06_ambermorn24
    amb "This pussy owns you."
    mc_s "Pretty sure that's not how ownership works."
    amb "It is now. Any objections, Detective?"
    mc_s "...No ma'am."
    amb "That's what I thought."
    mc_t "She always needs the last word. I'm not complaining."
    jump ep06_madisonintro


label ep06_mornwithamber_corruption:
    show ep06_ambermorn25
    amb "You want a show?"
    mc_s "Every detail."
    amb "Pervert."

    show ep06_ambermorn26
    amb "Started here..."
    mc_s "Keep going."
    amb "Thinking about your tongue."

    show ep06_ambermorn27
    amb "Then deeper..."
    mc_s "Show me."
    amb "Like this..."

    show ep06_ambermorn28
    mc_s "What were you imagining?"
    amb "You... using me..."
    mc_s "How?"
    amb "However you want."
    mc_t "Look at her. She fucking loves this."

    show ep06_ambermorn29
    amb "Fuck..."

    show ep06_ambermorn30
    amb "Please..."
    mc_s "Please what?"
    amb "Fuck me."


label ep06_mornwithamber_corruption_sexmenu:
    menu:
        amb "What do you want from me?"
        
        "Use your mouth." if not e6_amber_cor_blowjob_seen:
            mc_s "Use your mouth."
            $ e6_amber_cor_blowjob_seen = True
            jump ep06_mornwithamber_cor_blowjob
        
        "Your tits. Now." if not e6_amber_cor_boobjob_seen:
            mc_s "Your tits. Now."
            $ e6_amber_cor_boobjob_seen = True
            jump ep06_mornwithamber_cor_boobjob
        
        "Turn around." if not e6_amber_cor_assjob_seen:
            mc_s "Turn around."
            $ e6_amber_cor_assjob_seen = True
            jump ep06_mornwithamber_cor_assjob
        
        "On your knees." if not e6_amber_cor_footjob_seen:
            mc_s "On your knees."
            $ e6_amber_cor_footjob_seen = True
            jump ep06_mornwithamber_cor_footjob
        
        "Spread your legs." if (e6_amber_cor_blowjob_seen and e6_amber_cor_boobjob_seen and 
                                e6_amber_cor_assjob_seen and e6_amber_cor_footjob_seen):
            mc_s "Spread your legs."
            jump ep06_mornwithamber_cor_continue


label ep06_mornwithamber_cor_blowjob:
    show ep06_ambermorn31
    mc_s "All the way."
    amb "Mmph..."
    mc_s "Take it."

    show ep06_anim07
    mc_s "Good girl."

    show ep06_ambermorn32
    mc_s "Look at you..."
    amb "Mmph..."
    mc_s "Fucking perfect."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_boobjob:
    show ep06_ambermorn33
    mc_s "Keep that tongue out."
    amb "Mmm..."
    mc_s "Just like that."

    show ep06_ambermorn34
    mc_s "Squeeze harder."
    amb "Like this?"
    mc_s "Perfect."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_assjob:
    show ep06_ambermorn35
    amb "You want this ass?"
    mc_s "Keep moving."
    amb "Someday?"
    mc_s "Maybe."
    mc_t "Not yet. But she wants it."
    amb "I'd let you. If you wanted."

    show ep06_anim08
    mc_s "Slower."
    amb "Mmm..."

    show ep06_ambermorn36
    amb "One day... will you?"
    mc_s "Soon..."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_footjob:
    show ep06_ambermorn37
    mc_s "Keep going."
    amb "You like this?"
    mc_s "Don't stop."
    show ep06_ambermorn38
    amb "Should I stop?"
    mc_s "No."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_continue:
    show ep06_ambermorn39
    amb "Please fuck me."
    mc_s "Beg better."
    amb "I need your cock. Please."

    show ep06_ambermorn40
    mc_s "This what you wanted?"
    amb "Yes... yes..."
    mc_s "Say it."
    amb "Use me... fuck..."

    show ep06_ambermorn41
    mc_s "Look at you..."
    amb "I'm yours..."
    mc_s "Say it again."
    amb "Yours. All yours."

    show ep06_ambermorn42
    mc_s "Too much?"
    mc_t "Her pulse is racing. She's not stopping me."
    amb "More..."

    show ep06_ambermorn43
    amb "Fuck... you're so strong..."
    mc_s "Hold on."
    amb "Don't stop..."

    show ep06_ambermorn44
    amb "Watch..."
    mc_s "I am."
    amb "You love this ass."

    show ep06_ambermorn45
    amb "Mmm... fuck..."

    show ep06_ambermorn46
    mc_s "You close?"
    amb "So close..."
    mc_t "Right there. Almost."
    mc_s "Then cum for me."

    show ep06_ambermorn47
    amb "Inside... yes..."
    mc_s "All of it."
    mc_t "Mine. She's fucking mine."
    menu:
        "You're mine.":
            mc_s "You're mine completely."
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)
        "Fucking perfect.":
            mc_s "Fucking perfect."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
        "Good girl.":
            mc_s "Good girl."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

    show ep06_ambermorn48
    amb "Mmm..."
    mc_s "Dirty girl."
    amb "Your dirty girl."

    show ep06_ambermorn49
    amb "Don't look at me like that."
    mc_s "Like what?"
    amb "Like I'm... like I'm not broken. Like you don't see all the fucked up—"
    mc_s "I see you."
    amb "That's what scares me."
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_love:
    show ep06_ambermorn50
    amb "Say that again."
    mc_s "You're the only good thing."
    amb "I..."
    amb "I don't know how to do this."
    show ep06_ambermorn51
    mc_s "Do what?"
    amb "Let someone... I mean, when you look at me like that, it's like you're..."
    mc_t "She's terrified?"
    mc_s "Like I'm what?"
    amb "Seeing all the parts I try to hide. And I don't... I can't..."
    mc_s "Can't what?"
    amb "I can't keep pretending I don't need this. Need you."


label ep06_mornwithamber_love_sexmenu:
    menu:
        amb "What do you want?"
        
        "Let me show you." if not e6_amber_love_worship_seen:
            mc_s "Let me show you how beautiful you are."
            $ e6_amber_love_worship_seen = True
            jump ep06_mornwithamber_love_worship
        
        "Let me taste you." if not e6_amber_love_oral_seen:
            mc_s "Let me taste you first."
            $ e6_amber_love_oral_seen = True
            jump ep06_mornwithamber_love_oral
        
        "Let me touch you." if not e6_amber_love_assjob_seen:
            mc_s "Let me love you with my hands first."
            $ e6_amber_love_assjob_seen = True
            jump ep06_mornwithamber_love_assjob
        
        "Let me hold you." if (e6_amber_love_worship_seen and e6_amber_love_oral_seen and 
                              e6_amber_love_assjob_seen):
            mc_s "Let me hold you close while we make love."
            jump ep06_mornwithamber_love_hold


label ep06_mornwithamber_love_worship:
    show ep06_ambermorn52
    mc_s "Every inch of you..."
    amb "Don't..."
    mc_s "Don't what?"
    amb "Don't make me cry."

    show ep06_anim09
    amb "Fuck..."
    mc_s "What?"
    amb "You're making me feel things."

    show ep06_anim10
    amb "God... yes..."
    mc_s "You're perfect."
    amb "I'm not."
    mc_s "To me you are."
    mc_t "I'll show you. Every day."
    jump ep06_mornwithamber_love_sexmenu


label ep06_mornwithamber_love_oral:
    show ep06_ambermorn53
    mc_s "Relax..."
    amb "I can't..."
    mc_s "Why not?"
    amb "Because you're... because this is..."
    mc_t "Stop thinking..."
    amb "Fuck..."

    show ep06_anim11
    amb "There... right there..."
    mc_s "Mmm..."
    amb "Don't stop... please don't stop..."
    jump ep06_mornwithamber_love_sexmenu


label ep06_mornwithamber_love_assjob:
    show ep06_ambermorn54
    amb "I want to pleasure you..."
    mc_s "You don't have to—"
    amb "I want to. Let me."

    show ep06_anim12
    mc_s "You're so beautiful..."
    amb "You make me feel it."
    jump ep06_mornwithamber_love_sexmenu


label ep06_mornwithamber_love_hold:
    show ep06_ambermorn55
    amb "I love you."
    mc_s "I know."
    amb "Do you love me?"

    show ep06_ambermorn56
    mc_s "I love you too."
    amb "Then show me."
    mc_s "How?"
    amb "Slowly."

    show ep06_ambermorn57
    amb "Oh god..."
    mc_s "Look at me."
    amb "I can't..."
    mc_s "Why not?"
    amb "Too much..."

    show ep06_ambermorn58
    mc_s "Open your eyes."
    amb "I can't..."
    mc_s "Please."
    mc_t "Let me see you. Please."

    show ep06_ambermorn59
    amb "I see you too."
    mc_s "What do you see?"
    amb "Someone who..."
    amb "Someone who stays."

    show e06_anim13
    amb "Mmm... fuck... mmm..."

    show ep06_ambermorn60
    amb "Faster... I need..."
    mc_s "Tell me."
    amb "I need you... deeper... harder..."
    mc_s "Like this?"
    amb "Yes... fuck yes..."

    show e06_anim14
    amb "Don't let go..."
    mc_s "Never."
    amb "Promise..."
    mc_s "I promise."

    show ep06_ambermorn61
    amb "I'm... fuck... I'm..."
    mc_s "I've got you."
    amb "Don't... let... go..."
    mc_s "I won't. I'm here."

    menu:
        "I love you.":
            mc_s "I love you. Always."
            $ rm.update("amber", "love", 3)
            $ check_levels("amber", "love", 3)
        "You're safe.":
            mc_s "You're safe with me."
            $ rm.update("amber", "love", 2)
            $ check_levels("amber", "love", 2)
        "I'm staying.":
            mc_s "I'm not going anywhere."
            $ rm.update("amber", "love", 1)
            $ check_levels("amber", "love", 1)
    
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_rejection:
    show ep06_ambermorn62
    mc_s "Amber, I can't do this right now."
    amb "What the fuck do you mean you can't?"

    show ep06_ambermorn63
    mc_s "The case from yesterday... my head isn't right. I need to focus."
    mc_t "It's a lie. And she knows it."
    amb "Bullshit. This is about something else."

    show ep06_ambermorn64
    amb "You're shutting me out. Just like everyone else does."
    mc_s "It's not about shutting you out—"
    amb "Don't fucking lie to me! I can see it in your eyes. You're already pulling away."

    show ep06_ambermorn65
    amb "You know what? Fuck it. You want to push me away? Fine."
    mc_t "I'm losing her. Right now."

    show ep06_ambermorn66
    amb "You want to know why I need you to stay exactly as fucked up as you are?"
    mc_s "Amber..."
    mc_t "Here it comes."
    amb "No, you're going to hear this. Since you're so fucking determined to become the perfect cop."

    show ep06_ambermorn67
    amb "When we were kids, before everything went to shit with this family..."
    mc_t "She's going all the way back."

    show ep06_ambermorn68
    amb "You were the only one who actually saw me. Not Mom's perfect blonde doll she wanted to parade around. Just... me."
    amb "When I cut and dyed my hair, destroyed her precious image, Dad called me a disappointment."
    mc_s "I remember."

    show ep06_ambermorn69
    amb "Mom just... looked through me like I didn't exist. Like I'd..."
    mc_t "God, she's breaking."
    amb "Like I'd become invisible."

    show ep06_ambermorn70
    amb "But you? You said I looked like a warrior."
    mc_s "Because you did. You do."
    amb "You saw something worth protecting when everyone else saw a problem to fix."

    show ep06_ambermorn71
    amb "That's why I need you damaged. Because damaged people understand each other."

    show ep06_ambermorn72
    amb "But go ahead. Become the perfect detective. Let this fucking job fix you."
    mc_s "It's not about fixing—"
    amb "Whatever. Point is, don't let this fucking job change you. I need you exactly this damaged."

    show ep06_ambermorn73
    amb "Because once you're fixed, once you're the shining hero cop..."
    mc_t "She's leaving. This is it."

    show ep06_ambermorn74
    amb "You'll look at me the same way they all do. Like I'm the problem that needs solving."
    mc_s "That's not true."
    amb "Isn't it? You're already starting to reject me."

    show ep06_ambermorn75
    amb "You know what the difference is between you and every other man in my life?"
    mc_t "Don't say it. Please."

    show ep06_ambermorn76
    amb "You actually made me believe someone could want the real me. Not the fantasy, not the rebellion, not the shock value."
    mc_s "I do want the real you."
    amb "Sure you do. That's why you're pushing me away the moment things get ... Forget it!"

    show ep06_ambermorn77
    amb "Here's some free advice, Detective: I'm the only one who's ever seen the real you and didn't flinch."
    mc_t "She's right. Fuck, she's right."

    show ep06_ambermorn78
    amb "So when you're lying in bed tonight, being the perfect cop with the clean conscience..."
    mc_s "Amber, wait—"
    amb "Remember that I'm the only one who loved you when you were broken. And I was the only one honest enough to stay broken with you."

    show ep06_ambermorn79
    mc_s ". . ."

    show ep06_ambermorn80
    mc_s "Fuck."
    mc_t "I lost her."
    mc_s "This is the right choice."
    mc_t "...Isn't it?"
    jump ep06_madisonintro


label ep06_madisonintro:
    scene eigengrau
    show ep06_madisoncamera01
    mad "Oh!"
    mad "You're actually awake."
    mc_s "Work starts at eight."
    mad "Right... Your detective job."
    mc_t "Three months of silence. Now small talk."

    show ep06_madisoncamera02
    mad "I have a photoshoot. Near Sakuradamon station."
    mc_s "That's not close to my office."
    mad "Oh. I thought it was."
    mc_s "Thirty-minute train ride."
    mad "Still. Same direction, right?"
    mc_t "She looked up the route."

    show ep06_madisoncamera03
    mad "Could we take the same train?"
    mc_s "Why?"
    mad "I want to play a game with you."
    mc_s "A game..."
    mad "On the train. Thirty minutes."

    show ep06_madisoncamera04
    mc_s "What kind of game?"
    mad "The confession kind."
    mc_s "Pass."
    mad "Even if I make it worth your while?"

    show ep06_madisoncamera05
    if ep05_confrontation_peaceful:
        mad "I have something you want deleted."
        mc_t "The recording."
        mc_s "What do you want for it?"
        mad "Honesty. Six questions worth."
        mc_s "And if I lie?"
        mad "I keep it forever."

        show ep06_madisoncamera06
        mc_s "That's blackmail."
        mad "That's negotiation."
        mc_s "What makes you think I care if you keep it?"
        mad "Because you haven't asked me to delete it in three months."

        show ep06_madisoncamera09
        mc_t "She's been waiting for me to beg."
        mc_s "Fine."
    else:
        mad "I need to understand why you said no."
        mc_s "Ask someone else."
        mad "I can't ask in this house."
        mc_s "Why not?"
        mad "Because if Michael hears what I'm asking, he'll know."
        mc_s "Know what?"
        mad "That I'm questioning what he taught me."
        mc_s "What did he teach you?"

        show ep06_madisoncamera07
        mad "That all men want the same thing. That I should use it."
        mc_t "Michael taught her to weaponize sexuality."

        show ep06_madisoncamera08
        mc_s "And you believed him."
        mad "Everyone proved him right. Except you."
        mc_s "So this is about proving Father wrong."
        mad "This is about finding out if he was."

        show ep06_madisoncamera09
        mc_t "She's testing whether Michael lied to her."
        mc_s "Six questions. Then we're done."
    
    mad "Let's go."
    jump ep06_madison_traingame

label ep06_madison_traingame:
    show ep06_madisoncamera10
    mc_t "Not an accident. She positioned herself for this angle."
    mad "Round one."
    
    show ep06_madisoncamera11
    pause
    show ep06_madisoncamera12
    pause
    show ep06_madisoncamera13
    pause
    show ep06_madisoncamera14
    pause
    show ep06_madisoncamera15
    pause
    show ep06_madisoncamera16
    pause
    show ep06_madisoncamera17
    pause
    show ep06_madisoncamera18
    pause
    show ep06_madisoncamera19
    pause
    show ep06_madisoncamera20
    pause
    show ep06_madisoncamera21
    pause
    show ep06_madisoncamera22
    pause
    show ep06_madisoncamera23
    pause
    show ep06_madisoncamera24
    pause
    show ep06_madisoncamera25
    pause
    show ep06_madisoncamera26
    pause
    show ep06_madisoncamera27
    pause
    show ep06_madisoncamera28
    pause
    show ep06_madisoncamera29
    pause
    show ep06_madisoncamera30
    pause
    show ep06_madisoncamera31
    pause
    show ep06_madisoncamera32
    pause
    show ep06_madisoncamera33
    pause
    show ep06_madisoncamera34
    pause
    show ep06_madisoncamera35
    pause
    show ep06_madisoncamera36
    pause
    show ep06_madisoncamera37
    pause
    show ep06_madisoncamera38
    pause
    show ep06_madisoncamera39
    pause
    show ep06_madisoncamera40
    pause
    show ep06_madisoncamera41
    pause
    show ep06_madisoncamera42
    pause
    show ep06_madisoncamera43
    pause
    show ep06_madisoncamera44
    pause
    show ep06_madisoncamera45
    pause
    show ep06_madisoncamera46
    pause
    show ep06_madisoncamera47
    pause
    show ep06_madisoncamera48
    pause
    show ep06_madisoncamera49
    pause
    show ep06_madisoncamera50
    pause
    show ep06_madisoncamera51
    pause
    show ep06_madisoncamera52
    pause
    show ep06_madisoncamera53
    pause
    show ep06_madisoncamera54
    pause
    show ep06_madisoncamera55
    pause
    show ep06_madisoncamera56
    pause
    show ep06_madisoncamera57
    pause
    show ep06_madisoncamera58
    pause
    show ep06_madisoncamera59
    pause
    show ep06_madisoncamera60
    pause
    show ep06_madisoncamera61
    pause
    show ep06_madisoncamera62
    pause
    show ep06_madisoncamera63
    pause
    show ep06_madisoncamera64
    pause
    show ep06_madisoncamera65
    pause
    show ep06_madisoncamera66
    pause
    show ep06_madisoncamera67
    pause
    show ep06_madisoncamera68
    pause
    show ep06_madisoncamera69
    pause
    show ep06_madisoncamera70
    pause
    show ep06_madisoncamera71
    pause
