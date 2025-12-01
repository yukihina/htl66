



label ep05_start:
    $ persistent.current_episode = 5
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ renpy.block_rollback()
    $ renpy.save_persistent()
    jump ep05_intro


## -- INTRO COFFEE




label ep05_intro:
    $ config.rollback_enabled = True
    scene eigengrau
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)

    show ep05_coffee01 at ken_burns_right_to_left with slowfade
    show screen stats_button
    show screen walkthrough_icon

    mc_t "Another morning in this madhouse..."
    mc_t "At least the kitchen's empty. Small mercies."
    mc_t "Where did [mo_r] hide the coffee this time?"

    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_kitchen_rumm, "sfx", 1, False, 1, 0)

    hide ep05_coffee01
    mc_t "Found it. Behind the wine bottles. Classic Elizabeth."

    $ stopAudio("sfx", 1, 0.5)
    $ setChannelVolume("sfx", 2, 0.7, 0)
    $ playAudio(sfx_coffee_mkr, "sfx", 2, False, 1, 0)

    show ep05_coffee02
    mc_t "Could've used something stronger than coffee after yesterday..."
    mc_t "The sun's pretty nice today though. Maybe I should..."

    $ stopAudio("sfx", 2, 1)

    show ep05_coffee03 at ken_burns_corner_to_corner3 with slowfade
    mc_t "Perfect. Coffee by the pool sounds good right now."
    mc_t "Might help clear my head after all."
    mc_t "What could possibly go wrong with a quiet morning coffee?"

    $ stopAllSubchannels("amb", 2.0)
    #######FIX STRIKES_BUG
    if ep03_amberstrike or ep03_amberangry:
        $ ss.add("amber", "strike")
    ########
    jump ep05_madyoga




label ep05_madyoga:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 1, 0.4, 0)
    $ setChannelVolume("amb", 2, 0.5, 0)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 1, 0)
    $ playAudio(sfx_wind_pool, "amb", 2, True, 1, 0)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(madison_nan_theme, "music", 1, True, 4, 0)

    show ep05_madintro01 at ken_burns_corner_to_corner4 with circlewipe
    mad "Okay, like this... smooth and gentle. Feel the stretch in your core."
    nana "Wow, you're amazing at this, Maddie! I wish I could move like that..."
    mad "It just takes practice, sweetie. Stay with me and you'll get there."
    mad "I'll make sure you learn everything you need."
    show ep05_madintro02 at ken_burns_left_to_right
    mad "The secret is in the details. Watch how I position myself."
    nana "Um... I-Is this actually yoga? It looks different from the videos..."
    mad "Trust your best friend, Nanami. I've been doing this way longer than those YouTube wannabes."
    mad "Besides, this is... a special kind of practice."
    show ep05_madintro03 at subtle_zoom_out
    mad "Now we stretch a little... wider."
    nana "M-Maddison! Are you sure?"
    mad "Relax. Nobody's watching but me."
    show ep05_madintro04 with vpunch
    mad "See how liberating this is?"
    nana "It looks... intense."
    mad "You'll see how good it feels soon enough."
    show ep05_madintro05 with normalfade
    mad "Want to give it a shot? I'll help you get into position."
    nana "I don't know... what if I fall over?"
    mad "I won't let that happen. I've got you."
    mad "Always."
    show ep05_madintro06 at dramatic_focus with normalfade
    nana "Eeeeh... Maddie... these clothes feel really tight..."
    mad "They're supposed to be. Shows off your beautiful curves perfectly."
    nana "But everyone can see everything!"
    mad "That's the whole point, silly."
    mad "Besides, it's just us here..."
    show ep05_madintro07 with hpunch
    mad "Here, let me help you get the position right..."
    nana "M-Maddie... this is so embarrassing... what if someone sees?"
    mad "Stop thinking so much. Just feel it."
    mad "Focus on my hands guiding you..."
    show ep05_madintro08
    mad "Let's see what you've got."
    nana "But I'm not ready..."
    mad "You never are, and that's why it's fun."
    show ep05_madintro09 with normalfade
    mad "Perfect form, Nanami. You're such a natural."
    nana "R-really? Thank you so much, Maddie!"
    mad "Of course. You know I only want what's best for you."
    mad "We're going to get even closer..."
    show ep05_madintro10 at ken_burns_left_to_right with normalfade
    mad "Just need to adjust a few things..."
    mad "Here... and here... feels good, right?"
    nana "Y-yes... I think so..."
    show ep05_madintro11 at camera_zoom with vpunch
    nana "Am I doing this correctly, Maddie?"
    mad "Mmm... almost there. Just a bit more..."
    mad "You're so responsive to my touch..."
    show ep05_madintro12 at ken_burns_corner_to_corner2
    mad "Your skin's gotten so soft lately..."
    nana "I've been using that special lotion you bought me! Every night, just like you said!"
    mad "Such a good girl... following all my instructions."
    mad "Now bring those legs closer together... trust me."
    nana "But the yoga book shows it differently..."
    mad "Forget the book. This way feels much better, doesn't it?"
    show ep05_madintro13 with hpunch
    nana "I-is this the right position, Maddie?"
    mad "You're such a perfect student... so eager to please..."
    mad "Let me reward you..."
    show ep05_madintro14 with normalfade
    mad "This next pose needs special attention..."
    nana "M-Madison! That's not... we shouldn't..."
    mad "Shh... just relax. Let me take care of everything."
    mad "You know I only want what's best for you..."
    show ep05_madintro15
    nana "You're acting strange today..."
    mad "Am I? Or are you just scared of getting closer to me?"
    nana "I... I don't understand what you mean..."
    mad "You will. Soon."
    mad "Now... copy my movements exactly, okay?"
    show ep05_madintro16
    nana "Like this? Am I doing okay?"
    mad "Perfect. Can you feel how connected we are?"
    mad "This is how it should always be..."
    show ep05_madintro17 at subtle_zoom_out
    mad "You're mine to protect... to guide... to cherish."
    nana "Maddie... you're being intense again..."
    mad "Let's take things further. You trust me, right?"
    mad "I'll show you things you've never imagined..."
    show ep05_madintro18 at dramatic_focus_out with slowfade
    if ep04_madstory and ep04_madnanastory:
        mc_t "Whatever they're doing... it's not my business. Better leave them alone."
        mc_t "Madison would just start another fight anyway..."
        mc_t "And I really need my morning coffee..."

        $ stopAllSubchannels("amb", 2.0)
        $ stopAllSubchannels("sfx", 2.0)
        $ stopAllSubchannels("music", 2.0)
        jump ep05_ambercof


    else:
        mc_t "Something's definitely wrong here. Madison's acting weird..."
        mc_t "I should check on Nanami. This doesn't look right."
        mc_s "Hey... what's going on out here?"
        pass
    show ep05_madintro19 with hpunch
    nana "[mc_name]! It's not what it looks like! Maddie's teaching me some morning stretches!"
    mad "We're in the middle of something. Get lost, pervert."
    mc_s "Teaching? That looked more like groping to me."
    mad "Nobody asked for your opinion."
    show ep05_madintro20
    nana "It's a special technique Maddie invented! Right, Maddie?"
    mad "Ignore him, Nanami. He's just jealous he can't join in."
    mad "Men always want to ruin everything..."
    show ep05_madintro21
    mad "Keep going sweetie, you're doing so well."
    nana "O-okay, Maddie! If you say so..."
    mad "That's my girl. So obedient..."
    show ep05_madintro22
    mad "Let me handle this asshole. Don't stop practicing."
    nana "Uhm... please don't fight..."
    mad "Just a quick chat between siblings. Right, [br_full_r_low]?"
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep05_madintro23 with circlewipe
    mad "Seriously, what's your problem now?"
    mad "Can't you see we're busy here? Go jerk off somewhere else."
    mc_s "Cut the act. That's not yoga and you know it."
    mad "Oh? And what exactly do you think it is?"
    mc_s "You're manipulating her. She trusts you and you're taking advantage."
    mad "Aww, is big [br_full_r_low] playing white knight now? How noble."
    show ep05_madintro24
    mad "Don't pretend you weren't enjoying the show, pervert."
    mc_s "I'm not a pervert. Just looking out for her."
    mad "Right. Because creeping on young girls is totally normal..."
    mc_s "What are you talking about?"

    show ep05_madintro25
    mad "Look at you... acting all righteous while undressing her with your eyes."
    mad "You're just like every other man - thinking with your dick."
    mc_s "What the hell are you talking about?"
    mad "Don't play dumb. It's pathetic."
    mad "I see everything in this house, remember? Every little interaction..."
    mc_s "I barely know her! We've only talked like twice!"
    if not ep04_madstory:
        show ep05_madintro26
        mad "Always excuses with you men, isn't it?"
        mad "You know who you remind me of right now?"
        mad "Dear old [daddy_r]. King of excuses himself."
        mc_s "Madison-"
        mad "Wonder what he's doing in his office right now? More 'late night surgeries'?"
        mc_s "I don't care what he does."

        show ep05_madintro27
        mad "Of course not. Because we don't care what anyone does in this [fm_r_low], do we?"
        mc_s "What does he have to do with you basically molesting Nanami?"
        mad "'Molesting'? Please. I'm helping her grow."
        mad "Teaching her confidence. Something you wouldn't understand."
        mc_s "That wasn't confidence - it was control."
        mad "And? What's wrong with that? Let me tell you a story, dear [br_full_r_low]."
        mad "About a little redhead who learned life's hardest lesson..."
        mc_s "Madison, I just want my coffee."
        mad "You'll listen whether you like it or not."
        show ep05_madintro28
        mad "Once upon a time, there was a girl who lived in a big house."
        mad "She thought it was her castle, but it was more like a cage."
        mad "She watched her [mo_r] get slapped around every night. When she tried to help? Guess what happened?"
        mad "She got slapped, too."
        mc_s "Madison, stop—"
        mad "No interrupting! Stories have rules."
        mad "[mo_r] called her a nuisance. Told her to go away."
        mc_s "Why are you telling me this?"

        show ep05_madintro29
        mad "Because you need to understand why things are this way."
        mad "That good little girl? She died that night. Learned something important."
        mad "Being good gets you hurt. Being bad? That's how you survive."
        mc_s "I had no idea..."

    scene eigengrau
    $ setChannelVolume("music", 2, 0.4, 0)
    $ playAudio(madison_theme, "music", 2, True, 4, 0)

    show ep05_madintro30 with slowfade
    mad "You like her, don't you? Our precious little Nanami..."
    mad "Don't worry. I like her too. Different kind of like though."
    mc_s "It's not like that at all..."
    mad "Just look at her... so pure, so innocent."
    mad "What do you see when you look at her? Nice tits? Cute face? Bet you've thought about it..."
    mc_s "I don't-"

    show ep05_madintro31
    mad "Shut up. We both know that's exactly what you see."
    mad "Want to know what I see? Everything. The girl crying in bathroom stalls."
    mad "The one apologizing for breathing. My precious little Nanami..."
    mad "She's grown so much with me, but inside? Still that scared bunny. She needs me."
    show ep05_madintro32
    mad "Want to hear how we met? It's quite the story."
    mc_s "Do I have a choice in this?"
    mad "Found her locked in the school bathroom. Crying her eyes out."
    mad "Called her pathetic, slapped her, told her to grow up. She looked at me like I'd kicked a puppy. It was adorable."
    mc_s "That's... horrible."

    show ep05_madintro33
    mad "Next day? Her bullies vanished. One got expelled. Others... learned their lesson."
    mc_s "What did you do to them?"
    mad "Protected what's mine. She's been following me ever since."
    mad "Like a lost puppy finding its owner..."
    show ep05_madintro34
    mad "You're not ruining this. She needs me. She belongs to me."
    mad "Get it through your thick skull, [br_full_r_low]."
    mc_s "She's not your property!"
    mad "Oh please. Like you know anything about her."
    show ep05_madintro35
    mad "Look at you playing hero. It's honestly pathetic."
    mad "You don't know the first thing about her. Just projecting your sick fantasies."
    mc_s "That's bullshit! You're the one who's sick!"
    mad "Am I? You think she needs you? That she sees you the way you see her?"
    mad "I'm her everything. Her protector. Her confidante. Her salvation."
    show ep05_madintro36
    mad "Do you even know what it feels like to be with a woman?"
    mc_s "Are we really having this conversation?"

    show ep05_madintro37
    mad "Look at her... all you see is eye candy. But I see her soul."
    mc_s "You're sick for even suggesting that."
    mad "No, [br_full_r_low]. You're the sick one. This is real love. Pure love."
    mad "Not your twisted male fantasy version of it."
    show ep05_madintro38
    mad "This is why women are superior. We see the whole picture."
    mad "Your dick only sees half the story. We see love in its purest form."
    mad "That's what makes us more human than you'll ever be."
    show ep05_madintro39
    mc_s "Jesus Christ... I just wanted some breakfast."
    mc_s "I'm out of here."
    mad "Running away? Typical man."
    show ep05_madintro40
    mad "That's right. Leave. Men never want to face reality."
    mad "This is exactly why Nanami needs someone like me."
    mad "Someone who'll stay. Who'll protect her."
    show ep05_madintro41
    if ep04_mcdrunk:
        mad "Oh, by the way - remember getting her drunk that night?"
    else:
        mad "Oh, by the way - remember keeping her up late that night?"
    mad "She told me everything. 'Maddie, your [br_full_r_low] touched me...'"
    mad "Nobody touches what's mine. Remember that."
    mc_s "Go fuck yourself!"

    show ep05_madintro42
    mad "Oh look! Perfect timing - Nanami's shower time!"
    mad "Nanami! Ready for your morning routine?"
    mad "Don't forget to use that special soap I got you..."
    show ep05_madintro43
    nana "Thanks for the amazing lesson, Maddie! It was really fun!"
    mad "Anything for you, sweetie."
    nana "I'm gonna go shower now, okay?"
    mad "Go ahead."
    show ep05_madintro44 at ken_burns_left_to_right with slowfade
    mad "Now then, dear [br_full_r_low]..."
    mad "Let's discuss keeping secrets, shall we?"
    mad "[fm_r] secrets are the best kind..."
    if ep04_madnight == 0:
        show ep05_madintro45 with slowfade
        mc_s "What are you-"
        mad "Shh... just taking a little insurance policy."
        mad "Say cheese, big [br_full_r_low]..."
        show ep05_madintro46 at photo_effect with flash
        show photo_flash with dissolve
        mad "Behave, or everyone sees this lovely topless pic of me with their favorite pervert."
        mad "Wonder what Nanami or Isabella would think?"
        mc_s "Delete that right now!"

        show ep05_madintro47
        mad "Not happening. Be a good boy and maybe I won't share them."
        mad "Your reputation is in my hands now..."
    show ep05_madintro48
    if ep04_madnight == 0:
        mad "Perfect blackmail material..."
    else:
        mad "Now that Nanami is gone, don't forget you owe me a favor. Remember the photo, right? We'll talk later."
    mad "Have fun dying alone, [br_full_r_low] dear."
    mad "Now if you'll excuse me, Nanami needs help washing her back..."
    $ stopAllSubchannels("amb", 2.0)
    $ stopAllSubchannels("sfx", 2.0)
    $ stopAllSubchannels("music", 2.0)
    jump ep05_ambercof




