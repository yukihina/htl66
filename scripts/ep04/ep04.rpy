



label ep04_start:
    $ persistent.current_episode = 4
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ renpy.block_rollback()
    jump ep04_intro


## -- INTRO SCENE HOME




label ep04_intro:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ config.rollback_enabled = True
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 1, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_wind_pool, "amb", 2, True, 1, 0)

    show ep04_intro1 at zoom_out with slowfade
    show screen stats_button
    show screen walkthrough_icon

    mc_t "Why on earth did she keep this photo all these years? And why is it here, of all places?"
    mc_t "What am I thinking? There's got to be a logical explanation for this."
    mc_t "...I-- I'll just ask Isabella when she gets back."

    show ep04_intro2 at concentrate
    mc_t "Just when I thought I was finally starting to forget about her..."
    mc_t "It's like the universe is conspiring against me, refusing to let me move on. Every time I think I'm making progress, something like this comes out of nowhere."
    mc_t "Damn it! This is mentally exhausting."

    show ep04_intro3 at ken_burns_bottom_to_top with normalfade
    mc_t "I think I need more than just pain meds..."
    mc_t "I need a way to purge these memories, these feelings, from my mind. But how the hell do I do that?"
    mc_t "Sleep seems like the only way out of this mess..."

    show ep04_intro4 at focus_shift, ken_burns_corner_to_corner
    mc_t "Just vanish from my mind... I can't deal with this right now."
    mc_t "God, please, let me find peace in my dreams, even if it's just for a little while."

    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    jump ep04_nanapool




label ep04_nanapool:
    scene eigengrau with bokeh2
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_intro01 at slow_reveal with slowfade
    mc_t "Uhhh..."
    mc_t "Did I fall asleep again? Fuck, I can't keep doing this."
    "Girl" "Huh?"

    show ep04_nan_intro02 at focus_shift, ken_burns_left_to_right
    mc_t "What the fuck? Who is this girl?"
    mc_t "She looks so young and innocent... how the hell did she get into the house?"
    mc_s "Who are you?"

    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_yellnana, "sfx", 9, False, 0, 0)

    show ep04_nan_intro03 with hpunch
    "Girl" "AHHH!"
    mc_s "Holy shit!"

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_splashpool, "sfx", 1, False, 0, 0)

    show ep04_nan_intro04 at subtle_zoom_out with vpunch
    mc_t "Wow... that was one hell of a flash."
    mc_t "Shit! I should help her before she drowns!"

    scene eigengrau with circlewipe
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_pool_splash, "sfx", 2, False, 0, 0)

    show ep04_nan_intro05 with circlewipe
    mc_s "Whoa! Are you alright?"
    "Girl" "I--I don't... know. S-Sorry..."
    mc_s "Are you sure?"
    "Girl" "U-um... I... I think so... My clothes are all wet though..."
    mc_s "Yeah, that tends to happen when you fall into a pool. Can you stand?"
    "Girl" "I-I'll try... Oh!"
    mc_s "Whoa, easy there. Here, let me help you up."

    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.5)
    $ playAudio(sfx_pool_surfacing, "sfx", 3, False, 0, 0)

    show ep04_nan_intro07 at slow_reveal with vpunch
    mc_t "Fuck me... what a beauty!"
    mc_t "Her skirt is so short, I can almost see her pussy. I don't understand how she can walk around like that without flashing everyone."

    show ep04_nan_intro06
    mc_s "Are you hurt?"
    "Girl" "Uhm..."
    "Girl" "N-No... just a bit dizzy. I-I'm okay, really..."

    show ep04_nan_intro08 at ken_burns_right_to_left
    mc_s "Do you feel lightheaded?"
    "Girl" "I... I don't know. M-Maybe a little..."
    mc_s "What were you doing here anyway?"
    "Girl" "Aww... all my stuff is soaked... O-Oh no..."

    show ep04_nan_intro09
    "Girl" "Y-You wouldn't happen to have seen my glasses, would you? I-I can't see very well without them..."
    mc_s "I think they sank to the bottom."
    "Girl" "What about my shoes?"
    mc_s "Sorry, they're probably down there too."
    "Girl" "I don't know how I'm going to get home like this... I-I'm such a klutz..."
    mc_s "So are you gonna answer my question? What were you doing here?"

    show ep04_nan_intro10
    "Girl" "Huh? Oh... um..."
    "Girl" "Uhm..."
    "Girl" "I--I--"
    mc_s "You what?"

    show ep04_nan_intro11
    "Girl" "Um... Well... Uh... You see..."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.15)
    $ playAudio(nanami_theme, "music", 1, True, 5, 0)
    nana "I-I'm sorry, I didn't mean to cause any trouble. M-My name's Nanami. P-Please don't be angry..."
    $ rm.set_knows("nanami", True)

    mc_s "Uhhh, that doesn't really answer my question."
    nana "I'm sorry, please forgive me. I--I didn't mean to intrude, it's just..."
    mc_s "Look, I'm not mad at you, but I do need to know why you're here."

    show ep04_nan_intro12
    nana "I--I'm friend of Madison. S-She told me to meet her here. We were supposed to study together, but when I arrived, no one answered the door."
    nana "I-I thought maybe she was out back, so I came to check... I-I hope that's okay..."
    mc_s "But why did you come here to the pool?"
    nana "I--I couldn't find her anywhere. I saw you lying there, and I thought you might be hurt or something. I-I was worried..."
    mc_s "I see..."

    show ep04_nan_intro13
    mc_s "I'm not sure Madison will be back anytime soon. You can wait here if you want, but I don't know how much help I'll be. I'm not feeling well."
    nana "W-What? But-- Oh no..."
    mc_s "Like I said, I'm not sure when she'll be back. You're welcome to wait here, but I'm going to take a nap."

    show ep04_nan_intro14
    nana "P-Please, don't leave me alone. I'm sorry if I'm causing you any trouble, but I--I can't go home like this. I-I don't know what to do..."
    nana "I--I mean... Well... I mean..."
    nana "..."
    mc_s "Alright, alright, I'll stay here."

    show ep04_nan_intro15 at ken_burns_left_to_right
    mc_s "Can you at least tell me why you're so desperate to see Madison?"
    nana "Uh... well... Uh... She's my best friend. I've known her for a while, and she promised to meet me today, but I haven't heard from her."
    nana "I-I was worried something might have happened..."
    mc_s "Can you just text her?"

    show ep04_nan_intro16
    nana "I forgot my phone... I-I'm so silly sometimes..."
    mc_s "..."
    nana "Um... yeah. I know, I'm  a bit clumsy. That's why Madison always tells me I need someone to look after me."
    nana "But--but I don't think it's a big deal, I can manage on my own. M-Most of the time, at least..."
    mc_s "Hmmm..."

    show ep04_nan_intro17 at focus_shift, subtle_zoom_out
    mc_t "Holy fuck! She has nice tits!"
    mc_t "She's not even wearing a bra. It seems like she's allergic to underwear or something. Not that I'm complaining."

    show ep04_nan_intro18 at ken_burns_bottom_to_top
    nana "I--I'm getting a little cold now. S-Sorry for the trouble..."
    mc_s "Yeah, that's because you're all wet."
    mc_t " Look at them nipples... those titties! Fuck, I can't stop looking at them!"
    mc_t "Yeah, so fucking perky! It's like they're begging to be touched."
    nana "Huh? W-Why are you staring at me like that? D-Did I do something wrong?"
    show ep04_nan_intro19
    nana "Is there something wrong with my clothes? O-Oh no, did I rip something?"
    mc_s "Ahhh... no, it's nothing."

    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_eeeh_female, "sfx", 4, False, 0, 0)

    show ep04_nan_intro20 with hpunch
    $ stopAudio(channel="music", subchannel=1, fadeout=1)
    nana "Um... i-is it because I don't have a bra on? I-I'm so embarrassed..."
    mc_s "I..."
    nana "Y-You're looking at my chest, aren't you? P-Please don't think badly of me..."
    mc_s "Well..."
    nana "I--I'm sorry, it's just that... well..."
    nana "Oh... my god! What did I do? What if you think I'm a slut or something? I-I promise I'm not like that!"
    mc_s "No, no, no! It's not like that!"
    nana "But I mean, it's weird that I'm not wearing a bra, right? That's what Madison always tells me... and my [mo_r_low]... T-They say it's not proper..."
    mc_s "Well... I mean... maybe a little, but it's fine."
    nana "Oh... oh my god, I'm so sorry! I didn't mean to embarrass you. I-I'm such a bother..."
    mc_s "It's not that, I don't mind. It's just... you know..."

    show ep04_nan_intro21 at ken_burns_bottom_to_top
    nana "But if you're not looking at me like that because I'm not wearing a bra, then... then... You think I'm fat, don't you?"
    nana "O-Oh no, I knew I should have gone on that diet..."
    mc_s "Ehhh--"
    nana "I-- I'm trying to be more like Madison, and I thought not wearing a bra would help me look slimmer... but maybe it doesn't. I-I'm so confused..."
    nana "A few days ago, Madison said I looked fat because I had my sweater on, so I took it off."
    nana "I was kinda cold, but she told me not to wear it anymore, and I listened. Then I asked her if I looked slimmer now without it, and she said..."
    nana "W-Well, she wasn't very nice about it..."
    mc_t "That doesn't explain being pantyless..."

    hide ep04_nan_intro21 with normalfade
    mc_s "Don't worry about it."
    mc_s "Although I must say, the view isn't half bad."
    nana "Huh? W-What do you mean?"
    nana "Ahh! D-Don't stare at me like that! I-I feel so exposed..."
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.8)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)

    show ep04_nan_intro22 with vpunch
    nana "P-Please don't look! I-I'm so embarrassed..."
    mc_s "Relax, I'm just messing with you. It's not a big deal."
    mc_s "Look, you're pretty wet, why don't you dry yourself off with one of my towels? It's no big deal."
    nana "Uhm... sure... T-Thank you for being so kind..."
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 2, True, 0, 0)

    show ep04_nan_intro23
    nana "Huh? W-Why are you getting so close? I-I'm not used to this..."
    mc_s "You said you name is Nanami, right?"
    nana "Umm... Yes... T-That's right..."
    mc_s "Alright. I'm [mc_name]. I'm Madison's [br_full_r_low]."
    nana "N-Nice to meet you, [mc_name]. I-I'm sorry for the trouble I've caused..."
    nana "I'm sorry I didn't ask your name sooner, I'm not good at talking to people... I-I get nervous easily..."
    mc_s "That's alright. I'm not a big talker either."

    show ep04_nan_intro24 at focus_shift, subtle_zoom_out
    mc_t "God... so close... She's so cute."
    nana "W-What? What is it? D-Did I say something wrong?"
    mc_s "..."
    mc_s "Nothing... I'll just be right back. Wait here."

    show ep04_nan_intro25 with vpunch
    nana "Ehh... uhm... o-okay... P-Please don't leave me for too long..."
    mc_s "I'll bring you a towel so you can dry yourself off."
    nana "Umm... okay... Th-Thank you. Y-You're very kind..."
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_hallwalkmale, "sfx", 7, False, 0, 1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAudio(channel="music", subchannel=2, fadeout=1)
    scene eigengrau with slowfade
    pause 2
    $ stopAudio(channel="sfx", subchannel=7, fadeout=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_intro26 with circlewipe
    nana "Oh! Uhm... th-thank you. I-I'm sorry for causing so much trouble..."
    mc_s "How do you feel now?"
    nana "M-Much better... thank you. Y-You're very kind..."
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.8)
    $ playAudio(sfx_bodyfall, "sfx", 8, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.8)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)

    show ep04_nan_intro27 at subtle_zoom_in with vpunch
    nana "M-Maybe my glasses fell here... I really need them. I-I can't see very well without them..."
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4)
    $ playAudio(sfx_water_walk, "sfx", 1, False, 0, 0)

    mc_s "No luck, huh? Don't worry, they'll probably turn up eventually."
    nana "Oh no! I hope they're not broken... I-I'd be lost without them..."
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 3, True, 0, 0)

    show ep04_nan_intro28 with normalfade
    mc_s "Are you okay?"
    nana "It's just... I'm still wet, I don't know how long it'll take for me to dry off. I don't want to stay like this... I-I feel so embarrassed..."
    mc_s "Ahh, well if that's all you're worried about then maybe we can do something about that."
    nana "Eh? W-What do you mean? I-I hope it's not too much trouble..."
    mc_s "Maybe a change of clothes?"

    show ep04_nan_intro29
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_laughnana2, "sfx", 2, False, 0, 0)
    nana "Oh! Uhm... i-if it's not too much trouble, then yes please. I-I'd be very grateful..."
    mc_s "It's not a problem at all. But... let me think for a moment."
    mc_t "Look at her body, those curves... Fuck, she can't fit into Madison's clothes. Those tits are too big... Amber's clothes probably wouldn't fit her either."

    show ep04_nan_intro30
    nana "I-Is something wrong? D-Did I say something inappropriate?"
    mc_s "What? Oh, nothing's wrong... I just don't know if any of our clothes will fit you."
    nana "Awww... Madison was right... my body's all fat. I-I knew I should have gone on that diet..."
    mc_s "Of course not!! It's just... uhh... maybe your size is different from any of my [si_full_r_low]s or my [dau_r_low]."

    show ep04_nan_intro31 at ken_burns_right_to_left
    nana "Oh... well. M-Maybe I can stay at the pool then? I mean I won't feel cold if I'm in the water... I-I don't want to be a bother..."
    mc_s "Are you sure? I don't know if that's such a good idea..."

    show ep04_nan_intro32
    nana "Or... uhm... M-Maybe I can just take off my clothes and stay in the towel... while they dry? I-I hope that's not too inappropriate..."
    mc_t "Damn! So innocent and so fucking naughty at the same time. And she doesn't even know it!"
    nana "A-All my wet clothes should dry up pretty quickly, right? I can put them in the dryer when they're not wet anymore..."
    nana "Y-You have a dryer, right? I-I'm sorry for asking so many questions..."
    mc_s "Yeah... yeah we do."
    mc_s "Uhm... Can you wait here for a moment? I gotta think of something..."
    nana "S-Sure... I'll be waiting. P-Please don't leave me for too long..."
    $ stopAudio(channel="music", subchannel=3, fadeout=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 9, False, 0, 0)

    show ep04_nan_intro33 at subtle_zoom_in with slowfade
    mc_t "I can't have this girl in a bikini running around the house...  or even worse, naked in a towel! Fuck, that would be too much."
    mc_t "I mean, I'm not complaining or anything... but this is my [si_full_r_low]'s friend... and probably Isabella's friend too."
    mc_t "What would they think? And then what if Nanami meets Amber? They don't know her like I do... she'll probably think I'm doing something bad..."
    mc_t "Sh-shit! Why am I feeling nervous about this?"

    $ stopAudio(channel="sfx", subchannel=9, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_eeh_nanami, "sfx", 1, False, 0, 0)

    show ep04_nan_intro34 at ken_burns_bottom_to_top with hpunch
    nana "Ehh... Uhm... I-I hope I'm not being a nuisance..."
    mc_s "What is it?"
    nana "I-I think I made a decision... Um, if it's okay... M-Maybe I could go to Madison's room to get a swimsuit?"
    nana "That way I won't be in wet clothes, and I can wait for her by the pool... I-Is that alright?"
    show ep04_nan_intro35
    nana "W-Will that be okay? I-I don't want to overstep any boundaries..."
    mc_s "..."
    nana "B-But I guess that's fine... If you want me to go home, I will... I don't want to cause any trouble... I-I'm sorry for being such a bother..."
    mc_s "Why would I tell you to go home?"
    nana "Um... I... I'm not sure... You're probably busy and I'm bothering you, I know that. So, um... I'll be going to Madison's room now. I-I hope that's alright..."
    $ show_walkthrough("ep04_nana_m1")
    menu:
        mc_t "Should I stop her? I don't know if it's a good idea."
        "Don't stop her":
            hide screen walkthrough_screen

            mc_t "Nah, I won't stop her. I guess as she said, her clothes can dry while she can get warm in the water."
            mc_t "Besides, maybe she will give me a show... Like when she fell in the pool. Fuck, that was hot."
            mc_s "Okay, go ahead."

            $ ep04_nanpath = 1
            $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
            $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
            jump ep04_nanpool


        "Stop her":
            hide screen walkthrough_screen

            mc_t "Isabella isn't at home, but maybe she can get here any moment. What would she think?"
            mc_t "I can't say to her... Hey I was at the pool with this girl and her tits looked great in a bikini, so yeah!"
            mc_t "That's just wrong... But if she stays in a towel then it's okay."
            mc_s "Okay, wait."
            nana "Huh? W-What's wrong? D-Did I do something wrong?"
            mc_s "Look... I don't think it's a good idea."

            $ ep04_nanpath = 2
            jump ep04_nantowel




label ep04_nanpool:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_bikini01 at dramatic_realization with circlewipe
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(nanami_chill_theme, "music", 1, True, 5, 0)
    nana "I--Is it ok? I-I hope it's not too inappropriate..."
    mc_t "Holy fuck! Is this real?"
    mc_t "Oh my god! How did she put that on? It's too fucking small! It's like it's painted on her body."
    mc_t "Did she realize how skimpy that is? Does she have any idea what she looks like?"
    mc_t "Madison and Isabella would freak out if they saw her like this... Hell, I'm freaking out right now."
    nana "So... umm... What do you think? I-Is it too much?"
    $ show_walkthrough("ep04_nana_m2")
    menu:
        mc_t "Should I reply honestly? What should I say? Fuck... I'm getting an erection just looking at her. This girl is something else... Keep it together, man."
        "Be honest and check her out":
            hide screen walkthrough_screen

            mc_s "So... How exactly did you put that on? It looks... challenging."
            nana "Eh?! Uhh... W-What do you mean? Did I do it wrong?"
            show ep04_nan_bikini02 at subtle_zoom_in, ken_burns_bottom_to_top
            mc_s "I mean, you look amazing in it, but it's barely covering anything."
            nana "Umm... But Madison said she looked great in this... And I think I look great in it too... D-Don't I?"
            mc_s "You're joking, right? You look incredible, but it's very..."
            nana "I mean... Umm... Madison showed me how to tie it so that it won't come off..."
            nana "So... umm... Is there something wrong with it? Did I misunderstand?"
            mc_s "I-- No, there's nothing wrong with it... The only wrong thing would be I'll keep staring at you all day long if you don't change. Not that I'd mind..."
            nana "Y-You think I look that good? R-Really?"
            mc_s "Yes... You do. You're stunning, actually."

            show ep04_nan_bikini03 at subtle_zoom_in, ken_burns_top_to_bottom
            nana "Ahhh! Don't look down there! I-I'm so embarrassed!"
            nana "I--I know I'm not pretty like Madison or Isabella... I'm fat and clumsy, and I don't wear any fancy clothes... I'm so sorry... I must look ridiculous..."
            mc_s "I didn't say that. You're way prettier than them. I mean it. You're in a league of your own."
            mc_s "You do realize how tiny that thing is, right? It leaves very little to the imagination."
            nana "Eh?! Uhm... W-What do you mean?!"
            mc_s "Don't tell me you don't know."
            nana "I-I don't understand... W-What's wrong with it?"
            mc_s "See this part here? It's supposed to cover more."
            nana "Umm... Ehh... Oh no, did I put it on wrong?"
            mc_s "It's not supposed to show. But don't worry, you look amazing."
        "Don't":
            hide screen walkthrough_screen

            mc_s "Um, sure it's fine. It's very... eye-catching."
            pass
    show ep04_nan_bikini04 with vpunch
    nana "So you're saying... That--That it doesn't look good? I've made a fool of myself, haven't I?"
    mc_s "No... I think it looks great... on you. But I mean, if you walk around like this, I won't be able to take my eyes off of you. You're absolutely breathtaking."
    nana "You're not just saying that to make me feel better, right? You really mean it?"
    mc_s "Of course not! You're beautiful and sexy, and any guy would love to see you like this! You're a knockout, Nanami."

    show ep04_nan_bikini05 with normalfade
    nana "You think I'm sexy? Me? For real? I-I've never been called sexy before..."
    mc_s "Absolutely! You're the definition of sexy."
    nana "Thank you... I-I really appreciate it. That means a lot..."
    show ep04_nan_bikini06
    nana "I'm so sorry for being so weird... I don't have much experience with boys... I'm kinda nervous right now. My heart's racing..."
    mc_s "You don't have to be nervous around me. I promise, okay?"
    nana "It's just Madison told me... Uh... I shouldn't show my body too much in front of boys, that they might think bad things about me."
    nana "She says they're all perverts and that I should stay away from them. But you're different, right?"
    mc_s "Oh... She did? That does sound like something Madison would say. Well I assure you, I don't think bad things about you."
    mc_s "In fact, I think you look amazing. You're absolutely beautiful, inside and out."
    mc_t "Who am I kidding? I'd love to fuck her right here and now!"

    show ep04_nan_bikini07
    nana "I-Is it okay if I tell you something? Something personal?"
    $ stopAudio(channel="music", subchannel=1, fadeout=2.5)

    mc_s "Sure. Anything you want. I'm all ears."
    nana "Alright... Here goes..."
    nana "It's just... sometimes I feel like I don't fit in with the other girls my age. It feels like they all have so much more experience than me."
    nana "You know? I'm always the last one to know anything about... Well... You know... Stuff that other girls know. I feel so out of place sometimes..."
    show ep04_nan_bikini08 at ken_burns_left_to_right with hpunch
    nana "Madison even told me my breasts are too big and that I should be embarrassed by them. She said they make me look... slutty."
    mc_t "Fucking Madison... God, she can be such a bitch sometimes."
    mc_s "Nanami, you're perfect just the way you are. Don't let anyone tell you otherwise."
    nana "No, no! It's fine! I get it now. If Madison says so then it must be true, right? She knows so much more than me..."
    show ep04_nan_bikini09 at focus_shift, subtle_zoom_in
    nana "Right?! Just look at these things! They're huge! I know they're freakishly huge! They're so embarrassing!"
    nana "I hate them so much! They make me look like a cow! I can't even wear kimonos or yukatas as Madison does!"
    nana "I tried but it's so hard to find one that fits my boobs! And even if I did, they wouldn't look good on me! They never do! I'm so jealous of Madison..."
    nana "Can you imagine what would happen if I wore them?! I would probably tear the fabric and spill out!"
    nana "Then everyone would see my udders and laugh at me! I'd die of shame!"
    mc_s "Why do you say that? You're gorgeous! They're beautiful! Everything about you is beautiful. You shouldn't be ashamed of your body."

    $ setChannelVolume(channel="music", subchannel=5, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 5, True, 0, 0)

    show ep04_nan_bikini10 with normalfade
    mc_s "Whatever Madison told you, don't listen to her. She's not a boy, so she doesn't know what they want to see."
    mc_s "And just because you don't have experience doesn't mean anything. That just means you're innocent and pure."
    mc_s "That's exactly what guys like! Your innocence is charming."
    nana "Like you? Do you like that about me?"
    mc_s "Especially me."
    nana "Mmmm... You think I'm sexy... but you also say that I'm cute... I don't understand..."
    nana "Madison is always saying that boys are attracted to only one thing, and that's my boobs. So when I'm around her friends, I don't feel cute at all."
    nana "I feel like a freak..."
    mc_s "Hey... hey! What are you talking about? Of course you're cute! You're adorable and sexy at the same time."
    nana "Really? How do you know? You're not just saying that?"
    mc_s "Let me just say this... If I could have my way, I'd spend all day staring at you..."
    nana "You would? That's so sweet..."
    mc_s "Of course! Look at you! You're fucking hot! And trust me, other guys would too. You're a knockout, Nanami."

    show ep04_nan_bikini11 at ken_burns_top_to_bottom with vpunch
    nana "But... Is it really okay if I stay here like this? I--I mean... I don't want anyone to see me like this... What if someone comes?"
    mc_s "What do you mean? There's nobody here except us. We're alone, don't worry."
    nana "I-I know... It's just... I'm full of doubts right now... And I don't know what to do. I feel so exposed..."
    mc_s "Look... If you don't feel comfortable showing off your body, then don't. Nobody can tell you what to do. But don't be afraid to show off a little bit."
    mc_s "It doesn't make you a bad person."
    nana "Umm.. maybe you could ask your other [si_full_r_low]... I know she has kind of my size..."
    mc_t "Oh yeah, Amber would be thrilled to have you wear her clothes. She'd be jumping up and down in excitement, running around the house screaming."
    mc_t "Fuck! What should I do?"
    nana "Maybe she could give me something... Like a T-shirt or something? Please... Please [mc_name]?"
    mc_s "Alright, alright. I'll see what I can do."

    $ stopAudio(channel="music", subchannel=5, fadeout=2)

    show ep04_nan_bikini12
    nana "Thank you, [mc_name]. You're so kind..."
    mc_t "I thought she wouldn't notice she and Amber are the same size, I was so wrong..."

    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms01




label ep04_amb_sms01_bik_post:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_bikini12
    hide ep04_ambersmsbg1
    mc_s "Uhm... Can you look at me for a moment?"
    nana "M-Mmm? What is it? Did I do something wrong?"
    mc_s "It's nothing, I just need to take a picture. It's for my [si_full_r_low]."

    scene eigengrau with dissolve
    show ep04_nan_bikini13 at focus_pulse, subtle_breathing with slowfade
    nana "A-A picture? Of me? Like this?"
    mc_s "Yeah, like that. But can you get up for a sec?"
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)

            show ep04_nan_bikini13 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "Alright..."

    hide photo_flash
    show ep04_nan_bikini14 at focus_pulse, subtle_breathing
    nana "Ehh?! Like this? Or... I-I'm not very good at posing..."
    mc_s "Hold on. Don't move. Stay still."
    mc_t "Damn, she looks incredible. I feel a bit guilty, but..."
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)

            show ep04_nan_bikini14 at photo_effect with flash
            show photo_flash with dissolve
            pause
    mc_t "Wow... I should definitely save that one."

    show ep04_nan_bikini15
    hide photo_flash
    nana "So... Um... Did you get it? W-Was it okay?"
    mc_s "Yeah, I think so... I'll text Amber."
    nana "O-Oh, I see... I hope it's alright..."
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms02




label ep04_nanpool2:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    hide ep04_ambersmsbg2
    if ep03_amberstrike:
        mc_t "Damn it! Amber's giving me the silent treatment."
        mc_t "That woman can hold a grudge like no other."
    elif ep03_amberangry: 
        mc_t "Hmmmm... Amber's still pissed at me. No help from her, I guess."
    elif ep04_amberno: 
        mc_t "Ah, just as I expected."
        mc_t "At least she's cool with me grabbing those clothes from her room."
    else:
        mc_t "Fuck... Now I'm all worked up."
        mc_t "She's so fucking hot it should be illegal..."

    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_eeh_nanami, "sfx", 1, False, 0, 0)

    show ep04_nan_bikini16 with vpunch
    nana "S-So... uhm-- D-Did she say yes?"
    if not ep03_amberangry or ep03_amberstrike:
        mc_t "I know I should tell her yes, but damn! That bikini's barely there. I'd be an idiot to waste this chance..."
    nana "If she didn't, I-I understand... It's a bit of a weird request... M-Maybe I shouldn't have asked..."
    mc_s "Sorry, Nanami... Amber said no."

    show ep04_nan_bikini18
    nana "I see... I-I guess it was too much to ask..."
    mc_s "Don't worry! I'm sure I can find something for you to wear. But if you ask me, you look great just the way you are."
    nana "Really?"
    mc_s "Absolutely! Look at yourself... You're gorgeous! Anyone who says otherwise is either blind or lying."

    $ setChannelVolume(channel="music", subchannel=4, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 4, True, 0, 0)

    show ep04_nan_bikini17
    nana "W-Wow! Thank you! I don't know what to say... I-I'm not used to compliments..."
    mc_t "Holy shit, those are huge! What I wouldn't give to see them pop out of that bikini... Fuck me!"
    nana "You're such a good person, [mc_name]."
    mc_s "I try... So... How about we hit the water?"

    show ep04_nan_bikini19 at ken_burns_left_to_right
    nana "You mean, swim?"
    mc_s "Sure. That's what you wanted to do, right?"
    nana "Together?"
    mc_s "No, no, no. I'll sit this one out... I'll just hang out here and keep an eye on you. That okay?"
    nana "You don't want to swim with me?"
    mc_s "It's not that. It's just someone has to play lifeguard, don't you think?"

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
    $ playAudio(sfx_pool_moving, "sfx", 1, False, 0, 0)

    show ep04_nan_bikini20 at subtle_zoom_in, ken_burns_bottom_to_top with normalfade
    nana "Then... can I ask you a favor? It might sound a bit odd..."
    mc_s "Anything. What's on your mind?"
    nana "Well... While I'm at the pool, can I call you [da_r]? I know it's weird, but..."
    mc_s "[da_r]? Where'd that come from? That's... unexpected."
    nana "It's just... I had this dream since I was little about having a [da_r] watching me while I learn to swim... I never had that chance growing up."
    mc_t "Whoa, didn't see that coming... This girl is more innocent than I thought... So damn adorable!"
    nana "I know it's silly... but I always wanted that. My [da_full_r_low] left my [mo_r] when I was very young, and I never knew him."
    nana "So uhm... I never had a real [da_r_low] to watch me swim or teach me how to ride a bike. So, uhm... I know we just met today but, can you be my [da_r_low]? For a day?"
    mc_t "This is weird as hell, but I kinda love it. I know I hated the idea with Aoi before, but this girl is different... This feels so natural..."
    mc_t "And yet, there's something so wrong about it. Am I being a creep, taking advantage of her innocence?"
    nana "If this makes you uncomfortable then it's fine..."
    $ show_walkthrough("ep04_nana_m3")
    menu:
        mc_t "What should I say?"
        "Accept her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)
            $ ep04_nanadad = True

            mc_s "I would be honored."
            nana "Really?! You'll be my [da_r]? Really?!"
            mc_s "Sure. Why not?"
        "Deny her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", -2)
            $ check_levels("nanami", "trust", -2)

            mc_s "I'm sorry, Nanami. But... I can't do that."
            nana "Oh... Okay... It's fine. I understand."
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_pool_moving, "sfx", 2, False, 0, 0)

    show ep04_nan_bikini21 at ken_burns_right_to_left with slowfade
    if ep04_nanadad:
        mc_t "Damn... I'm really glad I could help her with that."
    else:
        mc_t "Shit... I kinda regret I couldn't help her with that."
    mc_t "It's fucking sad she never had a real [da_full_r_low] figure growing up. Can't blame her for wanting one."
    mc_t "That being said, it's a fucking miracle that bikini hasn't burst yet! Those tits are massive! Fuck!"

    show ep04_nan_bikini22 at ken_burns_corner_to_corner2 with circlewipe
    if ep04_nanadad:
        nana "Hey [da_r]! Is this good?"
    else:
        nana "[mc_name]! Is this good?"
    mc_s "Look at you go! You're doing great."
    nana "It's so warm here! This feels great!"
    nana "I was right, I'm not cold at all!"
    mc_s "Looks like you're having a blast."

    show ep04_nan_bikini23 at ken_burns_bottom_to_top
    if ep04_nanadad:
        nana "Watch [daddy_r]! [daddy_r], look at me! Look!"
    else:
        nana "Watch [mc_name]! [mc_name], look at me! Look!"
    nana "It feels so good in here! I love it!"
    mc_s "I see you're a natural."
    nana "I know! Madison always tells me I'm so clumsy and that I can't do anything right, but I know how to swim! See?"
    mc_t "Well... She is clumsy, but that's part of her charm. She's so damn cute..."

    show ep04_nan_bikini24 at ken_burns_top_to_bottom with circlewipe
    if ep04_nanadad:
        nana "Hey [da_r], come in the pool with me! Please?"
    else:
        nana "Hey [mc_name], come in the pool with me! Please?"
    mc_t "Should I? If Isabella or anyone shows up I'm fucked... But I don't want to let this moment slip away either..."
    mc_t "I mean, I'm already in hot water if they see Nanami in that tiny bikini... So what's the difference?"
    mc_t "Gotta think straight here, can't do anything stupid... But fuck! She looks so fucking hot!"
    if ep04_nanadad:
        nana "[daddy_r], come on! Come in with me!"
    else:
        nana "[mc_name], come on! Come in with me!"
    mc_s "No, you stay there."
    nana "Why not?"
    mc_s "Because I said so."

    $ stopAudio(channel="music", subchannel=4, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.6)
    $ playAudio(sfx_water_walk, "sfx", 8, False, 0, 0)

    show ep04_nan_bikini25 with hpunch
    if ep04_nanadad:
        nana "[da_r]? Did I do something wrong?"
    else:
        nana "[mc_name]? Did I do something wrong?"
    mc_s "What? No, it's just... You want the truth? I'm afraid if I get in there with you, everyone can misunderstand what's going on. You know what I mean?"
    nana "Uhm... I don't think so."
    mc_s "Well... You're here at my house, and you're wearing a bikini. And I'm alone with you. It might look shady, like I'm taking advantage of you or something."
    nana "You would never do that!"
    mc_s "I know, but people might not think so. So, I'd rather stay here."
    nana "Oh... Okay."
    $ stopAudio(channel="sfx", subchannel=8, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_pool_outof, "sfx", 2, False, 0, 0)

    show ep04_nan_bikini26 with normalfade
    nana "Well if I can't swim with you, can I at least sit next to you?"
    mc_t "I'm not complaining, but this girl is so damn clingy! I mean, I don't mind it, but still..."
    nana "Please? I promise I'll be good."
    mc_s "Alright, come on over."

    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=5)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_bikini27 at focus_shift, ken_burns_right_to_left with dissolve
    if ep04_nanadad:
        nana "Hey [da_r], can you scratch my back for me? Please?"
    else:
        nana "Hey [mc_name], can you scratch my back for me? Please?"
    mc_t "Should I? There's nothing wrong with that, right? I mean, she just wants a back scratch..."
    nana "Please? It itches so bad!"
    mc_s "Uhm... Okay."
    if ep04_nanadad:
        nana "Thanks, [da_r]! You're the best!"
    else:
        nana "Thanks, [mc_name]! You're the best!"
    mc_s "No problem."
    if ep04_nanadad:
        nana "Hey [da_r], can I ask you something?"
    else:
        nana "Hey [mc_name], can I ask you something?"
    show ep04_nan_bikini28 at subtle_zoom_out, subtle_breathing
    mc_s "Sure, what is it?"
    nana "You're Isabella's [da_full_r_low], right?"
    mc_s "Yes."
    nana "I don't wanna be nosy or anything, but... Where's her [mo_r]? I mean... Is she around?"
    mc_s "No. She's not."
    nana "Did you two get divorced?"
    mc_s "No."
    nana "Then what happened? Did she die or something?"
    mc_s "Not really. I don't know ..."
    nana "You don't know? What do you mean you don't know?"
    mc_s "Look, I'd rather not talk about it, okay? It's personal."
    nana "Right... I-I'm sorry for asking..."
    mc_s "..."

    show ep04_nan_bikini29 with vpunch
    nana "I'm sorry! I didn't want to make you angry!"
    mc_s "It's fine, don't worry about it. I just don't like talking about it, okay?"
    nana "Okay..."
    show ep04_nan_bikini30 with normalfade
    nana "I feel terrible... I didn't mean to upset you."
    mc_s "Forget it. It's fine."
    nana "It's just that... I asked about her because I was thinking if you were engaged or something like that... I mean, I know it's not my business, but..."
    mc_s "What? No, no, no... I'm not engaged. I'm not seeing anyone right now."
    nana "You mean you're single?"
    mc_s "Yeah."
    nana "Why??!!"
    mc_s "Why what?"

    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 1, True, 0, 0)

    show ep04_nan_bikini31
    nana "Well... You're a good person, and you're handsome too... Why don't you have a girlfriend?"
    mc_t "I wonder how far I can push this with her... She seems so naive and innocent... I bet she'd do anything I ask..."
    mc_t "But I can't take advantage of her... Even if she's a bit of a pushover, she's still a nice girl... I shouldn't be thinking about her like that."
    if ep04_nanadad:
        nana "[da_r]?"
    else:
        nana "[mc_name]?"
    mc_s "Sorry, I was just thinking."
    nana "About what?"
    mc_s "Well... About you."

    show ep04_nan_bikini32 with hpunch
    nana "Me?! What about me?!"
    mc_s "You want to know why I don't have a girlfriend?"
    nana "Uhm... Yeah?"
    mc_s "Because I'm waiting for the right one. When she comes along, I'll know."

    show ep04_nan_bikini33 at ken_burns_right_to_left
    nana "Really? That's so romantic! I wish someone would say that about me..."
    mc_s "Huh?"
    nana "I'm sorry... It's just... I've never heard a guy say something like that before... It's really beautiful."
    mc_s "Oh, I didn't realize it sounded romantic... I guess I never thought about it that way."
    nana "No, it's fine! I love it! It's so sweet!"
    nana "It's just... I've always wanted to meet someone who would say something like that to me..."
    nana "Someone who would say I'm beautiful and that I'm special..."
    nana "Someone who cares about me and wants to be with me."
    mc_t "What the fuck? Did I just accidentally make her fall for me?"

    show ep04_nan_bikini34 at ken_burns_top_to_bottom
    nana "But... I know that's not gonna happen. Not for me."
    mc_s "Hey! Why do you say that?"
    nana "Because... Because..."
    nana "Don't try to make me feel better, okay? I know what I am... I'm fat and ugly, and I don't have any friends..."
    nana "I'm too shy to talk to people, and I'm clumsy and awkward..."
    nana "I know I'm not pretty or special, so I've accepted it. But it still hurts sometimes."
    mc_s "You know what? If I was your age, I'd totally ask you out."

    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_surprisenana, "sfx", 1, False, 0, 0)

    show ep04_nan_bikini35 with vpunch
    nana "W-What did you say?"
    mc_s "I'd totally date you... If I was your age, of course."
    nana "You... You would?"
    mc_s "Yeah..."

    show ep04_nan_bikini36 with hpunch
    nana "Wow... I never thought someone would say that to me..."
    mc_s "Well, it's true."
    nana "I... I think you're amazing... I mean... You're so nice and sweet, and you're handsome too... I wish there were more guys like you."
    mc_s "Guess I'm one of a kind."
    nana "I don't know what to say... I'm so happy right now! I really am!"
    mc_s "Oh... we forgot about your clothes."
    nana "My clothes? Oh yeah... My clothes..."
    mc_s "I'll put them on the dryer. Wait here."
    nana "Okay... I'll wait here..."
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 3, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_bikini37 at ken_burns_top_to_bottom with circlewipe
    $ stopAudio(channel="sfx", subchannel=3, fadeout=1)
    nana "Alright, your clothes are drying off."
    if ep04_nanadad:
        nana "Thank you so much, [da_r]!"
        mc_t "Oh, right. I forgot she's calling me that."
    else:
        nana "Thank you so much, [mc_name]!"
    nana "I found my glasses too! Look!"
    nana "Yeah, I noticed."
    mc_t "Look at them... They're so big! So young and firm... So juicy... Fuck!"

    show ep04_nan_bikini38 at impact_shake
    nana "I guess... they're not that bad, huh?"
    mc_s "Huh? What?"
    nana "You're staring at my boobs again..."
    mc_s "No, I'm not."
    nana "Yes, you are. I can tell."
    show ep04_nan_bikini39 at ken_burns_left_to_right with hpunch
    nana "It's okay... I don't mind it. I like it when you look at me..."
    mc_s "Really?"
    nana "Yeah... but I don't know what's so special about them... They're just breasts... I mean, they're big and they're always in the way, but that's all they are..."
    mc_s "Are you kidding me? They're fucking amazing! They're perfect!"

    show ep04_nan_bikini40 at dramatic_focus with vpunch
    nana "Perfect? These things? They're freakishly huge!"
    mc_t "Damn, she looks so hot right now! I can't take it anymore!"
    nana "What do you see in them anyway?"
    mc_s "Everything!"
    nana "Oh!"
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 2, True, 0, 0)

    show ep04_nan_bikini41 at ken_burns_left_to_right with hpunch
    nana "So if I do this... You'll like it, right?"
    mc_s "Yeah... It's really fucking hot."
    nana "And this... Is this sexy?"
    mc_s "Very sexy."

    show ep04_nan_bikini42 at ken_burns_bottom_to_top with hpunch
    nana "What if I do this?"
    nana "Is it sexy? Do you like it?"
    mc_s "Yeah... I like it a lot."
    mc_t "Fuck! This girl is so fucking hot! I can't take it anymore!"

    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)

    show ep04_nan_bikini43 at subtle_breathing with vpunch
    if ep04_nanadad:
        nana "[da_r]? What's wrong? You're sweating..."
    else:
        nana "[mc_name]? What's wrong? You're sweating..."
    mc_s "It's nothing... I just..."
    nana "It doesn't look like nothing... Your face is all red."
    mc_s "I'm fine, I'm fine. It's just that..."
    nana "What? Tell me!"
    mc_s "I think you should go put your clothes back on."

    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
    $ playAudio(sfx_onknees, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.6)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)

    show ep04_nan_bikini44 with vpunch
    nana "Why? Did I do something wrong?"
    nana "You're not mad at me, are you?"
    mc_s "No, no, you didn't do anything wrong! I just..."
    mc_t "Fuck! I better get out of here before I do something I'll regret! I can't control myself anymore!"
    if ep04_nanadad:
        nana "[da_r], please tell me! I'll do anything you want! Just tell me what's wrong!"
    else:
        nana "[mc_name], please tell me! I'll do anything you want! Just tell me what's wrong!"
    mc_s "Do anything?"
    nana "Anything you want."
    mc_t "This girl is really testing my limits... I don't know how much more I can take..."

    $ setChannelVolume(channel="sfx", subchannel=7, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 7, False, 0, 0)

    show ep04_nan_bikini45 at subtle_zoom_out
    mc_s "Forget it. I better check on your clothes."
    if ep04_nanadad:
        nana "Wait! [da_r]! What did I do?!"
    else:
        nana "Wait! [mc_name]! What did I do?!"
    nana "I thought you liked it when I showed you my boobs!"
    mc_t "Ahh! Don't say it like that! You're making it worse! I need to get out of here before I lose it."

    $ ep04_ach_nanabikini = True
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_madcaught




label ep04_nantowel:
    show ep04_nan_clothes01
    nana "W-Why not? Is... is there something wrong with me?"
    mc_s "Come on, have you seen Madison? She's built like a stick. You can't wear her bikini. It'd be like trying to cover a watermelon with a handkerchief."
    nana "W-What do you mean? Are you saying I'm... big?"
    mc_s "Look, Madison's thin as a rail, no curves to speak of. You're the opposite. You've got... assets she doesn't."

    show ep04_nan_clothes02 at ken_burns_bottom_to_top
    nana "I... Oh God, you mean... I'm fat?"
    mc_s "Hell no! I'm talking about your chest! Your body is smoking hot, it's just that you've got way bigger breasts than Madison."
    mc_s "Her bikini wouldn't cover a fraction of you!"
    nana "Oh... I-I see. So my... my boobs are too big?"
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.1)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)

    show ep04_nan_clothes03
    mc_s "We need to find another solution... but damn if I know what."
    nana "Well... I guess I could just stay in the towel... you know... while my clothes dry off. Unless... unless that's too much?"
    mc_t "Christ, she'd be naked under that towel... Is that a good idea? Then again, a bikini might be even worse. Or better, depending on how you look at it."
    mc_s "Alright... if that's what you're comfortable with."
    nana "Okay... um, could you... could you turn around?"
    show ep04_nan_clothes04
    nana "I... I need to take off my clothes."
    mc_s "Oh, right. Sure thing. I can wait for you at the pool, just tell me when you're ready."
    nana "T-Thank you... I'll be quick, I promise."
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.2, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(nanami_chill_theme, "music", 1, True, 5, 0)

    show ep04_nan_clothes05 at subtle_breathing, ken_burns_left_to_right with circlewipe
    mc_t "Fuck me, she's already stripping... I shouldn't be watching this, but I can't look away."
    mc_t "I'm doing the right thing, right? I mean... she'd be bursting out of Madison's tiny bikini."

    show ep04_nan_clothes06 at subtle_breathing, ken_burns_right_to_left with circlewipe
    mc_t "What I don't get is why she isn't wearing any underwear... not even a bra. Does she always go commando?"
    mc_t "It's probably for the best that I can't see her tits from here... right? Who am I kidding, I'd kill for a peek."

    show ep04_nan_clothes07 at focus_shift, dramatic_realization
    mc_t "Can't help but imagine her huge tits hanging free, bouncing with every move..."
    mc_t "God, what a sight that would be... I'm getting hard just thinking about it."
    pause 1.5
    show ep04_nan_clothes08 at subtle_breathing, ken_burns_left_to_right with normalfade
    mc_t "This is wrong, I'm not some horny teenager... I shouldn't be peeping on her. But fuck, I can't tear my eyes away."

    show ep04_nan_clothes09 at focus_shift, ken_burns_top_to_bottom
    mc_t "But I can't help myself... What I wouldn't give to bury my face between that ass! It's perfect!"
    pause 1.5
    show ep04_nan_clothes10 at subtle_breathing, ken_burns_right_to_left with normalfade
    mc_t "Her body is unreal... Look at that cute little butt! I'm dying to grab a handful."

    show ep04_nan_clothes11 at focus_shift, subtle_zoom_out
    mc_t "Big boobs, tiny waist, small but firm ass, long legs... She's a walking wet dream!"
    pause 1.5
    show ep04_nan_clothes12 at subtle_breathing, ken_burns_left_to_right with normalfade
    mc_t "Show's almost over... Damn, I wish I could record this."

    show ep04_nan_clothes13 at focus_shift, ken_burns_bottom_to_top
    mc_t "Shit, did she just look this way? I hope she didn't catch me staring!"
    mc_t "So long, sweet view... Goodbye to that ass, goodbye pretty pussy, and farewell, glorious tits. I'll be replaying this in my head for weeks."
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_clothes14 with circlewipe
    $ stopAudio(channel="music", subchannel=1, fadeout=2)
    nana "I-I'm ready now... I think."
    mc_t "Damn, even in a towel, she's a knockout. How am I supposed to keep my hands to myself?"
    nana "Um, [mc_name]? The towel feels a bit short... Are you sure this is okay? I mean... look at my... uhm.. you know... It barely covers anything!"
    nana "Isn't it kind of... really revealing?"
    mc_s "It's fine, trust me. The sun will dry you off in no time. Besides, you look great."
    nana "R-Really? I guess it doesn't matter then. As long as you're okay with it..."
    mc_s "I'll dry your clothes for you, and then we can do something else while we wait."
    nana "U-hu..."
    mc_s "I'll be right back, try not to get into any trouble while I'm gone."
    nana "Okay! I'll wait here. Please hurry..."
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_hallwalkmale, "sfx", 2, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_clothes15 at ken_burns_bottom_to_top with circlewipe
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1)

    mc_s "Hey, look at that! You have your glasses back! That's good news."
    nana "Yeah, I found them at the bottom of the pool. "
    mc_s "At the bottom? How did you get them?"
    nana "Well... I... Uhm... I had to go down there... without my clothes... so I didn't get your towel wet."
    mc_t "Holy shit!! Really? Did I miss that? Fuck, I would've paid to see that!"
    nana "It was kinda cold... that's why I'm glad the sun is warming me up. It feels nice on my skin..."
    show ep04_nan_clothes17
    nana "I'm really sorry I put you through this... You must think I'm such a bother."
    mc_s "That's okay, don't worry about it. You look cute. More than cute, actually."

    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 2, True, 0, 0)
    nana "What? ........ Are you... joking?"
    mc_s "Dead serious. I mean it. You're beautiful. Stunning, even."
    nana "No way... you're just saying that to make me feel better. Aren't you?"
    mc_s "Why don't you believe me? Can't you see how gorgeous you are?"

    show ep04_nan_clothes19
    nana "I don't know... maybe because I'm fat? Everyone always says I am..."
    mc_s "You're not fat! You have a killer body!"
    nana "Me? But... but I'm not thin like Madison. I'm all... curvy and stuff."
    mc_s "And? You think that's the only thing that matters? Trust me, curves are good."
    nana "Well, isn't it? She's tall, beautiful, and thin. And she always gets attention from guys. That's why she's so popular at school. I never get any attention..."
    mc_s "And yet, you're still prettier than her. Way prettier, if you ask me."
    nana "But she's a model... and I'm just... well... me. Just plain old Nanami."
    mc_s "I think you're more beautiful than her. And I've seen my fair share of beautiful women."

    show ep04_nan_clothes20
    nana "Yeah, right. There's no way that's true."
    mc_s "You could be a model too, you know? A damn good one."
    nana "What? Really? You... you really think so?"
    mc_s "Of course. You have a great body, Nanami. The kind most girls would kill for."
    nana "But... Madison told me I couldn't become a model because my boobs are too big... She said they'd look weird in photos."
    mc_s "That's ridiculous! She's just jealous of you. Trust me, your boobs are perfect."

    show ep04_nan_clothes16 at ken_burns_bottom_to_top
    nana "Wow... I never thought about it like that before. You really think she might be jealous?"
    mc_s "Why do you care so much about what she says? She's not exactly an expert."
    nana "I don't know... I guess I always feel like she knows more than me. About everything."
    mc_t "Is she really this oblivious about her body or is she doing it on purpose? Either way, it's driving me crazy."
    nana "She knows so much more about boys and sex. And... well, she's so popular. I've never had a boyfriend..."
    nana "I'm always the one who gets dumped. Or worse, never asked out in the first place."
    mc_s "What? Are you kidding me? You're so cute, Nanami. Any guy would be lucky to have you."
    nana "Really? You're not just saying that?"
    mc_s "Yes, you only need to have confidence in yourself. Believe me, you've got plenty to be confident about."
    nana "Confidence? But how? I wouldn't even know where to start..."
    mc_s "Well, for starters you could act a little more sexy. You know, own your body."

    show ep04_nan_clothes18 at subtle_zoom_out with vpunch
    nana "Sexy? Me? You mean like this? Is this sexy? Am I doing it right?"
    mc_t "Jesus Christ, I can't believe she's showing me her pussy! Does she remember the towel isn't long enough? This girl is going to be the death of me."
    nana "Is it working? Do I look... sexy?"
    mc_s "Uhm... yeah... sure... You look incredible."
    mc_t "I can't stop looking at her pussy! It's right there, perfect and pink..."

    $ stopAudio(channel="music", subchannel=2, fadeout=2)

    show ep04_nan_clothes21 with vpunch
    nana "Oh! I'm sorry! I forgot about the towel! Oh God, you saw everything, didn't you?"
    mc_s "No, no! It's okay! It's okay. Really, don't worry about it."
    nana "But you were staring at me... You saw... down there..."
    mc_s "Yeah, I couldn't help myself... You're just too beautiful."
    nana "Oh... uhm. I don't think I should stay like this... It's too revealing, isn't it?"
    mc_t "Fuck! I shouldn't have said that! Now she's feeling uncomfortable! Way to go, idiot."
    nana "Can I wear anything else? Something less... exposing?"
    mc_s "What do you mean?"

    show ep04_nan_clothes22 at ken_burns_right_to_left with normalfade
    nana "I-- I mean... I don't know, but... anything else than a towel... Can you ask your [si_full_r_low] Amber for something to wear?"
    nana "I don't want to trouble you again. But I feel so... naked."
    mc_s "Amber? You want me to ask Amber for something to wear? Are you sure about that?"
    nana "Yeah, I mean... she has the same size as me, right? At least... in the chest area..."
    mc_t "Damn... I thought she wouldn't notice Amber's body is similar to hers."
    nana "Please [mc_name]... I just want to cover myself... I feel so exposed like this."
    show ep04_nan_clothes23 with normalfade
    mc_s "I guess it's okay... but... I'm not sure she'll be happy about it. Amber can be... territorial about her stuff."
    nana "Oh! Thank you! Thank you so much! You're a lifesaver, really!"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms01




label ep04_amb_sms01_tow_post:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_clothes23
    hide ep04_ambersmsbg1
    mc_s "Hey, Nanami. Can you look at me for a moment?"
    nana "M-Mmm? What is it? Did I... Did I do something wrong?"
    mc_s "It's nothing bad, I just need to take a picture. It's for my [si_full_r_low]. She wants to see how it fits."

    scene eigengrau with dissolve
    show ep04_nan_clothes24 at focus_pulse, subtle_breathing with slowfade
    nana "A-A picture? Of me? Like this? But I'm... I'm barely dressed!"
    mc_s "Yeah, like that. But can you get up for a sec? I need to get the full view."
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)

            show ep04_nan_clothes24 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "Alright..."

    hide photo_flash
    show ep04_nan_clothes25 at focus_pulse, subtle_breathing
    nana "Ehh?! Like this? Or... I-I'm not very good at posing... Should I... should I do something with my hands?"
    mc_s "Hold on. Don't move. Stay still. You're perfect just like that."
    mc_t "Holy shit, she looks incredible. I feel a bit guilty, but... damn, those tits are unreal."
    menu:
        "Take picture":
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
            $ playAudio(sfx_camerashot, "sfx", 1, False, 0, 0)

            show ep04_nan_clothes25 at photo_effect with flash
            show photo_flash with dissolve
            pause
    mc_t "Wow... I should definitely save that one. For purely innocent reasons, of course."

    show ep04_nan_clothes26 with normalfade
    nana "So... Um... Did you get it? W-Was it okay? I hope I didn't look too... exposed."
    mc_s "Yeah, I think so... I'll text Amber. You looked great, by the way."
    nana "O-Oh, I see... I hope it's alright... Your [si_full_r_low] won't think I look... slutty, will she?"
    mc_s "Trust me, you look amazing. Maybe a little too amazing..."
    nana "Oh! I... I see. Thank you, I think? You're making me blush..."
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=1)
    jump ep04_amb_sms02




label ep04_nantowel2:
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    hide ep04_ambersmsbg2
    if ep03_amberstrike:
        mc_t "Damn it! Amber's giving me the silent treatment."
        mc_t "That woman can hold a grudge like no other."
    elif ep03_amberangry: 
        mc_t "Hmmmm... Amber's still pissed at me. No help from her, I guess."
    elif ep04_amberno: 
        mc_t "Ah, just as I expected."
        mc_t "At least she's cool with me grabbing those clothes from her room."
    else:
        mc_t "Fuck... Now I'm all worked up. Amber sure knows how to push my buttons."
        mc_t "She's so fucking hot it should be illegal..."

    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_eeh_nanami, "sfx", 4, False, 0, 0)

    show ep04_nan_clothes27 with vpunch
    nana "So... uhm... hi? Have you finished talking to your [si_full_r_low]?"
    mc_s "Oh, yeah!"
    if not ep03_amberstrike or ep03_amberangry or ep04_amberno:
        mc_t "Shit, I totally forgot about Nanami! Focus, man."
    nana "Did you ask her? About the clothes, I mean..."
    if ep03_amberstrike or ep03_amberangry:
        mc_s "Of course! I told her everything, but she's being... difficult."
        mc_s "But don't worry, I'll... borrow something from her wardrobe that fits you."
    else:
        mc_s "Of course! I told her everything. And she's cool with it."

    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_towelshake, "sfx", 2, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_laughnana, "sfx", 4, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
    $ playAudio(nanami_theme, "music", 3, True, 0, 0)

    show ep04_nan_clothes28 at ken_burns_corner_to_corner2 with hpunch
    nana "Really? That's great! Thank you so much! You're so kind to me!"
    mc_t "Holy fucking shit, she's flashing her tits! Keep it together, man!"
    nana "I'm getting clothes! I'm getting clothes! I'm getting clothes! No more towel!"
    mc_s "Uhm... o-okay... That's... quite the celebration."
    nana "Huh?!! Oh no..."
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.6)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 3, False, 0, 0)

    show ep04_nan_clothes29 with vpunch
    nana "Oh my god! I'm sorry! I'm so sorry! I got too excited and... oh no..."
    mc_s "Hey, no harm done. These things happen."
    nana "Oh my god, I can't believe I did that! I'm so sorry, [mc_name]! You must think I'm such an idiot!"
    nana "You had to see these fat cow udders jumping around! I'm so embarrassed!"
    mc_s "Whoa, hey! Don't talk about yourself like that! Your body is beautiful, Nanami."
    nana "You don't have to say that... I know I'm not..."
    $ stopAudio(channel="music", subchannel=3, fadeout=2)
    scene eigengrau with slowfade
    pause 1
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2)
    $ playAudio(nanami_secure_theme, "music", 4, True, 0, 0)

    show ep04_nan_clothes30 at ken_burns_bottom_to_top
    nana "You're being so kind to me. Why? No one's ever..."
    mc_t "Now I feel like a creep for enjoying the view. But damn, those curves..."
    nana "I've caused you so much trouble. Maybe I should just stick with the towel?"
    mc_s "Not at all. I'll grab those clothes now. Try to keep your enthusiasm in check, yeah?"

    $ setChannelVolume(channel="sfx", subchannel=5, volume=1)
    $ playAudio(sfx_hallwalkmale, "sfx", 5, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2, fade_duration=1.5)

    show ep04_nan_clothes31 with circlewipe
    $ stopAudio(channel="sfx", subchannel=5, fadeout=1)

    mc_s "Here we go. Amber's finest. Or at least, what I could snag quickly."
    nana "Thank you! You're like the [da_r_low] I never had."
    mc_s "Well, I am a [da_r_low]. Comes with the territory, I suppose."
    nana "Um... would it be weird if I... If I called you [daddy_r]?"
    nana "It's okay if that's too strange. I know it's an odd request..."
    $ show_walkthrough("ep04_nana_m3")
    menu:
        mc_t "This is... unexpected. How do I handle this?"
        "Accept her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)
            $ ep04_nanadad = True

            mc_s "I would be honored."
            nana "Really?! This is... I don't know what to say!"
            mc_s "Let's give it a shot. No harm in trying, right?"
        "Deny her request":
            hide screen walkthrough_screen
            $ rm.update("nanami", "trust", -2)
            $ check_levels("nanami", "trust", -2)

            mc_s "I appreciate the thought, Nanami, but that's not appropriate."
            nana "Of course, I understand. I shouldn't have asked. How embarrassing..."
    if ep04_nanadad:
        nana "I'll go change now... [daddy_r]. That feels so nice to say!"
    else:
        nana "I'll go change now, [mc_name]. Thanks again for everything."
    nana "Back in a flash! No peeking, okay?"
    if ep04_nanadad:
        mc_t "What have I gotten myself into? If Isabella finds out..."

    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAudio(channel="music", subchannel=4, fadeout=2)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=5, volume=0.2)
    $ playAudio(nanami_chill_theme, "music", 5, True, 4, 0)

    show ep04_nan_clothes32 at subtle_breathing, ken_burns_left_to_right with circlewipe
    mc_t "And here I go again, being a total creep. I'm definitely going to hell for this."

    show ep04_nan_clothes33 at focus_shift, ken_burns_bottom_to_top
    mc_t "Those breasts are a work of art. I could stare all day."
    pause 1.5
    show ep04_nan_clothes34 at subtle_breathing, ken_burns_right_to_left with normalfade
    mc_t "Her body is incredible. How can she not see it?"

    show ep04_nan_clothes35 at focus_shift, ken_burns_top_to_bottom
    mc_t "That pussy... I can't believe I got so lucky earlier."
    mc_t "A virgin too... That's... wow. Down, boy."
    mc_t "Shit, she's done. Act natural, you perv."
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAudio(channel="music", subchannel=5, fadeout=2)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    show ep04_nan_clothes36 with circlewipe
    if ep04_nanadad:
        nana "Um... [daddy_r]? How do I look in this?"
    else:
        nana "[mc_name]? Is this okay?"
    mc_s "All done? That was... efficient."
    nana "Does it fit alright? It's not too revealing, is it?"
    mc_s "You look stunning, Nanami. Seriously, you're a knockout."
    nana "You mean it? You're not just being nice?"
    mc_s "Absolutely. You're gorgeous."

    show ep04_nan_clothes37 with hpunch
    nana "Even from this angle? It doesn't make me look... big?"
    mc_s "You look amazing from every angle. Trust me on this."
    nana "Wow! I don't know what to say..."
    $ setChannelVolume(channel="music", subchannel=7, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 7, True, 0, 0)

    show ep04_nan_clothes38 at subtle_breathing
    nana "No one's ever said these things to me before. It feels... surreal."
    mc_s "That's hard to believe. How could anyone not see how beautiful you are?"
    if ep04_nanadad:
        nana "I wish I heard it more often, [daddy_r]. It makes me feel... special."
    else:
        nana "I wish I heard it more often, [mc_name]. It's nice to feel... noticed."
    mc_s "Well, I'm happy to remind you anytime. Because it's the truth, Nanami."
    nana "That's so sweet! But you don't have to go out of your way..."
    mc_s "Hey, what's wrong? You seem suddenly down."
    nana "It's just... I'm not used to people being this kind to me."
    mc_s "Well this is the first day of your life with someone who will always tell you how beautiful you are."
    if ep04_nanadad:
        nana "Thank you, [daddy_r]! You're amazing!"
    else:
        nana "Thank you, [mc_name]! You've been so wonderful..."
    show ep04_nan_clothes39 with vpunch
    nana "Oh! Um... I didn't mean to..."
    mc_s "What happened? Everything okay?"
    nana "I-- I... Oh no..."
    $ ep04_ach_nanagoth = True
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_madcaught




label ep04_madcaught:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(madison_bad_theme, "music", 1, True, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_impact, "sfx", 1, False, 0, 0)

    show ep04_nanmad01 at action_sequence, subtle_zoom_out
    mad "Well, well, well. What do we have here? A little private party I wasn't invited to?"
    nana "M-Madison! I... Um... This isn't what it looks like!"
    mad "Zip it, sweetheart. I'm talking to my dear [br_full_r_low]. Care to explain, [mc_name]?"
    nana "Please, it was my fault! I needed clothes and-"
    mc_s "We were having a perfectly fine time before you barged in, Madison."
    mad "Oh, I bet you were. Seems I've stumbled upon quite the... intimate gathering."
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)

    show ep04_nanmad02 at ken_burns_left_to_right with hpunch
    nana "I'm so sorry, Madison. We didn't mean to-"
    mad "What did you do to her, [mc_name]? She looks like a deer in headlights."
    mc_s "I didn't do a damn thing to her. Why are you jumping to conclusions?"
    mad "Because she looks terrified. What kind of sick game are you playing?"
    mc_s "The only one scaring her is you, with your little power trip."
    nana "No, no! It's not like that! It's my fault, really. I'm the one who-"
    mad "Did I say you could speak? Zip it, Nanami."
    nana "O-Okay..."
    mad "I said shut it. Your voice is grating on my nerves."
    mc_s "Hey! Don't talk to her like that!"
    mad "Why do you care? She's not your property, big [br_full_r_low]."
    $ show_walkthrough("ep04_nanamad_1")
    menu:
        "Defend Nanami":
            hide screen walkthrough_screen
            $ ep04_madpath += 1
            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)

            mc_s "I don't give a damn. You don't get to treat her like dirt."

            jump ep04_madcaught_defend


        "Make peace with Madison":
            hide screen walkthrough_screen
            $ ep04_madpath += 2
            $ rm.update("madison", "trust", 5)
            $ check_levels("madison", "trust", 5)
            jump ep04_madcaught_agree




label ep04_madcaught_defend:
    show ep04_nanmad03 at ken_burns_bottom_to_top with hpunch
    mad "Fine... But I'm not going anywhere."
    mc_s "Isn't she supposed to be your best friend? Some friend you are."
    mad "So what? That doesn't give her a free pass to fool around with my [br_full_r_low]."
    nana "M-Maybe I should just go... I don't want to cause any more trouble."
    mc_s "No, Nanami. You're not leaving because of her tantrum. Madison's the one who needs to back off."
    mad "Excuse me? You're in MY house with MY friend, and you have the audacity to tell ME to leave?"
    mc_s "Damn right I do. Nanami and I were having a perfectly fine time before you barged in."
    nana "I'm so sorry, [mc_name]. I never meant for any of this to happen..."
    mc_s "It's not your fault, Nanami. It's all on Madison and her drama queen act."

    show ep04_nanmad04 at ken_burns_left_to_right
    mad "Oh, that's rich. Need I remind you that the only reason she's even here is because of me? You wouldn't even know her name if it wasn't for me."
    mc_s "Yeah, you brought her here, and now you're treating her like garbage. Real classy, [sis_r_low]."
    mad "Don't you dare talk to me like that, you sanctimonious prick."
    mc_s "I'll talk to you however I damn well please."
    mad "You don't get to boss me around. Who the fuck do you think you are?"
    mc_s "Your [br_full_r_low], remember? And I'm not about to let you treat Nanami like shit."
    mad "Fuck off! Nanami is MY best friend, not yours. So butt out!"
    nana "Please, stop fighting... This is all my fault..."
    mad "Nanami, just shut your mouth and stay out of this."
    nana "I'm sorry, Madison..."
    show ep04_nanmad05 at subtle_breathing with vpunch
    mad "You think you're hot shit because you're a man? You think you can do whatever you want? Well, newsflash: you can't. You're nothing but a pathetic loser who couldn't even keep his own [fm_r_low] together."
    mc_s "What the fuck did you just say?"
    mad "You heard me. You're a pathetic piece of shit who couldn't even take care of his own [dau_r_low]. Some [da_full_r_low] you are."
    mc_s "Don't you dare bring Isabella into this!"

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_hallwalkfemale, "sfx", 1, False, 0, 0)

    show ep04_nanmad06 at subtle_zoom_in with normalfade
    mad "I don't have time for this bullshit. You're not worth it."
    mc_s "Fuck you too, Madison."
    mad "Come on, Nanami. We're out of here."
    nana "O-Okay..."
    mad "And you, stay the fuck away from my friend! She doesn't need your sleazy ass in her life."
    $ stopAudio(channel="music", subchannel=1, fadeout=2)

    show ep04_nanmad07 with normalfade
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    nana "I'm so sorry about Madison... She didn't mean those awful things she said."
    mc_s "It's okay, Nanami. You don't need to apologize for her toxic behavior."
    nana "I... I want to thank you for standing up for me. No one's ever done that before."
    mc_s "Don't mention it. I'd do it again in a heartbeat."
    if ep04_nanadad:
        nana "You're so brave, [daddy_r]! I wish I could be more like you..."
    else:
        nana "You're so brave, [mc_name]! I wish I had your courage..."
    nana "I... I should probably go now. Madison's waiting, and I don't want to make her angrier..."
    mc_s "Alright... Take care, Nanami. Don't let her push you around."

    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_tablehit, "sfx", 2, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.8)
    $ playAudio(sfx_sofa_move, "sfx", 3, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2)
    $ playAudio(nanami_clumsy_theme, "music", 4, True, 0, 0)

    show ep04_nanmad08 with hpunch
    nana "Ouch! Oh no..."
    mc_s "Nanami!"

    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1)
    scene eigengrau with hpunch
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.4, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.2, fade_duration=1.5)

    show ep04_nanmad09 at dramatic_focus with normalfade
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_bodyfall, "sfx", 4, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.7)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False, 0, 0)
    nana "Ow... My ankle... It hurts..."
    mc_s "Easy there. Are you okay?"
    nana "Y-Yes, I think so... Just give me a moment."
    mc_s "You sure are clumsy, aren't you?"

    show ep04_nanmad10 at focus_shift, subtle_breathing, subtle_zoom_out with normalfade
    nana "Yeah... I guess I am. Always tripping over my own feet..."
    mc_t "Damn... She looks incredibly sexy like this. Those..."
    nana "Huh? Why are you looking at me like that?"
    mc_s "Oh, uh... It's nothing. Just making sure you're not hurt."
    mc_t "Her ass feels amazing on my lap... Focus, man!"
    nana "What are you staring at? Is there something on my face?"
    mc_s "No, it's... uh... your..."
    nana "My what? Oh! Oh no!"
    show ep04_nanmad11 at subtle_breathing, impact_shake
    nana "I'm so sorry! I didn't mean to... to flash you like that!"
    mc_s "It's fine, really. We'll blame it on the fall, okay?"
    if ep04_nanadad:
        nana "Uhm... [da_r]?"
    else:
        nana "Uhm... [mc_name]?"
    mc_s "Yeah?"
    nana "Could you... could you help me up, please?"
    mc_s "Of course, here, let me..."
    mc_t "Shit... She's going to feel my hard-on..."
    nana "T-Thank you..."
    $ stopAudio(channel="music", subchannel=4, fadeout=2)

    show ep04_nanmad12 with vpunch
    nana "W-What was that? Did I touch something?"
    mc_s "Huh? What do you mean?"
    nana "That... that thing I felt. It was... hard."
    mc_s "Oh... That's my... Well..."
    nana "Oh! Oh my god, I'm so sorry! I didn't mean to touch your... your..."
    mc_s "It's okay, Nanami. It's a natural reaction."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 1, True, 0, 0)

    show ep04_nanmad13
    nana "You're... You're like that... because of me?"
    mc_s "Yeah... Can't really help it."
    nana "Really? I... I've never... made anyone feel like that before."
    mc_s "Well, there's a first time for everything."
    nana "I can't believe it... Someone actually finds me... attractive?"
    mc_s "Very much so. But let's keep this between us, okay?"
    nana "Of course! I'd never tell anyone. It's our secret."
    if ep04_nanadad:
        nana "Ehh... uhm... [daddy_r]?..."
    else:
        nana "Ehh... uhm... [mc_name]?..."
    mc_s "What is it, Nanami?"
    nana "Can I... Can I tell you a secret too?"
    mc_s "Sure, go ahead."
    nana "Could you... come a little closer?"
    mc_s "Okay..."

    $ setChannelVolume(channel="sfx", subchannel=7, volume=1)
    $ playAudio(sfx_kiss_nana, "sfx", 7, False, 0, 0)

    show ep04_nanmad14 at subtle_breathing with vpunch
    nana "Mmmmm..."
    mc_t "Holy shit... Her lips are so soft..."
    nana "Mmm... That felt... amazing..."
    $ setChannelVolume(channel="sfx", subchannel=8, volume=0.8)
    $ playAudio(sfx_footsteps_female_semirun, "sfx", 8, False, 0, 0)

    show ep04_nanmad15 at ken_burns_bottom_to_top with hpunch
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_laughnana, "sfx", 9, False, 0, 0)

    mc_s "Wait, Nanami! We shouldn't..."
    nana "You're my first kiss! I... I've never felt like this before..."
    if ep04_nanadad:
        nana "I'll see you later, [daddy_r]! Thank you for everything!"
    else:
        nana "I'll see you later, [mc_name]! Thank you for being so kind to me!"
    $ ep04_nanakiss = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_nanarun




label ep04_madcaught_agree:
    mc_s "Alright, let's talk this out like adults."
    mad "Talk about what, dear [br_full_r_low]? Your pervy tendencies?"
    mc_s "Cut the crap, Madison. What's really bothering you?"
    mad "Oh, where do I start..."
    show ep04_nanmad16
    if ep04_nanadad:
        nana "It's all my fault. I fell into the pool and [da_r]-- I mean... [mc_name]..."
    else:
        nana "Please, it's my fault. I fell into the pool and [mc_name]..."
    mad "Zip it, you airhead! Can't you see the adults are talking?"
    nana "I'm sorry... I'll be quiet..."
    show ep04_nanmad17
    mc_t "Why is Nanami apologizing? This isn't fair. Madison's being a total bitch."
    mad "Well, for starters, I don't appreciate the way you're eye-fucking Nanami."
    mc_t "Shit, her top's barely containing those perky tits. Focus, man."
    mc_s "What are you talking about?"
    mad "Don't play dumb. Your eyes are practically undressing her. It's revolting."
    mc_t "Damn, she noticed? I thought I was being subtle."
    mad "Let's be real. Who wouldn't want to bend her over?"
    nana "Madison! It's not like that at all!"
    show ep04_nanmad18 at ken_burns_top_to_bottom with vpunch
    mad "Relax, I get it. He's a man, after all. A slave to his base instincts."
    mc_t "What the fuck is she playing at? Trying to make me look like a creep? I'm not a pervert... well I am but I'm not THAT pervert."
    mad "It's only natural for men to think with their dicks. You can't help it, can you, [br_full_r_low]?"
    mc_t "Christ, now her tits are practically spilling out. What's her game?"
    mad "See? Even now, you're ogling my chest. Such a perv."
    mc_s "That's not true. I wasn't looking at your tits."
    mad "Please, I'm not an idiot. I know they're out. I know you're drooling over my petite rack."
    nana "Stop it, Madison! This is making me uncomfortable..."
    mad "Oh, sweetie. You need to understand that men are slaves to their desires. Even my dear [br_full_r_low]."
    mc_s "That's enough of your bullshit!"

    show ep04_nanmad19
    nana "Please, Madison. This isn't funny anymore. Can we just stop?"
    mad "So you're telling me he didn't try anything? Nothing happened at all?"
    nana "Nothing happened... I swear."
    mad "Really? You expect me to believe that?"
    nana "It's the truth..."
    mad "God, you're so naive. I bet he's already pictured you naked."
    mc_t "Fuck me, I hate that she's right. Those images are burned into my brain."
    mc_s "I'm not looking for a fight, Madison. You're way off base here."

    show ep04_nanmad20
    mad "It doesn't matter. I know exactly what kind of man you are. No use hiding it."
    mc_s "Oh yeah? Enlighten me. What kind of man am I?"
    mad "I'll spell it out for you... but not with little miss innocent here."
    mc_s "What the hell are you on about?"
    mad "Look at her. So pure, so naive. You don't want to taint that, do you?"
    mc_s "You're out of your mind."
    mad "Want me to spill the beans in front of her? Because I will."
    nana "What are you talking about? What don't I know?"
    mad "Nothing, sweetie. Your virgin ears don't need to hear this."
    $ stopAudio(channel="music", subchannel=1, fadeout=2)

    show ep04_nanmad21 at ken_burns_right_to_left
    nana "I'm not a child, Madison. Just tell me what's going on!"
    mad "Trust me, you're better off not knowing. Some things can't be unheard."
    nana "Why are you being like this? Just tell me!"
    mad "Forget it. We're leaving. Now."
    nana "Where are we going?"
    mad "My room. You need clothes that aren't soaked in my [br_full_r_low]'s drool."
    nana "Are you sure about this?"
    if ep04_nanpath == 1:
        mad "Dead sure. I don't want you parading around in my bikini anymore."
    elif ep04_nanpath == 2:
        mad "Absolutely. I don't want you wearing that bitch's hand-me-downs."
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
    $ playAudio(sfx_footsteps_heelstile, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=7, volume=0.2)
    $ playAudio(nanami_love_theme, "music", 7, True, 0, 0)

    show ep04_nanmad22
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0, fade_duration=6)
    if ep04_nanadad:
        nana "Goodbye, [daddy_r]. I'll see you later..."
        mad "What the fuck did you just call him?"
        nana "N-Nothing..."
    else:
        nana "Goodbye, [mc_name]. Thank you for everything..."
    mc_s "Take care, Nanami."
    nana "...and thanks again for being so kind."
    mad "What are you thanking him for? He didn't do jack shit."
    nana "I-I know, but..."
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_bodygrab, "sfx", 3, False, 0, 0)

    show ep04_nanmad23 with hpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_surprisenana, "sfx", 2, False, 0, 0)
    mad "Enough chitchat. Move your ass!"
    nana "Okay, okay... I'm coming."
    mad "Later, perv. Try not to jerk off thinking about us."
    mc_s "..."
    mc_t "Poor Nanami... stuck dealing with Madison's psycho ass 24/7."
    if ep03_madtalk:
        $ ep04_ach_madison = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_nanarun




label ep04_nanarun:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.3)
    $ playAudio(sfx_earlymor, "amb", 3, True, 1, 0)   
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_footsteps_heelstile, "sfx", 1, False, 0, 0)

    show ep04_madnan01 at ken_burns_right_to_left
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0, fade_duration=8)
    mad "This is my fault. I should've known you'd fall for his act."
    nana "Madison, wait up! Your legs are longer than mine..."
    mad "What did I expect from you? You're as naive as a newborn kitten."
    nana "I-I'm sorry... Please don't be mad at me. I didn't mean to upset you."
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=1)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)

    show ep04_madnan02 at ken_burns_left_to_right with hpunch
    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_fearanana, "sfx", 9, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(madison_nan_theme, "music", 2, True, 0, 0)
    nana "Ouch!"
    mad "Spill it, Nanami. Now!"
    nana "W-What? What do you want me to say?"
    if ep04_nanpath == 1:
        mad "Why are you prancing around in that skimpy bikini? Why were you alone with my [br_full_r_low]? I bet he was practically drooling over you."
    elif ep04_nanpath == 2:
        mad "Why are you wearing those slutty clothes? What were you doing with my perv of a [br_full_r_low]? Did he make you put those on?"
    nana "Please, Madison. Don't be angry. I can explain everything..."
    mad "Then explain! I'm waiting! And it better be good."
    nana "W-Well, he was by the pool... I came in because you told me to... and I saw him on the floor, then I tripped and... I-I don't know what happened next."
    mad "That's not an explanation, that's a fucking fairytale."
    nana "But I've told you everything! Why don't you believe me?"
    mad "You're lying! I can smell the bullshit from here! Tell me the truth! Did he touch you?"
    nana "No! I swear on my life! Nothing like that happened."
    show ep04_madnan03 at subtle_zoom_in, ken_burns_bottom_to_top
    if ep04_nanpath == 1:
        mad "Alright... let's break this down. Why were you wearing that barely-there bikini? Did he ask you to put it on?"
    elif ep04_nanpath == 2:
        mad "Fine... let's take it slow. Why were you wearing those trashy clothes? Was this his idea of dressing you up?"
    nana "I didn't have anything else... I fell in the pool and was soaked to the bone. He was just trying to help..."
    mad "And he didn't try to cop a feel? Not even a little grope? Come on, Nanami, I know my [br_full_r_low]."
    nana "No! Nothing happened! We were just talking when you showed up. He was... kind."
    mad "He didn't try to slide his hand up your thigh? Or 'accidentally' brush against your tits?"
    nana "Of course not! Why are you asking such embarrassing things?"
    mad "Because he's my [br_full_r_low] and he'd fuck anything with a pulse."
    nana "He would never! He was nothing but kind to me."
    mad "Oh, honey... Men are only kind because they want to bury themselves in that tight little hole you have between your legs."
    show ep04_madnan04 at ken_burns_right_to_left with hpunch
    nana "Stop it! He didn't do anything wrong! You're being cruel! Why can't you believe that someone might genuinely be nice?"
    mad "You're defending him? Are you out of your mind? After everything I've done for you?"
    nana "I'm not defending him! I'm just saying he's not the monster you're making him out to be. Why do you hate him so much?"
    mad "Listen, you airhead. You're too naive, too trusting. Men aren't like you think. They're not like us. They're walking hard-ons. Don't ever forget that."
    nana "But... I... He seemed so genuine..."
    mad "You always see the best in people, even when they're plotting to bend you over. But you can't trust men. They'll use you and toss you aside like a used condom."
    nana "I don't know... He was so nice... He's your [br_full_r_low], after all."
    show ep04_madnan05
    mad "No... no... no... Get it through your thick skull. He's not nice. He's a pervert, a sexual predator."
    nana "How can you say that? You don't even know him that well!"
    mad "Nanami, please. I'm trying to protect your virgin ass. I don't want to see you get hurt... and if you trust him... I'll be beyond disappointed."
    nana "..."
    mad "So, do you trust me or not?"
    nana "I... I do..."
    show ep04_madnan06 at dramatic_focus
    mad "Really? You trust me over him? Over some guy you just met?"
    nana "Yes... of course I trust you. You're my best friend. You've protected me all these years."
    mad "Even though I can be a royal bitch sometimes? Even when I push you to do things?"
    nana "Maddie... you're not a bitch. You're just... intense. You do it because you care, right?"
    mad "You know I'm not actually evil, right? Everything I do is to protect you."
    nana "I know that. You're just looking out for me. Like you always have."
    mad "Then promise me something... Like we did when we were kids."
    nana "What is it?"
    show ep04_madnan07 at subtle_zoom_out
    mad "Promise me you'll never trust my [br_full_r_low] again... and if he tries to get in your pants, you'll tell me immediately. No secrets between us, remember?"
    nana "But... what if he really is just being nice?"
    mad "Nanami... do you love me? After everything we've been through together?"
    nana "I do! You're my best friend in the whole world. You know that."
    mad "Then promise me. Now. Show me I can trust you."
    nana "I... I promise..."
    mad "Good girl. Now let's get you out of those clothes."
    nana "O-Okay..."
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep04_isajelously




label ep04_isajelously:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.8)
    $ playAudio(sfx_midnightpast, "amb", 4, True, 1, 0)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.8)
    $ playAudio(sfx_hairdryeron, "sfx", 1, True, 1, 0)

    show ep04_isajel01 at ken_burns_left_to_right with circlewipe
    mc_t "Why is she in my room? And in that... barely-there outfit?"
    isa "I hope you don't mind, [da_r]. I borrowed your hair dryer. It's so... hot in here, isn't it?"
    if ep03_amberleft or ep03_amberstrike:
        mc_s "It's not even mine."
        isa "Oopsie! Silly me, it's mine. I'm just so... flustered today. Wonder why?"
        mc_t "Huh? That's an odd response."
    else:
        mc_s "It's not mine. Amber said it was yours."
        isa "[aun_r] Amber stopped by? My, my... what other secrets are you keeping, [daddy_r]?"
        mc_t "Damn, I shouldn't have mentioned that."

    $ stopAudio(channel="sfx", subchannel=1, fadeout=2)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_hairdryeroff, "sfx", 2, False, 0, 0)

    show ep04_isajel02 with normalfade
    isa "Hey, [da_r], did you see that kawaii pic I sent you? You know, the one at the photoshoot?"
    if sawpic_ep03_sms1:
        mc_s "Yeah, I saw it."
        isa "So you know I was with [aun_r] Madison and [gra_r] at the photoshoot, right?"
        mc_s "Yeah, I got that."
    else:
        mc_s "Nope, must've missed it."
        isa "Oh, so you don't know about my fabulous day with [aun_r] Madison and [gra_r] at the photoshoot?"
        mc_s "No, I didn't."
        isa "Well, now you know. Better late than never, I guess."
    isa "Connect the dots for me, [daddy_r]. Or do I need to... draw you a picture?"
    mc_s "What are you getting at, Isabella?"
    isa "I heard what happened at the pool, [da_r]. Every. Little. Detail. It was quite... enlightening."
    mc_s "What are you talking about?"
    isa "Nanami, [da_r]. I'm talking about Nanami and Madison. What exactly did you do?"
    mc_t "This is not good. She's got me cornered."
    isa "Well? I'm waiting for an explanation, [da_r]."
    $ show_walkthrough("ep04_isa_m1")
    menu:
        mc_t "Truth or lie? What if she's bluffing? I need to gauge how much she knows."
        "Tell her the truth":
            hide screen walkthrough_screen
            $ ep04_isatruth = True
            $ rm.update("isabella", "trust", 5)
            $ check_levels("isabella", "trust", 5)

            mc_s "Sorry, honey, I didn't know you were here. Well, your friend--"
        "Try to investigate":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", -2)
            $ check_levels("isabella", "trust", -2)

            mc_s "And why are you so interested?"

    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(isabella_anger_theme, "music", 2, True, 0, 0)

    show ep04_isajel03 at dramatic_realization
    if ep04_isatruth:
        isa "She's not my friend. Let's not confuse the players in this little... game."
        mc_s "Oh... I thought you two were close."
        isa "She's Madison's little pet, not mine. Different circles..."
        mc_s "What do you mean?"
        isa "You know, [da_r]... That Nanami girl... She's always been... how do I put this... not quite what she seems?"
        mc_s "Not quite how?"
    else:
        isa "B-because... Well, I... Because I'm just worried that maybe... because..."
        isa "Well, the only thing I saw was [aun_r] Madison doing her best banshee impression but..."
        isa "Mmmm"
        isa "Want to know a fun fact about that girl?"
        mc_s "You mean your friend Nanami?"

    show ep04_isajel04 at dramatic_focus
    if ep04_isatruth:
        isa "You know that shy, innocent act she puts on? It's quite the... performance, [daddy_r]."
        mc_s "What act?"
        isa "The whole 'oh, I'm so pure' routine? It's all smoke and mirrors. She's not the angel you think she is."
        mc_s "Uhm..."
        mc_t "Is Isabella really talking about Nanami like this? And why is she talking like a grown woman?"
        isa "You're not seeing the full picture, [daddy_r]. I've known her since we were little... girls. She's not as pure as the driven snow."
        mc_s "Honey, I don't think--"
        isa "She always does this. Plays the innocent damsel, but trust me, she's got... hidden depths. I bet she's been planning this little... encounter for a while."
        mc_s "I... I don't know what to say."
    else:
        isa "First off, she's not my friend, [daddy_r]. Let's get our... relationships straight."
        mc_s "Why the hostility?"
        isa "I don't like her. She's Madison's... plaything, not mine."
        mc_s "Uhmmm... well..."
        isa "It's all an act, [daddy_r]. She looks shy and sweet, but she's playing a very... adult game."
        isa "She uses that innocent facade like a weapon. I'm giving you the inside scoop here."
        mc_s "Are we talking about the same Nanami? This sounds like a different person entirely."
        mc_t "This is a side of Isabella I've never seen before..."

    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_walk_barefoot, "sfx", 4, False, 0, 0)

    show ep04_isajel05 with normalfade
    isa "Don't worry, [daddy_r]. I'm used to people falling for her... charms. Even big, strong men like you."
    mc_s "Used to it?"
    isa "How everyone buys into her little... performance. It's quite... entertaining to watch."
    mc_s "Hmm..."
    isa "Nanami's not the pure little flower she pretends to be. She's more like a... Venus flytrap."
    $ stopAudio(channel="sfx", subchannel=4, fadeout=1)
    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.4)
    $ playAudio(sfx_chair_rolling, "sfx", 5, False, 0, 0)

    show ep04_isajel06 with normalfade
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.7)
    $ playAudio(sfx_officechair_creak, "sfx", 6, False, 0, 0)

    mc_s "What are you up to now?"
    isa "Oh nothing, just looking for something..."
    mc_s "Be careful, you're gonna fall."
    isa "You have experience with falling, don't you?"
    mc_t "Huh? What does she know?"
    isa "Where is it? Where is it? Oh, the things I do for you, [da_r]..."
    $ show_walkthrough("ep04_isa_m2")
    menu:
        "Help her":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", 2)
            $ check_levels("isabella", "trust", 2)

            mc_s "Baby, what are you looking for? I can help you if you tell me."
        "Leave her alone":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", -2)
            $ check_levels("isabella", "trust", -2)

            mc_s "Okay, baby... But please, be careful. I don't want you getting hurt."

    show ep04_isajel07 at impact_shake
    if ep04_nanadad:
        isa "Don't call me baby, I'm not your baby, I'm your ONLY [dau_r_low]. And I can do this... all by myself."
    else:
        isa "Don't call me baby, I'm not your baby, I'm your [dau_r_low]. And I can handle this... situation."
    mc_s "Alright, fine. But why are you acting so... different?"
    isa "I'm just looking for something I hid before you came back from the hospital."
    mc_s "Okay, I get it. But please be careful, I don't want you falling."

    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_officechair_sit, "sfx", 7, False, 0, 0)

    show ep04_isajel08 at ken_burns_top_to_bottom with vpunch
    isa "Why so worried, [daddy_r]? Afraid I might... expose something? Or someone?"
    mc_s "Huh? What are you talking about?"
    if not sawpic_ep03_sms1:
        isa "I mean I send you a picture and you don't even reply."
        mc_s "That's because... Well..."
        isa "Save it, [daddy_r]. If you start with 'well', you're lying. I thought we had a more... honest relationship."
        mc_t "Damn, when did she get so... sharp?"
    else:
        if ep04_nanadad:
            isa "So you have two daughters now, [daddy_r]?"
            mc_s "What?! No, of course not."
            isa "Did I mishear then? You weren't playing... [daddy_r_low] with her?"
            mc_s "Well... I mean..."
            isa "There's that 'well' again. You're lying, [daddy_r]. I thought we were... closer than that."
            mc_t "This is getting dangerous..."
        else:
            isa "You had a good time with Nanami, right? Was she... entertaining?"
            mc_s "I... Well... No! It wasn't like that."
            if ep04_nanpath == 1:
                isa "Really? You didn't enjoy her in that tiny bikini? All wet and... glistening?"
            elif ep04_nanpath == 2:
                isa "Really? You didn't like her in just a towel? So... exposed?"
            mc_s "W-well... I... I don't--"
            isa "There's that 'well' again. You're lying, [daddy_r]. I thought we could be... honest with each other."
            mc_t "When did she become so... perceptive?"

    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.4)
    $ playAudio(sfx_chair_rolling, "sfx", 5, False, 0, 0)

    show ep04_isajel09 with hpunch
    isa "Finally! I found my... treasure."
    mc_s "What did you find?"
    isa "Look, [daddy_r]. Isn't it... tempting?"
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with slowfade
    pause 1
    $ setChannelVolume(channel="music", subchannel=5, volume=0.2)
    $ playAudio(isabella_happy, "music", 5, True, 0, 0)

    show ep04_isajel10 at impact_shake
    mc_s "A lollipop?"
    isa "Mm-hmm. With bubblegum inside. Want a... taste, [daddy_r]?"
    mc_s "This is what you were looking for?"
    isa "Of course! I love savoring lollipops. It's so... satisfying."
    $ setChannelVolume(channel="sfx", subchannel=9, volume=0.8)
    $ playAudio(sfx_licklolli, "sfx", 9, False, 0, 0)

    show ep04_isajel11 at slow_reveal
    isa "See? Isn't it delicious? The way it... slides in and out?"
    mc_t "What the hell is she doing? Is this on purpose?"
    isa "What's wrong, [daddy_r]? Don't you like watching? I thought you enjoyed... sweet things."
    mc_s "Uhm... Well..."
    isa "I thought you liked innocent girls, [daddy_r]. Like Nanami. Am I not... sweet enough?"
    mc_s "Huh?"
    isa "Never mind. Perhaps I'm not your... preferred flavor."
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_bed_creaking, "sfx", 1, False, 0, 0)
    $ stopAudio(channel="music", subchannel=5, fadeout=2)

    show ep04_isajel12 at ken_burns_right_to_left with normalfade
    isa "We need to discuss something important, [daddy_r]. Something... personal."
    mc_s "Okay... but first, why are you acting like this?"
    mc_s "You're barely dressed, being unusually forward, saying strange things, and acting like a--"

    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)

    show ep04_isajel13 with vpunch
    isa "A slut, right? Is that what you want to say, [daddy_r]?"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.4)
    $ playAudio(isabella_serious, "music", 1, True, 0, 0)

    mc_s "What? No! I wasn't going to say that!"
    isa "Really? Then what were you going to say? What am I acting like?"
    mc_s "Uhm... well... I just wanted to know why you're acting like this."
    isa "I thought you like it when girls act like this. I'm doing this for you, [da_r]. Don't you... appreciate it?"
    mc_s "What gave you that idea?"
    isa "Oh, I've been observant. I saw how you looked at Nanami..."
    if ep03_madtalk or ep03_madcaught:
        isa "And with [aun_r] Madison... You seemed to enjoy her company that night."
    isa "Those tattooed women in yukatas at the hospital... with their ample... assets. They had caught your eye, didn't they?"
    isa "Oh, and that blonde woman too... She seemed very... friendly."
    isa "I've seen it all, [daddy_r]. I'm not as naive as you think."
    show ep04_isajel14
    mc_t "She's fishing for information, right? She's trying to get me to tell her what happened."
    mc_s "I don't know what you think you saw but --"
    isa "And the clothes? Well, this is how I dress when I'm alone in my room. Does it... excite you?"
    mc_s "What are you talking about? You never dress like this."
    isa "Yes I do. You just never noticed because you never lived with me. But now you can... appreciate it."
    mc_s "I... you're right. I'm sorry."

    show ep04_isajel16
    isa "Look, [da_r], I'm a grown up girl now... I'm not that little kid that you left behind."
    mc_s "Yeah, yeah, I'm noticing that."
    isa "But you don't want me to grow up, right? You want to keep me as your little girl?"
    mc_s "I... cannot have this conversation with you right now."

    $ stopAudio(channel="music", subchannel=1, fadeout=2)

    show ep04_isajel15
    mc_s ". . ."
    isa "I'm sorry [da_r], I didn't mean to... overwhelm you."
    mc_s "No, it's okay. It's fine, really."
    mc_s "I'm just fed up with all this drama. I'm tired of everyone being mad at me or blaming me for stuff I didn't even know about."
    isa "I'm not mad at you, [da_r]. I just want to... understand you better."
    mc_s "No, it's okay to be mad at me, you have every right to be mad at me. I was... I am an awful [da_full_r_low]."

    show ep04_isajel17
    isa "That's what you think? That you're... awful?"
    mc_s "Yes, and I know fucked up with you and with this [fm_r_low]... I fucked up friends, my own life, everything."
    isa "[da_r]..."
    mc_s "Look, I know I'm a piece of shit. I know I'm selfish, I know I'm an asshole, I know I'm a liar... I know all of this because I'm the one who knows me the best."
    isa "[da_r]..."
    mc_s "No, let me finish."

    show ep04_isajel19
    isa "[da_r]! Shut up! You're being ridiculous!"
    isa "Calm down, okay? You're not a piece of shit, you're not selfish, you're not an asshole, and you're not a liar."
    isa "Well maybe a little bit of everything but that's not the point right now. The point is..."
    mc_s "What's the point?"
    isa "You're doing just what you said you hate. Being all... dramatic."
    mc_s "Oh... I didn't realize..."

    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(isabella_theme, "music", 2, True, 0, 0)

    show ep04_isajel18
    isa "I know, that's why I'm here to help you."
    mc_s "Ehh... uhm... I don't know what to say... It's just everything I've been through lately... It's all so much."
    isa "It's okay, [da_r], I'm here for you."
    mc_s "Thanks, baby. So uhm... about earlier..."
    isa "Earlier?"
    mc_s "What you said about talking about something important..."

    show ep04_isajel20
    isa "Oh... that..."
    mc_s "Yes, that. I'm confused. Is about Nanami?"
    isa "Forget about her, okay? She's not important. Just try to be honest with me, please. Don't I... matter more?"
    mc_s "Sure, baby-- I mean Isabella."
    isa "It's okay, [da_r]... you can call me baby if you want to."
    mc_t "She's behaving really weird today."

    show ep04_isajel21
    isa "Don't worry, [da_r]. You're not alone in this. I'm always here for you, you know that right? I can be... whatever you need."
    mc_s "Yeah... of course."
    isa "I'm just a little bit jealous, that's all. I don't want to lose you, [da_r]."
    mc_s "To who? Nanami?"

    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

    show ep04_isajel22 at ken_burns_left_to_right with vpunch
    isa "To anyone, [da_r]. To anyone. I want to be the only one in your life."
    mc_s "What are you doing?"
    isa "Nothing. I'm just your little girl trying to cheer you up, that's all. Can't your babygirl have a hug? A special... [daddy_r_low] - [dau_r_low] moment?"
    mc_s "Uhm... okay..."

    show ep04_isajel23 at ken_burns_right_to_left
    isa "Don't you want me to cheer you up, [daddy_r]? I can make you feel so much better."
    mc_s "What?!"
    isa "Isn't this nice? Just us, so close. Don't I feel... good against you?"
    mc_s "Well... yes, but --"
    mc_s "What are you doing?"
    isa "Whatever you want me to do, [da_r]. You know I'm here for you right? For whatever you need. Any desire you have, I can fulfill."
    mc_s "Wha... what?"

    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

    show ep04_isajel24 with vpunch
    isa "[daddy_r]! Why so tense? Don't you like how I'm cheering you up? I'm just being a good girl for you. Isn't this what daddies and daughters do?"
    mc_s "Look, baby, I'm your [da_r_low], this is not right."

    show ep04_isajel25
    isa "I mean it's not weird for a [daddy_r] to kiss his little girl's forehead or cheek, right? It's perfectly... natural."
    mc_s "Yeah... I guess... I mean it's not bad but --"
    isa "And, of course, it's not bad for a little girl to kiss her [daddy_r_low]'s cheek or forehead. It's not weird. It's... loving."
    mc_s "Yeah, I suppose so..."
    isa "Then we don't have a problem, do we? We're just being... affectionate."
    mc_s "No... no, we don't."
    isa "Of course not. And if we don't have a problem then it should be fine for me to kiss my [daddy_r]'s cheek right? To show how much I... love him?"
    mc_s "Uh... yeah..."
    isa "Or maybe... your lips? That's where the real love is, isn't it, [daddy_r]?"
    $ show_walkthrough("ep04_isa_m3")
    menu:
        mc_t "What should I do? This is getting out of hand..."
        "Give her your cheeks":
            hide screen walkthrough_screen
            $ setChannelVolume(channel="sfx", subchannel=3, volume=1)
            $ playAudio(sfx_kiss_one, "sfx", 3, False, 0, 0)
            $ stopAudio(channel="music", subchannel=2, fadeout=2)

            show ep04_isajel26 at subtle_breathing with hpunch
            $ rm.update("isabella", "trust", 2)
            $ check_levels("isabella", "trust", 2)
            isa "Mmm... you taste nice, [daddy_r]."
            mc_t "Oh man, why is she acting like this? Is this because of Nanami's presence?"

            $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
            $ playAudio(isabella_happy, "music", 3, True, 0, 0)

            show ep04_isajel27 at ken_burns_bottom_to_top with vpunch
            isa "That was fun, wasn't it? Did it make you feel good, [daddy_r]?"
            mc_s "Why are you doing this, baby?"
            isa "Because you let me, [daddy_r]. We're not doing anything wrong. It's just love, isn't it? Pure, deep... love."
            mc_s "Yes... but why the sudden change in attitude?"

            show ep04_isajel28 with hpunch
            isa "Oh, [daddy_r]... Your little girl knows how to play the game."
            isa "As Hannibal once proved, sometimes the best path to victory lies through the enemy's own backyard."
            mc_s "That's... an interesting use of history."
            isa "Of course it is. I'm pretty clever aren't I?"
            mc_s "I mean I didn't expect you to talk like that."

            show ep04_isajel29 with normalfade
            isa "There's a lot you don't know about me, [daddy_r]. There's so much you don't know. But I'd love to... show you."
            mc_s "Yes, I understand that now. You're not the same little girl I left behind."
            isa "Oh, I'm still your little girl, [daddy_r]. Just a different kind of little girl. A more... mature one."
            mc_s "And what kind of little girl is that?"
            isa "The kind of little girl that is going to make sure you don't get seduced by any other slut."
            mc_s "..."
            isa "Bye, [daddy_r]! Think of me!"
        "Give her your lips":
            hide screen walkthrough_screen
            $ ep04_isabellakiss = True
            $ setChannelVolume(channel="sfx", subchannel=4, volume=0.81)
            $ playAudio(sfx_kiss_op_isa, "sfx", 4, False, 0, 0)
            $ stopAudio(channel="music", subchannel=2, fadeout=2)

            show ep04_isajel26 at subtle_breathing with hpunch
            $ rm.update("isabella", "trust", 5)
            $ check_levels("isabella", "trust", 5)
            $ rm.update("isabella", "cor", 5)
            $ check_levels("isabella", "cor", 5)
            isa "Mmm... you taste even better than I imagined, [daddy_r]."
            mc_t "Oh god, this is wrong. Why can't I stop?"

            show ep04_isajel30 at subtle_breathing, impact_shake
            mc_t "What the hell did I get myself into?"
            mc_t "I didn't expect her to use her tongue, now that's escalated quickly."

            $ stopAudio(channel="sfx", subchannel=4, fadeout=1)
            $ setChannelVolume(channel="music", subchannel=3, volume=0.2)
            $ playAudio(isabella_happy, "music", 3, True, 0, 0)

            show ep04_isajel31 at ken_burns_bottom_to_top
            isa "Woah! This... uhm... got... pretty intense there, huh? Did you like it, [daddy_r]?"
            mc_s "Uh-huh."
            isa "You didn't hesitate at all! I'm so... excited. Are you excited too, [daddy_r]?"
            mc_t "I need to stop this. It's gone too far."
            mc_s "Baby, we should --"

            show ep04_isajel32 at impact_shake
            isa "That was so naughty, wasn't it? Our first real kiss! How... special. I bet you've never kissed anyone like that before."
            mc_t "What have I done?"
            isa "Are you as thrilled as I am? Tell me, [daddy_r]! Did it feel good? Do you want... more?"
            mc_s "Uhm..."
            isa "You promised you would be honest with me. Don't you want to share your... feelings?"
            mc_s "Uhm... why are you acting like this, Isabella?"

            show ep04_isajel33 at ken_burns_left_to_right with normalfade
            isa "Like what, [daddy_r]? Am I not being a good girl for you? Don't you want me to be... very good?"
            mc_s "Like this... you know... the kiss... the talk... the clothes..."
            isa "If I didn't know better, I'd think you don't like it when your [dau_r_low] gets close to you. What a weird [daddy_r]! Don't you wanna be... closer to me?"
            mc_s "No! I love spending time with you. It's just that..."

            show ep04_isajel34 at ken_burns_top_to_bottom with vpunch
            isa "This is what a war looks like, [daddy_r]. As Sun Tzu said, 'The supreme art is subduing without fighting'."
            isa "Before they even realize it, the battle's already won. And I intend to... win you."
            mc_s "What the..."
            isa "Yes... your little girl is intelligent enough to know how to beat other sluts, [da_r]. I won't let anyone take you from me."
            show ep04_isajel29
            isa "Have a nice evening, [daddy_r]. And thanks for teaching me to kiss! I look forward to our next... lesson."
            mc_s "..."
            isa "Bye, [daddy_r]! Sweet dreams... of me."
    if ep03_isahug:
        $ ep04_ach_isabella = True
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with slowfade
    show ep03_antoback01 with circlewipe
    if ep04_isabellakiss:
        mc_t "What the hell just happened? My sweet little girl... she kissed me. On the lips. With tongue."
        mc_t "And she called Nanami a slut. Where did she learn to talk like that?"
        mc_t "Christ, I can still taste her... No! Focus!"
    else:
        mc_t "Did that really just happen? My innocent [dau_r_low] tried to kiss me on the lips."
        mc_t "And she called Nanami a slut. When did she become so... aggressive?"
        mc_t "I can still feel her breath on my face... God, what am I thinking?"
    mc_t "Shit! With all this... excitement, I completely forgot about Antonella's picture!"
    mc_t "I need to clear my head. I'll ask Paz about it. Maybe she knows something."
    mc_t "Anything to stop thinking about Isabella's... No. Stop it."
    nvl clear
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.1, fade_duration=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)      
    jump ep04_paz_sms




label ep04_pazosaka:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_quietnite, "amb", 1, True, 1, 0)

    show ep04_mcapartment at ken_burns_bottom_to_top with ccirclewipe
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_door_open2, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.7)
    $ playAudio(sfx_extnight, "amb", 2, True, 1, 0)   

    show ep04_paztask01 at ken_burns_left_to_right
    pa_t "Piece of cake. Now to check for any signs of forced entry."
    pa_t "Gotta make this quick. This running outfit isn't exactly stealth gear..."
    #NOTIFICATION SAVE
    $ update_htl_episodes()
    if htl_episodes == 4.1:
        $ show_custom_notification("save_tip")

    show ep04_paztask02
    pa_t "Front door's locked, no damage, no trace of a break-in. Looks clean."
    pa_t "The things I do for you, [mc_name]... Hope you appreciate it."
    pa_t "Time to check out his bedroom."

    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.1, fade_duration=1)    
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)

    show ep04_paztask03 at ken_burns_bottom_to_top
    pa_t "Hm, lights are out here too. How convenient."
    pa_t "First time I've seen this room without a sea of clothes on the floor."
    pa_t "God, his scent is everywhere. It's... intoxicating."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.2)
    $ playAudio(redkitsune_theme, "music", 1, True, 4, 0)

    pa_t "Wait, what's that?"
    pa_t "I'll just turn that lamp on... Let's see..."

    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.6)
    $ playAudio(sfx_lamp_turnon, "sfx", 3, False, 0, 1)
    pause 1.0
    show ep04_paztask04 with normalfade
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_flaslight_turnon, "sfx", 4, False, 0, 0)

    pa_t "Not exactly bright, but it'll do."
    pa_t "This isn't normal. Someone placed this deliberately. No way [mc_name] or his [dau_r_low] left this here."

    show ep04_paztask05 at ken_burns_corner_to_corner
    pa_t "Keys? Interesting. Whoever left this wanted me to find it. But who? And why?"
    pa_t "Better snap a pic for [mc_name]. He might know what this is about."

    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_door_open_creak, "sfx", 4, False, 0, 0)

    show ep04_paztask06 with normalfade
    pa_t "There are like metal balls all around? What the fuck? What are these?"

    show ep04_paztask07 at subtle_zoom_out
    pa_t "Jingle bells... One, two... nine in total, including the center one."
    pa_t "This arrangement must mean something, but I'm drawing a blank."
    pa_t "This is where [mc_name]'s expertise would come in handy."
    pa_t "Well, he was right about one thing. Someone definitely broke in to leave this. Could be the same person who left that picture he mentioned."

    show ep04_paztask08 at ken_burns_top_to_bottom
    pa_t "These look like security box keys. Small, but potentially significant."
    pa_t "Better take a closer look, see if they're labeled..."
    "Masked Woman" "Hey..."

    $ setChannelVolume(channel="sfx", subchannel=5, volume=1)
    $ playAudio(sfx_katana_warn, "sfx", 5, False, 0, 0)

    show ep04_paztask09 with hpunch
    pa_s "What the f--!"
    "Masked Woman" "Don't move. Not a muscle."
    pa_s "Who the hell are you? What do you want?"
    "Masked Woman" "This wasn't supposed to happen. Put your gun down. Slowly."

    show ep04_paztask10
    pa_s "Okay, easy now. My gun's in its holster, see? I'm just holding the keys. No funny business."
    "Masked Woman" "Why are you here? This wasn't meant for you."
    pa_s "I could ask you the same thing. Let's talk this through."
    "Masked Woman" "That's not an option, Paz."
    pa_s "How do you know my name?"
    "Masked Woman" "I know many things. Your name is the least of them."

    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.7)
    $ playAudio(sfx_katana_sheath_hit, "sfx", 6, False, 0, 0)

    show ep04_paztask11 at action_sequence, subtle_zoom_out with flash
    pa_s "Ngh..."
    "Masked Woman" "You shouldn't be here, Paz. This was for him. Always for him."

    show ep04_paztask12 with normalfade
    $ setChannelVolume(channel="sfx", subchannel=7, volume=1)
    $ playAudio(sfx_breathmouth_sleep_f, "sfx", 7, False, 0, 0)

    "Masked Woman" "Still breathing. Good. It wasn't time yet."
    "Masked Woman" "All this... for a photo. Now it's complicated. Dangerous."
    "Masked Woman" "You weren't supposed to be here... but you've done my work for me."

    show ep04_paztask13 at emotional_flashback with slowfade
    "Masked Woman" "I'm sorry, Paz. We're all part of something bigger. Even me."
    "Masked Woman" "Anonymity is no longer possible. The game has changed."
    "Masked Woman" "The next phase begins. Whether I want it or not."
#-- Hide and Turn off stuff
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
#-- End Update
    if htl_episodes == 4.1:
        pause 2
        scene eigengrau
        return


    else:
        jump ep04_mcnananight


    # else:
    #     scene eigengrau with rose
    #     pause 2
    #     $ resetAllVolumes()
    #     jump ep05_title




label ep04_mcnananight:
##episode 3 bug fix (delete on final version)
    if rm.get("elizabeth", "cor") > 2:
        $ rm.update("amber", "cor", 1)
        $ show_custom_notification("bugfix")
    if rm.get("elizabeth", "trust") > 2:
        $ rm.update("amber", "trust", 2)
        $ show_custom_notification("bugfix")
#####
#opening scene
    scene eigengrau with clouds_inverse
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)

    show ep04_mcroom01 at ken_burns_bottom_to_top with slowfade
    show home_location zorder 2 with dissolve
    pause 4
    hide home_location with dissolve
    show ep04_mcroom02  at slow_reveal with slowfade
    mc_t "Come on, she should've messaged something by now."
    mc_t "What if she discovered something... No, I can't think like that..."
    mc_t "No way I'm getting any sleep like this."

    show ep04_mcroom03
    mc_t "Fuck it... I need a drink to clear my head. I know it's not the best idea, but..."
    if rm.get('nanami', 'trust') > 40:
        $ ep04_nanaskimpy = True
    else:
        $ ep04_nanaskimpy = False
    $ stopAudio("amb", 2, 1)
    jump ep04_nanameet




label ep04_nanameet:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.6)
    $ playAudio(sfx_dooropen, "sfx", 1, False, 0, 0)
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.3)
    $ playAudio(sfx_fridge_hum, "sfx", 2, True, 1, 0)

    show ep04_nanakitchen01 at ken_burns_right_to_left
    mc_t "What's she doing in my kitchen at this time of the night?"
    nana "I know I put my drink here.... Did Madison take it again?"
    show ep04_nanakitchen02 at subtle_zoom_in with normalfade
    mc_t "Oh... Damn..."
    mc_t "She looks so hot dressed like that."
    nana "Where could it be...?"
    if ep04_nanadad:
        mc_t "Should I try my luck with her? I mean she already told me she wants me to be her [daddy_r] after all..."
    else:
        mc_t "Should I try my luck with her? She's been so shy around me..."
    mc_s "Hey there."
    nana "Huh? O-oh!"
    mc_s "Hi sweetie, what are you looking for in my kitchen at this time of night?"

    $ playAudio(nanami_theme, "music", 1, True, 2.0, 1.0)

    show ep04_nanakitchen03 with vpunch
    if ep04_nanadad:
        nana "[daddy_r]!!!"
    else:
        nana "M-Mr. [mc_name]!!"
    mc_t "She's really into me huh?"
    mc_s "Hey sweetheart!"

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_fridge_closedoor, "sfx", 1, False, 0, 0)
    $ stopAudio("sfx", 2, 1)

    show ep04_nanakitchen04 with hpunch
    if ep04_nanadad:
        nana "H-hi [daddy_r]... I-I just came to get my drink, if that's okay... I forgot to take it this afternoon..."
    else:
        nana "I-I'm so sorry, Mr. [mc_name]... I just came to get my drink... I-I forgot it here this afternoon..."
    mc_s "Sure honey, no problem."
    if ep04_nanadad:
        nana "T-thank you, [daddy_r]..."
    else:
        nana "Y-you're very kind, Mr. [mc_name]..."
    show ep04_nanakitchen05 at subtle_zoom_out with normalfade
    mc_t "This little thing is driving me crazy..."
    mc_t "Her skin looks so soft... Those tits are so perfect..."
    if ep04_nanadad:
        nana "A-are you okay, [daddy_r]? You seem... distracted..."
    else:
        nana "E-excuse me, Mr. [mc_name]... but are you feeling unwell...?"
    mc_s "Huh? Oh, Yeah sure."

    show ep04_nanakitchen06
    nana "Is there s-something wrong?"
    mc_s "Yes, sweetie... There's something wrong... You know that, don't you?"
    nana "W-well... No?"
    mc_s "You can't walk around like that without expecting consequences..."
    nana "Like w-what...?"
    mc_s "You look... uhm... incredible... in that outfit."

    show ep04_nanakitchen07
    nana "Haha, O-oh... um... well..."
    if ep04_nanadad:
        nana "D-[daddy_r], I didn't think it would cause any p-problem... That's how I sleep all the time..."
    else:
        nana "I-I'm so sorry, Mr. [mc_name]... This is just my usual sleepwear... I-I didn't mean to be inappropriate..."
    mc_s "But sweetie... You can't be dressed like that in my house and expect me to..."
    mc_t "What am I saying... She's not ready for this kind of talking... she has such pure innocence..."
    nana "E-expect what...?"
    mc_s "..."

    show ep04_nanakitchen08 at dramatic_realization
    mc_t "She looks so good... And we're totally alone right now..."
    mc_s "I mean... You can't be dressed like this, and not expect me to do anything about it..."
    nana "O-oh..."
    show ep04_nanakitchen10
    if ep04_nanadad:
        nana "But D-[daddy_r]... what do you...?"
    else:
        nana "Mr. [mc_name], I-I don't quite understand..."
    mc_t "Oh little one..."
    mc_t "You have no idea how hot you are..."
    mc_s "Nothing sweetie, don't worry."
    mc_s "I'm going to get a beer from the fridge. You can get your drink and we can both go back to bed."
    if ep04_nanadad:
        nana "But [daddy_r]! I... I w-wanna stay here with you..."
    else:
        nana "Please, Mr. [mc_name]... C-could I maybe... stay for a moment...?"
    show ep04_nanakitchen09
    mc_s "I know that honey... But it's getting really late, we should go to sleep, shouldn't we?"
    if ep04_nanadad:
        nana "W-well... I just wanted to spend time with y-you, [daddy_r]... Could I maybe stay here for a l-little while...?"
    else:
        nana "I-I understand it's late, but... maybe I could stay just a little longer, Mr. [mc_name]...?"
    mc_s "I don't know sweetie..."
    if ep04_nanadad:
        nana "Please? I-I'll just drink milk, t-that's all, p-pinky promise!"
    else:
        nana "I-I'll only have my milk... I promise I won't be any trouble..."
    mc_s "Hmm... Okay, fine. But just until your drink is finished."
    if ep04_nanadad:
        nana "[daddy_r], y-you won't regret it!"
    else:
        nana "T-thank you so much, Mr. [mc_name]!"
    mc_t "I already regret it... I don't know if I'm gonna be able to control myself near this cute little thing..."

    $ stopAudio("music", 1, 2)
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    pause 0.5
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0) 

    show ep04_nanakitchen11 with circlewipe
    if ep04_nanadad:
        nana "[daddy_r], could you help...? It's stuck..."
    else:
        nana "Um... Mr. [mc_name]? The lid seems to be stuck..."
    mc_t "Oh man..."
    mc_s "Sure..."
    if ep04_nanadad:
        nana "Thank you, [daddy_r]!"
    else:
        nana "I really appreciate your help, Mr. [mc_name]..."
    show ep04_nanakitchen12 at subtle_zoom_out with normalfade
    nana "Oh! I should get a glass for the milk..."
    mc_s "Why? Just drink it straight from the bottle, sweetie. It's not a problem."
    nana "Uhm... It's just t-that... I prefer using proper glasses..."
    if ep04_nanaskimpy:
        show ep04_anim_nana02
    else:
        show ep04_anim_nana01
    nana "Would you... would you m-mind putting the milk in a g-glass...?"
    mc_s "Yeah sure, honey. Glasses are in the shelf near the stove."
    mc_t "Damn... She's incredibly sexy without even trying..."

    show ep04_nanakitask01 with normalfade
    nana "Are they up there...?"
    mc_s "Yes."
    if ep04_nanaskimpy:
        mc_t "Her top is slipping... Should I warn her...?"
        mc_t "Maybe I should just..."

    show ep04_nanakitask02
    mc_t "No way she's reaching that..."
    if ep04_nanaskimpy:
        mc_t "And that babydoll is barely hanging on... Just a little more..."
    else:
        mc_t "That top is struggling to contain her..."
    if ep04_nanadad:
        nana "Aww... I can't reach it, [daddy_r]... C-could you help me...?"
    else:
        nana "I-I'm sorry to ask, Mr. [mc_name], but... could you possibly help me reach it...?"
    if ep04_nanaskimpy:
        mc_t "One shoulder down... Just one more and..."
    if ep04_nanadad:
        nana "...[daddy_r]?"
    else:
        nana "...Mr. [mc_name]?"
    mc_s "What? Oh right! Sorry sweetheart. Let me help you."

    $ setAllSubchannelsVolume("amb", 0, 1.0) 
    scene eigengrau with slowfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1
    $ setAllSubchannelsVolume("amb", 0.3, 1.0) 

    show ep04_nanakitask05 with circlewipe
    mc_s "Here you go, sweetie."
    if ep04_nanadad:
        nana "Woah... Thank you, [daddy_r]! You're so strong and tall!"
    else:
        nana "O-oh my... Thank you, Mr. [mc_name]! You make it look so easy..."
    mc_s "Haha, it's nothing."

    show ep04_nanakitask06 with normalfade
    if ep04_nanadad:
        nana "You're amazing, [daddy_r]!"
    else:
        nana "You're so helpful, Mr. [mc_name]..."
    mc_s "Haha... Just for getting a glass? That's all it takes?"
    nana "Y-yes! I tried so many times but I-I couldn't reach... You did it so easily!"
    mc_s "Well, that's because you're so tiny, sweetie. It's nothing special."
    if ep04_nanadad:
        nana "Ohh... But I l-love that you're so big, [daddy_r]!"
    else:
        nana "I-It's nice having someone so... big around..."
    mc_t "And speaking of big things..."
    nana "I wish I was bigger... Then maybe we could share that beer t-together..."
    mc_s "You want to try the beer?"
    nana "I-I've had some before... It's strange, but... if you're drinking it too, m-maybe it wouldn't be so bad..."
    mc_t "Should I let her drink? This could be interesting..."
    mc_t "A perfect chance to be alone with her... But also risky..."

    $ show_walkthrough("ep04_nanameetmenu")
    menu:
        mc_t "... I don't know what to do..."
        "Let her try the beer":
            hide screen walkthrough_screen

            mc_s "Alright, sweetie. You can have some. But if you don't like it, stop right away."
            mc_s "Understood?"
            nana "Understood!!"
            $ rm.update("nanami", "cor", 2)
            $ check_levels("nanami", "cor", 2)
            jump ep04_nanabooze #to beer scene (condition have points on corruption)


        "Keep it innocent":
            hide screen walkthrough_screen

            mc_s "I'm sorry sweetie, but no beer tonight. Let's stick with your milk, okay?"

            scene eigengrau with slowfade
            show ep04_nanakitask03
            nana "Aww... O-okay..."
            nana "...Maybe some other time?"
            mc_s "Maybe when you're a bit older. Right now, it's way past your bedtime."
            nana "I-I understand..."
            show ep04_nanakitask04
            $ rm.update("nanami", "trust", 2)
            $ check_levels("nanami", "trust", 2)
            if ep04_nanadad:
                nana "D-[daddy_r]... would you fill me up, p-please?"
            else:
                nana "Mr. [mc_name]... would you p-please fill me?"
            mc_t "..."
            mc_t "The way she said that... Is she even aware of how that sounds?"
            nana "Please! My glass is empty!"
            mc_s "Oh god... You're too much..."
            nana "Huh? Did I say something w-wrong?"
            mc_s "No sweetie, let me get your milk ready."

            $ ep04_mcmilk = True
            jump ep04_nanamilk




label ep04_nanamilk:
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_chair_lather_sit, "sfx", 1, False, 0, 0)
    pause 1
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)

    show ep04_nanakitmilk01 at ken_burns_right_to_left with circlewipe
    if ep04_nanadad:
        nana "T-tell me more about yourself! Y-you're my [daddy_r], but I barely know anything..."
    else:
        nana "I'd love to know more about you, Mr. [mc_name]... If that's okay..."
    mc_s "Sure thing, sweetie. What would you like to know?"
    nana "Oh! W-when was your f-first kiss?"
    mc_s "My first kiss, huh..."

    $ setChannelVolume("amb", 1, 0, 1.5)
    pause 0.5
    scene eigengrau with smoke
    $ playAudio(antonella_love, "music", 1, True, 2.0, 1.0)

    show ep01_postgame07 at ken_burns_left_to_right with smoke
    mc_s "It was with this girl Antonella... We were young, probably around your age."
    nana "H-how was it like?"
    mc_s "I was terrified, honestly."
    mc_s "We'd just finished our first date at a bowling alley... Both of us were so awkward, but the kiss was sweet."

    show ep01_postgame09 with smoke
    mc_s "It feels like forever ago..."
    mc_s "She had this gorgeous smile that could light up a room..."
    mc_s "Could've had any guy she wanted, but somehow picked me..."

    show ep01_postgame08 at ken_burns_right_to_left with smoke
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_kiss_one, "sfx", 1, False, 0, 0)

    mc_s "Her lips were so soft, like silk... She kissed my cheek first, and then--"
    nana "Wait... not on the l-lips first?"
    mc_s "No, actually..."
    nana "Didn't you l-like her enough?"
    mc_s "I liked her a lot! That was the problem... I was too nervous..."

    $ stopAudio("music", 1, 2)
    pause 0.5
    scene eigengrau with smoke
    $ setChannelVolume("amb", 1, 0.3, 1.5)

    show ep04_nanakitmilk02 with smoke
    nana "You? N-nervous?"
    mc_s "Hard to believe, right?"
    nana "Like... like how I get?"
    show ep04_nanakitmilk03 at dramatic_focus
    mc_s "Similar, yeah. Everyone's got their shy moments."
    mc_t "Though I'm definitely not that shy kid anymore..."
    if ep04_nanadad:
        nana "That's s-so sweet, [daddy_r]... I never thought you'd be shy..."
    else:
        nana "How s-surprising, Mr. [mc_name]... It's quite endearing..."
    mc_s "Thanks, princess."
    mc_s "But hey, you haven't touched your milk. Drink up, or it's bedtime."
    nana "O-oh right! I got distracted..."
    $ playAudio(nanami_chill_theme, "music", 2, True, 2.0, 1.0)

    show ep04_nanakitmilk04 with vpunch
    nana "*gulp, gulp*"
    mc_t "This girl looks like a little innocent angel..."
    mc_t "But seeing her swallow that milk  is making me feel things... Like an urge to..."
    nana "*gulp, gulp*"
    show ep04_nanakitmilk05 with normalfade
    mc_t "...An urge to... Make her mine..."
    mc_t "To take advantage of this cute innocent babygirl and make her completely addicted to me."
    nana "*gulp, gulp*"
    mc_t "To make her so dependent on my cock and my orders... She'll do anything I command, my little fuckdoll..."
    mc_t "For fuck's sake! What's wrong with me? These thoughts..."

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_glass_ontable, "sfx", 1, False, 0, 0)

    show ep04_nanakitmilk06 with normalfade
    nana "Mmm, that was really good!"
    mc_t "This girl has a gift... Every single thing she does turns me on somehow..."
    nana "Y-you should give me m-milk more often..."
    mc_t "Oh... Yeah..."
    mc_t "Of course she has to say it like that..."
    mc_t "The way those drops landed on her chest... This is pure torture..."
    mc_s "Sweetie, you've got something there."
    nana "Where?"
    mc_s "On your neck... and your face. Got some milk drops."

    show ep04_nanakitmilk07 with normalfade
    nana "O-oh no! Where? This is so e-embarrassing!"
    nana "Oh m-my gosh... T-that's so embarrassing! I-I didn't notice it... Please don't l-laugh at me!"
    nana "I-I'm so clumsy and s-stupid!"
    mc_s "Hey don't say that! It's nothing sweetie..."
    mc_s "Here, let me help clean you up."

    show ep04_nanakitmilk08
    nana "O-okay."
    if ep04_nanadad:
        nana "I'm s-sorry for being so messy, D-[daddy_r]..."
    else:
        nana "I apologize for being so clumsy, Mr. [mc_name]..."
    mc_t "That innocent, messy face... If she only knew what it does to me..."
    mc_s "That's okay honey, don't worry about it."
    nana "I-I always do t-this kind of things... It's e-embarrassing..."
    show ep04_nanakitmilk09 with normalfade
    mc_s "You know what?"
    nana "Hmm?"
    mc_s "Your innocence... it makes me want to..."
    mc_s "Take care of you... Keep you safe..."
    mc_t "I'm really gonna scare her if I continue like this..."
    nana "Um... what about here?"
    mc_s "What?"
    nana "The drops... on my chest... Could you help clean those too?"
    mc_s "..."
    mc_s "Of course, sweetie..."

    show ep04_nanakitmilk10 with normalfade
    mc_t "This girl's going to be the death of me..."
    if ep04_nanadad:
        nana "T-thank you, [daddy_r]... You make me feel so p-protected..."
    else:
        nana "T-thank you, Mr. [mc_name]... You're so gentle..."
    mc_s "Yeah..."
    mc_s "I'm sure about that sweetie..."

    $ stopAllSubchannels("music", 2.0)

    show ep04_nanakitmilk11 with normalfade
    mc_s "It's all clean now."
    nana "Oh..."
    mc_s "Huh?"
    nana "I-I only d-drank half..."
    mc_s "Oh yeah... It is just half full..."
    mc_s "That's okay, honey."
    nana "B-But... I-I didn't drink i-it all..."
    mc_s "Yeah, but that's okay sweetie. You don't have to finish it right now."

    show ep04_nanakitmilk12 with normalfade
    nana "...But I'm feeling sleepy already..."
    if ep04_nanadad:
        nana "I'm s-sorry, [daddy_r]... I tried to stay awake..."
    else:
        nana "Please forgive me, Mr. [mc_name]... I'm trying my best..."
    nana "I don't want to d-disappoint you, but--"
    mc_s "Shh... Don't say that."
    mc_s "It's okay sweetie, you haven't let me down."
    mc_s "In fact, if you're sleepy, it might be a good idea for us to go to bed now, don't you think?"
    mc_s "I can take that glass back to the fridge, so it won't spoil."

    show ep04_nanakitmilk13
    nana "But... I wanted to stay with you longer..."
    mc_s "You're barely keeping your eyes open, sweetie."
    nana "I know, but..."
    mc_s "What is it?"
    nana "Well..."
    if ep04_nanadad:
        nana "If you w-want me to... I can try to stay up a bit longer, D-[daddy_r_low]..."
    else:
        nana "If you'd like... I could try to stay awake, Mr. [mc_name]..."
    nana "...If that would make you h-happy."
    $ show_walkthrough("ep04_nanamilkmenu")
    menu:
        mc_t "Should I keep her here with me? She already told me she's feeling sleepy."
        "Make her stay":
            hide screen walkthrough_screen

            mc_s "Yeah, sure honey. If that's not a problem for you."
            ##already giving 2 points on love @ label
            jump ep04_nana_askkiss


        "Send her to bed":
            hide screen walkthrough_screen

            mc_s "No sweetie, you're going to bed if you're tired. Don't worry about that."

            jump ep04_nananostay




label ep04_nananostay:
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(nanami_secure_theme, "music", 1, True, 2, 0)

    show ep04_nanakitmorekiss00
    $ rm.update("nanami", "trust", 0)
    $ check_levels("nanami", "trust", 0)
    nana "O-oh... Okay... If y-you're sure."
    mc_s "It's for the best, honey. You need your rest."
    nana "I know it's silly, but..."
    nana "The thought of doing something that would m-make you happy... it makes my heart feel warm..."
    nana "...I just wanted to be useful to y-you somehow..."
    mc_s "Sweetie..."
    mc_t "God, keeping her here would be so easy..."
    mc_t "But I can see how tired she is... And if she stays, I might not be able to hold back..."
    mc_s "Don't worry about that right now, okay? There'll be plenty of chances for us to spend time together."

    show ep04_nanakitmorekiss05
    if ep04_nanadad:
        nana "If that's what D-[daddy_r_low] wants..."
    else:
        nana "If that's what you think is best, Mr. [mc_name]..."
    nana "W-When would y-you prefer me to drink your milk?"
    mc_s "My milk...?"
    nana "Y-yes, from the glass you p-poured for me..."
    mc_t "God... The way she phrases things..."
    mc_s "...Right. That milk."
    nana "I can finish it tomorrow... or whenever you'd l-like me to..."
    mc_t "Keep it together... She has no idea what she's implying..."

    show ep04_nanakitmorekiss06 with normalfade
    if ep04_nanadad:
        nana "I guess I'll see you tomorrow then... G-goodnight, [daddy_r]..."
    else:
        nana "I should let you rest... G-goodnight, Mr. [mc_name]..."
    mc_s "Sweet dreams, honey. May angels sing you to sleep."
    nana "Wow! T-that was so beautiful! Did you come up w-with that?"
    mc_s "No, sweetie. My [mo_full_r_low] used to say it to me every night."
    nana "Oh! It's such an amazing p-phrase!"
    mc_t "She gets excited over the simplest things... It's both adorable and dangerous..."

    show ep04_nanakitkiss07 with normalfade
    if ep04_nanadad:
        nana "Thank you for the milk, D-[daddy_r_low]! And for being so nice..."
    else:
        nana "Thank you for your kindness, Mr. [mc_name]... And the milk..."
    mc_s "Sleep well, princess."
    mc_t "That was... intense."
    mc_t "Now she really does look like an angel... It would've been too tempting if I had let her stay here..."
    mc_t "Looking at her now, she really does look angelic... Would've been impossible to resist if she'd stayed..."
    mc_t "I don't even need that beer anymore. Better head back before these thoughts get worse."

    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom




label ep04_nana_askkiss:
    show ep04_nanakitkiss01
    $ rm.update("nanami", "trust", 1)
    $ check_levels("nanami", "trust", 1)
    nana "Umm..."
    mc_s "Something wrong? I thought this would make you happy."
    nana "Y-yes, but... I..."
    mc_s "But what?"
    mc_s "You can tell me."
    nana "I-I'm not sure if I should say this..."
    mc_s "Hey, take your time, sweetie. You're safe with me."
    nana "I... I want..."
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(nanami_love_theme, "music", 1, True, 2, 0)

    show ep04_nanakitkiss02 at slow_reveal with normalfade
    nana "I want you to k-kiss me..."
    mc_s "You want what?!"
    if ep04_nanadad:
        nana "Please k-kiss me... [daddy_r]..."
    else:
        nana "P-please kiss me... Mr. [mc_name]..."
    if ep04_nanakiss:
        mc_t "We've shared that quick, innocent peck before... But this feels different..."
    else:
        mc_t "Our first kiss... She's really asking for this..."

    show ep04_nanakitkiss03 at subtle_zoom_out with normalfade
    if ep04_nanadad:
        nana "Please D-[daddy_r_low]... Would you k-kiss me?"
    else:
        nana "Mr. [mc_name]... Would you consider... k-kissing me?"
    mc_t "Should I do it? The only one who's losing if I don't is myself."
    if ep04_nanadad:
        mc_t "She does deserve it... She has behaved like such a good girl since she arrived here."
        mc_t "And a good [daddy_r] needs to reward a good girl after all... and I don't mind at all kissing this sexy babygirl..."
        mc_t "Who would? I can't even control myself now!"
    else:
        mc_t "She does deserve it... She's been nothing but sweet and well-behaved since she arrived..."
        mc_t "And she needs to know she's special... Plus, I definitely wouldn't mind kissing such a gorgeous girl..."
        mc_t "Who could resist? I can barely control myself..."

    $ show_walkthrough("ep04_nanaaskismenu")
    menu:
        mc_t "She asked for it herself... That makes it okay, right?"
        "Kiss her":
            hide screen walkthrough_screen

            mc_s "Come here, baby girl..."
            if not ep04_nanakiss:
                $ ep04_nanakiss = True
            # +2 cor @ end of label
            jump ep04_nanakiss


        "Reject her":
            hide screen walkthrough_screen

            mc_s "I'm sorry sweetie... But we shouldn't..."
            # no points @ end of label
            jump ep04_nananokiss




label ep04_nananokiss:
    $ ep04_refusednanakiss = True
    $ stopAllSubchannels("music", 2.0)

    show ep04_nanakitmorekiss05
    mc_s "It wouldn't be right..."
    nana "B-but..."
    mc_s "I could give you a forehead kiss instead?"
    nana "Hmmmm... No, it's o-okay... If y-you don't want t-to k-kiss me, that's f-fine..."
    mc_s "Huh? You sure honey?"

    $ setChannelVolume(channel="music", subchannel=2, volume=0.3)
    $ playAudio(nanami_innocence_theme, "music", 2, True, 2, 0)

    show ep04_nanakitmorekiss00
    nana "Y-yes... Please don't worry about m-me..."
    mc_s "I really am sorry..."
    mc_s "Maybe some other--"
    if ep04_nanadad:
        nana "It's fine, D-[daddy_r_low]... You've made your feelings c-clear..."
    else:
        nana "Please don't trouble yourself, Mr. [mc_name]... I was too f-forward..."
    mc_s "..."

    show ep04_nanakitkiss07 with normalfade
    nana "I should g-go to bed now..."
    mc_s "Wait..."
    if ep04_nanadad:
        nana "G-goodnight [daddy_r]."
    else:
        nana "G-goodnight, Mr. [mc_name]..."
    mc_t "Fuck... I really messed this up..."
    mc_t "The hurt in her eyes... She must hate me now..."
    mc_t "Why do I always make the wrong choice?"
    mc_t "Fuck it, I'm back to my room. This is making me feel like shit."

    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom




label ep04_nanakiss:
    show ep04_nanakitkiss04
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_kiss_nana, "sfx", 1, False, 0, 0)

    mc_t "Oh god... Her lips are so soft..."
    mc_t "The way she trembles against me... So innocent..."
    nana "Mmmmh..."
    show ep04_nanakitkiss05
    nana "That was... amazing... This... This is the b-best feeling e-ever..."
    nana "It's l-like... M-my heart is beating s-so fast..."
    if ep04_nanadad:
        nana "...[daddy_r]... I've never felt anything like this... It's like my whole body is..."
    else:
        nana "...Mr. [mc_name]... These feelings... I've never..."
    nana "Is it n-normal to feel so... so warm inside?"
    mc_s "That's perfectly natural, sweetie... Your body is just responding to new feelings..."
    if ep04_nanadad:
        mc_s "[daddy_r] will guide you through everything..."
    else:
        mc_s "I'll help you understand these new sensations..."
    nana "Your kiss... it makes everything feel r-right..."
    if ep04_madpath == 1:
        show ep04_nanakitkiss06 with normalfade
        nana "W-we can do it a-again if y-you want, D-[daddy_r]..."
        mc_t "Her innocence... She's so pure... This is making me feel bad... It feels like I'm using her somehow."
        mc_t "Should I do it again? She's so goddamn addicting..."
        mc_t "One more couldn't hurt..."
        mc_s "Alright princess, one more... But then it's bedtime, okay?"
        nana "Yay!"
        jump ep04_nana2ndkiss


    else:
        show ep04_nanakitkiss06 with normalfade
        nana "I never knew a kiss could feel like that..."
        nana "My whole body feels like it's floating..."
        if ep04_nanadad:
            nana "D-[daddy_r_low]... will you teach me more things like this?"
        else:
            nana "Mr. [mc_name]... would it be possible to... learn more from you?"
        mc_s "All in good time, princess. But now it's late..."

        show ep04_nanakitkiss07 with normalfade
        nana "You're right... I should go..."
        if ep04_nanadad:
            nana "Thank you for the kiss, [daddy_r]... I'll treasure it forever..."
            nana "G-goodnight [daddy_r]."
        else:
            nana "Thank you for this precious moment, Mr. [mc_name]..."
            nana "G-goodnight, Mr. [mc_name]..."
        mc_t "Anyways, I'm back to my room. I don't even need that beer anymore."

        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("music", 2.0)
        jump ep04_isabella_mcroom




label ep04_nana2ndkiss:
    menu:
        "Kiss her again":
            pass
    show ep04_nanakitmorekiss01 with vpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_kiss_op_isa, "sfx", 2, False, 0, 0)
    if ep04_nanadad:
        nana "Mmm... K-kiss me again, [daddy_r]..."
    else:
        nana "Mr. [mc_name]... would you k-kiss me once more...?"
    mc_s "Of course sweetie."
    nana "Mmmmm..."
    mc_t "Fuck... Those little sounds she's making... So innocent yet so sexy... Making me want to devour her..."

    show ep04_nanakitmorekiss02
    mc_t "Wait... What's she doing?"
    nana "Mmmmm..."
    mc_t "Is she trying to hint at something?"
    nana "Mmmmmm..."
    show ep04_nanakitmorekiss03
    mc_t "Ah... I see what you want, you little tease..."
    mc_t "Alright princess, since you're asking so sweetly..."
    nana "Uhm?"
    show ep04_nanakitmorekiss04
    nana "MMmmph!!!"
    nana "Mmmmmmmmm!!!"
    nana "Mmmmm..."
    $ stopAllSubchannels("sfx", 1.0)
    $ stopAllSubchannels("music", 2.0)

    show ep04_nanakitmorekiss05 with normalfade
    if ep04_nanadad:
        nana "D-[daddy_r_low]! Your t-tongue... it just..."
    else:
        nana "Mr. [mc_name]! Y-your tongue... I never..."
    mc_s "Isn't that what you wanted?"

    show ep04_nanakitmorekiss06 with normalfade
    nana "When I opened my m-mouth? I... I was just trying to breathe..."
    nana "I d-didn't expect you to... to do that inside..."
    mc_s "Oh shit... You really didn't know?"
    mc_s "I'm so sorry, sweetie. I misunderstood."
    nana "It was kind of t-ticklish a-and n-nice..."
    nana "I-I liked i-it a l-lot, b-but t-this f-feels s-so w-weird..."
    nana "I-I mean i-it's g-good a-and all... B-but..."
    mc_s "But...?"
    nana "N-Nothing..."
    show ep04_nanakitmorekiss07
    nana "I'm starting to feel... different..."
    mc_t "What does she mean?"
    nana "Well... I feel r-really hot... L-Like s-something is happening t-to me..."
    nana "...Down there."
    mc_s "From our kissing?"
    nana "Yes..."
    if ep04_nanadad:
        mc_t "Time to be the kind of [daddy_r_low] she needs..."
        mc_s "Want [daddy_r_low] to help you feel better?"
    else:
        mc_t "She needs guidance..."
        mc_s "Would you like me to help you understand these feelings?"

    $ stopAllSubchannels("music", 2.0)

    show ep04_nanakitmorekiss08 with normalfade
    nana "W-What do y-you mean?"
    if ep04_nanadad:
        mc_s "[daddy_r] can make those feelings better..."
        nana "...Make it better?"
    else:
        mc_s "I can show you what these sensations mean..."
        nana "...Show me?"
    mc_t "She's so innocent... Does she even understand what's happening to her body?"
    mc_s "You're feeling heat... between your legs, aren't you?"
    nana "Y-yes... I'm all wet... Is that normal?"
    mc_s "That's perfectly natural, sweetie. It happens when someone gets... excited."
    nana "Is that what this is? Being... excited?"
    if ep04_nanadad:
        mc_s "Would you let [daddy_r_low] check?"
    else:
        mc_s "Would you trust me to help you understand?"
    nana "I... okay..."
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_surprisenana, "sfx", 1, False, 0, 0)

    show ep04_nanakitmorekiss09 with vpunch
    nana "Ah! W-what are you...?!"
    if ep04_nanadad:
        mc_s "Shh... [daddy_r_low]'s just making sure everything's okay."
        nana "O-okay [daddy_r_low]..."
    else:
        mc_s "Trust me... I'll take care of you."
        nana "Y-yes, Mr. [mc_name]..."
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_bodydrop_ontable, "sfx", 2, False, 0, 0)
    pause 0.2
    show ep04_nanakitmorekiss10 with vpunch
    nana "S-should I do a-anything?"
    mc_s "Just relax, Nanami."
    nana "... Like, spread l-legs?"
    if ep04_nanadad:
        mc_s "That's my good girl... Open up for [daddy_r_low]."
    else:
        mc_s "Yes... just like that..."

    $ playAudio(mc_nanami_theme, "music", 3, True, 2.0, 1.0)
    nana "L-like this?"
    mc_s "Perfect, princess."
    if ep04_nanadad:
        nana "Is everything okay, D-[daddy_r_low]?"
    else:
        nana "Is this... appropriate, Mr. [mc_name]?"
    mc_s "We need to remove these first..."
    if ep04_nanadad:
        nana "D-[daddy_r_low]... What are you...?"
    else:
        nana "Mr. [mc_name]... Should we...?"
    if ep04_nanaskimpy:
        show ep04_anim_nana03
    else:
        show ep04_anim_nana04
    mc_s "Just checking if everything's as it should be..."
    mc_s "Are you uncomfortable, sweetie?"
    nana "N-no... Yes... Maybe... I don't know..."
    nana "It feels strange being... exposed like this..."
    if ep04_nanadad:
        nana "Especially for you, D-[daddy_r_low]..."
        mc_s "Oh baby girl..."
        mc_s "[daddy_r] loves what he sees... Such a pretty little flower..."
        nana "Really? It's... cute enough?"
    else:
        nana "Especially with you, Mr. [mc_name]..."
        mc_s "You're beautiful..."
        mc_s "Perfect... absolutely perfect..."
        nana "You really think so?"
    mc_s "It's more than cute..."
    mc_s "It's the most beautiful thing I've ever seen..."
    if ep04_nanadad:
        nana "C-can I close them now, D-[daddy_r_low]? You've seen so much..."
        mc_s "Don't you trust [daddy_r_low]?"
    else:
        nana "May I... close them now, Mr. [mc_name]? This is so embarrassing..."
        mc_s "Don't you trust me?"
    nana "I do, but... it's overwhelming..."
    mc_s "Of course you can close them, princess."

    $ setAllSubchannelsVolume("amb", 0, 1.0)
    $ stopAllSubchannels("music", 2.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)

    show ep04_nanakitmorekiss13
    mc_s "You good?"
    mc_t "Was that too much too soon?"
    mc_t "Did I ruin everything?"
    mc_s "Sweetie? Are you okay?"
    nana "..."
    show ep04_nanakitmorekiss14
    if ep04_nanadad:
        nana "D-[daddy_r_low]... You were right..."
    else:
        nana "Mr. [mc_name]... What you said..."
    mc_s "About what?"
    nana "These feelings..."
    nana "My body is still... reacting..."
    $ playAudio(nanami_love_theme, "music", 1, True, 2.0, 1.0)

    show ep04_nanakitmorekiss15
    nana "It's like... Some parts are g-getting hot... and I want to rub against s-something."
    nana "This h-has never h-happened to me before, D-[daddy_r]... Why is t-this happening?"
    mc_t "She's aroused but doesn't understand how to handle it..."
    mc_t "Is she asking for more?"

    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 3, False, 0, 0)

    show ep04_nanakitmorekiss16 with vpunch
    nana "I-I'm gonna g-go to my r-room n-now."
    if ep04_nanadad:
        nana "Thank you for everything, D-[daddy_r_low]..."
    else:
        nana "Thank you for your... attention, Mr. [mc_name]..."
    mc_s "Wait, are you upset?"
    nana "No, not at all..."
    nana "You showed me something... wonderful tonight."
    nana "I'm happy but now..."
    show ep04_nanakitkiss07 with normalfade
    nana "...I n-need to go and..."
    nana "You know... Enjoy it w-while I c-can."
    nana "Thank y-you!"
    mc_s "Hold on..."
    mc_t "Why such a sudden exit?"
    mc_t "Damn... Forgot all about that beer... Better head back to my room..."

    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom




label ep04_nanabooze:
    $ setAllSubchannelsVolume("amb", 0, 1.0)
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_chair_lather_sit, "sfx", 1, False, 0, 0)
    pause 1
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)

    show ep04_nanakitdrunk01 at ken_burns_left_to_right with circlewipe
    if ep04_nanadad:
        nana "How did your first time feel, [daddy_r]?"
    else:
        nana "Mr. [mc_name]... may I ask about your first... um..."
    mc_s "...Huh?"
    nana "Your f-first time! How did i-it feel?"
    mc_s "What do you mean my first time? My first time doing what?"
    if ep04_nanadad:
        nana "Well, your f-first time... y'know... having s-s..."
    else:
        nana "Your first... when you... I mean... s-s..."
    mc_s "Oh! Ohhhhhh... Yeah... That first time..."
    if ep04_nanadad:
        nana "Hehe, y-yeah [daddy_r_low]... Your f-first time!"
    else:
        nana "Y-yes, Mr. [mc_name]... that time..."
    mc_s "It was a long time ago, sweetie..."
    nana "Was it with the same p-person you had Isabella?"
    $ setChannelVolume("amb", 1, 0, 1)
    scene eigengrau with smoke
    if not ep01_first:
        $ playAudio(antonella_sad_theme, "music", 1, True, 2.0, 1.0)

        show ep04_anto_memory01 at ken_burns_right_to_left with smoke
        mc_s "...Yes."
        if ep04_nanadad:
            nana "Woahhhh! It m-must be amazing to h-have your first t-time with s-someone y-you love..."
        else:
            nana "Woahhhh! To share such a s-special moment with someone you l-love..."
        hide ep04_nanakitdrunk01
        show ep04_anto_memory02 at subtle_zoom_in with smoke
        if ep04_nanadad:
            nana "And even b-better, to have y-your child with her!!"
        else:
            nana "And then... to have a c-child together..."
        mc_s "Yes... it really was a dream come true..."

        $ setChannelVolume("amb", 1, 0, 1.5)
        scene eigengrau with smoke
        show ep04_nanakitdrunk01 with smoke
        if ep04_nanadad:
            nana "[daddy_r]... Can y-you tell me m-more about it?"
            nana "How i-it felt? How did s-she looked like? How i-it all happened? Please?"
        else:
            nana "Mr. [mc_name]... Would you t-tell me more?"
            nana "How was it? What was she l-like? How did it h-happen?"
        $ setChannelVolume("amb", 1, 0, 1)
        scene eigengrau with smoke
        show ep01_game49 at subtle_zoom_out with smoke
        mc_s "Well, she was... really special to me."
        mc_s "I've never felt so good with someone before her. She was so smart and sexy."
        mc_s "It's been almost 20 years since then... I still remember everything like it happened yesterday."
        if ep04_nanadad:
            nana "Awww... That sounds s-so sweet!"
        else:
            nana "That's so r-romantic..."
        show ep01_pregame08 at ken_burns_left_to_right
        mc_s "She had this adorable face that made my heart skip a beat."
        mc_s "She always knew how to make me feel good."
        mc_s "When she smiled, it was like... the whole world lit up around her."
        if ep04_nanadad:
            nana "Awww! But [daddy_r]... what about your first t-time?"
            nana "How did y-you do it?"
        else:
            nana "But Mr. [mc_name]... about that first t-time..."
            nana "How did it h-happen?"
        show ep04_anto_memory03
        mc_s "Hmmm... That day... Well..."
        mc_s "She was nervous... it was her first time too. Even though she acted tough and mature..."
        nana "And then?..."
        show ep04_anto_memory04 at ken_burns_top_to_bottom
        mc_s "She couldn't take her eyes off me... just kept staring..."
        nana "And after that...?"
        show ep04_anto_memory05
        hide ep04_nanakitdrunk01
        mc_s "If I remember correctly, she kept saying 'This wasn't supposed to happen', or 'I shouldn't be here right now...' or something like that."
        mc_s "But it was like her mind was telling her to stop... But her body and heart wanted me."
        mc_s "The way she looked at me when we started..."

        show ep04_anto_memory06 at ken_burns_right_to_left
        mc_t "Fuck... Just remembering this is getting me hard..."
        mc_s "And well... that's how it happened. The end."
        mc_s "Any other questions?"
        if ep04_nanadad:
            nana "Woahhh! But, y-you didn't t-tell me how--"
        else:
            nana "Oh! But you haven't told me about--"
    else:
        $ playAudio(amber_sad_theme, "music", 1, True, 2.0, 1.0)

        show ep01_amberconfess24 at ken_burns_right_to_left with smoke
        mc_s "No, sweetie, it wasn't her..."
        if ep04_nanadad:
            nana "Oohh, who was it then? Someone from your s-school?"
        else:
            nana "Oh... who was it, Mr. [mc_name]? A classmate perhaps?"
        show ep01_amberconfess33 with smoke
        mc_s "Uhh... Well... Yeah, kinda."
        if ep04_nanadad:
            nana "Was s-she your girlfriend b-back then?"
        else:
            nana "Were you t-together?"
        show ep01_amberconfess34 at ken_burns_bottom_to_top with smoke
        mc_s "... Yeah, kinda again... Well she uhm..."
        mc_s "It's complicated..."
        mc_s "We weren't really dating... just liked spending time together..."
        if ep04_nanadad:
            nana "Woahhh! What did she l-look like? What did s-she like to do?  Was she pretty?"
        else:
            nana "Please tell me more about her, Mr. [mc_name]... Was she beautiful?"
        show ep01_home12 with smoke
        mc_s "I knew her from before. And yeah, she was pretty."
        nana "Tell me more, please!"
        show ep04_amber_remember01 at subtle_zoom_out with smoke
        mc_s "Hmm... okay... She had long hair, blue eyes, and a cute smile. She liked to cook and play videogames with me."
        if ep04_nanadad:
            nana "W-Wowww! That sounds amazing!"
        else:
            nana "That sounds wonderful..."
        if ep04_nanadad:
            nana "How d-did the moment happen? Was i-it after school or something?"
        else:
            nana "How did it... happen? After classes maybe?"
        show ep01_amberconfess06 with smoke
        mc_s "No, we were just hanging out in her room... as we always did."
        if ep04_nanadad:
            nana "Did she ask y-you to do i-it or did y-you ask h-her?"
        else:
            nana "Who... who made the first m-move?"
        hide ep04_nanakitdrunk01
        show ep01_amberconfess38 at ken_burns_top_to_bottom with smoke
        mc_s "Well... we kinda just ended up doing it..."
        nana "But what happened after? Did s-she become your g-girlfriend?"
        mc_s "No, not really... we kept doing it over the next few weeks but that was it."
        if ep04_nanadad:
            nana "Awww... That's so s-sad... It would've been s-sweet if you guys h-had stayed together f-forever."
        else:
            nana "Oh... that's unfortunate... You could have been something special..."
        show ep04_amber_remember02 at ken_burns_left_to_right with smoke
        mc_s "She wasn't looking for a relationship..."
        mc_t "I'm not telling Nanami the whole truth... but now's not the time..."

        show ep04_amber_remember03 at subtle_zoom_in with smoke
        mc_s "Haha... yeah..."
        mc_s "It just wasn't meant to be..."
        nana "Ohhh..."
        nana "So---"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with smoke
    $ setChannelVolume("amb", 1, 0.3, 1.5)

    show ep04_nanakitdrunk01 with smoke
    mc_s "Your beer's getting warm, sweetie. It'll taste awful if you let it sit too long."
    if ep04_nanadad:
        nana "Oh! Sorry d-[daddy_r_low], h-how do I drink i-it? L-like milk?"
    else:
        nana "Oh! Mr. [mc_name], h-how should I... drink this?"
    mc_s "Yeah, just take it slow. Don't force yourself if you don't like it."
    if ep04_nanadad:
        nana "O-okay [daddy_r], t-thank you."
    else:
        nana "I understand, Mr. [mc_name]... thank you..."
    $ playAudio(nanami_chill_theme, "music", 2, True, 2.0, 1.0)

    show ep04_nanakitdrunk02 with vpunch
    if ep04_nanaskimpy:
        mc_t "Damn... That nightgown really can't contain those massive breasts..."
        mc_t "Fuck... They're huge..."
    else:
        mc_t "Those lips... so soft and inviting..."
        mc_t "God... I wish she could wrap those lips around my..."
    mc_t "She's drinking way too fast... She'll be drunk in no time..."
    mc_s "Hey, slow down. Take your time, sweetie."

    show ep04_nanakitdrunk03 with vpunch
    mc_t "Her breasts are incredible... Even bigger than Amber's..."
    mc_t "Damn... She really doesn't know what 'slow' means..."
    mc_s "Nanami, please don't drink it all at once."
    mc_s "Hey... Are you listening? Take a breath!"

    show ep04_nanakitdrunk04 with vpunch
    mc_s "Sweetie...?"
    mc_t "She's like a machine... Has she done this before?"
    mc_t "Something's not right... Is she okay?"
    if ep04_nanadad:
        nana "[daddy_r], i-it tastes weird... but n-not bad!"
        nana "I mean! It's not g-good exactly but... I k-kinda like it!"
    else:
        nana "Mr. [mc_name], it's s-strange... but interesting!"
        nana "I mean... it's not exactly t-tasty but... I think I like it!"
    mc_s "Hahaha, yeah. You'll get used to the taste."
    nana "W-wow... Everything's spinning... Hehehe..."
    mc_s "That's the alcohol kicking in... Better stay still."

    show ep04_nanakitdrunk05
    if ep04_nanadad:
        nana "Hehe... D-[daddy_r_low]... You're s-so handsome..."
        mc_s "Oh yeah? Thanks, honey."
        nana "Do you... Do you think I'm p-pretty?"
        mc_s "...Yeah."
        nana "Just p-pretty? Not... s-sexy?"
        mc_s "Yes... You're sexy too..."
        nana "Wanna know what I'm th-thinking?"
        mc_s "Sure, sweetie."
        nana "I think... you should g-get me another bottle... Hehehe..."
    else:
        nana "Mr. [mc_name]... you're very... attractive..."
        mc_s "Thank you, Nanami."
        nana "Do you... find me attractive too?"
        mc_s "...Yes, I do."
        nana "Just... attractive? Not... d-desirable?"
        mc_s "You're very desirable..."
        nana "May I... tell you something?"
        mc_s "Of course."
        nana "I think... I'd like another drink... Hehe..."
    mc_t "Should I give her another beer? I could get in trouble if someone finds out..."
    if ep04_nanadad:
        nana "I'll be your g-good girl if you get me a-another..."
    else:
        nana "I'll be very well-behaved if you bring me one more..."
    mc_t "But if nobody finds out..."
    if ep04_nanadad:
        nana "Pleeeeeeaseeeeeeee daddyyyyyyyyy?"
    else:
        nana "Please, Mr. [mc_name]... just one more?"
    mc_t "She's already tipsy... She probably won't notice if I stop now."

    $ show_walkthrough("ep04_nanaboozmenu")
    menu:
        "Give her more beer":
            hide screen walkthrough_screen
            if ep04_nanadad:
                mc_s "Alright sweetie. But just one more, ok?"

                show ep04_nanakitdrunk06 with normalfade
                $ rm.update("nanami", "cor", 1)
                $ check_levels("nanami", "cor", 1)
                nana "C-can you give me more? J-just 2 more please?!"
                nana "Pleeeeaaaaaseeeee [daddy_r_low]! J-just 2, p-pinky promise!"
                nana "I-I won't drink them all at once! P-promise!"
                mc_s "...Hmmmm... I don't know if that's a good idea..."
                nana "Just t-two please?!"
                mc_s "Alright... Two more."
                nana "Thank y-you [daddy_r_low]! Y-you're the best!"
            else:
                mc_s "Fine. One more, but that's it."

                show ep04_nanakitdrunk06 with normalfade
                $ rm.update("nanami", "cor", 1)
                $ check_levels("nanami", "cor", 1)
                nana "Mr. [mc_name]... c-could I maybe have... two more?"
                nana "Please, Mr. [mc_name]! I p-promise to be careful!"
                nana "I'll drink them s-slowly this time! Really!"
                mc_s "...Hmmmm... That might not be wise..."
                nana "Just... just two more? Please?"
                mc_s "...Alright. Two more."
                nana "Thank you so much, Mr. [mc_name]! You're so kind!"
            #only way to see isabella mast
            $ setAllSubchannelsVolume("amb", 0, 1.0)
            jump ep04_nanamorebooze


        "Better stop now":
            hide screen walkthrough_screen
            #only way to dream heaven and hell
            $ ep04_mcdrunk = True

            mc_s "Sweetie, that's enough."
            if not ep04_nanakiss:
                $ ep04_nanakiss = True
            jump ep04_nana_nobooze




label ep04_nana_nobooze:
    $ stopAllSubchannels("music", 2.0)

    show ep04_nanakitmilk13 with normalfade
    if ep04_nanadad:
        nana "What? No! Why not, [daddy_r]?"
        mc_s "One is plenty for now."
        nana "B-but [daddy_r]! That's not fair!"
        mc_s "Nanami, try to understand..."
        nana "Just one m-more! Please?"
        nana "I can take it! I p-promise!"
    else:
        nana "Oh... but why not, Mr. [mc_name]?"
        mc_s "One is enough for now."
        nana "But... that's not fair..."
        mc_s "Please try to understand, Nanami..."
        nana "Just... one more? Please?"
        nana "I can handle it... I'm sure..."
    mc_s "No, sweetie. You've had enough."
    nana "But... Please..."
    mc_s "I said NO."

    show ep04_nanakitkiss01
    if ep04_nanadad:
        nana "You're being m-mean, [daddy_r]!"
    else:
        nana "You're not being very n-nice, Mr. [mc_name]..."
    mc_s "Listen... You'll feel awful tomorrow if you drink more."
    mc_s "I'm looking out for you."
    if ep04_nanadad:
        nana "B-but [daddy_r]!"
        nana "It didn't taste g-good but... it made me feel nice..."
    else:
        nana "But Mr. [mc_name]..."
        nana "The taste wasn't great but... I liked how it made me feel..."
    mc_s "Trust me on this. Let's stop here, okay?"
    nana "If you won't give me another... then..."
    nana "I want something else..."
    mc_s "What's that?"

    $ playAudio(nanami_love_theme, "music", 3, True, 2.0, 1.0)

    show ep04_nanakitkiss02 at slow_reveal with normalfade
    nana "...Kiss me..."
    if ep04_nanadad:
        nana "Then maybe... I'll f-forgive you... hehehehe..."
    else:
        nana "Then perhaps... I won't be upset... hehe..."
    mc_s "What? Kiss you?"
    if ep04_nanadad:
        nana "Y-yes please... K-kiss me and I'll stop asking for more..."
    else:
        nana "Please... if you kiss me, I won't ask for more drinks..."
    show ep04_nanakitkiss03 at subtle_zoom_out with normalfade
    if ep04_nanadad:
        nana "K-kiss me D-[daddy_r_low]..."
    else:
        nana "Please... kiss me, Mr. [mc_name]..."
    mc_s "...Are you sure?"
    nana "I n-need it... Please..."
    menu:
        "Kiss her":
            pass
    show ep04_nanakitkiss04
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_kiss_nana, "sfx", 1, False, 0, 0)
    nana "Mmmmm..."
    nana "Mmmmmmmmmmmmm..."
    nana "Mmm..."
    show ep04_nanakitkiss05
    nana "Hahhh... That was... what I needed..."
    if ep04_nanadad:
        nana "Better than b-beer, right [daddy_r]?"
    else:
        nana "Much better than the drink... isn't it?"
    mc_s "I never expected this from such a shy girl."

    show ep04_nanakitkiss06 with normalfade
    nana "Oh! S-shy?"
    if ep04_nanadad:
        nana "Not shy anymore... Hehehehe."
        mc_t "This is unexpected. Will she always be like this when drinking?"
        nana "Kiss me again, [daddy_r]... Don't make me beg..."
    else:
        nana "The drink made me... braver... Hehe."
        mc_t "This is surprising. Is this what alcohol does to her?"
        nana "Please... kiss me again, Mr. [mc_name]..."
    menu:
        "Kiss her again":
            pass
    show ep04_nanakitmorekiss01 with vpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
    $ playAudio(sfx_kiss_op_isa, "sfx", 2, False, 0, 0)
    nana "Mmmmmm..."
    mc_t "She's full of surprises..."

    show ep04_nanakitmorekiss04
    nana "...Mmmmh... Mmmgh.... Mmmmmm..."
    mc_t "Damn... She's so eager... Like she's been starving for this."
    mc_t "Incredible... She's completely different..."
    nana "Mmmmh... Mmmm... Mmmgh!"
    $ stopAllSubchannels("sfx", 1.0)

    show ep04_nanakitmorekiss08 with normalfade
    mc_t "I need to explore this side of her more... It's too tempting..."
    mc_t "Did she use the beer as an excuse? She seems to know exactly what she wants..."
    if ep04_nanadad:
        mc_s "Is this how my innocent little girl acts when she's tipsy?"
        nana "Hahaha, maybeeee..."
    else:
        mc_s "Who knew you had this side to you?"
        nana "Hehe... the drink helped..."
    show ep04_nanakitmorekiss06 with normalfade
    if ep04_nanadad:
        nana "You liked it... didn't you, [daddy_r]?"
        nana "You tasted me... licked me... enjoyed it..."
        nana "Want to make it more interesting, D-[daddy_r_low]? Hehehehe..."
    else:
        nana "Did you... enjoy it, Mr. [mc_name]?"
        nana "The way you tasted me... the way you kissed..."
        nana "We could... do more... Hehe..."
    show ep04_nanakitmorekiss07
    if ep04_nanadad:
        nana "Too bad I'm not drunk enough... If I was, maybe I'd let you..."
        nana "...Let you..."
        nana "Do things to me... Things a [daddy_r] shouldn't do with his little girl... Hahaha..."
    else:
        nana "If I'd had more to drink... maybe we could..."
        nana "...We could..."
        nana "Do things we shouldn't... Things that would be... inappropriate... Hehe..."
    mc_s "Oh... Damn..."

    show ep04_nanakitkiss07 with normalfade
    if ep04_nanadad:
        nana "Good night, D-[daddy_r_low]!"
    else:
        nana "Good night, Mr. [mc_name]..."
    mc_t "She's something else entirely..."
    mc_t "Maybe I should have given her that second drink..."
    mc_t "Whatever... Time for bed... Hope this night doesn't haunt my dreams."

    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_isabella_mcroom




label ep04_nanamorebooze:
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)

    show ep04_nanakitdrunk07 with circlewipe
    mc_t "Wow... This girl can really drink..."
    if ep04_nanadad:
        nana "D-[daddy_r_low]! Everything feels so... floaty! Like I'm a j-jellyfish! Hehehe..."
        nana "A floating j-jellyfish!"
    else:
        nana "Mr. [mc_name]! Everything's so... weird! Like I'm floating! Hehehe..."
        nana "Like a j-jellyfish!"
    mc_s "Maybe we should stop here, sweetie?"
    if ep04_nanadad:
        nana "Noooooo! More d-drinks, [daddy_r]!"
    else:
        nana "But... but I don't want to stop yet!"
    mc_s "Come on, it's not good to drink this much..."
    if ep04_nanadad:
        nana "Then... if you won't give me more... you have to give me a m-massage!"
        mc_s "A massage? Where did that come from?"
        nana "If you're not gonna be fun... at least make me feel g-good, [daddy_r]!"
    else:
        nana "Then... um... could you maybe... give me a massage instead?"
        mc_s "A massage? That's unexpected."
        nana "Please, Mr. [mc_name]? It would feel so nice..."
    mc_s "Alright, if that's what you want..."

    show ep04_nanakitdrunk08 with normalfade
    nana "Aaaaaaahhhh... that feels amazing..."
    mc_s "You like that?"
    nana "Yes... please don't stop..."
    scene eigengrau with slowfade
    show ep04_nanakitdrunk09 with hpunch
    mc_s "Hey! That's my beer!"
    mc_t "Did she just...?"
    if ep04_nanadad:
        nana "Hahahahaha, oopsie! Was it yours, D-[daddy_r_low]? My bad!"
    else:
        nana "Hehehe... sorry, Mr. [mc_name]! Couldn't help myself!"
    mc_s "We really should stop drinking now..."
    if ep04_nanadad:
        nana "No way! This is too much fun!"
    else:
        nana "But... I'm enjoying myself so much..."
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_bodydrop_ontable, "sfx", 3, False, 0, 0)

    show ep04_nanakitdrunk10 with vpunch
    mc_t "She's completely drunk..."
    nana "Mhmmmm... my head's spinning..."
    mc_s "I warned you about drinking too much..."

    show ep04_nanakitdrunk11 with vpunch
    if ep04_nanadad:
        nana "Owww [daddy_r]... my head really hurts! Can we go to my room?"
    else:
        nana "Everything's spinning... Mr. [mc_name], could we go to my room?"
    nana "Please?"
    mc_s "You mean Madison's room?"
    nana "Y-yeah..."
    mc_t "If Madison sees her like this, I'm dead..."
    if ep04_nanadad:
        nana "Please [daddy_r]? Can we go?"
    else:
        nana "Please, Mr. [mc_name]?"
    mc_s "I don't think that's a good idea right now."
    if ep04_nanadad:
        nana "Then... can we go to your room, [daddy_r]?"
    else:
        nana "What about... your room then?"
    mc_t "Better than Madison's room... Maybe she can sober up there for a bit..."
    mc_s "Alright, we can go to my room."

    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 4, False, 0, 0)

    show ep04_nanakitdrunk12 with vpunch
    nana "Yayyy!!"
    mc_s "Wait... what happened to your headache?"
    if ep04_nanadad:
        nana "It's still there, [daddy_r]! Really!"
    else:
        nana "It still hurts, Mr. [mc_name]! Honest!"
    mc_s "Funny how it seemed to improve when I mentioned my room..."
    if ep04_nanadad:
        nana "You're silly, [daddy_r]! It really hurts! Let's hurry!"
    else:
        nana "Don't be mean... my head's spinning! Can we go?"
    mc_s "If you say so..."

    scene eigengrau with slowfade
    show ep04_nanakitdrunk13 at ken_burns_left_to_right
    mc_t "Something's not adding up here... Is she really this drunk or is she putting on an act?"
    mc_t "Isabella did warn me about this... said she wasn't really the innocent girl she pretends to be..."
    mc_t "But then again, she's clearly tipsy... Unless she's using that as an excuse to..."
    mc_t "Damn, what if she planned this from the start? Get 'drunk' to have an excuse to come to my room?"
    mc_t "Or maybe I'm just being paranoid and she's genuinely drunk... Fuck, I can't tell anymore."
    if ep04_nanadad:
        nana "...love how your hands feel on me..."
    else:
        nana "...your touch feels so nice..."
    mc_s "What was that?"
    if ep04_nanadad:
        nana "Nothing, [daddy_r]! Come on, let's go!"
    else:
        nana "Oh! N-nothing, Mr. [mc_name]! Shall we?"
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_nanadrunkmcroom




label ep04_nanadrunkmcroom:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)

    show ep04_nanamcroom01 at ken_burns_top_to_bottom with circlewipe
    if ep04_nanadad:
        nana "T-thanks for bringing m-me here, [daddy_r]!"
    else:
        nana "Thank you for h-helping me, Mr. [mc_name]..."
    mc_s "Of course, sweetie."
    mc_t "Fuck... Her breasts are pressed right against me..."
    mc_s "Would you like to lie down for a bit?"
    if ep04_nanadad:
        nana "Yes please... My head's s-spinning so much..."
        nana "You'll stay with me, right [daddy_r]? Until I fall asleep?"
    else:
        nana "Please... Everything's so d-dizzy..."
        nana "Would you... stay with me for a while, Mr. [mc_name]?"
    mc_s "I don't know if that's the best idea..."
    mc_s "Here, sit on the bed for a moment..."

    $ setChannelVolume("sfx", 1, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom02 with normalfade
    if ep04_nanadad:
        nana "...[daddy_r]... Maybe I should... go to Madison's room instead..."
        nana "If she f-finds us here together... We're both d-dead..."
    else:
        nana "...Mr. [mc_name]... Perhaps I should return to Madison's..."
        nana "If she sees me here... She'll be so angry..."
    mc_s "But you're the one who wanted to come here. And you insisted on more drinks!"
    if ep04_nanadad:
        nana "But... you're the grown up, [daddy_r]! You should've stopped me!"
    else:
        nana "Yes, but... you're supposed to be responsible one, Mr. [mc_name]..."
    mc_t "She has a point..."
    mc_s "Maybe you're right, but..."

    show ep04_nanamcroom03
    nana "Everything's... spinning..."
    mc_t "Shit... She's completely wasted..."
    nana "And I'm so... thirsty..."
    mc_s "No more alcohol, sweetie."
    if ep04_nanadad:
        nana "No, [daddy_r]! Just water... please?"
        nana "The kitchen's so far... and my head hurts..."
    else:
        nana "Just water, Mr. [mc_name]... please?"
        nana "I can't walk to the kitchen like this..."
    mc_t "At least she's not asking for more beer..."
    mc_s "Okay, wait here. I'll get you some water."

    $ setAllSubchannelsVolume("amb", 0, 1.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setAllSubchannelsVolume("amb", 0.3, 1.0)

    show ep04_nanamcroom04 at ken_burns_corner_to_corner with circlewipe
    mc_t "Already passed out? I was gone for like two minutes..."
    mc_t "That position can't be good for her neck..."

    show ep04_nanamcroom05 at subtle_zoom_in
    mc_t "And she's still wearing her glasses..."
    mc_t "This isn't good... If I wake her, she might not get back to sleep."
    mc_t "But leaving her like this... She could get sick, or worse, choke if she throws up..."

    $ show_walkthrough("ep04_nanadrumcmenu")
    menu:
        "Wake her up":
            hide screen walkthrough_screen

            mc_t "Better wake her up... At least then I'll know she's okay."
            if ep04_nanadad:
                mc_s "Hey sweetie... Wake up... Let's get you properly on the bed."
            else:
                mc_s "Nanami... Wake up... You shouldn't sleep like this."

            jump ep04_nanadrunkawake


        "Let her sleep":
            hide screen walkthrough_screen
            $ ep04_nanastay = True

            mc_t "No... Maybe I should just let her rest..."
            mc_t "She's probably fine sleeping like this... What's the worst that could happen?"
            if ep04_nanadad:
                mc_t "Good night, princess..."
            else:
                mc_t "Sleep well, Nanami..."

            $ stopAllSubchannels("amb", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 1, 1, 0)
            $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
            pause 0.5
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1.0
            jump ep04_elimeet_intro




label ep04_nanadrunkawake:
    show ep04_nanamcroom06 with hpunch
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_surprisenana, "sfx", 1, False, 0, 0)
    if ep04_nanadad:
        nana "...Hmmmm... D-[daddy_r_low]?"
    else:
        nana "...Hmmmm... Mr. [mc_name]?"
    mc_s "Come on honey... Get your head on the pillow. You'll thank me in the morning..."
    mc_t "Wait a minute... Are those her bare shoulders under the sheet?"
    if ep04_nanadad:
        nana "...Why're you being so serious, [daddy_r]?"
    else:
        nana "...Why so concerned, Mr. [mc_name]?"
    mc_s "Just in case anything happens. I don't want you feeling worse tomorrow."
    nana "Hahahaha d-[daddy_r_low]! T-that's so s-stupid... W-what do y-you mean with... something h-happening?"
    mc_s "I'm serious. Please, just get comfortable on the bed..."

    $ playAudio(nanami_secure_theme, "music", 1, True, 2.0, 1.0)

    show ep04_nanamcroom07
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    if ep04_nanadad:
        nana "Like this, [daddy_r]...?"
    else:
        nana "Is this better...?"
    mc_t "Fuck... She's completely topless under there..."
    mc_s "Sweetie... Where are your clothes?"
    nana "These aren't clothes...? The sheets?"
    mc_s "No, I mean what you were wearing before..."

    show ep04_nanamcroom08
    if ep04_nanadad:
        nana "Ohhh... they were too hot, [daddy_r]... Everything feels so warm..."
        mc_s "They were too hot?"
        nana "Mhm... while you were getting water... I just had to take them off..."
    else:
        nana "It was getting so warm... I couldn't help myself..."
        mc_s "You took them off?"
        nana "While you were gone... I just needed to cool down..."
    mc_s "I... see..."

    show ep04_nanamcroom09 with vpunch
    mc_t "The way she's moving... Is this really the same shy girl from before?"
    if ep04_nanadad:
        nana "[daddy_r]... do you feel warm too?"
    else:
        nana "It's still so hot in here... don't you think?"
    mc_s "I... uhm..."

    show ep04_nanamcroom10 with hpunch
    if ep04_nanadad:
        nana "My whole body feels like it's burning up, [daddy_r]..."
        nana "Maybe... you could help cool me down?"
    else:
        nana "Everything's so... hot... Mr. [mc_name]..."
        nana "Would you... help me feel better?"
    mc_t "Shit... This is too much..."
    nana "You know... Madison says something about that..."
    show ep04_nanamcroom11
    mc_s "...Madison?"
    if ep04_nanadad:
        nana "[daddy_r]... when you kiss someone... does it make the heat go away, like Madison says?"
        nana "Could you... show me?"
    else:
        nana "Madison says... a kiss can make everything better..."
        nana "Would you... try it?"
    mc_t "This is so wrong on so many levels... She's my [si_full_r_low]'s best friend, she's wasted, and she's just..."
    if ep04_nanadad:
        nana "So? What do you say, [daddy_r]?"
    else:
        nana "Uhm... Wanna try me, Mr. [mc_name]?"
    $ show_walkthrough("ep04_nanadrumcmenu_2")
    menu:
        mc_t "There's no going back now..."
        "Give her a peck":
            hide screen walkthrough_screen
            show ep04_nanamcroom12 at subtle_zoom_in with hpunch
            $ rm.update("nanami", "trust", 1)
            $ check_levels("nanami", "trust", 1)
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
            $ playAudio(sfx_kiss_nana, "sfx", 1, False, 0, 0)
            if ep04_nanadad:
                mc_t "Her lips are so incredibly soft... Maybe I should stop here..."
                nana "Mhmmmm... [daddy_r]..."
            else:
                mc_t "Such soft lips... Better not take this further..."
                nana "Mhmmmm... Mr. [mc_name]..."
        "French kiss her":
            hide screen walkthrough_screen
            show ep04_nanamcroom12 at subtle_zoom_in with hpunch
            $ rm.update("nanami", "trust", 2)
            $ check_levels("nanami", "trust", 2)
            $ setChannelVolume(channel="sfx", subchannel=2, volume=0.7)
            $ playAudio(sfx_kiss_op_isa, "sfx", 2, False, 0, 0)

            mc_t "God... those plump, inviting lips..."
            mc_t "Better start slow... tease her a little..."
            if ep04_nanadad:
                nana "Mhmmmm... yes, [daddy_r]..."
            else:
                nana "Mhmmmm... please..."
            mc_t "Time to deepen the kiss..."

            show ep04_nanamcroom13 at subtle_zoom_out
            nana "Mhhm? Hnnngh... mmmm..."
            mc_t "She's really into this..."
            nana "Nnhhh..."
            mc_t "Her tongue is so hot against mine..."
            if ep04_nanadad:
                nana "Hahhh... [daddy_r]... mnnnn..."
            else:
                nana "Hahhh... mnnnn... more..."
            $ stopAllSubchannels("sfx", 1.0)

    show ep04_nanamcroom14 with hpunch
    mc_s "How are you feeling now, sweetie?"
    if ep04_nanadad:
        nana "Better, [daddy_r]..."
        mc_s "Is your headache gone?"
        nana "My head doesn't hurt anymore but..."
        nana "My heart's beating so fast, [daddy_r]..."
    else:
        nana "Better, Mr. [mc_name]..."
        mc_s "Has your headache improved?"
        nana "The pain is gone but..."
        nana "My heart won't stop racing..."
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom15
    if ep04_nanadad:
        nana "Hehehe! Everything feels tingly, [daddy_r]!"
        mc_s "You're really drunk, aren't you?"
        nana "Don't tease meeeee!"
        nana "Come closer, [daddy_r]..."
    else:
        nana "Hehehe! I feel so strange..."
        mc_s "The alcohol's really hitting you, huh?"
        nana "Don't make fun of me..."
        nana "Please... come here..."
    mc_s "...Sweetie?"

    show ep04_nanamcroom16 at subtle_zoom_out with normalfade
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_shortmakeout, "sfx", 2, False, 0, 0)
    nana "Mhmmmngh... Mmmhmnnnghm..."
    mc_t "She's kissing me like she's starving..."
    if ep04_nanadad:
        mc_s "Easy there, babygirl. We have time."
        nana "Hehehehe... [daddy_r]... Your kisses are amazing..."
        nana "More please, [daddy_r]..."
    else:
        mc_s "Slow down, sweetie. Take your time."
        nana "Mmm... you're so good at this..."
        nana "Please... don't stop..."
    $ stopAllSubchannels("sfx", 1.0)
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom17 at ken_burns_top_to_bottom with normalfade
    nana "Mhmmmngh... Mmmhmnnnghm..."
    mc_t "She's completely different from before..."
    if ep04_nanadad:
        nana "[daddy_r]! Why'd you stop? Don't be mean!"
    else:
        nana "Why are you stopping? Please..."
    show ep04_nanamcroom18 with normalfade
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_shortmakeout, "sfx", 2, False, 0, 0)
    nana "Mhmmmngh... Mmmhmnnnghm..."
    nana "Nhhmmmm... mhmhhhmnmmmhmm..."
    nana "Hmmm..."
    if ep04_nanadad:
        nana "[daddy_r]... it feels incredible..."
    else:
        nana "This feels... amazing..."
    $ stopAllSubchannels("sfx", 1.0)
    $ show_walkthrough("ep04_nanadruawaksmenu")
    menu:
        mc_s "What if I try here...?"
        "Suck her tits":
            hide screen walkthrough_screen
            show ep04_nanamcroom19 at ken_burns_left_to_right
            $ ep04_nanakiss_breasts = True
            if ep04_nanadad:
                nana "Haaahhh! [daddy_r]!"
                nana "Ahhhhnghhh!!"
                mc_s "Does that feel good, baby?"
                nana "Y-Yes... D-[daddy_r_low]... Don't stop!"
            else:
                nana "Haaahhh! Oh god..."
                nana "Ahhhhnghhh!!"
                mc_s "You like that?"
                nana "Please... keep going!"
            nana "Hahh, hahhhh... ahhhhh..."
        "Go down on her":
            hide screen walkthrough_screen
            if ep04_nanadad:
                nana "Wait, [daddy_r]! Not yet!"
            else:
                nana "Please wait! I'm not ready!"
    show ep04_nanamcroom20 at ken_burns_bottom_to_top with normalfade
    if ep04_nanakiss_breasts:
        if ep04_nanadad:
            nana "Haah, hahhh... That was incredible, [daddy_r]! Like electricity through my whole body!"
        else:
            nana "Haah, hahhh... That felt amazing... I've never felt anything like it!"
        mc_s "...And what about if I try down here...?"
    else:
        mc_s "...What about if I try down here...?"

    show ep04_nanamcroom21
    if ep04_nanadad:
        nana "Ahhhnngh!... [daddy_r]... Wait, please..."
    else:
        nana "Ahhhnngh!... Please, just a moment..."
    show ep04_nanamcroom21b
    if ep04_nanadad:
        nana "Look how wet I am, [daddy_r]... It's so embarrassing..."
        mc_t "So pink and glistening..."
    else:
        nana "I'm so wet... This is so embarrassing..."
        mc_t "She's perfect..."

    show ep04_anim_nana05
    if ep04_nanadad:
        nana "It's all sticky... You probably don't want to touch it..."
        nana "Even my... my other hole is twitching..."
    else:
        nana "Everything's so sticky... You must think it's gross..."
        nana "My whole body is reacting..."
    if ep04_nanadad:
        nana "Ahh! My body's moving by itself! I can't help it! It's so embarrassing..."
        nana "I've never shown anyone before... I'm sorry, [daddy_r]! Your little girl is such a mess..."
    else:
        nana "Ahh! I can't control it! This is so shameful..."
        nana "Nobody's ever seen me like this... I'm sorry... I'm such a mess..."
    nana "Hngh... Hahhh... hahhh... ahhhhh!"
    nana "What's happening to me!? Everything's tingling...!"
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

    show ep04_nanamcroom22 at subtle_zoom_out with vpunch
    $ setChannelVolume("sfx", 4, 0.7, 0)
    $ playAudio(sfx_surprisenana, "sfx", 4, False, 0, 0)

    mc_s "Are you okay, sweetie?"

    $ stopAllSubchannels("music", 2.0)
    if ep04_nanadad:
        nana "D-[daddy_r_low]... That felt incredible... But... I'm so embarrassed..."
        mc_s "Embarrassed? You sounded beautiful, baby."
    else:
        nana "That was... amazing... But... I feel so shy..."
        mc_s "Don't be. You were perfect."
    mc_s "Do you want to stop?"
    mc_s "Don't be embarrassed... It's just us here. Everything's okay."

    show ep04_nanamcroom23 at ken_burns_top_to_bottom
    if ep04_nanadad:
        nana "But [daddy_r]... What if someone finds out?"
        mc_s "Nobody will know, honey. Just us."
        nana "... You promise?"
        mc_s "I promise."
        nana "O-okay [daddy_r]..."
    else:
        nana "But... what if someone discovers us?"
        mc_s "This stays between us."
        nana "... Really?"
        mc_s "You have my word."
        nana "A-alright..."
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

    show ep04_nanamcroom24 at ken_burns_bottom_to_top with vpunch
    if ep04_nanadad:
        nana "[daddy_r]... I have an idea."
        nana "Sometimes I see these videos in Madison's room, when she thinks I'm not around..."
        nana "The girls get kissed everywhere, and they seem to love it."
        nana "I want to know where I like it most... Could we play a game?"
        nana "You could kiss me wherever you want, and I'll tell you if it feels good..."
        nana "Is that okay to ask, D-[daddy_r_low]?"
        mc_s "And what do I get if I win?"
        nana "W-win?"
        mc_s "Well, if it's a game, there should be prizes, right?"
        nana "...Hmmmm..."
        nana "If you win... I'll stay here tonight..."
        nana "But if you l-lose... I go back to Madison's..."
        mc_s "How do I win?"
        nana "You have to make me feel... special. If you can't... I win!"
        mc_s "Sounds easy enough."
        nana "Don't be so sure, [daddy_r]! You'll have to try lots of places..."
    else:
        nana "I... I sometimes see these videos Madison watches..."
        nana "The girls seem to love being kissed all over..."
        nana "Maybe we could try that? Like a game... to find my sensitive spots..."
        nana "Would that be okay?"
        mc_s "What's the prize if I win?"
        nana "Oh! Um..."
        mc_s "Every game needs stakes, right?"
        nana "...Well..."
        nana "If you win... I stay here tonight..."
        nana "If you lose... I return to Madison's..."
        mc_s "And how do I win?"
        nana "Make me feel... something special. If you can't... then I win!"
        mc_s "Doesn't sound too hard."
        nana "Don't be so confident! You'll have to try a lot..."
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(nanami_chill_theme, "music", 1, True, 4, 0)
    nana "So, where would you start kissing me?"
    $ show_walkthrough("ep04_nanagamesmenu")
    menu nanami_choice_menu:
        "Her neck" if not ep04_neck_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 2:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed


            else:
                $ ep04_neck_completed = True

                show ep04_nanamcroom26 at ken_burns_top_to_bottom with normalfade
                if ep04_nanadad:
                    nana "Hehehe! It tickles, D-[daddy_r_low]! But... it feels so good!"
                    nana "More... try another spot!"
                else:
                    nana "That tickles! But... don't stop..."
                    nana "Please... somewhere else now..."
                jump ep04_nanami_next_choice


        "Her shoulders" if not ep04_shoulders_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 3:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed


            else:
                $ ep04_shoulders_completed = True

                show ep04_nanamcroom28 at ken_burns_left_to_right with normalfade
                if ep04_nanadad:
                    nana "Hahhhm! Your lips are magical, [daddy_r]!"
                    nana "Please... I need more!"
                else:
                    nana "Hahhhm! That feels incredible..."
                    nana "Don't stop... please..."
                jump ep04_nanami_next_choice


        "Her mouth" if not ep04_mouth_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 1:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed


            else:
                $ ep04_mouth_completed = True

                show ep04_nanamcroom25 at subtle_zoom_out with normalfade
                nana "Hmmhmmm..."
                if ep04_nanadad:
                    nana "T-that was perfect, D-[daddy_r_low]... Mmmh..."
                    nana "Try s-somewhere else now..."
                else:
                    nana "That felt wonderful... Mmmh..."
                    nana "Please... k-kiss me somewhere else..."
                jump ep04_nanami_next_choice


        "Her breasts" if not ep04_breasts_completed:
            $ ep04_nanagame += 1
            if ep04_nanagame != 4:
                $ ep04_nanagame = 0
                jump ep04_nanami_sequence_failed


            else:
                $ ep04_breasts_completed = True

                show ep04_nanamcroom27 at subtle_zoom_in with normalfade
                if ep04_nanadad:
                    nana "Ahhhh! Oh g-god, [daddy_r]... that's perfect!"
                    nana "You're... you're so good at this..."
                else:
                    nana "Ahhhh! That's... that's amazing..."
                    nana "You really know what you're doing..."
                jump ep04_nanami_success_path




label ep04_nanami_next_choice:
    if ep04_neck_completed and ep04_shoulders_completed and ep04_mouth_completed and ep04_breasts_completed:
        jump ep04_nanami_success_path


    else:
        jump nanami_choice_menu




label ep04_nanami_success_path:
    hide screen walkthrough_screen
    show ep04_nanamcroom30 with hpunch
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    if ep04_nanadad:
        nana "Yayyyyyy!!! [daddy_r] wins!!"
        mc_s "That's right, baby girl. [daddy_r] knows just what you like."
    else:
        nana "Yayyyyyy!!! You won!!"
        mc_s "I did promise to make you feel good..."
    mc_t "God... she's absolutely adorable..."

    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom29 at ken_burns_top_to_bottom with vpunch
    if ep04_nanadad:
        nana "D-[daddy_r_low]... it's too intense... my whole body's tingling!"
    else:
        nana "It's... it's too much... I'm burning up!"
    mc_t "She acts so innocent... but look how her body responds..."
    mc_t "That perfect pussy... glistening wet..."

    show ep04_nanamcroom34 with vpunch
    if ep04_nanadad:
        nana "[daddy_r]... don't stop... I need your lips on me again..."
        nana "Make your little girl feel good all over, please..."
    else:
        nana "Please... keep going... I need to feel your lips..."
        nana "Make my whole body feel good..."
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

    show ep04_nanamcroom35 at ken_burns_bottom_to_top with hpunch
    $ setChannelVolume("sfx", 4, 0.3, 0)
    $ playAudio(sfx_shortmakeout, "sfx", 4, False, 0, 0)

    mc_t "Her skin is like silk... so warm..."
    if ep04_nanadad:
        nana "[daddy_r]!... More kisses! Please don't stop!"
    else:
        nana "Please... more! Don't stop now!"
    mc_t "God... She's so tiny compared to me..."
    mc_t "She's so small in my arms..."
    nana "Hmmmnngh... mhhm, mhhh..."
    mc_s "Are you sure about this? You're pretty drunk..."
    if ep04_nanadad:
        nana "Yes, [daddy_r]! I need more!"
    else:
        nana "Yes! Please, don't stop!"
    $ stopAudio("sfx", 4, 1)

    show ep04_nanamcroom36
    $ setChannelVolume("sfx", 5, 0.3, 0)
    $ playAudio(sfx_kiss_op_isa, "sfx", 5, False, 0, 0)
    nana "Mmhhmn... I-I can't take it anymore!"
    nana "Hnhhhh..."
    if ep04_nanadad:
        mc_s "You're driving me crazy... so soft, so warm..."
        nana "[daddy_r], please! Touch me, kiss me! Do something!"
    else:
        mc_s "You feel amazing... so soft under my hands..."
        nana "Please! Touch me more! Kiss me! Anything!"
    $ stopAudio("sfx", 5, 1)
    scene eigengrau with slowfade
    show ep04_anim_nana06
    nana "Haaaahhhh! Ahhh!"
    if ep04_nanadad:
        nana "[daddy_r]! That's... that's incredible!"
        mc_s "You taste so sweet, babygirl..."
        nana "More, [daddy_r]! Please!"
    else:
        nana "Oh god! That feels amazing!"
        mc_s "You taste incredible..."
        nana "Please... more!"
    nana "I need to lie down... my head's spinning..."
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    pause 1
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom37 at ken_burns_left_to_right with vpunch
    if ep04_nanadad:
        nana "I want to... spread my legs for you, [daddy_r]... let you k-kiss me... down there..."
        nana "I want to know... how it feels when you... when you kiss me there..."
    else:
        nana "I want to lie back... let you kiss me... everywhere..."
        nana "I need to know... how it feels... down there..."
    show ep04_nanadrunknude01 at subtle_zoom_out with normalfade
    nana "Everything's spinning..."
    mc_s "Don't fall asleep on me now..."
    nana "I won't..."
    nana "...I promise... just... feeling... sleepy..."
    $ stopAllSubchannels("music", 2.0)
    $ show_walkthrough("ep04_nanasucpathmenu")
    menu:
        mc_t "Fuck! She's about to pass out and I'm rock hard... Wake her or let her sleep?"
        "Try to wake her":
            hide screen walkthrough_screen
            # +2x cor @ end label
            jump ep04_nanalicking


        "Let her rest":
            $ ep04_nanastay = True
            hide screen walkthrough_screen
            # +1x love @ end label
            jump ep04_nanacarrybed




label ep04_nanami_sequence_failed:
    hide screen walkthrough_screen
    $ stopAllSubchannels("music", 2.0)

    show ep04_nanamcroom31 at hpunch
    nana "Aahhh... wait, please!"
    mc_s "What's wrong?"
    if ep04_nanadad:
        nana "D-[daddy_r_low], stop! Not there!"
        mc_s "But sweetie, this was your game..."
        nana "I know but... it doesn't feel right there. You're not... it's not the right spot..."
    else:
        nana "Mr. [mc_name], please stop! That spot..."
        mc_s "I thought this was what we agreed to..."
        nana "Yes, but... it's not feeling right there. Maybe... maybe we're doing it wrong..."
    mc_s "Where would you like me to kiss you then?"
    nana "I... I don't know... Maybe we should stop..."
    jump ep04_nanaleave




label ep04_nanacarrybed:
    $ playAudio(nanami_love_theme, "music", 3, True, 2.0, 1.0)

    show ep04_nanasleep02 at ken_burns_right_to_left
    $ rm.update("nanami", "trust", 1)
    $ check_levels("nanami", "trust", 1)

    mc_t "Better stop now... Even if she's driving me crazy..."
    mc_t "God, seeing her naked like this... No!! Focus. She needs to sleep this off."
    mc_t "At least let me get her comfortable on the pillow..."

    show ep04_nanasleep01 at subtle_zoom_out with normalfade
    if ep04_nanadad:
        nana "...[daddy_r]... W-what are... you doing...?"
        mc_s "Just getting you comfortable, princess. You need to rest..."
        mc_s "I'll take the couch in the living room..."
        nana "But... it's your bed, [daddy_r]..."
        mc_t "Even half-asleep, she's still thinking of others..."
        mc_s "Don't worry about me, sweetie. Just get some sleep."
    else:
        nana "...What are... you doing...?"
        mc_s "Getting you to bed, sweetie. You need to sleep..."
        mc_s "I'll take the living room..."
        nana "But... this is your bed..."
        mc_t "She's so considerate, even when she's barely awake..."
        mc_s "It's fine. Just rest."

    jump ep04_nana_sleepbed




label ep04_nana_sleepbed:
    scene eigengrau with normalfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_bedmove2, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom32 at ken_burns_right_to_left with normalfade
    if ep04_nanadad:
        mc_s "Sweet dreams, my little angel..."
    else:
        mc_s "Sleep well, beautiful..."
    mc_t "Real smart, [mc_name]... Now what about this raging hard-on..."

    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 0.5
    show ep04_nanamcroom33 at ken_burns_corner_to_corner with normalfade
    mc_t "Look at her sleeping... so peaceful, so innocent..."
    mc_t "Damn, her naked body under those sheets... No, stop thinking about that."
    mc_t "Did I take advantage of her drunken state? Maybe I should've stopped earlier..."
    if ep04_nanadad:
        mc_t "At least we didn't go too far... Nothing we'll regret when morning comes..."
        mc_t "Even if part of me wishes we had..."
    else:
        mc_t "Better we stopped here... Though part of me wishes we hadn't..."
        mc_t "No, this was the right call."

    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    pause 0.5
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_elimeet_intro




label ep04_nanalicking:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep04_nanadrunknude02 with hpunch
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_sigh_nana, "sfx", 1, False, 0, 0)
    $ rm.update("nanami", "cor", 2)
    $ check_levels("nanami", "cor", 2)
    if ep04_nanadad:
        mc_s "Don't fall asleep yet, babygirl..."
        nana "Mhhm... hmmm... [daddy_r]...?"
        mc_s "Remember what you said earlier..."
        mc_s "About wanting to feel my kisses... down there..."
        mc_s "Do you still want that, honey?"
        nana "...Y-yes... [daddy_r]!... Please..."
    else:
        mc_s "Stay with me a little longer..."
        nana "Mhhm... hmmm... yes...?"
        mc_s "You mentioned wanting to feel more..."
        mc_s "To explore those things you wanted to feel..."
        mc_s "Would you still like that?"
        nana "...Y-yes... Please..."
    mc_s "But first, you need to get your legs in the right position."

    $ playAudio(nanami_chill_theme, "music", 5, True, 2.0, 1.0)

    show ep04_nanadrunkforced01 at subtle_zoom_out with hpunch
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)
    if ep04_nanadad:
        nana "Like... this... D-[daddy_r_low]?"
    else:
        nana "Is this... right...?"
    mc_t "Fuck... Look at that... She's literally offering herself to me right now."
    mc_t "That tight little virgin pussy... AAAAAHHHH, just fuck everything, let's do it!"
    if ep04_nanadad:
        nana "Am I doing it right, [daddy_r]?"
    else:
        nana "Is this how you want me?"
    scene eigengrau
    show ep04_nanadrunknude03 at subtle_zoom_in with normalfade
    mc_s "Just like that, baby..."
    if ep04_nanadad:
        nana "[daddy_r]... Are you sure? Even though..."
        mc_s "What is it, princess?"
        nana "I'm all wet down there... Is that okay?"
        mc_s "That's more than okay, babygirl..."
        nana "You really don't mind?"
    else:
        nana "Are you sure about this? Even though..."
        mc_s "What's wrong?"
        nana "I'm so wet... Isn't that strange?"
        mc_s "That's perfectly normal..."
        nana "You're sure?"
    show ep04_anim_nana08 with slowfade
    $ setChannelVolume("sfx", 3, 0.2, 0)
    $ playAudio(sfx_madbreathxxx, "sfx", 3, False, 0, 0)
    if ep04_nanadad:
        mc_s "Trust [daddy_r], baby. It's perfect."
    else:
        mc_s "Trust me. You're perfect."
    nana "Okay then..."
    nana "J-just be gentle..."
    if ep04_nanadad:
        mc_s "[daddy_r] will take good care of you, princess."
    else:
        mc_s "I'll be very gentle, I promise."
    nana "Ah! Mmmmmm! Ahhhhhh!"
    if ep04_nanadad:
        nana "Uhhhnngg! D-[daddy_r]!... It feels so s-strange!"
        mc_s "Good strange?"
        nana "Hnhhnnn, ahgnnn, uhhnn... it's so embarrassing... Y-your tongue..."
        nana "But... Y-yes... It feels good, [daddy_r]..."
    else:
        nana "Uhhhnngg! That's... that's incredible!"
        mc_s "Does it feel good?"
        nana "Hnhhnnn, ahgnnn, uhhnn... it's embarrassing... Your tongue..."
        nana "But... Y-yes... Don't stop..."
    $ stopAudio("sfx", 3, 1)

    show ep04_anim_nana07
    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_madohxxx, "sfx", 4, False, 0, 0)
    nana "Mhhhmmmmm..."
    nana "Ahghnn! Ahgggnnhhh... Ohh... This is amazing..."
    nana "Ahhh! More! Please don't stop!"
    nana "Ngghhhh! Nnnhhhhhhh... What's happening? Everything's getting so tight!"
    if ep04_nanadad:
        mc_s "You're almost there, baby..."
    else:
        mc_s "Just let it happen..."

    $ stopAudio("sfx", 4, 0.5)

    show ep04_anim_nana09
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_moan_breath2, "sfx", 5, False, 0, 0)
    nana "NGHHHAGHHGHGHHHHH!!! HNNNGGHHH!!"
    nana "I-it h-hurts! Wait! Please!"
    if ep04_nanadad:
        nana "D-[daddy_r], stop! It hurts!"
    else:
        nana "Please stop! It hurts!"
    mc_s "It's okay, just relax..."
    nana "But it hurts!"
    mc_t "Goddamn it, this girl can't make up her mind!"
    if ep04_nanadad:
        mc_s "Baby, it'll feel worse if we stop now..."
        nana "N-no, [daddy_r]! I'm scared! It's too intense!"
    else:
        mc_s "It'll be worse if we stop here..."
        nana "No! I'm scared! It's too much!"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep04_nanadrunkforced02 at subtle_zoom_out with normalfade
    mc_s "Alright... we'll stop."
    nana "Thank you..."
    $ setChannelVolume("sfx", 3, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

    show ep04_nanadrunkforced03 with vpunch
    mc_t "God! She is such a pain in the ass... I'll just let her sleep."
    mc_s "Do you want me to leave, sweetie?"
    mc_t "Great, now she's silent..."
    if ep04_nanadad:
        mc_s "Listen, princess... I'm sorry if I pushed too far. I thought you wanted this but if you're uncomfortable..."
        nana "I'm s-sorry, [daddy_r]..."
    else:
        mc_s "I'm sorry if this was too much. I thought you were ready but if you're uncomfortable..."
        nana "I'm so sorry..."
    $ setChannelVolume("music", 1, 0.5, 1.0) 
    $ playAudio(nanami_innocence_theme, "music", 1, True, 2.0, 1.0)

    show ep04_nanadrunkforced04 at ken_burns_bottom_to_top with vpunch
    $ setChannelVolume("sfx", 4, 0.5, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 4, False, 0, 0)

    mc_s "What's...?"
    if ep04_nanadad:
        nana "[daddy_r]... Please don't be mad at me..."
        mc_s "Baby, don't kneel like that..."
        nana "I disappointed you... I'm not good enough..."
    else:
        nana "Please don't be upset with me..."
        mc_s "You don't need to kneel..."
        nana "I failed you... I couldn't handle it..."
    nana "You made me feel amazing and... my body went crazy... and I got scared... and ashamed..."
    mc_s "Nanami... Please stand up..."

    show ep04_nanadrunkforced05
    nana "I'll do anything for another chance..."
    mc_s "Stop this. You don't need to..."
    nana "But..."
    mc_s "Shhh... It's okay--"
    nana "Let me touch you instead!"
    mc_s "What?"
    if ep04_nanadad:
        nana "Madison explained it to me... I could make you hard again... help with your needs... Please, [daddy_r], let me make it up to you."
    else:
        nana "Madison told me about it... I could help you feel good... Please let me make things right."
    mc_s "You're not listening--"

    show ep04_nanadrunkforced06 at ken_burns_top_to_bottom
    nana "Just put it in my hand!"
    mc_t "Well... I wouldn't mind that, actually."
    mc_t "But all this situation is pretty weird..."
    mc_t "Am I really gonna let a drunk girl jerk me off? [mc_name], you got yourself a new low. Again..."
    if ep04_nanadad:
        nana "Please, [daddy_r]..."
        mc_s "Nanami, just stand up."
    else:
        nana "Please..."
        mc_s "Nanami, that's enough."

    show ep04_nanadrunkforced07
    nana "Not until I make things right..."
    mc_t "What is she--"
    nana "Should I use my mouth instead...? Just tell me what you want..."
    mc_t "Fucking hell, she's so pushy..."

    show ep04_nanadrunkforced08
    mc_s "Enough! Time for bed. You're drunk, and tomorrow's going to be rough. Let's just forget this happened..."
    if ep04_nanadad:
        nana "Did I upset you again, [daddy_r]? What did I do wrong?"
        mc_s "No, princess... That's not it..."
        nana "Then why are you pushing me away? Did I ruin everything?"
    else:
        nana "Are you angry with me? What did I do?"
        mc_s "No, it's not that..."
        nana "Then why won't you let me fix this?"
    mc_t "Oh, god... I can't with this girl."
    mc_s "Just sit down, please."

    jump ep04_nanaleave2




label ep04_nanaleave:
    $ stopAllSubchannels("music", 2.0)

    show ep04_nanadrunkleave01 with normalfade
    if ep04_nanadad:
        nana "[daddy_r] should know the right places..."
        mc_t "She seems really disappointed..."
        mc_s "I do know, baby. But maybe you could guide me?"
        nana "No... we can stop playing..."
        mc_s "Come on! We can't stop now! Tell me where you want to feel my lips..."
    else:
        nana "You should understand where..."
        mc_t "She's genuinely upset..."
        mc_s "I want to understand. Help me learn what you like..."
        nana "Maybe we should just stop..."
        mc_s "We've come this far! Just tell me where you want to be kissed..."

    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_yawnnana, "sfx", 4, False, 0, 0)

    show ep04_nanadrunkleave02
    if ep04_nanadad:
        nana "Mmmm... [daddy_r]... I'm getting so sleepy..."
        nana "Can we continue tomorrow?"
    else:
        nana "I'm... really tired now..."
        nana "Maybe tomorrow..."
    mc_t "Tomorrow? Like she'll remember any of this..."
    mc_t "The alcohol must be really hitting her now..."
    mc_s "Are you falling asleep on me?"
    nana "...Maybe..."
    nana "I should probably go..."
    mc_s "Will you be okay getting back?"
    nana "Don't worry about me..."
    $ show_walkthrough("ep04_nanaleavemenu")
    menu:
        mc_t "I should make sure she's safe for the night..."
        "Ask her to stay":
            hide screen walkthrough_screen
            $ ep04_nanastay = True

            mc_s "Please stay here tonight..."
            # +1x love @ endlabel
            jump ep04_nanaleave_bed


        "Let her go to Madison":
            hide screen walkthrough_screen
            # -1x love @ endlabel
            mc_s "...Alright, sweetie. But if you're not feeling too well, just know that you're welcome to stay the night here."

            jump ep04_nanaleave_hall




label ep04_nanaleave2:
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep04_nanadrunkleave01 with circlewipe
    if ep04_nanadad:
        nana "You must hate me now... Don't y--?"
        mc_s "No, sweetie, that's not--"
        mc_t "How do I explain this to her?"
    else:
        nana "You're disappointed in me... Aren't y--?"
        mc_s "No, please listen--"
        mc_t "This is complicated..."
    mc_s "You're just... you're..."

    $ setChannelVolume("sfx", 4, 0.2, 0)
    $ playAudio(sfx_yawnnana, "sfx", 4, False, 0, 0)

    show ep04_nanadrunkleave02
    if ep04_nanadad:
        nana "I understand, [daddy_r]..."
    else:
        nana "It's okay... I get it..."
    mc_s "Hmmm..?"
    mc_t "She's cute as fuck, but she can be so dense."
    if ep04_nanadad:
        nana "I'm really sleepy now, [daddy_r]..."
        nana "Maybe I should go to Madison's..."
        nana "Goodnight, [daddy_r]..."
    else:
        nana "I'm so tired..."
        nana "I should return to Madison's room..."
        nana "Goodnight, Mr. [mc_name]..."
    $ show_walkthrough("ep04_nanaleave2menu")
    menu:
        mc_t "Should I ask her to stay or what? I'm just too tired for this shit right now..."
        "Ask her to stay":
            hide screen walkthrough_screen

            mc_s "Please stay here tonight..."

            $ ep04_nanastay = True
            # +1x love @ endlabel
            jump ep04_nanaleave_bed


        "Let her go to Madison":
            hide screen walkthrough_screen

            mc_s "Goodnight, honey..."
            # -1x love @ endlabel
            jump ep04_nanaleave_hall




label ep04_nanaleave_bed:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("music",2, 0.3, 1.0)
    $ playAudio(nanami_love_theme, "music", 2, True, 2.0, 1.0)

    show ep04_nanadrunkleave03
    $ rm.update("nanami", "trust", 1)
    $ check_levels("nanami", "trust", 1)
    if ep04_nanadad:
        nana "...Sleep here with you, [daddy_r]?"
        mc_s "No, sweetie! You take the bed, I'll sleep on the couch."
        nana "But Madison... if she finds out..."
        mc_s "We'll just say you weren't feeling well enough to make it to your room."
    else:
        nana "...Stay here?"
        mc_s "You can take the bed. I'll use the couch."
        nana "Madison might get upset..."
        mc_s "We can explain you weren't feeling well enough to walk to your room."

    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

    show ep04_nanasleep03 with hpunch
    if ep04_nanadad:
        nana "Okay [daddy_r]... if you're sure..."
        nana "...[daddy_r]... Before bed... can I have my goodnight kiss?"
    else:
        nana "If you think it's okay..."
        nana "...Before I sleep... could I have a goodnight kiss?"
    show ep04_nanasleep04 with normalfade
    nana "Right here... on my cheek..."
    mc_s "Of course..."

    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

    show ep04_nanasleep05 at ken_burns_right_to_left with hpunch
    mc_t "Sneaky girl... turning to catch my lips instead..."
    nana "Mhmmm...?"
    show ep04_nanasleep06
    $ setChannelVolume("sfx", 3, 0.6, 0)
    $ playAudio(sfx_kiss_nana, "sfx", 3, False, 0, 0)
    nana "Mhmm... Mwah! Mhmhmmmwah..."
    show ep04_nanasleep07
    nana "Mmmmhmmmmm..."
    if ep04_nanadad:
        nana "Hehehehe! Best goodnight kiss ever, [daddy_r]!"
    else:
        nana "Hehehehe! What a perfect goodnight kiss..."
    nana "Now I should slee—"
    show ep04_nanasleep08 at subtle_zoom_in
    mc_s "Such amazing tits..."
    nana "...Hmmmm?"
    if ep04_nanadad:
        nana "...[daddy_r]!! You pervert!"
    else:
        nana "...You're such a pervert!"
    mc_s "Huh?"

    hide ep04_nanasleep08
    mc_s "I-I'm sorry honey, it's just..."
    mc_s "You are so pretty, I couldn't resist staring..."
    if ep04_nanadad:
        nana "Hehehe... It's okay [daddy_r]... but you're still a pervert..."
    else:
        nana "Hehehe... I'll forgive you... this time..."
    show ep04_nanasleep09 with normalfade
    nana "I'm... so... sleepy..."
    mc_s "Rest now, sweetie. You need it."
    if ep04_nanadad:
        mc_t "While I think about those perfect tits..."
        nana "...Thank you... [daddy_r]..."
    else:
        mc_t "While I remember how beautiful she is..."
        nana "...Thank you... for everything..."
    mc_s "Sleep well, sweetie."

    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_bedmove2, "sfx", 1, False, 0, 0)

    show ep04_nanamcroom32 at ken_burns_right_to_left with normalfade
    mc_t "She looks like an angel when she sleeps..."
    mc_t "Maybe I shouldn't feel this way about someone so young..."
    mc_t "I'm definitely going to hell for this..."

    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 0.5
    show ep04_nanamcroom33 at ken_burns_corner_to_corner with normalfade
    mc_t "But if loving her is a sin... then I'll gladly burn..."
    if ep04_nanadad:
        mc_t "Sweet dreams, my little angel..."
    else:
        mc_t "Sleep well, beautiful..."

    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
    pause 0.5
    $ stopAllSubchannels("music", 2.0)
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_elimeet_intro




label ep04_nanaleave_hall:
    show ep04_nanadrunkleave04
    $ rm.update("nanami", "trust", -1)
    $ check_levels("nanami", "trust", -1)
    if ep04_nanadad:
        nana "Don't worry about me, [daddy_r]! I'll be fine!"
    else:
        nana "Please don't worry, Mr. [mc_name]! I can manage!"
    mc_t "She seems disappointed... Maybe I made a mistake not letting her stay..."

    scene eigengrau with slowfade
    show ep04_nanadrunkleave05 with circlewipe
    if ep04_nanadad:
        nana "...Y-you know where to find me if you w-want to play more, [daddy_r]..."
    else:
        nana "...If you want to continue... later... you know where I am..."
    mc_t "Maybe it's better to end the night here..."
    mc_t "But what if she trips? Those stairs could be dangerous in her state..."

    $ show_walkthrough("ep04_nanalehallmenu")
    menu:
        "Walk her to her room":
            hide screen walkthrough_screen
            # +1x love @ endlabel
            if ep04_nanadad:
                mc_s "Wait up, sweetie. Let me walk you to Madison's room."
            else:
                mc_s "Hold on. I'll make sure you get there safely."

            show ep04_nanadrunkleave07 at ken_burns_left_to_right with normalfade
            if ep04_nanadad:
                nana "Thanks for tonight, [daddy_r]! It was the best!"
                mc_s "Anytime, princess."
            else:
                nana "Tonight was wonderful... Thank you for everything..."
                mc_s "Of course, sweetie."

            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1.0
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with slowfade
            $ setChannelVolume(channel="amb", subchannel=3, volume=0.3)
            $ playAudio(sfx_nightsleep, "amb", 3, True, 1.5, 0)

            show ep04_hallmeeting01 at ken_burns_bottom_to_top with circlewipe
            if ep04_nanadad:
                nana "[daddy_r], this was amazing! I'm so happy I met you!..."
                nana "Do you think Madison would be mad if I told her how good tonight was?"
                mc_s "Let's keep this between us, honey. It's our little secret."
                nana "Mmm... y-you're probably right, [daddy_r]."
            else:
                nana "I never thought tonight would be so special..."
                nana "Should... should we tell Madison about this?"
                mc_s "Better keep this just between us."
                nana "Yes... you're right..."
            show ep04_hallmeeting02 with normalfade
            if ep04_nanadad:
                nana "[daddy_r]... Everything's spinning again... Your kisses made it better before..."
                mc_s "Not here, sweetie. It's too risky."
                nana "Just one more?"
                mc_s "We can't, baby. Not right outside Madison's room. Someone might see."
            else:
                nana "I'm feeling dizzy again... Maybe one more kiss would help..."
                mc_s "We shouldn't, not here."
                nana "Please?"
                mc_s "It's too dangerous, right outside Madison's room."

            show ep04_hallmeeting03
            $ rm.update("nanami", "trust", 1)
            $ check_levels("nanami", "trust", 1)
            nana "Aww... well, thank you for everything, [daddy_r]. This was incredible."
            if ep04_nanadad:
                mc_s "Sleep well, sweetie. Good night."
            else:
                mc_t "What? Did she just call me [daddy_r_low]?"
                mc_s "Sleep well, Nanami. Good night."

            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 0.5
            show ep04_hallmeeting04 at ken_burns_left_to_right with circlewipe
            mc_t "What a night..."
            mc_t "Wonder if she'll remember any of this tomorrow..."
            amb "Well, well, well..."
            jump ep04_ambhall


        "Let her go alone":
            hide screen walkthrough_screen
            # -2x love @ endlabel
            if ep04_nanadad:
                mc_s "Okay princess, just be careful on the stairs."
                nana "I will, [daddy_r]! Don't worry about me."
            else:
                mc_s "Alright, just watch your step on the stairs."
                nana "I'll be careful, promise."
            show ep04_nanadrunkleave06  at ken_burns_left_to_right with normalfade
            mc_t "That outfit is so damn sexy..."
            mc_t "I still feel like letting her leave was a bad idea... but it's probably for the best..."

            $ rm.update("nanami", "trust", -2)
            $ check_levels("nanami", "trust", -2)
            $ ep04_afternanami += 1
            scene eigengrau with normalfade
            $ setChannelVolume("sfx", 2, 0.6, 0)
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1.0
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep04_mad_mcroom




label ep04_ambhall:
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(amber_2nd_theme, "music", 1, True, 5.0, 0)
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep04_hallmeeting05 at ken_burns_bottom_to_top
    amb "Look who finally decided to show his face. Having fun with your new fucking toy?"
    mc_s "Huh?"
    amb "Don't play dumb with me. Are you two fucking or what? Because that's what it looked like from where I was standing."
    if ep03_amberstrike or ep03_amberangry:
        show ep04_hallmeeting07 with normalfade
        mc_s "Of course not!"
        amb "Oh, so you can actually keep it in your pants? That's a fucking revelation."
        mc_s "Don't say bullshit."
        amb "Right, because I'm just imagining things. Just like I'm imagining how you look at me when you think I'm not watching."
        mc_s "Why are you saying nonsense things like that?"

        show ep04_hallmeeting09 with normalfade
        amb "You know what? Fuck this. Go chase your precious little princess. That's what you're good at, isn't it?"
        mc_s "Hey... Wait a second!"
        amb "Go to hell, asshole. Sweet fucking dreams."
        mc_t "Fuck, she's still pissed. Well, I hope she'll get over it quickly."

        $ show_walkthrough("ep04_ambhallmenu")
        menu:
            mc_t "I need some distraction from all these things... I could watch TV, or just go directly to my room."
            "Go to the livingroom":
                hide screen walkthrough_screen
                $ ep04_amber_rejects_mc = True
                $ stopAllSubchannels("music", 2.0)
                $ stopAllSubchannels("amb", 2.0)
                jump ep04_elimeet_intro


            "Go to your room":
                hide screen walkthrough_screen
                $ ep04_amber_rejects_mc = True
                $ ep04_afternanami += 2
                $ stopAllSubchannels("music", 2.0)
                $ stopAllSubchannels("amb", 2.0)
                jump ep04_mad_mcroom


    else:
        show ep04_hallmeeting07 with normalfade
        mc_s "What? Are you jealous?"
        amb "Jealous? Don't make me fucking laugh."
        amb "I just want to know if my dear [br_full_r_low] is fucking around with every piece of ass that moves."
        mc_s "Of course not. Why would I fuck my [si_full_r_low]'s best friend?"
        amb "So, why did she call you '[daddy_r_low]' then? What's wrong with your head?"
        mc_s "And what's wrong with your head? She didn't call me that because we're having sex; it was a simple mistake. Don't be paranoid."

        show ep04_hallmeeting06
        amb "Hmph... Okay, I'll pretend to believe you."
        mc_s "Good girl."
        amb "Don't piss me off with your bullshit! And stop smiling like an idiot! You really are an idiot!"
        mc_s "Okay, okay... Sorry, I was just joking. So... Do you want to talk or something?"

        show ep04_hallmeeting08 with normalfade
        amb "What do you think?"
        mc_s "I'm not sure, that's why I asked."
        amb "God, you're dense. Let me spell it out for you - my room, you and me, no talking required. Unless..."
        mc_s "You do realize anyone could hear what you're saying, right?"
        amb "Then we better hurry before they do!"
        mc_s "Okay."  

        $ stopAllSubchannels("music", 2.0)
        $ stopAllSubchannels("amb", 2.0)
        scene eigengrau with normalfade
        $ setChannelVolume("sfx", 2, 0.6, 0)
        $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
        pause 1.0
        jump ep04_ambroom_intro




label ep04_ambroom_intro:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 4, True, 1.5, 0)

    show ep04_ambroom01 at ken_burns_left_to_right with circlewipe
    amb "Welcome to where the magic happens, [br_full_r_low]."
    mc_s "You sure do like leds, don't you?"
    amb "Nah, not too much... it's my viewers who like them."
    mc_s "Viewers? Do you make content with leds on?"

    scene eigengrau with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_changeclothes_nozip, "sfx", 2, False, 0, 0)
    pause 1.5
    show ep04_ambroom02 with normalfade
    amb "Yes, dumbass, do you even know what I do?"
    mc_s "I know what you do, just not the details."
    amb "It doesn't matter how the fuck exactly. Do you have something against leds anyway?"
    mc_s "No, not at all. Leds are great. You just have so many lights in here, it's impressive."

    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(antonella_sexy_theme, "music", 1, True, 5.0, 0)

    show ep04_ambroom03 at ken_burns_bottom_to_top
    amb "Oh? And what do you think is most impressive about this room?"
    mc_s "I already told you... the amount of leds everywhere."
    amb "Fuck, you're such an idiot!"
    mc_s "What?"

    show ep04_ambroom04 with hpunch
    amb "Let me spell it out for you, since you're clearly struggling..."
    amb "What do you think is the most impressive thing in this room right now?"
    $ show_walkthrough("ep04_ambroommenu")
    menu:
        "You?":
            hide screen walkthrough_screen

            mc_s "You?"

            show ep04_ambroom07 at ken_burns_top_to_bottom with vpunch
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            amb "Fucking finally! Someone give this boy a prize."
            amb "So, are you just gonna stand there or what? Why don't you come and play with me?"
            mc_s "I'm listening..."
            amb "No more talking. From now on, you do exactly what I say. Got it?"
            amb "And trust me, big [br_full_r_low]... you're about to get one hell of a private show."
            mc_s "Hmph..."

            $ stopAllSubchannels("music", 2.0)
            $ setChannelVolume("amb", 4, 0, 1.0)
            jump ep04_amber_dancing


        "LEDs?":
            hide screen walkthrough_screen

            mc_s "Um... the amount of leds...?"

            $ ep04_mc_amber_dumb = True
            $ stopAllSubchannels("music", 1.0)
            $ setChannelVolume("sfx", 1, 0.4, 0)
            $ playAudio(sfx_recstop, "sfx", 1, False, 0, 0)

            show ep04_ambroom06 with vpunch
            $ rm.update("amber", "cor", -1)
            $ check_levels("amber", "cor", -1)
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
            amb "UGH! Forget it. You're just an idiot!"
            mc_s "Why are you getting so worked up?"
            amb "Because you're sitting here drooling over some fucking LIGHTS while your [si_full_r_low] is practically throwing herself at you!"
            mc_s "Oh... OH! You were trying to..."

            show ep04_ambroom05 with hpunch
            amb "Get the fuck out! NOW! Before I completely lose it!"
            mc_s "Amber, wait, I didn't mean to-"
            amb "I said GET OUT! Go find someone else to disappoint tonight!"
            mc_s "Alright, I'm going..."

            $ show_walkthrough("ep04_ambroommenu_2")
            menu:
                mc_t "Well, that could have gone better... What now?"
                "Go to the livingroom":
                    hide screen walkthrough_screen
                    $ stopAllSubchannels("amb", 2.0)
                    jump ep04_elimeet_intro


                "Go to your room":
                    hide screen walkthrough_screen
                    $ ep04_afternanami += 3
                    $ stopAllSubchannels("amb", 2.0)
                    jump ep04_mad_mcroom




label ep04_amber_dancing:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 4, 0.3, 1.0)

    show ep04_ambdance01 at ken_burns_left_to_right with normalfade
    amb "Look at you, being all quiet... What's wrong, big [br_full_r_low]? Cat got your tongue?"
    mc_s "Let's just say I've learned when to shut up around women."

    show ep04_ambdance02
    amb "Oh? Finally growing some brains to match that cock of yours?"
    mc_s "Recent experience."
    amb "Mhm... we'll see about that."
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 2.0, 0)

    show ep04_ambdance03
    amb "Aren't you dying to know why your little [si_full_r_low]'s putting on this private show for you?"
    mc_s "Maybe. But I'm learning to enjoy the view without asking too many questions."
    amb "Fuck... when did you get so smooth? Making me wet just listening to you..."
    mc_s "I have my moments."

    show ep04_ambdance04 at ken_burns_right_to_left with vpunch
    amb "Take a good look at what you've been missing all this time. Tell me how bad you want it."
    mc_s "Your body's fucking perfect, Amber. You know that."
    amb "Mmm... I can feel how hard you are through those pants. Your cock never could lie to me..."
    mc_s "Never said I was lying."

    show ep04_ambdance05 at ken_burns_corner_to_corner2
    amb "You like how your [si_full_r_low] smells? How about when I get all hot and bothered like this?"
    mc_s "Fuck... you know I do."
    amb "Bet you'd love to have this scent all over your bed, wouldn't you? Your [si_full_r_low]'s pussy getting your sheets all wet..."
    mc_s "Yeah... fuck..."

    show ep04_ambdance06 at ken_burns_bottom_to_top with normalfade
    amb "Just think... you could've been fucking me senseless whenever you wanted. Your own [si_full_r_low], begging for your cock..."
    mc_s "Amber..."
    amb "Wonder what everyone would think? Finding out you're balls deep in your little [si_full_r_low] every night?"
    mc_s "Shit... yeah..."

    show ep04_ambdance07 at subtle_zoom_out with normalfade
    amb "But you were too blind to see it, weren't you? All this time... I've been right here, waiting..."
    mc_s "Oh, come on, don't start that again..."
    amb "I'll always feel this way... Every time I look at you, I remember all those moments we lost..."
    mc_s "Forget about it. It's not like I'm not here with you right now."

    show ep04_ambdance08 with normalfade
    amb "You're right. You're finally here, as you should have always been."
    amb "Look at what you're making me feel right now, you idiot..."
    mc_s "This is not the best time to talk about this."
    amb "Yeah you're right, it's time to play!"
    mc_s "What?!"

    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 0.9, 0)
    $ playAudio(sfx_changeclothes_zip, "sfx", 1, False, 0, 0)
    pause 2.0
    show ep04_ambdance09 with circlewipe
    amb "No underwear? Naughty big [br_full_r_low]..."
    mc_s "Thought you might appreciate easy access."
    amb "Mmm... someone came prepared for his [si_full_r_low]..."
    jump ep04_amber_tasting_d




label ep04_amber_tasting_d:
    amb "What the fuck? Where'd all that hardness go?"
    mc_s "What do you mean?"
    amb "Don't play dumb. Your cock was rock hard when I was grinding on it. What happened?"
    mc_s "Maybe it has stage fright?"

    show ep04_ambtaste01
    amb "You idiot, this cock knows exactly who I am. We played many times on the past, don't we, buddy?"
    amb "Remember the first time you fucked your [si_full_r_low]?"
    amb "Even with your precious girlfriend waiting at home, you couldn't resist shoving it in me, could you?"
    if ep01_first:
        mc_s "Fuck..."
        amb "Yeah, you love that, don't you? Fuck your own [si_full_r_low], knowing you shouldn't... isn't that just perfect?"
    else:
        mc_s "That's not how it happened!"
        amb "Oh yeah? Then why is your cock getting harder? You fucking love that your [si_full_r_low]'s such a slut for you, don't you?"
    mc_s "Stop talking to my dick..."

    show ep04_ambtaste02
    amb "Look who's back to full attention..."
    mc_s "Shit... you know exactly what you're doing."
    amb "Always have, big [br_full_r_low]..."
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(amber_sexy_theme2, "music", 1, True, 2.0, 0)

    show ep04_ambtaste03
    amb "Such a bad boy... What would everyone in this house think if they knew?"
    mc_s "Amber, cut it out..."
    amb "Don't act like you don't love it. The dirtier it feels, the harder you get. I know you."
    mc_s "Well..."
    amb "That's what I thought."
    amb "Now shut up and let your [si_full_r_low] take care of you!"
    show ep04_ambtaste04
    $ setChannelVolume("sfx", 1, 0.5, 0)
    $ playAudio(sfx_female_hmm2, "sfx", 1, False, 0, 0)

    mc_s "Holy fuck..."
    amb "Mmmhhh..."
    show ep04_ambtaste05 at ken_burns_bottom_to_top with normalfade
    mc_s "Damn you're good..."
    amb "What, did you forget how good your [si_full_r_low] is at sucking cock?"
    amb "Say it. Tell me how much you love your [si_full_r_low]'s mouth."
    mc_s "I..."
    amb "Fucking say it!"
    mc_s "Yes... fuck yes."

    show ep04_ambtaste06
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_female_hmm, "sfx", 2, False, 0, 0)
    amb "Hmph..."
    amb "Hmph... humph... mmmm..."
    mc_t "This is so wrong..."
    mc_t "Fuck it, just enjoy it..."

    show ep04_ambtaste07 at ken_burns_bottom_to_top
    amb "Ngh... mmph... hng..."
    amb "Been dreaming of this... fucking dreaming of you..."
    amb "Nobody's cock feels like yours..."
    amb "Should've been like this from the start..."
    show ep04_ambtaste08
    amb "Just like this..."
    amb "Using your [si_full_r_low]'s mouth whenever you need to..."
    amb "Ngh... ngh..."
    show ep04_ambtaste09
    $ setChannelVolume("sfx", 3, 0.4, 0)
    $ playAudio(sfx_female_hmm2, "sfx", 3, False, 0, 0)

    mc_t "Why do her dirty words turn me on so much..."
    amb "Hmph! Humph... ugh..."
    mc_t "Shit, I'm close..."

    show ep04_ambtaste10
    $ setChannelVolume("sfx", 4, 0.4, 0)
    $ playAudio(sfx_gagreflex4, "sfx", 4, False, 0, 0)
    amb "Mmh... hmph... ugh..."
    mc_t "Oh shit... Amber!"

    show ep04_ambtaste11
    amb "What's wrong? Can't handle it?"
    mc_s "Don't fucking stop!"
    amb "Patience, you desperate fuck."
    amb "You'll get to cum... but first I want to get comfortable."
    mc_t "Uh?"

    show ep04_ambtaste12 with normalfade
    amb "Want to know my dirtiest fantasy? That you stop treating me like your precious [si_full_r_low] and just use me like the whore I am..."
    mc_s "Shit, Amber..."

    show ep04_ambtaste13
    amb "Every fucking day... Every day I think about getting on my knees for you like this."
    amb "Lost count of how many times I've gotten myself off in your room, thinking about you..."
    show ep04_ambtaste14
    amb "Remember when we were younger?"
    amb "Even then, watching you in the bathroom... I'd touch myself thinking about you bending me over and fucking me raw."
    mc_s "You're fucking insane..."

    show ep04_ambtaste15 with normalfade
    amb "You were so in love with that bitch Antonella... while your [si_full_r_low] was next door, fucking herself every night thinking about you."
    amb "Some [br_full_r_low] you are."
    mc_s "I-"
    amb "Nothing to say, huh?"
    amb "If you have no words to say, just use that dick of yours to answer."
    $ stopAllSubchannels("sfx", 1.0)
    jump ep04_amber_bj




label ep04_amber_bj:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ ss.add("amber", "blowjob")

    show ep04_amber_bj01
    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_fellatio1, "sfx", 5, False, 0, 0)

    mc_s "Holy fuck, Amber..."
    amb "Mmmhh, mmhh!"
    show ep04_amber_bj02
    mc_s "Shit... where'd you learn to suck cock like that?"

    show ep04_amber_bj03
    amb "Mmmhh..."
    show ep04_amber_bj04
    mc_s "That's it, [sis_r_low]... take it all..."

    show ep04_amber_bj05
    amb "Ngh... mmh... mph..."
    show ep04_amber_bj06
    mc_s "You fucking love this, don't you?"

    show ep04_amber_bj07
    mc_s "Can't hear you with that mouth full!"

    show ep04_amber_bj08
    amb "Hmm! Hmmgh!"
    show ep04_amber_bj09
    mc_s "Yeah, that's what I thought. Too busy sucking your [br_full_r_low]'s cock."

    show ep04_amber_bj10
    amb "Ngh... ngh..."
    show ep04_amber_bj11
    amb "Hmm! Mmh... ngh..."
    show ep04_amber_bj12
    mc_s "Fuck, gonna cum if you keep that up..."
    amb "Mmh!"
    $ stopAllSubchannels("sfx", 1.0)
    scene eigengrau
    show ep04_amber_bj_back01 with normalfade
    amb "Not yet, you desperate fuck. Your [si_full_r_low]'s not done tasting you..."
    show ep04_amber_bj_back03
    amb "Just let me enjoy this thick cock a bit longer..."
    show ep04_amber_bj_back04
    amb "Ngh... mmgh... mmmh... fuck yes..."
    show ep04_amber_bj_back06
    amb "Mmgh... ahh... mmph..."
    show ep04_amber_bj_back08
    amb "Hmmgh... this is exactly what I've been craving..."
    show ep04_amber_bj_back09
    mc_s "Whatever you want..."

    show ep04_amber_bj_back12
    amb "Good boy. Now don't fucking move."
    show ep04_ambblow01 with normalfade
    mc_t "Holy shit, how deep can she...?!"

    show ep04_amber_bj_side01 with normalfade
    mc_t "This is fucking insane..."

    show ep04_amber_bj_side02
    amb "Ngh... mph... yes... mmmhh..."
    amb "Tell me how good your [si_full_r_low]'s throat feels..."
    show ep04_amber_bj_side03
    mc_s "Fuck..."

    show ep04_amber_bj_side04
    amb "Having fun with your little [si_full_r_low]?"
    mc_s "God yes..."

    show ep04_amber_bj_side05
    amb "Bet that prude Antonella never sucked you like this... Does it turn you on knowing what a whore your [si_full_r_low] is?"
    show ep04_amber_bj_side06
    mc_s "Hey, don't say that!"

    show ep04_amber_bj_side07
    amb "Still can't admit how much you love it, can you?"
    mc_s "Shit..."

    show ep04_amber_bj_side08
    amb "Your cock's doing all the talking for you, big [br_full_r_low]..."
    show ep04_amber_bj_side09
    amb "You love that I'm such a dirty slut for you..."
    show ep04_amber_bj_side10
    amb "You're about to burst, aren't you?"
    mc_s "Fuck... yes..."

    show ep04_amber_bj_side11
    amb "Want to mark your territory? Cover your [si_full_r_low] in cum?"
    show ep04_amber_bj_side12
    amb "Show me who I belong to... make me yours..."
    scene eigengrau
    show ep04_ambblow02
    amb "Cover me in that hot load... just not on my--"
    $ show_walkthrough("ep04_ambbjmenu")
    menu:
        "Cum on her tits":
            hide screen walkthrough_screen
            $ ep04_ambnight_cum += 2

            show white zorder 1.0 at ejaculation_flash
            show ep04_ambblow03 at vpunch with flash
            mc_s "Fuck! Here it comes!"
            amb "! ! !"
            show ep04_ambblow04
            $ stopAllSubchannels("music", 2.0)
            amb "Huh?"
            mc_s ". . ."

            show ep04_ambblow05 at subtle_zoom_in
            $ playAudio(amber_sexy_theme, "music", 3, True, 2.0, 1.0)
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            amb "What the actual fuck?! A little warning next time?!"
            mc_s "Thought cum sluts didn't need warnings."

            show ep04_ambblow06 with hpunch
            amb "Fuck you, [mc_name]!"
            amb "Look at this mess! You just had to shoot like a fucking firehose!"
            mc_s "Like I could control it..."
            amb "And wipe that smirk off your face, asshole!"
            mc_s "Can't help it... but look at you... you look like pornstar covered in cum."

            show ep04_ambblow07 with normalfade
            amb "God, you're right. It looks fucking great. Damn, that was a lot."
            mc_s "Oh, you loved it, didn't you?"

            show ep04_ambblow08
            amb "Maybe... just a little..."
            amb "But next time warn me or I swear to god..."
            mc_s "Or what?"
            amb "Or... um... no more [si_full_r_low]-[br_full_r_low] fun time..."
            mc_s "Deal."
            amb "Alright."
            amb "Now get out so I can clean up. And remember what I said!"
            show ep04_ambblow09 at subtle_zoom_out with normalfade
            mc_s "Yes ma'am..."
            mc_t "Holy shit... best head of my life. And those tits... fucking perfect."
            mc_t "She's wasting her time with basic content... she could be making millions in porn."

            jump ep04_amber_endscene


        "Cum on her face":
            hide screen walkthrough_screen
            $ ep04_ambnight_cum += 1

            show white zorder 1.0 at ejaculation_flash
            show ep04_ambblow03 at vpunch with flash
            mc_s "I don't care!"

            show ep04_ambblow10
            $ stopAllSubchannels("music", 2.0)
            amb "Oh?"
            mc_s ". . ."

            show ep04_ambblow11 with hpunch
            $ playAudio(amber_sexy_theme, "music", 3, True, 2.0, 1.0)
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
            amb "You fucking ASSHOLE! What did you DO?!"
            mc_s "Marked you like you wanted..."

            show ep04_ambblow12
            amb "On my TITS, you dipshit! Not my fucking FACE!"
            amb "Do you know how long this makeup took?! My fucking HAIR!"
            mc_s "Come on, you're being dramatic... besides, you look hot as fuck like that."

            show ep04_ambblow13 with normalfade
            amb "That's not a fucking compliment, you dick!"
            amb "You're lucky we're [fm_r_low], or I'd fucking end you..."
            mc_s "What?!"
            amb "Get. Out."
            mc_s "Amber..."

            show ep04_ambblow14 with normalfade
            amb "Are you fucking deaf?! GET OUT!"
            mc_s "No way..."
            amb_y "GET THE FUCK OUT OF MY ROOM RIGHT NOW BEFORE I FUCKING KILL YOU!"
            mc_s "Alright, okay..."
            mc_t "Maybe that wasn't my smartest move..."

            jump ep04_amber_endscene




label ep04_amber_endscene:
    if ep04_ambnight_cum == 2:
        $ ep04_ach_amber = True
    $ show_walkthrough("ep04_ambendmenu")
    menu:
        mc_t "Anyway... where should I go next?"
        "Go to the livingroom":
            hide screen walkthrough_screen
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep04_elimeet_intro


        "Go to your room":
            hide screen walkthrough_screen
            $ ep04_afternanami += 4
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep04_mad_mcroom




label ep04_mad_mcroom:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)

    show ep04_madmcroom01 with circlewipe
    if ep04_afternanami == 1:
        mc_t "Holy shit... I can't get what happened out of my head. Nanami was something else tonight..."
        mc_t "Those tits... So big, so soft, so firm. God, I wanted to fuck her so hard..."
        mc_t "But no, that would've been messed up. She was completely wasted... Plus she's Madison's friend, practically [fm_r_low]... Still, goddamn..."
        mc_t "I need to sleep this shit off before I lose my mind."
    elif ep04_afternanami == 2:
        mc_t "What a fucking disaster of a night..."
        mc_t "First Paz goes MIA, then Nanami gets wasted, and now Amber's bitching at me for whatever reason. Just perfect."
        mc_t "I'm done with this shit. Sleep is exactly what I need right now."
    elif ep04_afternanami == 3:
        mc_t "What a mess of a night..."
        mc_t "Paz disappears, Nanami gets hammered, and Amber flips out over some stupid LEDs. Like, seriously?"
        mc_t "Whatever. Maybe things'll make more sense after some sleep."
    else:
        mc_t "Hell of a night..."
        mc_t "Paz vanishes, Nanami gets totally plastered, and then that thing with Amber..."
        mc_t "My head's spinning. Need to crash and process all this..."

    $ setChannelVolume("sfx", 1, 0.8, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 1, False, 0, 0)

    show ep04_madmcroom02 at focus_pulse:
        rotate 180
        xzoom -1
        align (0.5, 0.5)
    mc_t "What the... Who's in here?"
    mc_t "How'd she even get in? I swear I locked that door..."

    $ stopAudio("sfx", 1, 1)

    show ep04_madmcroom03:
        rotate 180
        xzoom -1
        align (0.5, 0.5)
    $ setChannelVolume("sfx", 2, 0.8, 0)
    $ playAudio(sfx_phone_typing, "sfx", 2, False, 0, 0)

    mc_t "Seriously? Just barging in here like she owns the place..."
    mc_t "And now she's just chilling on her phone like this is totally normal..."
    mc_s "Hey! What the hell?"
    mad "Mmmm, just a sec. This is important."
    mc_s "Ever heard of knocking? This is my room, you know."

    $ stopAudio("sfx", 2, 1)

    show ep04_madmcroom04:
        rotate 180
        xzoom -1
        align (0.5, 0.5)
    mad "Nope! Never got that lesson. Mind if I make myself comfortable?"
    mc_s "Are you serious right now?"
    mad "Ugh, just scoot over already."
    $ setChannelVolume("music", 2, 0.5, 1.0) 
    $ playAudio(madison_theme, "music", 2, True, 2.0, 1.0)

    show ep04_madmcroom05 at ken_burns_bottom_to_top with normalfade
    mad "You're going to help me with something."
    mc_s "Huh?"
    mad "My muscles are sooo tense... How about a massage, big [br_full_r_low]?"
    mc_s "And why would I do that?"
    mad "Aww, come on! Aren't you supposed to take care of your sweet little [si_full_r_low]?"
    show ep04_madmcroom06
    mc_s "I don't have time for your games, Madison."
    mad "Oh? Then maybe [mo_r] and Amber would love to hear about you and Nanami earlier..."
    mc_s "The fuck?"
    mad "Just a teensy massage. That's all I'm asking..."
    mc_s "This is blackmail and you know it."
    mad "Is it? How mean of you to suggest that!"
    $ show_walkthrough("ep04_madmcmenu")
    menu:
        "Massage her":
            hide screen walkthrough_screen

            mc_s "Fine. Let's get this over with."
            mad "Yay! But first... Turn those lights up, will you? This mood lighting is sooo not working for me."
            mc_s "Whatever..."

            jump ep04_mad_massagebody


        "Refuse":
            hide screen walkthrough_screen
            $ stopAudio("music", 2, 2)
            $ rm.update("madison", "trust", -2)
            $ check_levels("madison", "trust", -2)

            mc_s "Screw this. I don't care what you do."

            $ setChannelVolume("music", 3, 0.5, 1.0) 
            $ playAudio(madison_bad_theme, "music", 3, True, 2.0, 1.0)

            show ep04_madmcroom07 with vpunch
            $ setChannelVolume("sfx", 2, 0.8, 0)
            $ playAudio(sfx_phone_typing, "sfx", 2, False, 0, 0)
            mad "Perfect!"
            mc_s "Wait, hold up! What are you doing?"
            mad "Oh, nothing much..."
            mc_s "What are you typing?"
            mad "Just a little story about someone taking advantage of their drunk friend... Ring any bells?"
            mc_s "For fuck's sake, Madison!"

            $ stopAudio("sfx", 2, 1)

            show ep04_madmcroom08 at ken_burns_right_to_left with hpunch
            mad "I gave you two chances to play nice."
            mad "But your dick does all the thinking, doesn't it?"
            mad "I tried asking sweetly--"
            mc_s "Sweetly? You call that sweet?"

            show ep04_madmcroom09 at subtle_zoom_out with normalfade
            mad "--but since you want to be difficult, I guess [mo_r] and Amber need to know what kind of creep they're living with."
            mad "Wonder how they'll react when--"
            mc_s "This is fucking insane."
            mad "What's insane?"
            mc_s "All of this. You're actually crazy."

            show ep04_madmcroom10 with hpunch
            mad "Hey, what are you staring at? They're not much compared to Amber's..."
            mad "See? Totally tiny... Not your type at all, right?"
            mc_s "Madison... What the hell are you doing?"
            mad "Just wondering why you can't keep your eyes up here..."
            mc_s "Get out! Now!"
            mad "Sure, sure... Right after I get a pic with my pervy [br_full_r_low]."
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)

            show ep04_madmcroom11 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "What?!"
            mad "Say 'I'm a total creep!'"
            mc_s "You little..."
            mad "Shhhh! Perfect shot!"
            show ep04_madmcroom12 with normalfade
            mad "Look how cute we are! Well, I'm cute. You look like a deer in headlights..."
            mad "Just a little insurance policy. Never know when it might come in handy..."
            mc_s "You're actually evil, you know that?"
            mad "Mmm, maybe I am..."
            mad "But here's the deal - Nanami's off limits."
            mad "Try anything again, and everyone - [mo_r], Amber, [daddy_r] dearest - they all get front row seats to your perverted adventures."
            mad "Plus this adorable photo, of course!"
            mad "Got it?"
            mc_s "Okay..."

            show ep04_madmcroom13
            mad "Good boy! See how easy that was?"
            mad "Sweet dreams, big [br_full_r_low]! And remember... behave yourself, or things might get really interesting around here..."
            mc_t "This [fm_r_low] is so fucked up..."

            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "What just happened? Why's she so protective of Nanami?"
            mc_t "And that picture... Fuck! This is such a mess. Whatever, I'll deal with this shit tomorrow."

            $ ep04_madnight += 1
            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall




label ep04_mad_massagebody:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep04_madmassage01
    $ rm.update("madison", "trust", 2)
    $ check_levels("madison", "trust", 2)

    mc_t "Seriously? Blackmailing me for a fucking massage? This girl's lost it..."
    mc_t "And she acts like this is perfectly normal..."

    $ setChannelVolume("amb", 1, 0, 1.0)
    $ setAllSubchannelsVolume("music", 0, 1.0)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 1.0
    $ setChannelVolume("amb", 1, 0.3, 1.0)
    $ setAllSubchannelsVolume("music", 0.5, 1.0)

    show ep04_madmassage02 at ken_burns_top_to_bottom with circlewipe
    mc_s "What... the fuck?"
    mad "What's wrong? Can't handle your [si_full_r_low] getting comfy? Or maybe you're enjoying the view too much, perv..."
    mc_s "I'm not- That's not-"

    show ep04_madmassage03 at subtle_zoom_out
    mad "Not what? Not staring at my panties? Or maybe it's the whole forbidden [si_full_r_low] thing that's got you all worked up."
    mc_s "Fuck, Madison, I'm not looking at anything!"

    show ep04_madmassage04
    mad "No? Then why are you just standing there like an idiot? Getting a good view of your little [si_full_r_low]'s ass?"
    mad "What's wrong? Guilty conscience catching up with you?"
    mc_s "Can we just get this over with already?"

    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

    show ep04_madmassage05
    mad "Sure thing, big [bro_r_low]. But remember... I see everything."
    mc_s "You're actually enjoying this, aren't you?"
    mad "Watching you squirm is delightful."
    show ep04_madmassage06 with normalfade
    mad "Mmm... you're actually pretty good at this..."
    mc_s "Glad you're having fun with your blackmail massage."
    mad "Don't be such a grump! Think of it as quality [sib_r] time."
    mc_s "Pretty sure normal siblings don't pull this kind of shit."

    show ep04_madmassage07 at ken_burns_left_to_right with normalfade
    mad "But we're not exactly normal, are we? Your hands really are amazing though..."
    mc_s "Whatever."
    mad "So grumpy. You know you're still my favorite toy to play with."
    show ep04_madmassage08 with normalfade
    mc_s "Right, that's why you're blackmailing me."
    mad "I prefer to call it strategic motivation."
    mc_s "Call it whatever you want."
    mad "Your anger just makes this more entertaining, you know."
    mc_s "..."

    show ep04_madmassage09 at ken_burns_top_to_bottom
    mad "Don't go silent now. We're just getting to the fun part."
    mc_s ". . ."
    mad "You can ignore me all that you want, big [bro_r_low]. But don't forget, that I'm still in charge here."
    mc_s "Are we done yet?"

    $ stopAllSubchannels("music", 2.0)

    show ep04_madmassage10 with normalfade
    mad "Not quite. We still have some unfinished business."
    mc_s "What now?"
    mad "Something I think you'll find quite... interesting."
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.3)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)

    show ep04_madmassage11
    mad "I've noticed how stressed you've been lately. Not good for your health."
    mad "As your caring little [si_full_r_low], I have a proposition that could benefit us both."
    mc_s "What are you talking about?"
    mad "Let me stretch a bit first... Your hands really did wonders."
    mc_s "Just get to the point."

    show ep04_madmassage12
    mad "Here's the deal: I know you've got the hots for our [si_full_r_low] Amber. Don't even try denying it."
    mad "And [mo_r] too... quite the [fm_r_low] man, aren't you?"
    mad "Oh, and let's not forget about Nanami."
    mad "The girl you conveniently got drunk tonight?"
    mad "Even your own [dau_r_low]... My, my, such naughty thoughts about Isabella..."
    mc_s "You're talking nonsense."

    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(madison_dom_theme, "music", 1, True, 2.0, 1.0)

    show ep04_madmassage13 with normalfade
    mad "So here's my offer: Help me with some personal matters, and all these dirty little secrets stay buried."
    mad "Imagine what everyone would think about your... particular interests in your [fm_r_low]."
    mc_s "What kind of personal matters?"
    mad "Don't worry about the details yet. You'll find out soon enough."
    mad "Now... kneel."
    mc_s "..."
    mad "Do it."
    show ep04_madmassage14 at ken_burns_bottom_to_top with normalfade
    mc_s "There. Happy now?"
    mad "Just wanted to see you where all men belong."
    mc_s "This is ridiculous. Just tell me what you want and let's end this shit."

    $ stopAudio("music", 1, 2)

    show ep04_madmassage15 at ken_burns_top_to_bottom
    mad "Let me tell you a story. About a big [br_full_r_low] who ran away to another castle, abandoning his [fm_r_low]."
    $ setChannelVolume("music", 2, 0.3, 1.0)
    $ playAudio(madison_sad_theme, "music", 2, True, 2.0, 1.0)
    mad "He left his [si_full_r_low]s, his [mo_full_r_low]... even his own [dau_r_low]..."
    mc_s "Don't bring her into this."
    mad "Quiet. I'm not finished."
    mad "There was this beautiful little redhead girl. The most adorable thing you'd ever seen."
    mad "But her [mo_full_r_low] ignored her, too busy fighting with the older [si_full_r_low] and caring for a tiny blonde baby that her [so_r_low] had abandoned."
    show ep04_madmassage16
    mad "The poor girl had no one. Not a single soul to talk to or play with."
    mad "Every night, she'd cry herself to sleep, alone in the darkness."
    mad "Then one day, she heard her [mo_full_r_low] crying. She went to check and found her [mo_full_r_low] in the bedroom, being slapped by her [da_full_r_low]."
    mad "The little girl couldn't understand. She just saw her [mo_full_r_low] screaming, crying, while her [da_full_r_low] wouldn't stop."
    mad "When he finally left, she tried to comfort her [mo_full_r_low]. But [mommy_r_low] just screamed at her, called her a nuisance, told her to disappear."
    show ep04_madmassage17 with hpunch
    mad "That night, something broke inside the little redhead. She made a decision - no more tears, no more being the good girl."
    $ stopAudio("music", 2, 2)
    mad "She learned that being good only gets you hurt. Being bad... that's how you survive. That's how you take control."
    mad "And that's how the little redhead became the big bad wolf."
    mc_s "Madison... I had no idea..."
    mad "Save your pity. You're worthless as a [br_full_r_low] and even worse as a [da_full_r_low]. Now, are you going to help me or not?"
    $ ep04_madstory = True
    $ show_walkthrough("ep04_madmassmenu")
    menu:
        "Help her":
            hide screen walkthrough_screen

            mc_s "Fine... I'll help."
            mad "See? Was that so hard?"
            mc_s "What do you need?"
            #+1X love @ endlabel
            jump ep04_mad_reward


        "Refuse":
            hide screen walkthrough_screen
            $ rm.update("madison", "trust", -2)
            $ check_levels("madison", "trust", -2)

            mc_s "I'm sorry for what happened, but I won't let you blackmail me."

            scene eigengrau
            $ setChannelVolume("music", 3, 0.3, 1.0)
            $ playAudio(madison_bad_theme, "music", 3, True, 2.0, 1.0)

            show ep04_madmassage18 at ken_burns_bottom_to_top with vpunch
            mad "What a shame. But don't worry, I'm here to help fix your... character flaws."
            mad "I'll give you one more chance tomorrow. Choose carefully..."
            mad "If the answer's still no... well, things will get very interesting around here."
            mc_s "I don't care, I'm not going to be blackmailed by a brat like you."

            $ setChannelVolume("sfx", 1, 0.9, 0)
            $ playAudio(sfx_punch, "sfx", 1, False, 0, 0)

            show ep04_madmassage19 with hpunch
            mad "You will respect me. Understood?"
            mc_s "Ow! What the fuck?!"
            mad "Watch your tongue. Never speak to me like that again."
            mad "I'm done with this pathetic display of masculinity. I'm changing and leaving."
            scene eigengrau with slowfade
            show ep04_madmassage20 with vpunch
            mad "And if you thought you were different from other men... you're just as weak and pathetic as the rest."
            mad "We'll talk tomorrow, and you better have a different answer."
            mad "Or you'll discover just how creative I can be."
            show ep04_madmassage21
            mc_t "What the fuck just happened?"
            mc_t "She's completely insane."

            show ep04_madmassage22 with hpunch
            mc_s "Now what?!"
            mad ". . ."
            mc_s "Hey! I'm talking to you!"

            show ep04_madmassage23 with normalfade
            mad "Relax. Just forgot something."
            mc_t "Her phone? Seriously?"
            mad "There it is."
            show ep04_madmassage24
            mc_s "What?"
            mad "Nothing."
            mad "Just thinking that you're a pathetic man. That's all."
            mc_s "You're just going to stand there and insult me?"

            show ep04_madmassage25
            mad "Not insulting. Just stating facts. You're pathetic - that's why I'm here."
            mad "I'm going to fix you. Whether you like it or not."
            mc_y "Get out. NOW!"
            mad "Of course... but first... Smile!"
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)

            show ep04_madmassage26 at photo_effect with flash
            show photo_flash with dissolve
            mad "Smile! This is a moment to remember."
            mc_s "What the fuck are you doing?!"
            mad "Just a little souvenir. You can see it as a blackmail material or a gift from a beautiful [si_full_r_low], I don't care."
            mc_s "You're fucking insane!"

            show ep04_madmassage27
            mad "Oh, I am. Thanks to men like you."
            mad "Men who treat women like objects, use them and throw them away. You make me sick."
            mad "But don't worry - I'll help fix you. Nothing too extreme... wouldn't want to damage your precious morality, if you even have any."
            mc_t "She's completely psychotic!"
            mad "I can't read minds, but I know you're thinking what a bitch I am."
            mad "Good. That's exactly what I want. Fear is the best teacher of respect."
            show ep04_madmassage28
            mad "Sweet dreams, big [br_full_r_low]. Don't forget to think of me."
            mc_s "Fuck off."

            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "What the hell did I just get myself into? This girl's a complete nightmare..."

            $ ep04_madnight += 2
            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall




label ep04_mad_reward:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("music", 2, 0.3, 1.0)
    $ playAudio(madison_theme, "music", 2, True, 2.0, 1.0)

    show ep04_madnopanties01
    $ rm.update("madison", "trust", 2)
    $ check_levels("madison", "trust", 2)
    mad "You're going to start by kissing my feet."
    mc_s ". . ."
    mad "Don't make me repeat myself, big [bro_r_low]. Kiss. My. Feet."
    mc_s ". . ."

    show ep04_madnopanties02 with vpunch
    mad "Oh my god! You were actually going to do it? This is priceless!"
    mc_s "You told me to do it."
    mad "Yeah, but I didn't think you'd actually stoop that low."
    mc_s "Just tell me what you want and end this."

    show ep04_madnopanties03
    mad "Look at you, ready to do anything your little [si_full_r_low] asks. How pathetic."
    mc_s "Just get to the point already."
    mad "Don't be such a grump. I'm just having a bit of fun."
    mc_s "This isn't my idea of fun."

    show ep04_madnopanties04 with normalfade
    mad "How about now? Having fun yet?"
    mc_s ". . ."
    mc_t "Why is my body reacting like this?"

    show ep04_madnopanties05 with normalfade
    mad "Oh, someone's finally getting into it."
    mc_s "You've had your fun. I agreed to whatever you wanted, now let's end this."
    mad "You wound me, big [bro_r_low]. Don't you enjoy our quality time?"
    mc_s "Your words, not mine."

    show ep04_madnopanties06 at ken_burns_left_to_right with normalfade
    mad "Fine then. I'll give you something else to do. Something you'll definitely enjoy."
    mc_s "I doubt that."
    mad "Have some faith. Trust me, this will be interesting."
    mc_s "Madison, just stop and go back to your room."

    show ep04_madnopanties07 with normalfade
    mad "Even like this?"
    mc_s "You can't seduce me, Madison."
    mad "Oh, I wouldn't dream of it. But maybe this will change your mind."
    mad "Since you seem to have such... interesting tastes in [fm_r_low] members."
    $ stopAllSubchannels("music", 2.0)

    show ep04_madnopanties08 with normalfade
    mc_s "What are you doing?"
    mad "Giving you what you want. Isn't that what all your [si_full_r_low]s do?"
    mc_s "I don't want this."
    mad "Sure you don't. Now help me with these."
    mc_s "Fine. But this is the last thing."

    $ setChannelVolume("music", 5, 0.3, 1.0)
    $ playAudio(nanami_innocence_theme, "music", 5, True, 2.0, 1.0)

    show ep04_madnopanties09 at ken_burns_left_to_right with normalfade
    mad "Oh! Wha-What am I d-doing here?"
    mc_s "What the hell are you doing?"
    mad "I'm just a sweet and innocent girl who doesn't know anything about sex... I don't even know what a penis is..."
    mc_s "What are y..."

    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.8)
    $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

    show ep04_madnopanties10 with normalfade
    $ setChannelVolume("sfx", 3, 0.8, 0)
    $ playAudio(sfx_phone_typing, "sfx", 3, False, 0, 0)
    mad "I'm just gonna write to Maddie that I love her and that she's like a [si_full_r_low] to me."
    mad "That she's the most amazing girl that I know and that I'll always be there for her."
    mad "M-Madison isn't like other people. She's... um, she's difficult to explain."
    mad "To most people, she's cold, bossy, even mean. B-but to me... she's my best friend."
    mad "It wasn't always like that. Back in school, she... she scared me. Everyone respected her, but not in a good way."
    mad "Madison didn't care about rules or consequences, and she was... kind of cruel."
    mad "She never picked on me directly, though. I guess I wasn't even worth noticing."
    show ep04_madnopanties11 with normalfade
    mad "That changed when some girls started bullying me. I-I don't really know why they picked me... I guess I was an easy target."
    mad "I was clumsy, quiet, always apologizing for everything."
    mad "At first, it was little things—hiding my books, laughing when I tripped."
    mad "But one day, they locked me in the bathroom. I sat there for hours, crying, but not loud enough for anyone to hear."
    mad "When I got out, Madison was waiting for me. She... um, she didn't look mad or worried, just... amused."
    mad "She said, 'You're pathetic.' I-I didn't even argue."
    show ep04_madnopanties12
    mad "But after that, everything changed."
    mad "The girls stopped bothering me. They... they got in trouble. One of them was suspended, and the others... well, they never spoke to me again."
    mad "I didn't understand why until I noticed Madison smirking at me in class."
    mad "When I asked her about it, she just shrugged and said, 'Yeah, it was me. What about it?'"
    mad "I tried to thank her, but she grabbed my chin and said, 'You're mine now, Nanami. Nobody touches what's mine.'"
    show ep04_madnopanties13
    mad "Madison isn't... um, she's not a hero or anything."
    mad "She's still mean, and she doesn't care about being nice. But with me... she's different."
    mad "I don't know why. I don't even think I deserve it."
    mad "B-but I guess... it's enough."
    mc_s "Uh..."
    mad "Hey, Maddie. Are... are we still friends even if your [br_full_r_low] made me drink and then touched me against my will?"
    mc_s "What?"

    show ep04_madnopanties14
    mad "Of course we are, sweetie. You're just to pure for this world, and I'll be always there to take care of you."
    mad "And don't worry about that pervert, I'll take care of him too. He will regret what he did to such an innocent girl like you."
    mc_s "I... I..."

    $ stopAllSubchannels("music", 2.0)

    show ep04_madisonleave01 with normalfade
    $ ep04_madnanastory = True
    mad "Did you like how I portrayed our dearest Nanami?"
    mad "I bet you have never fucked a sweet girl like that, don't you?"
    mad "I bet your predatory senses are screaming inside your tiny dirty brain 'take her.'"
    mc_s "What is wrong with y..."

    show ep04_madisonleave02 with normalfade
    mad "Shut up. Here are your options - no complaints. Keep massaging or I leave, and you know what that means."
    mc_s "You think I'm your slave?"
    mad "Slaves don't get choices. You do."
    mc_s "You're just cruel."
    mad "Aww, is that how you talk to your helpful little [si_full_r_low]?"
    mc_s "Helpful? This is your idea of help?"
    mad "Whatever. Massage or I leave. Choose."
    $ show_walkthrough("ep04_madrewamenu")
    menu:
        "Continue":
            hide screen walkthrough_screen

            mc_s "Like I have a choice..."
            mad "Now you're getting it, big [bro_r_low]!"
            # 1x love @endlabel
            jump ep04_mad_assjob


        "Stop":
            hide screen walkthrough_screen

            mc_s "I'm done with this."
            mad "Suit yourself. Have fun with what comes next."
            # -1x love @endlabel
            $ ep04_madnight += 3
            jump ep04_mad_assjob_deny




label ep04_mad_assjob_deny:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("music", 2, 0.3, 1.0)
    $ playAudio(madison_bad_theme, "music", 2, True, 2.0, 1.0)

    show ep04_madisonleave03 with vpunch
    $ rm.update("madison", "trust", -2)
    $ check_levels("madison", "trust", -2)
    mad "Remember what I told you when we first met? I see everything. Being a cop won't protect you from what I can do."
    mad "Sure, you don't want to massage me anymore... fine."
    mad "But you still promised to help me. Making me feel bad though... that's not very nice to someone who cares about you..."
    mad "I get it - you're used to breaking women, treating them like toys. But trust me, dear [br_full_r_low], you've never dealt with anyone like me."
    mc_s "What twisted shit happened to make you this way?"

    show ep04_madisonleave04 with normalfade
    mad "Were you even listening earlier? Or do you just enjoy wasting my time?"
    mad "I told you that story so you'd understand what's happening, but apparently that's too much for your simple mind."
    mad "Whatever. Come here."
    mc_s "Why?"
    mad "Don't be difficult. Just do it."
    $ setChannelVolume("sfx", 3, 0.8, 0)
    $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)

    show ep04_madmassage26 at photo_effect with flash
    show photo_flash with dissolve
    mad "Give me your best smile, big [br_full_r_low]!"
    mc_s "What are you-"
    mad "Quiet. This is going to make excellent leverage."
    mc_s "Stop this shit. I'm not playing your game."

    show ep04_madmassage27
    mad "I warned you day one - don't test me."
    mad "You really don't want to see my bad side."
    mad "Now that I've got what I need, I'll let you get your beauty rest. God knows you need it."
    show ep04_madmassage28
    mad "Sweet dreams, big [bro_r_low]. Don't forget our little arrangement~"
    mc_t "What the actual fuck..."

    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.0
    show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
    mc_t "I need to find a way to stop this psycho... but how?"
    mc_t "Maybe I can reason with her... make her see she needs help."
    mc_t "Fuck it. I'll deal with this tomorrow. Just need to sleep and forget this nightmare."

    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall




label ep04_mad_assjob:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("music", 1, 0.2, 1.0)
    $ playAudio(madison_sexy_theme, "music", 1, True, 2.0, 1.0)

    show ep04_madmovingass01 at concentrate with hpunch
    $ rm.update("madison", "trust", 2)
    $ check_levels("madison", "trust", 2)
    mad "Come on, massage it!"
    mc_s "What are you-"
    mad "Just do it!"
    mc_s ". . ."
    mad "Are you deaf? I said do it!"
    show ep04_madmovingass02 at concentrate
    mc_s "This is insane..."
    mad "Did I say use your hands?"
    mc_s "What-"
    mad "Use your mouth, idiot."
    mc_s "You can't be serious."
    mad "I don't have time for this. Use. Your. Mouth."
    show ep04_madmovingass03 at concentrate
    mad "Lick it like the obedient dog you are."
    mc_s "I'm not doing that."
    mad "Be a good boy and I'll let you finish when we're done."
    mc_t "Fuck... I need that release. Should I just do what she wants?"

    $ show_walkthrough("ep04_madajmenu")
    menu:
        "Continue":
            hide screen walkthrough_screen

            mc_s "Fine. Just this once."
            pass
        "Stop":
            hide screen walkthrough_screen

            mc_s "I'm done with this."
            mad "Your loss. Good luck with what comes next."
            $ stopAllSubchannels("music", 2.0)
            $ ep04_madnight += 3
            # -1x love @endlabel
            jump ep04_mad_assjob_deny


    show ep04_madi_asslick01
    $ rm.update("madison", "trust", 2)
    $ check_levels("madison", "trust", 2)
    $ rm.update("madison", "cor", 1)
    $ check_levels("madison", "cor", 1)
    mad "That's it, good boy. Show your little [si_full_r_low] some love."
    mc_s ". . ."

    show ep04_madi_asslick02
    mad "Mmm, you've done this before, haven't you?"
    mc_s ". . ."

    show ep04_madi_asslick03
    mad "Fuck! Yes! Right there!"
    mc_s ". . ."

    show ep04_madi_asslick04
    mad "Such a good boy, aren't you?"
    mc_s ". . ."

    show ep04_madi_asslick05
    mad "Don't you dare stop now."
    mc_s ". . ."

    show ep04_madi_asslick06
    mad "You've made me very happy, big [br_full_r_low]."
    mc_s ". . ."
    mad "Now let's see what else you can do."
    mc_s "What are you-"
    mad "Same thing, but with something else this time."
    $ show_walkthrough("ep04_madajmenu_2")
    menu:
        mc_t "Fuck, I need this release so bad... Should I keep going?"
        "Continue":
            hide screen walkthrough_screen

            mc_s "Let's just get it over with."

            $ setChannelVolume("amb", 1, 0, 1.0)
            pass
        "Stop":
            hide screen walkthrough_screen

            mc_s "No more."
            mad "Your choice. Deal with what comes next."
            $ ep04_madnight += 3
            $ stopAllSubchannels("music", 2.0)
            $ setChannelVolume("amb", 1, 0, 1.0)
            jump ep04_mad_assjob_deny


    $ ss.add("madison", "assjob")
    $ ep04_madnight += 4
    pause 1.0
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.3, 1.0)

    show ep04_madassj01 with circlewipe
    $ rm.update("madison", "cor", 1)
    $ check_levels("madison", "cor", 1)
    mad "Damn, no wonder you've got half the [fm_r_low] wrapped around your finger..."
    mc_s "Whatever."
    mad "Don't get any ideas. Just do what you're told. And make it quick."
    mc_s "Like I'd want anything else."

    show ep04_madassj02 with normalfade
    mad "Remember - no penetration."
    mc_s "I know."
    mad "Do you? Seems like you're getting other ideas."
    mc_s "Just shut up."
    mad "You could just take what you want. I wouldn't stop you."
    mc_s "I'm not a rapist."
    mad "What's a little jail time compared to fucking your little [si_full_r_low]?"
    mc_s "Shut the fuck up!"

    show ep04_madi_assjob01
    mad "The angrier you get, the harder you become. Interesting."
    mc_t "Fuck, this feels too good."

    show ep04_madi_assjob02
    mad "Good boy, keep going. Such an obedient pet."
    mc_t "She's infuriating, but this feels amazing."

    show ep04_madi_assjob03
    mad "Careful not to slip in. Wouldn't want to commit a crime, would we?"
    mc_s "You're not making this easier."

    show ep04_madi_assjob04
    mad "We both know it's inevitable."
    mc_s "Just stop talking."

    show ep04_madi_assjob05
    mad "My ass is just too tempting, isn't it? Hard to resist?"
    mc_s "I won't rape my [si_full_r_low]. That's sick."

    show ep04_madi_assjob06
    mad "What's sicker - the rape part or the [si_full_r_low] part?"
    mc_s "Both."

    show ep04_madi_assjob07
    mad "But Amber's different somehow? Interesting."
    mc_s "Just. Shut. Up."

    show ep04_madi_assjob08
    mad "Not possible, big [bro_r_low]. You're too cute when you're angry."
    mc_t "I'm close and she won't stop running her mouth."
    mad "Getting close? Going to make a mess of your [si_full_r_low]'s ass?"
    show ep04_madi_assjob09
    mc_s "Fuck, I'm gonna cum."
    mad "Choice time, big [br_full_r_low]. Inside your [si_full_r_low]'s ass, or hold back and I'll let you feel something else."
    $ show_walkthrough("ep04_madajmenu_3")
    menu:
        mc_t "Fuck, what do I do?"
        "Cum inside her":
            hide screen walkthrough_screen

            mc_t "Fuck it."

            $ stopAllSubchannels("music", 2.0)
            #rrec stop sound
            show white zorder 1.0 at ejaculation_flash
            show ep04_madassj03 at hpunch with flash
            mad "What are you-"
            mc_s "Shut up, I'm cumming."
            mad "Did you just- Are you fucking serious?"
            mc_s "You offered."
            mad "You weren't supposed to actually do it!"
            $ rm.update("madison", "trust", -3)
            $ check_levels("madison", "trust", -3)
            $ rm.update("madison", "cor", 1)
            $ check_levels("madison", "cor", 1)

            show ep04_madassj04 at ken_burns_top_to_bottom with vpunch
            mc_s "Too late. That felt amazing."
            mad "But... but... what the hell?"
            mc_s "That's what happens when you play games, Madison."
            mad "I was just teasing! That wasn't supposed to happen!"
            mc_s "Well, it did. Deal with it."
            mad "I... that... whatever."
            show ep04_madassj08 with normalfade
            mad "You really did a number on my ass, dumbfuck."
            mc_s "Good."
            mad "Stay right there."
            mc_s "What?"

            $ setChannelVolume("music", 2, 0.3, 1.0)
            $ playAudio(madison_bad_theme, "music", 2, True, 2.0, 1.0)
            mad "Just getting a little souvenir."
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)

            show ep04_madassj07 at photo_effect with flash
            show photo_flash with dissolve
            mc_s "Wait, what are-"
            mad "Too late. Insurance policy in case you try anything stupid."
            mc_s "What the fuck is wrong with-"
            mad "Nothing's wrong. Just being careful."
            show ep04_madassj09
            mc_s "You can't do that!"
            mad "Already did."
            mc_s "What are you going to do with it?"
            mad "Nothing... unless you piss me off."
            show ep04_madmassage28
            mad "Sweet dreams, big [bro_r_low]."
            mc_s "Hey! We're not done here!"
            mad "Oh, we definitely are."
            mc_s "No, we're not! What-"
            mad "Bye!"
            mc_s "Fuck!"

            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "What the hell did I just do?"
            mc_t "Every woman in this house is like a walking fantasy. And they're all [fm_r_low]."
            mc_t "Not all of them, but still... I'm going to hell for this."
            mc_t "I need sleep."
        "Hold it":
            hide screen walkthrough_screen

            mc_t "I need to feel her... God help me."
            mc_s "Fine."
            mad "Fine what?"
            mc_s "I'll hold back."

            $ ss.add("madison", "pussyjob")

            show ep04_madassj05 with normalfade
            mad "Good boy."
            mc_s "Stop with the dog shit."
            mad "Just this once."
            mc_t "That was... surprisingly easy?"

            show ep04_madassj06
            mad "I honestly thought you'd just lose control and cum like an animal."
            mc_s "Fuck you."
            mad "I love how angry you get. Makes me want to kiss that scowl off your face."
            show ep04_madassj10
            mc_s "Uh..."
            mad "But that's not what you want, is it?"
            mc_s "What?"

            show ep04_madassj11
            mad "You want to feel your little [si_full_r_low]'s pussy, don't you? Feel how wet and warm she is?"
            mc_s "I..."
            mad "Go ahead. Make yourself feel good."
            mc_s "This is so fucked up..."
            mad "That's why it's fun."
            mc_s "You're seriously twisted."
            mad "Maybe, but that's why you love it. Why you're rubbing against your [si_full_r_low] right now."
            mc_s "I don't love-"
            mad "Shut up and cum. We both know you're close."
            mc_t "Fuck, she's right."

            show white zorder 1.0 at ejaculation_flash
            show ep04_madassj13 with flash
            mc_s "I'm cumming."

            show white zorder 1.0 at ejaculation_flash
            show ep04_madassj14 with flash
            mad "Cover your [si_full_r_low]'s pussy, big [bro_r_low]."
            $ stopAllSubchannels("music", 2.0)

            show ep04_madassj12 with slowfade
            mc_s "Fuck!"
            mad "You'll like what comes next."
            show ep04_madassj15 with hpunch
            mc_s "Holy shit..."
            mad "Look at all that mess you made!"
            mc_t "That was intense."
            mad "Someone needs to clean this up."
            mc_s "What are you-"

            show ep04_madassj16
            mad "Looks delicious, doesn't it?"
            mc_s "You're not serious."
            mad "What? Don't all men love seeing this?"
            mc_s "I..."
            mad "Watch carefully."
            show ep04_madassj17 with normalfade
            $ rm.update("madison", "trust", 3)
            $ check_levels("madison", "trust", 3)
            $ rm.update("madison", "cor", 2)
            $ check_levels("madison", "cor", 2)

            mc_t "Fuck, that's hot."
            mc_s "I... uh..."
            mad "Like seeing your little [si_full_r_low] all dirty?"
            mc_s "I..."

            $ setChannelVolume("music", 2, 0.3, 1.0)
            $ playAudio(madison_theme, "music", 2, True, 2.0, 1.0)
            mad "Let me show you something."
            $ setChannelVolume("sfx", 3, 0.8, 0)
            $ playAudio(sfx_camerashot, "sfx", 3, False, 0, 0)

            show ep04_madassj18 at photo_effect with flash
            show photo_flash with dissolve
            mad "Time for a selfie."
            mc_s "I... uh..."
            mad "Don't be shy. After what we just did?"
            mc_s "Fine."
            mad "Good boy."
            mc_s "What are you doing with that picture?"
            mad "Just a memory. Nothing more."
            mc_s "I don't believe you."

            show ep04_madassj19
            mad "You shouldn't. But that doesn't matter now, does it? Not with all this mess."
            mc_s "..."
            mad "Let's clean up."
            mc_s "What-"
            mad "Kiss me."
            mc_s "What?"

            show ep04_madassj08
            mad "Kidding!"
            mad "You've surprised me tonight, big [br_full_r_low]."
            mad "Helping me, almost kissing my feet, restraining yourself, and now this."
            mad "Almost fell for the kiss too. Hilarious."
            mc_s "I wasn't going to."
            mad "Maybe you're different from the others."
            mc_s "What are you talking about?"
            mad "You'll see soon enough."
            show ep04_madassj09
            mad "You've been good tonight. I'll let you rest."
            mad "But remember - I've got plans for us. Don't forget your promise. I'm always watching."
            mad "Sweet dreams."
            show ep04_madmassage28
            mc_s "I..."
            mad "Goodnight, big [bro_r_low]."
            mc_s "Yeah... goodnight."

            $ stopAllSubchannels("music", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.0
            show ep04_madmassage29 at ken_burns_bottom_to_top with normalfade
            mc_t "What the fuck just happened?"
            mc_t "That was fucked up... but intense."
            mc_t "I need sleep. Now."

            $ ep04_ach_madison2 = True
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall




label ep04_elimeet_intro:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
    $ setChannelVolume(channel="amb", subchannel=8, volume=0.3)
    $ playAudio(sfx_fireplace, "amb", 8, True, 1.5, 0)

    show ep04_elimeet01 with circlewipe
    mc_t "Everything that's happened since I got back... it feels surreal."
    mc_t "And still no word from Paz..."

    show ep04_elimeet02
    mc_t "Fuck it. More beer it is."

    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_keys, "sfx", 1, False, 0, 0)

    show ep04_elimeet03 with hpunch
    mc_t "What the..."

    $ stopAudio("sfx", 1, 0.5)

    show ep04_elimeet04 with normalfade
    $ setChannelVolume("sfx", 2, 0.6, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)

    mc_t "[mo_r]? At this hour? She doesn't look too steady..."
    mc_t "We haven't really talked since I got back. Maybe I should..."

    show ep04_elimeet05 with normalfade
    mc_s "[mo_r]? Everything okay?"

    $ show_walkthrough("ep04_elimeetmenu")
    menu:
        "Be gentle":
            hide screen walkthrough_screen

            mc_s "Had a fun night out?"

            show ep04_elimeet05_y
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
            eli "Oh! My baby boy's still up!"
            eli "Mmm... come give [mommy_r] a hug..."
            mc_s "Whoa, easy there..."
            eli "Always so caring... such a good boy..."
        "Be direct":
            hide screen walkthrough_screen

            mc_s "You're drunk, aren't you?"

            show ep04_elimeet05_n
            $ rm.update("elizabeth", "trust", -1)
            $ check_levels("elizabeth", "trust", -1)
            eli "Oh... sweetheart..."
            eli "Just... just a few glasses of wine..."
            mc_s "[mo_r]..."
            eli "Don't look at me like that..."
    show ep04_elimeet06 with normalfade
    $ rm.set_knows("elizabeth", True)
    eli "You look tired, baby. Everything alright?"
    mc_s "Shouldn't I be asking you that? It's pretty late... Are you drunk?"
    eli "Drunk? Maybe a little... but [mommy_r]'s fine..."
    mc_t "It's almost impressive how she's trying to act sober while swaying in those heels."
    mc_s "Since when do you drink this much? You used to hate it."

    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_changeclothes_nozip, "sfx", 2, False, 0, 0)
    $ setChannelVolume("sfx", 3, 1, 0)
    $ playAudio(sfx_toweldrop, "sfx", 3, False, 0, 0)

    show ep04_elimeet07
    eli "A girl needs to unwind sometimes... Nothing wrong with that..."
    eli "Let me grab some water and we can catch up! It's been so long..."
    show ep04_elimeet08
    mc_s "God, [mo_r] - you can barely walk. Let me help."
    eli "Don't fuss, darling. [mommy_r]'s perfectly capable..."
    eli "Just... give me a minute. Then we can talk properly..."
    eli "Like we used to... remember?"
    mc_t "This isn't like her at all..."

    show ep04_elimeet09 with normalfade
    mc_t "[mo_r]'s in a much worse situation than she appears to be."
    mc_t "Pills.... Hmm, what would she need them for? And so many, too.."

    show ep04_elimeet10 at subtle_zoom_out
    mc_t "That's a lot of cash too. What the hell is going on?"
    mc_t "Better put it back before she notices..."

    $ setChannelVolume("music", 3, 0.3, 1.0)
    $ playAudio(elizabeth_theme, "music", 3, True, 2.0, 1.0)

    show ep04_elimeet11 at ken_burns_bottom_to_top
    eli "Look what [mommy_r] brought! For us to share..."
    mc_s "[mo_r], come on - you've had enough."
    mc_s "Give me the bottle."

    show ep04_elimeet12
    eli "Don't you want to drink with me? Your own [mo_full_r_low]?"
    mc_s "You can barely stand up straight."
    eli "Then you'll have to catch me if I fall..."
    mc_s "At least sit down before you hurt yourself."

    scene eigengrau with slowfade
    show ep04_elimeet13 at ken_burns_left_to_right
    mc_s "[mo_r]... can we talk?"
    eli "Aren't we talking now, sweetie?"
    mc_s "You know what I mean. About... all this."

    show ep04_elimeet14 with slowfade
    eli "All what?"
    mc_s "This isn't like you. The drinking, coming home late..."
    eli "It's just one more glass... Get the nice ones from the cabinet?"
    show ep04_elimeet15 at subtle_zoom_out
    mc_t "Maybe if she opens up a bit... Plus I could use a drink myself."
    mc_t "Then again, enabling her probably isn't the best idea..."

    $ show_walkthrough("ep04_elimeetmenu_2")
    menu:
        "Get the glasses":
            hide screen walkthrough_screen

            mc_s "Just one glass."
            pass
        "Refuse":
            hide screen walkthrough_screen

            mc_s "No, [mo_r]. You've had enough."

            show ep04_elimeet16
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)

            mc_s "Talk to me. What's really going on?"
            eli "Nothing's 'going on'! Can't a [mo_full_r_low] have a drink?"
            eli "You disappear for years and now you're interrogating me?"
            mc_s "[mo_r], please calm down..."
            eli "Maybe you should just go to bed. Let [mommy_r] handle her own problems..."
            $ stopAllSubchannels("music", 2.0)

            show ep04_elimeet17 at ken_burns_corner_to_corner
            mc_s "Okay. We'll talk another time."
            mc_s "Just... take it easy with the wine, okay?"
            eli "Too late..."
            eli "Goodnight, baby..."
            if ep04_nanastay:
                mc_t "Great... now I'll have to sleep on the couch in my room."

                jump ep04_pazcall


            else:
                jump ep04_mad_mcroom


    show ep04_elimeet18
    $ rm.update("elizabeth", "cor", 2)
    $ check_levels("elizabeth", "cor", 2)
    $ rm.update("elizabeth", "trust", 0)
    $ check_levels("elizabeth", "trust", 0)
    eli "Such a good boy!"
    eli "Come sit with [mommy_r]..."
    eli "Just like old times..."
    show ep04_elimeet19 at ken_burns_corner_to_corner
    mc_s "Only two glasses..."
    eli "Hurry, hurry!"
    eli "[mommy_r]'s waiting..."
    $ stopAllSubchannels("music", 2.0)
    $ setChannelVolume("amb", 1, 0, 1.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.3, 1.0)

    show ep04_elimeet20 with circlewipe
    mc_s "Getting comfortable?"
    eli "Oh god, these heels are murder..."
    eli "My hero, coming to [mommy_r]'s rescue..."
    show ep04_elimeet21
    eli "Mmm... divine."
    eli "Don't you think, darling?"
    mc_s "It's... nice."

    show ep04_elimeet22
    eli "Now... what did you want to ask me?"
    mc_s "The pills in your bag. The money. What's going on?"
    eli "What?"
    show ep04_elimeet23
    eli "There's nothing in my bag, sweetie..."
    mc_s "[mo_r], I saw them. Are you in trouble?"
    eli "Of course not!"
    show ep04_elimeet24
    eli "Were you snooping in [mommy_r]'s purse?"
    eli "Such a naughty boy..."
    mc_s "You dropped it when you came in. Everything spilled out."
    eli "Oh... More wine, darling?"
    mc_s "Fine. One more."

    show ep04_elimeet25
    eli "You know what this is, baby?"
    eli "Domaine Takahiko. Very rare nowadays..."
    mc_s "That expensive, huh?"
    eli "Mmm... special occasion wine..."
    show ep04_elimeet26
    eli "About earlier - those are just supplements, sweetie. And the money's from my old modeling days!"
    mc_s "Supplements? That many?"
    eli "Just some things I found online..."
    show ep04_elimeet27 at subtle_zoom_in
    mc_t "God... she's completely unaware her legs are spread, that sheer underwear hiding absolutely nothing..."
    mc_s "That's a lot of cash for old modeling jobs, [mo_r]..."
    eli "You worry too much, darling..."
    eli "Those jobs paid very well, you know that..."
    mc_s "[mo_r], please don't lie to me..."

    $ setChannelVolume("music", 4, 0.2, 1.0)
    $ playAudio(elizabeth_sexy_theme2, "music", 4, True, 2.0, 1.0)

    show ep04_elimeet28
    eli "Naughty boy... staring at [mommy_r]'s panties..."
    mc_s "I wasn't... I mean..."
    eli "It's okay, baby... I know you can see everything..."
    show ep04_elimeet29
    eli "These are so tight... need them off..."
    mc_s "[mo_r]! What are you doing?"
    eli "Just getting comfortable with my baby boy..."
    show ep04_elimeet30 at ken_burns_left_to_right with normalfade
    eli "Remember when I used to walk around naked?"
    eli "Back when [mommy_r] was younger..."
    mc_s "Yeah, traumatized for life, thanks."
    eli "You were such an innocent little thing..."
    show ep04_elimeet31 with normalfade
    eli "So many regrets, baby..."
    eli "This industry... they use you like a puppet..."
    eli "Not just the modeling..."
    mc_s "What do you mean?"

    show ep04_elimeet32 at subtle_zoom_in
    mc_t "Seeing them so close, brings memories to me... She confused me so much when she used to show off like that..."
    eli "The choices we make, darling... how things should've been..."
    eli "Life's good when you don't think about tomorrow..."
    mc_s "[mo_r], I care about you, you know that?"
    eli "Of course you do, baby..."
    show ep04_elimeet33 with vpunch
    eli "That's why you keep staring at my breasts..."
    mc_s "What? No, I wasn't-"
    eli "Such a bad liar..."
    scene eigengrau with smoke
    show ep01_elidress07 with smoke
    eli "Remember this pose, darling?"
    eli "Just like old times..."
    scene eigengrau with smoke
    show ep04_elimeet33 with smoke
    mc_s "[mo_r], you don't have to..."

    show ep04_elimeet34
    eli "You're no fun anymore!"
    eli "Such a boring boy now..."
    mc_s "You look exhausted, maybe you should rest..."

    show ep04_elimeet35
    eli "Not yet! Still half a bottle left..."
    eli "Why so shy about [mommy_r]'s body?"
    show ep04_elimeet36
    eli "These breasts fed you, remember?"
    eli "When you were just a tiny thing..."
    mc_s "[mo_r], you're drunk... you don't know what you're doing..."
    eli "So boring now..."
    mc_s "It's not that, you know. I'm just genuinely concerned about you."

    $ stopAllSubchannels("music", 2.0)

    show ep04_elimeet37
    eli "Such a sweet boy though..."
    eli "[mommy_r] can handle herself, don't worry..."
    eli "Always my good boy..."
    mc_s "[mo_r], please..."
    eli "Always were such a perfect child..."
    show ep04_elimeet38
    eli "Then you left me..."
    eli "Never called, never wrote... forgot all about your [mo_full_r_low]..."
    eli "How could you be so cruel?"
    mc_s ". . ."

    show ep04_elimeet39
    eli "Left your [dau_r_low] too... your little girl..."
    eli "Missed everything... first steps, first words..."
    mc_s "I had no choice..."

    show ep04_elimeet40
    eli "But you're back now... that's what matters..."
    mc_s "What do you mean?"
    eli "Stay with [mommy_r]... forever..."
    eli "You're all she needs... her only [so_r_low], only love..."
    mc_s "[mo_r], the wine's talking..."
    eli "Just telling the truth..."
    show ep04_elimeet41
    eli "More wine!"
    mc_s "No more, [mo_r]. You've had enough."
    eli "Just a little more..."
    show ep04_elimeet42
    eli "Mmm... so good..."
    mc_s "Why are you so stubborn?"
    eli "Because it's delicious..."
    show ep04_elimeet43
    mc_s "You'll regret this tomorrow..."
    eli "No regrets when you're here..."
    eli "You'll take care of [mommy_r]..."
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False, 0, 0)

    show ep04_elimeet44 with vpunch
    mc_t "And there she goes... sprawled out like a ragdoll..."
    mc_s "[mo_r]? Maybe time for bed?"

    show ep04_elimeet45
    eli "I'm fine here..."
    eli "You can take me to bed whenever..."
    eli "Stay with me longer..."
    $ setChannelVolume("music", 4, 0.3, 1.0)
    $ playAudio(elizabeth_theme, "music", 4, True, 2.0, 1.0)

    show ep04_elimeet46 at ken_burns_right_to_left with normalfade
    mc_s "Come on, let's get you up..."
    eli "Having such a nice time..."
    mc_s "You can barely talk..."
    eli "Fine..."
    show ep04_elimeet47
    mc_s "You can't walk alone..."
    eli "Watch me! I'll prove it..."
    mc_s "This should be good..."

    show ep04_elimeet48
    eli "These are so tight..."
    eli "Don't mind [mommy_r]'s panties, do you?"
    mc_s "Would it matter if I did?"
    eli "Not at all..."
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bodyfall, "sfx", 5, False, 0, 0)

    show ep04_elimeet49 at impact_shake with vpunch
    eli "Oops!"
    eli "Maybe you were right..."
    mc_s "You think?"

    show ep04_elimeet50 with normalfade
    eli "Baby... carry me to the bathroom?"
    mc_s "After all that wine, of course..."
    eli "Then you can leave [mommy_r] alone..."
    show ep04_elimeet51 with normalfade
    mc_t "She's changed so much..."
    mc_t "Everything feels wrong here..."
    mc_t "What kind of trouble is she in?"

    show ep04_elimeet52 at ken_burns_left_to_right
    eli "So strong now... those arms..."
    eli "Your smell... so different..."
    mc_s "You haven't changed much..."
    eli "Such a sweet liar..."
    show ep04_elimeet53
    eli "Here's fine, darling..."
    mc_s "Sure? You'll fall again..."
    eli "Toilet's right there..."
    eli "Wait outside? Won't be long..."
    mc_s "Let me help you in..."
    eli "If it makes you happy..."
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.25
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)

    show ep04_elimeet54
    eli "Thank you, baby..."
    mc_s "Just don't want you hurt..."
    eli "Always caring..."
    show ep04_elimeet55
    eli "Stay? Just until I finish..."
    mc_s "[mo_r], what? No, I'll--"

    show ep04_elimeet56
    eli "Don't go!"
    eli "Too drunk to balance..."
    eli "I'll show you..."
    show ep04_elimeet57 at ken_burns_top_to_bottom with normalfade
    mc_s "[mo_r]! Some modesty!"
    eli "Need to pee, darling..."
    eli "Want me to wet myself?"
    mc_s "That's not..."

    show ep04_elimeet58
    eli "Not as pretty as before..."
    eli "Don't have to look..."
    eli "Just hold [mommy_r] up..."
    mc_t "She might fall again..."

    $ show_walkthrough("ep04_elimeetmenu_3")
    menu:
        mc_t "Help her or leave?"
        "Stay and watch":
            hide screen walkthrough_screen

            mc_s "Alright, [mo_r]. Let's just finish this as soon as possible."

            $ ep04_elilook = True
            $ ep04_elistay = True

            show ep04_elimeet60
            $ rm.update("elizabeth", "trust", 2)
            $ check_levels("elizabeth", "trust", 2)
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
            eli "Such a good boy..."
            eli "You'll watch? In case I fall?"
            mc_s "Just hurry..."

            jump ep04_elizabeth_gold


        "Stay but look away":
            hide screen walkthrough_screen

            mc_s "I'll help, but I'm not looking..."

            $ ep04_elistay = True

            show ep04_elimeet59
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
            eli "Don't want to watch?"
            mc_s "Of course not..."
            eli "Just teasing, baby..."
            $ setChannelVolume("amb", 1, 0, 1.0)
            jump ep04_elizabeth_gold


        "Leave":
            hide screen walkthrough_screen

            mc_s "Handle this yourself, [mo_r]. Hold the wall..."

            show ep04_elimeet61
            $ rm.update("elizabeth", "trust", -2)
            $ check_levels("elizabeth", "trust", -2)
            eli "If that's how you feel..."
            mc_s "Just... ease up on the drinking..."
            eli "If that's what you want..."
            mc_s "Sleep well, [mo_r]."

            $ stopAllSubchannels("amb", 2.0)
            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.25
            $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
            $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)
            $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
            $ playAudio(sfx_fireplace, "amb", 2, True, 1.5, 0)

            show ep04_eligold31 with circlewipe
            mc_t "This [fm_r_low]'s so fucked up..."
            mc_t "No wonder I am how I am..."
            mc_t "Need sleep..."

            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall




label ep04_elizabeth_gold:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    if ep04_elilook:
        show ep04_eligold01 with normalfade
        mc_t "God... her smile's completely gone. Like every ounce of joy just drained away..."
        mc_t "Hard to believe this is the same woman who used to light up every room. Now she's just... empty."

        show ep04_eligold02
        eli "Look at what time's done to your [mo_full_r_low], sweetie... disgusting, isn't it?"
        eli "All these wrinkles... this saggy skin... thank god these fake tits were worth the money..."
        $ show_walkthrough("ep04_eligolmenu")
        menu:
            "Look down":
                hide screen walkthrough_screen
                show ep04_eligold03
                $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
                $ playAudio(sfx_piss_fem, "sfx", 1, False, 0, 0)
                $ rm.update("elizabeth", "cor", 2)
                $ check_levels("elizabeth", "cor", 2)
                eli "Be honest with [mommy_r]... what do you see?"
                mc_t "Damn... how am I supposed to answer while she's showing her pussy like this..."

                show ep04_eligold04
                eli "Even my pussy's given up on me... all loose and hanging... Bet you've seen prettier ones in Osaka..."
                mc_s "God! [mo_r]... you can't just say stuff like that..."

                show ep04_eligold07
                eli "Mmm... for someone so shocked, you sure can't stop looking..."
                mc_s "I... well... that's..."

                show ep04_eligold06
                eli "It's okay baby... [mommy_r] doesn't mind if you look..."
                eli "Just tell me the truth... do I disgust you? Is your [mo_full_r_low] just another dried-up old slut now?"
                mc_s "[mo_r], stop it. You're beautiful. Always have been, always will be. Age doesn't change that."

                show ep04_eligold08 at ken_burns_bottom_to_top
                eli "My precious boy... always knows exactly what to say...."
                eli "Such a good [so_r_low]... making [mommy_r] feel young again..."
                mc_s "[mo_r]... your breasts..."

                $ stopAllSubchannels("sfx", 2.0)
            "Keep looking her":
                hide screen walkthrough_screen
                show ep04_eligold05
                $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
                $ playAudio(sfx_piss_fem, "sfx", 1, False, 0, 0)
                eli "Tell [mommy_r] what you see in these old eyes..."
                eli "Everything's sagging now... even my poor pussy's given up. Time's such a cruel bastard..."
                mc_s "[mo_r], please... too much information..."
                eli "Just tell me truth... am I repulsive now? Just another aging woman past her prime?"
                show ep04_eligold08 at ken_burns_bottom_to_top
                mc_s "You're gorgeous, [mo_r]. Always have been. Age changes nothing."
                eli "Such a sweet boy..."
                eli "Making your old [mo_full_r_low] feel like a woman again..."
                mc_s "Um, [mo_r]... your breasts..."

                $ stopAllSubchannels("sfx", 2.0)

        show ep04_eligold09
        eli "Haha! What about them, honey?"
        eli "Don't worry sweetie... I promise they won't bite... unless you want them to..."
        mc_s "They're literally just... out there..."

        show ep04_eligold11 at ken_burns_top_to_bottom
        eli "Oh my... how naughty of them..."
        mc_s "Shouldn't you maybe... cover up?"
        eli "Well..."
        show ep04_eligold10
        eli "Why? Is your old [mo_full_r_low] too much for you to handle?"
        mc_s "That's... that's not what I..."

        show ep04_eligold12
        eli "Then enjoy the view, baby... nothing here you haven't sucked on before..."
        mc_s "God! [mo_r]... I was an infant..."
        eli "Mmm... and by that bulge, seems like someone wants to be a baby again..."
        mc_s "[mo_r]! You can't just... fuck..."

        show ep04_eligold13
        eli "Tell [mommy_r] something... were these really your first tits?"
        mc_s "Y-yeah..."
        eli "And now look at you... all grown up... do they still make you hard like they used to?"
        mc_s "[mo_r]... this is so wrong..."

        show ep04_eligold14
        eli "Just teasing you, darling!"
        eli "But if I can still make my big strong boy squirm... maybe [mommy_r]'s still got it after all..."
    else:
        pause 1.0
        scene eigengrau with slowfade
        $ setChannelVolume("amb", 1, 0.3, 1.0)

        show ep04_eligold15 with circlewipe
        eli "All done sweetie. Your [mo_full_r_low]'s decent again..."
        eli "You can turn back."
    jump ep04_elizabeth_kiss




label ep04_elizabeth_kiss:
    show ep04_eligold16
    eli "Thank you for taking care of me, baby..."
    mc_s "Someone has to. You're too drunk to manage alone."
    mc_s "And don't worry about all that stuff you said. The wine was talking."

    show ep04_eligold17
    eli "You're too good to [mommy_r]..."
    eli "Help me to the stairs? These legs aren't too steady..."
    mc_s "Come on, let's go."

    $ stopAllSubchannels("amb", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.25
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)

    show ep04_eligold18 with circlewipe
    mc_s "Wait. One more thing."
    eli "Hmm?"
    mc_s "This lifestyle... the drinking, those pills you're popping like candy. It's killing you, [mo_r]."

    $ setChannelVolume("music", 3, 0.3, 1.0)
    $ playAudio(elizabeth_theme, "music", 3, True, 2.0, 1.0)

    show ep04_eligold19 with normalfade
    eli "Baby, I'm fine. Don't fuss over [mommy_r]..."
    mc_s "No, you're not fucking fine! Look at you!"
    mc_s "You are just drinking and just spending the night outside doing god knows what."
    eli "Just drinking alone in bars, sweetie. Nothing exciting..."
    eli "The alcohol... the pills... they help me sleep. Make everything... quieter."
    show ep04_eligold20
    eli "Don't lecture me. I'm still your [mo_full_r_low], even if I'm a pathetic one."
    mc_s "Someone has to say something, [mo_r]. You're destroying yourself."
    eli "I'm not worth saving, darling."
    eli "A failure like me deserves this. Just let me fade away..."
    mc_s "[mo_r]... stop it."

    show ep04_eligold22
    mc_s "Look, I know I'm the last person who should talk, but... you're worth so much more than this. You deserve better."
    mc_s "People still love you. Me, Isabella, Amber..."
    eli "Isabella, maybe. Amber and Madison want nothing to do with their worthless [mo_full_r_low]."
    eli "Your [da_full_r_low] made that clear enough... 'Just a dried-up cunt now' he said. Like a knife through my heart..."
    show ep04_eligold21
    mc_s "[da_r]'s a fucking piece of shit! He never deserved you!"
    mc_s "I don't know what's wrong with Amber and Madison, but you're still a great [mo_full_r_low]. Always have been."
    eli "Baby..."
    eli "Could... could [mommy_r] have a hug?"
    mc_s "Come here..."

    show ep04_eligold24
    eli "You came back when I needed you most..."
    eli "So strong now... like a shield around [mommy_r]... keeping all the bad things away..."
    eli "Feel so safe in your arms..."
    show ep04_eligold23
    eli "If things were different... maybe we could..."
    mc_s "Could what, [mo_r]?"
    eli "Nothing! Forget I said anything..."
    mc_s "[mo_r], tell me..."
    eli "Just... thank you for coming home. When I needed you..."
    mc_t "What is she-"

    show ep04_eligold26
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.6)
    $ playAudio(sfx_kiss_one, "sfx", 1, False, 0, 0)

    mc_s ". . ."
    mc_t "Holy shit... did she just kiss me on the lips?"

    show ep04_eligold25
    eli "I... I need to..."
    eli "I have to go..."
    show ep04_eligold27 with normalfade
    eli "I'm so sorry... that won't... I didn't mean..."
    eli "I don't know what came over me..."
    mc_s "It's okay, [mo_r]. You're drunk..."

    show ep04_eligold28
    eli "Yes... just drunk..."
    eli "Who'd want to kiss these old lips anyway?"
    mc_s "[mo_r], don't..."

    show ep04_eligold29
    eli "Having you back... makes this place feel like home again. Not just... empty walls and silence."
    mc_s "[mo_r]..."
    eli "I need to be alone now. Goodnight, baby..."
    eli "Sweet dreams, honey. May angels sing you to sleep."
    mc_s "Yeah... goodnight..."

    show ep04_eligold30 at subtle_zoom_in with normalfade
    mc_t "Fuck... wasn't expecting that."
    mc_t "Our relationship's always been weird but this... this is something else."
    mc_t "Why am I seeing her as a woman and not... fuck, what's wrong with me?"
    mc_t "This house is messing with my head..."

    $ stopAllSubchannels("music", 2.0)
    $ setChannelVolume("amb", 1, 0, 1.0)
    pause 1.0
    scene eigengrau with slowfade
    $ setChannelVolume("amb", 1, 0.3, 1.0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_fireplace, "amb", 2, True, 1.5, 0)

    show ep04_eligold31 with circlewipe
    $ ep04_ach_elizabeth = True

    mc_t "I'm losing it. This whole day's been one massive mindfuck."
    mc_t "This couch looks good enough... and passing out sounds perfect right now..."

    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall




label ep04_isabella_mcroom:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_mc_room_night, "amb", 1, True, 1.5, 0)

    show ep04_isamcroom01 with circlewipe
    mc_t "Fuck... these thoughts are so messed up. Why am I getting turned on by the idea of corrupting her?"
    mc_t "Some cop I am. Should be protecting innocence, not fantasizing about destroying it. But damn... there's just something about her..."

    $ setChannelVolume("sfx", 1, 0.2)
    $ playAudio(sfx_sighbreathfem, "sfx", 1, False, 0, 0)

    show ep04_isamcroom02
    mc_t "Can't get it out of my head - the way she carries that innocence around like a shield."
    mc_t "And here I am, thinking about tearing it all down..."
    mc_t "She's like this perfect, untouchable thing. And that just makes me want to..."
    mc_t "God, I need help. Seriously fucked up to think about her like this..."

    $ setChannelVolume("sfx", 2, 0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 2, False, 0, 0)
    $ setChannelVolume("music", 1, 0.4)
    $ playAudio(isabella_serious, "music", 1, True, 4, 0)

    show ep04_isamcroom03 with hpunch
    isa "What were you and Nanami doing in the kitchen?"
    mc_s "Shit- Isabella! You scared me. Why aren't you in bed?"

    show ep04_isamcroom04
    isa "You're dodging my question, [da_r]. What was she doing here so late?"
    mc_s "Just getting some milk, that's all..."
    isa "Really? Milk? At this hour?"
    mc_s "Look, that's what happened. Nothing more to it."

    show ep04_isamcroom05
    isa "Come on, [da_r]. I'm not stupid. What aren't you telling me?"
    mc_s "Nothing, baby. Really."
    mc_t "How do I always end up in these situations? Fuck my life..."

    show ep04_isamcroom06
    isa "I saw everything, you know. The way she was dressed... why she really came here..."
    mc_s "She was just wearing her normal stuff. You're reading too much into this."
    mc_t "This is getting worse by the second."
    isa "God, [da_r], you're so blind! She's playing the innocent card to get to you. Can't you see she's just manipulating you?"
    mc_s "It's not like that. She's just... shy. That's all."

    show ep04_isamcroom08
    isa "What makes her so special, huh? What does she have that I don't?"
    mc_s "There's nothing going on between us, Isabella."
    isa "Is it how she dresses? You want me dressing like that too?"
    mc_s "Those are just her pajamas. She likes sleeping in that kind of stuff."

    show ep04_isamcroom07 at ken_burns_top_to_bottom
    isa "Look at me! I can look good without dressing like some... you know what I mean!"
    isa "You think she's prettier than me, don't you?"
    $ stopAudio("music", 1, 2)

    hide ep04_isamcroom07
    mc_s "Hey, stop that. You're the most beautiful girl in the world. You don't need to dress any different."

    $ setChannelVolume("music", 3, 0.2, 0)
    $ playAudio(isabella_theme, "music", 3, True, 2.0, 1.0)

    show ep04_isamcroom09 with normalfade
    mc_s "Nobody compares to you, Isabella. Especially not her."
    isa "You really mean that?"
    mc_s "Of course I do. Look, it's late - we should both get some sleep. We can talk more tomorrow, okay?"

    show ep04_isamcroom10
    isa "Fine... but remember what you promised - always be honest with me."
    mc_s "I remember. We'll talk tomorrow."
    mc_t "What a fucking mess this turned into..."

    show ep04_isamcroom11
    mc_s "Night, Isabella."
    isa "Night, [daddy_r]. Sweet dreams."
    show ep04_isamcroom12
    isa "Just remember - you're MY [da_r]. Nobody else's."
    mc_s "I know, baby. Don't worry about it."

    $ setChannelVolume("music", 3, 0, 2.0) 

    show ep04_isamcroom13 with normalfade
    mc_t "This is getting out of control..."
    mc_t "How am I supposed to handle both Isabella and Nanami?"

    show ep04_isamcroom14
    mc_t "Need to figure this shit out before it explodes in my face..."

    $ setChannelVolume("sfx", 1, 0.7)
    $ playAudio(sfx_footsteps_bare_wood, "sfx", 1, False, 0, 0)

    show ep04_isamcroom15 with normalfade
    mc_s "Huh?"

    show ep04_isamcroom16
    mc_s "What the-"

    $ stopAudio("sfx", 1, 1.5)
    $ setChannelVolume("sfx", 2, 0.7)
    $ playAudio(sfx_jump_to_floor, "sfx", 2, False, 0, 0)

    show ep04_isamcroom17
    isa "Catch me, [daddy_r]!"
    mc_s "Whoa, Isabella! What are you doing?"

    show ep04_isamcroom18
    mc_t "She really is beautiful. Like something out of a dream..."

    $ setChannelVolume("sfx", 2, 0.7)
    $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)

    show ep04_isamcroom19 at impact_shake
    isa "I love you so much, [daddy_r]! You're the best!"
    mc_s "Love you too, sweetheart."
    mc_t "How did we get here?"

    $ setChannelVolume("music", 3, 0.2, 2.0) 
    $ setChannelVolume("sfx", 3, 0.7)
    $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)

    show ep04_isamcroom20 with vpunch
    mc_t "Where'd this come from?"
    isa "Just showing my [daddy_r] some love!"
    mc_s "You're something else, you know that?"
    mc_t "This clingy behavior... something's up."
    mc_s "What's gotten into you tonight?"

    show ep04_isamcroom21 with normalfade
    isa "Can't a girl just want to spend time with her [da_r]? Is that so weird?"
    mc_s "Come on, Isabella. What's really going on? This isn't like you."
    isa "Maybe I just missed being close to you..."
    mc_t "There's definitely more to this."
    mc_s "Remember what you said about honesty? Works both ways."

    show ep04_isamcroom22
    isa "Fine... seeing Nanami all over you made me jealous, okay? I just... I want to show you I'm better than her."
    mc_s "Oh, baby... you don't need to be jealous. You're my number one, always will be."

    show ep04_isamcroom23
    isa "You promise?"
    mc_s "With all my heart."
    mc_t "Can't let this jealousy thing get worse..."
    isa "I just want to be perfect for you, [daddy_r]. That's all I want."
    mc_s "You already are, sweetheart. Never doubt that."

    $ stopAllSubchannels("music", 2.0)

    show ep04_isamcroom24 with vpunch
    if ep04_nanadad:
        isa "Then why does she call you '[daddy_r]' too?! What's up with that?!"
    else:
        isa "Then why do you let her act like she's your [dau_r_low]?! What's that about?!"
    mc_s "What are you talking about?"
    if ep04_nanadad:
        isa "She calls you '[daddy_r]' - just like I do! Why?!"
        mc_s "It's just a word to her, Isabella. Doesn't mean anything."
        isa "No! It's OUR thing! OURS!"
    else:
        isa "The way she acts around you - like she's your [dau_r_low]! And you just let her!"
        mc_s "I'm just being nice, Isabella. It's nothing."
        isa "That's not nothing! What we have is special!"
    isa "Don't let her take that away!"
    mc_s "Nobody's taking anything away. You're my girl, always."

    show ep04_isamcroom25
    isa "I don't trust her. That's why I'm staying here tonight - to keep an eye on things!"
    mc_s "Come on, isn't this a bit much? You're being ridiculous."
    isa "No! She's not stealing you away from me!"
    $ show_walkthrough("ep04_isamcmenu")
    menu:
        "Let her stay":
            hide screen walkthrough_screen

            mc_s "Alright, alright. You can stay. Just... calm down, okay?"

            jump ep04_isabella_nobra


        "Send her away":
            hide screen walkthrough_screen

            mc_s "No, you need to sleep in your own room tonight. That's final."

            show ep04_isamcroom26
            $ rm.update("isabella", "trust", -2)
            $ check_levels("isabella", "trust", -2)
            isa "Why are you pushing me away?! Why don't you want me here?!"
            mc_s "This isn't normal, Isabella. This isn't how fathers and daughters act."
            isa "You don't get it! She's trying to take you from me!"
            mc_s "Enough! You're being paranoid and possessive."

            show ep04_isamcroom27
            isa "Fine! Go ahead and pick anyone over me - just like always!"
            isa "Not like I should be surprised anymore!"
            mc_s "That's not what this is about! You know that!"

            scene eigengrau with normalfade
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            pause 1.25
            show ep04_isamcroom28
            mc_t "Did I just screw everything up? What's happening with her?"
            mc_t "I'm trying to do the right thing here... aren't I?"
            mc_t "Yeah, she's clingy because of the past, but... don't I deserve some space?"
            mc_t "Am I really choosing others over her?"
            mc_t "Maybe she just needs time to cool off. She'll understand... right?"
            mc_t "Whatever. I'll deal with this tomorrow."
            mc_t "She's gotta calm down eventually..."

            $ stopAllSubchannels("amb", 2.0)
            jump ep04_pazcall




label ep04_isabella_nobra:
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep04_isanobra01
    isa "I guess I was right all along... you always choose them over me, don't you, [daddy_r]?"
    mc_s "Isabella, I literally just said you could stay. What are you still arguing about?"

    show ep04_isanobra02
    isa "Oh? You're really letting me stay?"
    mc_s "Yes, but we need to talk about this jealousy thing. It's getting out of hand."

    show ep04_isanobra03
    $ rm.update("isabella", "trust", 2)
    $ check_levels("isabella", "trust", 2)
    isa "Yay! You're the bestest [daddy_r] ever!"
    isa "I love you sooo much!"
    mc_s "Careful there, don't hurt yourself."

    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(isabella_sexy, "music", 1, True, 2.0, 1.0)

    show ep04_isanobra04
    isa "Hey [daddy_r]... you know what I've always wondered?"
    isa "Do you know how bra clasps work? They're so tricky sometimes..."
    mc_s "That's... not really appropriate for us to discuss."
    isa "But who else can I ask? It's not like [mommy_r]'s around to help..."
    isa "Please help your little girl?"
    mc_s "I mean... yes, I know how they work."
    mc_s "Why are you asking?"

    show ep04_isanobra05
    isa "So if you can put them on... you must know how to take them off too, right?"
    mc_s "Hold up. What's this about?"
    isa "I just can't sleep with it on - it hurts. Won't you help me, [daddy_r]?"
    mc_s "Isabella, you're old enough to handle that yourself."
    isa "Pretty please? Just this once? I really need my [daddy_r]'s help..."
    $ show_walkthrough("ep04_isanobramenu")
    menu:
        "Help her":
            hide screen walkthrough_screen

            mc_s "Fine... turn around. Let's get this over with."
            isa "You're the best [daddy_r] ever!"
            show ep04_isanobra06
            $ rm.update("isabella", "cor", 2)
            $ check_levels("isabella", "cor", 2)

            mc_s "Your shirt's too tight, I can't..."
            isa "I could always take it off..."
            mc_s "No! Absolutely not!"

            show ep04_isanobra07
            isa "But [daddy_r], you're just helping your little girl. What's wrong with that?"
            mc_s "This doesn't feel right. You're grown up now..."
            isa "But you promised to help... and [daddy_r] always keeps his promises, right?"
            show ep04_isanobra08
            isa "I know! What if you turn around while I take off my shirt? Then you can just help with the clasp?"
            mc_s "Yeah... okay, that works."
            mc_s "Just tell me when."
            mc_t "How do I get myself into these situations..."

            show ep04_isanobra09
            isa "Aww, is my [daddy_r] being shy? That's so sweet!"
            mc_s "I'm being respectful. Let's just do this."
            isa "Okay, you can turn around now."
            scene eigengrau with slowfade
            isa "Ready, [daddy_r]!"
            mc_s "That was quick. Let's make this fast."

            show ep04_isanobra13
            isa "Ta-da!"
            isa "What do you think? Aren't I pretty, [daddy_r]?"
            mc_s "Isabella... don't."
            mc_s "Let's just finish this."
            isa "I was just playing! You're so serious sometimes, [daddy_r]!"
            show ep04_isanobra14
            mc_s "Stay still..."
            mc_s "Almost done."

            show ep04_isanobra15
            mc_s "There. Now put your shirt back on."
            isa "Thank you, [daddy_r]!"
            isa "You're the best ever."
            isa "Um... maybe help with my shirt too?"
            isa "Please?"
            mc_s "No. You can handle that yourself."
            mc_s "I'm not your personal dresser."
            mc_s "You're getting too old for this kind of thing."

            show ep04_isanobra16
            isa "Oh no... I accidentally threw it on your bed. Could you get it for me?"
            isa "Pretty please?"
            mc_s "Damn- Isabella! Cover yourself!"
            mc_s "You're not a kid anymore!"
            isa "But [daddy_r], we're [fm_r_low]. Why are you being so weird about it?"
            isa "Don't you love me anymore?"
            show ep04_isanobra17
            mc_s "Here's your shirt."
            mc_s "Don't do this again."
            isa "Thanks, [daddy_r]!"
            isa "You don't have to be so shy. [fm_r] shouldn't have secrets, right?"
            mc_s "Just get dressed. I'm done."
            isa "Okay, you can turn around now!"
            scene eigengrau with slowfade
            isa "All done!"
            show ep04_isanobra10
            mc_s "You're still half-dressed!"
            isa "Oopsie! Silly me!"
            mc_s "Just... put it on."

            show ep04_isanobra11
            isa "Don't be mad, [daddy_r]. You know I just want to make you happy..."
            mc_s "I'm trying to be responsible here. You're not making it easy."
            isa "I'll be good now. Promise!"
            show ep04_isanobra12
            isa "See? All better now. Happy, [daddy_r]?"
            mc_s "Yes, thank you. Can we sleep now?"
            isa "Of course, [daddy_r]."
        "Dont help her":
            hide screen walkthrough_screen

            mc_s "No way. That's not happening."
            mc_s "I can't do that."

            show ep04_isanobra07
            $ rm.update("isabella", "trust", 1)
            $ check_levels("isabella", "trust", 1)
            isa "I see... I guess I'll just do it myself then."
            isa "Even though you're the only one I can trust..."
            scene eigengrau with slowfade
            show ep04_isanobra10
            mc_s "Wait... are you sure about this?"
            mc_s "Maybe I should leave..."
            isa "It's fine, [daddy_r]. Just don't look, okay?"
            isa "Usually Madison helps me, but... well, you know."
            mc_s "Just... hurry up."

            scene eigengrau with slowfade
            show ep04_isanobra11
            isa "All done! See? That wasn't so bad."
            mc_s "You could've warned me about showing your... um..."
            isa "About my little peek-a-boo? Don't be shy, [daddy_r]..."
            show ep04_isanobra12
            isa "Not like there's much to hide anyway... I'm still growing, you know?"
            mc_s "Let's just go to sleep."
            isa "Whatever you say, [daddy_r] dearest."
    jump ep04_isabella_sleepnight




label ep04_isabella_sleepnight:
    show ep04_isanight01
    isa "I can't believe I finally get to sleep next to my [daddy_r]!"
    mc_s "Come on over here, babygirl. Time for bed."
    isa "Thank you, [daddy_r]!"
    show ep04_isanight02 at ken_burns_top_to_bottom with vpunch
    mc_s "Whoa- Isabella, what are you doing?"
    isa "Just getting comfy. Is something wrong?"
    mc_s "You're taking off your pants - that's what's wrong!"

    show ep04_isanight03
    isa "But [daddy_r], I always sleep like this. You want me to be comfortable, don't you?"
    mc_s "This isn't the time for games. Put them back on and let's sleep."

    show ep04_isanight04
    isa "Don't be silly, [daddy_r]. It's nothing you haven't seen before..."
    isa "Remember this afternoon? When I was drying my hair?"
    isa "What's different now?"
    show ep04_isanight05 at ken_burns_bottom_to_top
    mc_s "That was different. This crosses a line - we're sharing a bed, Isabella."
    isa "But we're just sleeping, silly! What's wrong with that?"
    isa "You wouldn't want your little girl to be all uncomfortable, would you?"
    mc_s "Fine... but this isn't becoming a regular thing."

    show ep04_isanight07
    isa "You're the best, [daddy_r]!"
    isa "You know something? Even though you were... away... for a while, you're still the best thing that's ever happened to me."
    mc_s "I don't deserve that, Isabella."
    isa "Don't say that!"
    isa "You're everything I could want in a [daddy_r_low]."
    show ep04_isanight06 at ken_burns_bottom_to_top
    mc_s "How can you say that after everything I've put you through?"
    isa "All that matters is you're here now, [daddy_r]. With me."
    isa "Let's just focus on now, okay? The past is the past."
    mc_s "Where did you get such a positive outlook? It amazes me."

    show ep04_isanight08
    isa "From you, silly! Even when you left... you taught me something important."
    isa "You showed me that real love is worth fighting for, no matter what. That you have to chase it until you catch it..."
    mc_s "I... I don't know what to say..."
    isa "And I found it again, [da_r]. This time I'm not letting go, just like you taught me."
    show ep04_isanight09 at ken_burns_right_to_left
    isa "Promise me something, [daddy_r]? Promise you won't leave your babygirl again?"
    mc_s "I promise, Isabella. You have my word."
    isa "Thank you, [daddy_r]. Let's get some sleep now?"
    mc_s "Yeah... let me get the lights."

    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with normalfade
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 5, True, 1.5, 0)

    show ep04_isanight10
    mc_t "Damn... when did she get so... No, can't think like that."
    isa "Penny for your thoughts, [daddy_r]?"
    mc_s "Just thinking it's late. We should sleep."
    isa "Is that really all?"
    mc_s "Yes. Now let's get some rest."

    show ep04_isanight11
    isa "Look [daddy_r], I'm being such a good girl..."
    mc_s "Isabella! Put your legs down!"

    show ep04_isanight12
    isa "What's wrong? Don't you think they're pretty?"
    mc_s "That's not the point. Stop being so... you know what you're doing."
    isa "Doing what, [daddy_r]? I'm just being me!"
    mc_s "No games. Just get in bed properly."

    show ep04_isanight13
    isa "Okay, okay... no need to be such a grumpy [daddy_r_low]."
    mc_s "I'm not grumpy. Just... behave yourself."
    mc_s "Let's just sleep, alright?"

    show ep04_isanight14
    isa "Of course, [daddy_r]!"
    isa "But don't forget to hold me tight..."
    isa "Wouldn't want to get cold in the night."
    mc_s "Alright, babygirl."
    mc_s "Goodnight, Isabella."
    isa "Night night, [daddy_r]!"
    $ setChannelVolume("sfx", 3, 0.7)
    $ playAudio(sfx_bedmove, "sfx", 3, False, 0, 0)

    show ep04_isanight15 with normalfade
    mc_t "This is gonna be one hell of a long night..."
    mc_t "Just hope she doesn't try anything else. Already more than I bargained for."

    $ setChannelVolume("amb", 5, 0, 1.0)
    if ep04_mcdrunk:
        jump ep04_isabella_dream


    else:
        jump ep04_isabella_masturbation




label ep04_isabella_dream:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 5, 0.3, 1.0)

    show vignette zorder 1.0 at pov_die
    show ep04_isanight24
    mc_t "Huh?"
    mc_t "Something woke me..."
    isa "Mmmm..."
    $ setChannelVolume("sfx", 1, 0.6)
    $ playAudio(sfx_moan_breath, "sfx", 1, False, 0, 0)

    show ep04_isanight25
    mc_t "Is she...?"
    isa "Ahhh..."
    mc_t "Oh god..."
    isa "Ohhh..."
    $ setChannelVolume("sfx", 2, 0.4)
    $ playAudio(sfx_moan_breath2, "sfx", 2, False, 0, 0)

    show ep04_isanight26
    mc_t "Those moans... fuck, I shouldn't be listening to this."
    mc_t "Just a dream, has to be just a dream."
    mc_t "I need to sleep. Just... sleep."

    $ stopAllSubchannels("amb", 2.0)
    scene eigengrau with clouds
    hide vignette
    if ep04_isatruth:
        $ setChannelVolume(channel="amb", subchannel=8, volume=0.3)
        $ playAudio(sfx_wind_pool, "amb", 8, True, 1.5, 0)
        $ setChannelVolume("music", 1, 0.3, 1.0)
        $ playAudio(heaven_theme, "music", 1, True, 2.0, 1.0)

        show ep04_isaheaven01 at focus_pulse with clouds
        mc_t "What the... Where am I?"
        mc_t "Is this a dream? Why am I watching myself from outside my body?"

        show ep04_isaheaven02 at ken_burns_left_to_right with normalfade
        mc_t "Someone's there..."
        mc_t "Coming closer in the moonlight... those curves..."

        show ep04_isaheaven03 at ken_burns_bottom_to_top with normalfade
        mc_t "God... she's incredible."
        mc_t "The way the moonlight catches her body... I can't stop staring..."

        $ setChannelVolume("sfx", 1, 0.8)
        $ playAudio(sfx_bed_creaking, "sfx", 1, False, 0, 0)

        show ep04_isaheaven04 with vpunch
        mc_t "What's she planning? The way she's moving..."
        mc_t "Something about her... I should look away but I can't..."

        $ setChannelVolume("sfx", 2, 0.8)
        $ playAudio(sfx_bed_laying, "sfx", 2, False, 0, 0)

        show ep04_isaheaven05 with normalfade
        mc_s "Isabella?"
        mc_s "Baby... this isn't right. You shouldn't be here."
        mc_s "This has to stop..."
        isa "[daddy_r]... look how perfectly we fit together."
        show ep04_isaheaven06 with normalfade
        isa "Just you and me, in this... bed."
        mc_s "Isabella, please... get off me."
        isa "Feel how warm I am? How soft?"
        isa "Don't fight this divine connection..."
        mc_s "We can't... this is wrong!"

        show ep04_isaheaven07 at subtle_zoom_in
        isa "Look at my ass, [daddy_r]..."
        isa "So pure... so ready to be blessed by you..."
        mc_s "Isabella, stop this!"
        mc_s "This is wrong!"
        isa "Nothing is wrong in paradise..."
        $ setChannelVolume("sfx", 3, 0.4)
        $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

        show ep04_isaheaven08 with vpunch
        isa "Watch your babygirl touch herself, [daddy_r]..."
        isa "See how wet you make your little blessing?"
        mc_s "Please stop..."
        mc_s "This isn't right..."

        show ep04_isaheaven09
        isa "But [daddy_r], don't you want to feel my virgin pussy against your hard cock?"
        isa "Dripping holy nectar just for you..."
        isa "Let me be your salvation..."
        mc_s "Isabella, stop!"
        isa "Let me show you something first..."
        mc_s "What are you..."

        scene white with flash
        $ setChannelVolume("sfx", 4, 0.4)
        $ playAudio(sfx_wings, "sfx", 4, False, 0, 0)

        show ep04_isaheaven10 at subtle_zoom_out with slowflash
        isa "Your perfect angel, [daddy_r]..."
        isa "Pure as heaven, wet as sin..."
        isa "Am I holy enough for you?"
        mc_s "I... I can't..."

        show ep04_isaheaven11
        isa "This is divine destiny, [daddy_r]..."
        isa "Our sacred union..."
        mc_s "You're my [dau_r_low]..."
        isa "I'm your everything - your angel to corrupt, your blood to taint, [mo_full_r_low]'s beauty to possess..."
        isa "And I'll never fall from your grace like she did..."
        mc_s "I shouldn't want this..."

        scene white with flash
        $ setChannelVolume("sfx", 4, 0.4)
        $ playAudio(sfx_wings, "sfx", 4, False, 0, 0)

        show ep04_isaheaven12 with slowflash
        isa "Let your angel guide you to bliss..."
        isa "See how my holy pussy weeps for you?"
        isa "Don't you want to drink from this sacred cup?"
        isa "Give in to heaven..."
        mc_s "Isabella, no! You're my [dau_r_low]!"
        isa "That makes it more divine..."
        isa "The holiest fruit is forbidden..."
        show ep04_isaheaven13 with slowflash
        isa "Gaze upon your angel..."
        isa "My holes aching for your blessing..."
        isa "Don't you want to consecrate me?"
        isa "Fill me with your holy seed..."
        isa "Touch your angel..."
        isa "Feel this heavenly body..."
        isa "Anoint me..."
        mc_s "This is sin..."
        mc_s "We can't..."

        show ep04_isaheaven14 at ken_burns_right_to_left with slowflash
        isa "I am your divine judgment!"
        isa "Your angel of destiny!"
        isa "Paradise is within me..."
        isa "Your soul is mine..."
        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("music", 2.0)
    else:
        $ setChannelVolume(channel="amb", subchannel=8, volume=0.3)
        $ playAudio(sfx_fireplace, "amb", 8, True, 1.5, 0)
        $ setChannelVolume("music", 1, 0.3, 1.0)
        $ playAudio(hell_theme, "music", 1, True, 2.0, 1.0)

        show ep04_isahell01 at focus_pulse with clouds
        mc_t "This red light... where am I?"
        mc_t "Why am I watching myself like this?"

        show ep04_isahell02 at ken_burns_bottom_to_top with normalfade
        mc_t "That woman..."
        mc_t "She's mesmerizing in this hellish glow..."

        $ setChannelVolume("sfx", 3, 0.4)
        $ playAudio(sfx_bed_creaking, "sfx", 3, False, 0, 0)

        show ep04_isahell03 at vpunch with normalfade
        mc_t "The way she moves in this crimson light..."
        mc_t "Like she's stepping in flames..."

        $ setChannelVolume("sfx", 3, 0.25)
        $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

        show ep04_isahell04 at ken_burns_bottom_to_top with normalfade
        mc_t "Those curves..."
        mc_t "Every detail so clear, so tempting..."

        $ setChannelVolume("sfx", 4, 0.5)
        $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)

        show ep04_isahell05 at vpunch, ken_burns_left_to_right with normalfade
        mc_t "Fuck... that perfect ass..."
        mc_t "I want to reach out and grab it..."

        show ep04_isahell06 at ken_burns_bottom_to_top with normalfade
        mc_t "Wait... no... Is that..."
        mc_s "Isabella?"

        show ep04_isahell07 with vpunch
        isa "Miss me, [daddy_r]?"
        mc_t "Why am I dreaming of her like this?"
        mc_s "Isabella, what are you doing?"
        isa "Feeling how hard your cock is for me..."
        isa "Throbbing against my wet cunt..."
        mc_s "Stop this..."

        show ep04_isahell08
        isa "Your cock says otherwise..."
        isa "Aching to split your [dau_r_low]'s pussy open..."
        mc_s "This is wrong..."
        isa "Wrong feels so fucking good..."
        mc_s "We can't..."
        isa "Let me show you what I really am..."
        mc_s "What?"

        scene eigengrau with normalfade
        $ setChannelVolume("sfx", 1, 0.5)
        $ playAudio(sfx_wings_evil, "sfx", 1, False, 0, 0)

        show ep04_isahell09 at subtle_zoom_out with slowfade
        isa "Like what you see, [daddy_r]?"
        mc_s "You're a..."
        isa "Your personal succubus..."
        isa "I know every filthy thought you've had about me..."
        isa "Forget I'm your [dau_r_low]... just fuck me like you've always wanted..."
        mc_s "Isabella..."

        show ep04_isahell10
        isa "Want to fuck [mommy_r]'s replacement?"
        isa "I can be your perfect little slut, [daddy_r]..."
        mc_s "This is too much..."
        isa "I'm everything dark inside you - your urge to corrupt innocence, your need to taint [fm_r_low], your desire to possess what was hers..."
        isa "And unlike her, I'll be your permanent sin..."
        isa "Want to hear me scream your name while you destroy my holes?"
        mc_s "Isabella, please..."

        scene eigengrau with normalfade
        $ setChannelVolume("sfx", 1, 0.5)
        $ playAudio(sfx_wings_evil, "sfx", 1, False, 0, 0)

        show ep04_isahell11 with slowfade
        isa "Stop thinking, start feeling..."
        isa "Feel how wet your baby girl is for you..."
        isa "I know you want to breed your own [dau_r_low]..."
        isa "Make me your personal fucktoy..."
        mc_s "Isabella..."

        show ep04_isahell12 with slowfade
        isa "Eat your [dau_r_low]'s cunt, [daddy_r]..."
        isa "Taste how wet you make me..."
        mc_s "We can't..."
        isa "Drink your baby girl's juices..."
        isa "I want your tongue deep in my holes..."
        mc_s "No, this is wrong."

        show ep04_isahell13 with slowfade
        isa "Look at your [dau_r_low]'s fuckholes, [daddy_r]..."
        isa "Ready for your thick cock..."
        isa "Don't you want to ruin [daddy_r]'s little girl?"
        isa "Split me open and fill me up..."
        mc_s "No, Isabella..."
        isa "Your cock says you want to breed your baby..."
        isa "Our dirty little secret..."
        mc_s "We can't do this..."

        show ep04_isahell14 at ken_burns_right_to_left with slowfade
        isa "I am your damnation!"
        isa "Your eternal torment!"
        isa "Hell is where you belong..."
        isa "And I'm taking you there..."
        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("music", 2.0)
    scene eigengrau with clouds_inverse
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 5, True, 1.5, 0)

    show ep04_isanight27 at vpunch with clouds_inverse
    mc_t "Fuck... was that...?"
    mc_t "A dream about Isabella...?"
    mc_t "Felt so real..."
    mc_t "What's wrong with me?"
    mc_t "These thoughts about my own [dau_r_low]..."
    mc_t "Just forget it... just sleep..."

    $ ep04_ach_isabella2 = True
    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall




label ep04_isabella_masturbation:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 5, 0.3, 1.0)

    show ep04_isanight16 at ken_burns_right_to_left with circlewipe
    isa_t "God... can't sleep at all with him right here. My heart's racing just feeling him next to me."
    isa_t "Why am I getting so hot? No, I know exactly why... always happens when he's close. My body's such a traitor sometimes."

    show ep04_isanight17
    isa_t "He looks so peaceful sleeping like that... still has that strength about him even now."
    isa_t "Ugh, it's not fair. He's not even trying and he looks this good. And here I am, staring like an idiot..."
    isa_t "Can't help it though. Something about him just... pulls me in. Always has."

    show ep04_isanight18
    isa_t "And then there's Nanami... God, she thinks she's so smooth with her little act. Please."
    isa_t "He's MY [da_r]. She has no idea what we've been through, what we mean to each other."
    isa_t "Maybe I should remind him who really matters here... show him what he's missing by hanging around her."
    isa_t "Just need to be smart about it... can't be too obvious. Need to keep playing it cute and sweet while I figure this out."

    show ep04_isanight19
    isa_t "Damn... this feeling's getting stronger. No point lying to myself about what I want."
    isa_t "My body knows exactly what it needs..."

    show ep04_isanight20 at ken_burns_bottom_to_top
    isa_t "Is this what they call being horny? God, that sounds so dumb but... yeah, that's definitely what this is."
    isa_t "Should probably feel worse about wanting my own [da_r_low] like this. But honestly? No one else gets me like he does."
    isa_t "Can think about how messed up this is all I want, but it's not going away..."

    show ep04_isanight21
    isa_t "What if I just... touched him? Just a little? No, no, bad idea. Really bad idea."
    isa_t "He could wake up any second. Everything I've worked for would go poof."
    isa_t "Gotta keep it together. That's how I always win..."

    show ep04_isanight22 with normalfade
    isa_t "But seriously, why him? Maybe because he's the only one who might actually understand the real me..."
    isa_t "Yeah, yeah, [daddy_r_low] issues or whatever. But it's more than that. Way more."
    isa_t "There's gotta be a way to make this work... just need to think it through."

    show ep04_isanight23
    isa_t "Shit... can't believe I just did that. Me, always so careful, and I just... lost it."
    isa_t "I'm a terrible [dau_r_low], doing something so shameful like this. How can i face him tomorrow?"
    isa_t "His smell, how warm he is... drives me crazy. Makes me forget all my plans and just want..."
    isa_t "No point pretending I didn't know what I was doing. I knew. I wanted to."

    show ep04_isanight26
    isa_t "If he wakes up... God, that could either be really good or really, really bad."
    isa_t "He wouldn't hate me though... he'd probably be more freaked out about how much he liked it."

    show ep04_isamast01
    isa_t "Like Nanami could ever compete with me. She's so basic she probably thinks missionary is kinky."
    isa_t "Okay, breathe Isabella. You're still in control. Even if your body's screaming otherwise..."
    isa_t "But damn... this feeling isn't going anywhere. My brain says stop but everything else..."

    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(isabella_sexy, "music", 1, True, 2.0, 1.0)

    show ep04_isamast02
    isa_t "This isn't just being horny anymore. I want him. All of him. Want him to be mine completely."
    isa_t "Other guys? Please. They see what I want them to see. The cute, sweet girl. So boring."
    isa_t "[da_r] though... he could handle the real me. If I ever showed him..."

    show ep04_isamast03
    isa_t "But how do I make him see me as more than his little girl without ruining everything?"
    isa_t "For now just... keep playing my part. Figure the rest out later."

    show ep04_isamast04
    isa_t "Screw it... I need to... just a quick touch. Just to take the edge off..."
    isa_t "Just this once... to clear my head..."

    show ep04_isamast05
    isa_t "This is such a risk but... god, it feels too good to stop."
    isa_t "My whole body's on fire... need more..."

    $ setChannelVolume("sfx", 1, 0.4)
    $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)

    show ep04_isamast06 with hpunch
    isa_t "Getting harder to think straight... but who cares anymore?"
    isa "Hmmm..."
    isa_t "Being [daddy_r_low]'s bad girl... oh, that makes it even hotter."
    isa "Ohh..."
    isa_t "The fact that we shouldn't makes me want it more..."

    show ep04_isamast07
    isa_t "Touching myself right next to him... god, I'm really doing this. Such a bad idea but..."
    isa_t "Look at him sleeping... no clue what his little girl is doing right here."
    isa_t "He has no idea what he does to me. Just being near him makes me lose my shit completely."

    $ setChannelVolume("sfx", 2, 0.4)
    $ playAudio(sfx_femheavybreath, "sfx", 2, False, 0, 0)

    show ep04_isamast08
    isa_t "Wonder what he's dreaming about... is he thinking of me too?"
    isa "Mmmmmm...."
    isa_t "Mmmm... every touch feels better than the last. Getting so wet..."

    show ep04_isamast09
    isa_t "What if he wakes up right now? Sees his perfect [dau_r_low] being such a slut..."
    isa_t "Shit, even thinking about him catching me... makes me wetter..."
    isa "Hmmmmph..."
    $ stopAudio("sfx", 2, 1)
    $ setChannelVolume("sfx", 3, 0.8)
    $ playAudio(sfx_moan_breath, "sfx", 3, False, 0, 0)

    show ep04_isamast10
    isa_t "Being such a naughty girl for [daddy_r_low]... god, that sounds so dirty. I love it."
    isa_t "Need more... this isn't enough anymore..."

    $ setChannelVolume("sfx", 4, 0.8)
    $ playAudio(sfx_mast_fem, "sfx", 4, False, 0, 0)

    show ep04_isamasturbation01 with normalfade
    isa_t "Can't control myself anymore... don't even want to... feels too good..."

    show ep04_isamasturbation02
    isa_t "Yes... fuck being the good girl right now... just want to feel good..."

    show ep04_isamasturbation03
    isa_t "Been holding back so long... can't anymore... don't want to..."

    show ep04_isamasturbation04
    isa_t "[daddy_r]... wish you'd wake up and see me... see how much I need you..."

    show ep04_isamasturbation05
    isa_t "If you won't touch me... guess I'll have to do it myself..."

    $ setChannelVolume("sfx", 1, 0.25)
    $ playAudio(sfx_madbreathxxx, "sfx", 1, False, 0, 0)

    show ep04_isamastur201 with normalfade
    isa_t "What would you think, seeing your little girl like this? All hot and bothered for you..."

    show ep04_isamastur202
    isa_t "Your sweet innocent [dau_r_low]... being such a dirty girl..."

    show ep04_isamastur203
    isa_t "No more pretending... at least not right now..."

    show ep04_isamastur204
    isa "Ahh..."
    isa_t "Getting close... can't hold back anymore..."

    show ep04_isamastur205
    isa_t "Need you so bad... want you to make me yours..."

    show ep04_isamastur206
    isa_t "You'd know what to do with me... how to make me feel so good..."

    show ep04_isamastur207
    isa "Ahhhhh..."
    isa_t "Almost there... can't stop now..."

    show ep04_isamastur208
    isa_t "Yes... fuck yes... so close..."

    show ep04_isamastur209
    isa_t "Imagining your hands on me... inside me..."

    show ep04_isamastur210
    isa_t "Can't play innocent anymore... too far gone..."

    show ep04_isamastur211
    isa_t "Gonna cum... gonna cum thinking of you [daddy_r_low]..."

    show ep04_isamastur212
    isa_t "Oh fuck... yes... claiming what should be mine..."

    show ep04_isamast11 with normalfade
    isa_t "Yes... [daddy_r]... I'm yours!"

    $ setChannelVolume("sfx", 1, 0.4)
    $ playAudio(sfx_madmoan2xxx, "sfx", 1, False, 0, 0)

    show white zorder 1.0 at ejaculation_flash
    show ep04_isamast12 at impact_shake with flash
    isa "AHHHHHHH!!!"
    $ stopAllSubchannels("music", 2.0)

    show ep04_isamast13
    isa_t "Holy shit... that was... intense."
    isa_t "Worth the risk... so worth it..."

    show ep04_isamast14
    isa_t "Back to being [daddy_r]'s good girl tomorrow... but tonight..."
    isa_t "Tonight I got to be who I really am..."

    show ep04_isamast15
    isa_t "Still sleeping... didn't hear a thing. My dirty little secret."
    isa_t "Wonder how long I can keep playing innocent after this..."
    isa_t "What if he knows? What if he sees right through me?"
    isa_t "Maybe part of me wants him to..."

    show ep04_isamast16
    isa_t "Need to calm down... get my head straight again."
    isa_t "Get some space..."

    show ep04_isamast17 at ken_burns_left_to_right
    isa_t "Just need to think this through... plan it right. This isn't over, Nanami..."

    $ stopAllSubchannels("amb", 2.0)
    jump ep04_pazcall




label ep04_pazcall:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.15)
    $ playAudio(sfx_morning, "amb", 1, True, 1.5, 0)
    $ setChannelVolume("music", 1, 0, 1.0)
    $ playAudio(mc_theme, "music", 1, True, 2.0, 1.0)

    show ep04_pazwake01 at subtle_zoom_out with circlewipe
    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    pa_s "Mhh... my head..."

    $ setChannelVolume("amb", 1, 0.05, 1.0)

    show ep04_pazwake02 with normalfade
    pa_t "What... what happened? God, everything hurts..."
    pa_t "Haven't had a headache this bad since that night [mc_name] and I went drinking after graduation."

    show ep04_pazwake03
    pa_t "Where...? Oh right, [mc_name]'s place. Shouldn't have dozed off here..."
    pa_t "Morning already? Shit, I've been out for hours. [mc_name]'s gonna be worried sick."

    show ep04_pazwake04
    pa_t "That girl! She actually knocked me out!"
    pa_t "Who was she? The way she moved... I've never seen anything like it at the dojo."
    pa_t "Something's not right here. This isn't some random attack."

    show ep04_pazwake05 at ken_burns_corner_to_corner4
    pa_t "My gun... dammit, she took my gun! The captain's going to kill me."
    pa_t "Some cop I am. [mc_name] trusts me to help and I get knocked out in his own apartment."
    pa_t "These things she left... they're meant for him. But why? What's he got himself mixed up in now?"

    $ stopAllSubchannels("amb", 2.0)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_japanday_cross, "amb", 2, True, 1.5, 0)

    show ep04_mcmorn01 with lines
    show outside_home_for_work zorder 2 with dissolve
    pause 4
    hide outside_home_for_work with dissolve
    $ setChannelVolume("music", 1, 0.3, 2)

    mc_t "God, finally some fresh air. Being stuck at home was suffocating. [fm_r]'s great and all, but 24 hours straight? Pure torture."
    mc_t "Everything's such a mess right now. Paz, Nanami, Isabella... Amber... [mo_r]. And Madison - that kid's gonna drive me crazy. Can't catch a break lately."

    show ep04_mcmorn02
    mc_t "Need to get my shit together and figure this out. Head's pounding like crazy though."
    mc_t "And Paz... radio silence. Not a single call or text. That's not like her at all."
    mc_t "What if she ran into the same trouble as Arlette? Damn... what if something happened because I asked her to check the apartment?"
    mc_t "If anything's happened to her... that's on me. Should've known better than to drag her into this mess."
    mc_t "Huh? A text?"

    show ep04_mcmorn03
    mc_t "Let's see..."
    nvl clear
    jump ep04_paz_sms_5


    #SMS




label ep04_pazcall_post:
    show ep04_mcmorn03 at focus_shift
    mc_t ". . ."

    show ep04_mcmorn04 with slowfade
    mc_t "Blonde girl... like Antonella? No way... but she did have our picture. Too weird to be coincidence..."
    mc_t "At least I've got something to focus on now. Better than drowning in [fm_r_low] drama and life choices."
    mc_t "Maybe I can actually figure this out. Do something right for once."
    mc_t "And make sure Paz stays safe - she's always had my back, time to return the favor."

    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep04_antonella_return




label ep04_antonella_return:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.3)
    $ playAudio(sfx_morning_late, "amb", 3, True, 1.5, 0)

    show ep04_antoshow01 at dramatic_focus_out
    $ setChannelVolume("music", 1, 0.3, 1.0)
    $ playAudio(antonella_theme, "music", 1, True, 2.0, 1.0)

    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "Good morning!"
    ed "In Osaka, it's 9:00 AM. The temperature is 23 degrees Celsius with scattered clouds."
    ed "Today's forecast shows a high of 25 degrees Celsius and a low of 21 degrees Celsius."
    ## save notification
    if htl_episodes == 4.2:
        $ show_custom_notification("save_tip")
    $ setChannelVolume("amb", 3, 0.1, 1.0)

    show ep04_antoshow02 at ken_burns_right_to_left
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "Here are your morning news headlines."
    ed "The Prime Minister has announced new measures to combat political corruption, while the government faces mounting criticism for its handling of the yakuza crisis."
    ed "The Japanese stock market is experiencing a sharp decline. Analysts predict continued volatility in coming weeks."
    show ep04_antoshow03 at subtle_zoom_out
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "Updates on the yakuza situation."
    ed "The government's crackdown on organized crime has led to increased violence between rival factions."
    ed "Local authorities advise avoiding areas known for criminal activity."
    show ep04_antoshow04 at ken_burns_corner_to_corner4
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "The weather is perfect for outdoor activities in Osaka today."
    $ setChannelVolume("sfx", 2, 0.3)
    $ playAudio(sfx_phonering, "sfx", 2, True, 0, 0)
    ed "Check your Alexa app for local events and activities."
    ed "That's your morning update. I'll notify you of important news throughout the day."
    $ stopAudio("sfx", 2, 1)

    show ep04_antoshow05 with normalfade
    anto "Yes?"
    $ rm.set_knows("antonella", True)
    hir "Has your body recovered from the last assignment?"
    anto "Fully operational, sir."
    hir "Excellent. Next target: Tokyo. Your old hunting ground, isn't it?"
    anto "Indeed, sir."
    show ep04_antoshow06 with normalfade
    hir "I'm accompanying you this time. Private jet departs in 5 hours. Meet at Kansai International in 3."
    hir "Understood?"
    anto "Affirmative. Kansai International, 3 hours."
    show ep04_antoshow07
    hir "One detail... Hideo's circle still believes our narrative about the police?"
    anto "They've accepted it completely. The seeds we planted grew exactly as planned."
    hir "Excellent work. Keep this precision. Airport soon."
    anto "Acknowledged."
    show ep04_antoshow08 at subtle_zoom_in with slowfade
    anto_t "Poor little one... still searching for a name, for a place to belong..."
    anto "Alexa, what's the weather in Tokyo?"
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "The current weather in Tokyo is 22 degrees Celsius and partly cloudy.The humidity is 65 percent with east winds at 10 kilometers per hour."
    ed "Would you like to hear an extended forecast?"
    anto "No."
    anto_t "Look how you tremble at the thought of them. Such a fragile thing you are..."

    scene eigengrau with slowfade
    show ep04_antoshow09 at subtle_zoom_out
    anto_t "Sleep now, little one. The nameless don't need to feel."
    anto "Alexa, turn off notifications."
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "I've turned off notifications. You won't receive alerts until you turn them back on."
    show ep04_antoshow10 with normalfade
    anto "Alexa, goodbye."
    $ stopAudio("sfx", 1, 0)
    $ setChannelVolume("sfx", 1, 0.3)
    $ playAudio(sfx_echodot, "sfx", 1, False, 0, 0)
    ed "Goodbye!"
    anto "Thanks... friend."
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    $ setChannelVolume(channel="amb", subchannel=6, volume=0.1)
    $ playAudio(sfx_airportwalla, "amb", 6, True, 1.5, 0)
    $ setChannelVolume(channel="amb", subchannel=7, volume=0.3)
    $ playAudio(sfx_earlypast, "amb", 7, True, 1.5, 0)

    show ep04_antoshow11 with circlewipe
    anto "Yoshida-sama."
    hir "Punctual as always."
    show ep04_antoshow12 at ken_burns_right_to_left
    hir "You understand seeing him is still not possible, even in Tokyo."
    anto "Understood."
    hir "Good. Any association would be too risky at this stage. The timing isn't right."
    hir "Your meeting will have to wait. Is that clear?"
    $ rm.set_knows("antonella", True)

    show ep04_antoshow13 with normalfade
    anto "Crystal clear."
    hir "Board the plane. We'll discuss details in the air."
    anto "Yes, sir."
    #-- End Episode 4
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
    pause 2.0
    if htl_episodes == 4.2:
        return


    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep05_title


