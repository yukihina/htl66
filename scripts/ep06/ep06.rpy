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
    $ renpy.free_memory()
    show location_tmpd_m with slowfade
    show tmpd_location zorder 2 with dissolve
    pause 5
    hide tmpd_location with dissolve
    jump ep06_ope


label ep06_ope:
    scene eigengrau
    $ config.rollback_enabled = True
    pause 1.0

    show screen stats_button
    show screen walkthrough_icon

    $ playAudio(japanday_cross, "amb", 1, True, 3.0)
    $ setChannelVolume("amb", 1, 0.6, 0)

    show ep06_opening01 at ken_burns_bottom_to_top
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

    show ep06_opening03 at ken_burns_left_to_right with clouds_inverse
    mc_t "[mo_full_r]'s wrists. Gauze. Pulse."
    mc_t "Three months of visiting hours."

    show ep06_opening04
    mc_t "She's awake now. Talking. Smiling at the nurses."
    mc_t "That smile. I know that smile."

    $ setAllSubchannelsVolume("sfx", 1.0, 1)
    $ setAllSubchannelsVolume("amb", 1.0, 1)

    show ep06_opening05 at ken_burns_right_to_left with fade
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
    wat "[da_full_r]: British subject. [mo_full_r]: Italian national."
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

    show ep06_opening08 with fade
    wat "Of course. We are short-handed, after all. Even... unconventional assets are useful."
    wat "Welcome to the First Investigation Division, Sōsa Ikka. We handle homicides."

    $ playAudio(mc_suspense_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)

    show ep06_opening09 at ken_burns_corner_to_corner3
    wat "Specifically, the homicide of Detective Yamamoto. Found dead last night."
    wat "Professional execution. Three shots. No wasted movement."
    wat "It lacks the... emotional messiness typical of domestic crimes. It feels imported."
    mc_t "Foreign killer. Foreign detective. He's putting the trash together."
    mc_s "Yakuza?"
    wat "Because of the context, the Organized Crime Division, Sotai, has jurisdiction on the motive, but we have jurisdiction on the body."
    wat "Inspector Sato from 'Sotai' requested a liaison from our division. Specifically you."
    mc_s "Why me?"

    $ setAllSubchannelsVolume("amb", 0.0, 1)

    show ep06_opening12 at dramatic_focus_out
    wat "Osaka connections, perhaps."
    wat "Because Sato thinks you fit in."
    wat "You understand the Yakuza. Their crude manners. Their... loudness."
    
    $ setAllSubchannelsVolume("amb", 0.5, 1)

    hide ep06_opening12 with fade
    wat "The clans are obsessed with tradition. With 'Wa'—Harmony."
    wat "They react violently to external elements that look different. That don't belong."
    wat "Sato hopes your... appearance... might provoke a reaction that a Japanese officer could not elicit."

    show ep06_opening10
    mc_t "I'm not a detective to them. I'm bait. Foreign bait."
    wat "In this department, Inspector, we utilize every tool available."

    $ show_walkthrough("ep06_case_attitude_menu")
    menu:
        "[Light] I'll do this right.":
            hide screen walkthrough_screen
            mc_t "I'll investigate thoroughly. I won't give him a reason to doubt my badge."
            $ rm.update("mc", "integrity", 1)

        "[Balance] I wasn't ready for this.":
            hide screen walkthrough_screen
            mc_t "Dead cop. Yakuza war. Three months wasn't enough recovery time for this."

        "[Darkness] Perfect. Time for payback.":
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

    show ep06_shadowdir01 at ken_burns_left_to_right with fade
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

    show ep06_shadowdir03 with fade
    hir "None. Lives alone. Works late Thursdays."
    hir "Returns home past midnight. Drunk, usually. Keys in left pocket."
    anto "Why him?"

    show ep06_shadowdir04
    hir "He's connecting dots. Osaka to Tokyo. Surgical modifications, territory shifts, missing women."
    hir "Last week he requested files on Kudo-kai specifically."

    $ setChannelVolume("amb", 2, 0.3, 1)
    $ setChannelVolume("amb", 1, 0.5, 1)

    show ep06_shadowdir05 at ken_burns_left_to_right with fade
    hir "Smart detective. Dangerous detective."
    hir "You play chess, Antonella?"

    show ep06_shadowdir06 with fade
    anto "No."
    hir "You should learn."
    hir "Chess teaches you how to win wars."

    show ep06_shadowdir07 at ken_burns_bottom_to_top
    hir "You don't attack the king directly. Too obvious. Too defended."
    hir "You remove his pieces. One by one."
    hir "First the knights. Then the bishops. Then the rooks."
    hir "When the king is alone and blind..."

    show ep06_shadowdir08 at dramatic_focus_out
    hir "...he falls without a fight."
    hir "Yamamoto is a knight. Intelligent. Mobile. Dangerous."
    anto "And after the knight falls?"
    hir "The board shifts. Tokyo Metropolitan loses its best investigator."

    show ep06_shadowdir09 at slow_reveal with fade
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

    show ep06_shadowdir12 at ken_burns_right_to_left with fade
    anto "Thursday night. Apartment 204."
    anto "Three shots. Professional spacing."
    anto "The knight falls."

    show ep06_shadowdir13 at dramatic_focus_out
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

    show ep06_execution01 at ken_burns_left_to_right
    yam_t "Seventeen women. Seventeen families asking when I'll find answers."
    yam_t "Surgical chest incisions. Professional precision. Osaka to Tokyo - someone's expanding operations."

    show ep06_execution02 with clouds
    yam_t "11:43 PM. Miyuki called three hours ago. Sounded tired. I told her two more days in Tokyo."
    yam_t "Lied. Probably four more days. Maybe five."
    yam_t "But I'm close. The connection between Osaka and Tokyo - it's here somewhere in these files."

    $ playAudio(door_knock, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_execution03 with hpunch
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

    show ep06_execution04 at focus_shift with fade
    yam_t "Uhm..."
    yam_t "Delivery person?"

    show ep06_execution05
    yam_t "Young."

    show ep06_execution06
    yam_t "European features: Black hair, pale, blue eyes with glasses."

    show ep06_execution07
    yam_t "Curves straining fabric. Wrong size. Abdomen scar visible. Work accident, maybe."

    show ep06_execution08 with fade
    yam_t "Late shift worker. Probably part-time student."
    anto "Delivery for Yamamoto-san. Signature required."
    yam_t "Light accent. Foreign worker."
    yam_t "Wrong apartment probably. Common mistake with Japanese names."

    $ playAudio(door_wood, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.8, 0)
    
    show ep06_execution09 at ken_burns_bottom_to_top with slowfade
    yam "I think you have the wrong—"
    anto "Yamamoto-san? Detective Yamamoto Koji?"
    yam "...Yes?"

    $ setAllSubchannelsVolume("amb", 0.0, 3)
    $ setChannelVolume("sfx", 4, 1, 2)

    yam_t "She knows I'm a detective... How?"
    yam_t "Sender must have specified? Precinct sometimes sends-"

    $ playAudio(guncock9mm, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.8, 0)

    show ep06_execution10 with vpunch

    $ fadeToAudio(heartbeatfast, "sfx", 4, 2.0, True)

    yam_t "European."

    show ep06_execution11 with hpunch
    yam_t "Osaka."

    show ep06_execution12 at slow_reveal with slowflash
    yam_t "Miyuk—"

    $ playAudio(gunshot_glock_3shots, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    scene bloodbg
    show blood_overlay at blood_cover zorder 100
    show ep06_execution13 at impact_shake with shot
    pause 0.6  # Let the blood drip animation complete
    hide blood_overlay


    $ stopAudio("sfx", 4, 3.0)

    anto_t "Professional spacing."
    anto_t "The knight falls."

    $ playAudio(bodyfall_carpet, "sfx", 3, False, 0)
    $ setChannelVolume("sfx", 3, 1, 0)
    $ setChannelVolume("amb", 1, 0.2, 2)
    $ setChannelVolume("amb", 2, 0.1, 2)
    $ setChannelVolume("amb", 3, 0.05, 2)

    show ep06_execution14 at ken_burns_right_to_left with fade
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

    show ep06_crimescene01 at ken_burns_left_to_right
    mc_t "First day back."
    mc_t "First crime scene in three months."

    show ep06_crimescene02 at animated_glitch with flash
    mc_t "The last crime scene I was at..."
    mc_t "I was the one bleeding."

    $ setAllSubchannelsVolume("amb", 0.1, 2)

    show ep06_crimescene03 with fade
    mc_t "Second floor. Apartment 204. Asagaya."
    mc_t "Three yellow markers on the floor."
    mc_t "Gray-haired man crouching by the bullets. Wire-rim glasses. Cheap suit."
    mc_t "That's him. Detective Inspector Sato from Organized Crime."

    $ playAudio(mc_thinking_theme, "music", 1, True, 3)
    $ setChannelVolume("music", 1, 0.5, 1.0)
    $ stopAllSubchannels("sfx", 2.0)

    show ep06_crimescene04 at ken_burns_left_to_right with fade
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

    show ep06_crimescene10 at subtle_zoom_out
    tak "Now, here is the lesson regarding our killer."
    tak "What kind of person executes a cop, then stays to arrange casings in a geometric pattern?"
    mc_s "That depends on how you look at it."

    $ show_walkthrough("ep06_killer_profile_menu")
    menu:
        "[Light] They believed in justice.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 2)
            mc_s "Someone with a code. Distorted, maybe. But they believe they are creating order."
            tak "Order. Yes. A fanatic creates order out of chaos."

        "[Balance] Just following orders.":
            hide screen walkthrough_screen
            mc_s "Someone doing a job. Following a manual. No emotion involved."
            tak "A machine made of meat. Possible."

        "[Darkness] They enjoyed the kill.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -2)
            mc_s "A sadist. Someone who leaves a signature to taunt us."
            tak "Arrogance. That is a weakness we can exploit."

    tak "Whatever they are, they are disciplined."
    tak "Precisely. Stand up. Let's look at the victim."

    show ep06_crimescene05 with fade
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

    show ep06_crimescene08 at ken_burns_left_to_right
    tak "You know why Watanabe gave you to me?"
    mc_s "Because I'm expendable."
    tak "We are all expendable. That's part of the job."
    tak "He gave you to me because we are both 'broken' tools in their eyes."
    tak "You are a gaijin. I am... inconveniently stubborn."
    tak "They put the broken tools in the basement so we don't ruin the display case."
    tak "But broken tools have jagged edges. They cut deeper."
    mc_t "Useful. He thinks I'm useful."
    tak "Come. Look at where he fell."

    show ep06_crimescene11 with fade
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

    show ep06_crimescene13 with fade
    tak "Yamamoto was tracking a specific anomaly. Murders."
    tak "Seventeen women over three months. Osaka to Tokyo pipeline."
    tak "All found with surgical incisions."
    mc_s "Breast tissue removed?"
    tak "Systematically. Look at the timeline on the laptop."

    call screen confirm(
        message="Gore content ahead. Continue?",
        yes_action=[SetVariable("e6_gore", True), Return()],
        no_action=[SetVariable("e6_gore", False), Return()]
    )

    $ playAudio(officechair_sit, "sfx", 5, False, 0)
    $ setChannelVolume("sfx", 5, 0.3, 0)
    
    show ep06_crimescene14 with vpunch
    mc_t "Bodies. Female. Surgical cuts."

    if e6_gore:
        $ playAudio(mouseclick, "sfx", 1, False, 0)
        $ setChannelVolume("sfx", 1, 1, 0)
        show ep06_crimescene15 at animated_glitch, concentrate with fade
        tak "Victim one. Three months ago. Look at the incision."
        mc_t "Clean sutures. Minimal bruising."
        mc_s "Surgical precision. Looks like a professional augmentation job."
        tak "Correct. A doctor—or someone very skilled—did this."

        $ playAudio(mouseclick, "sfx", 2, False, 0)
        $ setChannelVolume("sfx", 2, 1, 0)
        show ep06_crimescene16 at animated_glitch, concentrate with fade
        tak "Victim eight. Two months ago."
        mc_t "Jagged edges. Bruising."
        mc_s "Getting sloppy. There's infection around the wound."
        tak "The hand is shaking. The time is shortening."

        $ playAudio(mouseclick, "sfx", 3, False, 0)
        $ setChannelVolume("sfx", 3, 1, 0)
        show ep06_crimescene17 at animated_glitch, concentrate with fade
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

    show ep06_crimescene18 with fade
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
        "[Light] Stop them legally.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 2)
            mc_s "We build the case. We prosecute. We show them that the law is stronger than their greed."
            tak "The noble path. Hard. Slow. But necessary for civilization."

        "[Balance] Just catch them.":
            hide screen walkthrough_screen
            mc_s "We find them and we cage them. I don't care about the philosophy."
            tak "Pragmatic. Good. Emotion clouds judgment."

        "[Darkness] They deserve everything.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -2)
            mc_s "People who do this aren't human. I don't care what happens to them when we find them."
            tak "Be careful. If you hunt monsters with rage, you might forget when to stop."

    show ep06_crimescene20
    tak "The autopsy results will be ready tomorrow... Dr. Hatanaka."
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
    scene eigengrau with lines
    show next_morning
    pause 3
    show location_denenchofu_m with slowfade
    show home_location zorder 2 with dissolve
    pause 5
    hide home_location with dissolve
    jump ep06_mornwithamber


label ep06_mornwithamber:
    scene eigengrau

    $ playAudio(earlymor, "amb", 1, True, 2.0)
    $ setChannelVolume("amb", 1, 0.4, 2)
    $ playAudio(mc_room_night, "amb", 2, True, 2.0)
    $ setChannelVolume("amb", 2, 0.2, 2)
    $ playAudio(clockalarm, "sfx", 1, True, 5.0)
    $ setChannelVolume("sfx", 1, 0.8, 5)

    show ep06_ambermorn01 at ken_burns_right_to_left
    pause

    $ stopAudio("sfx", 1, 1.0)
    $ playAudio(clockalarm_stop, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    show ep06_ambermorn02 with vpunch
    mc_s "Shit... late again."
    mc_t "Ugh. Stuck. Something heavy is pinning the blanket down."
    mc_t "Warm. Too warm. And soft."
    mc_t "Wait. Skin?"

    show ep06_ambermorn03 at ken_burns_left_to_right with hpunch
    amb "No."
    mc_s "Wh— Amber?!"
    mc_s "What are you doi—"
    amb "I said no. You're not going anywhere."

    show ep06_ambermorn04 with vpunch
    amb "Haah..."
    mc_t "Naked. She's completely naked straddling me."
    mc_t "But that look... soft. Like she's looking at a puppy, not a man."

    if ss.get("amber", "strike") == 1:
        mc_s "Amber, we talked about this..."
        amb "We talked. You ran. I'm just holding you here."

    elif ss.get("amber", "strike") == 2:
        mc_s "You're pushing your luck..."
        amb "I'm pushing you. Don't look away from me."

    else:
        mc_s "Amber, when did you— Nevermind!"
        mc_s "I gotta get up..."

    show ep06_ambermorn05 at subtle_zoom_out
    amb "Shut up and feel this."
    mc_t "Her skin is burning against mine. Hell."
    mc_t "Wet. She's already wet."
    mc_t "I need to push her off, but my hands aren't listening."

    $ show_walkthrough("ep06_amber_first_decision_menu")
    menu:
        "[Corruption] Show me." if ss.get("amber", "strike") == 0 and rm.get("amber", "cor") >= 20:
            hide screen walkthrough_screen
            mc_s "Show me what you were doing."

            $ e6_amber_path = "corruption"
            jump ep06_mornwithamber_corruption

        "[Neutral] You're impossible.":
            hide screen walkthrough_screen
            mc_s "You're impossible."

        "[Love] I missed this.":
            hide screen walkthrough_screen
            mc_s "I missed this too."

            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "[Reject] Not now.":
            hide screen walkthrough_screen
            mc_t "No. Not today. I can't get pulled into this vortex today."

            $ e6_amber_path = "rejection"
            $ ss.add("amber", "strike")

            if ss.get("amber", "strike") == 1:
                $ show_custom_notification("strike1")
            elif ss.get("amber", "strike") == 2:
                $ show_custom_notification("strike2")
            elif ss.get("amber", "strike") >= 3:
                $ show_custom_notification("strike3")
            jump ep06_mornwithamber_rejection

    $ playAudio(amber2_love_theme, "music", 2, True, 5.0)
    $ setChannelVolume("music", 2, 0.5, 0)

    show ep06_ambermorn06 at subtle_zoom_in
    mc_t "She stopped moving. Her eyes dropped."
    amb "This scar..."
    mc_s "What about it?"

    show ep06_ambermorn07 with vpunch
    amb "It's so fucking hot."
    mc_t "That look... the sweetness is gone. Just hunger now."

    $ show_walkthrough("ep06_amber_intimacy_response_menu")
    menu:
        "[Love] You see me." if ss.get("amber", "strike") == 0 and rm.get("amber", "trust") >= 35:
            hide screen walkthrough_screen
            mc_s "You've always seen me."

            $ e6_amber_path = "love"
            jump ep06_mornwithamber_love

        "[Neutral] You like broken things?":
            hide screen walkthrough_screen
            mc_s "You like broken things?"
            amb "You'll see..."

            $ e6_amber_path = "neutral"
            jump ep06_mornwithamber_neutral

        "[Corruption] Like the view?":
            hide screen walkthrough_screen
            mc_s "Like what you see?"
            amb "Oh... I'm looking at something that really turns me on."

            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)
            $ e6_amber_path = "neutral"
            jump ep06_mornwithamber_neutral


label ep06_mornwithamber_neutral:
    scene eigengrau with fade
    $ stopAudio("music", 2, 2.0)
    $ playAudio(moan_breath3, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_ambermorn08 with vpunch
    amb "God... wait—"
    mc_s "Too much?"
    amb "No. Just... slow at first."
    mc_s "You're so tight, Amber."
    amb "Shh. Just breathe. Let me take it in."

    $ playAudio(moan_breath, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    show ep06_ambermorn09 at ken_burns_left_to_right
    amb "Yeah. Fuck, yeah. There it is."
    amb "Mmm... fuuuuck."
    mc_s "Mmmm..."
    amb "Don't just make noises. Tell me. Use your words."

    $ show_walkthrough("ep06_amber_sex_neutral_talk_menu")
    menu:
        "[Love] I love you.":
            hide screen walkthrough_screen
            mc_s "I love you, Amber."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "[Corruption] Fucking perfect.":
            hide screen walkthrough_screen
            mc_s "Your pussy's perfect."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

        "[Neutral] Only you.":
            hide screen walkthrough_screen
            mc_s "No one else compares."
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)

    $ playAudio(moan_breath2, "sfx", 3, False, 0)
    $ setChannelVolume("sfx", 3, 1, 0)

    show ep06_ambermorn10 with vpunch
    amb "Mmm... can you feel that?"
    amb "Deeper... I need it deeper."
    mc_s "You look... lost."
    amb "What the fuck are you talking about? I'm not lost. Just yours."

    show ep06_ambermorn11 at ken_burns_right_to_left
    amb "You feeling how wet I am?"
    mc_s "Yeah... I can't stop myself."
    amb "Good."
    amb "Now... what do you want?"
    mc_s "I get a choice?"
    amb "Don't waste it."
    mc_s "But..."
    
    show ep06_ambermorn14 with hpunch
    amb "Shh..."
    mc_s "Amber?"
    amb "Not inside right now. I want to play with you first."
    amb "Tell me where you want me."


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
    scene eigengrau
    show ep06_ambermorn12 at ken_burns_bottom_to_top with fade
    mc_s "You look hungry."
    amb "Starving."
    amb "I want to taste every drop of you."

    $ playAudio(fellatio1, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)
    
    show ep06_anim01 at focus_shift, dizzyness
    mc_s "Jesus— Amber! Slow down!"
    amb "Mmph... Gawk.... Nnh..."
    mc_s "Fuck... you're so eager."
    amb "Mmph!"

    show ep06_anim02 at focus_shift, dizzyness
    amb "Mmm... better?"
    mc_s "Yeah. Just like that. Use your tongue."
    amb "I can hear your breath hitching... You like this view?"
    mc_s "I love watching you serve me."

    $ stopAudio("sfx", 1, 2)
    show ep06_ambermorn13 with fade
    mc_s "Wait. Hold it."
    amb "Mmph?"
    mc_s "Too close. If you keep sucking like that, I'm finishing right now."
    amb "Mmm... then choose. What comes next?"
    jump ep06_mornwithamber_neutral_sexmenu


label ep06_mornwithamber_neutralboobj:
    $ ss.add("amber", "titjob")
    scene eigengrau
    show ep06_ambermorn15 at ken_burns_left_to_right with fade
    mc_s "Look at you... all spread out."
    amb "Don't just look. Use them."
    amb "Slide it right here. Make them heavy."

    show ep06_anim03 at focus_shift, dizzyness
    mc_s "Fuck... so soft."
    amb "Mmm... yeah? Slippery?"
    amb "Ah... ah... keep going."

    show ep06_anim04 at focus_shift, dizzyness
    mc_s "That tongue..."
    amb "I want to taste it on my skin. Coat me."
    mc_s "You're squeezing so hard..."
    amb "Because you're mine."

    show ep06_ambermorn16 with fade
    mc_s "Amber, I'm—"
    amb "Not yet."
    amb "I'm enjoying the view too much. What's next?"
    jump ep06_mornwithamber_neutral_sexmenu


label ep06_mornwithamber_neutral_continue:
    scene eigengrau
    show ep06_ambermorn17 with fade
    amb "You know why we fit?"
    mc_s "Why?"
    amb "Your darkness... matches mine."
    mc_s "You're crazy."
    amb "We both are."

    $ show_walkthrough("ep06_amber_neutral_climax_menu")
    menu:
        "[Love] Only you get me.":
            hide screen walkthrough_screen
            mc_s "Only you understand."
            amb "Never letting go."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

        "[Corruption] Take it all.":
            hide screen walkthrough_screen
            mc_s "Take everything."
            amb "Gladly."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

        "[Corruption] Broken together.":
            hide screen walkthrough_screen
            mc_s "We're both fucked up."
            amb "Perfect fit."
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)

    show ep06_ambermorn18 with vpunch
    $ ss.add("amber", "sex")
    mc_s "On your back."
    amb "Ah!"
    mc_s "Better?"
    amb "Yes! Harder!"

    $ playAudio(moan_generic, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_anim06 at focus_shift, dizzyness
    mc_s "Look at you... gone."
    amb "Fuck... [mc_name]!"
    mc_s "Taking it all?"
    amb "Deep! Too deep!"

    show ep06_anim05 at focus_shift, dizzyness
    amb "Ah... ah... ah..."
    amb "Need it... don't stop!"

    show ep06_ambermorn19
    mc_s "Amber... I'm close."
    amb "Inside."
    mc_s "Sure?"
    amb "Fill me."
    mc_s "Mouth. Open."

    show white zorder 1.0 at ejaculation_flash

    $ playAudio(moan_cum_generic, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    show ep06_ambermorn20 at vpunch with flash
    $ ss.add("amber", "creampie")
    amb "Mmph! Gawk!"
    mc_s "Cumming!"
    amb "Nghhh!"
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_postclimax:
    scene eigengrau
    show ep06_ambermorn21 at ken_burns_top_to_bottom with vpunch
    if e6_amber_path == "corruption":
        amb "You made a mess of me..."
        mc_s "You asked for it."
        amb "I did. I always do."
        $ playAudio(amber2_love_theme, "music", 2, True, 5.0)
        $ setChannelVolume("music", 2, 0.5, 0)

        amb "It reminds me of that day... you remember?"
        
        show ep06_ambermorn22 with clouds_inverse
        amb "When I butchered my hair. I wanted to kill the 'perfect [dau_r_low]'."
        amb "Everyone looked at me with horror. Like I was a freak."
        mc_s "I didn't."
        amb "No. You looked at me like I was... interesting."

        show ep06_ambermorn23 with fade
        amb "You saw the cracks in me, and instead of fixing them, you touched them."
        amb "That's why I let you do this to me. Because you like the damage."

        $ show_walkthrough("ep06_amber_corruption_postclim_menu")
        menu:
            "[Love] You don't scare me.":
                hide screen walkthrough_screen
                mc_s "Your cracks don't scare me. They let me in."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "[Neutral] We fit perfectly.":
                hide screen walkthrough_screen
                mc_s "We're both broken. That's why we fit."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                $ rm.update("amber", "cor", 1)
                $ check_levels("amber", "cor", 1)

            "[Reject] Stop overthinking.":
                hide screen walkthrough_screen
                mc_s "Stop analyzing. You're just a toy I like to play with."
                $ rm.update("amber", "trust", -1)
                $ check_levels("amber", "trust", -1)
        
        $ stopAudio("music", 2, 2.0)
        jump ep06_mornwithamber_ending

    elif e6_amber_path == "love":
        amb "I feel..."
        mc_s "How?"
        amb "Safe. I feel safe."

        $ playAudio(amber2_love_theme, "music", 2, True, 5.0)
        $ setChannelVolume("music", 2, 0.5, 0)
        amb "It takes me back... to the living room floor."

        show ep06_ambermorn22 with clouds_inverse
        amb "[mo_r] wouldn't even look at me. She told [da_r] I looked like a monster. That I was unlovable."
        mc_s "I found you sitting on the floor in the dark."
        amb "You didn't tell me to fix it. You crawled in there with me and kissed my jagged hair."

        show ep06_ambermorn23 with fade
        amb "You told me you liked it short... because you could finally see my eyes clearly."
        amb "You turned my shame into something beautiful. Just like you did right now."
        amb "I love you so much it hurts."

        $ show_walkthrough("ep06_amber_love_postclim_menu")
        menu:
            "[Love] I mean it.":
                hide screen walkthrough_screen
                mc_s "I meant it then, and I mean it now. I love seeing you."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "[Love] Test me.":
                hide screen walkthrough_screen
                mc_s "I'm not going anywhere. You can lean on me forever."
                $ rm.update("amber", "trust", 2)
                $ check_levels("amber", "trust", 2)

            "[Love] Help me understand.":
                hide screen walkthrough_screen
                mc_s "Let me help you believe it. Every day."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
        
        $ stopAudio("music", 2, 2.0)
        jump ep06_mornwithamber_ending

    elif e6_amber_path == "neutral":
        amb "This... us... it works."
        mc_s "Yeah. It does."

        $ playAudio(amber2_love_theme, "music", 2, True, 5.0)
        $ setChannelVolume("music", 2, 0.5, 0)
        amb "You've always had my back. Even back then."
        
        show ep06_ambermorn22 with clouds_inverse
        amb "When I cut it all off... [mo_r] screamed. [da_r] left the room."
        mc_s "I remember. You looked like a boy."
        amb "You didn't laugh though. You said I looked like a warrior."

        show ep06_ambermorn23 with fade
        amb "No one else said that. Everyone else just saw a mistake."
        amb "But you saw strength. Even when I was crying."
        amb "That's why I trust you with my body."

        $ show_walkthrough("ep06_amber_neutral_postclim_menu")
        menu:
            "[Love] Perfect to me.":
                hide screen walkthrough_screen
                mc_s "You've always been perfect to me. Warrior or not."
                $ rm.update("amber", "trust", 3)
                $ check_levels("amber", "trust", 3)

            "[Neutral] Warriors together.":
                hide screen walkthrough_screen
                mc_s "We're a team. Two warriors against the world."
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)
                $ rm.update("amber", "cor", 1)
                $ check_levels("amber", "cor", 1)

            "[Reject] Time to go.":
                hide screen walkthrough_screen
                mc_s "We should get ready."
                $ rm.update("amber", "trust", -1)
                $ check_levels("amber", "trust", -1)
        
        $ stopAudio("music", 2, 2.0)
        jump ep06_mornwithamber_ending


label ep06_mornwithamber_ending:
    scene eigengreau 
    show ep06_ambermorn24 at ken_burns_right_to_left with fade
    if e6_amber_path == "corruption":
        amb "You going to the station like that?"
        mc_s "Like what?"
        amb "Smelling like your favorite toy."
        mc_s "I should shower."
        amb "Don't. Keep it on you."
        amb "Let everyone know exactly who owns that cock."
        mc_t "She wants to mark her territory. Fine by me."

    elif e6_amber_path == "love":
        amb "Do you really have to put that on?"
        mc_s "It's work, Amber. Shirt and tie."
        amb "I hate it. It covers up all my favorite parts."
        amb "Go ahead, play Detective. But remember who this body belongs to when you come home."
        mc_s "I think I know."
        amb "Good. Because I'm not sharing the best parts of you with anyone."
        mc_t "Strange... No insults. No sharp edges."
        mc_t "Usually she's sour. Foul-mouthed. Always looking for a fight."
        mc_t "But this... she's actually softening."
        mc_t "Territorial and sweet. I really like it."
    
    else:
        amb "You know the truth now, right?"
        mc_s "What truth?"
        amb "This pussy owns you."
        mc_s "Pretty sure that's not how ownership works."
        amb "It is now. Any objections, Detective?"
        mc_s "...No ma'am."
        amb "That's what I thought."
        mc_t "She always needs the last word. I'm not complaining."
    
    $ stopAllAudio(2.0)
    jump ep06_madisonintro


label ep06_mornwithamber_corruption:
    $ amber_cor_choices += 1
    $ rm.update("amber", "cor", 10)
    $ check_levels("amber", "cor", 10)

    $ playAudio(amber_sexy_theme, "music", 1, True, 10)
    $ setChannelVolume("music", 1, 0.5, 0)
    
    scene eigengrau with fade
    show ep06_ambermorn25 at subtle_zoom_in with vpunch
    amb "I was getting impatient..."
    mc_s "So you started without me?"
    amb "I couldn't wait. Look at me... open for you."
    mc_s "Spread them wider. I want to see everything."
    amb "Like this? You pervert... staring right inside."

    show ep06_ambermorn26
    amb "I was touching myself... imagining your hands..."
    mc_s "And?"
    amb "Imagining you using me. Like a toy. However you want."
    mc_s "Show me. Show me how a toy touches itself."
    amb "Mmm... just circling... getting it wet for you."

    show ep06_ambermorn27 at subtle_zoom_in
    amb "See? I'm soaking."
    mc_s "Filthy. You're leaking everywhere."
    amb "Touch it. Check if I'm ready."

    $ playAudio(bodyfall_carpet, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.8, 0)
    $ setChannelVolume("music", 1, 0.1, 8)

    show ep06_ambermorn28 at ken_burns_left_to_right with vpunch
    mc_s "Enough watching."
    amb "Ah! You're rough..."
    mc_s "You said you wanted to be used. So I'm taking what's mine."
    amb "Yes... please... break me."

    $ playAudio(moan_breath, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.8, 0)

    show ep06_ambermorn29 at subtle_zoom_out
    mc_s "Tight. Relax."
    amb "Fuck... your fingers..."
    mc_s "Stretching you out. Making room."
    amb "Deeper... ruin me."

    show ep06_ambermorn30
    mc_s "You like being forced open?"
    amb "I love it... I love belonging to you."
    mc_s "Then beg for it."
    amb "Please... fuck me hard. Don't hold back."
    mc_s "Good. But toys don't get to demand things. They get chosen."
    mc_s "You're just a collection of parts waiting for me."
    amb "Yes... use me... mouth, tits, ass... anything."
    mc_s "Hold still. Let me decide where I want to start."


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
    scene eigengrau
    $ ss.add("amber", "blowjob")

    $ playAudio(licklolli, "sfx", 3, False, 0)
    $ setChannelVolume("sfx", 3, 0.8, 0)

    show ep06_ambermorn31 at ken_burns_bottom_to_top with fade
    mc_s "Ass up. Face down. That's a good view."
    amb "Mmph! Gawk!"
    mc_s "I've got you. Don't pull back. Take it deeper."
    amb "Glk... Mmph...!"

    $ stopAudio("sfx", 3, 1)

    show ep06_anim07 at focus_shift, dizzyness
    mc_s "Look at that mess... slobbering all over me."
    amb "Slurp... Mmph! Gulp!"
    mc_s "That's it. Be a good little slut. Make it wet."
    amb "Mmm... Gawk!"

    show ep06_ambermorn32 at impact_shake with fade
    mc_s "Stop."

    $ playAudio(moan_breath2, "sfx", 4, False, 0)
    $ setChannelVolume("sfx", 4, 1, 0)

    amb "Mmph? ...Gulp."
    mc_s "Look at your face. Covered in spit. Desperate."
    amb "More... please... use my throat."
    mc_s "Not yet. Hold that pose while I decide what to use next."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_boobjob:
    scene eigengrau
    $ ss.add("amber", "titjob")

    show ep06_ambermorn33 at ken_burns_bottom_to_top with fade
    mc_s "Tongue out."
    amb "Aah... Mmm..."
    mc_s "Don't lick. Just stay there and look desperate."
    amb "So close... please... let me taste..."
    mc_s "Actually... no. Changed my mind."

    show ep06_ambermorn34 at ken_burns_left_to_right with hpunch
    amb "Ah!"
    mc_s "I don't want a show anymore. I want to fuck them."
    mc_s "On your back. Squeeze them together."
    amb "Like... this? You want to use them?"
    mc_s "Tighter. Make a hole for me. I'm going to ruin them."
    amb "Yes... break me..."
    mc_s "Hold still. I haven't decided how to finish you yet."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_assjob:
    scene eigengrau
    $ ss.add("amber", "assjob")

    show ep06_ambermorn35 with vpunch
    amb "You want this ass? It's right here."
    mc_s "Look at you. Rubbing against me like a bitch in heat."
    mc_s "Is that all you are? Just a piece of meat looking for a pole?"
    amb "Yes... Mmm... Just meat... rubbing against you..."
    mc_s "Disgusting. Grind harder. Earn it."
    amb "God... please... stop teasing... wreck me."

    show ep06_anim08 at focus_shift, dizzyness
    mc_s "Beg. Show me how desperate you are to be used."
    amb "Ah... ah... I'm just a hole... please..."
    mc_s "A hole for what? Say it."
    amb "For your cock... fuck me... make me regret it!"

    $ playAudio(femexhale, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_ambermorn36 at subtle_zoom_in with hpunch
    amb "Ah! You're going to do it?"
    mc_s "Spread them. Wide. I want to inspect the merchandise before I break it."
    amb "Look... pink and gaping... waiting for you..."
    mc_s "Hold it open. Let me see if you're loose enough to take me."
    amb "Ruin it... turn me inside out..."
    mc_s "Stay right there. I'm deciding which hole deserves to be punished."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_footjob:
    scene eigengrau
    $ ss.add("amber", "footjob")

    show ep06_ambermorn37 at ken_burns_left_to_right
    mc_s "Look at you. You're better with your feet than most whores are with their hands."

    $ playAudio(moan_breath, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    amb "Mmm... wrapping them around... do you like it?"
    mc_s "Yeah, good girl. Know your place. Squeeze harder."

    show ep06_ambermorn38
    mc_s "Just the toes. Tease it."
    amb "Right here? Mmm..."
    mc_s "Look at that focus. Desperate to please me even with your toes."
    mc_s "Pathetic. And fucking hot."
    amb "I want to make it twitch... make it leak for me..."
    mc_s "Enough playing with your food. Hold it there."
    mc_s "I need to decide which part of you I'm going to break next."
    jump ep06_mornwithamber_corruption_sexmenu


label ep06_mornwithamber_cor_continue:
    scene eigengrau
    $ ss.add("amber", "oral")

    $ playAudio(bed_laying, "sfx", 3, False, 0)
    $ setChannelVolume("sfx", 3, 0.8, 0)

    show ep06_ambermorn39 with vpunch
    mc_s "Face down. Ass up."
    amb "Ah... your tongue..."
    mc_s "Let me taste everything."
    amb "Yes... right there... eat me."

    show ep06_ambermorn40 with hpunch
    $ ss.add("amber", "sex")
    
    mc_s "Mine. Every inch of this skin is mine."

    $ playAudio(moan_breath2, "sfx", 4, False, 0)
    $ setChannelVolume("sfx", 4, 1, 0)
    amb "OH! Fuck... yes! Own me!"
    mc_s "You don't even fight back. You just take it."
    amb "Use me... break me... I'm yours!"

    show ep06_ambermorn41 with vpunch
    mc_s "On your back. Now!"
    amb "Look... gaping for you..."
    mc_s "Look at yourself. Just a hole waiting to be filled."
    amb "Fill it... stretch it until it hurts!"

    show ep06_ambermorn42 at ken_burns_top_to_bottom
    mc_s "Choking on it? Good."
    amb "Ghk... harder... squeeze..."
    mc_s "Your life is in my hands right now. And you're smiling."
    amb "Yes... kill me with it... [mc_name]!"

    show ep06_ambermorn43 at ken_burns_right_to_left with hpunch
    amb "Fuck... too deep... hitting the bottom!"
    mc_s "You're just a ragdoll. I can toss you wherever I want."
    amb "Mmm... yes... toss me around... wreck me..."

    show ep06_ambermorn44 with fade
    mc_s "Bounce. Earn your keep."
    amb "Is it good? Am I doing it right?"
    mc_s "Doesn't matter. You're just a warm sleeve keeping my cock happy."
    amb "Yes... just a sleeve... use it..."

    show ep06_ambermorn45
    amb "Can't... think... brain... empty..."
    mc_s "Perfect. Mindless little slut. That's all you need to be."

    show ep06_ambermorn46 with hpunch
    amb "Ah! Ah! You're splitting me!"
    mc_s "Taking my load. That's your only job right now."
    amb "Cum! Ruin me! Fill your slut up!"

    show white zorder 1.0 at ejaculation_flash
    show ep06_ambermorn47 at vpunch with flash
    $ ss.add("amber", "creampie")

    mc_s "Take it!"
    amb_y "AAAAH! YES! WARM!"
    mc_s "Look at that. Leaking my mess. Like a used trash can."

    $ show_walkthrough("ep06_amber_corruption_sex_menu")
    menu:
        "[Corruption] You're mine.":
            hide screen walkthrough_screen
            mc_s "You're mine completely. Marked inside and out."
            $ rm.update("amber", "cor", 2)
            $ check_levels("amber", "cor", 2)

        "[Neutral] Fucking perfect.":
            hide screen walkthrough_screen
            mc_s "Fucking perfect. A perfect cumdump."
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)

        "[Love] Good girl.":
            hide screen walkthrough_screen
            mc_s "Good girl. You took it all."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

    $ stopAllSubchannels("music", 2.0)

    show ep06_ambermorn48 at ken_burns_left_to_right with slowfade
    mc_s "Jesus... Amber..."
    amb "Mmm... so warm... leaking out..."
    amb "I can't lose it. It's mine."
    mc_s "You're... cleaning it up?"
    amb "Slurp... every drop... delicious..."

    show ep06_ambermorn49
    amb "Mmm... All gone."
    mc_s ". . ."
    amb "Don't look at me like that."
    mc_s "Like what?"
    amb "Like I'm... like I'm broken. Like—"
    mc_s "It's okay, Amber."
    amb "This is where I belong, [mc_name]. Right here."

    $ ep06_ach_ambcor = True
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_love:
    $ amber_love_choices += 1
    $ rm.update("amber", "trust", 10)
    $ check_levels("amber", "trust", 10)
    
    show ep06_ambermorn50 at ken_burns_bottom_to_top with vpunch
    amb "You really see me?"
    mc_s "I do. I see the only person who never gave up on me."
    amb "God... say that again. Please."
    mc_s "You're the best thing in my life, Amber."
    amb "I... I don't know how to do this. I don't know how to be..."
    mc_s "You don't have to do anything."

    $ playAudio(shortmakeout, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.8, 0)

    show ep06_ambermorn51 at zoom_out with vpunch
    mc_s "Come here. Let me show you."
    amb "Ah... gentle... you're being so gentle..."
    mc_s "Because you deserve it."
    amb "Mmm... [mc_name]..."
    mc_s "Don't hide from me. Open up."
    amb "I can't hide... not when you kiss me like that. I'm yours."


label ep06_mornwithamber_love_sexmenu:
    $ show_walkthrough("ep06_mornwithamber_love_sexmenu")
    menu:
        amb "How? How do you want to love me?"

        "Let me show you." if not e6_amber_love_worship_seen:
            hide screen walkthrough_screen
            mc_s "Let me show you exactly how beautiful you are."
            $ e6_amber_love_worship_seen = True
            jump ep06_mornwithamber_love_worship

        "Let me taste you." if not e6_amber_love_oral_seen:
            hide screen walkthrough_screen
            mc_s "Let me taste you first. I want to memorize you."
            $ e6_amber_love_oral_seen = True
            jump ep06_mornwithamber_love_oral

        "Let me touch you." if not e6_amber_love_assjob_seen:
            hide screen walkthrough_screen
            mc_s "Let me love every inch of you with my hands."
            $ e6_amber_love_assjob_seen = True
            jump ep06_mornwithamber_love_assjob

        "Let me hold you." if (e6_amber_love_worship_seen and e6_amber_love_oral_seen and
                              e6_amber_love_assjob_seen):
            hide screen walkthrough_screen
            mc_s "Let me hold you close while we make love."
            jump ep06_mornwithamber_love_hold


label ep06_mornwithamber_love_worship:
    scene eigengrau
    $ ss.add("amber", "pussyjob")

    show ep06_ambermorn52 at ken_burns_corner_to_corner3 with fade
    mc_s "Every inch of you... so soft."
    amb "Mmm... [mc_name]..."
    mc_s "I want to memorize this skin. Worship it."
    amb "Don't... you're going to make me cry."
    mc_s "Why?"
    amb "Because no one touches me like this. With so much care."
    mc_s "Come here. Sit on me."

    $ setAllSubchannelsVolume("music", 0.2, 2.0)
    show ep06_anim09  at focus_shift, dizzyness
    amb "Ah... yes... right there..."
    mc_s "Your heartbeat is racing."
    amb "Because of you. I love feeling your hair... holding you close."

    show ep06_anim10 at focus_shift, dizzyness
    amb "God... it feels so good..."
    mc_s "You're beautiful, Amber. Perfect."
    amb "I'm not perfect. I'm a mess."
    mc_s "To me, you're perfect. And I'm going to prove it to you."
    amb "Okay... show me more. Don't stop."
    jump ep06_mornwithamber_love_sexmenu


label ep06_mornwithamber_love_oral:
    scene eigengrau
    $ ss.add("amber", "oral")

    $ setAllSubchannelsVolume("music", 0.5, 2.0)
    show ep06_ambermorn53 at ken_burns_right_to_left with fade
    mc_s "Relax... let your legs fall open."
    amb "I can't... I'm shaking."
    mc_s "Why? You're safe with me."
    amb "Because this is... it's so weird. Looking at me like that..."
    mc_s "Shhh... Stop thinking. Just feel my tongue."
    amb "Okay... yes... just you..."

    $ setAllSubchannelsVolume("music", 0.2, 2.0)
    $ playAudio(moan_generic, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.5, 0)

    show ep06_anim11 at focus_shift, dizzyness
    mc_s "Mmm... you taste so sweet, Amber."
    amb "Oh god... [mc_name]..."
    amb "There... right there... don't stop..."
    mc_s "I'm not stopping. I wanna make you feel good."
    amb "You are... you're making me feel everything."
    jump ep06_mornwithamber_love_sexmenu


label ep06_mornwithamber_love_assjob:
    scene eigengrau
    $ ss.add("amber", "assjob")

    $ setAllSubchannelsVolume("music", 0.2, 2.0)
    show ep06_ambermorn54 at ken_burns_bottom_to_top with fade
    amb "I want to make you feel good... using my body."
    mc_s "Amber, you don't have to prove anything."
    amb "I know. That's why I want to do it. Just... feel how soft I am for you."

    $ setAllSubchannelsVolume("music", 0.2, 2.0)
    show ep06_anim12 at focus_shift, dizzyness
    mc_s "God... you feel amazing against me."
    amb "Mmm... you like it? Just my skin?"
    mc_s "Yeah. I can't look away..."
    amb "When you touch me... I actually believe it."
    jump ep06_mornwithamber_love_sexmenu


label ep06_mornwithamber_love_hold:
    scene eigengrau

    $ playAudio(female_hmm2, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(bed_laying, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.9, 0)

    show ep06_ambermorn55 at ken_burns_left_to_right with hpunch
    amb "I love you... haa..."
    mc_s "I know."
    amb "Please... stop waiting. Make me yours."
    
    $ stopAllSubchannels("music", 2.0)

    show ep06_ambermorn56
    mc_s "Not yet... look at us."
    amb "Kiss me... nnh... please..."
    mc_s "Just a second. Feel how close we are."
    amb "Mmm... you're teasing me..."

    show ep06_ambermorn57 with hpunch
    $ ss.add("amber", "sex")

    amb "Ah... let me..."
    mc_s "Slowly... relaxing for me..."
    amb "Haa... ah... God... [mc_name]..."
    mc_s "That's it. All the way in."

    $ playAudio(femexhale, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_ambermorn58 with hpunch
    amb "So deep... I have to close my eyes."
    mc_s "It's okay. I've got you."
    amb "Mmm... your hand... feels so safe..."
    mc_s "Let go, Amber. Just feel it."

    show ep06_ambermorn59
    mc_s "Look at me. Right here."
    amb "Nnh... I see you..."
    mc_s "Who am I?"
    amb "Mine. Just mine."

    $ playAudio(shortmakeout, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_anim13 at focus_shift, dizzyness
    amb "Mmph... [mc_name]... kiss me!"
    mc_s "Mmph..."
    amb "Haa... yes... just like that... don't stop..."

    show ep06_ambermorn60 at concentrate
    mc_s "Look at you... touching yourself."
    amb "Ah... ah... can't help it... feels too good!"
    mc_s "Beautiful. You're absolutely beautiful."
    amb "Deeper! Please... hit that spot!"

    $ playAudio(moan_generic, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 1, 0)

    show ep06_anim14 at focus_shift, ken_burns_right_to_left
    mc_s "Hands. Give me your hands."
    amb "Haa... holding tight...!"
    mc_s "I'm close. Coming with you."
    amb "Yes! Fill me! I love you!"

    show white zorder 1.0 at ejaculation_flash
    show ep06_ambermorn61 at vpunch with flash
    $ ss.add("amber", "creampie")

    amb "Ahhh! Warm! So warm!"
    mc_s "Amber!"
    amb "Haa... haa... inside me..."

    $ show_walkthrough("ep06_amber_love_declaration_menu")
    menu:
        "I love you.":
            hide screen walkthrough_screen
            mc_s "I love you. Always."

            $ rm.update("amber", "trust", 10)
            $ check_levels("amber", "trust", 10)

        "You're safe.":
            hide screen walkthrough_screen
            mc_s "You're safe with me. I promise."

            $ rm.update("amber", "trust", 7)
            $ check_levels("amber", "trust", 7)

        "I'm staying.":
            hide screen walkthrough_screen
            mc_s "I'm not going anywhere. I'm staying right here."

            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
    
    $ ep06_ach_amblove = True
    jump ep06_mornwithamber_postclimax


label ep06_mornwithamber_rejection:
    $ playAudio(bodyfall_carpet, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.6, 0)

    show ep06_ambermorn62 with vpunch
    mc_s "Amber, I can't do this right now."
    amb "What the fuck do you think you're doing?"
    mc_s "Look, I gotta..."
    amb "Get off me."
    mc_s "Huh?"

    $ playAudio(bodyfall, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.6, 0)

    show ep06_ambermorn63 with hpunch
    amb_y "I said get off me!"
    mc_s "Amber... relax. I just wanna tell you-"
    amb_y "Don't you ever fucking touch me like that again!"
    mc_s "I didn't mean to... it was a reflex."
    amb "You better hope it was."

    $ playAudio(bed_creaking, "sfx", 3, False, 0)
    $ setChannelVolume("sfx", 3, 0.6, 0)
    
    show ep06_ambermorn64
    amb_y "You seriously don't get why I'm here!"
    mc_s "Calm down, Amber! Let go of my arms!"
    amb_y "Ugh! God dammit, why do you have to be like this?!"
    if ss.get("amber", "strike") <= 2:
        amb_y "I can't! I just... I can't figure you out!"
    
    else:
        amb_y "I tried to! I really tried to! And you just... pushed me away!"

    show ep06_ambermorn65
    amb "You know what? Fuck it. You want to push me away? Fine."
    if ss.get("amber", "strike") == 1:
        mc_s "Listen, it's just bad timing. Don't be so dramatic."
        amb "Bad timing, huh?"
        mc_s "I really don't have time for this right now. I gotta work."
    
    else:
        mc_s "Listen, I thought I made it very clear that I wanted some space."
        amb "Space, huh?"
        mc_s "I really can't waste time on this right now."

    $ playAudio(bodyfall_carpet, "sfx", 4, False, 0)
    $ setChannelVolume("sfx", 4, 0.6, 0)

    show ep06_ambermorn66 with vpunch
    amb "Alright..."
    mc_t "Huh? She changed her mood all of a sudden."
    mc_s "Amber..."

    $ playAudio(amber2_theme, "music", 1, True, 10)
    $ setChannelVolume("music", 1, 0.3, 0)

    amb "Do you know why I keep trying? Why I keep looking for you? Why I keep trying to touch you?"
    mc_s "Please, can we talk about this later?"
    if ss.get("amber", "strike") == 1:
        amb "No. You're going to listen. Since you're becoming just like everyone else."
    
    else:
        amb "No. You're going to listen. Since you're so fucking dead set on pushing me away."

    show ep06_ambermorn67
    amb "When we were younger, before everything went to shit with this [fm_r_low]..."
    mc_s "What about it?"
    amb "You were the only one who actually {i}saw{/i} me."
    amb "Not just [mo_r]'s perfect blonde doll to parade around."
    amb "Just... me."

    show ep06_ambermorn22 with clouds_inverse
    amb "When I cut and dyed my hair... ruined her 'precious image'... She called me a disappointment."
    mc_s "I remember."
    amb "But you were standing right there. Trying to protect me with your words... with just being there."
    amb "Like this giant shield around me that I didn't ask for, but needed so damn much."
    mc_s "I remember... though I can't say I did it on purpose."
    amb "But you did it."

    show ep06_ambermorn68 with fade
    mc_s "Why is it so important to bring this up now? Like this?"
    amb "See? You still don't get it... You're looking at the logic, not at me."
    amb "I'm not talking about when we were younger anymore."
    amb "I'm saying that... since then, you became the only real thing in my world."
    if ss.get("amber", "strike") == 1:
        amb "I came here hoping..."
        amb "Hell, you could have tried to kiss me. Or just hold me."
        amb "Instead, you tossed me aside like I was nothing."
    
    else:
        amb "But it's just a one-way street with you, isn't it?"
        amb "I bleed myself dry for you, and you don't even care."

    $ playAudio(bodyfall_carpet, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.6, 0)

    show ep06_ambermorn69 with vpunch
    amb "Ugh..."

    $ setChannelVolume("music", 1, 0.0, 10)

    if ss.get("amber", "strike") == 1:
        amb "I'm sorry... I shouldn't have dumped all this on you."
        mc_s "It's okay... but I honestly don't know what to say anymore."
        mc_s "I feel like anything I say right now is just going to make it worse."
        amb "Yeah... I'm sorry. I'm just not thinking straight."
    
    else:
        amb "I'm sorry... I shouldn't have wasted your time with my emotional crap."
        amb "It's just that... God, it hurts."
        mc_s "I think you're making a scene out of nothing, Amber."
        amb "A scene...?"
        amb "Where did he go? The [br_full_r_low] from my memories... where the hell did he go?"
    
    mc_t "She's spiraling. I can't deal with this loop."
    mc_t "Twenty minutes to get to the station. If I don't leave now, Watanabe is going to kill me."

    show ep06_ambermorn70 with vpunch
    if ss.get("amber", "strike") == 1:
        amb "Look at me. Forget the badge for one second and just look at me."
        mc_s "Amber, I really have to be at the station in twenty minutes."
        amb "Twenty minutes... Is that all I'm worth now?"
    
    elif ss.get("amber", "strike") == 2:
        amb "You're checking the time? Seriously?"
        amb "Work. That's your new shield, isn't it?"
        mc_s "It's not a shield, it's a job. People are dying out there."
        amb "And I'm dying right here! Doesn't that matter to you at all?!"
    
    else:
        amb "You're looking right through me. Like I'm just another suspect."
        mc_s "I'm looking at the time. I really have to go."
        amb "My God... you actually mean it. You really don't feel a thing for me anymore."

    $ playAudio(bodyfall, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(bed_laying, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.6, 0)

    show ep06_ambermorn71 with hpunch
    if ss.get("amber", "strike") == 1:
        amb_y "Stop looking through me! I'm the one who is alive! Not her!"
        mc_s "Amber, you're heavy. Please, let me get up."
        amb "Heavy...? I'm begging you to feel something and I'm just... dead weight to you?"
    
    elif ss.get("amber", "strike") == 2:
        amb_y "You think that badge is going to love you back?! It won't!"
        mc_s "At least the job makes sense! Unlike this! Now get off me!"
        amb "Unlike me... right?"
    
    else:
        amb "I'm staring right into your eyes... and it's like looking at a wall."
        mc_s "I need to shower. Move."
        amb "Gone. You're actually gone."

    $ setChannelVolume("music", 1, 0.3, 10)

    show ep06_ambermorn72 with fade
    if ss.get("amber", "strike") ==1:
        mc_t "Fuck... I didn't mean to call her dead weight."
        mc_t "She looks so small curling up like that."
        mc_s "Amber... look, I just meant physically heavy. I'm sore, okay?"
        amb "Just stop. Don't try to fix it with logic. You just make it uglier."
    
    elif ss.get("amber", "strike") ==2:
        mc_t "Great. Now she's shut down. If I touch her, she explodes. If I speak, she explodes."
        mc_s "Are we done screaming? Because I really need to get ready."
        amb "You call this screaming? I'm holding myself together so I don't break your damn windows."
    
    else:
        mc_t "She's doing the victim pose. Curled up, eyes closed. Waiting for me to cave."
        mc_t "I don't have time for this performance."
        mc_s "If you're going to sit there and cry, can you do it in the living room?"
        amb "..."

    show ep06_ambermorn73 at ken_burns_bottom_to_top with vpunch
    mc_t "Watching the curve of her hips as she bends over... God."
    mc_t "It's almost a shame. All that passion, all that heat... wasted on a conversation like this."
    if ss.get("amber", "strike") == 1:
        amb "You know what's funny? You're a total mess, [mc_name]. Obsessed with a dead woman."
        amb "You chase ghosts. And I never judged you for it."
        mc_s "Amber, don't start..."
        amb "I took all your baggage because it was yours. I just thought... maybe you could handle mine."
    
    elif ss.get("amber", "strike") == 2:
        amb "I put up with so much bullshit from you! Your drama! Your obsession with HER!"
        amb "I lived in second place for years because I loved the real you, fucked up as you are!"
        mc_s "That's different."
        amb "It's not different! You're just a hypocrite who wants a silent doll to fuck, not a real person!"
    
    else:
        amb "I always loved how damaged you were. I thought it made you deep."
        mc_s "Amber, spare me the poetry."
        amb "I was wrong. You're not deep, [mc_name]..."
        amb "You're just hollow. And I'm done throwing myself into a black hole."

    show ep06_ambermorn74 with fade
    if ss.get("amber", "strike") == 1:
        amb "You know... I used to hate her. I hated how much space she took up in your head."
        amb "But look at me now. Crying over a guy who won't even look at me properly."
        amb "I guess I'm no better. You have your ghost... and I have... you."

    elif ss.get("amber", "strike") == 2:
        amb "She wins. She always fucking wins."
        amb "I spent my entire youth trying to be brighter than a ghost. Trying to make you look at me."
        amb "But you walked right past the living to bury yourself with the dead. You idiot."

    else:
        amb "I used to wonder why you couldn't let her go. Why you loved a memory more than real life."
        amb "But I get it now. I finally get it."
        amb "Because I'm doing the exact same thing right now. You are my Antonella, [mc_name]..."
        amb "Dead to the world, but alive in my head. And just as impossible to reach."

    show ep06_ambermorn75
    mc_t "She's not looking at me with love anymore. She's looking at me with... clarity."
    if ss.get("amber", "strike") == 1:
        amb "Don't look at me like that. Like you are the victim."
        mc_s "I never meant to hurt you, Amber. I swear."
        amb "I know. That's the worst part."
        amb "You destroyed me by accident. You didn't even care enough to do it on purpose."

    elif ss.get("amber", "strike") == 2:
        amb "Take a good look, [mc_name]. Memorize it."
        mc_s "Amber, stop..."
        amb "No. You look."
        amb "You wanted the past so bad? You got it."
        amb "But this? Me? Warm, alive, right here? ...This is the future you just killed."

    else:
        amb "You look surprised. Did you think I'd stay a foolish little girl forever?"
        mc_s "..."
        amb "The girl who chased you is gone, [mc_name]."
        amb "Congratulations. You buried her right next to Antonella."

    $ playAudio(footsteps_bare, "sfx", 1, True, 0)
    $ setChannelVolume("sfx", 1, 0.6, 0)

    show ep06_ambermorn76 with fade
    if ss.get("amber", "strike") == 1:
        mc_t "Am I following her? Why the hell am I doing that?"
        mc_t "I just crushed her because I was tired and sore. Why try to fix it now?"
        amb "Just keep walking, Amber. One foot in front of the other."
        amb "Don't turn around. Don't beg. Just... get to the door."
        mc_s "Amber, wait..."

    elif ss.get("amber", "strike") == 2:
        mc_t "Why do I want to call her name? Why?"
        mc_t "I just told her she's suffocating me. Why am I terrified of the silence she's leaving behind?"
        amb "Stupid... you are so stupid."
        amb "He chose the corpse. He actually chose the corpse. God, I'm such an idiot for believing in him."
        mc_s "Don't walk away from me!"

    else:
        mc_t "What the fuck? I almost went after her. Pure muscle memory."
        mc_t "Why bother? I just told her she means nothing. Chasing her now would just be... stupid."
        amb "There's nothing there. I was screaming at a wall."
        amb "No heart. No [br_full_r_low]. Just... empty space."
        mc_s "Amber."

    $ stopAudio("sfx", 1, 1)

    show ep06_ambermorn77 with hpunch
    if ss.get("amber", "strike") == 1:
        amb "Don't. Don't you dare apologize."
        amb "If you say 'I'm sorry' right now, I'm going to scream."
        amb "Your apologies are worthless, [mc_name]. They're just noises you make to feel better."

    elif ss.get("amber", "strike") == 2:
        amb "Shut up! Just... shut the fuck up!"
        amb "I don't want to hear your logic! I don't want to hear your excuses!"
        amb "You want silence? You want space? Then start by keeping your mouth shut!"

    else:
        amb "Shhh. Save it."
        amb "Don't speak. Don't pretend you have anything human left to say."
        amb "You made your choice. Now live with the quiet."

    $ playAudio(footsteps_bare, "sfx", 1, True, 0)
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ setChannelVolume("music", 1, 0.5, 10)

    show ep06_ambermorn78 at subtle_zoom_in with fade
    mc_t "Damn. Look at that."
    mc_t "She's walking out of my life, and I'm just standing here staring at her ass in that white lace."
    mc_t "Everything is going to shit... but hell, at least I get a good view."
    if ss.get("amber", "strike") == 1:
        amb "You're staring, aren't you?"
        amb "That's your problem, [mc_name]. You always watch life happen from a distance."
        amb "You never grab it. You just... watch it leave."

    elif ss.get("amber", "strike") == 2:
        amb "Enjoy the view. Take a picture if you want."
        amb "Because this?"
        amb "This is the only part of me you ever really gave a shit about."

    else:
        amb "I can feel your eyes. Burning a hole in my back."
        amb "But it doesn't matter anymore."
        amb "Ghosts can't touch the living."
    
    show ep06_ambermorn79
    if ss.get("amber", "strike") == 1:
        amb "You're letting me walk out. Again."
        amb "I hope the view was worth it, [mc_name]."
        amb "Because one of these days... I'm going to walk out and I won't look back."

    elif ss.get("amber", "strike") == 2:
        amb "Keep staring. Fill your eyes."
        amb "That's all you get. Just the shell. Just the ass. Just the 'chaos'."
        amb "I gave you another chance, and you used it to push me away. Don't expect a third one."

    else:
        amb "And just like that... the cord is cut."
        amb "No more pain. No more trying to wake up a corpse."
        amb "Rest in peace, [mc_name]. I'm finally done visiting your grave."

    $ stopAllSubchannels("music", 1.5)
    $ stopAudio("sfx", 1, 1)
    $ playAudio(doorclose, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 1, 0)

    show ep06_ambermorn80 at ken_burns_right_to_left with slowfade
    mc_t "6:30. Shit. I wasted too much time on this."
    if ss.get("amber", "strike") == 1:
        mc_t "She's gone. I got my schedule back."
        mc_t "So why am I staring at nothing expecting her to walk back in?"
        mc_t "Dammit. This feels wrong."

    elif ss.get("amber", "strike") == 2:
        mc_t "Quiet. Finally."
        mc_t "I thought she was never going to shut up."
        mc_t "I need coffee. A lot of it."

    else:
        mc_t "Problem solved. Door shut."
        mc_t "Now I can actually hear myself think."
        mc_t "Where did I put my keys?"
    
    $ stopAllAudio(2.0)
    jump ep06_madisonintro


label ep06_madisonintro:
    scene eigengrau with slowfade
    $ playAudio(stairs_up, "sfx", 1, False)
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(earlypast, "amb", 1, True)
    $ setChannelVolume("amb", 1, 0.2, 0)

    show ep06_madisoncamera01 at ken_burns_bottom_to_top
    mad "Oh! Look who's finally awake."
    mad "I was starting to think you were going to sleep in."
    mc_s "Work starts at eight."
    mad "Right... Your detective job."
    mc_t "Three months of silence. Now small talk."

    $ stopAudio("sfx", 1, 1)

    show ep06_madisoncamera02
    mad "I have a photoshoot today! Near Sakuradamon."
    mad "That's right next to your HQ, isn't it? I checked the map."
    mc_s "That's not close to my office."
    mad "Oh. I thought it was."
    mc_s "Thirty-minute train ride."
    mad "Still. Same direction, right?"
    mc_t "She looked up the route."

    show ep06_madisoncamera03
    mad "We're taking the same train."
    mc_s "Why?"
    mad "Because I want to play a game with you."
    mc_s "I'm not in the mood for games."
    mad "You're going to play this one. Thirty minutes."

    show ep06_madisoncamera04
    mc_s "What kind of game?"
    mad "The truth kind."
    mc_s "Pass."
    mad "Even if I make it worth your while?"

    show ep06_madisoncamera05
    if ep05_confrontation_peaceful:
        mad "I have something you want deleted."
        mc_t "The recording."
        mc_s "What do you want for it?"
        mad "Honesty. Six questions worth."
        mc_s "And if I lie?"
        mad "Then I keep it. Maybe I'll even upload it to the cloud. Just for safekeeping."

        show ep06_madisoncamera06
        mc_s "That's blackmail."
        mad "Please. 'Blackmail' is such an ugly word. Let's call it... leverage."
        mc_s "What makes you think I care if you keep it?"
        mad "Because I know you. You like to pretend you're the hero. Heroes don't have sex tapes with their sisters."
        mad "Besides, you haven't asked me to delete it in three months. You like knowing I have it."

        show ep06_madisoncamera09
        mc_t "She's been waiting three months to use this trap."
        mc_s "Fine. Six questions."
    else:
        mad "I need to understand why the machine didn't work."
        mc_s "What machine?"
        mad "You. Us. That night."
        mc_s "Ask someone else."
        mad "I can't. You're the only variable that doesn't fit the equation."
        mc_s "Why does it matter?"
        mad "Because Michael taught me how the world works. And you broke the rules."
        mc_s "What rules?"

        show ep06_madisoncamera07
        mad "That men are simple. That if you offer them the candy, they eat it."
        mc_t "She sees sex as a transaction she's supposed to win."

        show ep06_madisoncamera08
        mc_s "And I didn't eat."
        mad "Everyone else proved him right. You're the only glitch."
        mc_s "So this is about your ego."
        mad "This is about quality control. I need to know if my radar is broken or if you're just... defective."

        show ep06_madisoncamera09
        mc_t "She's not hurt. She's annoyed that her calculations were off."
        mc_s "Fine. Six questions. Then you leave it alone."
    
    mad "Let's go."

    $ stopAllAudio (2.0)
    jump ep06_madison_traingame

label ep06_madison_traingame:
    # TRAIN SEQUENCE - ROUND 1 SETUP
    scene eigengrau with slowfade

    $ playAudio(traininterior, "amb", 1, True, 5)
    $ setChannelVolume("amb", 1, 0.3)
    $ playAudio(train_ext, "amb", 2, True, 5)
    $ setChannelVolume("amb", 2, 0.2)

    show ep06_madisoncamera10 at ken_burns_left_to_right
    mc_t "Not an accident. She positioned herself for this angle."
    mad "Round one."

    $ playAudio(madison_suspense_theme, "music", 1, True, 2)
    $ setChannelVolume("music", 1, 0.3)

    # ROUND 1 - Madison Asks
    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks about wanting her
        show ep06_madisoncamera11 with fade
        mad "Did you want me that night?"

        $ show_walkthrough("ep06_madison_deepq_round1_menu")
        menu:
            "[Truth] I don't know.":
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

            "[Deflect] Does it matter?":
                hide screen walkthrough_screen
                mc_s "Does it matter?"
                mad "It matters to my ego."
                mc_s "It happened. That's all that matters."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera13
                mad "Boring answer."
                mc_s "Practical answer."
                mad "You're dodging. You wanted me, but you hate admitting it."
                mc_t "She wants me to confess I was weak."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] No. I didn't.":
                hide screen walkthrough_screen
                mc_s "No. I didn't."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera14
                mad "Liar."
                mc_s "You forced the situation."
                mad "I offered. You took. Don't rewrite history to feel cleaner."

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks why MC said no
        show ep06_madisoncamera11 with fade
        mad "Why did you say no?"

        $ show_walkthrough("ep06_madison_response_round1_menu")
        menu:
            "[Truth] Because you're irritating.":
                hide screen walkthrough_screen
                mc_s "Because you're irritating."
                mad "Excuse me?"
                mc_s "Everything's a war with you. Every interaction."
                $ rm.update("madison", "trust", -2)
                $ check_levels("madison", "trust", -2)

                show ep06_madisoncamera15
                mad "So you prefer dumb girls who just smile."
                mc_s "I prefer genuine ones. You're exhausting."
                mad "Hmph. At least I'm not boring."

            "[Deflect] Because the timing was wrong.":
                hide screen walkthrough_screen
                mc_s "Because the timing was wrong."
                mad "Timing is an excuse for cowards."
                mc_s "Or for people with self-control."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera13
                mad "Bullshit. You were scared."
                mc_s "Maybe."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] Because I wasn't attracted to you.":
                hide screen walkthrough_screen
                mc_s "Because I wasn't attracted to you."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera14
                mad "Liar."
                mc_s "Think what you want."
                mad "I saw your eyes. You wanted to ruin me."

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    # ROUND 1 - MC Asks
    show ep06_madisoncamera16
    mad "My turn to answer. Go ahead."

    if ep05_confrontation_peaceful:
        # TRUE PATH - MC asks about recording
        mc_s "Why did you record it?"

        show ep06_madisoncamera17
        mad "Insurance."
        mc_s "Against what?"
        mad "Against you waking up the next day and pretending you're a saint."
        mad "I needed proof that the 'perfect detective' is just as dirty as the rest of us."
        mc_t "She wants to drag me down to her level."

    else:
        # FALSE PATH - MC asks why Madison offered herself
        mc_s "Why did you offer yourself?"

        show ep06_madisoncamera18
        mad "I wanted to see if you'd break."
        mc_s "And?"
        mad "You didn't. It... annoyed me."
        mc_s "Just annoyed?"
        mad "And fascinated me. A dog that doesn't eat the steak? That's a rare breed."

    mad "Round two."


    # ROUND 2 - Madison Asks
    show ep06_madisoncamera37

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC was really protecting Nanami
        mad "I told you I was doing it to protect Nanami."
        mad "I gave you my body so you wouldn't chase her."
        mad "Tell me, [mc_name]..."
        mad "Was I really protecting her? Or was I just using that as an excuse to use you?"

        $ show_walkthrough("ep06_madison_deepq_round2_menu")
        menu:
            "[Truth] I don't know. You tell me.":
                hide screen walkthrough_screen
                mc_s "I don't know. You tell me."
                mad "I'm asking you."
                mc_s "It sounded convincing at the time."
                mad "Of course it did. I'm a good liar."
                mc_s "So you were lying?"
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera38
                mad "I... I don't know."
                mad "I wanted to save her. But I think I wanted to destroy you more."
                mc_t "She's actually confused. The mask is slipping."

            "[Deflect] You believed it when you said it.":
                hide screen walkthrough_screen
                mc_s "You believed it when you said it."
                mad "Does that make it true?"
                mc_s "It makes it honest in the moment."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera39
                mad "Coward."
                mc_s "Why? How am I supposed to know how you feel?"
                mc_t "I don't know what I should say to her question."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] You were protecting her. Obviously.":
                hide screen walkthrough_screen
                mc_s "You were protecting her. Obviously."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera40
                mad "Don't be naive. It's insulting."
                mc_s "You love her."
                mad "That doesn't mean I'm noble."
                mad "I used her safety as currency to buy your cock."

                # 70% chance of detection
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if it was because she's MC's [si_full_r_low]
        mad "Was it because I'm your [si_full_r_low]? Is that the only reason you stopped?"

        $ show_walkthrough("ep06_madison_response_round2_menu")
        menu:
            "[Truth] Partially.":
                hide screen walkthrough_screen
                mc_s "Partially."
                mad "Only partially?"
                mc_s "The blood matters. But your personality matters more."
                mad "Ouch."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera41
                mad "So if I were a stranger... you might have?"
                mc_s "Maybe. If you weren't so... you."
                mc_t "She looks almost disappointed."

            "[Deflect] Does it matter?":
                hide screen walkthrough_screen
                mc_s "Does it matter? The answer was no."
                mad "Details matter."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera39
                mad "But that's not all, right? You're holding back."
                mc_s "It's all I'm giving you"

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] Yes. Only because you're my [si_full_r_low].":
                hide screen walkthrough_screen
                mc_s "Yes. Only because you're my [si_full_r_low]."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera40
                mad "Liar. I've seen the way you look at Amber."
                mc_s "That's differ—"
                mad "It's exactly the same. You just don't want me."

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
                    mad "It forces honesty."
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
                    mad "Paranoid? Good."

                    show ep06_madisoncamera44
                    mad "No. Once I send it, I lose my leverage."
                    mc_s "So I'm safe as long as I'm useful."
                    mad "Exactly."

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
                "How many men have said yes?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera45
                    mad "Are you calling me a slut?"
                    mc_s "I'm asking for data."
                    mad "None. I tease them until they beg, then I leave."

                "Did any of them say no? Or was I the first?":
                    hide screen walkthrough_screen
                    mc_s "Did any say no?"
                    mad "You're the first."

                    show ep06_madisoncamera44
                    mad "Most men are pathetic. A little skin and they forget their names."

                    $ ep06_mc_advantage_points -= 1
        else:
            mc_s "How many men said yes before me?"

            show ep06_madisoncamera45
            mad "Zero. I never let it get that far. You were the exception."


    # ROUND 3 - Madison Asks
    show ep06_madisoncamera19

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC regrets it happened
        mad "Do you regret fucking me?"

        $ show_walkthrough("ep06_madison_deepq_round3_true_menu")
        menu:
            "[Truth] No. I don't.":
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

            "[Deflect] Sometimes.":
                hide screen walkthrough_screen
                mc_s "Sometimes. When you act like this."
                mad "Like what? In control?"
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera21
                mc_s "Like a sociopath."
                mad "Flattery won't work on me."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] Yes. Absolutely.":
                hide screen walkthrough_screen
                mc_s "Yes. It was a mistake."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera22
                mad "Liar. Your body said otherwise."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if MC thinks she's broken
        mad "Do you think I'm broken?"

        $ show_walkthrough("ep06_madison_deepq_round3_false_menu")
        menu:
            "[Truth] You want me to answer that seriously?":
                hide screen walkthrough_screen
                mc_s "You want me to answer that seriously?"
                mad "Yes."
                mc_s "I'm not one to judge. I'm hardly a model of mental health myself."
                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

                show ep06_madisoncamera20
                mad "That's not an answer."
                mc_s "Fine. Yes. You're broken."
                mad "Wow. Blunt."
                mc_s "But so am I. So is everyone."
                mad "That doesn't make me feel better."

            "[Deflect] Define \"broken\".":
                hide screen walkthrough_screen
                mc_s "Define \"broken\"."
                mad "Don't play semantics with me."
                $ rm.update("madison", "cor", 1)
                $ check_levels("madison", "cor", 1)

                show ep06_madisoncamera21
                mad "You're dodging."
                mc_s "I'm saying you're functional. Just... twisted."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] No. You're fine. Really.":
                hide screen walkthrough_screen
                mc_s "No. You're fine. Really."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera22
                mad "Liar."
                mc_s "You asked my opinion."
                mad "I asked for truth."
                mc_s "Why is it so hard to believe I think you're normal?"
                mad "Don't patronize me. I know what I am."

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
        mc_s "So you're teaching her to hate."
        mad "I'm teaching her to trust ME."

        show ep06_madisoncamera25
        mc_s "That's isolation."
        mad "It's protection."
        mc_s "Protection from what?"

        show ep06_madisoncamera26 at ken_burns_corner_to_corner4 with clouds_inverse
        mad "I won't let her end up like [mo_r]. Used up. Discarded."

    else:
        # FALSE PATH - MC asks if Nanami knows Madison loves her
        mc_s "Do you love Nanami?"
        mad "..."

        show ep06_madisoncamera27
        mad "If she knew the extent of it... she'd run."
        mc_s "You're sure of that."
        mad "I know it. My love is... heavy."
        mc_s "Have you ever considered telling her anyway?"
        mad "Don't you fucking dare suggest that."
        mc_s "I wasn't—"

        show ep06_madisoncamera28
        mad "Listen to me."
        mad "If you breathe a word of this to her, I will kill you."
        mc_s "I believe you."

    $ setChannelVolume("music", 1, 0.0, 1)
    $ playAudio(bodyfall_carpet, "sfx", 1, False, 0)
    $ setChannelVolume("sfx", 1, 0.8)
    $ playAudio(sighbreathfem, "sfx", 2, False, 0)
    $ setChannelVolume("sfx", 2, 0.5)
    # ROUND 4 - Train Lurch / Madison Falls
    show ep06_madisoncamera46 with vpunch
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

    show ep06_madisoncamera47 with fade
    mad "Where were we?"
    mc_s "Round—"
    mad "Round four."
    $ setChannelVolume("music", 1, 0.3, 2)

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if Isabella knows
        mad "Does Isabella know what you did with me?"

        $ show_walkthrough("ep06_madison_nanami_knows_true_menu")
        menu:
            "[Truth] Of course not. Are you insane?":
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

            "[Deflect] I don't think so.":
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

            "[Lie] Maybe. I don't know.":
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
        mad "Is that why you left us for so many years?"

        $ show_walkthrough("ep06_madison_why_left_false_menu")
        menu:
            "[Truth] What do you mean?":
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

            "[Deflect] I left for work.":
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
                mc_s "From the noise. From this [fm_r_low]."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] I left because of career opportunities.":
                hide screen walkthrough_screen
                mc_s "I left because of career opportunities."
                $ rm.update("madison", "cor", 2)
                $ check_levels("madison", "cor", 2)

                show ep06_madisoncamera50
                mad "You're lying."
                mc_s "How do you—"
                mad "You don't care about money."
                mc_s "People change."
                mad "Not you."

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
                    mad "Physically? Nothing. He turned on the lights."
                    mad "He showed me the machinery behind the marriage."
                    mad "Love is a scam to control women."
                    mc_s "That's when the good girl died."
                    mad "No. That's when she woke up."

                "Did Michael touch you? Is that why you use sex as a weapon?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera54
                    mad "He never touched me. That would be too simple."
                    mc_s "Explain."
                    mad "He destroyed [mo_r] without lifting a finger. He just... stopped looking at her."
                    mad "He pointed at her one night. Laying there, crying, fading."
                    mad "He told me: 'Look at her, Madison. She used to be a luxury import. Now she's just used furniture.'"
                    mc_s "Jesus..."

                    show ep06_madisoncamera55
                    mad "He taught me basic economics, [br_full_r_low]."
                    mad "[mo_r] was a depreciating asset. Once her beauty faded, her value dropped to zero."
                    mc_s "That's horrible."
                    mad "That's reality. Michael didn't invent the market, he just stopped paying rent."
                    mad "I decided I'd never be a tenant, not for you, not for anyone."

                    $ ep06_mc_advantage_points -= 2
        else:
            mc_s "What did Michael do to you the night you stopped being good?"

            show ep06_madisoncamera53
            mad "He showed me that [mo_r] was disposable. And that I would be too."

    else:
        # FALSE PATH - MC asks if Michael taught Madison to use sex as leverage
        if ep06_mc_advantage_points >= 2:
            $ show_walkthrough("ep06_madison_deepq_round4_false_menu")
            menu:
                "Did Michael teach you to use sex as leverage?":
                    hide screen walkthrough_screen
                    show ep06_madisoncamera53
                    mad "Not directly. But through [mo_r]."
                    mc_s "Explain."
                    mad "He made me see that women have an expiration date."
                    mad "Once desire fades, you're trash. I decided never to be trash."

                "Did you despise Elizabeth for staying?":
                    hide screen walkthrough_screen
                    mc_s "Did you despise Elizabeth for staying?"

                    show ep06_madisoncamera54
                    mad "I despised her for being weak."
                    mc_s "She was a victim."
                    mad "She was a fool! She had everything! Beauty, status, power!"
                    mad "And she traded it all to be a housewife for a man who treated her like spoiled meat."
                    mc_s "So you vowed to be the opposite."
                    mad "I vowed to never kneel."
                    mad "[mo_r] gave her power to a man. I take power FROM men."
                    mad "It's the only way to ensure I don't end up discarded in the corner."

                    $ ep06_mc_advantage_points -= 2
        else:
            mc_s "Did Michael teach you to use sex as leverage?"

            show ep06_madisoncamera53
            mad "He taught me that once men stop wanting you, you disappear."


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
            "[Truth] No.":
                hide screen walkthrough_screen
                mc_s "No."

                show ep06_madisoncamera58
                mad "No?"
                mc_s "No. I don't erase history."
                mad "Most men would."
                mc_s "I own my choices."

                show ep06_madisoncamera59
                mad "Explain."
                mc_s "I can hate that we did it, and still admit that we did."
                mad "So I'm not just a dirty secret?"
                mc_s "You're a secret. But you're real."

            "[Deflect] Probably not.":
                hide screen walkthrough_screen
                mc_s "Probably not."
                mad "Probably."
                mc_s "I'm not in the habit of lying to myself."

                show ep06_madisoncamera61
                mad "That's not a promise."
                mc_s "It's a probability."
                mad "It's evasive. It means you MIGHT."

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] If you delete it, it never happened.":
                hide screen walkthrough_screen
                mc_s "If it's gone, it's gone."

                show ep06_madisoncamera62
                mad "Liar. You're praying I delete it."
                mad "Typical. Men always bury the evidence."

                # 70% chance of detection - Check for game over
                $ ep06_detect_lie(70)  # Madison may notice the lie

    else:
        # FALSE PATH - Madison asks if MC would have said yes if not related
        show ep06_madisoncamera57
        mad "Would you have said yes if I wasn't related to you?"

        $ show_walkthrough("ep06_madison_response_round5_false_menu")
        menu:
            "[Truth] I already told you. It's not about being related.":
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

            "[Deflect] Maybe.":
                hide screen walkthrough_screen
                mc_s "Maybe."
                mad "Maybe?"
                mc_s "Attraction isn't a science."

                show ep06_madisoncamera63
                mad "That's a non-answer."
                mc_s "It's the only one I've got. Without the taboos... who knows?"

                # 50% chance of detection
                $ ep06_detect_lie(50)  # Madison may notice the lie

            "[Lie] Probably yes.":
                hide screen walkthrough_screen
                mc_s "Probably yes."

                show ep06_madisoncamera62
                mad "Liar."
                mc_s "You asked for a hypothetical."
                mad "I know men."
                mc_s "So?"
                mad "If you really wanted to fuck me, a little thing like '[fm_r_low]' wouldn't have stopped you."
                mad "Men break rules for lust. You didn't."
                mad "So you don't want me. At all."

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
        mad "Love? That's a weak word for it."
        mc_s "Then what is it?"
        mad "Ownership. Salvation."
        mad "I want to carve my name into her ribs so she never forgets who saved her."
        mc_s "That sounds like obsession."
        mad "She doesn't see the filth in the world because I stand in front of it. And..."
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
        mad "'Saved' means 'weak'."
        mad "I'd rather be the monster that survives."

        show ep06_madisoncamera67
        mad "Monsters don't need anyone."


    # ROUND 6 - Final Question / Path Choice
    mad "Last question. My turn."

    show ep06_madisoncamera30

    if ep05_confrontation_peaceful:
        # TRUE PATH - Madison asks if MC would do it again
        mad "If I delete this right now..."
        mad "Would you do it again?"

        $ show_walkthrough("ep06_madison_critical_true_menu")
        menu:
            "[Love] Not like that.":
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

            "[Corruption] Yes.":
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

            "[Neutral] No.":
                hide screen walkthrough_screen
                mc_s "No."

                show ep06_madisoncamera35
                mad "Just no?"
                mc_s "The answer will always be no."
                mad "Why?"
                mc_s "Because you don't want me. You want a puppet."
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
            "[Love] Honestly? The dynamic has changed.":
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

            "[Corruption] Probably. Depends.":
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

            "[Neutral] No.":
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

                    $ stopAllSubchannels("music", 2.0)
                    show ep06_madisoncamera69 with fade
                    mad "Over not being hurt again."
                    mc_t "The good girl isn't gone. She's just armored."

                "If you could kill Michael and get away with it, would you?":
                    hide screen walkthrough_screen
                    mc_s "If you could kill [da_r] and get away with it, would you?"
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

                    $ stopAllSubchannels("music", 2.0)
                    show ep06_madisoncamera69 with fade
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

            $ stopAllSubchannels("music", 2.0)
            show ep06_madisoncamera69 with fade
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

                    $ stopAllSubchannels("music", 2.0)
                    show ep06_madisoncamera69 with fade
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

                    $ stopAllSubchannels("music", 2.0)
                    show ep06_madisoncamera69 with fade
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

            $ stopAllSubchannels("music", 2.0)
            show ep06_madisoncamera69 with fade
            mad "Villains have more fun. And they live longer."
            mc_t "She wears the villainy like a shield."


    # Platform Scene - Final Choice
    $ stopAllSubchannels("amb", 2.0)

    scene eigengrau
    pause 1.0

    $ playAudio(trainstationquiet, "amb", 1, True, 2)
    $ setChannelVolume("amb", 1, 1.0)
    $ playAudio(stationamb, "amb", 2, False, 2)
    $ setChannelVolume("amb", 2, 0.5)
    $ playAudio(hallwalkfemale, "sfx", 2, True, 5)
    $ setChannelVolume("sfx", 2, 0.5)
    $ playAudio(hallwalkmale, "sfx", 3, True, 5)
    $ setChannelVolume("sfx", 3, 0.5)

    show ep06_madisoncamera70 with fade
    mad "My studio's just two blocks from here. Second floor, above a convenience store."
    mc_s "I have a briefing."
    mad "I know. Everyone knows the famous Osaka detective's schedule."
    mc_t "\"Famous.\" She's mocking me."

    if ep06_madison_path == "love":
        mad "Just ten minutes... My equipment is heavy."
        mc_s "Is that really what you need?"
        mad "And... I don't want to be alone in that studio today. Please, Big [br_full_r]?"
        mc_t "There it is. The weaponized innocence."

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
    $ stopAllSubchannels("sfx", 2.0)
    
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
            else:
                # MC threatened her in ep05, MC lied 0 times, corruption path
                mad "We both know what we are now."
                mad "Broken. Complicated."
                mad "You threatened me that night. But today you showed me your true face."
                mad "My studio. Now."

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


    if htl_episodes == 6.1:
        $ show_custom_notification("save_tip")
    else:
        pass
    mad "Ten minutes."
    mad "Then you can go play hero."

    mc_t "Last chance to walk away."
    mc_t "Every reason says run. Every instinct says stay."

    #-- End Update
    if htl_episodes == 6.1:
        $ stopAllAudio(3.0)
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