label ep05_ambercof:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 1, 0.6, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)

    show ep05_amberintro01 at dramatic_focus with circlewipe
    $ setChannelVolume("sfx", 8, 0.4, 0)
    $ playAudio(sfx_yawnfem, "sfx", 8, False, 1, 0)
    amb "Coffee time."
    mc_t "Always right after her streams..."

    $ setChannelVolume("sfx", 1, 0.4, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 1, False, 1, 0)

    show ep05_amberintro02 at zoom_out
    mc_s "Stream's done?"
    amb "Just finished. Gonna chill now."
    mc_t "She seems less aggressive than usual..."

    $ stopAudio("sfx", 1, 1)
    if ss.get("amber", "strike") > 0:
        show ep05_amberintro03
        mc_t "Maybe I should say something about last time..."
        mc_t "She looks tired... might be a good moment."

        $ show_walkthrough("ep05_ambcofmenu")
        menu:
            mc_t "Maybe I should try to make things right..."
            "Apologize to her":
                hide screen walkthrough_screen
                show ep05_amberintro04
                mc_s "About last time..."
                amb "Save it. I don't do apologies."
                mc_t "Classic Amber..."

                show ep05_amberintro05
                mc_s "I was wrong."
                amb "Yeah, you were. Don't do it again."
                amb "... but thanks for saying it."
                $ rm.update("amber", "trust", 5)
                $ check_levels("amber", "trust", 5)
                $ ss.set("amber", "strike", ss.get("amber", "strike") - 1)
                pass
            "Don't apologize to her":
                hide screen walkthrough_screen
                show ep05_amberintro06
                mc_s "Amber..."
                amb "You're blocking the coffee maker."
                mc_t "Guess she's still mad..."

                $ rm.update("amber", "trust", -5)
                $ check_levels("amber", "trust", -5)
                $ setChannelVolume("sfx", 2, 0.7, 0)
                $ playAudio(sfx_coffee_mkr, "sfx", 2, False, 1, 0)

                show ep05_amberintro07
                mc_t "The tension is unbearable..."
                isa "[da_r]? Can you come to my room? I need to talk to you..."
                mc_t "Saved by Isabella..."

                $ ep05_ambignore = True
                $ stopAllSubchannels("sfx", 2.0)
                $ stopAllSubchannels("amb", 2.0)
                jump ep05_isacos


    show ep05_amberintro08
    amb "You look tense. Madison giving you trouble?"
    mc_s "No more than usual. Just... dealing with things."
    amb "She's such a little bitch sometimes..."
    $ setChannelVolume("sfx", 2, 0.7, 0)
    $ playAudio(sfx_coffee_mkr, "sfx", 2, False, 1, 0)

    show ep05_amberintro09
    amb "Hmm."
    amb "Want to talk about it?"
    mc_s "I'm just realizing how little control we really have. Even when we try to do what's right."

    show ep05_amberintro10
    amb "That's deep for a morning chat."
    mc_s "Yeah. Just thinking aloud."
    amb "You always overthink everything..."
    $ stopAudio("sfx", 2, 2)

    show ep05_amberintro11
    amb "Well, don't think too hard. Life's easier that way."
    mc_s "I'll keep that in mind."
    amb "Let me help you forget all that crap..."
    $ setChannelVolume("sfx", 3, 0.7, 0)
    $ playAudio(sfx_glass_ontable, "sfx", 3, False, 0, 0)

    show ep05_amberintro12
    amb "Want me to help you relax?"
    amb "I've got just the thing."
    mc_s "What do you mean?"

    $ stopAudio("sfx", 3, 2)
    $ setChannelVolume("music", 1, 0.2, 0)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 4, 0)

    show ep05_amberintro13
    amb "Let's just say, it'll take your mind off things."
    mc_s "Here? Someone could-"
    amb "That's what makes it fun."
    mc_s "Amber..."

    show ep05_amberintro14 with hpunch
    amb "Scared someone will see us?"
    amb "Or that you won't be able to stop yourself?"
    mc_s "We shouldn't be doing this... at least not here or even at this time..."

    show ep05_amberintro15
    amb "No? Then why are you watching me so closely?"
    mc_t "She's got a point..."

    show ep05_amberintro16
    amb "Nervous?"
    amb "Or excited?"
    mc_s "Someone could come in any second..."

    show ep05_amberintro17 with vpunch
    amb "Mmm..."
    amb "Like Madison? Or sweet little Isabella?"
    amb "You know... The risk is half the fun."
    show ep05_amberintro24
    amb "Where do you want it?"
    amb "Upstairs? My room?"
    mc_s "Amber... we can't..."

    $ show_walkthrough("ep05_ambsexmenu")
    menu:
        mc_t "This is crazy... but..."
        "Accept her advances":
            hide screen walkthrough_screen

            mc_s "Alright."
            amb "That's what I like to hear..."
            mc_s "You're going to get us in trouble..."

            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)
            pass
        "Reject her":
            hide screen walkthrough_screen
            show ep05_amberintro18
            mc_t "We really shouldn't..."
            mc_s "We can't keep doing this, Amber."
            amb "Fine. Be boring."
            $ rm.update("amber", "cor", -3)
            $ check_levels("amber", "cor", -3)
            $ stopAllSubchannels("music", 2.0)

            show ep05_amberintro07
            amb "Whatever. I just wanted coffee anyway."
            mc_t "She's really upset..."
            isa "[da_r]? Can you come to my room? I need to talk to you..."
            $ ep05_ambignore = True
            $ stopAllSubchannels("amb", 2.0)
            $ stopAllSubchannels("sfx", 2.0)
            $ stopAllSubchannels("music", 2.0)
            jump ep05_isacos


    show ep05_amberintro19 with hpunch
    amb "Shhh... wouldn't want anyone hearing..."
    mc_s "We shouldn't-"
    amb "Stop thinking so much..."
    show ep05_amberintro20 at ken_burns_top_to_bottom
    amb "Shut up and watch me."
    mc_t "She's so demanding..."
    amb "I know you want to..."
    show ep05_amberintro21
    amb "Does this catch your eye?"
    mc_s "Amber..."
    amb "Just say yes..."
    show ep05_amberintro22 with hpunch
    amb "I can feel how much you want this..."
    mc_s "We shouldn't..."
    amb "But we will..."
    scene eigengrau with slowfade
    show ep05_amberintro24 with circlewipe
    amb "Shouldn't what? This?"
    mc_s "Someone could walk in..."
    amb "Scared? Or turned on?"
    show ep05_amberintro23
    amb "Then we better make it quick..."
    amb "Come here..."
    show ep05_amberintro25 with vpunch
    mc_s "Fuck... you're so wet..."
    amb "All for you, big [br_full_r_low]..."
    mc_t "The way she says that..."

    show ep05_amberintro26 at dramatic_focus
    amb "Now, do it! Quick!"
    mc_s "You want me to...?"
    amb "Fuck me!"
    show ep05_amberintro27 with normalfade
    amb "Stop teasing and put it in already..."
    mc_s "So impatient..."
    amb "Please... I need it..."
    show ep05_amberintro28 with hpunch
    amb "Just the tip? Really?"
    mc_s "You like it slow... right?"
    amb "Fuck slow, I want all of it!"
    show ep05_amberintro29 with hpunch
    amb "Stop being gentle..."
    mc_s "Make me..."
    amb "You asked for it..."
    scene eigengrau
    show ep05_amber_anim at dramatic_focus_out
    amb "Tell me how good it feels..."
    mc_s "So fucking good..."
    amb "Harder... fuck me harder!"
    mc_s "You're insatiable..."
    amb "Only for you... god, only for you..."
    mc_s "Amber... fuck..."
    amb "Don't stop... please don't stop..."
    scene eigengrau
    show ep05_amber_anim2 at dramatic_focus, vpunch_effect(time=0.3, offset=10, pause=0.4), concentrate
    amb "Right there... yes!"
    mc_s "You feel amazing..."
    amb "Keep going... just like that..."
    mc_s "You're so tight..."
    amb "All yours... I'm all yours..."
    scene eigengrau with slowfade
    show ep05_amberintro30 at dramatic_realization with vpunch
    amb "Keep fucking me..."
    mc_t "She's getting close..."
    amb "Don't you dare slow down..."
    show ep05_amberintro31 at subtle_zoom_out with vpunch
    amb "I'm close..."
    mc_s "Me too..."
    amb "Together... let's cum together..."
    scene eigengrau
    show ep05_amber_anim4 at dramatic_focus, vpunch_effect(time=0.3, offset=10, pause=0.3), concentrate
    amb "Yes! Just like that!"
    mc_s "Amber... I can't hold it..."
    amb "Don't hold back... give it to me..."
    mc_s "You're squeezing me so tight..."
    amb "I'm gonna cum... gonna cum..."
    scene eigengrau
    show ep05_amber_anim3 at slow_reveal, camera_zoom, ken_burns_left_to_right
    amb "Fuck yes! Don't stop!"
    mc_s "So close..."
    amb "Me too... me too..."
    scene eigengrau with slowfade
    show ep05_amberintro32 with vpunch
    amb "Wait! Wait! Wait!"
    mc_s "What!!"
    amb "You know what would be fun? Giving my coffee a special... creamer."
    mc_s "That's..."

    show ep05_amberintro33 at subtle_zoom_in
    amb "Perverted? That's the point."
    mc_s "But..."
    amb "Shut up and do it..."
    scene eigengrau with slowfade
    show ep05_amberintro34 with vpunch
    amb "Come for me, big [br_full_r_low]."
    amb "Do it."
    mc_s "You're crazy..."

    show ep05_amberintro35
    mc_s "Oh god..."
    amb "Come on, give my coffee what it needs..."
    mc_t "This girl is unbelievable..."

    show ep05_amberintro36
    mc_s "You're fucking insane, you know that?"
    amb "You love it though..."
    mc_s "God help me, I do..."

    show ep05_amberintro37 at ken_burns_left_to_right
    mc_s "Fuck, fuck, fuck!"
    amb "Yes... give it all to me..."
    mc_t "Can't hold back anymore..."

    show white zorder 1.0 at ejaculation_flash
    show ep05_amberintro38 at vpunch with flash
    amb "That's it..."
    mc_s "Holy shit..."
    amb "Perfect..."
    show ep05_amberintro39 at dramatic_focus_out
    amb "Now that's a proper drink."
    mc_t "She's really going to..."

    show ep05_amberintro40
    amb "Cheers..."
    amb "The perfect blend..."
    mc_s "You're something else..."

    show ep05_amberintro41
    amb "Mmm... much better than the store-bought stuff."
    mc_s "You're insane."
    amb "You mean creative..."
    show ep05_amberintro42
    amb "You love it. So, feeling better now?"
    mc_s "Yeah... yeah, actually."
    amb "Told you I'd help..."
    show ep05_amberintro43
    amb "Alright! Now just let me fix my clothes..."
    mc_s "That was intense..."
    amb "What, getting shy now after all that?"
    show ep05_amberintro44
    amb "Yummy!"
    amb "Best coffee I've had all week..."
    mc_t "The way she licks her lips..."

    show ep05_amberintro45
    mc_s "We really need to be careful..."
    amb "What's life without a little risk?"
    if ep04_ambnight_cum == 1:
        amb "Finally got to swallow instead of wearing it..."
        mc_s "Jesus, Amber..."
    else:
        amb "By the way, for future reference, I can swallow but never ever do it on my face. It's just a pain to clean up."
    mc_s "Good to know."
    amb "Let's clean this jizz before I go."
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep05_amberintro46
    amb "Well, that's my morning pick-me-up done. Better than caffeine, right?"
    mc_s "Yeah... thanks, Amber."
    amb "Anytime, big [br_full_r_low]..."
    show ep05_amberintro47
    amb "Oh, by the way - Elizabeth's been popping pills again. More than usual."
    mc_s "How do you know?"
    amb "She's not exactly subtle..."
    show ep05_amberintro48
    amb "Hard to miss the rattling when she walks by. Plus Isabella's been hovering around her door like a concerned little nurse."
    mc_s "Isabella?"
    amb "Your [dau_r_low] notices more than you think..."
    show ep05_amberintro49
    amb "Yeah, she's got quite the observation skills."
    mc_t "Just like her [mo_full_r_low]..."
    amb "Better keep an eye on both of them..."
    $ stopAllSubchannels("amb", 2.0)
    jump ep05_isacos




