label ep06_start:
    $ persistent.current_episode = 6
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ persistent.act2_play = True
    $ renpy.block_rollback()
    $ renpy.save_persistent()
    jump ep06_intro


label ep06_intro:
    scene eigengrau with lines
    show location_tmpd_m with slowfade
    show tmpd_location zorder 2 with dissolve
    pause 5
    hide tmpd_location with dissolve
    jump ep06_ope


label ep06_ope:
    scene eigengrau
    $ config.rollback_enabled = True
    $ renpy.free_memory()
    pause 1.0

    show screen stats_button
    show screen walkthrough_icon

    $ playAudio(japanday_cross, "amb", 1, True, 3.0)
    $ setChannelVolume("amb", 1, 0.6, 0)

    show ep06_opening01
    mc_t "First day."
    mc_t "Nothing in the house is safe to say out loud anymore."

    $ stopAudio("amb", 1, 1.0)
    $ playAudio(policehall, "amb", 2, True, 3.0)
    $ setChannelVolume("amb", 2, 1, 0)
    $ playAudio(hallwalkmale, "sfx", 1, True, 3.0)
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(mc_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)

    show ep06_opening02 with fade
    mc_t "The badge weighs nothing."
    mc_t "Three months since the hospital."
    
    $ setAllSubchannelsVolume("sfx", 0.0, 1)
    $ setAllSubchannelsVolume("amb", 0.0, 1)

    show ep06_opening03
    mc_t "Mother's wrists. Gauze. Pulse."
    mc_t "Three months of visiting hours."

    show ep06_opening04
    mc_t "She's awake now. Talking. Smiling at the nurses."
    mc_t "That smile. I know that smile."

    $ setAllSubchannelsVolume("sfx", 1.0, 1)
    $ setAllSubchannelsVolume("amb", 1.0, 1)

    show ep06_opening05
    mc_t "Michael calls it 'remarkable progress.'"
    mc_t "Michael says a lot of things."

    $ stopAllAudio(2)

    scene eigengrau with fade
    $ playAudio(doorclose, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)
    pause 1

    $ playAudio(policeoffice, "amb", 1, True, 3.0)
    $ setChannelVolume("amb", 1, 0.5, 0)

    show ep06_opening06
    wat "Ah. Inspector..."
    wat "Kuro... Kurōfōdo-han. Yes."
    mc_t "Crawford..."

    show ep06_opening08
    wat "Sit. I was just reviewing your... unique demographics."
    mc_s "Is there a problem with my file, Chief?"
    wat "Problem? No. It is just... administratively fascinating."
    wat "Father: British subject. Mother: Italian national."
    wat "Born in Tokyo. Naturalized citizenship upon joining the force."
    wat "Technically Japanese. On paper."

    hide ep06_opening08
    mc_s "I was born here. I speak the language."
    wat "Right..."
    wat "But let's move on. The paperwork mentioned the incident."

    $ setAllSubchannelsVolume("amb", 0.0, 1)
    $ playAudio(gunshots_glock, "sfx", 2, False, 1)
    $ setChannelVolume("sfx", 2, 1.0, 0)
    $ playAudio(heartbeatfast, "sfx", 1, True, 1)
    $ setChannelVolume("sfx", 1, 1.0, 0)

    show ep06_opening07 with slowflash
    wat "Three months of leave. Psychological evaluation pending."
    mc_s "I've recovered. I'm ready for duty."
    
    $ setAllSubchannelsVolume("amb", 0.5, 1)
    $ stopAllSubchannels("sfx", 1.0)

    show ep06_opening08
    wat "Of course. We are short-handed, after all. Even... unconventional assets are useful."
    wat "Welcome to the First Investigation Division, Sōsa Ikka. We handle homicides."

    $ playAudio(mc_suspense_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)

    show ep06_opening09
    wat "Specifically, the homicide of Detective Yamamoto. Found dead last night."
    wat "Professional execution. Three shots. No wasted movement."
    wat "It lacks the... emotional messiness typical of domestic crimes. It feels imported."
    mc_t "Foreign killer. Foreign detective. He's putting the trash together."
    mc_s "Yakuza?"
    wat "Because of the context, the Organized Crime Division, Sotai, has jurisdiction on the motive, but we have jurisdiction on the body."
    wat "Inspector Sato from 'Sotai' requested a liaison from our division. Specifically you."
    mc_s "Why me?"

    $ setAllSubchannelsVolume("amb", 0.0, 1)

    show ep06_opening12
    wat "Osaka connections, perhaps."
    wat "Because Sato thinks you fit in."
    wat "You understand the Yakuza. Their crude manners. Their... loudness."
    
    $ setAllSubchannelsVolume("amb", 0.5, 1)

    hide ep06_opening12
    wat "The clans are obsessed with tradition. With 'Wa'—Harmony."
    wat "They react violently to external elements that look different. That don't belong."
    wat "Sato hopes your... appearance... might provoke a reaction that a Japanese officer could not elicit."

    show ep06_opening10
    mc_t "I'm not a detective to them. I'm bait. Foreign bait."
    wat "In this department, Inspector, we utilize every tool available."

    $ show_walkthrough("ep06_case_attitude_menu")
    menu:
        "I'll do this right.":
            hide screen walkthrough_screen
            mc_t "I'll investigate thoroughly. I won't give him a reason to doubt my badge."
            $ rm.update("mc", "integrity", 1)

        "I wasn't ready for this.":
            hide screen walkthrough_screen
            mc_t "Dead cop. Yakuza war. Three months wasn't enough recovery time for this."

        "Perfect. Time for payback.":
            hide screen walkthrough_screen
            mc_t "Good. I've got unfinished business with those bastards anyway."
            $ rm.update("mc", "integrity", -1)

    $ playAudio(door_glass, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1.0, 0)
    $ playAudio(policeoffice_loud, "amb", 2, False, 4.0)
    $ setChannelVolume("amb", 2, 0.1, 0)

    show ep06_opening11 with fade
    wat "Inspector Sato is waiting at the crime scene in Asagaya."
    wat "Try to blend in, Crawford. If that is even possible."
    mc_t "Osaka. It follows me like a bullet I can never hear coming."

    $ stopAllAudio(2)
    jump ep06_operative


label ep06_operative:
    scene eigengrau with lines
    show days_before
    pause 3
    show location_kabuchikotower_n with slowfade
    show kabukicho_night zorder 2 with dissolve
    pause 5
    hide kabukicho_night with dissolve
    jump ep06_shadow


label ep06_shadow:
    scene eigengrau

    $ playAudio(kudokai_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)
    $ playAudio(raining_ext, "amb", 1, True, 3.0)
    $ setChannelVolume("amb", 1, 0.5, 0)
    $ playAudio(evening_pool, "amb", 2, True, 3.0)
    $ setChannelVolume("amb", 2, 0.3, 0)

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

    $ setAllSubchannelsVolume("amb", 0.0, 1)

    show ep06_shadowdir03
    hir "None. Lives alone. Works late Thursdays."
    hir "Returns home past midnight. Drunk, usually. Keys in left pocket."
    anto "Why him?"

    show ep06_shadowdir04
    hir "He's connecting dots. Osaka to Tokyo. Surgical modifications, territory shifts, missing women."
    hir "Last week he requested files on Kudo-kai specifically."

    $ setChannelVolume("amb", 2, 0.3, 1)
    $ setChannelVolume("amb", 1, 0.5, 1)
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

    show ep06_shadowdir09 with fade
    hir "Yamaguchi-gumi, Sumiyoshi-kai, Inagawa-kai, all the old families - they think this is random violence. Gang war."
    hir "They don't see the pattern. They don't see me moving pieces."

    show ep06_shadowdir10 with fade
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

    $ stopAllSubchannels("music", 2.0)
    $ playAudio(heartbeatslow, "amb", 3, True, 3.0)
    $ setChannelVolume("amb", 3, 1, 5)

    show ep06_shadowdir12 with fade
    anto "Thursday night. Apartment 204."
    anto "Three shots. Professional spacing."
    anto "The knight falls."

    show ep06_shadowdir13
    anto "The board shifts."

    $ stopAllAudio(2)
    jump ep06_executiontitle


label ep06_executiontitle:
    scene eigengrau with lines
    show location_asagaya_n with slowfade
    show asagaya zorder 2 with dissolve
    pause 5
    hide asagaya with dissolve
    jump ep06_execution


