label ep05_elisuicide:
    $ stopAllAudio(2.0)
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3
    show loc_hospmichael_night with slowfade
    show hospital_location zorder 2 with dissolve
    pause 4
    hide hospital_location with dissolve
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)

    show ep05_hosd1_nan01 at ken_burns_bottom_to_top
    mc_t "Someone's coming down the hall... is that Nanami?"
    mc_t "What's she doing here at the hospital?"

    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(nanami_theme, "music", 1, True, 4, 0)

    show ep05_hosd1_nan02
    nana "Eep!"
    if ep04_nanadad:
        nana "Da--[daddy_r]!"
        nana "I-- I mean... sorry, I didn't expect to see you here!"
    else:
        nana "[mc_name]-san!"
        nana "Sorry for startling you!"
    mc_s "Nanami? What brings you to the hospital?"
    nana "I brought these flowers for your [mo_r_low]!"
    nana "When Madison told me what happened, I... I wanted to help somehow."
    mc_s "That's really sweet of you. Thank you."

    show ep05_hosd1_nan03
    mc_s "Did Madison come with you?"
    nana "She's in the cafeteria yelling at the cashier about juice prices."
    nana "Something about... um... 'guys always ripping off girls?'"
    mc_s "Yeah, that sounds like Madison alright."
    mc_t "She looks embarrassed about something. More than just Madison's drama."
    if ep04_mcdrunk:
        show ep05_hosd1_nan04
        nana "Um... [mc_name]-san? About that night when I got really drunk..."
        nana "I keep remembering... w-weird stuff. Like bits and pieces."
        nana "Madison said it would be fun to drink with you, and that I should... you know..."
        mc_s "What exactly do you remember, Nanami?"
        nana "It's kinda embarrassing to talk about here..."
        nana "C-could we sit down here? In the waiting area?"
        mc_s "Sure. Let's sit."
        mc_t "I knew this conversation would happen eventually."

        $ stopAudio("music", 1, 2)
        $ setChannelVolume("amb", 2, 0.4, 0)
        $ playAudio(sfx_clinicwalla2, "amb", 2, False, 2, 3)
        scene eigengrau with slowfade
        show ep05_hosd1_nan05 with circlewipe
        nana "I remember... taking my clothes off."
        nana "And you... touching me in places that felt weird."
        nana "Madison told me that's what I was supposed to do if I liked someone."
        mc_s "Nanami, I'm really sorry about that night."

        $ show_walkthrough("ep05_hosnan_m1")
        menu:
            "[Truth] Madison gave you bad advice":
                hide screen walkthrough_screen
                $ ep05_mc_blame_madison = True

                mc_s "Madison shouldn't have told you to get drunk and act that way."
                nana "But she said if I liked someone, I should show them by letting them touch me..."
                mc_s "Madison gives terrible advice. What happened wasn't your fault."

                $ rm.update("madison", "trust", -2)
                $ check_levels("madison", "trust", -2)
            "[Deflect] You didn't do anything wrong":
                hide screen walkthrough_screen
                $ ep05_mc_blame_madison = False

                mc_s "You were drunk and confused. You didn't do anything wrong."
                nana "But Madison said I was supposed to act like that around guys I liked..."
                mc_s "Madison doesn't always give good advice about this stuff."

                $ rm.update("madison", "trust", 2)
                $ check_levels("madison", "trust", 2)

        show ep05_hosd1_nan06
        mc_t "Shit... Madison gave her that advice because she wanted Nanami to act that way with her, not with guys."
        if ep05_mc_blame_madison:
            mc_s "You shouldn't feel bad about following crappy advice."
            nana "S-so Madison was totally wrong?"
            nana "Did I mess up that night? You stopped when things got... hot."
            mc_s "You didn't mess up. I stopped because I realized the situation wasn't right."
        else:
            mc_s "I should've been more responsible that night."
            nana "Then why did you touch me if it was wrong?"
            nana "Did I do something bad? You seemed into it but then you just... stopped."
            mc_s "I stopped because I realized what we were doing wasn't okay, even if it felt good."

        show ep05_hosd1_nan07
        $ show_walkthrough("ep05_hosnan_m2")
        menu:
            "[Love] I should have protected you":
                hide screen walkthrough_screen
                $ ep05_mc_takes_responsibility = True

                mc_s "I'm older. I should've stopped things right away."
                nana "So you AND Madison are both teaching me wrong stuff?"
                nana "I thought... older people were supposed to know better!"
                mc_s "You're right to be mad. We both screwed up."

                $ rm.update("nanami", "trust", 2)
                $ check_levels("nanami", "trust", 2)
            "[Deflect] We were both confused":
                hide screen walkthrough_screen
                $ ep05_mc_takes_responsibility = False

                mc_s "That night was confusing for everyone."
                nana "So you AND Madison are both teaching me wrong things?"
                nana "How am I supposed to know what's right if you guys don't even know?"
                mc_s "Sometimes older people mess up too, Nanami. Big time."

                $ rm.update("nanami", "trust", -2)
                $ check_levels("nanami", "trust", -2)
        $ setChannelVolume("music", 2, 0.3, 0)
        $ playAudio(nanami_clumsy_theme, "music", 2, True, 4, 0)

        show ep05_hosd1_nan08 with vpunch
        if ep05_mc_takes_responsibility:
            nana "Then who am I supposed to trust?"
            mc_s "Trust your gut. If something feels wrong, it's okay to say no."
            nana "Like when I made that gross pudding with salt instead of sugar!"
            nana "I trusted the recipe but I totally read it wrong and [mo_r] made the worst face!"
        else:
            nana "That's not really reassuring..."
            mc_s "I know it's confusing, but trusting your instincts is important."
            nana "Like when I made that nasty salty pudding thinking it said sugar!"
            nana "I should've tasted it first instead of just trusting I read it right!"
        mc_s "That's... not really the same thing, Nanami."
        nana "But it was REALLY gross pudding! [mo_r] said it was like eating cake-flavored seawater!"
        mc_t "She's trying to make light of this with her innocent comparisons. It's actually kind of sweet."
    else:
        nana "These flowers are from our garden. [mo_r] said bright colors help people get better."
        mc_s "I'm sure my [mo_full_r_low] will love them when she wakes up."
        nana "Madison said your [mo_r_low] had some kind of... accident?"
        mc_s "Something like that. She's gonna be okay though."
        nana "Oh good! I was really w-worried when Madison told me."
        $ stopAudio("music", 1, 2)
    $ setChannelVolume("amb", 2, 0.4, 0)
    $ playAudio(sfx_clinicwalla2, "amb", 2, False, 2, 3)

    show ep05_hosd1_nan09
    if ep04_nanadad:
        nana "[daddy_r]... can I ask you something kinda p-personal?"
    else:
        nana "[mc_name]-san... can I ask you something that's been bugging me?"
    $ stopAllSubchannels("music", 2)

    mc_s "What's on your mind?"
    nana "When Madison touches me... in certain places..."
    nana "It makes me feel weird but not... not bad weird. Is that normal?"
    $ show_walkthrough("ep05_hosnan_m3")
    menu:
        "[Reject] We shouldn't talk about this":
            hide screen walkthrough_screen
            $ ep05_nanami_sex_education = False

            mc_s "Nanami, we probably shouldn't discuss this stuff."
            nana "But I can't ask Madison 'cause she's the one doing it!"
            nana "And [mo_r]'s always working, and the school nurse just gave me some dumb pamphlet about periods!"
            mc_s "You should really talk to your [mo_r_low] about these feelings when she has time."
            nana "But you're the only older person I feel okay asking!"
            $ rm.update("nanami", "cor", -2)
            $ check_levels("nanami", "cor", -2)
        "[Corruption] Those feelings are normal":
            hide screen walkthrough_screen
            $ ep05_nanami_sex_education = True

            mc_s "Those physical feelings are normal for someone your age."
            nana "So I'm not weird or broken?"
            mc_s "You're totally normal. But what Madison's doing crosses lines."
            nana "Even if I kinda... like how it feels sometimes?"
            mc_s "Even then. These should be experiences you choose when you're ready."

            $ rm.update("nanami", "cor", 2)
            $ check_levels("nanami", "cor", 2)
            $ setChannelVolume("music", 3, 0.3, 0)
            $ playAudio(nanami_theme, "music", 3, True, 4, 0)

    show ep05_hosd1_nan10 at ken_burns_corner_to_corner3
    if ep05_nanami_sex_education:
        nana "Madison says I'm not too young though. She says I'm developing way faster than other girls."
        nana "Look, I'm already bigger than her!"
    else:
        nana "Madison says I'm developing super fast and that means I'm ready for these feelings."
        nana "See? I'm already bigger than Madison!"
    show ep05_hosd1_nan18 at concentrate
    mc_s "Nanami, please sit back down."
    mc_t "Shit, this is getting uncomfortable. She's trying to get me to look at her body."
    nana "Madison likes to... check out how I've grown. She says it's normal girl friendship stuff."
    mc_s "That's exactly what worries me about your relationship with her."

    show ep05_hosd1_nan11 with vpunch
    nana "So Madison's a bad person?"
    $ show_walkthrough("ep05_hosnan_m4")
    menu:
        "[Deflect] Madison cares but she's confused":
            hide screen walkthrough_screen
            $ ep05_madison_is_bad = False

            mc_s "Madison's not bad, but she has serious boundary problems."
            nana "So I should keep letting her touch me since we're friends?"
            mc_s "No. Even friends need to respect boundaries."
            nana "But Madison says all close friends do this kind of stuff together."
            mc_s "Madison's wrong about that."

            $ rm.update("madison", "trust", 3)
            $ check_levels("madison", "trust", 3)
        "[Truth] What Madison does isn't okay":
            hide screen walkthrough_screen
            $ ep05_madison_is_bad = True

            mc_s "What Madison's doing to you isn't okay, no matter what her reasons are."
            nana "So I should keep letting her touch me 'cause she's my best friend?"
            mc_s "No. Real friends don't pressure you into stuff that makes you uncomfortable."
            nana "But Madison says this is how all girlfriends bond."
            mc_s "Madison's manipulating you when she says stuff like that."

            $ rm.update("madison", "trust", -3)
            $ check_levels("madison", "trust", -3)
    $ stopAudio("music", 3, 2)
    nana "But you're my friend too, right? And you never make me do that stuff!"
    mc_s "Exactly. That's how healthy friendships work."

    $ setChannelVolume("music", 5, 0.3, 0)
    $ playAudio(nanami_love_theme, "music", 5, True, 4, 0)

    show ep05_hosd1_nan12 with hpunch
    if ep04_nanadad:
        nana "You're my favorite person, [daddy_r]!"
    else:
        nana "You're my favorite person, [mc_name]-san!"
    nana "Madison told me hugs need to last like twenty seconds to release oxy... oxy-something."
    mc_s "Oxytocin. It's a bonding hormone."
    nana "Can we try a real twenty-second hug? I really need one right now."
    mc_s "Of course. One... two... three..."
    mc_t "This seems innocent enough. She clearly needs comfort."

    show ep05_hosd1_nan13 at ken_burns_bottom_to_top
    nana "Madison never lets me finish counting. She always starts touching other places around ten seconds."
    mc_t "This position is getting uncomfortable. She's sitting right on... I should say something."
    nana "Fourteen... fifteen... sixteen..."
    mc_t "Just a few more seconds. Don't make this weird for her."

    show ep05_hosd1_nan14
    nana "This feels safe and warm. I always wondered what having a protective [da_full_r_low] would feel like."
    mc_t "She's just looking for the paternal comfort she never had. But this position is problematic."
    nana "Nineteen... twenty!"
    mc_t "Do I push her away and risk hurting her feelings? Let it slide this once? Or just... accept that she needs this right now?"

    $ show_walkthrough("ep05_hosnan_m5")
    menu:
        "[Reject] Get off me right now":
            hide screen walkthrough_screen

            mc_s "Nanami, you need to get off my lap. Now."

            $ stopAllSubchannels("music", 2)

            show ep05_hosd1_nan15 with hpunch
            $ setChannelVolume("sfx", 1, 0.3, 0)
            $ playAudio(sfx_walk_slow_f, "sfx", 1, False, 2, 2)
            nana "Did I do something wrong again?"
            mc_s "This position isn't appropriate for us. We can't sit like this."
            nana "I'm s-sorry... I just wanted to feel safe for a sec."
            mc_s "I know, but this crosses a line. Please understand."

            $ rm.update("nanami", "trust", -2)
            $ check_levels("nanami", "trust", -2)
            $ ss.add("nanami", "strike")
            if ss.get("nanami", "strike") == 1:
                $ show_custom_notification("strike1")
            elif ss.get("nanami", "strike") == 2:
                $ show_custom_notification("strike2")
            elif ss.get("nanami", "strike") >= 3:
                $ show_custom_notification("strike3")
        "[Neutral] This should be the last time":
            hide screen walkthrough_screen

            mc_s "Nanami, while that was nice, sitting on my lap isn't something we should do regularly."

            $ stopAllSubchannels("music", 2)

            show ep05_hosd1_nan17
            $ setChannelVolume("sfx", 1, 0.3, 0)
            $ playAudio(sfx_walk_slow_f, "sfx", 1, False, 2, 2)
            nana "Really? But it feels so natural and comfy!"
            nana "I always imagined this is what having a [da_r_low] would feel like!"
            mc_s "I get that you're looking for that connection, but we need boundaries."
            nana "But you take care of me like one would! What's the difference?"
            mc_s "The difference is we need to keep things appropriate between us."

            $ rm.update("nanami", "trust", -1)
            $ check_levels("nanami", "trust", -1)
        "[Love] Just enjoy the moment":
            hide screen walkthrough_screen

            mc_s "There. Twenty seconds exactly."

            show ep05_hosd1_nan16 with vpunch
            $ setChannelVolume("sfx", 1, 0.3, 0)
            $ playAudio(sfx_walk_slow_f, "sfx", 1, False, 2, 2)
            nana "See? Madison was right about the oxytocin! I do feel way better!"
            nana "Can we do this more often? It feels like what [fm_r_low] should be."
            mc_s "If it helps you feel better... I guess we can do this sometimes."
            nana "Really? Thank you so much! You're the best!"
            mc_t "I'm probably going to regret this decision..."

            $ stopAllSubchannels("music", 2)
            $ rm.update("nanami", "trust", 1)
            $ check_levels("nanami", "trust", 1)
    $ stopAllSubchannels("sfx", 2)
    jump ep05_hosmadison