label ep05_isacos:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 1, 0.4, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)
    if ep05_ambignore:
        show ep05_isaintro01
        isa "Let's go in, [da_r]. I need to show you something important."
        mc_t "She never asks me to her room..."
        isa "Please hurry, it's about [gra_r]..."
    else:
        $ setChannelVolume("sfx", 1, 1, 0)
        $ playAudio(sfx_door_knock, "sfx", 1, False, 0, 0)

        show ep05_isaintro02
        mc_s "Isabella, it's me... [mc_name]"
        isa "Come in, [da_r]. I've been wanting to talk to you."
        mc_t "She sounds worried..."

    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)

    show ep05_isaintro03 at ken_burns_right_to_left
    isa "Lock the door, [daddy_r]. What we need to discuss should stay private."
    mc_s "What's on your mind?"
    mc_t "She's never this secretive..."

    $ setChannelVolume("sfx", 3, 1, 0)
    $ playAudio(sfx_door_open2, "sfx", 3, False, 0, 0)

    show ep05_isaintro04
    isa "About [gra_r] Elizabeth. I've been watching her, studying her behavior..."
    mc_s "What about her?"
    isa "I've seen the bottles in her room, [da_r]. So many pills... different colors, different names."
    show ep05_isaintro05
    mc_s "Her pills? What do you mean?"
    isa "It's just... you weren't here, [da_r]. These past few years have been rough. [grf_short_r] keeps giving her all these pills, saying they'll help, but..."
    isa "Some days she's like a zombie, just sitting there. And when she skips them, she's either crying or throwing up in the bathroom."
    show ep05_isaintro06 at ken_burns_top_to_bottom
    mc_s "Uhm..."
    isa "I think she needs to see another doctor, [da_r]. Someone who actually wants to help her get better."
    isa "Because honestly? It feels like [grf_short_r]'s just playing around with her meds."
    isa "Every time she starts feeling better, he gives her more stuff until she's worse than before."
    mc_t "Michael... what are you doing to her?"

    show ep05_isaintro07 with normalfade
    mc_s "I'm gonna talk to her about this."
    isa "Thanks, [daddy_r]. Let's keep an eye on her, okay?"
    isa "I'm scared something bad might happen..."
    mc_s "Okay, Sweetheart. Changing the subject, can I ask what you are doing?"

    show ep05_isaintro08
    isa "What do you mean, [daddy_r]?"
    mc_s "Your clothes... is that lingerie?"

    show ep05_isaintro09 at ken_burns_bottom_to_top with vpunch
    isa "Oh... this? It's the base layer for Commander White's outfit."
    mc_s "Commander who?"
    mc_t "At least it's for cosplay..."

    show ep05_isaintro10 with normalfade
    isa "From NieR:Automata! You know, the beautiful commander with white hair?"
    mc_s "Still... isn't it a bit revealing for a base layer?"
    mc_t "Even if it's accurate, it's too much..."
    isa "But it has to be exact! Her outfit is all about the details..."
    show ep05_isaintro11
    mc_s "No, I don't like it... it's still inappropriate."
    mc_t "The Commander's outfit wasn't this revealing, was it?"

    show ep05_isaintro12 at ken_burns_bottom_to_top
    isa "But [daddy_r], her uniform needs this foundation! The structure is important."
    isa "See the regal-style lace? It's specifically designed for her look."
    mc_s "Well... It looks regal... I think so, but please tell me there's more to the costume."

    $ setChannelVolume("music", 1, 0.6, 0)
    $ playAudio(isabella_sexy, "music", 1, True, 4, 0)

    show ep05_isaintro13 with hpunch
    isa "Of course! We still need the coat, boots, and everything else!"
    isa "Commander White's uniform is really complex. All these pieces have to go on in the right order."
    mc_s "Oh thank god. For a moment there, Sweetheart, you had me worried."
    mc_s "Still... seeing you in something so mature, it just reminded me that you're growing up, and it's just... strange, that's all."

    show ep05_isaintro14
    isa "Shhh... Don't say that, [da_r]. You're making me blush..."
    isa "I'll always be your little girl. No matter what..."
    mc_t "Why does that sound different now..."

    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)

    show ep05_isaintro15
    isa "Hey... could you help me with something? I need help getting dressed properly."
    isa "The costume's not done yet... there are some parts I can't reach..."
    show ep05_isaintro16
    mc_s "What's missing, Sweetheart?"
    isa "Can't you tell? Look closer..."
    mc_s "Uhmm... nope?"

    show ep05_isaintro17
    isa "Well... Look carefully and tell me what's missing! The character always wears specific accessories..."
    mc_s "Uhmm..."

    $ show_walkthrough("ep05_isacheckmenu")
    menu:
        mc_t "She's waiting for an answer... what should I do?"
        "Let me check your outfit":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro18 with hpunch
            isa "Something's still not right though. Can you tell what it is, [da_r]?"
            mc_s "The... uhm... the bottom part looks incomplete..."
            mc_t "Focus on the costume, not my body..."

            show ep05_isaintro19 at ken_burns_top_to_bottom
            isa "Look carefully, [daddy_r]. The character wears something special over this..."
            isa "Feel how exposed the lace is? It needs something over it, right?"
            mc_t "Her body's looks so fragile..."

            show ep05_isaintro20
            isa "Think fashion, [da_r]. What covers but still shows skin?"
            mc_s "A jacket?"
            mc_t "Please let that be the right answer..."

            show ep05_isaintro21 with hpunch
            isa "Yes! And thigh-high boots too! Will you help me put them on?"
            mc_s "Sure, just tell me what to do."
            mc_t "At least we're getting somewhere safe..."

            $ rm.update("isabella", "trust", 2)
            $ check_levels("isabella", "trust", 2)
        "This isn't right...":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro22 with hpunch
            isa "Running away, [daddy_r]? When I need your help most..."
            isa "Can't you tell how excited I am to show you? My heart's racing..."
            mc_t "She's being too forward..."

            show ep05_isaintro23
            mc_s "Isabella, this isn't-"
            isa "Just help me with Commander White's jacket. That's all I want..."
            mc_s "I should go..."

            show ep05_isaintro24 at ken_burns_bottom_to_top
            isa "The uniform needs that military jacket, [daddy_r]... to complete the look."
            mc_s "That's not appropriate..."
            isa "Why not? I picked this costume specially for you..."
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)

            show ep05_isaintro25 at ken_burns_right_to_left
            isa "Please? You owe me at least this much. Remember how you never helped me dress up in the past?"
            mc_s "You know I can't say no when you look at me like that."
            mc_t "When did she learn to be so manipulative..."

            $ rm.update("isabella", "trust", 3)
            $ check_levels("isabella", "trust", 3)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Let me check you":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro26 with vpunch
            isa "D-[daddy_r_low]... what are you..."
            mc_s "The regal details on this lace are interesting..."
            mc_t "She wasn't expecting this..."

            show ep05_isaintro27
            isa "Wait... your hands..."
            mc_s "Commander White's uniform needs careful inspection..."
            isa "I... um... you're being different..."
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)

            show ep05_isaintro28 at ken_burns_corner_to_corner4 with vpunch
            isa "That's not... I mean... you're so close..."
            mc_s "The base layer is quite revealing..."
            isa "I didn't expect you to... notice so much..."
            show ep05_isaintro29 at ken_burns_left_to_right with hpunch
            isa "[daddy_r], you're making me nervous..."
            mc_s "The jacket will cover all this, right?"
            mc_t "Her skin's burning under my touch..."

            show ep05_isaintro30 with normalfade
            isa "Y-yes! The military jacket! It's over there..."
            isa "Should I... get it?"
            mc_s "Let me help you into it."

            show ep05_isaintro31
            isa "Okay, [da_r]... Let me get it."
            mc_t "She's still nervous from my touch..."
            mc_s "Right... the jacket..."

            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 3)
            $ check_levels("isabella", "cor", 3)
            $ ep05_isacosplay -= 1

    show ep05_isaintro32 with slowfade
    isa "Okay, I got it. It's heavier than I expected..."
    isa "Please, [daddy_r]? The shoulders are structured..."
    mc_t "Focus on helping her with the uniform..."

    $ show_walkthrough("ep05_isacheckmenu2")
    menu:
        mc_t "How should I help with this..."
        "Hold still":
            hide screen walkthrough_screen
            show ep05_isaintro33
            isa "Hold it open for me... it's pretty stiff..."
            mc_t "The details on this are impressive..."

            show ep05_isaintro34
            isa "The shoulders need to sit just right..."
            mc_t "At least this is covering more skin..."

            show ep05_isaintro35 with hpunch
            mc_s "Like this? The shoulders look even now."
            isa "Yes... perfect... you're good at this..."
            mc_t "Almost done..."

            $ rm.update("isabella", "trust", 3)
            $ check_levels("isabella", "trust", 3)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Let me adjust it":
            hide screen walkthrough_screen
            show ep05_isaintro36 with vpunch
            isa "D-[daddy_r_low]... your hands..."
            mc_t "The jacket's heavy but she's so warm..."

            show ep05_isaintro37
            mc_s "Stay still..."
            mc_t "Why am I touching her like this..."

            show ep05_isaintro38
            isa "The uniform... you're not really focusing on it..."
            mc_t "She knows exactly what I'm doing..."

            show ep05_isaintro39 at dramatic_focus_out with normalfade
            isa "I didn't know helping with cosplay would be like this..."
            mc_t "I should stop... but I can't..."

            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 3)
            $ check_levels("isabella", "cor", 3)
            $ ep05_isacosplay -= 1
    scene eigengrau with slowfade
    show ep05_isaintro40
    isa "Now for the boots... they're crucial for Commander White."
    mc_t "Those distinctive white boots..."
    isa "They're quite tall, like hers..."
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)

    show ep05_isaintro41 at ken_burns_top_to_bottom
    isa "Help me with these? They're not easy to put on..."
    mc_t "This part of the costume..."
    mc_s "Sure... let's get them on."

    show ep05_isaintro42 with vpunch
    isa "They go up past my knees... just like in the game..."
    mc_t "Keep it professional... it's just cosplay..."
    isa "The buckles are tricky..."
    $ show_walkthrough("ep05_isacheckmenu3")
    menu:
        mc_t "These do look complicated..."
        "Let me help with the buckles":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            show ep05_isaintro43 at ken_burns_left_to_right
            isa "Start from the bottom... work your way up..."
            isa "The other one needs the same... keep them even..."
            mc_t "Focus on the task, not her legs..."

            $ rm.update("isabella", "trust", 3)
            $ check_levels("isabella", "trust", 3)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Show me exactly how":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)

            show ep05_isaintro44 with vpunch
            mc_s "Guide my hands... show me how..."
            isa "L-like this? From ankle to thigh..."
            mc_t "Her skin's so warm..."

            show ep05_isaintro43 at ken_burns_left_to_right
            isa "The buckles... they need to be tight..."
            isa "Other side too... make them match..."
            mc_t "Every touch feels dangerous..."

            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 3)
            $ check_levels("isabella", "cor", 3)
            $ ep05_isacosplay -= 1
    scene eigengrau with slowfade
    show ep05_isaintro45 at ken_burns_corner_to_corner3 with vpunch
    isa "They're snug... like they should be..."
    mc_t "The white leather against her skin..."
    isa "Just the skirt left... to complete her look..."
    $ show_walkthrough("ep05_isacheckmenu4")
    menu:
        mc_t "Final piece..."
        "Let's finish the costume":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)

            show ep05_isaintro46 at ken_burns_left_to_right
            isa "The white skirt! Last piece..."
            mc_t "Keep it professional... almost done..."

            scene eigengrau with slowfade
            show ep05_isaintro48 at ken_burns_top_to_bottom with vpunch
            isa "These boots make standing difficult..."
            isa "Help me step into it..."
            mc_t "Just like a regular skirt..."

            $ rm.update("isabella", "trust", 3)
            $ check_levels("isabella", "trust", 3)
            $ rm.update("isabella", "cor", -1)
            $ check_levels("isabella", "cor", -1)
            $ ep05_isacosplay += 1
        "Stand still":
            hide screen walkthrough_screen
            scene eigengrau with slowfade
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)

            show ep05_isaintro47 at ken_burns_corner_to_corner4 with hpunch
            isa "Do I look like her? Like Commander White?"
            mc_t "She's really getting into character..."

            scene eigengrau with slowfade
            show ep05_isaintro49 at ken_burns_top_to_bottom with vpunch
            isa "The skirt's the final touch..."
            mc_s "Let me help you into it... slowly..."
            mc_t "One last chance to touch..."

            $ rm.update("isabella", "trust", -1)
            $ check_levels("isabella", "trust", -1)
            $ rm.update("isabella", "cor", 3)
            $ check_levels("isabella", "cor", 3)
            $ ep05_isacosplay -= 1

    show ep05_isaintro50 with normalfade
    isa "How do I look?"
    mc_t "Need to check everything..."
    isa "Inspect carefully, [daddy_r]..."
    mc_t "Final inspection..."
    while not (look_down_seen and look_middle_seen and look_up_seen):
        menu:
            "Look down" if not look_down_seen:
                $ look_down_seen = True

                show ep05_isaintro51 at subtle_zoom_in
                mc_t "Fuck... that slit in the skirt... I can see everything..."
                isa "The boots make the uniform look authentic, right?"
                mc_t "Those thighs... the way her lips peek through..."
            "Look at the middle" if not look_middle_seen:
                $ look_middle_seen = True

                show ep05_isaintro52 at subtle_zoom_out
                mc_t "Even with the jacket... her nipples are so visible through the lace..."
                isa "The material's really high quality! Just like in the reference..."
                mc_t "God... the way it clings to her body..."
            "Look up" if not look_up_seen:
                $ look_up_seen = True

                show ep05_isaintro53 at ken_burns_bottom_to_top
                mc_t "That innocent smile... she has no idea what she does to me..."
                isa "Did I capture Commander White's essence, [daddy_r]?"
                mc_t "My beautiful little girl... when did you grow up so much..."
    isa "Well? What do you think, [daddy_r]?"
    mc_s "I don't know much about Commander White, but you look stunning, Princess."

    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_inhale_fem, "sfx", 5, False, 0, 0)

    show ep05_isaintro54 at subtle_zoom_out with vpunch
    mc_t "She's jumping into my arms..."
    isa "You're the best, [daddy_r]! Thank you for helping!"
    mc_t "Her whole body's pressed against me..."

    $ stopAudio("sfx", 5, 2)
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_kiss_op_isa, "sfx", 4, False, 1, 0)

    show ep05_isaintro55 at ken_burns_right_to_left
    mc_s "Isab-mmph!"
    isa "Mmm..."
    if ep04_isabellakiss:
        mc_t "Her lips... she's actually kissing me again..."
    else:
        mc_t "Her lips... she's actually kissing me..."

    $ stopAudio("sfx", 4, 2)
    $ stopAllSubchannels("music", 2.0)
    scene eigengrau with slowfade
    show ep05_isaintro56
    isa "Oh god... I... I got too excited..."
    mc_t "Uhm.... she's covering her face in embarrassment..."
    mc_s "Isabella..."
    isa "Maybe you should check on [gra_r] now..."
    show ep05_isaintro57
    isa "I'll visit her later... after I finish the cosplay..."
    mc_s "Of course, Princess."
    mc_t "What have I awakened in her..."

    $ stopAllSubchannels("amb", 2.0)
    if ep05_isacosplay == 4 or ep05_isacosplay == -4:
        $ ep05_ach_isaintro = True
    jump ep05_elizintro




label ep05_elizintro:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
    pause 1.5
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_dooropen, "sfx", 2, False, 0, 0)
    $ setChannelVolume("amb", 1, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2, 0)

    show ep05_elizintro01
    mc_t "[mo_r]'s door is open..."
    mc_t "She never leaves it open..."
    mc_t "What's going on?"

    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(elizabeth_sad_theme, "music", 1, True, 4, 0)

    show ep05_elizintro02 at ken_burns_bottom_to_top
    mc_t "Huh? She's just sitting there in her babydoll... staring at the floor..."
    mc_t "Ever since I got here, she's been like this. Lost. Empty."
    mc_t "The light in her eyes is gone..."

    show ep05_elizintro03 at ken_burns_left_to_right
    mc_t "So many bottles of pills..."
    mc_t "Different colors, different labels... scattered everywhere."
    mc_t "[da_r]'s prescriptions... what are you doing to her?"

    show ep05_elizintro04 at ken_burns_bottom_to_top with hpunch
    mc_t "Huh?! What the-- when did she-? She's behind me..."
    mc_t "Her makeup's all smeared... has she been crying?"
    mc_t "She's just staring at herself in the mirror..."

    show ep05_elizintro05 with vpunch
    mc_s "[mo_r]?"
    mc_t "She's picking up more pills... swallowing them dry..."
    mc_t "Like they're candy..."
    ## save notification
    if htl_episodes == 5.1:
        $ show_custom_notification("save_tip")

    show ep05_elizintro06 at ken_burns_left_to_right with slowfade
    eli "[mc_name]...?"
    mc_t "That smile... but those eyes are drowning in tears..."
    eli "When did you come in, sweetie?"
    show ep05_elizintro07
    mc_t "She's trying so hard to look okay..."
    eli "You should've told me you were coming to visit..."
    mc_t "Her words are slurring..."

    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 5, False, 0, 0)

    show ep05_elizintro08 at subtle_zoom_in
    eli "Sit with me, darling... tell me about your day..."
    mc_s "[mo_r], I'm worried about you..."
    eli "Come here... let me hold you..."
    show ep05_elizintro09 with vpunch
    mc_t "Her body's so warm against mine..."
    eli "My sweet boy... you've grown so strong..."
    mc_t "My hands shouldn't be here... but I can't help it..."

    show ep05_elizintro10 at ken_burns_bottom_to_top with normalfade
    eli "Look at you... my handsome [so_r_low]..."
    mc_t "That smile... it's real this time..."
    mc_t "But something's wrong..."

    show ep05_elizintro11 at focus_shift
    mc_s "[mo_r]... what's happening to you?"
    eli "Everything's perfect now... just like before..."
#-- End Update
    if htl_episodes == 5.1:
        $ stopAllSubchannels(channel="sfx", fadeout=1)
        $ stopAllSubchannels(channel="amb", fadeout=1.5)
        $ stopAllSubchannels(channel="music", fadeout=2)
        scene eigengrau with rose
        pause 2.0
        $ resetAllVolumes()
        return


    else:
        jump ep05_elipast


## - 2ND DELIVERY