label ep06_execution:
    scene eigengrau

    $ playAudio(mc_room_night, "amb", 1, True, 2.0)
    $ setChannelVolume("amb", 1, 0.4, 2)
    $ playAudio(raining_ext, "amb", 2, True, 2.0)
    $ setChannelVolume("amb", 2, 0.3, 2)
    $ playAudio(tokyo_residential, "amb", 3, True, 2.0)
    $ setChannelVolume("amb", 3, 0.2, 2)

    show ep06_execution01
    yam_t "Seventeen women. Seventeen families asking when I'll find answers."
    yam_t "Surgical chest incisions. Professional precision. Osaka to Tokyo - someone's expanding operations."

    show ep06_execution02 with fade
    yam_t "11:43 PM. Miyuki called three hours ago. Sounded tired. I told her two more days in Tokyo."
    yam_t "Lied. Probably four more days. Maybe five."
    yam_t "But I'm close. The connection between Osaka and Tokyo - it's here somewhere in these files."

    $ playAudio(door_knock, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_execution03
    yam_t "11:47 PM."
    yam_t "Five knocks. Polite. Soft."
    yam_t "Neighbor? Building manager?"
    yam_t "This late?"

    $ playAudio(antonella_mistery_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)
    $ setChannelVolume("amb", 1, 0.2, 2)
    $ setChannelVolume("amb", 2, 0.1, 2)
    $ setChannelVolume("amb", 3, 0.05, 2)
    $ playAudio(heartbeatslow, "sfx", 4, True, 2.0)
    $ setChannelVolume("sfx", 4, 0.3, 2)

    show ep06_execution04 with fade
    yam_t "Delivery driver."

    show ep06_execution05
    yam_t "Young."

    show ep06_execution06
    yam_t "European features: Black hair, pale, blue eyes with glasses."

    show ep06_execution07
    yam_t "Curves straining fabric. Wrong size. Abdomen scar visible. Work accident, maybe."

    show ep06_execution08
    yam_t "Late shift worker. Probably part-time student."
    anto "Delivery for Yamamoto-san. Signature required."
    yam_t "Light accent. Foreign worker."
    yam_t "Wrong apartment probably. Common mistake with Japanese names."

    $ playAudio(door_wood, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.8, 0)
    
    show ep06_execution09 with slowfade
    yam "I think you have the wrong—"
    anto "Yamamoto-san? Detective Yamamoto Koji?"
    yam "...Yes?"

    $ setAllSubchannelsVolume("amb", 0.0, 3)
    $ setChannelVolume("sfx", 4, 1, 2)

    yam_t "She knows I'm a detective... How?"
    yam_t "Sender must have specified? Precinct sometimes sends-"

    $ playAudio(guncock9mm, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.8, 0)

    show ep06_execution10

    $ fadeToAudio(heartbeatfast, "sfx", 4, 2.0, True)

    yam_t "European."

    show ep06_execution11
    yam_t "Osaka."

    show ep06_execution12
    yam_t "Miyuk—"

    $ playAudio(gunshot_glock_3shots, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    show ep06_execution13 with flash

    $ stopAudio("sfx", 4, 3.0)

    anto_t "Professional spacing."
    anto_t "The knight falls."

    $ playAudio(bodyfall_carpet, "sfx", 3, False, 0)
    $ setChannelVolume("sfx", 3, 1, 0)
    $ setChannelVolume("amb", 1, 0.2, 2)
    $ setChannelVolume("amb", 2, 0.1, 2)
    $ setChannelVolume("amb", 3, 0.05, 2)

    show ep06_execution14 with fade
    anto_t "Wedding ring on his finger."
    anto_t "Doesn't matter."
    anto_t "Package. Take it."
    anto_t "Thirty seconds. Exit clean."

    $ stopAllAudio(2)
    jump ep06_crimescene


label ep06_crimescene:
    scene eigengrau with lines
    show present
    pause 3

    $ playAudio(celldoor, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)
    pause 1

    $ playAudio(tokyo_residential, "amb", 1, True, 2.0)
    $ setChannelVolume("amb", 1, 0.4, 2)
    $ playAudio(evenbalcony, "amb", 2, True, 2.0)
    $ setChannelVolume("amb", 2, 0.4, 2)

    $ playAudio(hallwalkmale, "sfx", 1, True, 2.0)
    $ setChannelVolume("sfx", 1, 1, 2)

    show ep06_crimescene01
    mc_t "First day back. First crime scene in three months."

    show ep06_crimescene02 with flash
    mc_t "The last crime scene I was at, I was the one bleeding."

    $ setAllSubchannelsVolume("amb", 0.1, 2)

    show ep06_crimescene03
    mc_t "Second floor. Apartment 204. Asagaya."
    mc_t "Three yellow markers on the floor."
    mc_t "Gray-haired man crouching by the bullets. Wire-rim glasses. Cheap suit."
    mc_t "That's him. Detective Inspector Sato from Organized Crime."

    $ playAudio(mc_thinking_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)
    $ stopAllSubchannels("sfx", 2.0)

    show ep06_crimescene04
    tak "Don't step on the chalk, [mc_name]."
    mc_s "Inspector Sato."
    tak "Just Takeo. Titles are for reports. Focus is for solving cases."
    tak "Look at these casings. Tell me what you see."
    mc_t "No handshake. No 'welcome back'. Straight to the work."
    mc_t "My kind of cop."
    tak "Get down there. Tell me what the floor tells you."

    show ep06_crimescene09
    mc_s "Ugh!"
    mc_t "The scar tissue is still tight. It burns like a hot wire against my ribs."
    tak "Ignore the pain. Focus on the metal."
    tak "Nine millimeter. What do you see in the arrangement?"
    mc_s "Triangular pattern. Even spacing between each casing."
    tak "Physics doesn't do that. Guns eject casings randomly."
    tak "To get a triangle like this, someone has to pick them up and place them down."
    tak "Three shots. Three decisions. Three certainties."
    mc_s "He killed a man, then took five seconds to arrange art on the floor?"

    show ep06_crimescene10
    tak "Now, here is the lesson regarding our killer."
    tak "What kind of person executes a cop, then stays to arrange casings in a geometric pattern?"
    mc_s "That depends on how you look at it."

    $ show_walkthrough("ep06_killer_profile_menu")
    menu:
        "They believed in justice.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 2)
            mc_s "Someone with a code. Distorted, maybe. But they believe they are creating order."
            tak "Order. Yes. A fanatic creates order out of chaos."

        "Just following orders.":
            hide screen walkthrough_screen
            mc_s "Someone doing a job. Following a manual. No emotion involved."
            tak "A machine made of meat. Possible."

        "They enjoyed the kill.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -2)
            mc_s "A sadist. Someone who leaves a signature to taunt us."
            tak "Arrogance. That is a weakness we can exploit."

    tak "Whatever they are, they are disciplined."
    tak "Precisely. Stand up. Let's look at the victim."

    show ep06_crimescene05
    tak "Yamamoto Koji. Forty-two. Veteran of the Fourth District."
    tak "Paranoid. Carried a backup piece in his ankle holster. Slept with a chair under the knob."
    tak "And yet... he opened his door at midnight."

    show ep06_crimescene06
    mc_t "Yamamoto... I saw the file. Wife and kids in Osaka."
    mc_t "He was supposed to retire next year."

    show ep06_crimescene07
    tak "Why, [mc_name]? Why does a paranoid man lower his shield?"
    mc_s "He saw someone he trusted."
    tak "Or someone innocuous. A delivery man. A lost neighbor."
    tak "Or a woman."
    tak "Evil doesn't always look like a monster. Sometimes it looks harmless until it pulls the trigger."
    mc_t "I would have opened the door too."
    mc_t "That's the scary part."

    show ep06_crimescene08
    tak "You know why Watanabe gave you to me?"
    mc_s "Because I'm expendable."
    tak "We are all expendable. That's part of the job."
    tak "He gave you to me because we are both 'broken' tools in their eyes."
    tak "You are a gaijin. I am... inconveniently stubborn."
    tak "They put the broken tools in the basement so we don't ruin the display case."
    tak "But broken tools have jagged edges. They cut deeper."
    mc_t "Useful. He thinks I'm useful."
    tak "Come. Look at where he fell."

    show ep06_crimescene11
    mc_t "Dried blood. Dark brown against the cheap vinyl flooring."
    mc_t "Yamamoto bled out here. On this floor. Alone."
    tak "No defensive wounds. No signs of struggle."
    tak "First shot: Chest. Standing."
    tak "Second shot: Chest. Falling."
    tak "Third shot: Head. Execution."
    mc_s "He didn't have time to react."
    tak "Or he didn't recognize the threat until it was too late."
    mc_s "All three shots within seconds?"
    tak "According to the neighbors who heard 'firecrackers', yes."
    tak "Speed over precision. They wanted to finish before he could scream."

    show ep06_crimescene12
    mc_t "The chalk outline looks too small. Bodies always look smaller after death."
    mc_t "Yamamoto had a family. A wife in Osaka. Kids."
    mc_t "Now he's just a geometry problem on the floor."
    tak "Execution implies punishment, [mc_name]. Or containment."
    tak "Was Yamamoto being punished? Or was he simply eliminated because he opened the wrong door?"
    mc_s "What was he investigating exactly?"
    tak "Come to the desk. This is what he died for."

    show ep06_crimescene13
    tak "Yamamoto was tracking a specific anomaly. Murders."
    tak "Seventeen women over three months. Osaka to Tokyo pipeline."
    tak "All found with post-mortem surgical incisions in the same location."
    mc_s "Breast tissue removed?"
    tak "Systematically. Look at the timeline on the laptop."

    call screen confirm(
        message="Gore content ahead. Continue?",
        yes_action=[SetVariable("e6_gore", True), Return()],
        no_action=[SetVariable("e6_gore", False), Return()]
    )

    $ playAudio(officechair_sit, "sfx", 5, False, 0)
    $ setChannelVolume("sfx", 5, 0.3, 0)
    
    show ep06_crimescene14
    mc_t "Bodies. Female. Surgical cuts."

    if e6_gore:
        $ playAudio(mouseclick, "sfx", 1, False, 0)
        $ setChannelVolume("sfx", 1, 1, 0)
        show ep06_crimescene15 with fade
        tak "Victim one. Three months ago. Look at the incision."
        mc_t "Clean sutures. Minimal bruising."
        mc_s "Surgical precision. Looks like a professional augmentation job."
        tak "Correct. A doctor—or someone very skilled—did this."

        $ playAudio(mouseclick, "sfx", 2, False, 0)
        $ setChannelVolume("sfx", 2, 1, 0)
        show ep06_crimescene16 with fade
        tak "Victim eight. Two months ago."
        mc_t "Jagged edges. Bruising."
        mc_s "Getting sloppy. There's infection around the wound."
        tak "The hand is shaking. The time is shortening."

        $ playAudio(mouseclick, "sfx", 3, False, 0)
        $ setChannelVolume("sfx", 3, 1, 0)
        show ep06_crimescene17 with fade
        tak "Victim seventeen. Last week."
        mc_t "God... ripped open."
        mc_s "That's not surgery. That's butchery."
        mc_t "Whatever was inside was torn out in a panic."
        tak "Exactly. From surgeon to butcher in ninety days."

    else:
        tak "Three months ago. First victim."
        mc_t "Clean cut. Precise medical work."
        tak "Two months ago. Victim eight."
        mc_t "Rougher. Less careful. Signs of infection."
        tak "Last week. Victim seventeen."
        mc_t "Butchered. Hack job. Whoever did this was either in a hurry or didn't care anymore."

    show ep06_crimescene18
    mc_s "You think it's organ harvesting?"
    tak "Think, Crawford. Kidneys have value. Livers have value."
    tak "Does breast tissue have black market value?"
    mc_s "No. No transplant demand."
    tak "So if the tissue is worthless, why cut it open?"
    mc_t "It's not about the flesh. It's about the space."
    mc_s "Implants."
    tak "Containers."
    tak "Sealed silicone compartments. High-grade liquid cocaine? Microchips? Rare earth metals?"
    tak "We don't know yet. But these women were not humans to the killers."
    tak "They were walking suitcases."

    show ep06_crimescene19
    mc_s "And Yamamoto figured it out."
    tak "He figured out that the 'surgeon' is losing his mind."
    tak "Look at the degradation. The panic."
    mc_s "Why kill the detective now?"
    tak "Because he found the link between the butcher in Tokyo and the supplier in Osaka."
    tak "This isn't just murder. This is industry. And industry protects its assets."
    tak "Tell me, [mc_name]. When you look at seventeen dead women treated like packaging..."
    tak "What is your instinct? Morally."

    $ show_walkthrough("ep06_criminal_vision_menu")
    menu:
        "Stop them legally.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 2)
            mc_s "We build the case. We prosecute. We show them that the law is stronger than their greed."
            tak "The noble path. Hard. Slow. But necessary for civilization."

        "Just catch them.":
            hide screen walkthrough_screen
            mc_s "We find them and we cage them. I don't care about the philosophy."
            tak "Pragmatic. Good. Emotion clouds judgment."

        "They deserve everything.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -2)
            mc_s "People who do this aren't human. I don't care what happens to them when we find them."
            tak "Be careful. If you hunt monsters with rage, you might forget when to stop."

    show ep06_crimescene20
    tak "The autopsy results will be ready tomorrow. Dr. Hatanaka."
    tak "She will tell us what was inside the implants."
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

    $ stopAllAudio(2)
    jump ep06_mornintro


label ep06_mornintro:
    scene eigengrau with clouds_inverse
    show next_morning
    pause 3
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

    $ show_walkthrough("ep06_amber_first_decision_menu")
    menu:
        "Show me." if amber_strikes == 0 and rm.get("amber", "cor") >= 25:
            hide screen walkthrough_screen
            mc_s "Show me what you were doing."

            $ e6_amber_path = "corruption"
            jump ep06_mornwithamber_corruption

        "You're impossible.":
            hide screen walkthrough_screen
            mc_s "You're impossible."

        "I missed this.":
            hide screen walkthrough_screen
            mc_s "I missed this too."

            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "Not now.":
            hide screen walkthrough_screen
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

    $ show_walkthrough("ep06_amber_intimacy_response_menu")
    menu:
        "You see me." if amber_strikes == 0 and rm.get("amber", "trust") >= 40:
            hide screen walkthrough_screen
            mc_s "You've always seen me."

            $ e6_amber_path = "love"
            jump ep06_mornwithamber_love

        "You like broken things?":
            hide screen walkthrough_screen
            mc_s "You like broken things?"

            $ e6_amber_path = "neutral"
            jump ep06_mornwithamber_neutral

        "Like the view?":
            hide screen walkthrough_screen
            mc_s "Like what you see?"

            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
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

    $ show_walkthrough("ep06_amber_sex_neutral_talk_menu")
    menu:
        "I love you.":
            hide screen walkthrough_screen
            mc_s "I love you, Amber."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "Fucking perfect.":
            hide screen walkthrough_screen
            mc_s "Your pussy's perfect."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

        "Only you.":
            hide screen walkthrough_screen
            mc_s "No one else compares."
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
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
    $ show_walkthrough("ep06_mornwithamber_neutral_sexmenu")
    menu:
        amb "Tell me what you want..."
        "Come here." if not e6_amber_neutral_blowjob_seen:
            hide screen walkthrough_screen
            mc_s "Come here."
            $ e6_amber_neutral_blowjob_seen = True
            jump ep06_mornwithamber_neutral_blowj

        "Let me see all of you." if not e6_amber_neutral_boobjob_seen:
            hide screen walkthrough_screen
            mc_s "Let me see all of you."
            $ e6_amber_neutral_boobjob_seen = True
            jump ep06_mornwithamber_neutralboobj

        "Keep going." if e6_amber_neutral_blowjob_seen and e6_amber_neutral_boobjob_seen:
            hide screen walkthrough_screen
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

    $ show_walkthrough("ep06_amber_neutral_climax_menu")
    menu:
        "Only you get me.":
            hide screen walkthrough_screen
            mc_s "You're the only one who understands."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "Take it all.":
            hide screen walkthrough_screen
            mc_s "Then take all of it."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

        "Broken together.":
            hide screen walkthrough_screen
            mc_s "Maybe we're both exactly as fucked up as we need to be."
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)

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

        $ show_walkthrough("ep06_amber_corruption_postclim_menu")
        menu:
            "You don't scare me.":
                hide screen walkthrough_screen
                mc_s "Nothing about you scares me."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "We fit perfectly.":
                hide screen walkthrough_screen
                mc_s "We're both exactly what we need to be."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                $ rm.update("amber", "cor", 1)
                $ check_levels("amber", "cor", 1)

            "Stop overthinking.":
                hide screen walkthrough_screen
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

        $ show_walkthrough("ep06_amber_love_postclim_menu")
        menu:
            "I mean it.":
                hide screen walkthrough_screen
                mc_s "I know exactly what I'm saying."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "Test me.":
                hide screen walkthrough_screen
                mc_s "Try me. Test it. I'm still here."
                $ rm.update("amber", "trust", 2)
                $ check_levels("amber", "trust", 2)

            "Help me understand.":
                hide screen walkthrough_screen
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

        $ show_walkthrough("ep06_amber_neutral_postclim_menu")
        menu:
            "Perfect to me.":
                hide screen walkthrough_screen
                mc_s "You've always been perfect to me."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "Warriors together.":
                hide screen walkthrough_screen
                mc_s "We're both warriors now."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                $ rm.update("amber", "cor", 1)
                $ check_levels("amber", "cor", 1)

            "Time to go.":
                hide screen walkthrough_screen
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
    $ amber_cor_choices += 1
    $ rm.update("amber", "cor", 10)
    $ check_levels("amber", "cor", 10)
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
    $ show_walkthrough("ep06_mornwithamber_corruption_sexmenu")
    menu:
        amb "What do you want from me?"

        "Use your mouth." if not e6_amber_cor_blowjob_seen:
            hide screen walkthrough_screen
            mc_s "Use your mouth."
            $ e6_amber_cor_blowjob_seen = True
            jump ep06_mornwithamber_cor_blowjob

        "Your tits. Now." if not e6_amber_cor_boobjob_seen:
            hide screen walkthrough_screen
            mc_s "Your tits. Now."
            $ e6_amber_cor_boobjob_seen = True
            jump ep06_mornwithamber_cor_boobjob

        "Turn around." if not e6_amber_cor_assjob_seen:
            hide screen walkthrough_screen
            mc_s "Turn around."
            $ e6_amber_cor_assjob_seen = True
            jump ep06_mornwithamber_cor_assjob

        "On your knees." if not e6_amber_cor_footjob_seen:
            hide screen walkthrough_screen
            mc_s "On your knees."
            $ e6_amber_cor_footjob_seen = True
            jump ep06_mornwithamber_cor_footjob

        "Spread your legs." if (e6_amber_cor_blowjob_seen and e6_amber_cor_boobjob_seen and
                                e6_amber_cor_assjob_seen and e6_amber_cor_footjob_seen):
            hide screen walkthrough_screen
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
    $ show_walkthrough("ep06_amber_corruption_sex_menu")
    menu:
        "You're mine.":
            hide screen walkthrough_screen
            mc_s "You're mine completely."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

        "Fucking perfect.":
            hide screen walkthrough_screen
            mc_s "Fucking perfect."
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)

        "Good girl.":
            hide screen walkthrough_screen
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

    $ ep06_ach_ambcor = True
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_love:
    $ amber_love_choices += 1
    $ rm.update("amber", "trust", 10)
    $ check_levels("amber", "trust", 10)
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
    $ show_walkthrough("ep06_mornwithamber_love_sexmenu")
    menu:
        amb "What do you want?"

        "Let me show you." if not e6_amber_love_worship_seen:
            hide screen walkthrough_screen
            mc_s "Let me show you how beautiful you are."
            $ e6_amber_love_worship_seen = True
            jump ep06_mornwithamber_love_worship

        "Let me taste you." if not e6_amber_love_oral_seen:
            hide screen walkthrough_screen
            mc_s "Let me taste you first."
            $ e6_amber_love_oral_seen = True
            jump ep06_mornwithamber_love_oral

        "Let me touch you." if not e6_amber_love_assjob_seen:
            hide screen walkthrough_screen
            mc_s "Let me love you with my hands first."
            $ e6_amber_love_assjob_seen = True
            jump ep06_mornwithamber_love_assjob

        "Let me hold you." if (e6_amber_love_worship_seen and e6_amber_love_oral_seen and
                              e6_amber_love_assjob_seen):
            hide screen walkthrough_screen
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

    $ show_walkthrough("ep06_amber_love_declaration_menu")
    menu:
        "I love you.":
            hide screen walkthrough_screen
            mc_s "I love you. Always."

            $ rm.update("amber", "trust", 10)
            $ check_levels("amber", "trust", 10)

        "You're safe.":
            hide screen walkthrough_screen
            mc_s "You're safe with me."

            $ rm.update("amber", "trust", 7)
            $ check_levels("amber", "trust", 7)

        "I'm staying.":
            hide screen walkthrough_screen
            mc_s "I'm not going anywhere."

            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
    
    $ ep06_ach_amblove = True
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
    # TRAIN SEQUENCE - ROUND 1 SETUP
    show ep06_madisoncamera10
    mc_t "Not an accident. She positioned herself for this angle."
    mad "Round one."

    # ROUND 1 - Madison Asks
    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks about wanting her
        show ep06_madisoncamera11
        mad "Did you want me that night?"

        $ show_walkthrough("ep06_madison_deepq_round1_menu")
        menu:
            "I don't know.":
                hide screen walkthrough_screen
                mc_s "I don't know."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera12
                mad "You don't know."
                mc_s "Sometimes you attract me. Sometimes you repulse me."
                mad "So both."
                mc_s "Yeah. Both."
                mad "Which was it that night?"
                mc_s "Both... At the same time."

            "Does it matter?":
                hide screen walkthrough_screen
                mc_s "Does it matter?"
                mad "Yes."
                mc_s "It happened. That's all that matters."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera13
                mad "Bullshit."
                mc_s "You asked. I'm saying it's complicated."
                mad "That's not an answer."
                mc_t "She knows I'm dodging."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "No. I didn't.":
                hide screen walkthrough_screen
                mc_s "No. I didn't."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera14
                mad "Then why did you--?"
                mc_s "You were there. You know why."
                mad "You're lying."
                mc_s "How would you know?"

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks why MC said no
        show ep06_madisoncamera11
        mad "Why did you say no?"

        $ show_walkthrough("ep06_madison_response_round1_menu")
        menu:
            "Because you're irritating.":
                hide screen walkthrough_screen
                mc_s "Because you're irritating."
                mad "Irritating."
                mc_s "Everything's a war with you. Every interaction."
                $ rm.update("madison", "trust", -2)
                $ check_levels("madison", "trust", -2)

                show ep06_madisoncamera15
                mad "That's not a reason."
                mc_s "You think sex is a tool. That everyone has to say yes."
                mad "So?"
                mc_s "So I'm not a pawn in your games."
                mad "That's it?"
                mc_s "That's enough."

            "Because the timing was wrong.":
                hide screen walkthrough_screen
                mc_s "Because the timing was wrong."
                mad "Timing."
                mc_s "Yeah."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera13
                mad "Bullshit."
                mc_s "Believe what you want."
                mad "That's not a reason. That's an excuse."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "Because I wasn't attracted to you.":
                hide screen walkthrough_screen
                mc_s "Because I wasn't attracted to you."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera14
                mad "Liar."
                mc_s "How would you know?"
                mad "Because you looked at me like I was exactly what you wanted."
                mad "Right before you said no."

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    # ROUND 1 - MC Asks
    show ep06_madisoncamera16
    mad "My turn to answer."
    mc_s "I haven't asked yet."
    mad "Then ask."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks about recording
        mc_s "Why did you record it?"

        show ep06_madisoncamera17
        mad "I never trust anyone."
        mc_s "That's not a reason."
        mad "It's the closest thing to forcing honesty I have."
        mc_s "By creating leverage."
        mad "By creating insurance."
        mc_s "Against what?"
        mad "Against you pretending it never happened."
        mc_t "She's afraid I'd deny her... but why does she care?"

    else:
        # FALSE PATH - MC asks why Madison offered herself
        mc_s "Why did you offer yourself?"

        show ep06_madisoncamera18
        mad "I wanted to test you."
        mc_s "Test me."
        mad "See if you're like the others. See if you're man enough."
        mc_s "And?"
        mad "And I was wrong."
        mc_s "Wrong how?"
        mad "I thought you'd say yes."
        mc_t "So I'm not man enough for her… should I take that as a blessing or a curse?"

    mad "Round two."


    # ROUND 2 - Madison Asks
    show ep06_madisoncamera37

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC was really protecting Nanami
        mad "Was I really protecting Nanami? Or was I using you?"

        $ show_walkthrough("ep06_madison_deepq_round2_menu")
        menu:
            "I don't know. You tell me.":
                hide screen walkthrough_screen
                mc_s "I don't know. You tell me."
                mad "What?"
                mc_s "You were the one who used that excuse."
                mad "I... I wasn't—"
                mc_s "You said it was to protect her purity. Your words."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera38
                mad "It was true! But--"
                mc_s "Then why are you asking me?"
                mad "Because I don't know if I was lying to myself."
                mc_t "First honest thing she's said."

            "You believed it when you said it.":
                hide screen walkthrough_screen
                mc_s "You believed it when you said it."
                mad "That's not answering my question."
                mc_s "It's the only answer I have."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera39
                mad "Coward."
                mc_s "Why? How am I supposed to know how you feel?"
                mc_t "I don't know what I should say to her question."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "You were protecting her. Obviously.":
                hide screen walkthrough_screen
                mc_s "You were protecting her. Obviously."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera40
                mad "Liar. You don't really believe that."
                mc_s "You asked for my opinion."
                mad "I asked for truth. That's not it."
                mc_s "How would you know?"
                mad "Because I'm certain you don't believe in noble sacrifices, especially when it comes to me"
                mc_t "She has quite an eye for this."

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if it was because she's MC's sister
        mad "Was it because I'm your sister?"

        $ show_walkthrough("ep06_madison_response_round2_menu")
        menu:
            "Partially.":
                hide screen walkthrough_screen
                mc_s "Partially."
                mad "Partially?"
                mc_s "It's more about the way you are. Not who you are."
                mad "The way I am?"
                mc_s "Yeah."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera41
                mad "So if I were different, you'd have said yes."
                mc_s "Maybe. I don't know."
                mc_t "Is she doubting herself?."

            "Does it matter?":
                hide screen walkthrough_screen
                mc_s "Does it matter?"
                mad "Yes."
                mc_s "Well, you could put it that way, and that's enough."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera39
                mad "But that's not all, right?"
                mc_s "It's all I'm giving you."
                mc_t "Not a lie. Just incomplete."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "Yes. Only because you're my sister.":
                hide screen walkthrough_screen
                mc_s "Yes. Only because you're my sister."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera40
                mad "I know you're lying."
                mc_s "How would you know?"
                mad "Because I've seen you with everyone else, and that wouldn't stop you."
                mc_s "That doesn't mean—"
                mad "It means exactly that."
                mc_t "She caught the tell."

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    # ROUND 2 - MC Asks
    show ep06_madisoncamera42
    mc_s "My turn."
    mad "Ask."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks about who Madison was planning to show recording to
        if ep06_mc_advantage_points >= 1:
            $ show_walkthrough("ep06_madison_response_round3_true_menu")
            menu:
                "Who were you planning on showing it to?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera43
                    mad "I already told you. It forces honesty."
                    mc_s "That's not who. That's why."
                    mad "Whether I use it depends on whether you're honest with me."
                    mc_s "You mean, when you need to force me to be."
                    mad "Exactly."
                    mc_s "So you don't trust anyone without leverage."
                    mad "Everyone's a potential liar."
                    mc_t "She sees the whole world as hostile."

                "Have you already sent it to someone?":
                    hide screen walkthrough_screen
                    mc_s "Have you already sent it to someone?"
                    mad "No."
                    mc_s "What stopped you?"

                    show ep06_madisoncamera44
                    mad "I didn't need to. Yet."
                    mc_s "Yet."
                    mad "Besides, a threat only works if you know I have it."
                    mc_t "She's holding it over my head."
                    mad "But the situation has changed."
                    mc_s "Meaning?"
                    mad "Meaning this game changes everything."

                    $ ep06_mc_advantage_points -= 1
        else:
            mc_s "Who were you planning on showing it to?"

            show ep06_madisoncamera43
            mad "I already told you. It forces honesty."
            mc_s "That's not who. That's why."
            mad "Whether I use it depends on whether you're honest with me."
            mc_s "You mean, when you need to force me to be."
            mad "Exactly."
            mc_s "So you don't trust anyone without leverage."
            mad "Everyone's a potential liar."
            mc_t "She sees the whole world as hostile."

    else:
        # FALSE PATH - MC asks how many men said yes before
        if ep06_mc_advantage_points >= 1:
            $ show_walkthrough("ep06_madison_response_round3_false_menu")
            menu:
                "How many men have said yes before me?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera45
                    mad "Are you calling me a slut?"
                    mc_s "I'm asking a question."
                    mad "That shouldn't matter to you."
                    mc_s "Answer it anyway."
                    mad "For your information, no one's ever been inside me."
                    mc_s "But you tested them, didn't you?"
                    mad "That's different."
                    mc_s "How many?"
                    mad "Enough to know you're the anomaly."

                "Did any of them say no? Or was I the first?":
                    hide screen walkthrough_screen
                    mc_s "Did any of them say no? Or was I the first?"
                    mad "Most men beg for it. You were the first."
                    mc_s "The first to say no."

                    show ep06_madisoncamera44
                    mad "But don't get arrogant. It's not like I ask just anyone."
                    mc_s "Just how selective are you?"
                    mad "I've played with men. Teased them. But I never let it get to... that."
                    mc_s "To sex?"
                    mad "To losing control."
                    mc_s "So I'm the first one you actually offered yourself to."
                    mad "Yes."

                    $ ep06_mc_advantage_points -= 1
        else:
            mc_s "How many men said yes before me?"

            show ep06_madisoncamera45
            mad "Are you calling me a slut?"
            mc_s "I'm asking a question."
            mad "That shouldn't matter to you."
            mc_s "Answer it anyway."
            mad "For your information, no one's ever been inside me."
            mc_s "But you tested them, didn't you?"
            mad "That's different."
            mc_s "How many?"
            mad "Enough to know you're the anomaly."


    # ROUND 3 - Madison Asks
    show ep06_madisoncamera19

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC regrets it happened
        mad "Do you regret that it happened?"

        $ show_walkthrough("ep06_madison_deepq_round3_true_menu")
        menu:
            "No. I don't.":
                hide screen walkthrough_screen
                mc_s "No. I don't."
                mad "Why not?"
                mc_s "The sex wasn't the problem. I wanted it. You wanted it."
                mad "Then what's the problem?"
                mc_s "Everything that came after."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera20
                mad "Meaning?"
                mc_s "Meaning you make it difficult."
                mc_s "Your personality. Your need to fight me on everything."
                mc_s "It makes me question if the headache is worth it."
                mad "So I'm the problem."
                mc_s "You make things complicated. That's not the same thing."
                mc_t "She's looking for blame. Not giving it."

            "Sometimes.":
                hide screen walkthrough_screen
                mc_s "Sometimes."
                mad "Sometimes you regret it."
                mc_s "Sometimes I think it was a mistake."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera21
                mad "Which times?"
                mc_s "When you're like this."
                mad "Like what?"
                mc_s "Like you're at war with the world."
                mc_t "Not a lie. Just not the whole truth."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "Yes. Absolutely.":
                hide screen walkthrough_screen
                mc_s "Yes. Absolutely."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera22
                mad "You're lying again."
                mc_s "Am I?"
                mad "Yes."
                mc_s "Prove it."
                mad "You wouldn't be here if you regretted it."
                mc_t "Shit. She's right."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if MC thinks she's broken
        mad "Do you think I'm broken?"

        $ show_walkthrough("ep06_madison_deepq_round3_false_menu")
        menu:
            "You want me to answer that seriously?":
                hide screen walkthrough_screen
                mc_s "You want me to answer that seriously?"
                mad "Yes."
                mc_s "I'm not one to judge. I'm hardly a model of mental health myself."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera20
                mad "That's not an answer."
                mc_s "Fine. Yes. You're broken."
                mc_s "But so am I. And so is everyone else in our goddamn house."
                mad "That's supposed to make me feel better?"
                mc_s "It's supposed to make you feel less alone."

            "Define \"broken\".":
                hide screen walkthrough_screen
                mc_s "Define \"broken\"."
                mad "You know what I mean."
                mc_s "Do I? Are we talking about a machine? A toy? A system?"
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera21
                mad "You're dodging."
                mc_s "I'm saying people aren't objects. You can't be 'broken' if you were never whole to begin with."
                mc_t "Philosophical bullshit. Let's hope she buys it."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "No. You're fine. Really.":
                hide screen walkthrough_screen
                mc_s "No. You're fine. Really."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera22
                mad "Liar."
                mc_s "You asked my opinion."
                mad "I asked for truth."
                mc_s "Why is it so hard to believe I think you're normal?"
                mad "Because you don't believe anyone is normal."
                mc_t "She knows my worldview too well."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    # ROUND 3 - MC Asks
    show ep06_madisoncamera23
    mc_s "My turn."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks what Madison is teaching Nanami
        mc_s "What are you really teaching Nanami?"
        mad "You want honesty?"
        mc_s "That's the game."
        mad "Fine."

        show ep06_madisoncamera24
        mad "The core of it? Men are parasites. They don't want connection, they want access."
        mc_s "So you're teaching her to trust women."
        mad "No. Women are snakes too. I'm teaching her to trust ME."

        show ep06_madisoncamera25
        mc_s "So it's about control."
        mad "It's about protection."
        mc_s "Protection from what?"

        show ep06_madisoncamera26
        mad "From being used until she breaks."
        mad "From ending up like Mom."
        mc_t "And there's the wound."

    else:
        # FALSE PATH - MC asks if Nanami knows Madison loves her
        mc_s "Does Nanami know you love her?"
        mad "No."
        mc_s "Why not?"

        show ep06_madisoncamera27
        mad "Because if she knew the extent of it... she'd run."
        mc_s "You're sure of that."
        mad "I know it. My love is... heavy."
        mc_s "Have you ever considered telling her anyway?"
        mad "Don't you fucking dare suggest that."
        mc_s "I wasn't—"

        show ep06_madisoncamera28
        mad "Listen to me."
        mad "If you breathe a word of this to her, I will kill you."
        mc_s "I believe you."

    # ROUND 4 - Train Lurch / Madison Falls
    show ep06_madisoncamera46
    mc_s "..."
    mad "..."
    mc_s "You okay?"
    mad "Obviously not."
    mad "The train hit a curve."
    mc_s "I noticed."
    mad "Don't get any ideas."
    mc_s "You're the one on your knees."
    mad "Because physics exists."
    mc_s "Physics. Right."
    mc_s "Need a hand?"
    mad "I can manage."

    show ep06_madisoncamera47
    mad "Where were we?"
    mc_s "Round—"
    mad "Round four."

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if Isabella knows
        mad "Does Isabella know what you did with me?"

        $ show_walkthrough("ep06_madison_nanami_knows_true_menu")
        menu:
            "Of course not. Are you insane?":
                hide screen walkthrough_screen
                mc_s "Of course not. Are you insane?"
                mad "Why would that be insane?"
                mc_s "Because she's too young to understand."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera48
                mad "Too young? We were born in the same year."
                mad "If she's too young, then what am I? And what does that make you?"
                mc_s "I—"
                mad "You're a hypocrite."
                mad "Don't worry, I won't tell her."
                mad "I don't have to. Every time you look at her face now... you'll remember my moan."
                mc_t "She's planting a virus in my head."

            "I don't think so.":
                hide screen walkthrough_screen
                mc_s "I don't think so."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera49
                mad "You don't \"think\" so."
                mc_s "She hasn't said anything."
                mad "Silence isn't the same as ignorance."
                mc_s "If she knew, she would've confronted me."
                mad "Would she? Or would she be too disgusted to speak?"
                mc_t "Fuck. Would she?"

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "Maybe. I don't know.":
                hide screen walkthrough_screen
                mc_s "Maybe. I don't know."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera50
                mad "Liar."
                mc_s "How—"
                mad "Because if you thought there was even a 1% chance she knew..."
                mad "You wouldn't be standing here talking. You'd be panicked."
                mc_t "She's right. Again."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if MC left because they're damaged
        mad "Is that why you left us for eight years?"

        $ show_walkthrough("ep06_madison_why_left_false_menu")
        menu:
            "What do you mean?":
                hide screen walkthrough_screen
                mc_s "What do you mean?"
                mad "Did you leave because we're all damaged goods?"
                mc_s "No."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera51
                mad "Then why?"
                mc_s "I was chasing a ghost. An impossible hope."
                mad "Antonella."
                mc_s "A hope that never dies, though I've wished it would more times than I can count."
                mc_t "First time I've said it out loud."

            "I left for work.":
                hide screen walkthrough_screen
                mc_s "I left for work."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera49
                mad "Bullshit."
                mc_s "Police academy was in Osaka."
                mad "There are academies in Tokyo."
                mc_s "I needed distance."
                mad "From what?"
                mc_s "From the noise. From this family."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "I left because of career opportunities.":
                hide screen walkthrough_screen
                mc_s "I left because of career opportunities."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera50
                mad "You're lying."
                mc_s "How do you—"
                mad "Because you've never cared about climbing the ladder."
                mc_s "People change."
                mad "Not you. You care about truth, not rank."
                mc_t "She reads me too well."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie


    # ROUND 4 - MC Asks
    show ep06_madisoncamera52
    mc_s "My turn to ask."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks about Michael
        if ep06_mc_advantage_points >= 2:
            $ show_walkthrough("ep06_madison_deepq_round4_true_menu")
            menu:
                "What did Michael do to you the night you stopped being good?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera53
                    mad "He didn't do anything. Not physically."
                    mc_s "But?"
                    mad "But he peeled back the curtain. He and Mom."
                    mc_s "What did you see?"
                    mad "That there is no love. Only leverage."
                    mc_s "That's when the good girl died."
                    mad "That's when the good girl got smarter."
                    mc_t "She doesn't see it as death. She sees it as evolution."

                "Did Michael touch you? Is that why you use sex as a weapon?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera54
                    mad "He never touched me. He didn't have to."
                    mc_s "Explain."
                    mad "He didn't need to touch me to fuck up my head."
                    mad "He pointed at Mom. Laying there, broken, fading."
                    mad "He told me: 'Look at her. She was a queen. Now she's just furniture.'"
                    mc_s "God..."

                    show ep06_madisoncamera55
                    mad "He taught me that a woman's beauty is a leasing contract."
                    mad "It has an expiration date. And once the skin sags, men stop paying rent."
                    mc_s "So you decided to become the landlord."
                    mad "I decided I would never give it away for free. Not like her."
                    mad "If I'm going to be consumed, I'm going to name the price."
                    mc_t "Michael didn't rape her body. He raped her worldview."

                    $ ep06_mc_advantage_points -= 2
        else:
            mc_s "What did Michael do to you the night you stopped being good?"

            show ep06_madisoncamera53
            mad "He didn't do anything. Not physically."
            mc_s "But?"
            mad "But he peeled back the curtain. He and Mom."
            mc_s "What did you see?"
            mad "That there is no love. Only leverage."
            mc_s "That's when the good girl died."
            mad "That's when the good girl got smarter."
            mc_t "She doesn't see it as death. She sees it as evolution."

    else:
        # FALSE PATH - MC asks if Michael taught Madison to use sex as leverage
        if ep06_mc_advantage_points >= 2:
            $ show_walkthrough("ep06_madison_deepq_round4_false_menu")
            menu:
                "Did Michael teach you to use sex as leverage?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera53
                    mad "Not directly."
                    mc_s "Explain."
                    mad "He never laid a hand on me."
                    mc_s "But?"
                    mad "But in how he treated Mom. What he said about her."
                    mad "He made me see that women have an expiration date."
                    mad "The moment that men's desire fades, you're just... trash."
                    mc_s "And you believed him."
                    mad "I looked at Mom. Crying. Waiting for him. And I knew he was right."
                    mc_t "He poisoned her soul."

                "Did you despise Elizabeth for staying? (Costs 2 advantage points)":
                    hide screen walkthrough_screen
                    mc_s "Did you despise Elizabeth for staying?"

                    show ep06_madisoncamera54
                    mad "I despised her for being weak."
                    mc_s "She was a victim."
                    mad "She was a fool! She had everything! Beauty, status, power!"
                    mad "And she traded it all to be a housewife for a man who treated her like spoiled meat."
                    mc_s "So you vowed to be the opposite."
                    mad "I vowed to never kneel."
                    mad "Mom gave her power to a man. I take power FROM men."
                    mad "It's the only way to ensure I don't end up discarded in the corner."
                    mc_t "She attacks men preemptively so she never becomes Mom."

                    $ ep06_mc_advantage_points -= 2
        else:
            mc_s "Did Michael teach you to use sex as leverage?"

            show ep06_madisoncamera53
            mad "Not directly."
            mc_s "Explain."
            mad "He never laid a hand on me."
            mc_s "But?"
            mad "But in how he treated Mom. What he said about her."
            mad "He made me see that women have an expiration date."
            mad "The moment that men's desire fades, you're just... trash."
            mc_s "And you believed him."
            mad "I looked at Mom. Crying. Waiting for him. And I knew he was right."
            mc_t "He poisoned her soul."


    # ROUND 5 - Madison Asks
    show ep06_madisoncamera56
    mad "Round five."
    mc_s "Madison, we don't have to—"
    mad "Round. Five."

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC will pretend it never happened if deleted
        show ep06_madisoncamera57
        mad "If I delete this, will you pretend it never happened?"

        $ show_walkthrough("ep06_madison_response_round5_true_menu")
        menu:
            "No.":
                hide screen walkthrough_screen
                mc_s "No."

                show ep06_madisoncamera58
                mad "No?"
                mc_s "I don't deny what's been done."
                mad "Even if you regret it later?"
                mc_s "Regret isn't amnesia."

                show ep06_madisoncamera59
                mad "Explain."
                mc_s "I can hate that we did it, and still admit that we did."
                mad "Most people would wash their hands of it."
                mc_s "I'm not most people."
                mc_t "She's testing if I'll erase her the moment the evidence is gone."

            "Probably not.":
                hide screen walkthrough_screen
                mc_s "Probably not."
                mad "Probably."
                mc_s "I'm not in the habit of lying to myself."

                show ep06_madisoncamera61
                mad "That's not a promise."
                mc_s "It's a probability."
                mad "It's evasive. It means you MIGHT."
                mc_t "She wants certainty. I can't give it."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "If you delete it, it never happened.":
                hide screen walkthrough_screen
                mc_s "If you delete it, it never happened."

                show ep06_madisoncamera62
                mad "You're lying."
                mc_s "That's what you want, isn't it?"
                mad "I want to know if I'm disposable to you."
                mc_s "If the file is gone, we go back to normal."
                mad "So I AM disposable."
                mc_t "Ah. There it is. The fear of abandonment."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if MC would have said yes if not related
        show ep06_madisoncamera57
        mad "Would you have said yes if I wasn't related to you?"

        $ show_walkthrough("ep06_madison_response_round5_false_menu")
        menu:
            "I already told you. It's not about being related.":
                hide screen walkthrough_screen
                mc_s "I already told you. It's not about being related."

                show ep06_madisoncamera58
                mad "Then what?"
                mc_s "It's about who you are."
                mad "My personality."
                mc_s "You... repulse me."

                show ep06_madisoncamera60
                mad "Repulsion."
                mc_s "Yeah. The hatred in you... it's suffocating."
                mc_t "She wanted the truth. There it is."

            "Maybe.":
                hide screen walkthrough_screen
                mc_s "Maybe."
                mad "Maybe?"
                mc_s "Attraction isn't a science."

                show ep06_madisoncamera63
                mad "That's a non-answer."
                mc_s "It's the only one I've got. Without the taboos... who knows?"
                mc_t "True, but incomplete."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "Probably yes.":
                hide screen walkthrough_screen
                mc_s "Probably yes."

                show ep06_madisoncamera62
                mad "Liar."
                mc_s "You asked for a hypothetical."
                mad "I know men."
                mc_s "So?"
                mad "If you really wanted to fuck me, a little thing like 'family' wouldn't have stopped you."
                mad "Men break rules for lust. You didn't."
                mad "So you don't want me. At all."
                mc_t "Her logic is twisted... but effective."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    # ROUND 5 - MC Asks
    show ep06_madisoncamera64
    mc_s "My turn."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks if Madison is in love with Nanami
        mc_s "Are you in love with Nanami?"
        mad "Honestly?"
        mc_s "That's the rule."

        show ep06_madisoncamera66
        mad "I think so. I don't know."
        mc_s "You don't know."
        mad "I want to lock her away. I want her to only look at me."
        mad "I want to breathe the same air she breathes."
        mc_s "That sounds like obsession."
        mad "She doesn't see the filth in the world. She's clean."
        mc_s "And?"

        show ep06_madisoncamera65
        mad "And that innocence brings out something dark in me. I want to corrupt it. But I also want to protect it."
        mc_s "So you don't know which one you want more."
        mad "No. I don't."
        mc_t "First time she's admitted confusion about Nanami."

    else:
        # FALSE PATH - MC asks if Madison wants to be saved or wants someone broken with her
        mc_s "Do you want to be saved, or do you want someone broken with you?"
        mad "I don't know."
        mc_s "That's honest."

        show ep06_madisoncamera66
        mad "I don't feel like I need saving. I feel like I'm seeing clearly."
        mc_s "But?"
        mad "But if I'm going to be this... monster..."
        mad "I want it to serve a purpose."
        mc_s "Protecting Nanami."
        mad "Yeah. If I'm the monster, she can be the princess."
        mc_s "So you want your damage to be a shield."

        show ep06_madisoncamera67
        mad "I guess so."
        mc_t "She sacrifices her own humanity to justify her existence."


    # ROUND 6 - Final Question / Path Choice
    mad "Last question. My turn."

    show ep06_madisoncamera30

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC would do it again
        mad "If I delete this right now..."
        mad "Would you do it again?"

        $ show_walkthrough("ep06_madison_critical_true_menu")
        menu:
            "Not like that.":
                hide screen walkthrough_screen
                mc_s "Not like that."
                mad "Not like what?"
                mc_s "Not as a transaction. Not as leverage."

                show ep06_madisoncamera31
                mad "Then how?"
                mc_s "I'd do it for YOU. Not for the game."
                mad "You think there's a difference?"
                mc_s "I think beneath the armor, you wanted to be touched. Just touched."

                show ep06_madisoncamera32
                mad "Maybe there's nothing beneath the armor."
                mc_s "I don't believe that."
                mad "Why not?"
                mc_s "Because you're still here asking me questions instead of destroying me."
                mc_t "She wants to be seen. Really seen."
                mad "Hmmmm... Okay."

                $ ep06_madison_path = "love"
                $ madison_love_choices += 1
                $ rm.update("madison", "trust", 10)
                $ check_levels("madison", "trust", 10)

            "Yes.":
                hide screen walkthrough_screen
                mc_s "Yes. God help me, yes."
                mad "Even knowing who I am?"
                mc_s "Because of who you are."

                show ep06_madisoncamera33
                mad "Explain."
                mc_s "We're both broken, Madison. Normal people bore me, and I'm sure you find them boring too."
                mc_s "You're like poison... but I think I like the taste."
                mad "So you accept the transaction."
                mc_s "I accept that we're both fucked up. Why pretend otherwise?"

                show ep06_madisoncamera34
                mad "Good. Honesty suits you."
                mc_t "She wants an accomplice, not a savior."

                $ ep06_madison_path = "corruption"
                $ madison_cor_choices += 1
                $ rm.update("madison", "cor", 10)
                $ check_levels("madison", "cor", 10)

            "No.":
                hide screen walkthrough_screen
                mc_s "No."

                show ep06_madisoncamera35
                mad "Just no?"
                mc_s "The answer will always be no."
                mad "Why?"
                mmc_s "Because you don't want me. You want a puppet."
                mc_s "And I'm done dancing on your strings."

                show ep06_madisoncamera36
                mad "Fine. Be boring."
                mc_t "A clean rejection. Final."

                $ ep06_madison_path = "neutral"

    else:
        # FALSE PATH - Madison asks if MC would say yes now
        mad "If I asked again—right now—"
        mad "Would you say yes?"

        $ show_walkthrough("ep06_madison_critical_false_menu")
        menu:
            "Honestly? The dynamic has changed.":
                hide screen walkthrough_screen
                mc_s "Honestly? The dynamic has changed."
                mad "How?"
                mc_s "Before, you were a threat. Now..."

                show ep06_madisoncamera31
                mad "Now?"
                mc_s "Now you're just a woman in pain."
                mad "Careful..."
                mc_s "So maybe. If you asked me as yourself, not as 'Madison the monster'."

                show ep06_madisoncamera32
                mad "I don't know how to be anyone else."
                mc_s "We could figure that out."
                mc_t "She's looking for hope. I gave her a lifeline."
                mad "Okay."

                $ ep06_madison_path = "love"
                $ madison_love_choices += 1
                $ rm.update("madison", "trust", 10)
                $ check_levels("madison", "trust", 10)

            "Probably. Depends.":
                hide screen walkthrough_screen
                mc_s "Probably. The taboo is... tempting."
                mad "Is it?"
                mc_s "You know it is."

                show ep06_madisoncamera33
                mad "So you're a hypocrite. You preach morals but want the sin."
                mc_s "I never claimed to be a saint. And you make it hard to think straight."
                mad "Good."
                mc_s "If we cross that line, there's no going back."

                show ep06_madisoncamera34
                mad "Good to know."
                mc_t "She wants me to acknowledge the desire is mutual."

                $ ep06_madison_path = "corruption"
                $ madison_cor_choices += 1
                $ rm.update("madison", "cor", 10)
                $ check_levels("madison", "cor", 10)

            "No.":
                hide screen walkthrough_screen
                mc_s "No."

                show ep06_madisoncamera35
                mad "No?"
                mc_s "The answer will always be no."
                mad "Why?"
                mc_s "Because I don't like you and because you weaponize sexuality."
                mc_s "Find another toy, Madison."

                show ep06_madisoncamera36
                mad "Go to hell."
                mc_t "A clean rejection. Final."

                $ ep06_madison_path = "neutral"

    # ROUND 6 - Final MC Question
    show ep06_madisoncamera68
    mc_s "Last question. My turn."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks about the good girl
        if ep06_mc_advantage_points >= 1:
            $ show_walkthrough("ep06_madison_finalq_round6_true_menu")
            menu:
                "Do you miss the good girl?":
                    hide screen walkthrough_screen
                    mc_s "Do you miss the good girl?"
                    mad "No."
                    mc_s "Just no?"
                    mad "You're asking if I miss being hurt and helpless."
                    mc_s "I'm asking if you miss who you were."

                    show ep06_madisoncamera29
                    mad "Same thing."
                    mc_s "Is that what you tell yourself?"
                    mad "Being good got me nothing. Being bad... at least I get control."
                    mc_s "Control over what?"

                    show ep06_madisoncamera69
                    mad "Over not being hurt again."
                    mc_t "The good girl isn't gone. She's just armored."

                "If you could kill Michael and get away with it, would you?":
                    hide screen walkthrough_screen
                    mc_s "If you could kill Dad and get away with it, would you?"
                    mad "Are you serious?"
                    mc_s "Dead serious. Would you end him?"
                    mad "I don't know."
                    mc_s "You don't know?"

                    show ep06_madisoncamera29
                    mad "I wouldn't waste the energy."
                    mc_s "You don't hate him?"
                    mad "Hate implies passion. I feel... nothing."
                    mad "He's a walking wallet. Nothing more."
                    mc_s "So you wouldn't kill him?"
                    mad "Only if he hurt Nanami."

                    show ep06_madisoncamera69
                    mc_s "Not for yourself—for Nanami."
                    mad "I told you. I don't feel anything for him."
                    mc_t "She wouldn't kill him out of rage. Just for Nanami."

                    $ ep06_mc_advantage_points -= 1
        else:
            mc_s "Do you miss the good girl?"
            mad "No."
            mc_s "Just no?"
            mad "You're asking if I miss being hurt and helpless."
            mc_s "I'm asking if you miss who you were."

            show ep06_madisoncamera29
            mad "Same thing."
            mc_s "Is that what you tell yourself?"
            mad "Being good got me nothing. Being bad... at least I get control."
            mc_s "Control over what?"

            show ep06_madisoncamera69
            mad "Over not being hurt again."
            mc_t "The good girl isn't gone. She's just armored."

    else:
        # FALSE PATH - MC asks if stopping being good was her choice
        if ep06_mc_advantage_points >= 1:
            $ show_walkthrough("ep06_madison_finalq_round6_false_menu")
            menu:
                "When you stopped being the good girl, was it your choice?":
                    hide screen walkthrough_screen
                    mc_s "When you stopped being the good girl, was it your choice?"
                    mad "Yes."
                    mc_s "You're sure."
                    mad "It had to be a choice."
                    mc_s "Or maybe it was a reaction. A survival reflex."

                    show ep06_madisoncamera29
                    mad "Calling it a reflex makes me a victim. Choosing it makes me the villain."
                    mc_s "And you prefer being the villain."

                    show ep06_madisoncamera69
                    mad "Villains have more fun. And they live longer."
                    mc_t "She wears the villainy like a shield."

                "Do you think you can ever go back?":
                    hide screen walkthrough_screen
                    mc_s "Do you think you can ever go back?"
                    mad "To what?"
                    mc_s "To before the bitterness. To being whole."
                    mad "I can't unsee what I've seen."
                    mc_s "You could try to heal."

                    show ep06_madisoncamera29
                    mad "You don't understand. The armor isn't on me."
                    mad "It IS me. If I take it off, there's no skin underneath."
                    mad "Just raw nerves."

                    show ep06_madisoncamera69
                    mc_s "That sounds lonely."
                    mad "It's safe."
                    mc_t "She believes she has mutated into this. Irreversibly."

                    $ ep06_mc_advantage_points -= 1
        else:
            mc_s "When you stopped being the good girl, was it your choice?"
            mad "Yes."
            mc_s "You're sure."
            mad "It had to be a choice."
            mc_s "Or maybe it was a reaction. A survival reflex."

            show ep06_madisoncamera29
            mad "Calling it a reflex makes me a victim. Choosing it makes me the villain."
            mc_s "And you prefer being the villain."

            show ep06_madisoncamera69
            mad "Villains have more fun. And they live longer."
            mc_t "She wears the villainy like a shield."


    # Platform Scene - Final Choice
    show ep06_madisoncamera70
    mad "My studio's just two blocks from here. Second floor, above a convenience store."
    mc_s "I have a briefing."
    mad "I know. Everyone knows the famous Osaka detective's schedule."
    mc_t "\"Famous.\" She's mocking me."

    if ep06_madison_path == "love":
        mad "Ten minutes—just help me carry equipment?"
        mc_s "Is that really what you need?"
        mad "I don't know what I need."
        mc_t "That sounded... honest."

    elif ep06_madison_path == "corruption":
        mad "Ten minutes—unless you're scared."
        mc_s "Of you?"
        mad "Of what happens when we're alone."
        mc_t "Thirty minutes on that train and she's still escalating."

    else:  # neutral
        mad "Ten minutes. Prove you're not a coward."
        mc_s "I don't have to prove anything to you."
        mad "You spent thirty minutes trying not to look at me."
        mad "That's proof enough."
        mc_t "She's not wrong."

    jump ep06_madison_station_proposal