label ep05_hosmadison:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 3, 0.1, 0)
    $ playAudio(sfx_clinicwalla3, "amb", 3, False, 3, 3)

    show ep05_hosd1_mad01
    mad "Well, well... isn't this cozy?"
    nana "M-Madison! We were just talking!"
    mad "About what exactly, sweetie?"
    mc_t "Fuck. How long has she been standing there?"

    show ep05_hosd1_mad02 at ken_burns_right_to_left
    nana "[mc_name]-san says you shouldn't touch me in private places even if it feels nice sometimes!"
    mad "Is that what he said? How interesting."
    mad "Nanami, be a dear and get us some coffee from the cafeteria."
    nana "But I don't really like coffee..."
    mad "Then get yourself a hot chocolate. Take your time."
    show ep05_hosd1_mad03
    nana "Will you both be here when I get back?"
    mad "Oh yes. We'll be right here having a nice little chat."
    if ep04_nanadad:
        nana "Remember what we talked about, [daddy_r]. Twenty seconds."
        mad "Twenty seconds? And '[daddy_r]'? How precious."
    else:
        nana "Remember what we talked about, [mc_name]-san. Twenty seconds."
        mad "Twenty seconds? How sweet."
    mc_t "I need to get Nanami away from this psycho."

    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(madison_bad_theme, "music", 1, True, 4, 0)
    $ setChannelVolume("sfx", 1, 0.7, 0)
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)

    show ep05_hosd1_mad04 at ken_burns_left_to_right with hpunch
    if ep04_mcdrunk:
        mad "Tell me, did you enjoy having her on your lap? Did it remind you of when she was drunk and you felt her up?"
    else:
        mad "Tell me, did you enjoy having her on your lap? Did it remind you of all those times you've fantasized about her?"
    mc_t "She's trying to piss me off. Do I take the bait?"

    $ show_walkthrough("ep05_hosmad_m1")
    menu:
        "[Love] Try to defuse the situation":
            hide screen walkthrough_screen
            $ ep05_confrontation_peaceful = True

            mc_s "Madison, let's not do this here. We both care about Nanami."
            mad "Care? Is that what you call groping vulnerable girls?"
            mc_s "I was comforting her. There's a difference."
            mad "Is there? Because from where I'm standing, you're just another predator."
            $ rm.update("madison", "trust", 2)
            $ check_levels("madison", "trust", 2)
        "[Reject] Put her in her place":
            hide screen walkthrough_screen
            $ ep05_confrontation_peaceful = False

            mc_s "You're one to talk about inappropriate touching."
            mad "At least I'm honest about what I want."
            mc_s "You're grooming her. Using her trust."
            mad "And what are you doing? Playing the hero while getting your rocks off?"
            $ rm.update("madison", "trust", -3)
            $ check_levels("madison", "trust", -3)
    $ setChannelVolume("sfx", 2, 0.7, 0)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)

    show ep05_hosd1_mad05 at ken_burns_right_to_left with hpunch
    mad "I saw how you looked at her. How you held her."
    mc_s "I'm trying to protect her from you."
    mad "By offering yourself as an alternative? How noble of you, big [br_full_r_low]."
    mad "Remember, you owe me a favor. Or did you forget about the photo?"
    mc_t "Shit. That topless selfie she took with me."

    show ep05_hosd1_mad06 at zoom_out
    mad "You want her just as much as I do. The difference is I admit it."
    mc_s "You're sick."
    mad "We're all sick, [br_full_r_low]. Some of us just embrace it."
    mad "I said we'd talk, didn't I? There's something I need... I want something for me and Nanami, and—"
    mc_s "Not now, Madison. Drop it."
    mc_t "Can't let her finish that thought."
    if not ep05_confrontation_peaceful:
        mc_s "Save it—I'm done. I'm out."

        show ep05_hosd1_mad07
        mc_s "I'm going to make sure everyone knows what you're really doing to her."
        mad "With what proof? Your word against mine?"
        $ show_walkthrough("ep05_hosmad_m2")
        menu:
            "[Reject] Make a direct threat":
                hide screen walkthrough_screen
                $ ep05_threat_direct = True

                mc_s "I'll tell [mo_r] and [da_r] exactly what their precious [dau_r_low] is up to."
                mad "They won't believe you. I'm their perfect little angel."
                mc_s "We'll see about that when I show them the evidence."

                $ rm.update("madison", "trust", -4)
                $ check_levels("madison", "trust", -4)
            "[Neutral] Hint at consequences":
                hide screen walkthrough_screen
                $ ep05_threat_direct = False

                mc_s "People are going to start noticing things, Madison."
                mad "What people? What things?"
                mc_s "Your behavior isn't as subtle as you think. Eventually someone will put the pieces together."
        if ep05_threat_direct:
            if ep04_nanadad:
                mad "The word of a man who lets a young girl call him '[daddy_r]'? Good luck with that."
            else:
                mad "The word of a man who gets off on vulnerable girls? Good luck with that."
        else:
            mad "Nobody will believe you. I'm just a caring friend helping a lonely girl."
        mad "Stay away from her, and I won't have to expose your little fantasies."
        mc_s "This isn't over."
        mad "I'll tell her you had an emergency and had to leave."
        $ stopAllAudio(2.0)
        jump ep05_hospaz


    else:
        mad "Let's take this somewhere a little more... peaceful. Wouldn't want any distractions, right?"
        $ stopAudio("music", 1, 2)
        scene eigengrau with slowfade
        $ setChannelVolume("amb", 2, 0.3, 0)
        $ playAudio(sfx_clinicwalla2, "amb", 2, False, 3, 0)

        show ep05_hosd1_mad08 at ken_burns_bottom_to_top
        mad "You know what? I can see how much you want her."
        mc_s "What are you talking about?"
        mad "I'll make a sacrifice. I'll give you what you really want."
        mc_t "What kind of game is she playing now?"

        $ setChannelVolume("sfx", 3, 0.7, 0)
        $ playAudio(sfx_bodyfall_carpet, "sfx", 3, False, 0, 0)
        pause 0.3
        show ep05_hosd1_mad09 with vpunch
        mad "I'll give you my body instead of hers. Isn't that generous of me?"
        mc_s "What?!"
        mad "I'm protecting her purity. Someone has to keep her innocent."
        mc_t "This is some twisted logic."

    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(madison_sexy_theme, "music", 2, True, 4, 0)

    show ep05_hosd1_mad10 at ken_burns_bottom_to_top with slowfade
    mad "I'm sacrificing myself so you won't corrupt her. I'm such a saint."
    mc_s "Madison, what the hell are you doing?"
    mad "Being noble. Offering my body to save hers."
    mc_t "This is fucked up, but... damn."

    show ep05_hosd1_mad11 at ken_burns_left_to_right
    mad "Mmm... see? I'm willing to let you use me to protect sweet, innocent Nanami."
    mc_s "This is fucking wrong... ahhh..."
    mad "Wrong? I'm being selfless here. My body for her virtue."
    mc_t "My dick doesn't care about her twisted logic right now."

    show ep05_hosd1_mad12 at subtle_zoom_in
    mc_s "We shouldn't be... ohhhh fuck..."
    mad "Mmmmph... you're right. But I'm sacrificing my body for her sake."
    mc_s "Stop with the martyr bullshit... ahhhh..."
    mc_t "Why am I not walking away?"

    show ep05_hosd1_mad13 at ken_burns_bottom_to_top
    mad "Mmmm... I'm literally offering my body to keep you away from her. Ahhh... I'm amazing."
    mc_s "You're fucking delusional... ohh god..."
    mad "Delusional? Mmmmph... I'm being the perfect protector here."
    mc_t "God, she's insane but this feels good."

    show ep05_hosd1_mad14 at ken_burns_right_to_left
    mc_s "Stop talking and just... ahhhhh..."
    mad "Mmmph... just what? Appreciate my physical sacrifice? Ohhhh... I'm practically a hero."
    mc_s "Your mouth feels so fucking good..."
    mc_t "I should walk away but fuck it."

    show ep05_hosd1_mad15 at subtle_zoom_out
    mad "Mmmmph... you're thinking about her, aren't you? About sweet little Nanami?"
    mc_s "I'm thinking about... ahhh... shutting you up."
    mad "Mmmm... but you can't have her. Only I can. So you'll settle for me."
    mc_t "Fuck. She's getting in my head again."

    show ep05_hosd1_mad43
    mad "Mmmmph... this is what you wanted to do to her, isn't it?"
    mc_s "This is about you being a... ohhhh... manipulative bitch."
    mad "Mmmm... poor Nanami. If only she knew what '[daddy_r]' really wants to do to her."
    mc_t "Why does that turn me on more?"

    show ep05_hosd1_mad44
    mc_s "You're the sick one... ahhhh... here."
    mad "Mmmph... then why is your cock getting harder every time I mention her?"
    mc_s "Because you're sucking it so good, psycho... ohhhh..."
    mad "Mmmmm... keep telling yourself that, [br_full_r_low]."
    show ep05_hosd1_mad16
    mad "Ahhh... ready for the real fun?"
    mc_s "Do whatever you want... just stop talking about her."
    mad "But talking about Nanami makes you throb. Feel that? Mmmmm..."
    mc_t "Shit. She's right and she knows it."

    show ep05_hosd1_mad17 with hpunch
    mad "Ohhhh... I'm giving you something she never could. My body, willingly sacrificed."
    mc_s "Madison, we can't keep... ahhhhh..."
    mad "Mmmm... can't keep what? Using my body while fantasizing about her pure one?"
    mc_s "You're seriously fucked up... but that feels amazing..."

    show ep05_hosd1_mad45
    mad "Ahhhh... what if Nanami came back right now and caught us?"
    mc_s "Then we should... ohhhh... stop."
    mad "Mmmm... she'd see how I sacrifice myself to protect her. What a good friend I am."
    mc_t "Fuck. Why does that idea turn me on?"

    show ep05_hosd1_mad18
    mad "Not yet... ahhhh... I want you inside me when you come. My body taking what was meant for hers."
    mc_s "This is insane..."
    mad "Mmmm... insane is watching you pretend to be noble while thinking about fucking her."
    mc_t "She's completely lost it."

    show ep05_hosd1_mad19 at subtle_zoom_out
    mad "Look at me... ohhhhh... really look."
    mc_s "I'm looking..."
    mad "No, you're seeing what you want Nanami to become. But she's pure. Only I can be dirty for you."
    mc_t "Damn her. She's fucking right."

    show ep05_hosd1_mad20 at subtle_zoom_in
    mad "Ahhhhhh... this is what you really want, isn't it? Her body, but you'll settle for mine."
    mc_s "You're twisting everything..."
    mad "Mmmm... I'm protecting her innocence by giving you mine."
    mc_t "I want to deny it but... fuck."

    show ep05_hosd1_mad21 at subtle_zoom_out
    mad "Say it... ohhhhh... say you want to fuck her."
    mc_s "Go fuck yourself..."
    mad "Ahhhh... you can't have her. But you can have me. Isn't that generous?"
    mc_t "She's breaking me down piece by piece."

    show ep05_hosd1_mad22
    mad "Feel how wet I am? Ahhhhh... that's because I'm sacrificing my body for her purity."
    mc_s "What the fuck is wrong with you?"
    mad "Mmmm... I'm being noble. My corruption for her innocence."
    mc_s "Shut the fuck up and just... ohhhh..."

    show ep05_hosd1_mad47
    mad "Ahhhhhh... imagine if she walked in. She'd see how I sacrifice myself to protect her."
    mc_s "Don't you dare... ohhhh fuck..."
    mad "Mmmm... she'd be so grateful. So proud of her selfless friend."
    mc_t "Why the hell does that thought make me harder?"

    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_madohxxx, "sfx", 4, False, 0, 0)
    scene eigengrau
    show ep05_hosd1_mad23 with vpunch
    mc_s "Fuck... your ass is so tight... ahhhhh..."
    mad "Ahhhhhh... tighter than you imagined hers would be?"
    mc_s "Stop bringing her into this... holy shit..."
    mad "Ohhhh... she's why we're here. I'm protecting her by giving you this."
    show ep05_hosd1_mad24 at ken_burns_bottom_to_top
    mad "Mmmmmph... what do you think innocent Nanami would say if she walked in right now?"
    mc_s "I said stop... ohhhh god..."
    mad "Ahhhhhh... she'd see what a good friend I am. Sacrificing my body for her virtue."
    mc_t "The image is driving me fucking crazy."

    show ep05_hosd1_mad25
    if ep04_nanadad:
        mad "Ohhhhh... would she still call you [daddy_r] after seeing you fuck me like an animal?"
        mc_s "Madison, please... ahhhhhh..."
        mad "Mmmmm... she'd understand. I'm taking the corruption so she can stay pure."
    else:
        mad "Ahhhhhh... would she still trust you after seeing you fuck me like this?"
        mc_s "Madison, please... ohhhhhh..."
        mad "Mmmm... she'd be grateful. I'm protecting her innocence with my sacrifice."
    show ep05_hosd1_mad26 at ken_burns_left_to_right
    mc_s "You're the one... ahhhhh... manipulating her."
    mad "Ohhhhhh... and you're the one dreaming about splitting her open. But I'm giving you mine instead."
    mc_s "That's not— fuck, you feel so good... ahhhhhh..."
    mc_t "She's winning this mind game."

    show ep05_hosd1_mad27
    mad "Harder! Ahhhhhh... every time she sits on your lap, you think about this!"
    mc_s "Shut the fuck— ohhhhh..."
    mad "Mmmmmph... but I'm protecting her. My body for her purity."
    mc_t "Can't deny it anymore."

    show ep05_hosd1_mad28
    mad "Fuck me like you want to fuck her! Ahhhhhhh... use my body so hers stays pure!"
    mc_s "This isn't about her... ohhhhhh fuck..."
    mad "Everything is about her! Mmmmph... I'm sacrificing myself for her innocence!"
    mc_t "She's completely dominating me."

    show ep05_hosd1_mad29 at subtle_zoom_out
    mad "Look at me and tell me... ahhhhhh... you don't want to see her face when you first push inside."
    mc_s "I... I don't... ohhhhhh..."
    mad "Mmmmmph... but you can't have her. So you'll use me. What a saint I am."
    mc_t "She's completely broken my defenses."

    show ep05_hosd1_mad30 at ken_burns_corner_to_corner2
    mad "That's it! Ahhhhhhh... show me what you want to do to her innocent body!"
    mc_s "This is about you... ohhhhhh..."
    mad "Mmmmmph... this is about protecting her. I'm the sacrifice."
    mc_t "Why does she have to be this right?"

    show ep05_hosd1_mad31
    mc_s "You're a sick, twisted bitch... ahhhhh..."
    mad "Ohhhhhh... I'm a martyr. Giving my body to protect hers."
    mc_s "I'm nothing like you... ohhhh fuck..."
    mad "Mmmmmph... keep telling yourself that while you fuck me thinking about her."
    show ep05_hosd1_mad32 with vpunch
    mad "Say her name! Ahhhhhh... say 'Nanami' and I'll let you come!"
    mc_s "No... I won't... ohhhhhh..."
    mad "Mmmmmph... you can't have her, but you can say her name while using me."
    mc_t "I'm losing this battle completely."

    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_slosh1, "sfx", 5, True, 0, 0)

    show ep05_hosd1_mad46
    mad "Feel how tight I am? Ahhhhhhh... I'm sacrificing this tightness to protect hers."
    mc_s "Stop it... ohhhhhh fuck..."
    mad "Mmmmmph... young, innocent, virgin tight. But mine, not hers. Aren't I generous?"
    mc_t "The image is too fucking perfect."

    $ stopAudio("sfx", 5, 2)

    show ep05_hosd1_mad33 with hpunch
    mc_s "Shut up! Just shut the fuck up... ahhhhhhh..."
    mad "Make me! Ohhhhhh... use my body like you want to use hers!"
    mc_s "You feel so fucking good... mmmmmph..."
    mc_t "Need to end this before I lose myself completely."

    show ep05_hosd1_mad34 with vpunch
    mad "Yes! Harder, [daddy_r]! Ahhhhhhh... show me what she's missing!"
    mc_s "Don't call me that... ohhhhhh..."
    mad "Mmmmmph... why not? You love when she does. But I'm the one sacrificing for her."
    mc_t "She's completely conquered me."

    show ep05_hosd1_mad35
    mc_s "I'm close... so fucking close... ahhhhh..."
    mad "Think about her! Ohhhhhh... think about the innocence I'm protecting!"
    mc_s "Nanami... ohhhhhh..."
    mc_t "Fuck. I said her name. Madison won."

    $ show_walkthrough("ep05_hosmad_m3")
    menu:
        "Finish inside her":
            hide screen walkthrough_screen
            $ ep05_finish_inside = True

            show white zorder 1.0 at ejaculation_flash
            $ setChannelVolume("sfx", 7, 0.5, 0)
            $ playAudio(sfx_cum_bigload_fast, "sfx", 7, False, 0, 0)

            show ep05_hosd1_mad36 at vpunch with flash
            mc_s "Fuck... I'm coming... Nanami! Ahhhhhhhhh..."
            mad "That's it! Ohhhhhh... come thinking about what you can't have! Fill me up!"
            mc_s "Holy shit... mmmmmph..."
            mc_t "What the fuck have I become?"

            $ rm.update("madison", "cor", 2)
            $ check_levels("madison", "cor", 2)

            show ep05_hosd1_mad37 at subtle_zoom_out
            mad "Mmmmmm... feel better now? I just saved her virtue with my sacrifice."
            mc_s "This was a mistake..."
            mad "No, this was noble. I protected her innocence by taking your seed."
        "Pull out":
            hide screen walkthrough_screen
            $ ep05_finish_inside = False

            show white zorder 1.0 at ejaculation_flash
            $ setChannelVolume("sfx", 7, 0.5, 0)
            $ playAudio(sfx_cum_bigload_fast, "sfx", 7, False, 0, 0)

            show ep05_hosd1_mad38 at vpunch with flash
            mc_s "I'm pulling out... Nanami! Ahhhhhhhhh..."
            mad "That's it! Ohhhhhh... come thinking about what you can't have!"
            mc_s "Holy shit... mmmmmph..."
            mc_t "What the fuck have I become?"

            $ rm.update("madison", "cor", 1)
            $ check_levels("madison", "cor", 1)

            show ep05_hosd1_mad39 at subtle_zoom_out
            mad "Clean yourself up. Your precious Nanami will be back soon."
            mc_s "How do I face her after this?"
            mad "With gratitude. I just protected her purity for you."
    $ stopAudio("music", 2, 2)
    scene eigengrau with slowfade
    show ep05_hosd1_mad40 
    mad "That was enlightening."
    mc_s "What do you want?"
    mad "I think we understand each other perfectly now."
    $ setChannelVolume("amb", 8, 0.2, 0)
    $ playAudio(sfx_clinicwalla3, "amb", 8, False, 3, 3)

    mc_t "She played me like a fucking violin."

    $ ss.add("madison", "blowjob")
    $ ss.add("madison", "anal")
    $ ss.add("madison", "assjob")

    show ep05_hosd1_mad41 at ken_burns_left_to_right
    mad "We understand each other now, right? Nanami is mine. You stay away from her."
    $ show_walkthrough("ep05_hosmad_m4")
    menu:
        "Accept defeat":
            hide screen walkthrough_screen
            $ ep05_stance_surrender = True

            mc_s "Fine. You win."
            mad "I knew you'd see reason."
            mc_s "Just... don't hurt her."
            mad "Hurt her? I just sacrificed my body to protect her."
            $ rm.update("madison", "trust", 10)
            $ check_levels("madison", "trust", 10)
        "Challenge Madison":
            hide screen walkthrough_screen
            $ ep05_stance_surrender = False

            mc_s "This isn't over. I won't let you control her."
            mad "After what just happened? You think you have any moral authority?"
            mc_s "I'll find a way to protect her."
            mad "From what? I'm the one protecting her virtue."
            $ rm.update("madison", "trust", -2)
            $ check_levels("madison", "trust", -2)
            $ ss.add("madison", "strike")
            if ss.get("madison", "strike") == 1:
                $ show_custom_notification("strike1")
            elif ss.get("madison", "strike") == 2:
                $ show_custom_notification("strike2")
            elif ss.get("madison", "strike") >= 3:
                $ show_custom_notification("strike3")
    if ep05_stance_surrender:
        mad "Smart choice. I'll keep sacrificing myself to keep her pure."
    else:
        mad "Oh, I hope you try. I'll just have to sacrifice more to protect her."
    mad "By the way, I recorded our entire conversation today... and everything that just happened."
    mc_s "You what?"
    mad "Every word about your fantasies with Nanami. Every moan. Every time you said her name while fucking me."
    mc_s "You're insane. Delete that."
    mad "Imagine how it would sound to her [mo_full_r_low]? Or the police? '[daddy_r]' having sexual fantasies about a vulnerable girl?"
    mc_s "You wouldn't dare."
    mad "Try me. Stay away from her, and this little recording stays between us."
    mad "But if you interfere with my friendship with Nanami again..."
    mc_s "You sick bitch."
    mad "I prefer 'protective friend.' Now, I'll tell her you had an emergency and had to leave."
    show ep05_hosd1_mad42 at ken_burns_corner_to_corner with slowfade
    mc_t "She played me perfectly. Every fucking move calculated."
    mc_t "Now she has all the power."
    mc_t "Nanami's walking back into a trap and doesn't even know it."

    $ stopAllAudio(2.0)
    jump ep05_hospaz