label ep05_elipast:
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAudio("amb", 1, 2)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene white with slowflash
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    $ setChannelVolume("amb", 2, 0.4, 0)
    $ playAudio(sfx_tokyo_residential, "amb", 2, True, 2, 0)

    show ep05_elipast01 at focus_shift, subtle_zoom_out
    mc_t "Stupid derivatives... stupid school..."
    mc_t "Damnit, what the hell is this? Why do they make math so complicated..."
    mc_t "If I don't finish this by tomorrow, I'm totally screwed for the test."

    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)

    show ep05_elipast02
    mc_t "Uhm... great! Now she's gonna scold me for sure!"
    eli "Such frustration in my precious boy..."
    eli "What's this? Calculus giving you trouble again?"
    eli "You look so adorably lost, sweetheart."
    # Decision point 1: affects elizabeth trust
    $ show_walkthrough("ep05_2nd_elipst")
    menu:
        "Annoyed response":
            hide screen walkthrough_screen

            mc_s "[mo_r], please. I'm trying to concentrate here."
            eli "Oh? Am I distracting you?"
            eli "I thought my brilliant [so_r_low] could handle a little... help."
            $ rm.update("elizabeth", "trust", -1)
            $ check_levels("elizabeth", "trust", -1)
        "Focus on studying":
            hide screen walkthrough_screen

            mc_s "Just... this test tomorrow..."
            eli "My poor darling. Math always was your weakness."
            eli "Good thing [mommy_r_low] knows just how to make it... click for you."
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
    $ setChannelVolume("sfx", 2, 0.3, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(elizabeth_play_theme, "music", 1, True, 4, 0)

    show ep05_elipast03 with hpunch
    eli "Let [mommy_r_low] teach you..."
    eli "These late-night galas are so dreadfully boring. I'd much rather be here with you."
    mc_s "Ehhh... These functions are impossible..."
    mc_t "She smells like champagne and that perfume she got from Paris."

    show ep05_elipast04 at subtle_zoom_in
    eli "Nothing's impossible with proper... instruction."
    eli "See, integration is all about finding what's hidden beneath the surface."
    eli "Something I've always been rather good at, wouldn't you say?"
    mc_t "Don't react... don't react..."
    mc_t "Focus on the math, not how her breath feels against my ear."

    $ setChannelVolume("music", 1, 0.15, 2.5)

    show ep05_elipast05 with normalfade
    eli "So, let's look at this integral... see how you can solve it step by step?"
    eli "The trick is knowing exactly when to... push forward and when to hold back."
    eli "Just like in life, darling. Timing is everything."
    mc_t "Focus, [mc_name]... just... don't think about [mo_r_low]'s... dress..."
    mc_t "God, why does she always do this after her parties?"

    show ep05_elipast06
    eli "It's all about... tension..."
    eli "The delicate balance between variables. Between what we want and what we're allowed."
    eli "Are you following me, sweetie?"
    mc_s "[mo_r], I can't focus when you're..."

    $ setChannelVolume("music", 1, 0.4, 2.5)

    show ep05_elipast07 at concentrate
    eli "When I'm what, darling?"
    eli "Using real-world applications to make your studies more... engaging?"
    eli "Or is it that you prefer your textbooks dry and boring?"
    mc_s "T-teaching like this..."
    mc_s "It's just... distracting."

    show ep05_elipast08 at concentrate
    eli "Don't think about [mommy_r_low] too much, sweetie."
    eli "Eyes on your paper. Though I can't help but notice yours keep... wandering."
    eli "Now, let's talk about limits..."
    eli "My favorite part of calculus, actually."
    show ep05_elipast09
    mc_s "Limits? Uh, yeah... like when something approaches but doesn't..."
    mc_s "When a function gets closer and closer to a value but never quite..."
    mc_t "She's practically sitting in my lap now. This is torture."
    eli "Exactly... approaching, getting so close, just not crossing that line..."
    eli "The mathematics of temptation, wouldn't you say?"
    show ep05_elipast10
    eli "Just like we are now... so close..."
    eli "I could practically solve this problem with my eyes closed. Want to see?"
    eli "Or would you rather just watch me, hmm?"
    mc_t "Oh God, this can't be happening..."
    mc_t "That's definitely not her perfume I'm smelling now."

    show ep05_elipast11 at ken_burns_right_to_left
    eli "You know, in Milan, they taught us that mathematics is the purest form of seduction."
    eli "The teasing possibility of a solution, always just out of reach."
    eli "Like now, when you're so close to understanding, but something's... distracting you."
    # Decision point 2: affects elizabeth corruption
    $ show_walkthrough("ep05_2nd_elipst2")
    menu:
        "Maintain innocence":
            hide screen walkthrough_screen

            mc_s "I'm just trying to learn calculus, [mo_r]."

            $ setChannelVolume("music", 1, 0, 3)

            mc_s "Can we focus on the formulas? Please?"
            eli "Such dedication to your studies. How... admirable."
            $ setChannelVolume("sfx", 3, 1, 0)
            $ playAudio(sfx_footsteps_bare_wood, "sfx", 3, False, 0, 0)
            eli "Very well, let's be proper then. No more... practical demonstrations."
            $ rm.update("elizabeth", "cor", -2)
            $ check_levels("elizabeth", "cor", -2)
        "Flirtatious reply":
            hide screen walkthrough_screen

            mc_s "Maybe the distraction is the point of this lesson?"

            $ setChannelVolume("music", 1, 0, 3)

            mc_s "You're making it hard to remember why I even cared about derivatives."
            eli "Clever boy. Understanding the subtext so quickly."
            $ setChannelVolume("sfx", 3, 1, 0)
            $ playAudio(sfx_footsteps_bare_wood, "sfx", 3, False, 0, 0)
            eli "Perhaps you're more like your [da_full_r_low] than I thought. Always seeing... opportunities."
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)

    show ep05_elipast12 with hpunch
    $ stopAudio("sfx", 3, 0.5)
    amb "[mo_r]! The show was amazing? I saw the news and--"
    amb "Oh. You're helping [mc_name] with homework? Can I watch too?"
    eli "Amber, darling... past your bedtime."
    eli "[mommy_r]'s giving your [br_full_r_low] a very special lesson right now."
    show ep05_elipast13
    amb "But I want to hear about—"
    amb "I just wanted to show you what they said about your dress on TV."
    eli "Bed. Now. Your [br_full_r_low] needs... tutoring."
    eli "The adults are talking, sweetheart. We'll discuss your little fashion opinions tomorrow."
    show ep05_elipast14 at ken_burns_top_to_bottom
    amb "Fine..."
    amb "I just thought you'd want to know they loved you..."
    mc_t "That look on Amber's face. [mo_r] crushed her without even trying."
    # Decision point 3: affects amber trust
    $ show_walkthrough("ep05_2nd_elipst3")
    menu:
        "Defend Amber":
            hide screen walkthrough_screen
            show ep05_elipast15
            mc_s "[mo_r], that was harsh. She just wanted to share something with you."
            mc_s "Amber looked really hurt just now."
            eli "Oh please, she's being dramatic. She knows I need to focus on your education."
            eli "When did you become so sensitive about your [si_full_r_low]'s feelings?"
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
        "Ignore the situation":
            hide screen walkthrough_screen
            show ep05_elipast15
            mc_s "Should we get back to these integrals? I still don't get them."
            mc_s "Time's running out and I really need to pass this test."
            eli "That's my boy. Always focused on what matters."
            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
    eli "Where was [mommy_r], sweetie? Oh right, limits... but maybe we'll just skip those tonight."
    eli "You seem tense. Perhaps we need a change of venue."
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_kiss_one, "sfx", 4, False, 0, 0)

    show ep05_elipast16 with hpunch
    eli "Perhaps tea would help us focus..."
    eli "Or something stronger? I have a bottle of that cognac you pretend not to steal sips from."
    eli "Our little secret, hmm? Just like these special tutoring sessions."
    eli "Your [da_full_r_low] never needs to know how... hands-on [mommy_r_low]'s teaching methods are."
    show ep05_elipast17 with normalfade
    mc_s "Tea... right..."
    mc_t "How the hell am I supposed to focus on calculus now?"

    $ stopAudio("amb", 2, 2)
    scene eigengrau with circlewipe
    pause 1
    show ep05_elipast18 with circlewipe
    $ setChannelVolume("amb", 3, 0.4, 0)
    $ playAudio(sfx_midnightpast, "amb", 3, True, 2, 0)
    eli "Your [da_full_r_low]'s always at that hospital..."
    eli "More concerned with his precious patients than his own [fm_r_low]."
    eli "He wouldn't notice if we burned the house down, would he, sweetheart?"
    mc_s "He works hard, [mo_r]. That's all."

    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 5, False, 0, 0)

    show ep05_elipast19 at impact_shake with vpunch
    mc_s "Whoa—!"
    mc_t "Shit! Of course I'd trip right now!"
    eli "Oh my, are you alright, darling?"
    show ep05_elipast20 at focus_shift
    eli "Always so clumsy around beauty, hmm?"
    eli "Or perhaps you just wanted a better view?"
    mc_s "I... I don't understand what you mean..."

    $ setChannelVolume("sfx", 6, 1, 0)
    $ playAudio(sfx_tea, "sfx", 6, False, 0, 0)
    eli "Those modeling shoots in Bali left such awkward tan lines... right?"
    mc_s "I-- I'm just... tired. Long day."
    mc_t "Don't look up. Don't look up. Don't—I'm looking up."

    show ep05_elipast21 at ken_burns_top_to_bottom
    $ stopAudio("sfx", 6, 0.5)

    mc_s "I should probably—"
    mc_s "It's getting late, and I still have that test..."
    eli "Shall we review limits again, sweetie?"
    eli "I find them so... fascinating. The point where restraint meets--"
    mc_s "Uhm, sure... limits, right."
    mc_t "Why does everything she says sound like she's talking about something else?"

    show ep05_elipast22
    eli "You know, we can bend them just a bit..."
    eli "Mathematics is all about knowing when to push beyond conventional boundaries."
    eli "Can you feel the tension in the equation, darling? How everything balances on a knife's edge?"
    mc_t "She's so close I can feel her heart beating. This is wrong. This is so wrong."
    mc_t "Move back. Now. Before this gets worse!"

    show ep05_elipast23 with hpunch
    mc_s "[mo_r]!"
    mc_s "I—you—this isn't—"
    eli "Wait!"
    eli "Oh!!"
    $ setChannelVolume("sfx", 7, 1, 0)
    $ playAudio(sfx_tea_splash, "sfx", 7, False, 0, 0)
    scene eigengrau
    pause 1
    show ep05_elipast24 at ken_burns_top_to_bottom
    eli "Quick, help [mommy_r_low] out of this... Can't let it ruin the fabric."
    eli "This dress cost more than your [da_full_r_low] earns in a week."
    eli "The silk is imported from Milan, and it's completely ruined now."
    mc_s "But..."
    mc_t "She can't be serious right now. Her dress is practically see-through!"

    $ setChannelVolume("sfx", 8, 1, 0)
    $ playAudio(sfx_clothes, "sfx", 8, False, 0, 0)

    show ep05_elipast25 at ken_burns_bottom_to_top
    eli "Shhh... just help [mommy_r_low]..."
    $ setChannelVolume("music", 1, 0.4, 3)
    eli "Don't act so shocked. You've seen models changing backstage plenty of times."
    eli "It's just skin, darling. Beautiful, expensive skin that your [da_full_r_low] pays fortunes to maintain."
    mc_t "Oh god, why is she... like that?"
    mc_t "This isn't normal. This isn't what [mo_full_r_low]s do."
    mc_s "We shouldn't..."

    show ep05_elipast26 at concentrate
    eli "Shouldn't what? Accidents happen, darling. Anyways, I can't be like this all night..."
    eli "Besides, it's nothing you haven't seen in those magazines you hide under your mattress."
    eli "Though I must say, [mommy_r_low]'s still got it better than those cheap girls, don't you think?"
    mc_s "This is wrong..."
    mc_t "I need to get out of here, now."

    show ep05_elipast27
    mc_s "You should cover up, [mo_r_low]!"
    mc_s "Anyone could walk in and see you like this!"
    eli "Maybe you're right... let's go to the bedroom."
    eli "I have something special there. Something I've been saving for the right moment."
    eli "Take my hand, sweetie. Let [mommy_r_low] show you something beautiful."
    $ stopAudio("amb", 3, 2)
    $ stopAudio("music", 1, 2)
    scene eigengrau with slowfade
    pause 1
    show ep05_elipast28 at focus_shift
    $ setChannelVolume("amb", 4, 0.4, 0)
    $ playAudio(sfx_mc_room_night, "amb", 4, True, 2, 0)
    eli "This is La Perla's finest. Imported from Italy, just like me."
    eli "The red is called 'Promessa passionale'. Appropriate, don't you think?"
    eli "They only made twelve of these in the world. I wore one just like it on the Milan runway last year."
    eli "Your [da_full_r_low] never notices these details..."
    eli "Too busy cutting into people to appreciate real art when it's right in front of him."
    mc_t "I shouldn't be seeing this. I shouldn't be here. Why can't I move?"

    $ setChannelVolume("music", 2, 0.4, 0)
    $ playAudio(elizabeth_theme, "music", 2, True, 4, 0)

    show ep05_elipast29 at ken_burns_corner_to_corner2
    eli "Let me show you a new thing... just don't tell [daddy_r_low], hmm?"
    eli "He wouldn't understand our special bond. How alike we truly are."
    eli "I see how you look at me, sweetie. It's the same way all men look at me."
    eli "But you're special. You're mine. My beautiful, brilliant boy."
    $ setChannelVolume("sfx", 9, 0.4, 0)
    $ playAudio(sfx_bed_sitdown, "sfx", 9, False, 0, 0)

    show ep05_elipast30
    eli "Just a little lesson, sweetie... You can use this example on the test tomorrow..."
    eli "Mathematics is about relationships between bodies, isn't it? The way they attract and repel."
    eli "See, the limit gets closer and closer... just like this..."
    eli "Feel how the tension builds as we approach the boundary?"
    mc_t "This can't be happening. My own [mo_full_r_low] is—I can't even think it."

    $ setChannelVolume("sfx", 1, 0.7, 0)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep05_elipast31
    mc_s "[mo_r], stop! You're drunk..."
    mc_s "This isn't you. This is the champagne talking."
    mc_t "Please let this be the alcohol. Please don't let this be who she really is."
    # Decision point 4: core amber suspicious of eli
    $ show_walkthrough("ep05_2nd_elipst4")
    menu:
        "Freeze in place":
            hide screen walkthrough_screen

            mc_s "I can't... we can't... this is insane."
            mc_t "I'm frozen. I can't even push her away. What's wrong with me?"
            eli "Don't fight it, darling. Some limits are meant to be crossed."
            eli "Besides, who would ever know? Our sweet little secret..."
            $ setChannelVolume("sfx", 3, 1, 0)
            $ playAudio(sfx_door_wood, "sfx", 3, False, 0, 0)
            $ stopAudio("music", 2, 3)
            scene eigengrau
            pause 1
            amb "[mo_r]? I had a nightmare..."
            $ ep05_ambersus_eli = True
            $ ep05_ach_ambvseli = True
        "Push her away":
            hide screen walkthrough_screen

            mc_s "Get off me! This has gone far enough!"

            $ setChannelVolume("sfx", 2, 1, 0)
            $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)
            $ setChannelVolume("sfx", 3, 0.6, 0)
            $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)
            $ stopAudio("music", 2, 3)
            scene eigengrau
            pause 1
            $ ep05_ambersus_eli = False
            $ ep05_ach_novseli = True

    show ep05_elipast32
    if ep05_ambersus_eli:
        amb "I saw monsters and they were—"
        amb "What... what are you doing?"
        amb "Why are you on top of [mc_name] like that?"
    else:
        mc_s "You need help, [mo_r]. This isn't normal!"
        eli "How dare you reject me! After everything I've done for you!"
        mc_s "Amber! Thank god you're here. [mo_r]'s not feeling well."
        mc_s "She had too much to drink at her party and fell. I was just helping her up."
        amb "Is [mommy_r] sick? Should I get [daddy_r] from the hospital?"
        amb "Your face is all red, [mc_name]. Are you getting sick too?"
        eli "Nobody's calling anybody. Especially not your [da_full_r_low]."
    show ep05_elipast33
    if ep05_ambersus_eli:
        $ setChannelVolume("music", 3, 0.4, 0)
        $ playAudio(elizabeth_anger_theme, "music", 3, True, 4, 0)
        eli "Go back to bed!"
        eli "This doesn't concern you, you stupid little girl!"
        amb "But..."
        amb "You're hurting [mc_name]. I can see it in his face."
        mc_t "Amber, please just go. You shouldn't see this."
    else:
        $ setChannelVolume("music", 3, 0.4, 0)
        $ playAudio(amber_sad_theme, "music", 3, True, 4, 0)

        mc_s "Everything's fine, [sis_r_low]. [mo_r] just needs some rest."
        mc_s "How about I check under your bed for monsters? Would that help?"
        amb "Would you? The shadows were moving again and making scary shapes."
        amb "You're the bravest, [mc_name]. You're not afraid of anything."
        mc_t "If only you knew how terrified I am right now."

    show ep05_elipast34
    if ep05_ambersus_eli:
        eli "Bed, now Amber."
        eli "I won't ask again."
        eli "Or I'll give you something to have nightmares about."
        mc_t "The look in [mo_r]'s eyes... I've never seen her like this. It's like she's possessed."
        amb "Okay... I'm sorry..."
    else:
        mc_s "Let's go check your room right now, okay? I'll stay until you fall asleep."
        mc_s "I'll even tell you that story about the brave fox you like so much."
        amb "The one where she outsmarts the snake? That's my favorite!"
        amb "Can we use flashlights under the blanket like a tent again?"
        mc_t "Anything to get away from this nightmare."

    show ep05_elipast35
    if ep05_ambersus_eli:
        mc_s "I-- I better just go... study alone..."
        mc_s "This... whatever this is... it needs to stop. Please."
        eli "Go, study... alone."
        eli "Ungrateful boy. Just like your [da_full_r_low]."
        mc_t "I've never been so relieved to escape a room in my life."
    else:
        mc_s "I'm sorry, [mo_r]. This was... I don't even know what this was."
        mc_s "But it can never happen again. Never."
        eli "Don't you dare judge me. You wanted it too. I saw it in your eyes."
        eli "Go play hero for your [si_full_r_low]. It's what you do best, isn't it?"
        mc_t "I need to protect Amber from... whatever [mo_r] is becoming."

    $ setChannelVolume("sfx", 4, 0.6, 0)
    $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)

    show ep05_elipast36 at ken_burns_top_to_bottom
    if ep05_ambersus_eli:
        eli "Tonight...I didn't want to be a [mo_r], I just wanted to be Elizabeth."
        eli "The Elizabeth who commands runways. The one men fight over backstage."
        eli "Not this shadow of myself, trapped between [chi_r] who needs me and a husband who doesn't see me."
        eli "Is it so wrong to want to feel that power again? Before it all slips away?"
    else:
        eli "They never understand what I sacrifice for them."
        eli "My career is at its peak, and what does Michael do? Works all night."
        eli "Men like the idea of a beautiful wife until she demands the attention she deserves."
        eli "Then they hide behind their work, their ethics... or run to younger women."
    $ stopAudio("amb", 4, 2)
    $ stopAudio("music", 3, 2)
    jump ep05_elishower