# Madison's final proposal at the station
label ep06_madison_station_proposal:
    # Note: ep06_madisoncamera71 is already shown from previous label
    # This is the station exit scene (e6_madisonintro_16)

    # Madison's attitude varies based on:
    # 1. Lies detected (0, 1-2, 3+)
    # 2. Chosen path (love, corruption, neutral)
    # 3. Whether they had sex in ep05 (ep05_confrontation_peaceful)

    show ep06_madisoncamera71

    if ep06_mc_lies_detected >= 3:
        # High lies detected - Madison is cold but still makes the proposal
        mc_t "She's been watching me differently since the train."
        mc_t "Colder. Like she's dissecting a frog."

        if ep06_madison_path == "love":
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 3+ times, love path
                mad "You said you wanted to know me."
                mad "But you sat there and lied to my face three times."
                mad "After fucking me... I thought you'd owe me the truth."
                mc_s "Madison—"
                mad "I'm still making the offer. My studio. Ten minutes."
                mad "But don't talk. I'm sick of your voice."
            else:
                # MC threatened her in ep05, MC lied 3+ times, love path
                mad "You said you wanted to know me."
                mad "But you lied to me three times on that train."
                mad "You walked out on me before, and now you lie."
                mc_s "Madison—"
                mad "I'm still making the offer. My studio. Ten minutes."
                mad "But don't expect me to trust a word you say."

        elif ep06_madison_path == "corruption":
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 3+ times, corruption path
                mad "You lied. Over and over."
                mad "At least we stopped pretending to be good people."
                mad "I gave myself to you that night. You gave me lies today."
                mad "We really deserve each other, don't we?"
                mad "My studio. Ten minutes. Come feed the monster."
            else:
                # MC threatened her in ep05, MC lied 3+ times, corruption path
                mad "You lied. Multiple times."
                mad "At least we both know what we are now."
                mad "Hypocrites."
                mad "We're perfect for each other."
                mad "My studio. Ten minutes. If you want to stop pretending."

        else:  # neutral
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 3+ times, neutral path
                mad "You said no. And you lied doing it."
                mad "After that night... after what we did..."
                mad "You're just a coward hiding behind morality."
                mad "My studio. Ten minutes."
                mad "Prove me wrong."
            else:
                # MC threatened her in ep05, MC lied 3+ times, neutral path
                mad "You said no. And you lied doing it."
                mad "You walked out that night. You lied on this train."
                mad "You're useless to me."
                mad "My studio. Ten minutes."
                mad "Last chance to be useful."

    elif ep06_mc_lies_detected >= 1:
        # Some lies detected - Madison is cautious
        mc_t "She caught me in at least one lie."
        mc_t "But she's still here. She hasn't left."

        if ep06_madison_path == "love":
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 1-2 times, love path
                mad "You weren't completely honest with me."
                mad "But after that night... I guess expecting truth is too much."
                mad "My studio. Ten minutes. Help me with equipment."
                mad "Maybe we can try this again. Better this time."
            else:
                # MC threatened her in ep05, MC lied 1-2 times, love path
                mad "You weren't completely honest with me."
                mad "But after you walked out that night... I get it. You're guarding yourself."
                mad "My studio. Ten minutes."
                mad "Let's start over."

        elif ep06_madison_path == "corruption":
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 1-2 times, corruption path
                mad "You lied. I lied too, probably."
                mad "We're both playing games."
                mad "At least the sex was real."
                mad "My studio's close. You coming or not?"
            else:
                # MC threatened her in ep05, MC lied 1-2 times, corruption path
                mad "You lied. I lied too, probably."
                mad "We're both playing games."
                mad "You walked out that night. I'm offering you a way back in."
                mad "My studio's close. Don't make me wait."

        else:  # neutral
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 1-2 times, neutral path
                mad "You said no."
                mad "Even after that night... you still said no."
                mad "I respect that, I guess. Even if you lied a little."
                mad "But... my studio. Ten minutes."
                mad "If you change your mind."
            else:
                # MC threatened her in ep05, MC lied 1-2 times, neutral path
                mad "You said no."
                mad "You said no that night too. When you walked out."
                mad "I respect that, I guess."
                mad "But... my studio. Ten minutes."
                mad "If you change your mind."

    else:
        # No lies detected - Madison is more open
        mc_t "Thirty minutes of brutal honesty."
        mc_t "And she's looking at me differently now. Like the armor is cracked."

        if ep06_madison_path == "love":
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 0 times, love path
                mad "You were honest with me. Even when it was ugly."
                mad "That's... I haven't had that. Ever."
                mad "After what happened between us..."
                mad "My studio's two blocks away. Come with me?"
                mad "Just ten minutes. I... I don't want to be alone right now."
                mc_t "She sounds like a little girl now."
            else:
                # MC threatened her in ep05, MC lied 0 times, love path
                mad "You were honest with me. Even when it hurt."
                mad "That's... rare."
                mad "You rejected me that night. But at least you respect me enough to tell the truth."
                mad "My studio's two blocks away. Come with me?"
                mad "Just ten minutes. Please."

        elif ep06_madison_path == "corruption":
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 0 times, corruption path
                mad "We both know what we are now."
                mad "Broken. Twisted. And completely honest about it."
                mad "That night proved it. This train ride confirmed it."
                mad "My studio. Now."
                mc_t "This isn't a question. It's a summons."
            else:
                # MC threatened her in ep05, MC lied 0 times, corruption path
                mad "We both know what we are now."
                mad "Broken. Complicated."
                mad "You threatened me that night. But today you showed me your true face."
                mad "My studio. Now."
                mc_t "She likes what she saw. The darkness recognizes the darkness."

        else:  # neutral
            if ep05_confrontation_peaceful:
                # They had sex in ep05, MC lied 0 times, neutral path
                mad "You were honest. I appreciate that."
                mad "Even if the answer was no."
                mad "After that night... I thought maybe things would be different."
                mad "My studio. Ten minutes."
                mad "The door will be unlocked. Just in case."
            else:
                # MC threatened her in ep05, MC lied 0 times, neutral path
                mad "You were honest. I appreciate that."
            mad "Even if the answer was no."
            mad "You said no that night too. At least you're consistent."
            mad "My studio. Ten minutes."
            mad "The door will be unlocked."

    # FINAL SCENE - Madison's pleading proposal (e6_madisonintro_16)
    # Image ep06_madisoncamera71 is already showing from start of this label

    mad "Ten minutes."
    mad "Then you can go play hero."

    mc_t "Last chance to walk away."
    mc_t "Every reason says run. Every instinct says stay."

    #-- End Update
    if htl_episodes == 6.1:
        $ stopAllSubchannels(channel="sfx", fadeout=1)
        $ stopAllSubchannels(channel="amb", fadeout=1.5)
        $ stopAllSubchannels(channel="music", fadeout=2)
        scene eigengrau with rose
        pause 2.0
        $ resetAllVolumes()
        return

    else:
        pass


    # CRITICAL CHOICE - Player decides
    $ show_walkthrough("ep06_madison_studio_decision_menu")
    menu:
        "Let's go.":
            hide screen walkthrough_screen
            mc_s "Let's go."
            if ep06_madison_path == "corruption":
                mc_t "I'm walking straight into hell. And I'm smiling."
            elif ep06_madison_path == "love":
                mc_t "I can't leave her like this."
            else:
                mc_t "I'm going to regret this."

            jump ep06_madison_studio

        "I'm not doing this.":
            hide screen walkthrough_screen
            mc_s "I'm not doing this."
            mad "Fine."

            if ep06_madison_path == "love":
                mc_t "She looks crushed. But she hides it quickly."
            else:
                mc_t "She doesn't look surprised. Just... resigned."

            jump ep06_madison_rejection