label ep05_hospaz:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)

    show ep05_hosd2_paz01
    $ setChannelVolume("sfx", 1, 0.2, 0)
    $ playAudio(sfx_vcall, "sfx", 1, True, 2, 2)

    mc_t "Phone's buzzing. Shit, who calls this late?"
    mc_t "Still fucked up from that whole Madison thing."
    mc_t "Wait, that's Paz."

    show ep05_hosd2_paz02
    mc_t "Video call? What the hell does she want at this hour?"
    mc_t "Hope it's not more bad news."
    mc_t "Better see what's up."

    call screen videocall_icons("ep05_hospaz_vc")




label ep05_hospaz_vc:
    show ep05_hosd2_paz02 at focus_shift_sms
    pause 1.0
    $ stopAudio("sfx", 1, 1)
    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(paz_theme, "music", 1, True, 4, 0)

    show ep05_hosd2_paz03 at scale_down, videocall_open
    pa_s "Hey partner. You look like you've been through hell."
    mc_s "Thanks for the pep talk. Hospital chairs aren't exactly comfortable."
    pa_s "How's your [mo_r_low] doing?"
    mc_s "Stable now. Doctors got her sedated."
    pa_s "That's good. Must have been scary as hell."
    mc_s "Yeah, it was. What's going on with you? Working late again?"

    show ep05_hosd2_paz04 at scale_down
    pa_s "Remember when I asked if I should grab that key from evidence?"
    mc_s "Yeah, and I told you it was risky as hell."
    pa_s "Well... I did it anyway."
    mc_s "Damn, Paz. What if you'd been caught?"
    pa_s "Look, I know you had your doubts, but something felt off about this whole thing."
    pa_s "My gut told me to do it, so I did."

    show ep05_hosd2_paz05 at scale_down
    mc_s "How the hell did you even pull that off?"
    pa_s "You know Takahashi? The evidence clerk who's always eye-fucking me?"
    mc_s "The creepy one? Yeah."
    pa_s "Let's just say I finally put his wandering eyes to good use."
    mc_s "Please tell me you didn't sleep with that pervert."
    pa_s "God no. But I gave him a little... show."

    show ep05_hosd2_paz06 at scale_down
    pa_s "Few wardrobe adjustments, some strategic positioning..."
    mc_s "You used your tits to distract him?"
    pa_s "Hey, if he's gonna stare anyway, might as well make it work for me."
    mc_s "That's... actually pretty smart."
    pa_s "While he was drooling, I snagged what I needed."
    pa_s "Got some interesting info too."

    show ep05_hosd2_paz07 at scale_down
    mc_s "What kind of info?"
    pa_s "That ritual setup in your apartment? I've never seen anything like it in any other case."
    pa_s "But here's the weird part - the department's treating this like it's priority one."
    mc_s "More than murder cases?"
    pa_s "Exactly. We've got bodies piling up, but they're obsessing over some bells and candles."
    pa_s "Also found references to doctors in different cities. Dr. Watanabe here in Osaka, others elsewhere."
    pa_s "All connected to yakuza families somehow. Don't know what they need doctors for, but it can't be good."

    show ep05_hosd2_paz08 at scale_down
    mc_s "Sounds like someone's trying to cover something up."
    pa_s "That's what I'm thinking."
    pa_s "[mc_name], I need to tell you something else. About that lie I told Kimura."
    mc_s "About us being together?"
    pa_s "Yeah. It's becoming a problem."
    mc_s "How so?"
    pa_s "He keeps asking questions. Personal stuff."

    show ep05_hosd2_paz09 at scale_down
    pa_s "And I realized I don't know how to answer them."
    mc_s "What do you mean?"
    pa_s "I mean... I've never actually been with a guy, [mc_name]."
    mc_s "Wait, really? I knew you were bi, but I thought you'd been with both."
    pa_s "Nope. All my experience has been with women."
    mc_s "Shit, Paz. That must make this even harder."

    show ep05_hosd2_paz10 at scale_down
    pa_s "You know how this department is. How they talk about anyone who's different."
    pa_s "Being hafu already makes us outsiders. But being hafu AND not straight?"
    mc_s "Shit, I never thought about it like that."
    pa_s "Remember when we first partnered up? We were the department's token foreigners."
    mc_s "Yeah, the gaijin kids who somehow made it through the academy."
    pa_s "Exactly. At least you just had to deal with the 'foreign parents' thing."
    pa_s "I've got that plus being mixed-race, and now this sexuality shit on top of it."
    mc_s "So when you said we were together..."
    pa_s "I panicked. Used you as cover because you're the only one who gets what it's like being the outsider."
    pa_s "But now Kimura wants details, and I don't know what the fuck to tell him."
    mc_s "What kind of details?"

    show ep05_hosd2_paz11 at scale_down
    pa_s "How you touch me. What you like. What I do for you."
    mc_s "I--."
    pa_s "I know it's fucked up, but I need your help."
    mc_s "Help with what exactly?"
    pa_s "Teaching me how to be convincing. How to act like I know what I'm doing with men."
    pa_s "I trust you, [mc_name]. And who else am I gonna ask?"

    show ep05_hosd2_paz12 at scale_down
    mc_s "That's... that's a hell of a request, Paz."
    pa_s "I know. But I'm asking anyway."
    mc_s "What exactly are you asking me to do?"
    pa_s "Show me. Teach me what men want."
    mc_s "Over a video call?"
    pa_s "It's a start, isn't it?"
    mc_t "Fuck. After Madison's mind games, this feels... different."
    mc_t "Paz isn't manipulating me. She's just asking for help."

    show ep05_hosd2_paz13 at scale_down
    pa_s "I know it's weird. But I'm tired of faking everything."
    mc_s "And you think this will help?"
    pa_s "I hope so. Will you help me?"
    mc_t "She actually looks worried. This isn't some game."
    mc_t "This is my partner asking for help."

    $ show_walkthrough("ep05_hospaz_m1")
    menu:
        "Help her learn":
            $ ep05_paz_choice = 1
            hide screen walkthrough_screen
            show ep05_hosd2_paz14 at scale_down
            mc_s "Alright. But this stays between us."
            pa_s "Of course. I wouldn't ask if I didn't trust you completely."
            mc_s "First thing - confidence. Men like to see you're into it."
            pa_s "Like this?"
            mc_s "Yeah, that's good. Natural."
            mc_t "She's actually pretty good at this."

            $ rm.update("paz", "trust", 2)
            $ check_levels("paz", "trust", 2)
            $ rm.update("paz", "cor", 3)
            $ check_levels("paz", "cor", 3)

            show ep05_hosd2_paz17 at scale_down
            mc_s "Eye contact is important. Don't look away when you want something."
            pa_s "Is this too much? I feel like I'm performing in a bad porn."
            mc_s "No, that's perfect. You're a natural."
            pa_s "Really? Because I have no fucking clue what I'm doing."
            mc_s "Trust me. Any guy would be lucky to have your attention."
            mc_t "Shit, she's actually turning me on."

            show ep05_hosd2_paz20 at scale_down
            pa_s "What else do they like?"
            mc_s "That. Definitely that."
            pa_s "Good to know I'm learning something useful."
            mc_s "Paz, you're incredible. Don't let anyone make you think otherwise."
            pa_s "Even you think so?"
            mc_s "Especially me."
            mc_t "Fuck... she's amazing."

            show ep05_hosd2_paz21 at scale_down
            pa_s "So that's what all the fuss is about?"
            mc_s "Part of it. The physical stuff is easy."
            pa_s "I think I'm starting to get it."
            mc_t "Yeah, me too."
        "This isn't a good idea":
            $ ep05_paz_choice = 2
            hide screen walkthrough_screen
            $ stopAudio("music", 1, 2)

            show ep05_hosd2_paz15 at scale_down
            mc_s "Paz, I don't think this is smart. Could fuck up our partnership."
            pa_s "Right. Of course. Forget I asked."
            mc_s "It's not that I don't want to help—"
            pa_s "No, you're right. This was stupid."
            mc_s "Look, there are other ways to handle Kimura."
            pa_s "Like what? Tell him to mind his own business?"

            $ rm.update("paz", "cor", -2)
            $ check_levels("paz", "cor", -2)

            show ep05_hosd2_paz18 at scale_down
            mc_s "Exactly. Your personal life isn't his concern."
            pa_s "Easy for you to say. You're not the one living a lie."
            mc_s "You're not living a lie. You're protecting yourself."
            pa_s "Same fucking difference."
            mc_s "If he keeps pushing, we'll deal with it together."
            pa_s "Right. Partners."
        "You don't need to change":
            $ ep05_paz_choice = 3
            hide screen walkthrough_screen
            show ep05_hosd2_paz16 at scale_down
            mc_s "Fuck Kimura. You don't need to prove anything to anyone."
            pa_s "That's easy to say when nobody's questioning you."
            mc_s "Then stop answering. Tell him to mind his own damn business."
            pa_s "You really think it's that simple?"
            mc_s "I think you're giving them too much power over who you are."
            pa_s "Maybe you're right."

            $ rm.update("paz", "trust", 2)
            $ check_levels("paz", "trust", 2)

            show ep05_hosd2_paz19 at scale_down
            mc_s "You're tough as nails, Paz. Don't let some rookie punk make you doubt yourself."
            pa_s "Thanks. I needed to hear that."
            mc_s "Anytime, partner."
            pa_s "You always know what to say."

    show ep05_hosd2_paz22 at scale_down
    if ep05_paz_choice == 1:
        pa_s "Thanks for... teaching me. I feel more confident now."
        mc_s "You were amazing, Paz. Any guy would be lucky."
        pa_s "Even you?"
        mc_s "Especially me."
    elif ep05_paz_choice == 2:
        pa_s "Thanks for being honest, even if it wasn't what I wanted to hear."
        mc_s "I just don't want to mess up what we have."
        pa_s "I get it. Professional boundaries and all that."
        mc_s "It's not just professional. You mean too much to me to risk it."
    else:
        pa_s "Thanks for reminding me I don't need to change for anyone."
        mc_s "You're perfect as you are, Paz."
        pa_s "Well, maybe not perfect, but I'm me."
        mc_s "And that's enough."
    pa_s "I should get going. Shift ends soon."
    mc_s "Thanks for calling. And for taking that risk with the key."
    pa_s "That's what partners do, right?"
    mc_s "Right."
    pa_s "I'm gonna try to figure out what this key opens. I'll send you photos and whatever I find."
    mc_s "Be careful with that. Don't do anything alone."
    pa_s "Keep this between us?"
    mc_s "Of course."

    show ep05_hosd2_paz23 at scale_down
    if ep05_paz_choice == 1:
        pa_s "And [mc_name]? This call never happened, but... I'm glad it did."
        mc_s "Me too."
        pa_s "Give Elizabeth my best when she wakes up."
        mc_s "Will do."
    elif ep05_paz_choice == 2:
        pa_s "And [mc_name]? Thanks for not making this weirder than it already was."
        mc_s "Hey, we've been through worse shit than this."
        pa_s "True. Give Elizabeth my best when she wakes up."
        mc_s "Will do."
    else:
        pa_s "You always know what to say to make me feel better."
        mc_s "That's what friends are for."
        pa_s "Give Elizabeth my best when she wakes up."
        mc_s "Will do."

    $ stopAudio("music", 1, 2)
    $ setChannelVolume("amb", 1, 0.2, 0)
    $ playAudio(sfx_clinicwalla3, "amb", 1, True, 2, 0)

    show ep05_hosd2_paz24
    "Nurse" "Mr. [mc_name]? Your [mo_full_r_low] is asking for you."
    if ep05_paz_choice == 1:
        mc_t "Back to reality. At least that helped clear my head... in more ways than one."
    elif ep05_paz_choice == 2:
        mc_t "Back to reality. Probably made the right call there."
    else:
        mc_t "Back to reality. Paz is stronger than she gives herself credit for."
    mc_t "Better check on Elizabeth."

    $ stopAllAudio(2.0)
    jump ep05_hosamber