label ep05_elishower:
    scene white with slowflash
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    # Initial sequence (01-05)
    show ep05_elibath01
    $ setChannelVolume("amb", 5, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 5, True, 2, 0)

    mc_t "Where's she? ... Bathroom?"
    mc_t "One minute we were talking, the next she just... disappeared."
    mc_t "These memory flashes are coming back. Why? I can't tell what's now and what's then anymore."

    show ep05_elibath02
    mc_t "The shower?"
    mc_t "I don't think she's in any state to take a shower. She'll just flood the room."
    mc_t "With all those pills in her system, she could slip, hit her head..."

    show ep05_elibath03
    mc_t "The last thing I need is to find her passed out in a puddle of water."
    mc_t "Damn, when did I become the parent in this relationship?"
    mc_t "Maybe I should check on her. Make sure she's okay."

    $ setChannelVolume("sfx", 1, 0.6, 0)
    $ playAudio(sfx_door_knock, "sfx", 1, False, 0, 0)

    show ep05_elibath04
    mc_s "[mo_r]? You there?"
    mc_s "I just want to make sure you're alright."
    mc_t "This feels oddly familiar."

    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(elizabeth_singing_song, "music", 1, True, 4, 0)

    show ep05_elibath05 at ken_burns_corner_to_corner4
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}I was searching for the ocean beyond your shoulder..."
    mc_t "What's she doing?"
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}In the corner of a landscape blurring with tears..."
    mc_t "Singing?"
    mc_t "That old Akina Nakamori song she used to sing when I was a kid."
    # First branch decision
    $ show_walkthrough("ep05_2nd_elishow")
    menu:
        "Show concern":
            hide screen walkthrough_screen

            mc_t "She's completely out of it. Those pills mixed with whatever she drank..."
            mc_t "I should get her out of there before she hurts herself."

            $ ep05_mcthinksex = False
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
        "Be suspicious":
            hide screen walkthrough_screen

            mc_t "Is this another manipulation? Another way to pull me into her web?"
            mc_t "Thirty years of modeling taught her how to make anything look natural."

            $ ep05_mcthinksex = False
        "Inappropriate thoughts":
            hide screen walkthrough_screen

            mc_t "Fuck... even at her age, her body's still incredible."
            mc_t "Those long legs, that ass that's still firm despite the years..."

            $ ep05_mcthinksex = True
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
    # Path after first decision (06-08)
    scene eigengrau with dissolve
    $ setChannelVolume("sfx", 3, 1, 0)
    $ playAudio(sfx_showering, "sfx", 3, True, 3, 0)
    pause 1
    show ep05_elishower1 at focus_shift, ken_burns_right_to_left with normalfade
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor} That shore scattered with our memories..."
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}I want to turn it into a small green stone and keep it in my heart..."
    $ setChannelVolume("sfx", 3, 0.4, 1.0)

    show ep05_elibath06 with normalfade
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}Between repeating dawns and dusks..."
    mc_t "I've got a bad feeling..."
    mc_t "She's not even aware I'm here."
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}We depart from the season of goodbyes..."
    $ setChannelVolume("sfx", 3, 0.8, 1.0)

    show ep05_elibath07 at ken_burns_corner_to_corner3
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}Leaving a fragment of emerald in each other's hearts..."
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}If you close your eyes, kiss my eyelids..."
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}I wish you'd quietly disappear without saying goodbye..."
    $ setChannelVolume("sfx", 3, 1, 1.0)

    show ep05_elishower2 at focus_shift, ken_burns_bottom_to_top
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}Like waking from a dream, I want to forget you..."
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}The memories reflected in my tears flow to the bottom of the sea..."
    $ setChannelVolume("sfx", 3, 0.4, 1.0)

    show ep05_elibath08 with normalfade
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}This wounded love can no longer look back..."
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}Turning my back on sadness, I feel I can walk alone now..."
    # Middle sequence (09-15) and reset mcthinksex
    $ setChannelVolume("sfx", 3, 0.7, 1.0)

    show ep05_elibath09 at ken_burns_left_to_right
    $ ep05_mcthinksex = False  # Reset mcthinksex
    eli "{outlinecolor=#ffffff00}🎶{/outlinecolor}Because I hold a fragment of emerald against my heart..."
    eli "I should have never left Milan... never married a man who can't see beauty decay..."
    eli "Thirty years of my life... wasted..."
    $ stopAudio("sfx", 3, 2)
    scene eigengrau with slowfade
    pause 1
    show ep05_elibath10 at ken_burns_bottom_to_top
    eli "My body betrays me... inside and out..."
    mc_t "I've never seen her this vulnerable before."
    mc_t "She's always been obsessed with her image, even at home. This is... disturbing."
    mc_t "No wonder she takes so many pills. Reality must be unbearable for her."

    $ stopAudio("music", 1, 4)

    show ep05_elibath11 with normalfade
    eli "Sweetie... how long have... have you been watching?"
    eli "Your [mo_full_r_low] is a mess, isn't she? Not the woman you remember."
    show ep05_elibath12 at ken_burns_right_to_left
    eli "You shouldn't see [mo_r] like this, so pathetic... so old..."
    eli "God, these sagging breasts, these stretch marks... this wasted body."
    show ep05_elibath13
    mc_s "[mo_r], no. You're beautiful. Always have been. You're just not well."
    mc_s "The pills, the drinking—they're making everything worse."
    mc_s "Let me help you. Please."

    show ep05_elibath14
    eli "I don't deserve a [so_r_low] like you. So... so good to me. And what am... what do... what have..."
    eli "Why am... am I such a failure? A drunk... a junkie..."
    show ep05_elibath15
    mc_s "Let me help you get to bed."
    mc_s "You're going to catch cold standing there like this."
    # Second branch decision
    $ show_walkthrough("ep05_2nd_elishow2")
    menu:
        "Positive memory":
            hide screen walkthrough_screen

            mc_s "Remember when you'd help me prepare for tests? How patient you were?"
            mc_s "You'd stay up all night if that's what it took. No matter how tired you were."
            mc_s "That woman is still in there somewhere. The one who cared so much."

            $ ep05_mcthinksex = False
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)
        "Vague recollection":
            hide screen walkthrough_screen

            mc_s "Life hasn't been easy for either of us, has it?"
            mc_s "But we're still here. We're still standing. That has to count for something."
            mc_s "Let's just get you to bed before you catch cold."

            $ ep05_mcthinksex = False
        "Inappropriate memory":
            hide screen walkthrough_screen

            mc_s "Remember how you used to come to my room in that silk nightgown?"
            mc_s "The way it clung to your body... how you'd let it slip off your shoulder..."
            mc_s "How your hand would always find its way under the covers..."

            $ ep05_mcthinksex = True
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)
    # Path after second decision (16-19)
    $ setChannelVolume("music", 2, 0.4, 0)
    $ playAudio(mc_elizabeth_theme, "music", 2, True, 4, 0)

    show ep05_elibath16
    eli "Remember when you'd help me prepare for shoots?"
    eli "You had such an eye for what worked. Which outfits would photograph best."
    eli "You knew my body better than anyone... every angle, every curve..."
    mc_s "Of course, [mo_r]. We made a great team, didn't we?"
    mc_s "You always looked perfect. Every magazine cover, every runway."

    show ep05_elibath17 at concentrate
    eli "Yes, yes. You were so helpful... and... and kind."
    eli "Even when the other boys your age were out playing, you stayed with [mommy_r_low]."
    eli "My perfect little man. The only one who ever truly saw me."
    show ep05_elibath18 at ken_burns_top_to_bottom
    eli "I'm tired..."
    eli "...of pretending everything is okay. It isn't... it hasn't been..."
    eli "The pills don't work anymore. Nothing does. I feel everything slipping..."
    eli "My beauty, my sanity, my purpose... what am I without them?"
    show ep05_elibath19
    eli "Please... just hold me..."
    eli "Make me feel beautiful again. Like when you were younger and looked at me that way."
    eli "...please..."
    eli "Just for tonight. Just for now. Before I disappear completely."
    # Determine which path to follow (naughty or love)
    $ ep05_naughty_path = False
    if rm.get("elizabeth", "cor") > rm.get("elizabeth", "trust"):
        $ ep05_naughty_path = True
    elif rm.get("elizabeth", "trust") == rm.get("elizabeth", "cor"):
        # Equal values - random choice
        $ ep05_naughty_path = renpy.random.randint(0, 1) == 1
    # Show appropriate images based on path
    if ep05_naughty_path:
        show ep05_elibath21
        eli "I need to feel something... anything besides... this..."
        eli "Feel like a woman again... not just a decoration in this house..."
        eli "Your touch... always made me feel so alive... so wanted..."
        show ep05_elibath23 at ken_burns_left_to_right
        eli "Look at us..."
        eli "Do anyone still want me? Even like this? Even with these wrinkles, these sagging breasts?"
        eli "I'm... disgusting... an old woman... a monster..."
        show ep05_elibath25 at ken_burns_corner_to_corner4
        eli "Your hands feel so good... so different from him..."
        eli "No one has to know... our little secret... like before... right?"
    else:
        show ep05_elibath20
        eli "I need to feel something... anything besides... this..."
        eli "Some mornings I wake up and don't recognize myself in the mirror."
        eli "Where did she go? That woman everyone wanted? That woman you adored?"
        show ep05_elibath22 at ken_burns_left_to_right
        eli "Look at us..."
        eli "Time is so cruel, isn't it? Especially to women like me."
        eli "I'm... disgusting... an old woman... a monster..."
        show ep05_elibath24 at ken_burns_corner_to_corner4
        eli "I turned down Paris for this life. My last chance at the big time."
        eli "Now I'm just Michael's aging wife. The European Rose, wilted."
    # Final sequence (20-25)
    show ep05_elibath26
    mc_s "[mo_r], look at me."
    mc_s "You need to stop this. You're hurting yourself."
    mc_s "You are the most beautiful woman in the world. No mirror will tell otherwise."
    mc_s "Let me help you get dressed and back to bed."

    show ep05_elibath27
    eli "No... get out! GET OUT!"
    eli "Don't look at me like that! With pity! I don't need your fucking pity!"
    eli "You're just like him! Pretending to care while judging every flaw!"
    eli "GET OUT! NOW! LEAVE ME ALONE!"
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_slamdoor, "sfx", 4, False, 0, 0)
    $ stopAudio("music", 2, 2)

    show ep05_elibath28
    mc_t "Fuck. I handled that all wrong."
    mc_t "She's too far gone right now. Too many pills, too much alcohol, too much self-loathing."
    mc_t "I'll check on her when she sobers up. If she even remembers any of this."

    $ stopAudio("amb", 5, 2)
    jump ep05_smspaz_intro




label ep05_smspaz_intro:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep05_smspz01 at ken_burns_left_to_right with circlewipe
    $ setChannelVolume("amb", 6, 0.5, 0)
    $ playAudio(sfx_earlypast, "amb", 6, True, 2, 0)

    mc_t "Elizabeth's breakdown was worse than I expected. She needs professional help, not more pills."
    mc_t "I need to clear my head. Focus on something I can actually solve."
    mc_t "That attack on Paz in my apartment... I should check how she's doing."
    mc_t "At least with Paz, I know where I stand. Unlike this twisted [fm_r_low] dynamic."

    show ep05_smspz02 at ken_burns_top_to_bottom
    mc_t "I'm just gonna make sure everything is all right."
    mc_t "She took a beating because of me. Because she was looking into things I asked her to."
    mc_t "While I've been dealing with Elizabeth's drama, Paz has been putting herself in real danger."

    show ep05_smspz03
    mc_t "What if that masked woman comes back for her? What if she's hurt worse than she let on?"
    mc_t "I couldn't protect Elizabeth from herself. Maybe I can at least help Paz."
    mc_t "After everything we've been through in Osaka, I owe her that much."

    jump ep05_smspaz_phone




label ep05_smspaz_call:
    # Initial sequence (01-21)
    show ep05_smspz03 at focus_shift
    pause 1.0
    $ setChannelVolume("sfx", 5, 0.5, 0)
    $ playAudio(sfx_vcall, "sfx", 5, True, 0, 0)
    call screen videocall_icons("ep05_pazvc")