label ep05_hosamber:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    $ setChannelVolume("amb", 2, 0.15, 0)
    $ playAudio(sfx_heart_monitor, "amb", 2, True, 2, 0)
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_clinicroom, "amb", 3, True, 2, 0)

    show ep05_hosd3_amb01 at ken_burns_right_to_left
    mc_t "What the hell? 'Roof. Now. Bring cigs.' That's random as fuck."
    mc_t "Amber never asks me to meet her anywhere. What's this about?"
    mc_t "And why the roof?"

    $ stopAudio("amb",1,2)
    $ stopAudio("amb",2,2)
    $ stopAudio("amb",3,2)
    $ setChannelVolume("amb", 4, 0.6, 0)
    $ playAudio(sfx_clinicrooftop, "amb", 4, True, 2, 0)
    $ setChannelVolume("amb", 5, 0.2, 0)
    $ playAudio(sfx_wind_pool, "amb", 5, True, 2, 0)

    show ep05_hosd3_amb02 with slowfade
    mc_s "Jesus, Amber. You're sitting pretty close to the edge there."
    amb "I like the view. You can see the whole city from up here."
    mc_s "You can also see the ground. Very clearly. And it's very far down."

    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(amber_sad_theme, "music", 1, True, 4, 0)
    amb "Still scared of heights, I see."
    mc_s "Some fears are rational. Like not wanting to fall off a hospital roof."
    amb "Some fears are just excuses to avoid shit."
    show ep05_hosd3_amb03 at ken_burns_corner_to_corner3 with slowfade
    amb "Managed to steal those from the doctor's lounge?"
    mc_s "Yeah. Figured you'd need them for whatever this is about."
    amb "Look at you, breaking rules now."
    mc_s "You're rubbing off on me."
    amb "In more ways than one, hopefully."
    mc_s "Amber..."

    show ep05_hosd3_amb04 at focus_shift with normalfade
    amb "So, [mo_r] tried to kill herself. Let's start there."
    mc_s "The doctors didn't exactly say—"
    amb "They wouldn't. But I can tell."
    amb "Broken mirror, slashed wrists that barely missed the arteries..."
    amb "Classic cry for help, not a real attempt."
    mc_s "How would you know that?"

    show ep05_hosd3_amb05 at ken_burns_left_to_right
    amb "Three times. That's my record."
    amb "First was pills. Second was cutting – obviously fucked that up."
    amb "Third time was more... creative."
    $ show_walkthrough("ep05_hosamb_m1")
    menu:
        "Show compassion":
            hide screen walkthrough_screen
            $ ep05_amber_compassion = True

            mc_s "Shit, Amber. I had no idea."
            amb "Why would you? You were already gone. Osaka and your police thing."
            mc_s "I should have been here."
            amb "Should have, could have, whatever. Past is past."
            mc_s "I'm sorry..."
            amb "Yeah, whatever."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
        "Stay detached":
            hide screen walkthrough_screen
            $ ep05_amber_compassion = False

            mc_s "That explains some things about you."
            amb "Wow. Thanks for the sympathy."
            mc_s "I didn't mean it like that."
            amb "Sure you didn't. Always so fucking emotionally available, aren't you?"
            mc_s "That's not fair."
            amb "Life's not fair. Deal with it."
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)

    show ep05_hosd3_amb06 at ken_burns_right_to_left
    if ep05_amber_compassion:
        amb "Want to know why I never called you during any of those times?"
        mc_s "Tell me."
        amb "What was I gonna say? 'Hey [mc_name], remember when I told you I loved you and you basically ran away? Well, now I'm dying about it'?"
    else:
        amb "You want to know why I never called you during my little episodes?"
        mc_s "Sure."
        amb "Because I knew you'd react exactly like this. Cold as fuck."
        mc_s "I'm not being cold."
        amb "Right. Sure."
    mc_s "I'm sorry. For not being there."
    amb "Sure, why not—one more apology to add to the collection."
    $ stopAudio("music", 1, 2)

    show ep05_hosd3_amb07
    if ep05_ambignore:
        amb "We've been dancing around each other since I got back."
        mc_s "Have we?"
        amb "Don't play dumb. The tension, the looks..."
        mc_s "Maybe that's safer."
        amb "Safer for who? Because it's driving me crazy."
        mc_s "What do you want me to say, Amber?"
        amb "I want you to be honest. About what you feel when you look at me."
        mc_s "Amber..."
        amb "I thought you'd understand. That you'd see I'm not a kid anymore."
        mc_s "I see that. That's the problem."
        amb "Why is it a problem? Because we're related? Because of what people might think?"
        mc_s "Because I don't have protection. Because this could lead somewhere we can't take back."
    else:
        mc_s  "That day, in the kitchen. We need to talk about it."
        amb "What about it?"
        mc_s "You didn't wear a condom."
        amb "No, I didn't."
        amb "I thought you'd understand what it meant when I let that happen without protection."
        mc_s "But that's exactly why we should have used it."
    amb "You know why part of me was terrified about not being careful?"
    mc_s "Because you were being responsible?"
    amb "Because I was fucking terrified."
    show ep05_hosd3_amb08
    amb "Not of getting pregnant or whatever excuse I gave you."
    mc_s "Then what?"
    amb "Of how much I wanted it. How much I wanted you."
    amb "I'd spent years building this wall around myself."
    mc_s "The whole goth metalhead thing?"
    amb "Yeah. The girl who doesn't give a fuck about anything."
    amb "But with you... I was just Amber again. That pathetic little girl who followed you around."
    show ep05_hosd3_amb09 with slowfade
    mc_s "You weren't pathetic."
    amb "I was weak. Needy. Everything I swore I'd never be again."
    amb "You know what it was like after you left? [da_r] got more controlling, the house got quieter..."
    amb "I was young, watching everything fall apart, and the one person who made me feel safe was gone."
    mc_s "I didn't know it was that bad."
    amb "Of course you didn't. You had your new life."
    amb "So I built something for myself. My streams, my fans, my own thing."
    $ setChannelVolume("music", 9, 0.3, 0)
    $ playAudio(amber_2nd_theme, "music", 9, True, 2, 2)
    pause 1
    $ setChannelVolume("sfx", 3, 0.6, 0)
    $ playAudio(sfx_carhit, "sfx", 3, False, 0, 0)

    show ep05_hosd3_amb10 at ken_burns_corner_to_corner2 with normalfade
    mc_s "I never really understood what you were going through."
    amb "No shit. You see the black hair and tattoos and think you know me."
    mc_s "So tell me. Help me understand."
    amb "Most days it doesn't feel real. Just another performance."
    amb "But sometimes... sometimes I remember what it felt like to just be me."
    mc_s "And back then?"
    amb "Back then my brain actually shut up for once."
    mc_s "And now?"
    amb "Now I'm thinking too much again."
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_punch, "sfx", 1, False, 0, 0)
    pause 0.5
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)

    show ep05_hosd3_amb11 with vpunch
    amb "Before, it was just... instinct. Pure need."
    mc_s "Ouch. Thanks for the shove... so, what about now?"
    amb "Right now it would be a choice."
    mc_t "She's giving me an out. Or an in."
    mc_t "Do I want this? Do I want her?"
    mc_t "Fuck, of course I do. I always have."

    $ show_walkthrough("ep05_hosamb_m2")
    menu:
        "Be romantic and gentle":
            hide screen walkthrough_screen
            $ ep05_amber_route = 1

            show ep05_hosd3_amb12
            mc_s "I want to make that choice. But I want to do this right."
            amb "What does 'right' mean?"
            mc_s "It means taking our time. It means this isn't just about sex."
            amb "You want to go slow?"
            mc_s "I want to make sure you know how much you mean to me."
            amb "God, you're going to make me cry."
            mc_s "Good tears or bad tears?"
            amb "Good tears, you idiot."
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
        "Be passionate and intense":
            hide screen walkthrough_screen
            $ ep05_amber_route = 2

            show ep05_hosd3_amb13
            mc_s "Fuck being careful. I want you. Right here, right now."
            amb "Even if someone could see us?"
            mc_s "I don't care who sees. I'm tired of hiding how I feel."
            amb "And how do you feel?"
            mc_s "Like I'm going crazy without you. Like I need you more than air."
            amb "Then take me. Stop thinking and just take what you want."
            mc_s "You sure you can handle that?"
            amb "Try me."
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)
        "Pull away":
            hide screen walkthrough_screen
            $ ep05_amber_route = 3

            mc_s "Maybe we should head back. It's getting cold."

            $ stopAllSubchannels("music", 2)

            show ep05_hosd3_amb14
            amb "Right. Forgot who I was talking to."
            amb "Mr. Run Away when things get real."
            mc_s "Amber, that's not—"
            amb "Save it. I'm going home to stream. Have fun with Elizabeth."
            amb "At least she's too drugged up to reject you."
            $ ss.add("amber", "strike")
            if ss.get("amber", "strike") == 1:
                $ show_custom_notification("strike1")
            elif ss.get("amber", "strike") == 2:
                $ show_custom_notification("strike2")
            elif ss.get("amber", "strike") >= 3:
                $ show_custom_notification("strike3")
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ stopAllSubchannels("sfx", 2)
            $ stopAllSubchannels("amb", 2)
            jump ep05_elidream


    show ep05_hosd3_amb15
    amb "I need you to know something before we do this."
    mc_s "What?"
    amb "I'm not on anything. No pill, no protection. And I don't care."
    mc_s "Amber..."
    amb "That's how much I trust you. How much I want this to matter."
    mc_s "Are you sure?"
    amb "More sure than I've been about anything."
    $ stopAllSubchannels("music", 2)
    scene eigengrau with slowfade
    show ep05_hosd3_amb16
    amb "Look at me. Really look..."
    mc_s "I'm looking."
    amb "See past all the bullshit?"
    mc_s "I see you."
    amb "Then touch me like you mean it..."
    mc_t "Fuck. There's no going back after this."
    mc_t "But I don't want to go back."

    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(amber_sexy_theme2, "music", 2, True, 4, 0)
    $ setChannelVolume("amb", 4, 0.3, 2.0)
    $ setChannelVolume("amb", 5, 0.1, 2.0)

    show ep05_hosd3_amb17
    amb "I used to imagine this. Us..."
    mc_s "Yeah?"
    amb "Stupid fantasies. But now..."
    mc_s "Now it's real."
    amb "Are you nervous?"
    mc_s "Scared shitless."
    amb "Good... mmm... feel something with me..."
    show ep05_hosd3_amb18 with vpunch
    mc_s "I always felt something... that was the problem..."
    amb "And now?"
    mc_s "Now I don't want to fight it..."
    amb "Then don't..."
    show ep05_hosd3_amb19
    mc_s "You're beautiful..."
    amb "Don't lie to me. Not now..."
    mc_s "I'm not lying."
    amb "Even with all my damage?"
    mc_s "Especially with it..."
    amb "Good answer..."
    $ setChannelVolume("sfx", 1, 0.2, 1.0)
    $ playAudio(sfx_carhit, "sfx", 1, False)

    show ep05_hosd3_amb20 with hpunch
    amb "God... your hands... ahhh..."
    mc_s "Tell me what you want... mmm..."
    amb "Everything. All of you... ohhh..."
    mc_s "You have me."
    amb "Do I? Really? Mmmm..."
    mc_s "Yes... fuck, yes..."

    show ep05_hosd3_amb21
    amb "Promise me something... ahhh..."
    mc_s "What?"
    amb "Don't think about her while you're with me... ohhh..."
    mc_s "Who?"
    amb "Don't play dumb. Antonella... mmmm..."
    mc_s "Amber..."
    amb "I need to know I'm enough. That I'm here, I'm real... ahhh..."
    show ep05_hosd3_amb22
    amb "I've been competing with a ghost..."
    mc_s "You're not competing with anyone..."
    amb "Aren't I?"
    mc_s "Right now, there's only you."
    amb "Prove it..."
    mc_t "She needs this. Needs to know she matters."

    show ep05_hosd3_amb23 at subtle_zoom_out
    amb "Let me take care of you first..."
    mc_s "You don't have to—"
    amb "I want to..."
    mc_s "Amber..."
    amb "Shut up and let me..."
    mc_t "The way she's looking at me... like I'm everything."

    show ep05_hosd3_amb24
    amb "You're shaking..."
    mc_s "Cold..."
    amb "Liar. You're nervous..."
    mc_s "Maybe."
    amb "Don't be. It's just me... mmmm... God, you're so hard..."
    mc_s "That's exactly why I'm nervous... fuck..."

    show ep05_hosd3_amb25
    amb "I love you. I've always loved you..."
    mc_s "Amber..."
    amb "Say it back..."
    mc_s "I love you too."
    amb "Even though we're fucked up?..."
    mc_s "Because we're fucked up..."

    show ep05_hosd3_amb26
    amb "I need you inside me... now..."
    mc_s "Are you ready?"
    amb "I've been ready for years..."
    $ setChannelVolume("sfx", 2, 0.1, 0)
    $ playAudio(sfx_gasp_female, "sfx", 2, False)

    show ep05_hosd3_amb27
    amb "Oh god... [mc_name]... yes..."
    mc_s "You okay?"
    amb "Perfect. So fucking perfect... ohhh..."
    mc_s "You feel..."
    amb "Like we were made for this... mmmm..."
    mc_s "God, Amber..."

    show ep05_hosd3_amb28
    amb "Move. Please move... deeper..."
    mc_s "Mmm..."
    amb "Ahhh... fuck yes..."
    mc_t "She's so tight, so warm... fuck."
    mc_t "The sounds she's making... driving me crazy."

    $ setChannelVolume("sfx", 3, 0.1, 1.0)
    $ playAudio(sfx_moan_generic, "sfx", 3, False)

    show ep05_hosd3_amb56 at focus_shift, ken_burns_left_to_right
    amb "Harder. I won't break... ahhh... mmmm..."
    mc_s "You sure? Ohhh..."
    amb "I'm sure. I want to feel you for days... ahhh..."
    mc_s "Fuck, Amber... mmm..."
    amb "That's it. Lose control... ohhh... yes..."
    show ep05_hosd3_amb29 with hpunch
    amb "Look at me while you fuck me... ahhh..."
    mc_s "I'm looking... mmm... you're so beautiful..."
    amb "See me. Not her. Me... ohhh... fuck..."
    mc_s "I see you. Only you... ahhh..."
    amb "Good. Because I'm the one here... mmmm... the one taking your cock..."
    mc_s "You're the one I want... God, Amber..."

    $ setChannelVolume("sfx", 5, 0.3, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False)
    pause 0.5
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_sexslide1, "sfx", 4, False)
    $ setChannelVolume("sfx", 6, 1, 0)
    $ playAudio(sfx_moan_breath2, "sfx", 6, False)

    show ep05_hosd3_amb30 with vpunch
    amb "Why did you choose her over me? Ahhh... fuck..."
    mc_s "Amber, not now— ohhh..."
    amb "Yes, now. While you're inside me... mmmm... why wasn't I enough?"
    mc_s "You were enough... ahhh... you were too much..."
    amb "What does that mean? Ohhh... harder..."
    mc_s "It means you scared me... mmm... because I wanted you so badly..."

    show ep05_hosd3_amb31
    amb "And she didn't scare you? Ahhh... fuck yes..."
    mc_s "She was safe... ohhh... you were everything..."
    amb "Am I still everything? Mmmm... God, yes..."
    mc_s "More than everything... ahhh..."
    amb "Then prove it... ohhh... make me forget every night I cried... ahhh..."
    mc_s "I will... fuck, I will..."

    show ep05_hosd3_amb32 with vpunch
    amb "I used to touch myself thinking about this... ahhh..."
    mc_s "Yeah? Mmm..."
    amb "Every night after you left... ohhh... imagining you coming back..."
    mc_s "I should have... fuck..."
    amb "You're here now... mmmm... ahhh..."
    mc_t "The way she moves... like she's trying to get closer than possible."

    $ setChannelVolume("sfx", 7, 1, 0)
    $ playAudio(sfx_moan_breath3, "sfx", 7, False)

    show ep05_hosd3_amb33 with vpunch
    amb "I love how you feel inside me... ohhh..."
    mc_s "I love being inside you... mmm..."
    amb "Better than her? Ahhh... fuck..."
    mc_s "There is no comparison... ohhh..."
    amb "Good answer..."
    mc_s "It's the truth... ahhh..."

    scene eigengrau
    $ setChannelVolume("sfx", 4, 1.0, 0)
    $ playAudio(sfx_moan_breath, "sfx", 4, False)

    show ep05_hosd3_amb60 at focus_shift, ken_burns_corner_to_corner3
    amb "I want to ride you... ohhh... show you what you missed..."
    mc_s "Show me... mmm..."
    amb "Watch my face while I take what's mine... ahhh..."
    mc_s "You're so fucking beautiful like this... ohhh..."
    amb "Like what? Mmmm..."
    mc_s "Wild. Free. Mine... fuck..."

    show ep05_hosd3_amb34 with vpunch
    amb "Tell me I'm better than your fantasies... ahhh..."
    mc_s "You're destroying every fantasy I ever had... ohhh..."
    amb "Good. I want to be the only thing you think about... mmmm..."
    mc_s "You already are... fuck..."

    show ep05_hosd3_amb35 at subtle_zoom_out with hpunch
    amb "God, you're so deep... ohhh... mmmm..."
    mc_s "Is it too much? Ahhh..."
    amb "It's perfect. You're perfect... ohhh..."
    mc_s "So are you... fuck..."
    amb "We're perfect together... ahhh... mmmm..."
    mc_s "Always have been... ohhh..."

    scene eigengrau
    $ setChannelVolume("sfx", 9, 0.4, 0)
    $ playAudio(sfx_panting1, "sfx", 9, False)

    show ep05_hosd3_amb61 at focus_shift, ken_burns_left_to_right
    amb "I'm going to cum... ahhh... are you close?"
    mc_s "Getting there... mmm..."
    amb "Cum with me. I want us to cum together... ohhh..."
    mc_s "Amber... fuck..."
    amb "Please. Make this perfect... ahhh... mmmm..."
    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False)

    show ep05_hosd3_amb36 with vpunch
    amb "From behind. I want to feel you deeper... ohhh..."
    mc_s "Mmm..."
    amb "You'll feel even bigger this way... mmmm..."
    mc_s "Are you sure?"

    show ep05_hosd3_amb37
    amb "Don't stop. Please don't stop..."
    mc_s "You want it?"
    amb "I never want this to end... "
    mc_s "Neither do I..."
    amb "Then don't let it and put it back in... mmmm..."
    mc_s "Mmmm..."

    show ep05_hosd3_amb38 at ken_burns_bottom_to_top with hpunch
    amb "Touch me. Touch all of me... ohhh..."
    mc_s "Where? Mmm..."
    amb "Everywhere... ahhh... fuck..."
    mc_s "Like this? Ohhh..."
    amb "Yes... God, yes... mmmm... ahhh..."
    scene eigengrau
    $ setChannelVolume("sfx", 2, 0.2, 0)
    $ playAudio(sfx_moan_generic, "sfx", 2, False)

    show ep05_hosd3_amb57 at focus_shift, ken_burns_right_to_left
    amb "Now, [mc_name]. Come with me now... ahhh..."
    mc_s "Amber! Not yet... fuck..."
    amb "Yes! God, yes... mmmm... ahhh..."
    mc_t "She's perfect. Absolutely perfect."
    mc_t "How did I live without this?"

    scene eigengrau
    show ep05_hosd3_amb58 at focus_shift, ken_burns_top_to_bottom, vpunch_effect(time=0.2, offset=5, pause=0.8)
    amb "I'm so close, [mc_name]. So fucking close... ahhh..."
    mc_s "Let go. I've got you... mmm..."
    amb "Promise you won't leave after? Ohhh..."
    mc_s "I promise... fuck..."
    amb "Then make me yours... ahhh... mmmm..."
    mc_s "You already are mine... ohhh..."

    show ep05_hosd3_amb39 with vpunch
    amb "Harder. I can take it... ahhh..."
    mc_s "You sure? Mmm..."
    amb "I'm sure... ohhh... fuck..."
    mc_s "Fuck, Amber... ahhh..."
    amb "That's it. Use me... mmmm... ohhh..."
    mc_s "I need you... fuck..."

    scene eigengrau
    show ep05_hosd3_amb59 at focus_shift, ken_burns_right_to_left, vpunch_effect(time=0.2, offset=5, pause=0.7)
    amb "Did she ever let you do this? Ahhh... fuck..."
    mc_s "Amber, please— mmm..."
    amb "Answer me. While you're fucking me... ohhh..."
    mc_s "No. Never like this... ahhh..."
    amb "Good. mmmm..."
    mc_s "Fuck..."

    scene eigengrau
    show ep05_hosd3_amb40 with hpunch
    amb "I'm going to come, [mc_name]... ahhh... fuck..."
    mc_s "Me too. Fuck, me too... ohhh..."
    amb "Inside me. Come inside me... mmmm..."
    mc_s "Are you sure? Ahhh..."
    amb "I've never been more sure... ohhh..."
    mc_s "Amber... fuck..."

    $ setChannelVolume("sfx", 9, 0.4, 1.0)
    $ playAudio(sfx_femheavybreath, "sfx", 9, False)

    show ep05_hosd3_amb42 with vpunch
    amb "Don't stop. Keep going... ohhh..."
    mc_s "I can't... I'm coming... ahhh..."
    amb "I can feel you... mmmm... fuck..."
    mc_s "Amber... fuck... ahhh..."
    amb "Give me everything... ohhh..."
    mc_s "I love you... mmm..."

    show ep05_hosd3_amb41 with hpunch
    amb "I want more. I want all of you... ahhh..."
    mc_s "You have all of me... ohhh..."
    amb "Do I? Even the parts you gave to her? Mmmm..."
    mc_s "There are no parts left for anyone else... fuck..."
    amb "Promise me... ahhh..."
    mc_s "I promise... ohhh..."

    show ep05_hosd3_amb43 with hpunch
    amb "Inside. Please... ahhh... mmmm..."
    mc_s "Are you sure? Ohhh..."
    amb "I've never been more sure... fuck..."
    mc_t "This is it. Everything's changing."
    mc_t "And I want it to change."
    menu:
        "Cum inside Amber":
            $ setChannelVolume("sfx", 2, 0.2, 0)
            $ playAudio(sfx_moan_orgasm_generic, "sfx", 2, False)
            pause 0.8
            pass
    show white zorder 1.0 at ejaculation_flash
    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_cum_bigload_fast, "sfx", 1, False)

    show ep05_hosd3_amb44 at vpunch with flash
    amb "Yes... fill me up... ahhh... mmmm..."
    mc_s "Amber... I'm coming... ohhh..."
    amb "I can feel you. So warm... ahhh..."
    mc_s "God, I love you... fuck..."
    amb "I love you too... mmmm..."
    mc_t "This is perfect. She's perfect."

    $ ss.add("amber", "sex")
    $ ss.add("amber", "creampie")

    show ep05_hosd3_amb45
    amb "Don't pull out yet. Stay with me... ohhh..."
    mc_s "As long as you want... mmm..."
    amb "Forever? Ahhh..."
    mc_s "If that's what you want... fuck..."
    amb "It is... mmmm..."
    mc_s "Then forever it is... ohhh..."

    $ stopAudio("music", 2, 2)
    $ stopAllSubchannels("sfx", 2)
    $ setChannelVolume("amb", 4, 0.6, 2)
    $ setChannelVolume("amb", 5, 0.2, 2)
    scene eigengrau with slowfade
    show ep05_hosd3_amb46 at ken_burns_bottom_to_top
    amb "That was... mmm..."
    mc_s "Yeah."
    amb "Better than I imagined. And I imagined it a lot."
    mc_s "Me too."
    amb "Really? You thought about me?"
    mc_s "More than I should have."

    show ep05_hosd3_amb47 at ken_burns_left_to_right
    amb "No regrets?"
    mc_s "None. You?"
    amb "Just one."
    mc_s "What's that?"
    amb "That we waited so long."
    mc_s "Waited for what?"

    show ep05_hosd3_amb48
    amb "For you to cum inside me."
    mc_s "You're absolutely nuts—but kinda charming."
    amb "You think so?"
    mc_s "I know so."
    amb "We should clean up before going back."
    mc_s "Probably."

    show ep05_hosd3_amb49
    amb "This isn't just sex for me."
    mc_s "I know. It's not for me either."
    amb "Good. Because I can't do casual. Not with you."
    mc_s "I don't want casual either."
    amb "What do you want?"
    mc_s "You. All of you."

    show ep05_hosd3_amb50
    amb "I used to dream about moments like this."
    mc_s "Just holding each other?"
    amb "Being yours. Really yours."
    mc_s "You are mine. You always have been."

    show ep05_hosd3_amb51
    amb "I'm scared."
    mc_s "Of what?"
    amb "That this is too good to be real. That I'll wake up and you'll be gone again."
    mc_s "I'm not going anywhere."
    amb "You said that before."
    mc_s "This time is different."
    amb "How?"
    mc_s "Because this time, I'm choosing to stay."

    $ setChannelVolume("sfx", 3, 0.1, 0)
    $ playAudio(sfx_phone, "sfx", 3, False)

    show ep05_hosd3_amb52 with slowfade
    amb "Shit, I need to check my stream schedule."
    mc_s "Right now?"
    amb "Sorry, but AmberDark has commitments. Even if Amber just had the best sex of her life."
    mc_s "How do you switch like that?"
    amb "Practice. And compartmentalization."
    amb "Stream starts in forty minutes."
    scene eigengrau with slowfade
    $ setChannelVolume("music", 3, 0.3, 0)
    $ playAudio(amber_theme, "music", 3, True, 4, 0)

    show ep05_hosd3_amb53 at ken_burns_left_to_right
    amb "Come here."
    mc_s "What?"
    amb "I want to say goodbye properly. Not just 'see you at home.'"
    mc_s "We do live together."
    amb "Exactly. Which makes this complicated."
    amb "Promise we won't make breakfast weird."
    mc_s "Define weird."

    show ep05_hosd3_amb54
    amb "No awkward avoiding, no pretending this didn't happen."
    mc_s "What do you want it to be?"
    amb "I want us to figure it out. No pressure."
    mc_s "Us?"
    amb "Yeah, us. Like it should have been."
    amb "Now go check on [mo_r]. I need to get home for my stream."
    show ep05_hosd3_amb55
    amb "And [mc_name]?"
    mc_s "Yeah?"
    amb "Next time, let's find somewhere with a bed. This concrete sucks."
    mc_s "Next time?"
    amb "Oh, there's definitely going to be a next time."
    $ stopAllAudio(2.0)
    jump ep05_elidream    




label ep05_elidream:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show days
    pause 3
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    $ setChannelVolume("amb", 2, 0.15, 0)
    $ playAudio(sfx_heart_monitor, "amb", 2, True, 2, 0)
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_clinicroom, "amb", 3, True, 2, 0)

    show ep05_hosd3_eli20 at ken_burns_right_to_left
    eli "There's my sweet boy..."
    eli "You stayed with me all night, didn't you?"
    eli "Always there when [mommy_r_low] needs you most."
    $ stopAllSubchannels("amb", 2)
    scene eigengrau with bokeh
    $ setChannelVolume("amb", 4, 0.6, 0)
    $ playAudio(sfx_fashion, "amb", 4, True, 2, 0)
    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(photos_theme, "music", 1, True, 4, 0)

    show ep05_hosd3_eli01 at focus_shift with clouds_inverse
    "Producer" "You can't be here, kid! This is a professional set!"
    eli "He's with me. School holiday."
    eli "My [so_r_low] stays where I want him."
    mc_t "Everyone's staring at [mo_r]'s dress... you can see everything through it."

    $ setChannelVolume("sfx", 1, 0.3, 0)
    $ playAudio(sfx_cameras_photoshoot, "sfx", 1, False, 4, 4)

    show ep05_hosd3_eli02
    eli "Sorry about dragging you to another boring shoot, baby."
    $ show_walkthrough("ep05_elid_m1")
    menu:
        "It's fine, Mom. I like watching you work.":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_s "It's cool, [mo_r]. I kinda like seeing you do your thing."
            eli "You're so sweet to say that, sweetheart."
            mc_t "She smiled like... really smiled. Like she's glad I'm here."

            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
        "It's okay. Better than being home alone.":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_s "Honestly? Way better than hanging out alone at home."
            eli "At least someone appreciates my company."
            mc_t "She sounded kinda down... maybe I should've been more into it."

            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
        "I don't mind waiting around.":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_s "It's cool—I don't really mind hanging around."
            eli "Such a patient boy... sometimes too patient."
            mc_t "Why'd she sound so let down? What was I supposed to say?"
    eli "Your [da_full_r_low]'s always at that damn hospital anyway."
    $ show_walkthrough("ep05_elid_m2")
    menu:
        "I shouldn't be looking at her like this...":
            $ ep05_guilt_points += 1
            hide screen walkthrough_screen

            mc_t "Shit, that dress is way too tight... I really shouldn't be looking."
            mc_t "Dude, she's my [mo_r_low]... why the hell am I even thinking this?"
        "She looks incredible in that dress":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_t "Jesus, [mo_r] looks... fuck, that dress doesn't hide anything."
            mc_t "Oh fuck, I can totally see... through that thing."

            $ rm.update("elizabeth", "cor", 1)
            $ check_levels("elizabeth", "cor", 1)
        "I'll just focus on something else":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_t "Okay, just focus on the cameras and shit."
            mc_t "Stop thinking about it, man. Just... don't."

            $ rm.update("elizabeth", "cor", -1)
            $ check_levels("elizabeth", "cor", -1)

    show ep05_hosd3_eli03
    eli "You're the only man who never disappoints me, you know that?"
    eli "[daddy_r] makes promises he breaks, but not my boy."
    $ show_walkthrough("ep05_elid_m3")
    menu:
        "I'll always be here for you, Mom.":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_s "Yeah, I'll stick around for you, [mo_r]."
            eli "Always? That's a big promise, sweetheart."
            eli "But I believe you mean it."
            mc_t "The way she's looking at me... it's kinda different than how she looks at [da_r]."

            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
        "I try my best not to let you down.":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_s "I try not to mess things up, you know?"
            eli "You never could, baby. You're perfect just as you are."
            mc_t "Perfect? I mean... that's still kinda a lot to live up to."

            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
        "That's what family does.":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_s "That's just what [fm_r_low] does, right?"
            eli "[fm_r]... yes, I suppose that's what we are."
            mc_t "She sounded kinda bummed when I said '[fm_r_low]'... did I say something wrong?"

    show ep05_hosd3_eli04
    "Producer" "Fifteen minutes to showtime!"
    "Producer" "Elizabeth, you look absolutely stunning tonight!"
    "Producer" "The cameras are going to love you!"
    eli "Wait for me at the hotel hall, sweetheart."
    $ stopAudio("music", 1, 2)
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_hotel_lobby, "amb", 3, True, 2, 0)

    show ep05_hosd3_eli05 at focus_shift
    eli "They want me for another shoot after this one."
    eli "I need you to wait a little longer, baby. Can you do that for [mommy_r_low]?"
    mc_s "How long you gonna be?"
    eli "Just a few hours. Stay in the hotel where it's safe."
    $ stopAudio("amb", 3, 2)
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 4, 0.6, 0)
    $ playAudio(sfx_room_noise, "amb", 4, True, 2, 0)

    show ep05_hosd3_eli06 at ken_burns_left_to_right
    mc_t "She never came back... it's been forever."
    mc_t "Maybe she's in her room? The door's kinda open..."
    mc_s "[mo_r]? You in there?"

    $ show_walkthrough("ep05_elid_m4")
    menu:
        "I should leave immediately":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_t "Oh fuck... I gotta get out of here right now."
            mc_t "This is so messed up, like really fucking wrong."

            $ rm.update("elizabeth", "cor", -1)
            $ check_levels("elizabeth", "cor", -1)
        "I should see if she's okay":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_t "What's she doing? Maybe I should check if she's okay or something."
            mc_t "What if she's hurt or sick ?"
        "I'll just pretend I didn't see anything":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_t "If I just back away real quiet, she won't even know I was here."
            mc_t "Yeah, better to just avoid this whole mess."

            $ rm.update("elizabeth", "cor", -2)
            $ check_levels("elizabeth", "cor", -2)
    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(elizabeth_sexy_theme, "music", 2, True, 4, 0)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_door_open_creak, "sfx", 1, False, 0, 0)
    $ setChannelVolume("amb", 4, 0.3, 1)

    show ep05_hosd3_eli07 at camera_zoom
    eli "Don't leave me... not tonight..."
    eli "Everyone always leaves when I need them..."
    eli "Someone stay with me... please..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "She's like, really wasted... I probably shouldn't be here."
        mc_t "But I can't just ditch her like this, right?"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "She looks kinda... I don't know, vulnerable or whatever."
        mc_t "Maybe this is like, what she needs or something?"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "This is way too much... I gotta think about something else."
        mc_t "Maybe I should call [da_r]."
    else:
        mc_t "I don't even know what I'm feeling right now."
        mc_t "Like, part of me wants to help, but part of me just wants to get out of here."

    show ep05_hosd3_eli08 at ken_burns_corner_to_corner3
    eli "So fucking empty... this room, this life..."
    eli "Nothing but cameras and fake smiles..."
    eli "Need to feel something real... mmm..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "She's... doing stuff... I should probably leave but..."
        mc_t "What if she like, hurts herself or something? She's totally wasted."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "She's... doing that... and it's kinda hot."
        mc_t "I've never seen... like, anything like this before."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "She needs help but like, not from me."
        mc_t "This is way beyond what I should be dealing with."
    else:
        mc_t "This is so messed up... I have no idea what to do."
        mc_t "Should I stay or just... get out of here?"

    $ setChannelVolume("sfx", 2, 0.8, 0)
    $ playAudio(sfx_female_hmm2, "sfx", 2, False, 2, 0)

    show ep05_hosd3_eli28 #anim
    eli "All these men... they look but never see..."
    eli "Never stay... never love the broken parts... ahh..."
    eli "But my boy... mmm... he sees everything..."
    eli "Sees [mommy_r_low] when she's not performing... ooh..."
    show ep05_hosd3_eli09
    eli "Always alone when the lights go down... ahh..."
    eli "They want the fantasy, not the woman..."
    eli "My sweet boy... ooh... the only one who sees me..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "This is making me feel sick, but I can't just bail on her."
        mc_t "What's she even need right now?"
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "I don't get why I'm even thinking about that."
        mc_t "She looks... kinda perfect like this."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "What's she even mean by that?"
        mc_t "Maybe it's just the booze talking."
    else:
        mc_t "This is so weird... like, is she hurt or something?"
        mc_t "I have no clue what I'm even feeling right now."

    show ep05_hosd3_eli10
    eli "[mc_name]... mmm... you never leave [mommy_r_low]..."
    eli "The only man who stays... ahh... who cares..."
    $ show_walkthrough("ep05_elid_m5")
    menu:
        "I want to respond, to comfort her...":
            hide screen walkthrough_screen
            $ ep05_curiosity_points += 1

            mc_t "I wanna tell her I'm here, that I'll like, always be around for her."
            mc_t "She's saying my name while she's... oh shit."

            $ rm.update("elizabeth", "cor", -1)
            $ check_levels("elizabeth", "cor", -1)
        "I shouldn't be hearing this...":
            hide screen walkthrough_screen
            $ ep05_guilt_points += 1

            mc_t "She's saying my name while she's... this is so fucked up."
            mc_t "I really shouldn't be hearing this, but I can't like... move."

            $ rm.update("elizabeth", "cor", 1)
            $ check_levels("elizabeth", "cor", 1)
        "I need to stay completely silent":
            hide screen walkthrough_screen
            $ ep05_evasive_points += 1

            mc_t "I can't encourage this shit but I can't stop it either."
            mc_t "Maybe if I just stay super quiet and don't move..."

            $ rm.update("elizabeth", "cor", -2)
            $ check_levels("elizabeth", "cor", -2)
    eli "Even when I'm alone... you're still with me... ooh..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "She's thinking about me while she's... shit, that's messed up."
        mc_t "This is like, really weird but she's hurting."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "She's actually thinking about me... like, saying my name and stuff."
        mc_t "Maybe we've got something kinda special going on?"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "She probably doesn't actually mean me though."
        mc_t "She's just like, confused and wasted."
    else:
        mc_t "I'm so lost... like, is this bad or what?"
        mc_t "My body's doing one thing but my brain's like freaking out."

    scene eigengrau
    show ep05_hosd3_eli24 #anim
    eli "This body... mmm... it's all I have to offer..."
    eli "But he loves me for more... ahh... loves broken [mommy_r_low]..."
    eli "Not like the others... ooh... who take and leave..."
    eli "He stays... even when I'm ugly inside... mmm..."
    scene eigengrau
    $ setChannelVolume("sfx", 3, 0.8, 0)
    $ playAudio(sfx_inhale_fem, "sfx", 3, False, 2, 0)

    show ep05_hosd3_eli25 #anim
    eli "So tired of being used... ooh... want to be loved..."
    eli "My beautiful boy would never hurt me... mmm..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "I mean, yeah I love her... but not like, in that way."
        mc_t "She's getting stuff mixed up, like different types of love."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "I do care about her... all the messed up parts too."
        mc_t "Maybe I can just be whatever she needs, you know?"
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "I love her 'cause she's my [mo_r_low], that's it."
        mc_t "This'll probably seem super weird tomorrow."
    else:
        mc_t "The way she talks about love... it's kinda desperate, man."
        mc_t "Maybe she needs something I can't really give her."

    scene eigengrau
    show ep05_hosd3_eli27 #anim
    eli "Someone who stays... ahh... who loves all of me..."
    eli "Not just the pretty parts... mmm... the broken parts too..."
    scene eigengrau
    show ep05_hosd3_eli26 #anim
    eli "Come closer, baby... ooh... don't be scared..."
    eli "[mommy_r] needs you... ahh... needs to feel wanted..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "Does she know I'm here? She's been like, talking to me this whole time."
        mc_t "This is so messed up but she's like, really hurting right now."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "Does she know I'm here? Kinda seems like she wants me to come closer."
        mc_t "Maybe I should... I dunno, maybe she needs this or something."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "I should just look at the window... the city lights and stuff."
        mc_t "Anything but whatever she's doing right now."
    else:
        mc_t "Part of me wants to go closer, part of me just wants to bail."
        mc_t "I'm so fucking confused right now, man."

    show ep05_hosd3_eli11 with normalfade
    eli "See what desire looks like without the costume?"
    eli "Raw and desperate and real..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "I probably shouldn't be seeing this... like, I'm her [so_r_low]."
        mc_t "But maybe she's showing me 'cause she actually trusts me or something."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "She's letting me see stuff that nobody else gets to see."
        mc_t "Man... this is kinda special, I guess."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "I mean, I'm not really looking at anything specific."
        mc_t "Just some drunk lady having a meltdown."
    else:
        mc_t "This is like, beautiful but also really messed up."
        mc_t "I have no clue what this even means."

    show ep05_hosd3_eli12
    eli "This is what your [mommy_r_low] really is underneath..."
    eli "Not the perfect image... just a woman who needs..."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        eli "You don't have to hide anymore, darling..."
        eli "I'm not mad, not even close. Come here, baby."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        eli "Come out of hiding, love—it's just us now."
        eli "It's alright, I promise. Just come to me, love."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        eli "No need to stay in the shadows, sweetheart..."
        eli "There's no anger here—just me, waiting for you."
    else:
        eli "No need to keep hiding, love. You're safe with me."
        eli "There's nothing to fear, love. Just come to me."
    $ stopAudio("music", 2, 2)
    $ setChannelVolume("amb", 4, 0.6, 1)
    scene eigengrau with slowfade
    show ep05_hosd3_eli13
    eli "This never happened, you understand me? Never."
    eli "The world isn't ready for love this complicated."
    eli "You don't need to understand, baby. Just forget."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_s "[mo_r], this is like... really messed up..."
        mc_s "You're kinda wasted and not thinking straight."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_s "Yeah, I get it. Won't say anything."
        mc_s "I mean, nobody else needs to know about this stuff anyway."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_s "Yeah, sure. Whatever you want, I guess."
        mc_s "I'll just act like this never happened."
    else:
        mc_s "I honestly have no clue what to say right now."
        mc_s "This whole thing is like, really confusing."
    # CURIOSITY PATH REWARD
    if ep05_curiosity_points >= 3:
        show ep05_hosd3_eli14
        eli "Good boy. Always such a good boy for [mommy_r_low]."
        eli "Some things are better left as dreams, sweetheart."
        if ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
            mc_t "She looks amazing... like, seriously beautiful."
            mc_t "I just wanna be close to her, y'know? Like, make her feel okay."
            mc_t "Maybe this kinda stuff actually happens for real."
        elif ep05_guilt_points > ep05_evasive_points:
            mc_t "I feel guilty, yeah. But she's still crazy beautiful."
            mc_t "I swear, I won't be able to get that outta my head."
        else:
            mc_t "I'm legit trying not to stare... but she's right there."
            mc_t "Okay but seriously... How do I erase that from my brain?"

        $ ep05_ach_final2 = True
    else:
        eli "Good boy. Always such a good boy for [mommy_r_low]."
        eli "Some things are better left as dreams, sweetheart."
        if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
            mc_t "Yeah, she's right... this stuff needs to stay in dreamland."
            mc_t "But like, seeing her hurt this bad really sucks."
        elif ep05_evasive_points > ep05_curiosity_points:
            mc_t "Way better as dreams. Or like, nightmares, whatever."
            mc_t "I just wanna go home and forget this whole mess."
        else:
            mc_t "I don't even know what to think anymore, man."
            mc_t "Everything's just so messed up and confusing."

    show ep05_hosd3_eli15
    eli "Come here, let [mommy_r_low] hold you."
    eli "You're shaking, sweet boy."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_s "I'm not freaked out or anything... just kinda confused and feel bad about it."
        mc_t "This is messed up but like... I can't just ditch her."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_s "I'm not scared or whatever... just feeling some weird new stuff."
        mc_t "Being this close to her is like... I don't know, intense or something."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_s "I'm good, [mo_r]. Just beat, you know?"
        mc_t "Can't wait for this to be over."
    else:
        mc_s "I'm just like... there's too much going on right now."
        mc_t "I have no clue what's going on with me right now."

    show ep05_hosd3_eli16
    eli "Confusion is normal when you see something beautiful."
    eli "Your heart's racing... mine too."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "My heart's going crazy but it's just guilt, not like... excitement."
        mc_t "But her skin's so warm though..."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "Her skin's so warm... and she's like, barely wearing anything."
        mc_t "I just wanna be close to her, y'know? Like, make her feel okay."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "I just want this whole thing to be done."
        mc_t "Tomorrow we'll probably just pretend this never happened."
    else:
        mc_t "My heart's going crazy... but I don't even know why."
        mc_t "Fear? Like, excitement? Guilt? All that shit?"

    $ stopAllSubchannels("amb", 2)
    scene eigengrau with slowfade
    $ setChannelVolume("music", 5, 0.3, 0)
    $ playAudio(elizabeth_theme, "music", 5, True, 4, 0)
    $ setChannelVolume("amb", 6, 0.4, 0)
    $ playAudio(sfx_nightclub, "amb", 6, True, 2, 0)

    show ep05_hosd3_eli17
    eli "The world doesn't understand connections like ours."
    eli "They see wrong where there's only love."
    mc_s "What are you saying, [mo_r]?"
    eli "I'm saying you're the only person who's never left me, baby."
    show ep05_hosd3_eli18
    eli "And maybe that means something more than they'd approve of."
    eli "But their approval never kept anyone warm at night."
    if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
        mc_t "This feels like I'm crossing some line I probably shouldn't."
        mc_t "But she needs someone... like, anyone."
    elif ep05_curiosity_points > ep05_guilt_points and ep05_curiosity_points > ep05_evasive_points:
        mc_t "Maybe some lines are like, meant to be crossed."
        mc_t "Maybe this is just natural between us or something."
    elif ep05_evasive_points > ep05_guilt_points and ep05_evasive_points > ep05_curiosity_points:
        mc_t "I'm not crossing any lines. This is just talking."
        mc_t "Just drunk, confused talking."
    else:
        mc_t "I don't even know where the lines are anymore."
        mc_t "Everything feels kinda blurry and messed up."
    # GUILT PATH REWARD
    if ep05_guilt_points >= 3:
        show ep05_hosd3_eli19
        if ep05_guilt_points > ep05_curiosity_points and ep05_guilt_points > ep05_evasive_points:
            mc_t "I can see... like, everything through that dress."
            mc_t "I shouldn't be looking but... damn, she's really pretty."
            mc_t "Even when she's all messed up, she's still... you know."
        elif ep05_curiosity_points > ep05_evasive_points:
            mc_t "Her dress is like, totally see-through... I can see her..."
            mc_t "Part of me feels like shit, part of me just... can't look away."
        else:
            mc_t "Her dress is kinda see-through but I'm trying not to, like, notice."
            mc_t "This guilt is seriously messing with my head."
        eli "Take a good look, sweet boy. Remember this moment."
        $ ep05_ach_final1 = True

    show ep05_hosd3_eli18 at focus_shift_sms
    $ stopAudio("music", 5, 2)
    $ stopAllSubchannels("amb", 2)
    pause 1
    scene eigengrau with clouds
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)
    $ setChannelVolume("amb", 2, 0.15, 0)
    $ playAudio(sfx_heart_monitor, "amb", 2, True, 2, 0)
    $ setChannelVolume("amb", 3, 0.6, 0)
    $ playAudio(sfx_clinicroom, "amb", 3, True, 2, 0)

    show ep05_hosd3_eli21
    mc_t "She looks so peaceful now... so different from before."
    mc_t "Was that real or just some fucked up dream?"
    mc_t "But I can still feel where she touched my hair..."

    show ep05_hosd3_eli22
    eli "[mc_name]...? You're... still here..."
    mc_s "I'm here, [mo_r]. How are you feeling?"
    eli "Had a... dream... about you... about us..."
    eli "You were so... young... shouldn't have... seen..."
    mc_s "What dream?"
    eli "Better left... as dreams... sweetheart..."
    $ setChannelVolume("sfx", 1, 0.1, 0)
    $ playAudio(sfx_phone, "sfx", 1, False, 1, 1)

    show ep05_hosd3_eli23
    mc_t "My phone's buzzing..."
    mc_t "A message from Madison? That's weird, she never texts me."
    mc_t "'Hey big [br_full_r_low], remember we were supposed to hang out today? Come meet me at the main lobby right now. Don't keep me waiting.'"
    mc_t "Hang out? This sounds off."
    mc_t "Madison doesn't talk like this. Too... polite? Formal?"
    mc_t "Since when does she call me 'big [br_full_r_low]' unironically?"
    mc_t "Something's weird about this message."
    mc_t "I don't want to leave [mo_r] when she's finally talking about... whatever that was."
    mc_t "But Madison never asks for anything. If she's reaching out..."
    mc_t "Maybe something's wrong?"

    $ stopAllAudio(2.0)
    jump ep05_hosfinal