label ep05_pazvc:
    hide ep05_smspz03
    $ stopAudio("sfx", 5, 0.5)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(paz_theme, "music", 1, True, 4, 0)

    show ep05_callpz01 at scale_down, videocall_open
    pa_s "Hell yeah, here I am on my new phone."
    pa_s "Thought I'd never cave, but turns out flip phones aren't cutting it anymore."
    pa_s "Don't judge the mess. Been busy with this... situation."

    show ep05_callpz02 at scale_down
    mc_s "So, about those pictures from my apartment—did you manage to recover them?"
    mc_t "Damn, she doesn't even realize how she's sitting. Same old Paz, zero self-awareness."
    pa_s "Yes. One moment..."
    pa_s "Gotta find it in this disaster of a gallery... there."

    show ep05_callpz03 at scale_down
    pa_s "Check this out."
    paz_nvl "{a=show:picview_ep05_sms03}{image=thumb_ep05_sms03}"
    pa_s "That's some occult shit, isn't it?"
    pa_s "Freaky as hell. Found it exactly like this when I got there."

    show ep05_callpz04 at scale_down
    pa_s "Does it mean anything to you? I mean that's what that woman said, that everything was for you."
    pa_s "Fox-mask lady had your name, knew your apartment. Creepy stuff."
    pa_s "Not your typical break-in, that's for sure."

    show ep05_callpz05 at scale_down
    mc_s "I don't know, I'm gonna check what I can find about it."
    mc_t "What the hell have I gotten her into?"
    pa_s "Do you think it's related to the Tanaka case?"
    mc_s "The Kobe Yagamaguchi-gumi?"
    pa_s "Maybe... I mean the case got closed pretty abruptly... like they didn't want us to keep investigating it."
    pa_s "Just when we were getting somewhere, poof—gone."

    show ep05_callpz06 at scale_down
    pa_s "You get promoted even when you were so deep in that case and suddenly all the evidence goes away."
    pa_s "Convenient timing, don't you think? You're out, case closed, everyone moves on."
    pa_s "Except now we've got fox-mask lady leaving you presents."
    mc_s "Well I can't argue about that..."
    mc_t "She's pissed. That spark in her eyes is the same one from the Takahashi raid. Nothing good follows that look."

    show ep05_callpz07 at scale_down
    pa_s "I know I'm not like you. You're like a genius and all, but don't you find that suspicious?"
    pa_s "You of all people. The guy who sees patterns in everything."
    pa_s "Ever since you left, stuff's been weird at the precinct."
    mc_s "I don't know... what are you trying to say, Paz?"
    mc_s "That someone's covering tracks?"

    show ep05_callpz08 at scale_down
    pa_s "I've been checking all these stuff..."
    pa_s "Been digging through what's left of your case files. Most of it's gone or redacted."
    pa_s "Sorry for unprofessional look but I've been here since 5 AM."
    pa_s "Haven't exactly been prioritizing dress code lately."

    show ep05_callpz09 at scale_down
    pa_s "So, there's no trace left in the system. Like someone deleted them."
    pa_s "Pictures, reports, witness statements—poof. Digital trail's cold."
    pa_s "Someone's got access who shouldn't."
    mc_s "Are you suggesting a conspiracy or we have a mole or something?"
    pa_s "Maybe. Don't you think it's all a bit... convenient? Like, too perfect?"
    pa_s "Our rookies couldn't delete lunch orders without leaving traces."
    mc_s "So, let me guess, what do you propose to do, then?"
    mc_t "She's already made up her mind. That determined look hasn't changed since academy days."

    show ep05_callpz10 at scale_down
    pa_s "We can investigate together. On our own."
    pa_s "Like we did with the smuggling ring. Just you and me, off the books."
    pa_s "Before things went to shit."

    show ep05_callpz11 at scale_down
    mc_s "Paz, I wish I could help, but honestly, what can we do right now?"
    mc_s "I'm still injured and fucked up in Tokyo and you're still a field officer in Osaka, right?"
    mc_s "Can't exactly hop on a train with this leg."
    pa_s "So you say I can't investigate because I'm not a detective like you?"
    pa_s "After all the crap we went through? That's how it is now?"
    pa_s "Rank finally went to your head, [mc_name]?"

    show ep05_callpz12 at scale_down
    mc_s "It's not about that. I didn't even want a promotion in the first place."
    mc_s "But the fact remains that you can't access some stuff."
    mc_s "Also, how could we do that from 500 kilometers away? You know that's not going to work, right?"
    mc_s "This isn't about badges or rank."
    mc_s "Besides that, what if something like the incident from that night happens to you again? What will happen then?"
    mc_s "I'm not there to have your back this time."

    show ep05_callpz13 at scale_down
    pa_s "Well, we could start with the info we got from the apartment, like that picture. It's a start, right?"
    pa_s "I'm already in it. Fox-mask lady made sure of that."
    pa_s "And don't worry about me. If anything like that ever happened to me again, well... let's say that I would make sure to be prepared this time."
    pa_s "Got my piece under the pillow now. Won't catch me sleeping again."

    show ep05_callpz14 at scale_down
    mc_s "You should rest, you still on night shift?"
    mc_t "She hasn't changed a bit. Still charging ahead, consequences be damned."
    pa_s "Can't sleep lately. Remember our late shifts? When you'd bring coffee at 3 AM?"
    pa_s "That god-awful vending machine sludge you called coffee."
    pa_s "Kinda miss it, actually. Quiet nights, bad coffee, good company."

    show ep05_callpz15 at scale_down
    mc_s "Worst coffee in Osaka, yeah. But your company made it taste good."
    mc_s "Never did find coffee that bad in Tokyo. It's a special Osaka talent."
    pa_s "Miss that. Miss working with you."
    pa_s "Place isn't the same without your brooding ass around."
    pa_s "Oh! Almost forgot."

    show ep05_callpz16 at scale_down
    pa_s "Check this too"
    paz_nvl "{a=show:picview_ep05_sms04}{image=thumb_ep05_sms04}"
    pa_s "Found it around all those bells."
    pa_s "Looks familiar?"

    show ep05_callpz17 at scale_down
    mc_s "A key?"
    mc_t "That key... reminds me of something, but I can't place it."
    pa_s "That's the key of the ritual circle found on your apartment."
    pa_s "Center of the whole thing. Like it was some kind of focal point."

    show ep05_callpz18 at scale_down
    mc_s "Do you have it?"
    mc_s "I need to get a closer look at it."
    pa_s "Sadly I don't. It's in evidence storage at the PD."
    pa_s "Standard procedure. Logged and bagged."
    pa_s "Evidence locker 3, if you're curious."

    show ep05_callpz19 at scale_down
    pa_s "Do you think I should take a trip there and retrieve it, what you say?"
    pa_s "Wouldn't be hard. Night shift's usually just Takeda, and he sleeps half the time."
    pa_s "In and out, ten minutes tops."
    mc_s "What? Stealing from an Osaka PD evidence locker?"
    mc_s "You can't be serious... that's career suicide!"
    mc_s "They catch you, that's it. No second chances."

    show ep05_callpz20 at scale_down
    pa_s "Well... you already have seen what happens to anything that has a link with the Kobe Yagamaguchi-gumi, haven't you?"
    pa_s "How long before this key disappears too? A day? A week?"
    pa_s "You know I'm right. We're running out of time."
    mc_s "I don't know... I can't push you to do that..."
    mc_s "It's your career on the line, not mine."

    show ep05_callpz21 at scale_down
    pa_s "Don't talk about pushing, lol, I haven't forgotten you pushed me from the car that night"
    pa_s "Saved my ass then. Maybe it's my turn to return the favor."
    pa_s "Well, it's up to you. I'm already deep in this."
    pa_s "Say the word, partner. Just like old times."

    $ show_walkthrough("ep05_2nd_paz")
    menu:
        "Support stealing evidence":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -8)
            $ ep05_integrity_choice = "negative"
        "Insist on legal methods":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 8)
            $ ep05_integrity_choice = "positive"
    # Final sequence with different dialogues based on choice
    show ep05_callpz22 at scale_down
    if ep05_integrity_choice == "negative":
        mc_s "You really don't have to do it."
        mc_s "But... yeah. Go for it. And be careful. Please. No risks."
        mc_s "First sign of trouble, you bail. Promise me that."
    else:
        mc_s "No, Paz. We do this by the book. Request the evidence properly."
        mc_s "I'm not letting you throw away your badge for this."
        mc_s "We'll find another way. We always do."

    show ep05_callpz23 at scale_down
    if ep05_integrity_choice == "negative":
        pa_s "Yes, sir!"
        pa_s "Look at you, all worried. It's cute."
        mc_s "Let me know when it's safe for you to head over."
        pa_s "I'm going right now!"
    else:
        pa_s "By the book? Seriously? After everything we've seen?"
        pa_s "You know that key won't be there in 24 hours."
        pa_s "But fine. Your call, [mc_name]. Hope you know what you're doing."

    show ep05_callpz24 at scale_down
    if ep05_integrity_choice == "negative":
        mc_s "Wait, NOW? Like, literally? Are you crazy?!"
        mc_s "God, Paz, at least wait till morning!"
        pa_s "You don't become a detective by being careful all the time, do you, [mc_name]?"
        pa_s "Night's the perfect time. Fewer eyes."
    else:
        mc_s "I know you're frustrated. I am too. But we can't stoop to their level."
        mc_s "If we break the rules, we're no better than them."
        pa_s "Rules. Right. Because they've worked so well for us."
        pa_s "Wake up, [mc_name]. The game is rigged."

    show ep05_callpz25 at scale_down
    if ep05_integrity_choice == "negative":
        mc_s "I don't like the idea, but okay..."
        mc_s "Just let me know when it's over, and stay safe, okay?"
        mc_s "And Paz? Thanks. I mean it."
    else:
        mc_s "Just give me time to figure something out from this end."
        mc_s "We'll get that key, but the right way."
        pa_s "Time. The one thing we don't have. But whatever."

    show ep05_callpz26 at scale_down
    if ep05_integrity_choice == "negative":
        pa_s "Don't worry, [mc_name]. You can always count on me."
        pa_s "Like old times, right? Me doing the legwork, you overthinking everything."
        pa_s "See ya later."
        mc_s "See ya, Paz. Be careful out there."
    else:
        pa_s "Twenty-four hours. That's all you get."
        pa_s "After that, I'm doing it my way, partner or not."
        pa_s "Don't let me down, [mc_name]."
        mc_s "I won't. I promise."

    show ep05_smspz03 at focus_shift
    pause 1.0
    $ stopAudio("music", 1, 4)
    jump ep05_intromn