label ep05_hosfinal:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_clinicwalla, "amb", 1, True, 2, 0)

    show ep05_hosd3_mic01
    mc_t "That message was weird as fuck..."
    mc_s "Madison? What are you doing here?"
    mad "I texted you, remember? We need to talk."
    mc_s "About what? And why here?"
    mad "About [mo_r]. About [da_r]. About things you need to know."
    mc_t "She's being way too serious."

    $ setChannelVolume("music", 1, 0.3, 0)
    $ playAudio(mic_theme, "music", 1, True, 4, 0)

    show ep05_hosd3_mic02 with hpunch
    mad "There he is. Right on time."
    mc_s "[da_r]."
    mic "[mc_name]. Still here?"
    mad "I called him, [daddy_r]. Just like we discussed."
    mc_t "Wait... they discussed this? What the fuck is going on?"
    mic "Madison, dear, let the grown-ups handle this conversation."
    mad "Of course, [daddy_r]. Sorry."
    mc_t "Huh? She just... apologized?"

    show ep05_hosd3_mic03
    mc_s "Before anything else, I need to know—what meds are you giving [mo_r]?"
    mic "Standard anti-anxiety protocol. Lorazepam, primarily."
    mic "Not that you'd understand the pharmacology, [mc_name]."
    mad "[daddy_r] knows what he's doing. He's helped [mo_r] so much over the years."
    mic "Madison, sweetie, your [da_full_r_low] and [br_full_r_low] need to discuss medical matters. Perhaps you should wait outside?"
    mad "Oh... okay. I'll just... stand here quietly."
    mc_t "She's accepting being dismissed like a fucking child. What happened to the Madison who never backs down?"

    $ show_walkthrough("ep05_mcmic_m1")
    menu:
        "[Darkness] Demand the truth about her medication":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -5)

            mc_s "Cut the bullshit, Michael. What are you really giving her?"
            mic "Such hostility. And here I thought police training taught discipline."
            mic "But then again, you've always been more emotion than intellect, haven't you?"

        "[Balance] Ask for specifics about her treatment":
            hide screen walkthrough_screen

            mc_s "I need to know exactly what medications she's been taking."
            mic "Your investigative instincts showing, [mc_name]? How... predictable."
            mic "Like a dog chasing cars, you bark loudly but comprehend nothing."

        "[Light] Assert your right to know as her son":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 5)

            mc_s "As her [so_r_low], I have a right to know her treatment plan."
            mic "Rights. How quaint. Medical decisions require expertise, not familial sentiment."
            mic "Your 'rights' are as meaningless as your presence here."
    show ep05_hosd3_mic04
    mc_t "I keep thinking about how she looked in that bed..."
    mc_t "So pale, so fragile. The machines beeping around her like a fucking death watch."
    mc_t "Her hands... they were shaking even while she slept. What the hell has he done to her?"
    mc_t "She looks like a ghost of herself."
    mc_s "Have you even seen her in that bed? She looked completely broken lying there."
    mic "Elizabeth has always been... fragile. You simply chose not to see it."
    mic "Or perhaps you were too self-absorbed to notice."
    show ep05_hosd3_mic05
    mc_t "All those bottles I found in her bedroom..."
    mc_t "Alprazolam, Clonazepam, some unmarked pills... enough to kill a horse."
    mc_t "Half of them had his clinic's labels, not proper pharmacy ones. That's not fucking normal."
    mc_t "The way they were scattered around like candy... how long has this been going on?"
    mc_s "I saw the prescription bottles in her room. Half of them don't have proper pharmacy labels."
    mic "Custom compounds. I have them prepared at my clinic."
    mic "Far beyond anything your limited understanding could grasp."
    show ep05_hosd3_mic06
    mc_s "That's not standard practice."
    mic "When did you become an expert in psychiatric medication, [mc_name]? Between getting shot and abandoning your responsibilities?"
    mic "Your expertise extends to... what exactly? Getting yourself hospitalized? Spectacular achievement."
    mad "I... I never knew it was that serious."
    mic "Madison, dear, these are complex matters best left to those with actual education."
    mad "Yes, [daddy_r]. I'm sorry for interrupting."
    mc_t "She's just... accepting his condescension. This isn't the Madison I know."

    $ show_walkthrough("ep05_mcmic_m2")
    menu:
        "[Darkness] Accuse him of hiding something":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -8)

            mc_s "You're hiding something, and I'm going to find out what."
            mic "Such determination. Such... futility."
            mic "You couldn't even stay conscious during a simple arrest. What makes you think you can solve this?"

        "[Balance] Challenge his medical practices":
            hide screen walkthrough_screen

            mc_s "I don't need to be a doctor to recognize malpractice."
            mic "Malpractice? From someone who let criminals put a bullet in him?"
            mic "Your judgment has proven... questionable at best."

        "[Light] Threaten to involve medical authorities":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 8)

            mc_s "There are medical boards that review cases like this."
            mic "Medical boards staffed by my dear colleagues. How charmingly naive."
            mic "You still believe in systems, don't you? After everything you've seen?"
    show ep05_hosd3_mic07
    mic "Your [mo_full_r_low]'s condition requires specialized treatment that isn't available through conventional channels."
    mic "Elizabeth has always had... episodes. Instability. More severe than you've been allowed to see."
    mic "I developed a regimen that gives her peace. Stability."
    mic "Memory reconsolidation inhibitors combined with targeted anxiolytics."
    show ep05_hosd3_mic08
    mc_s "Memory inhibitors? You're suppressing her memories?"
    mic "I'm treating intrusive traumatic recall patterns. It's cutting-edge psychiatry."
    mic "Far beyond your comprehension, naturally."
    $ show_walkthrough("ep05_mcmic_m3")
    menu:
        "[Darkness] Angrily accuse him of experimenting":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -10)

            mc_s "You're fucking experimenting on her!"
            mic "Such language. Such... impotence."
            mic "Emotional volatility. Perhaps you inherited more from your [mo_full_r_low] than I hoped."
        
        "[Balance] Question Elizabeth's knowledge of the treatment":
            hide screen walkthrough_screen

            mc_s "Does she know what these pills actually do?"
            mic "Informed consent is a luxury Elizabeth cannot afford in her current state."
            mic "But I wouldn't expect you to understand such nuances."
        
        "[Light] Point out the legal and ethical violations":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 10)

            mc_s "That's illegal. Unethical. You're violating her basic rights."
            mic "Ethics are subjective, especially in medical advancement."
            mic "Your morality is as rigid as your thinking. Both equally useless."
    show ep05_hosd3_mic09
    mic "My research has helped countless patients find peace from traumatic memories."
    mic "Though I doubt you'd appreciate the elegance of the methodology."
    mc_s "Research? Is that all [mo_r] is to you? A test subject?"
    mic "She's a case study in successful memory modification. One of my greatest achievements."
    mc_t "He's talking about her like she's not even human. And I can't do anything to stop him."

    show ep05_hosd3_mic10
    mic "Your [mo_full_r_low] witnessed something she shouldn't have. Many years ago."
    mic "Something that... affected her deeply."
    mc_s "What did she see?"
    mic "That's not important. What matters is that knowing endangered her. Endangered all of us."
    mic "But again, strategic thinking was never your strength."
    show ep05_hosd3_mic11 at ken_burns_bottom_to_top
    mic "I protected her the only way I could – by helping her forget."
    mc_s "She's remembering now, isn't she? That's why you're panicking."
    mc_s "I can see it in your eyes. Your perfect little experiment is falling apart."
    mc_t "Got him. He actually looks uncomfortable for the first time."

    show ep05_hosd3_mic12 at ken_burns_right_to_left
    mic "Panicking? How delightfully naive."
    mic "I don't panic, [mc_name]. I adapt. Which is why I've had Elizabeth committed for psychiatric evaluation."
    mic "Seventy-two hours minimum, potentially extendable to thirty days."
    mc_s "You can't do this."
    mic "Your opinion, as always, is irrelevant."
    $ show_walkthrough("ep05_mcmic_m4")
    menu:
        "[Darkness] Threaten to take matters into your own hands":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -8)

            mc_s "I'll handle this myself. You won't get away with this."
            mic "Handle it yourself? Like you handled that arrest in Osaka?"
            mic "Your track record for 'handling' things is rather... unimpressive."
        "[Balance] Promise to investigate officially":
            hide screen walkthrough_screen

            mc_s "I'll investigate this through proper channels."
            mic "With what evidence? Your detective's intuition?"
            mic "You have nothing. You are nothing. You can do nothing."

        "[Light] Threaten to file a formal report":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 8)

            mc_s "I'll file an official report about this."
            mic "Reports filed by detectives under psychological stress? How credible."
            mic "Your department might find your mental state... questionable."
    show ep05_hosd3_mic13
    mc_s "I won't let you destroy her mind."
    mic "You won't 'let' me? How presumptuous."
    mic "You couldn't even stay alert during a simple police operation. What makes you think you can protect anyone?"
    show ep05_hosd3_mic14
    mic "Consider this carefully, [mc_name]. Elizabeth is fragile. What happens if these memories return in full?"
    mic "The trauma, the fear... is that what you want for her? To suffer for the sake of your conscience?"
    mad "Maybe we should listen to [daddy_r]..."
    mic "Madison understands. Youth often sees more clearly than... experience."
    show ep05_hosd3_mic15
    mic "Besides, should you choose to make this... difficult... well, careers can also be so fragile."
    mc_s "Are you threatening me?"
    mic "I'm educating you about consequences. Something your generation seems to lack."
    mic "Your superiors might find certain information about our [fm_r_low]... illuminating."
    mc_t "What does he mean?"

    show ep05_hosd3_mic16
    mc_s "You sick bastard."
    mic "Security cameras in my home capture quite... comprehensive footage, [mc_name]."
    mic "Footage that could end careers, destroy reputations, ruin lives."
    mad "[daddy_r], what kind of footage?"
    mic "Nothing that concerns you, dear."
    mad "Oh. Okay."
    mc_t "Huh? Okay? What the fuck happened to her?"

    show ep05_hosd3_mic17
    mic "I had such hopes when you were born. The Crawford name, continuing in medicine perhaps."
    mic "Instead, you became... this. A failed detective, obsessing over your [mo_full_r_low], doing all that stuff you do at the house."
    mad "Stuff?"
    mic "Madison, sometimes truth is more complex than young minds can process."
    mad "I understand, [daddy_r]."
    mc_t "She's just... accepting whatever he tells her."

    show ep05_hosd3_mic18 at ken_burns_bottom_to_top
    mic "You're more like Elizabeth than me. Weak. Sentimental. Easily broken."
    mic "At least she had beauty to offer. You have... what exactly?"
    mc_s "At least I'm not experimenting on my [fm_r_low]."
    mic "My dear boy, that's exactly what you're doing. Just without the scientific method."
    mic "Without the intelligence. Without the vision. Without any meaningful result."
    show ep05_hosd3_mic19
    mic "Seven to nine, visiting hours. I'll make sure Elizabeth is lucid enough to recognize you."
    mic "Though I doubt she'll want to see the [so_r_low] who couldn't protect her."
    mic "Enjoy the rest of your night, [mc_name]."
    mc_t "He's walking away. Just... walking away like I'm nothing."

    $ stopAudio("music", 1, 2)
    scene eigengrau with slowfade
    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(mc_broken_theme, "music", 2, True, 4, 0)

    show ep05_hosd3_mic20 at ken_burns_left_to_right
    mad "[mc_name]? Are you okay? You look..."
    mc_t "She sounds concerned. Actually concerned. When did that happen?"
    mc_t "But it's too late. He's already won everything."
    mc_t "I can't protect [mo_r]. Can't protect anyone. He made that crystal fucking clear."

    show ep05_hosd3_mic21 at subtle_zoom_out
    mc_t "Madison's walking away too. Probably back to him."
    mc_t "Everyone always goes back to him."
    mc_t "I'm completely alone here. Just like I've always been."
    mc_t "He's right about everything. I am weak. I am useless."
    mc_t "And now [mo_r]'s going to suffer because I couldn't stop him."
    mc_t "What kind of [so_r_low] am I? What kind of man?"

    $ stopAllAudio(2)
    jump ep05_end




label ep05_end:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show loc_murderroom_night with slowfade
    show murderroom_location zorder 2 with dissolve
    pause 4
    hide murderroom_location with dissolve
    $ setChannelVolume("amb", 1, 0.5, 0)
    $ playAudio(sfx_factory, "amb", 1, True, 2, 0)
    $ setChannelVolume("music", 1, 0.5, 0)
    $ playAudio(antonella_horror_theme, "music", 1, True, 4, 0)

    show ep05_end01 at ken_burns_bottom_to_top
    "Unknown Woman" "Please... I don't understand why I'm here..."
    "Unknown Woman" "What did I do wrong? I've been loyal, I swear!"
    anto "You missed your appointment yesterday."
    show ep05_end02
    "Unknown Woman" "My [mo_full_r_low]... she got sick! I had to take care of her!"
    "Unknown Woman" "I was going to come today, I promise! Please, just let me explain!"
    anto "Explain what? How you planned to sell those implants to the Yamaguchi-gumi?"
    "Unknown Woman" "No! I would never! My [mo_full_r_low] had a stroke!"

    show ep05_end03
    surg "Scalpel or bone saw first?"
    anto "Scalpel. We need clean incisions."
    "Unknown Woman" "Please! You have to believe me! I have the hospital discharge papers!"
    surg "Both blades are sharp today."
    show ep05_end04
    surg "Understand this—before anything."
    "Unknown Woman" "Please, I'll do anything! I'll work for free! Forever!"
    surg "This isn't money. It's control."
    "Unknown Woman" "I am obedient! I've never disobeyed an order!"

    show ep05_end05
    anto "Tell me exactly where you were yesterday at 3 PM."
    "Unknown Woman" "At the hospital! My [mo_full_r_low] couldn't move her left side!"
    "Unknown Woman" "The nurses saw me! I stayed all night with her!"
    anto "Witnesses can be bought. Loyalty cannot."
    show ep05_end06
    anto "You know what happens to people who betray the Kudō-kai?"
    "Unknown Woman" "I didn't betray anyone! Please, just check the hospital records!"
    anto "Your [mo_full_r_low] will wonder why you never came home."
    "Unknown Woman" "She needs me! She can't take care of herself!"

    show ep05_end07
    anto "Last chance to tell the truth."
    "Unknown Woman" "I am telling the truth! Please, I have proof on my phone!"
    anto "Proof is irrelevant now."
    "Unknown Woman" "My [mo_full_r_low] is all I have left! I would never risk losing this job!"

    show ep05_end08
    surg "Ready when you are."
    anto "Proceed with the left implant."
    "Unknown Woman" "Wait! Please! I have photos from the hospital!"
    surg "This will hurt considerably."
    show ep05_end09
    "Unknown Woman" "Please! I have video calls with the nurses! Check my phone!"
    "Unknown Woman" "I would never betray the [fm_r_low] that feeds me!"
    surg "Left or right first?"
    anto "Left. And take your time."
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)
    $ setChannelVolume("sfx", 3, 0.5, 0)
    $ playAudio(sfx_blood_splash, "sfx", 3, False, 0, 0)

    show ep05_end10 at ken_burns_corner_to_corner3
    surg "Clean extraction. Product is intact."
    anto "Continue with the second one."
    "Unknown Woman" "I... I can't... feel my chest..."
    surg "Blood loss. She's fading fast."
    show ep05_end11
    surg "Here. Fifty grams, still sealed."
    anto "Good. No damage to the cocaine packets."
    surg "Should I finish her now?"
    anto "No. Give me the blade."
    show ep05_end12
    surg "Fresh scalpel for the final cut?"
    anto "Yes. This part I do myself."
    surg "As you wish."
    anto "Leave us alone for a moment."
    $ setChannelVolume("amb", 1, 0, 2)

    show ep05_end13 with slowfade
    $ setChannelVolume("sfx", 9, 1, 0)
    $ playAudio(sfx_heartbeatslow, "sfx", 9, True, 0, 0)
    anto "I'm so sorry... I'm so, so sorry..."
    "Unknown Woman" "Why... why did this happen..."
    anto "You didn't deserve this. Your [mo_full_r_low] needed you."
    anto "I'll make sure she knows you tried to come home."
    show ep05_end14
    "Unknown Woman" "Just tell her I tried... I really did. I tried to take care of her..."
    anto "I promise. I'll find a way to let her know."
    "Unknown Woman" "So cold... can't feel anything anymore..."
    anto "Rest now. No more pain."
    $ stopAudio("sfx", 9, 0)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 4, 0.5, 0)
    $ playAudio(sfx_knife_jab, "sfx", 4, False, 0, 0)
    $ setChannelVolume("amb", 1, 0.5, 0)

    show ep05_end15
    anto "Clean up this mess."
    surg "What about the [mo_full_r_low]?"
    anto "What about her? This garbage is no longer our concern."
    surg "But you said—"
    anto "I said nothing. Let's move the body."
    $ stopAudio("music", 1, 2)
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)
    scene eigengrau with slowfade
    $ setChannelVolume("music", 2, 0.3, 0)
    $ playAudio(kudokai_theme, "music", 2, True, 4, 0)
    $ setChannelVolume("amb", 2, 0.3, 0)
    $ playAudio(sfx_eveningtraffic, "amb", 2, True, 2, 0)

    show ep05_end16 at ken_burns_left_to_right
    hir "Efficient as always, Bertolini."
    anto "The product is intact. Two packets, fifty grams each."
    hir "Your foreign blood serves us well. Police never suspect a gaijin of yakuza connections."
    anto "Is that the only reason you keep me around?"
    show ep05_end17
    hir "You blend into crowds we cannot. Move through territories without suspicion."
    anto "And what's the next territory?"
    hir "Here in Tokyo. The Kobe Yamaguchi-gumi is finished, but loose ends remain."
    anto "What kind of loose ends?"
    show ep05_end18
    hir "Hideo Tanaka's death left a power vacuum in Osaka hostess clubs."
    anto "I handled that cleanly. No witnesses."
    hir "Too cleanly. Now Tokyo detectives are asking questions about yakuza connections."
    anto "What do you need me to do?"
    show ep05_end19
    hir "Eliminate the detective leading the investigation. Make it look like gang violence."
    anto "In Tokyo? That's Sumiyoshi-kai territory."
    hir "Exactly. Let them take the blame while we expand our operations."
    anto "I understand."
    hir "Good. This detective won't see you coming."
    $ stopAudio("music", 2, 2)
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)
    scene eigengrau with slowfade
    show loc_templeasak_night with slowfade
    show asakusa_location zorder 2 with dissolve
    pause 4
    hide asakusa_location with dissolve
    $ setChannelVolume("music", 3, 0.6, 0)
    $ playAudio(antonella_singing_act1, "music", 3, True, 4, 0)
    $ setChannelVolume("amb", 3, 0.3, 0)
    $ playAudio(sfx_temple_outside, "amb", 3, True, 2, 0)

    show ep05_end20 at subtle_zoom_out
    anto_t "Come, little fox spirit. Time to return to sacred ground."
    anto_t "Do you remember when [unc_r] Takeshi first brought you here?"
    anto_t "You believed the fox spirits could grant wishes for good people."
    anto_t "Such pure prayers you whispered to stone guardians."

    show ep05_end21
    anto_t "Each red torii marks a threshold between worlds."
    anto_t "Between who you were and who you must become."
    anto_t "The foxes understand that some transformations are necessary."
    anto_t "That sometimes we must become what the world needs us to be."

    show ep05_end22 at ken_burns_top_to_bottom
    anto_t "Kneel before Inari's messenger, little one."
    anto_t "The fox who serves the god of rice and prosperity."
    anto_t "But also justice. Divine justice that humans cannot provide."
    anto_t "The gods see what mortals cannot."

    show ep05_end23 at ken_burns_bottom_to_top with slowfade
    anto_t "Strip away the lies you wear like armor."
    anto_t "No clothes to hide the scars, no mask to hide the truth."
    anto_t "This is the body that carried his child."
    anto_t "This is the flesh that survived when love was stolen."

    show ep05_end24 
    anto_t "Touch the marks they left on you."
    anto_t "Isabella's birth scar. Bullet wounds from when evil tried to silence you."
    anto_t "Each scar a reminder of what was taken."
    anto_t "But you survived. Wounded, changed, but with purpose."

    show ep05_end25 at ken_burns_right_to_left
    anto_t "Time for the green mask, little fox."
    anto_t "The one that speaks wisdom wrapped in kindness."
    anto_t "In folklore, green foxes bring important messages to those who need guidance."
    anto_t "They appear to warn the good of hidden dangers."

    show ep05_end26 at subtle_zoom_out with smoke
    anto_t "Soon you'll find him again."
    anto_t "The good man who deserves to know the truth about his world."
    anto_t "He thinks he understands justice, but he hasn't seen the deeper corruption."
    anto_t "Sleep now, little spirit. Kitsune must help the righteous see clearly."

    hide screen stats_button
    hide screen walkthrough_icon
    $ stopAllSubchannels("sfx", 2)
    $ stopAllSubchannels("amb", 2)
    jump act1_ending




label act1_ending:
    scene eigengrau with rose
    show act1_ending_bg at slow_reveal zorder 1
    pause 2.0
    show sakura_movie zorder 2
    if htl_episodes == 5.3:
        $ show_custom_notification("save_tip")
    else:
        pass
    pause 6.0
    show the_end_text zorder 3 with dissolve:
        alpha 0.0
        zoom 0.8
        yoffset 30
        linear 3.0 alpha 1.0 zoom 1.0 yoffset 0
    pause 4.0
    show of_text zorder 3 with dissolve:
        alpha 0.0
        xoffset -50
        linear 2.0 alpha 1.0 xoffset 0
    pause 2.5
    show act_one_text zorder 3 with dissolve:
        alpha 0.0
        zoom 0.7
        linear 2.5 alpha 1.0 zoom 1.0
    pause 4.0
    $ renpy.call_screen("forced_pause")

    hide act_one_text with dissolve
    hide of_text with dissolve
    hide the_end_text with dissolve
    pause 1.5
    #-- End Episode 5
    $ stopAllAudio(3.0)
    $ update_htl_episodes()
    pause 2.0
    if htl_episodes == 5.3:
        return


    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep06_title