label ep05_intromn:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep05_mnintro01 at ken_burns_left_to_right
    mc_t "That call with Paz has my head spinning. Rituals, fox masks, evidence theft..."
    mc_t "I need to clear my mind."
    mc_t "After what I saw by the pool this morning, I should check on Nanami... just in case!"

    $ stopAudio("amb", 6, 2)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_door_knock, "sfx", 1, False, 0, 0)
    pause 1
    show ep05_mnintro02 with circlewipe
    $ setChannelVolume("amb", 7, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 7, True, 2, 0)
    isa "Searching for something, [da_full_r]?"
    isa "Or should I say... someone? You look like you're on a mission."
    mc_s "Madison and Nanami. Seen them?"

    show ep05_mnintro03 at ken_burns_right_to_left
    isa "Your real [dau_r_low] is right here."
    mc_s "Yes, yes, Commander White, don't be jealous now."
    mc_s "I just want to make sure Nanami is okay. Madison can be... intense."
    isa "They're not in this bathroom."
    isa "They were supposed to be doing yoga or something."
    show ep05_mnintro04
    isa "Wait! I know where they are... follow me."
    isa "Madison has a special spot for her 'private lessons' with Nanami."
    isa "I've seen them disappear there before. Madison thinks she's so sneaky."
    mc_s "Ok."
    mc_s "Lead the way, Commander."

    $ stopAudio("amb", 7, 2)
    scene eigengrau with slowfade
    pause 1
    show ep05_mnintro05
    $ setChannelVolume("amb", 1, 0.4, 0)
    $ setChannelVolume("amb", 2, 0.5, 0)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 1, 0)
    $ playAudio(sfx_wind_pool, "amb", 2, True, 1, 0)
    $ setChannelVolume("music", 1, 0.4, 0)
    $ playAudio(isabella_theme, "music", 1, True, 4, 0)
    isa "Now we just need to head left this way, and we'll find a new spot you haven't seen yet."
    mc_s "What the fuck?! Another room?"
    mc_s "How many secret spaces does this house have?"
    mc_t "Just when I think I know this place, something new appears."
    isa "They probably went to take a bath together... like they do most times..."
    isa "Madison says it's 'traditional Japanese bonding' or whatever."
    isa "She's been doing it since they became friends."
    mc_s "Most times?!!"
    mc_s "And nobody thought this was weird?"

    $ stopAudio("amb", 2, 2)
    scene eigengrau with slowfade
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_door_glass, "sfx", 2, False, 0, 0)
    pause 1
    show ep05_mnintro06
    isa "Yeah... like.. every time that Nanami is around..."
    isa "Madison's very... protective of their friendship."
    isa "Gets super jealous if anyone else spends time with Nanami."
    mc_s "Wow..."
    mc_s "That explains a lot about how she reacted when I talked to Nanami."
    mc_t "What exactly is Madison doing here?"

    show ep05_mnintro07 at ken_burns_bottom_to_top
    isa "Anyway, I'm off to the cosplay contest! I don't know why you wanted to check on them, but here it is, just in case."
    isa "Be careful though. Madison will flip if she catches you spying."
    isa "Just don't say or think anything that might upset me..."
    isa "You know how I feel about you paying attention to other girls."
    show ep05_mnintro08
    mc_s "Yes, ma'am, Commander White, ma'am."
    mc_s "Go win that contest. Show them what a real cosplayer looks like."
    isa "Don't mock me, [da_r_low]!"
    isa "I worked hard on this costume. I'm going to crush the competition."
    isa "Unlike some people, I actually finish what I start."
    $ stopAudio("music", 1, 2)

    show ep05_mnintro09 at subtle_zoom_out with normalfade
    mc_t "The garden greenhouse... converted to a Japanese bath? Elizabeth's extravagance knows no bounds."
    mc_t "Beautiful place though. Almost peaceful, if it weren't for what's happening in there."
    mc_t "I can hear voices... That's definitely Nanami and Madison."

    $ setChannelVolume("sfx", 3, 0.7, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 3, False, 0, 0)

    show ep05_mnintro10
    mad "What are you looking at?"
    $ stopAudio("sfx", 3, 2)
    mad "Spying again, [br_full_r_low]? Becoming quite the habit."
    mad "First by the pool, now here. Developing a taste for voyeurism?"
    mc_s "Just passing by. Didn't know anyone was here."
    mad "Thought you'd left."
    mc_s "Yeah, but.. uhm.. just checking up on things."
    mc_s "Making sure everything's okay after this morning."
    mad "Of course you are."
    mad "Always so concerned. Such a protective big [br_full_r_low]."
    mad "Though I notice you're more protective of some than others."
    $ setChannelVolume("sfx", 3, 0.7, 0)
    $ playAudio(sfx_footsteps_bare, "sfx", 3, False, 0, 0)

    show ep05_mnintro11 at ken_burns_left_to_right
    mc_t "Woah... Almost caught me checking on them!"
    mc_t "Madison's eyes... that wasn't just annoyance. That was pure possessive rage."

    $ stopAudio("sfx", 3, 2)

    mc_t "Maybe I should back off. But something about this feels wrong."
    mc_t "Is she going to get back? Maybe she is going to change clothes or something..."
    mc_t "I mean, Nanami is alone now... I can ask her how she's doing..."
    mc_t "But if Madison catches me talking to her again..."
    # First choice - Wait or Don't Wait
    $ show_walkthrough("ep05_2nd_mnbath")
    menu:
        "Wait for Madison to leave":
            hide screen walkthrough_screen
            $ ep05_mnwait = True
        "Check on Nanami now":
            hide screen walkthrough_screen
            $ ep05_mnwait = False
            # DON'T WAIT path - exits after completion
            $ stopAudio("amb", 1, 2)
            scene eigengrau with slowfade
            pause 1
            show ep05_mnbath01 at ken_burns_right_to_left
            $ setChannelVolume("amb", 3, 0.5, 0)
            $ playAudio(sfx_evening_pool, "amb", 3, True, 2, 0)

            mc_t "Just need to check if she's okay..."
            mc_t "If Madison's doing something to her... I can't just stand by."
            mc_t "And if Nanami's uncomfortable, she might not know how to speak up."

            $ setChannelVolume("sfx", 4, 0.7, 0)
            $ playAudio(sfx_grass_walk, "sfx", 4, False, 0, 0)

            show ep05_mnbath02
            mad "Really, [br_full_r_low]?"
            $ stopAudio("sfx", 4, 2)
            mad "Another man thinking he has the right to invade a woman's space."
            $ setChannelVolume("music", 2, 0.4, 0)
            $ playAudio(madison_bad_theme, "music", 2, True, 4, 0)
            mad "Did [daddy_r_low] teach you to be a peeping tom, or is that natural male instinct?"
            $ setChannelVolume("sfx", 5, 1, 0)
            $ playAudio(sfx_bodygrab, "sfx", 5, False, 0, 0)

            show ep05_mnbath03 at ken_burns_top_to_bottom with vpunch
            mc_s "I was just—"
            mc_s "Making sure Nanami isn't being manipulated."
            mad "Manipulated? Please."
            mad "You're exactly like [da_full_r]. Pretending nobility while satisfying your disgusting urges."
            mad "Men never protect women. They just pick which predator gets first access."
            show ep05_mnbath04
            mad "That's why I protect her from men like you--"
            mad "From men, period. The world's greatest disease."
            mad "Don't make me tell her what you tried to do."
            mad "I'd hate to shatter her pure image of her precious [mc_name]."
            mad "Though maybe seeing your true nature would be the best lesson..."
            show ep05_mnbath05
            mc_t "Maybe I should just go..."
            mc_t "Madison's hatred runs deeper than I thought. Has she always seen me this way?"
            nana "Maddie! Y-you're back!"
            mad "Sorry for the interruption, sweet one. Just chasing off a pest."
            nana "Was someone there? I thought I heard voices..."
            mad "Nobody important. Just my disgusting [br_full_r_low]."
            nana "[mc_name]? But he's not—"
            mad "Let me tell you what men really think about girls like us, Nanami..."
            $ stopAudio("music", 2, 2)
            $ stopAudio("amb", 3, 2)
            jump ep05_elibdown


    # If we get here, player chose WAIT path
    scene eigengrau with slowfade
    show ep05_mnbath01 with circlewipe
    mad "Still lurking around, [br_full_r_low]? Can't find anything better to do?"
    mc_s "Just making sure everyone's alright."
    mad "How noble. Always the [fm_r_low] protector."
    scene eigengrau with slowfade
    show ep05_mnbath02
    mc_t "She's gone back inside. What now?"
    mc_t "Nanami's alone with her again."
    mc_t "Something about their 'friendship' doesn't sit right."

    $ stopAudio("amb", 1, 2)
    scene eigengrau
    pause 1
    show ep05_mnbath03 at ken_burns_right_to_left with normalfade
    $ setChannelVolume("amb", 3, 0.5, 0)
    $ playAudio(sfx_evening_pool, "amb", 3, True, 2, 0)

    mc_t "I'll just observe from here. Need to see what Madison's really up to."
    mad "Here, I brought some water from inside."
    nana "Thank you, Maddie."
    mad "Of course, sweetie. I always take care of what's mine."
    $ setChannelVolume("sfx", 6, 0.5, 0)
    $ playAudio(sfx_drinking_fem, "sfx", 6, False, 0, 0)

    show ep05_mnbath04
    nana "Ehm, Maddie. I am thirsty too..."
    nana "Could I have some?"
    mad "I know a special way we can share."
    $ setChannelVolume("sfx", 7, 0.5, 0)
    $ playAudio(sfx_kiss_water, "sfx", 7, False, 0, 0)
    $ setChannelVolume("sfx", 8, 0.5, 0)
    $ playAudio(sfx_gulping_water, "sfx", 8, False, 0, 0)

    show ep05_mnbath05 at dramatic_focus
    nana "Mmph!!"
    mc_t "Fuck! Fuck! Fuck!!!"
    mc_t "Did she just—? With Nanami?"

    $ setChannelVolume("music", 3, 0.4, 0)
    $ playAudio(madison_nan_theme, "music", 3, True, 4, 0)

    show ep05_mnbath06 at ken_burns_bottom_to_top with normalfade
    mad "So? Did you like that?"
    mad "First time sharing like girls do? Like women do?"
    nana "I-- I didn't expect that at all..."
    mad "You're just too cute, Nanami."
    nana "Thank you, Maddie..."
    show ep05_mnbath07
    nana "But wasn't that a kiss?"
    mad "No... That was just sharing water."
    mad "Don't overthink it."
    nana "Eh?"
    nana "But your lips..."
    show ep05_mnbath08 at ken_burns_bottom_to_top
    mad "Kissing is more like this."
    mad "Let me show you what real women do together."
    mad "What we can share that men can never understand."
    $ setChannelVolume("sfx", 9, 0.8, 0)
    $ playAudio(sfx_kiss_one, "sfx", 9, False, 0, 0)

    show ep05_mnbath09 at dramatic_focus_out
    mc_t "Fuck! She's completely manipulating her."
    mc_t "Using Nanami's insecurity and need for acceptance."

    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_bathtub_sink1, "sfx", 1, False, 0, 0)
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_bathtub_sink2, "sfx", 2, False, 0, 0)
    scene eigengrau with slowfade
    pause 1
    show ep05_mnbath10
    mad "Feel the difference?"
    mad "How it makes your heart race?"
    nana "Yeah... but..."
    nana "Isn't this wrong? We're both girls..."
    mad "I don't mind teaching you more, just if you want to."
    mad "Men made those rules to control us."
    mad "It's not like we are girlfriends or anything like that."
    mad "We are just friends that teach things to each other..."
    mad "Special, pure friends. Without men's corruption."
    show ep05_mnbath11
    nana "Ehm... I just think we shouldn't do that kind of thing..."
    nana "My [mo_full_r_low] would be upset..."
    mad "Oh? Why not?"
    mad "Do you think I'm disgusting now?"
    $ setChannelVolume("sfx", 3, 0.5, 0)
    $ playAudio(sfx_pool_splash, "sfx", 3, False, 0, 0)

    show ep05_mnbath12 at ken_burns_left_to_right
    mad "Am I the only one who wants to be special friends?"
    mad "Everyone always leaves me. Even you now..."
    mad "Maybe I should just disappear..."
    $ setChannelVolume("sfx", 4, 0.5, 0)
    $ playAudio(sfx_pool_outof, "sfx", 4, False, 0, 0)
    scene eigengrau
    pause 1
    show ep05_mnbath13
    nana "No! Please don't cry!"
    nana "Don't say things like that, Maddie!"
    mad "You hate me now..."
    mad "Everyone does. I'm too broken to love."
    nana "Never! You're my best friend!"
    nana "I could never hate you! Never!"
    show ep05_mnbath14
    mad "Do you really mean it?"
    mad "You won't abandon me like everyone else?"
    nana "Yeah!"
    nana "You saved me when I was alone. I'd never leave you."
    show ep05_mnbath15
    mad "Then let's have lots of fun!"
    mad "I'm so happy."
    mad "Just us girls. No men to ruin our purity."
    nana "Me too."
    show ep05_mnbath16 at ken_burns_right_to_left
    nana "As long as we're just friends..."
    mc_t "So this is what Isabella meant about Madison and Nanami."
    mc_t "Amber warned me about this side of Madison. Should've listened."
    # Second choice - Voyeur or Active Path
    $ show_walkthrough("ep05_2nd_mnbath2")
    menu:
        "Continue watching":
            hide screen walkthrough_screen
            $ ep05_mnvoy = True
            # VOYEUR PATH - exits after completion
            scene eigengrau with slowfade
            show ep05_mnpaths01
            mc_t "They have no idea I'm watching. I should go, but..."
            mc_t "What Madison's doing doesn't seem right. Nanami looks uncomfortable."
            mad "Relax, Nanami-chan. Your muscles are so tense."
            mad "A proper bath is about more than just getting clean."
            nana "M-Maddie... this feels different from last time..."
            show ep05_mnpaths02
            mad "What happend? Don't you wanna take a bath together? Are we not friends anymore?"
            mad "After everything I've done for you? All those times I protected you?"
            nana "Ah! No, it's not that!"
            nana "I'm just embarrassed, that's all!"
            nana "It's just... your hands are..."
            show ep05_mnpaths03
            mad "Wow, Nanami. Your body is really beautiful!"
            mad "So soft, so pure."
            mad "You don't need to be shy around me. We are just girls bathing together..."
            nana "I-I know, but my [mo_full_r_low] always said touching like this is..."
            show ep05_mnpaths04
            mad "Now, let's continue having fun!"
            mad "Your [mo_full_r_low]'s ideas are so old-fashioned. This is how modern girls bond."
            nana "Eh... That tickles a little bit... aah..."
            nana "Should we be doing this, Maddie?"
            show ep05_mnpaths05
            mad "Let's wash this area next, okay?"
            mad "Every part needs proper attention, Nanami."
            nana "That... That's... My..."
            nana "Maddie, I don't think we should—"
            show ep05_mnpaths06 with vpunch
            mad "Hmm? What's wrong? Is this place dirty too?"
            mad "Don't worry, I know exactly how to clean it properly."
            mad "Trust me, Nanami. I'd never hurt you like a man would."
            nana "Aaah... Nnngg... Mmm..."
            nana "This isn't—I've never—"
            $ setChannelVolume("sfx", 4, 0.8, 0)
            $ playAudio(sfx_madohxxx, "sfx", 4, False, 0, 0)

            show ep05_mnpaths07 at ken_burns_corner_to_corner3
            mad "Your face is so cute when you're like this."
            nana "Ehh... Aah..."
            mad "See how special our friendship is? This is what I was talking about."
            nana "I can't... I'm feeling..."
            mad "Men could never understand this connection."
            # CUM
            nana "Aaaaah!!"
            show white zorder 1.0 at ejaculation_flash
            show ep05_mnpaths08 at vpunch with flash
            mad "See? It wasn't bad at all, don't ya think?"
            mad "Friends help friends get clean..."
            mad "And now you're truly clean, inside and out."
            $ stopAudio("music", 3, 4)

            show ep05_mnpaths09 at ken_burns_right_to_left
            nana "Maddie... I feel strange..."
            mad "Shhh... It's okay."
            mc_t "She's looking this way. Did she spot me?"
            mc_t "Nanami looks completely out of it. What has Madison done to her?"
            mc_t "That smile... she's proud of herself. Of breaking Nanami."

            show ep05_mnpaths10
            mad "I just have to grab more soap from over there. You wait here, ok?"
            mad "Rest a little, Nanami. The first time is always intense."
            nana "First... time?"
            mc_t "Shit!"
            mc_t "She's coming this way. I need to move..."

            show ep05_mnpaths11
            mad "Enjoying the view, [br_full_r_low]?"
            $ setChannelVolume("music", 4, 0.4, 0)
            $ playAudio(madison_bad_theme, "music", 4, True, 4, 0)
            mad "Pathetic male voyeur."
            mc_s "Shit!"
            mc_s "What you're doing to her is wrong, Madison."

            show ep05_mnpaths12 at ken_burns_top_to_bottom
            mad "Whatever, it doesn't matter anyway."
            mad "She's mine. Only mine."
            mad "A lesson for you, dear [br_full_r_low] - while men watch, women act."
            mad "Now go take care of your... problem. Somewhere else."
            mc_t "Nanami needs help, but confronting Madison now would only make things worse."
            mad "Before I tell Nanami exactly what kind of pervert you really are."
            mc_s "Whatever... Alright, bye."

            $ stopAudio("music", 4, 2)
            $ stopAudio("amb", 3, 2)
            jump ep05_elibdown


        "Intervene":
            hide screen walkthrough_screen
            $ ep05_mnvoy = False
    # If we get here, player chose ACTIVE path
    scene eigengrau with slowfade
    show ep05_mnpaths01
    mc_t "I need to see what happens next between them..."
    mc_t "After that kiss and Madison's manipulation, this could get worse."
    mad "Feels good, right? Being like this with me."
    mad "No men watching. Just us girls connecting in our special way."
    nana "Yeah... It feels really nice."
    nana "Your hands are so gentle, Maddie..."
    mad "And this is normal, right? We don't need to do anything else."
    mad "Just pure friendship between women, the way it should be."
    nana "Yes... we are just best friends enjoying our bath."
    mad "So much better than having disgusting boys around."
    show ep05_mnpaths02
    nana "Maddie, you're hurting me."
    nana "Your grip is too tight..."
    mad "Sorry. I'll hug you gentler."
    mad "I just get excited being with someone as beautiful as you."
    mad "Someone who actually appreciates me, unlike my [fm_r_low]."
    show ep05_mnpaths03
    nana "Ah!"
    nana "M-Maddie! What are you doing?"
    nana "Your hand is..."
    mad "I'm just washing your body."
    mad "These parts need special attention. They're so perfect."
    mad "You have a woman's body now, Nanami. So different from before."
    show ep05_mnpaths04 at subtle_zoom_out
    nana "But... You just pinched..."
    nana "...my nipple."
    nana "We shouldn't be touching like this..."
    mc_t "Madison's taking advantage of her."

    show ep05_mnpaths05 with normalfade
    mad "Oh! Sorry! That wasn't on purpose! My fingers just slipped!"
    mad "Don't be shy. Your body is reacting naturally."
    nana "Ehm... Ok."
    nana "If you say it's normal..."
    mad "You're so cute, it makes me want to hear more."
    mad "The sounds you make when I touch you... so pure."
    show ep05_mnpaths06
    nana "Wait... Ah!"
    nana "Your fingers... they're... Ah!!"
    nana "Maddie, this doesn't feel like just bathing anymore..."
    mad "Trust me, Nanami. This is how women show affection."
    mad "Better than any boy could ever make you feel."
    $ stopAudio("music", 3, 4)

    show ep05_mnpaths07 at ken_burns_right_to_left
    mc_t "What she's doing to Nanami... this is wrong."
    mc_t "I should stop this, but if I suddenly appear..."
    mad "Ah, [mc_name]."
    mad "Seems like my [br_full_r_low] was peeping at us."
    mad "Did you enjoy the show, you pervert?"
    show ep05_mnpaths08 at ken_burns_bottom_to_top
    nana "[mc_name]?! Oh no..."
    nana "This isn't... I wasn't..."
    mc_s "Madison, what the hell are you doing to her?"
    mc_s "This isn't right and you know it."

    show ep05_mnpaths09
    mad "How was that, dear [br_full_r_low]?"
    mad "Did that turn you on?"
    mad "Watching two women without their permission?"
    mc_s "This isn't about me. It's about what you're doing to Nanami."
    mc_s "She's not some toy."

    show ep05_mnpaths10
    mad "[br_full_r], join us!"
    mad "Since I caught you watching, might as well participate."
    nana "Wait! What?"
    nana "[mc_name], I didn't... this isn't what I..."
    mad "Help me teach Nanami how to be a grown-up. It'll be a fun group lesson."
    mad "Or are you too much of a coward to do more than just watch?"
    $ setChannelVolume("music", 4, 0.4, 0)
    $ playAudio(madison_theme, "music", 4, True, 4, 0)

    show ep05_mnpaths11 at subtle_zoom_out with normalfade
    mad "Watch how I touch her... learn from this."
    mc_s "Nanami doesn't want this, Madison."
    mc_s "Look at her face."

    scene eigengrau
    pause 1
    show ep05_mnpaths12 with vpunch
    nana "Ah!"
    nana "Stop... Please..."
    nana "[mc_name] is watching us... this is embarrassing..."
    mad "Why? Does it feel bad?"
    mad "Or are you just ashamed to let my [br_full_r_low] see how much you enjoy it?"
    nana "Ahhh!"
    mad "Men watch women all the time. Let him see what he's missing."
    show ep05_mnpaths13 at ken_burns_top_to_bottom
    nana "Ahhhhh!"
    nana "I-It doesn't feel bad, it just...."
    nana "It just feels weird."
    nana "I've never felt this way before..."
    show ep05_mnpaths14 with normalfade
    mad "Your turn, [br_full_r_low]."
    mad "Show Nanami what men really do to women."
    mad "Go on, don't be shy."
    mad "Prove me right about what disgusting creatures you all are."
# Third choice - Accept or Deny
    $ show_walkthrough("ep05_2nd_mnbath3")
    menu:
        "Accept her challenge":
            hide screen walkthrough_screen
            $ ep05_mntouch = True
            # ACCEPT path
            mc_t "She's challenging me... Does Madison always do this? Pushing boundaries to see who breaks first."
            mc_t "Maybe playing along will expose what she's really doing to Nanami."

            show ep05_mnpaths15 with hpunch
            # Update variables
            $ rm.update("nanami", "trust", -3)
            $ check_levels("nanami", "trust", -3)
            $ ss.add("nanami", "strike")
            if ss.get("nanami", "strike") == 1:
                $ show_custom_notification("strike1")
            elif ss.get("nanami", "strike") == 2:
                $ show_custom_notification("strike2")
            elif ss.get("nanami", "strike") >= 3:
                $ show_custom_notification("strike3")

            mc_s "Fine, I'll show you how men touch women."
            nana "Ah! [mc_name]! That hurts! You're too rough!"
            nana "Your hands are squeezing too hard... please..."
            mad "See how he grabs? No finesse. Just taking what he wants."
            mad "Men always hurt women. They can't help themselves."
            show ep05_mnpaths16
            mc_s "I'm sorry Nanami, but I can't resist."
            mc_s "Your lips look so soft. I need to taste them."
            mc_s "Just one kiss. Let me show you what it feels like."
            nana "Wait!!"
            nana "Please don't... not like this..."
            show ep05_mnpaths17 at ken_burns_bottom_to_top with vpunch
            mad "Now now, [br_full_r_low]."
            mad "We can't have that. No kissing."
            mad "Did you really think I'd let you kiss her? After I just kissed her myself?"
            mad "That's for me to give, not a brute like you."
            show ep05_mnpaths18 with normalfade
            mad "See? That's what men do, when they're alone with girls like you."
            mad "They hurt you, then try to force themselves on you when you're vulnerable."
            mad "That's what they're after. You understand now?"
            nana "[mc_name]... I trusted you..."
            show ep05_mnpaths19
            mc_s "What the fuck?! Are you just toying with me?!"
            mc_s "You set me up! You wanted me to do this!"
            mad "No, no... don't get mad."
            mad "Your true nature revealed itself. I merely provided the opportunity."
            mad "This is what all men do when given the chance."
            show ep05_mnpaths20
            mad "I was just showing how boys act around girls like Nanami."
            mad "They pretend to be gentle, then their hands turn to claws."
            mad "And that includes you too, [mc_name]."
            mad "Did you see how rough he was, Nanami? How he tried to take what wasn't offered?"
            mad "Now, be a good boy, and leave the bath, will you?"
            mc_t "Fuck! She played me perfectly..."

            show ep05_mnpaths21 at ken_burns_left_to_right
            mc_t "I became exactly what she wanted... a monster."
            mc_t "Nanami will never trust me now. I've proven Madison right."
            mad "There, there, Nanami. Your breasts must hurt from his rough handling."
            mad "Let me soothe them. Women know how to touch other women properly."
            nana "You were right about him, Maddie... I should have listened..."
            $ ep05_ach_nanastrike = True
        "Refuse to participate":
            hide screen walkthrough_screen
            $ ep05_mntouch = False
            # DENY path
            mc_t "I won't be part of Madison's game."
            mc_t "She wants me to prove her point about men... Not happening."

            show ep05_mnpaths15
            mc_s "Stop this, Madison."
            mc_s "Using Nanami to get at me? That's low."
            mad "Excuse me?"
            $ stopAudio("music", 4, 2)
            mad "Who do you think you are?"
            # Update variables
            $ rm.update("nanami", "trust", 3)
            $ check_levels("nanami", "trust", 3)

            show ep05_mnpaths16
            mc_s "I saw what you did. The way you pressured her into this."
            mad "Mind your own business, [br_full_r_low]."
            mad "You wouldn't understand the connection between women."
            $ setChannelVolume("music", 5, 0.4, 0)
            $ playAudio(mc_nanami_theme, "music", 5, True, 4, 0)

            show ep05_mnpaths17
            mc_s "Nanami, you don't have to do anything you don't want."
            mc_s "Don't let her pressure you. This isn't what friendship looks like."
            mc_s "You deserve better than being used in her games."
            mad "Shut up!"
            mad "Don't listen to him, Nanami! He's trying to corrupt you!"
            nana "I... I just wanted to take a bath..."
            show ep05_mnpaths18 with hpunch
            nana "I--I think I'd better head out..."
            mad "No!! Where are you going?!"
            nana "I... should get dressed..."
            mad "After everything I've done for you? All the bullies I protected you from?"
            nana "Please let go of my arm, Maddie... you're hurting me..."
            show ep05_mnpaths19 at ken_burns_right_to_left
            mad "It's all your fault! You!! Get out, NOW!!"
            mad "Leave us alone before you ruin everything else!"
            mad "This is what men do, Nanami. They destroy everything beautiful."
            nana "Wait... I'll go too."
            nana "I don't... I don't think I should stay..."
            show ep05_mnpaths20
            mad "You're choosing him?"
            mad "After everything I've taught you about men?"
            mc_s "Nanami, you don't need me or Madison to make your own choices."
            mc_s "Trust your instincts. You know what feels right and what doesn't."
            nana "I... I think I need to stand up for myself..."
            show ep05_mnpaths21 at ken_burns_left_to_right with normalfade
            mc_t "I should go. This is between them now."
            nana "Maddie, please stop. This isn't what I want."
            nana "I don't like being used to prove your points about men."
            mad "You ungrateful little—after all I've done for you?"
            mad "He's poisoned your mind already. Just like all men do."
    $ stopAudio("amb", 3, 2)
    $ stopAllSubchannels("music", 2.0)
    jump ep05_elibdown




label ep05_elibdown:
    scene eigengrau with slowfade
    pause 1.0
    $ renpy.free_memory()
    pause 1.0
    show ep05_elibreak01 at ken_burns_left_to_right
    $ setChannelVolume("amb", 4, 0.5, 0)
    $ playAudio(sfx_earlymor, "amb", 4, True, 2, 0)
    $ setChannelVolume("sfx", 1, 1, 0)
    $ playAudio(sfx_pills, "sfx", 1, False, 0, 0)
    eli "Pills for breakfast... lunch... dinner... my whole fucking life."
    eli "Michael doesn't even hide what they're for anymore. 'Take these, Elizabeth. You're getting hysterical again.'"
    eli "Just... one more. Just to make the mirror less cruel."
    eli "These aren't even working like they used to..."
    $ setChannelVolume("music", 1, 0.2, 0)
    $ playAudio(chaos_theme, "music", 1, True, 4, 0)

    show ep05_elibreak02 with flash
    eli "White lingerie... so fucking ironic. The virgin bride I never was."
    eli "Twenty years as decoration in this house. Twenty years as... the ornament on his shelf."
    eli "Maybe... maybe if I try to look like I used to... maybe then..."
    eli "Who am I kidding? He never looked at me. Just through me."
    show ep05_elibreak03
    eli "[mo_full_r] always said... always said... what was it? Beauty is... is currency."
    eli "My only value... gone."
    eli "Bankrupt. Fucking worthless now."
    eli "Can't even remember... what I'm supposed to be thinking about..."
    show ep05_elibreak04 with flash
    eli "Orange... like sunset in Milan. Sunset on my worth."
    eli "They called me The European Rose... now I'm just... just dried petals."
    eli "The perfect color... Orange to match his ties at medical galas."
    eli "Why can't I... why can't I make this body beautiful again?"
    $ setChannelVolume("music", 1, 0, 0.5)

    show ep05_elibreak05 at subtle_zoom_out with slowflash
    eli "Naked... naked is easier. No more... pretending."
    eli "Just meat on bones... just a body past its expiration date."
    eli "All those eyes staring at me..."
    eli "Like I'm already a corpse."
    $ setChannelVolume("music", 1, 0.3, 0.5)

    show ep05_elibreak06 with flash
    eli "Pink... like my first Vogue cover. Fucking lifetime ago."
    eli "These tits... these saggy, stretch-marked tits... used to make headlines."
    eli "Now they're just... evidence. Evidence of decay."
    eli "Maybe the wine will make me see what he saw. What everyone saw. Before..."
    show ep05_elibreak07 at ken_burns_bottom_to_top with flash
    eli "Red... always wore red in Milan. Red like... like..."
    eli "Like all that wine in my blood. Only thing real about me now."
    eli "Three kids... three fucking kids tore this body apart. For what? His image?"
    eli "Perfect surgeon. Perfect wife. Perfect... fucking... lie."
    show ep05_elibreak08 at ken_burns_right_to_left with flash
    eli "Black... for mourning. Mourning Bianca from Milan."
    eli "S'not even my real name... Elizabeth. Just... sounded better for this image."
    eli "Can't even... can't even remember what I wanted. Before him."
    eli "Just a body to breed his... his perfect little dolls. His props."
    $ setChannelVolume("music", 1, 0, 0.5)

    show ep05_elibreak09 at focus_shift with slowflash
    eli "Wine and pills... breakfast of champions. Hah."
    eli "Animal print... like I'm still wild. Still dangerous."
    eli "Just a caged animal now. In his... in his perfect fucking museum."
    eli "Why'd I even try these on? S'not like he's gonna... gonna notice."
    $ setChannelVolume("sfx", 2, 1, 0)
    $ playAudio(sfx_punch_floor, "sfx", 2, False, 0, 0)
    $ setChannelVolume("music", 1, 0.4, 0.5)

    show ep05_elibreak10 with vpunch
    eli_y "FUUUCK! WHY'S NOTHIN' WORK?!"
    eli "Wore this for... for wha? F'r who? Fuckin' nobody."
    eli "Time... time stole m'face. Stole everything..."
    eli "Jus'... jus' wanna feel pretty again. Jus'... once..."
    $ setChannelVolume("music", 1, 0, 0.5)

    show ep05_elibreak11 with slowfade
    eli "All bullshit... all...all these clothes. Bullshit."
    eli "Off... take it all off... all lies... all..."
    show ep05_elibreak12 with flash
    eli "Who's... who's tha' bitch? In there?"
    eli "Not... not me. Can't be. So old. So ugly."
    eli "Where'd I... where'd Bianca go? Where...?"
    eli "Mirror... fuckin' mirror lies."
    $ setChannelVolume("sfx", 3, 0.5, 0)
    $ playAudio(sfx_glassbreak, "sfx", 3, False, 0, 0)
    $ setChannelVolume("music", 1, 0.5, 0.5)

    show ep05_elibreak13 at action_sequence with flash
    eli_y "BITCH! OLD BITCH!"
    eli_y "DIE! DIE! DIE!"
    eli_y "HATE YOU! HATE THIS FACE!"
    show ep05_elibreak14 at ken_burns_top_to_bottom
    eli "Hurts... good. Pain's... real."
    eli "Not like... not like pills. Pills numb..."
    eli "Can't fix... can't fix old. Can't..."
    eli "Fallin'... fallin' apart. Like... like my skin."
    show ep05_elibreak15
    eli "Used me up... used all of me."
    eli "My youth... my beauty. My... my..."
    eli "Gave everythin'... got nothin'."
    eli "Empty... so empty now."
    $ setChannelVolume("sfx", 2, 0.5, 0)
    $ playAudio(sfx_punch_floor, "sfx", 2, False, 0, 0)
    $ setChannelVolume("sfx", 4, 1, 0)
    $ playAudio(sfx_punch_glass, "sfx", 4, False, 0, 0)

    show ep05_elibreak16
    eli_y "NOBODY SEES ME!"
    eli_y "INVISIBLE! OLD!"
    eli_y "CAN'T BREATHE! CAN'T..."
    eli_y "NOT FAIR! NOT... NOT..."
    show ep05_elibreak17 at ken_burns_right_to_left
    eli "Wanna... wanna tear it off."
    eli "This skin... this prison."
    show ep05_elibreak18
    show vignette at pov_die
    eli "Stupid... stupid girl. Stupid Bianca."
    eli "Trapped... trapped inside old body."
    eli "Young inside... old outside."
    eli "These pills make... make the mirror lie."
    show ep05_elibreak19 at focus_pulse, dizzyness with slowfade
    eli "I... I feel... feel alive now. Awake."
    eli "Pain makes... makes everything clear."
    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_bed_laying, "sfx", 5, False, 0, 0)

    show ep05_elibreak20 at focus_pulse, dizzyness with vpunch
    eli "Need... need a new skin. New face."
    eli "Paris... Paris will take me back."
    eli "If young again... if beautiful..."
    eli "Need... need to fix this shell."
    eli "One more chance... one last... last chance."
    eli "Not... not over yet. Not done..."
    $ stopAllSubchannels("music", 2.0)
    $ setChannelVolume("amb", 4, 0, 1.0)
    ## save notification
    if htl_episodes == 5.2:
        $ show_custom_notification("save_tip")
    scene eigengrau with slowfade
    pause 1
    show ep05_elibreak21 with line80
    $ setChannelVolume("amb", 5, 0.5, 0)
    $ playAudio(sfx_earlypast, "amb", 5, True, 2, 0)
    amb "What the actual fuck was that?"
    amb "Sounded like someone's murdering a glass factory in there."
    mc_t "What was that sound? Came from upstairs."
    mc_t "That crash... has to be from..."

    $ setChannelVolume("sfx", 5, 1, 0)
    $ playAudio(sfx_stairs_up, "sfx", 5, False, 0, 0)

    show ep05_elibreak22 at subtle_zoom_out
    mc_t "That scream. [mo_r]'s room."
    mc_t "Shit."

    show ep05_elibreak23 with hpunch
    amb "Whoa, where's the fire, detective?"
    amb "Going to rescue the queen of melodrama again?"
    mc_s "I heard glass breaking. Sounded bad."
    amb "Welcome home. [mo_r]'s famous for her dramatic exits."
    amb "She probably just dropped a wine bottle. Happens like twice a week."
    mc_s "Yeah... yeah... sure thing. Are you coming or not?"
    amb "Go where?"
    mc_s "Don't you want to know if [mo_r] is okay?"
    amb "Okay... you'll see there's nothing wrong with her, she's just being dramatic."
    $ stopAudio("amb", 5, 2)
    $ setChannelVolume("sfx", 6, 1, 0)
    $ playAudio(sfx_dooropen, "sfx", 6, False, 0, 0)
    scene eigengrau with slowfade
    pause 1
    $ setChannelVolume("sfx", 2, 7, 0)
    $ playAudio(sfx_doorclose, "sfx", 7, False, 0, 0)

    show ep05_elibreak24 with slowfade
    $ setChannelVolume("amb", 4, 0.5, 1.0)
    amb "Oh my god..."
    amb "Is that... blood?"
    mc_s "[mo_r]..."
    mc_t "There's glass everywhere... Her body... this is bad."
    mc_s "We need to call emergency services. Now!"
    amb "I can't... I can't look..."
    mc_s "119. Call 119, Amber."
    amb "[mo_r]... what did you do?"
    #-- End Update
    if htl_episodes == 5.2:
        $ stopAllAudio(3.0)
        scene eigengrau with rose
        pause 2.0
        $ resetAllVolumes()
        return


    else:
        jump ep05_elisuicide


