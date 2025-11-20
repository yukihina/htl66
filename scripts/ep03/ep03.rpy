



label ep03_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    $ renpy.block_rollback()
    jump ep03_isatalk


## -- INTRO SCENE HOME




label ep03_isatalk:
    call showNoise(0.1, 0.15, transition=dissolve)
    show ep03_backtohome01 with slowfade
    $ config.rollback_enabled = True
    show screen stats_button
    show screen walkthrough_icon
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    isa "[da_r]!"
    mc_s "W-What happened?"
    isa "..."
    isa "What's wrong, [da_r]?"
    mc_s "It's the--"
    isa "The meds, right? Well... I can see that..."
    $ playAudio(sfx_bedmove4, "sfx", 1, False, 0, 0)

    show ep03_backtohome02
    mc_s "Yeah..."
    isa "Aww, you look so tired. Just rest here, okay [da_r]?"
    mc_s "Wait! Why were you here in the first place?"
    isa "Oh.. it's just-- Nevermind. You need to rest, [da_r]. We can talk later."
    mc_s "No, tell me. What did you want to say, Isabella?"
    isa "I just wanted to show you this..."
    mc_s "What?"

    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(isabella_sad, "music", 1, True, 0, 0)

    show ep03_backtohome03 at camera_zoom
    isa "This..."
    isa "This was before she abandoned us."
    mc_s "Oh... Antonella... Yeah, I remember seeing that picture somewhere..."

    show ep03_backtohome04
    isa "I saw it when I was going through some things in my closet yesterday."
    isa "And... I don't know why, but seeing her... made me sad..."
    isa "I just thought you needed to see it too..."
    isa "Sorry."
    show ep03_backtohome05
    mc_s "Hey... Don't apologize, it's alright."
    mc_s "But you shouldn't say she abandoned us, OK? We don't know what happened..."
    isa "I... know [da_r]... it's just--"
    show ep03_backtohome06
    isa "I still don't know what did I do wrong... Maybe she didn't love me?"
    mc_s "No... hey... Hey, I'm sure she loved you, and... and I'm sure she still does."
    mc_s "If I ever saw her, I would tell her not to leave you again."
    mc_s "Because you're the most precious thing in my life and... I love you."

    show ep03_backtohome07
    isa "Then why did she leave us?!"
    mc_s "I... I don't know."
    mc_s "But we can't change what happened and thinking about it isn't gonna help."
    mc_s "Instead, we can just concentrate on the good stuff, like... hmm..."
    isa "See? You don't know either..."
    mc_s "No. No, I really don't..."
    mc_s "I'm sorry, I wish I knew why she left, and why she never came back... but we can't change that either."
    mc_s "But I am here for you, always."
    isa "Yeah... I know."
    $ playAudio(sfx_drop_ontable, "sfx", 2, False, 0, 0)

    show ep03_backtohome08
    mc_t "Somehow, saying this makes me feel awful."

    show ep03_backtohome09
    isa "Sorry if I disturbed you..."
    mc_s "You didn't."
    mc_s "Well, how can I not smile when my little girl is worried about me, huh?"
    mc_s "Plus, you're always such a good girl and never ask for anything."
    isa "I do ask for stuff, it's just that you don't listen to me."
    mc_s "I... alright... I admit to that, but still..."
    isa "*Sigh*"
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.4)
    $ playAudio(sfx_bed_sitdown, "sfx", 3, False, 0, 0)

    show ep03_backtohome10 with dissolve
    isa "Sorry [da_r]... I didn't mean to argue. You look stressed already and I got angry for no reason..."
    mc_s "Don't worry about it. "

    show ep03_backtohome14
    mc_t "She is acting strange."
    isa "I love you... you know? More than anything."
    mc_t "I know, and I love you too."

    show ep03_backtohome11
    isa "Can I get a hug?"
    $ show_walkthrough("ep03_isahug_menu")
    menu:
        mc_t "Should I hug her? Maybe I shouldn't..."
        "Comfort Isabella with a hug":
            hide screen walkthrough_screen
            $ ep03_isahug = True
            $ rm.update("isabella", "trust", 5)
            $ check_levels("isabella", "trust", 5)
            isa "You're too shy, [da_r]. If you won't hug me, I'll hug you."
            mc_s "U-um, it's not that, I-- Well... Okay, you can."

            jump ep03_isatalk_hug


        "Give Isabella a reassuring pat on the head":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", 1)
            $ check_levels("isabella", "trust", 1)
            isa "Hmmm...?"
            jump ep03_isatalk_nohug




label ep03_isatalk_hug:
    show ep03_backtohome12 with hpunch
    isa "I love you so much, [da_r]!"
    mc_s "Me too."

    show ep03_backtohome16
    isa "It's just hard sometimes, not knowing why she left. I'm sorry..."
    mc_s "Isabella, don't apologize."
    isa "Right... but [da_r]..."
    mc_s "Yeah?"
    isa "Do you think we'll ever find out? What happened to [mo_r]?"
    mc_s "I don't know, but whatever it is, we'll face it together. Okay?"

    show ep03_backtohome18
    isa "I'm glad I have you, [da_r]. You're my hero!"
    mc_s "And I'm glad I have you. My lovely little princess."

    jump ep03_isatalk_end




label ep03_isatalk_nohug:
    show ep03_backtohome13 with vpunch
    isa "I just wanted a hug... but it's okay. Thanks for stroking my head."
    mc_s "I'm sorry, Isabella. I'm just... tired, really tired."

    show ep03_backtohome17
    isa "I see... It's just... you know... it's been so long since I held you close... It makes me miss you."
    mc_s "I know. And I'm sorry. I didn't realize it was such a big deal."
    mc_s "You're not mad at me, are you?"

    show ep03_backtohome16
    isa "I... no. Don't worry about it."
    jump ep03_isatalk_end




label ep03_isatalk_end:
    show ep03_backtohome19
    isa "[da_r], promise me one thing."
    mc_s "Anything, what is it?"
    isa "Promise me that no matter what happens, you'll always be honest with me."
    isa "That no matter what, you will always tell me the truth. Just one promise..."
    mc_s "I promise... But why are you asking me something like that, anyway?"

    show ep03_backtohome20
    isa "Just a hunch, [da_r]."
    isa "Alright. Goodnight... Dream of something fun."
    isa "I hope you recover soon. And... [da_r]?"
    mc_s "Hmm?"
    isa "Will you love me no matter what?"
    mc_s "Yeah, of course. Why are you even asking me that?"
    isa "Promise?"
    mc_s "I promise, Isabella."

    show ep03_backtohome21
    isa "...okay. G-good night, [da_r]."
    mc_s "Good night, Isabella."
    mc_t "What a weird question... This has to be Antonella's genes in action."
    mc_t "Her emotions are difficult to read, even for me..."

    $ stopAllSubchannels(channel="music", fadeout=2.5)
    $ stopAllSubchannels(channel="amb", fadeout=2)
    $ stopAllSubchannels(channel="sfx", fadeout=2)
    jump ep03_antodream




label ep03_antodream:
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)

    show ep03_antodream01 with slowfade
    mc_t "Antonella... sometimes I wonder if you ever think of me, Isabella, or... or all of us."
    mc_t "I miss the way you used to smile, the way you made me feel."
    mc_t "Looking at this photo, it feels like a lifetime ago. There is so much I wish I had said, or done differently."
    mc_t "I'm not even sure what I would do if I ever saw you again."
    mc_t "But now, all that's left is this... longing, for the life we could have had."

    show ep03_antodream02
    mc_t "Isabella... she has your eyes. She's growing up so fast. And... I hardly know anything about her..."

    show screen mcpov_dying

    mc_t "I wish I could hate you, but my heart won't let me. All I know is... that I miss you, and I always will."
    mc_t "Even if you never loved me, I always loved you."
    #begins transition to dream
    hide screen mcpov_dying
    $ stopAudio(channel="amb", subchannel=1, fadeout=1)
    scene eigengrau with clouds_inverse
    pause 1
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.7)
    $ playAudio(sfx_windyprairie, "amb", 2, True, 1.5, 0)

    show ep03_antodream03 with slowfade
    mc_t "Where... where am I? Wasn't I in my room?"
    mc_t "This place... it feels familiar. Where... oh."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.8)
    $ playAudio(antonella_love, "music", 1, True, 1.5, 0)

    show ep03_antodream04
    mc_t "Is that... Antonella? What's she doing here...?"

    show ep03_antodream05
    anto "Hey, you! What are you doing here? "
    mc_s "H-Huh?! Antonella... is it really you?"

    show ep03_antodream06
    anto "Of course, it's me. Why do you look so surprised? Are you okay?"
    mc_s "I... I thought I had lost you. "
    anto "Why would you think that? I've always been here, with you."
    show ep03_antodream07
    anto "I'm not going anywhere, you dummy!"
    mc_s "You disappeared, Antonella. It's been years. I've searched everywhere for you, tried so hard, I--"
    anto "Look, I'm standing right in front of you. Do I feel real enough?"
    mc_t "I want to believe it, but... it's just too good to be true."
    #roll
    show ep03_antodream08 at slow_pan with vpunch
    mc_s "I've missed you so much... please tell me you're real, please..."
    anto "What do you mean, years? What happened to you? Are you feeling okay?"
    mc_s "I... I've been searching for you, all this time. Isabella and I... we needed you."
    #end roll
    show ep03_antodream09
    anto "Huh? Who is Isabella? I... I don't understand. This is all so sudden. Can we slow down, please?"
    mc_s "What? Antonella... what are you saying? She's our [dau_r_low], ours!"

    show ep03_antodream10
    anto "Don't be silly, I've never been pregnant."
    mc_s "Don't lie to me! This isn't funny, Antonella!"

    show ep03_antodream11
    anto "Look, you're here now. We can be happy again, can't we? Just you and me?"
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=1, volume=0, fade_duration=1)
    $ playAudio(sfx_glitch, "sfx", 1, True, 1, 0)

    show ep03_antodream11 at animated_glitch
    mc_s "...!"
    anto "Hey, everything can be like it was before. I'm here, and I'm happy. Won't you be happy with me, just like before?"
    mc_s "This isn't right. Something's off, but I don't know what..."

    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.8, fade_duration=1)

    show ep03_antodream12 with vpunch
    anto "If there's something you need to do, you should get to it. Time to go."
    mc_s "No, wait! I need you to know..."

    show ep03_antodream13
    mc_s "I never stopped loving you. Even now, it's always you... even... even if you aren't real."
    anto "I've already told you, silly, I've always been here. You can stay with me, and be happy."
    $ stopAudio(channel="music", subchannel=1, fadeout=2.5)

    show ep03_antodream14 with hpunch
    anto "We'll be together forever, in a world made only for us. Just you, and me. Like it should be."
    anto "Now... wake up."
    #end dream
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    jump ep03_madtalk




label ep03_madtalk:
    scene eigengrau with clouds
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 1, True, 1.5, 0)

    show ep03_ambertalk01 with slowfade
    mc_t "Fuck! Why can't I just let this go? She's gone. She's not coming back..."
    mc_t "Every time I close my eyes, it's like I'm haunted by her memory."

    show ep03_ambertalk02
    mc_t "I can't keep doing this. I need to clear my head. Maybe some fresh air will do me good."
    mc_t "Or perhaps some TV would take my mind off things."
    mc_t "But first, I need to put this damn photo away. It's driving me insane."

    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)

    show ep03_madtalk01 with circlewipe
    mc_t "Ha... I can't help but feel a little better. This feels like home."
    mc_t "Watching TV at night, alone... just like before."
    mc_t "I just need some booze and everything would be perfect. It's been so long since I had a good drink."

    show ep03_madtalk02
    show screen mcpov_dying

    mc_t "Getting sleepy in front of the TV... this brings back memories."

    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    hide screen mcpov_dying
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=3)
    $ playAudio(sfx_bed_sitdown, "sfx", 1, False, 1, 0)

    show ep03_madtalk03 with slowfade
    mc_t "Uh... what the-?"
    mc_t "What? Madison...?"
    mc_t "I haven't seen her in so long. But now, here she is."
    mc_t "Wait, when did she come in?"
    mc_t "And since when did Madison start wearing such revealing clothing? It's like she's practically naked."

    $ setChannelVolume(channel="music", subchannel=2, volume=0.6)
    $ playAudio(madison_theme, "music", 2, True, 2.5, 0)

    show ep03_madtalk04
    mc_t "How has her body even changed so much since I last saw her? I don't remember her being so... developed..."
    mc_t "...Fuck. I know she's my [si_full_r_low], but damn, she's hot. No wonder she's following [mo_r]'s career."
    mc_t "She looks so different from Amber. So petite and delicate, yet--"

    $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)

    show ep03_madtalk05 with hpunch
    $ rm.set_knows("madison", True)
    mad "Why are you looking at me like that? Do I have something on my face?"
    mc_s "No...no, sorry. It's just that-it's been a while. I didn't expect you to show up here dressed like that."
    mc_t "There is literally nothing covering her body."
    mc_t "What was [mo_r] thinking, letting her walk around nearly nude?"
    mad "Oh. Right. Sorry I changed the channel."
    mc_s "It's fine. How have you been?"

    show ep03_madtalk06
    mad "Fine, I guess."
    mc_s "Just fine?"
    mad "Yeah, sure. Do you expect me to tell you any more than that?"
    mc_s "I guess not. I'm glad you're well."
    mad "Do you always talk in cliches?"
    show ep03_madtalk07 at camera_zoom
    mc_s "It's what people say to each other, you know, small talk?"
    mad "Yeah, whatever. Are you just gonna watch TV all night?"
    mc_s "Yes? I mean, no. I was going to go to sleep, actually."
    mad "Here? How could you sleep here when there's a perfectly good bed in your room?"
    mc_s "The couch is quite comfortable, you know."

    show ep03_madtalk08
    mc_t "I can't help but feel drawn to her, even though I know it's wrong. What is happening to me?"
    mad "Do you think I'm pretty?"
    mc_s "Huh?"
    mad "Simple question. It shouldn't be that hard to answer."
    $ show_walkthrough("ep03_maddie_menu")
    menu:
        mc_t "What should I say? She's my [si_full_r_low], but, I just can't tear my eyes away from her body."
        "Admit that Madison is attractive":
            hide screen walkthrough_screen
            $ ep03_madtalk = True
            $ rm.update("madison", "trust", 10)
            $ check_levels("madison", "trust", 10)

            mc_s "Yeah, you're beautiful, Madison. You take after [mo_r]."
            mad "So,  would you fuck me if I weren't your [si_full_r_low]?"
            mc_s "What?!"
            mc_t "This is getting too weird. I need to get out of here."

            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)

            show ep03_madtalk09 with vpunch
            mad "No need to freak out. Just a question."
            mc_s "I-I-I mean, why are you asking me something like that?"
            mad "Curiosity. That's all."
            mc_s "So... yes, I would fuck you."
            mad "I knew it! Men are so predictable."
            mc_t "Look at her! She looks so innocent, but she's asking things like that without shame, like it's no big deal."
            mc_t "And the fact she looks so comfortable wearing only her underwear... it's driving me crazy."
            mc_s "Look, we shouldn't be talking about this, okay? Let's just forget about it."
            mad "Aw, man. You're no fun."
            show ep03_madtalk10
            mad "Alright. You can go to sleep, then."
            mc_s "Yeah. Yeah, I'm gonna go to sleep. Good night, Madison."
            mad "Night."
        "Deny finding Madison attractive":
            hide screen walkthrough_screen

            mc_s "Why are you asking me that? Where is this coming from?"
            mad "Just answer the question. Do you think I'm pretty or not?"
            mc_s "If I'm being honest... no. You're my [si_full_r_low], so obviously I wouldn't find you attractive."
            mad "I'm not asking you about that, I'm asking if you find me attractive."
            mc_t "This is getting too weird. I need to get out of here."

            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)

            show ep03_madtalk11 with vpunch
            mad "Ugh... Why are you making this so hard?"
            mc_s "Hard? Making what hard?"
            mad "Look, you're a man, right?"
            mc_s "Y-yeah. So?"
            mad "Then why are you acting like this? Normally, men can't take their eyes off me."
            mad "And you, you're no different. I can see it in the way you look at me."
            mc_s "I'm not sure what you're getting at."
            mad "Really? Look at me. Don't act like you haven't been staring at me this whole time."
            mad "It's not that hard to understand."
            show ep03_madtalk12
            mad "Whatever. I thought I could talk to you, but I guess I was wrong. This is pointless. "
            mad "You're all the same anyway."
            mc_s "Same, as in?"
            mad "Men. They're all the same. Thinking with their dicks and not their brains. Goodnight, [mc_name]."
            mc_s "Okay... goodnight."

            $ unlock_memory("m_ep03_tv")

    mc_t "Seriously, what was that about?"

    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_reunion




label ep03_reunion:
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)

    show ep03_ambertalk03 with slowfade
    mc_t "It's been a while since I last saw her, and the first thing she does is ask if I find her attractive."
    mc_t "It's almost like she expects me to."
    mc_t "Well, I'm not gonna think about that. Let's try to get some sleep."
    mc_t "What happened reminds me of Amber and all the trouble she used to give me years ago with her daily harassment."

    show ep03_ambertalk04
    mc_t "It's weird to think about Amber doing the same thing. She always tried to catch me by surprise."
    mc_t "That's how she was."
    amb "Hi [mc_name]. Remember me?"
    show ep03_ambertalk04 with hpunch
    mc_t "Uh oh..."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.7)
    $ playAudio(amber_theme, "music", 1, True, 2.5, 0)

    show ep03_ambertalk05 with dissolve
    amb "Sorry for not giving you a heads-up. I saw you were busy talking with Madison."
    mc_s "..."

    show ep03_ambertalk06
    $ rm.set_knows("amber", True)
    amb "Did you like her outfit? She always tries to seduce someone."
    mc_s "Seduce? Is that what she was trying to do? Because I don't-"
    amb "That's what she does. She likes to tease men and make them want her, so she can control them."
    amb "But that's not why I'm here... I have something else in mind."
    show ep03_ambertalk07
    amb "So, did you think about me, [mc_name]? Have you missed me?"
    amb "Or have you found someone else to replace me?"
    mc_s "Please, don't tell me we're back to that again."
    amb "It's just... I want to know where we stand."
    mc_s "Umm, Amber, maybe we can have this conversation another day..."
    amb "Alright... alright. It was a joke, okay? Just lighten up."
    amb "Okay, look. What I really wanted to talk about was what happened before... years ago."
    amb "You know what I'm talking about, [mc_name]."
    mc_s "Uh, what?"

    show ep03_ambertalk08 with slowfade
    amb "Just hear me out for a sec, okay?"
    mc_s "Um, I'd rather not-"
    if ep01_amblove:
        amb "Just listen..."
        amb "Remember the time you told me you had feelings for me? That you were in love with me?"
        amb "That I was the one who made you feel that way?"
        mc_s "That's not exactly what I said, but-"
        amb "I... I always felt like I had a special place in your heart. That maybe one day we could... you know, be together."
        amb "But then you said that you were in love with... Antonella instead."
    else:
        amb "Just listen..."
        amb "Before, when we were young, I tried so hard to catch your attention. I didn't know how to get you to notice me."
        mc_s "You weren't subtle."
        amb "I tried, though..."
        amb "I'd follow you around, flirt with you, do anything to make you look at me."
        amb "But you were always so focused on other stuff."
        if ep01_lieamber:
            amb "Like your lie about Antonella."
        else:
            amb "Like Antonella."
    mc_s "Wow, we're back to that, huh?"
    amb "Sorry, it's just... I had a hard time seeing you two together."
    amb "You two were so close, and I couldn't take that jealousy eating me up inside."
    show ep03_ambertalk09
    amb "But now, look where we are. We're adults now, and you're single."
    amb "So, maybe you can finally answer some questions that have plagued me for years."
    mc_s "Questions? What kind of questions could you possibly have?"
    amb "Oh, you know..."
    $ show_walkthrough("ep03_ambertits_menu")
    menu:
        "Focus on Amber's breasts":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            $ ep03_ambertits = True

            show ep03_ambertalk10 at zoom_in with dissolve
            mc_t "I can't help but notice how big her breasts have gotten over the years."
            mc_t "She wasn't nearly this busty as a teen, and I doubt her cleavage has always been so enticing."
            amb "Enjoying the view, [mc_name]?"
            mc_s "No... no, of course not! I-I was just distracted by your-your..."
        "Listen to what Amber is saying":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)
            amb "Questions... like... Like..."
            amb "I'll figure something out later."
            mc_s "You don't have questions, do you?"
            amb "No, I don't."
            amb "I mean right now, but I had something really good planned, you know? But then, you had to interrupt me."
            mc_s "Sorry for ruining your great plan."
            amb "Oh, I remember! I had a question for you, you know. So, answer me, [mc_name]--"
            mc_s "What?"

    show ep03_ambertalk11
    if ep03_ambertits:
        amb "My what?"
        mc_s "Your tattoos, Amber. Those tattoos. Yes, that's all it was."
        amb "You like my tattoos? Hmm, I didn't know you were into ink on a woman's body."
        mc_s "Eh..."
    else:
        amb "Stop interrupting me already!"
    amb "Anyway, as I was saying... I wanted to know..."
    mc_s "Yes? What do you wanna know, Amber?"

    show ep03_ambertalk12
    amb "Listen, this is gonna sound weird, but... I wanna have a serious conversation with you."
    amb "So it's not gonna be as before, like when we were young. It's gonna be different this time."
    amb "Can you handle that?"
    mc_s "I'm not sure I follow."

    show ep03_ambertalk13
    amb "I guess I'll just ask then..."
    if ep01_amblove:
        amb "[mc_name], did you ever love me? Even a little bit? Or were you just... lying?"
        mc_s "No, I wasn't lying. I did love you. But it wasn't that simple."
        mc_s "Antonella and I... we were together, and I just couldn't choose between you two."
        amb "You did, didn't you? You chose her over me..."
        amb "Was I not enough for you, [mc_name]? Was I just not good enough?"
        amb "Was I not pretty enough, or sexy enough, or just... not her? God, it hurts so much..."
        mc_s "Amber, look. What I did was wrong, but I can't change the past. And neither can you."
        mc_s "So, can't we just move on from this?"
    else:
        amb "When I was a teen, you never looked at me the way I wanted you to look at me."
        amb "You treated me like a child, like you didn't think of me as anything more than your little [si_full_r_low]."
        amb "But now, now we're different, and things are gonna be different..."
        mc_s "..."
        amb "What I wanted to talk about is why..."
        amb "Why you never saw me the way I saw you."
        amb "Because I tried, really I did, to show you who I was, but you never saw the real me."
        amb "In fact, you rejected me again and again..."
        mc_s "I-I'm not sure-"
        amb "Yes, you are. You remember how much I wanted you. But you always ignored me, treating me like a joke."
        mc_s "That's not true. I've never treated you like a joke."
        amb "You did. Every time I teased you, flirted with you, you just brushed me off like I was nothing."
        mc_s "That's the past now, Amber. Why can't you just accept it and move on?"

    show ep03_ambertalk14
    if ep01_amblove:
        amb "I know... I'm just so, so frustrated. I just need to talk about it, that's all. Can you give me that, at least?"
    else:
        amb "I did try to move on. I just wanted to talk about it, that's all. Can you give me that, at least?"
    $ show_walkthrough("ep03_amberfeels_menu")
    menu:
        mc_t "Should I give her a chance? Should I listen to her pour her heart out?"
        "Listen to Amber's feelings":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)

            mc_s "Alright, I'll listen. Go ahead, Amber. Tell me what's on your mind."
            amb "Are you sure, [mc_name]?"
            mc_s "Just go ahead, please."

            $ stopAllSubchannels(channel="music", fadeout=2)
            jump ep03_reunion_stay1


        "Refuse to hear Amber out":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ ep03_amberleft = True

            mc_s "You know, I'm actually feeling pretty tired right now. I think I'll go to sleep."
            mc_s "Maybe we can talk tomorrow, or some other time."
            amb "Oh... okay. We can talk tomorrow then if you're up for it."
            $ stopAudio(channel="music", subchannel=1, fadeout=4)
            jump ep03_reunion_left




label ep03_reunion_stay1:
    scene eigengrau with dissolve
    pause 1
    show ep03_ambertalk15 with slowfade
    mc_s "Alright, so what did you want to talk about?"
    if ep01_amblove:
        amb "It's not about what I want, it's about what you did. You lied to me, you led me on, and then you broke my heart."
        amb "I know you loved Antonella, but I thought you cared about me, and now I realize how wrong I was to believe that."
        mc_s "I'm sorry for that. I really am truly sorry."
        amb "Yeah, I know. But I need an explanation. Why did you do it?"
        mc_s "I-I can't give you an explanation, Amber. I'm sorry. I did what I thought was best at the time for everyone involved."
    else:
        amb "Why didn't you ever return my feelings, [mc_name]?"
        amb "Can you tell me that? Why couldn't you at least give me a chance, even when I poured my heart out to you?"
        amb "Why did you have to reject me?"
        mc_s "Easy, Amber. Look, if you want answers, you're not gonna like them, okay?"

    show ep03_ambertalk16
    if ep01_amblove:
        amb "But, I was right here, right here the whole time. Right here for you. But you left me, and you hurt me, and you--"
        if ep01_first:
            amb "I even gave you my body, and you used me and said you loved me, and then you went with her, and--"
        else:
            amb "I poured my heart out for you, and you said you loved me, and still you went with her, and--"
        amb "Do you realize what you did to me? Do you realize how bad you made me feel? How worthless and used-"
        mc_s "I didn't mean for that to happen, Amber. I didn't want to hurt you."
    else:
        amb "Fine then."
        mc_s "As I said back then, you were confused."
        mc_s "You just thought you had feelings for me, because I was your [br_full_r_low] and we spent a lot of time together growing up."
        amb "No, it was real. I was truly in love with you."
        mc_s "You just needed someone to hold on to, someone to make you feel less alone. And, well... you were too young to understand what real love is."
        amb "It wasn't just that and you know it."
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 4, 0)

    show ep03_ambertalk17 with vpunch
    if ep01_amblove:
        amb "Yeah... yeah, sure whatever you say."
        amb "Look, I know you're sorry. And I'm sorry for what happened between us. But we can't change the past."
        amb "It's done, and it's over now."
        mc_s "Okay... What do you want me to do, then to make things right?"
    else:
        amb "You still don't get it, do you?"
        amb "I mean... I give you that. I was a stupid kid, and you were right. I probably did fall in love with you for the wrong reasons."
        amb "But what I felt for you... it was real to me."
        amb "And even though I knew that, I couldn't bear seeing you with Antonella. It drove me insane with jealousy."
    show ep03_ambertalk19
    if ep01_amblove:
        amb "Nothing, nothing at all. It's not your fault, it's mine."
        amb "I was the one who fell in love with you, the one who couldn't move on, the one who--"
        mc_s "Stop. Just stop. You're being too harsh on yourself Amber."
        amb "No, you don't understand. You never will. You... you had Antonella, and I had no one. Not even you by my side."
        amb "What am I saying? I had no one, except me. I was alone. Just me against the world."
        mc_s "Look, I understand what you're saying, but--"
    else:
        amb "You don't care, do you about how I feel?"
        amb "Just say what's on your mind already."
        mc_s "You were my [si_full_r_low], Amber. Nothing else. Whatever you thought you felt for me, it was just because we were too close as [stp_sib_r_low]s."
        mc_s "I don't know how many times I have to repeat that, but you were confused, and I don't blame you for it now that we're older."
        mc_s "You thought you were in love, but you weren't."
        mc_s "And when you're young, it's difficult to tell the difference between love and infatuation."

    show ep03_ambertalk18
    if ep01_amblove:
        amb "But what? What, [mc_name]? Look this is not a rant, and I'm not trying to tell you how bad you are."
        amb "I just... want to get this off my chest once and for all."
        mc_s "Okay, okay I'm listening."
    else:
        amb "Are you done lecturing me?"
        mc_s "Yes, I'm done trying to explain."

    show ep03_ambertalk20
    if ep01_amblove:
        amb "It has been years since you broke my heart, and I've been trying to forget about it, but I can't seem to let it go."
        mc_s "Then... why don't you let it go and move on with your life?"
    else:
        amb "I... I wish we could have talked more back then. Maybe you would have understood me better."
        mc_s "Understood you better? What's not to understand? I've been clear since the beginning about how I felt."

    show ep03_ambertalk21
    if ep01_amblove:
        amb "It's not that easy. You can't just brush away your feelings, [mc_name]... You should know that better than anyone else."
        mc_s "What's that supposed to mean exactly?"
        amb "You're gonna tell me you let go of your feelings for Antonella, when you spent your whole life looking for her after she left?"
        amb "That's not something you just forget, no matter how hard you try to move on."
    else:
        amb "If you think that, then you're a fool and a hypocrite. Look, I'm not here to argue."
        amb "I'm just telling you how I feel... I mean, what I felt back then. Anyway, don't worry about it now."
        mc_s "You should get over this, Amber. It's in the past now and we've both grown up."
        amb "You sound so sure about this. Have you done the same, though? Have you moved on from Antonella?"
        mc_s "We're not talking about me right now."
        amb "Well, we should. You haven't moved on from her, have you?"
        amb "You're still hoping that she comes back, even though you have no idea where she is or even if she's still alive."
    mc_s "You know, Amber, maybe we should just stop talking about this, okay?"

    show ep03_ambertalk22
    amb "Alright, I'm sorry, I'm sorry. You just... make me so angry sometimes when you don't understand me."
    mc_s "I haven't done anything wrong, Amber."
    amb "I know... I'm just... frustrated and confused."
    amb "Let's stop talking about this, okay? I'll understand if you don't want to listen to me anymore tonight."
    $ show_walkthrough("ep03_amberstaygo_menu")
    menu:
        mc_t "Should I say anything else to her?"
        "Tell her to stay":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)

            mc_s "It's okay. We're both stressed, and you're still upset about the past."
            amb "So, you're not mad at me for bringing this up?"
            mc_s "Not at all. But I think we should change the subject."
            amb "Okay, if you say so I'll try to let it go."
            jump ep03_reunion_stay2


        "Tell her to leave":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ ep03_amberleft = True
            $ ep03_amberpastbehind = True

            mc_s "Right. Let's just stop this conversation. It's not helping anyone."
            amb "Can I just... hug you goodbye, at least?"
            mc_s "Sure, go ahead but make it quick."

            show ep03_ambertalk23 with hpunch
            mc_t "Don't look, don't look at her body. Just look ahead and think of something else."
            amb "Hugs make me feel better. You know, comforting, soft, warm... like old times."
            show ep03_ambertalk24
            mc_t "Don't look at her cleavage, don't look at her thighs. Don't look at anything inappropriate."

            show ep03_ambertalk25 with vpunch
            amb "Sorry, was that weird of me to say?"
            amb "Do you hate me for hugging you like this?"
            mc_s "I don't hate you, Amber. I could never hate you. You're my [si_full_r_low], after all and I love you."
            amb "Even though you want me?"
            mc_s "Look... I understand you are used to this kind of attention, Amber. But this is not the way you should go about it."

            $ stopAllSubchannels(channel="music", fadeout=2)

            show ep03_ambertalk27 with slowfade
            amb "Wow, way to kill the mood, [mc_name] you're such a buzzkill."
            amb "I just wanted to hug you for old times' sake. Is that so bad?"
            mc_s "We both know you wanted more than a hug, Amber. But I can't give you that kind of affection."

            show ep03_ambertalk28
            amb "Will you shut up, already? I didn't come here for this kind of rejection."
            mc_s "Then, why did you come here in the first place?"

            show ep03_ambertalk29
            amb "Just to talk. Like... to get closure on our past. But I better go, this is getting too awkward."
            show ep03_ambertalk30 with vpunch
            amb "Bye for now, [mc_name]."
            mc_s "Bye, Amber take care of yourself."

            jump ep03_reunion_left




label ep03_reunion_stay2:
    show ep03_ambertalk31 with vpunch
    amb "So... uh, what do you wanna talk about now, then?"
    mc_s "Anything is fine with me."

    show ep03_ambertalk32
    amb "What about your life in Osaka since you left?"
    mc_s "It's not as interesting as you may think. There's not much to share really."
    amb "Oh, come on. You have to have something interesting to share with me. Tell me about your job or whatever."
    amb "Did you meet anyone interesting? You can't have spent your whole time searching for Antonella all these years."
    mc_s "Believe it or not, but that's exactly how I spent my time. At least in my mind she was always there."

    show ep03_ambertalk33
    amb "Do you still think about her? Do you dream of her? Is that why you're so frustrated and closed off?"
    mc_s "Why the hell did you bring that up all of a sudden?"

    show ep03_ambertalk34
    amb "Okay... okay. What about other girls? Did you, I dunno, date anyone? Did you have sex with any of them while you were away?"
    mc_s "Does it matter? If I say yes, you're going to be jealous, and if I say no, you're going to feel sorry for me."
    mc_s "So what's the point in answering?"

    $ stopAllSubchannels(channel="music", fadeout=3)

    show ep03_ambertalk35
    amb "Was that bimbo that visited you at the hospital your girlfriend or something serious like that?"
    mc_s "What bimbo? Who are you talking about exactly?"
    amb "The one that visited you! Isabella told me there was a girl registered as a visitor at the hospital when you were unconscious."
    amb "What was her name again..."
    amb "Arianne or something like that. Remember her?"
    mc_s "Arlette is her name."

    show ep03_ambertalk36
    amb "Arlette..."
    amb "She's really your girlfriend then isn't she."
    mc_s "She's not my girlfriend... well not anymore at least."

    show ep03_ambertalk37
    amb "What does that mean, not anymore? Did you have sex with her before you broke up?"
    mc_s "Look, this is none of your business. And even if I did have sex with her, you should just learn to deal with it."
    mc_s "It's not like you and I are a couple or anything close to that."

    show ep03_ambertalk38
    amb "Maybe we should be a couple."
    mc_s "Amber, again with this nonsense?"
    amb "No, it was a joke... But hear me out for a second."
    show ep03_ambertalk39
    amb "I'm done trying to seduce you. You clearly don't want me, so what's the point in chasing after you anymore?"
    mc_s "Well, it sounds like you've finally realized the truth about us."

    show ep03_ambertalk40
    amb "I realize something, alright. I realize that you're not worth chasing after, not anymore after all this time."
    mc_s "Sounds like you're finally over me then."
    amb "Of course. How could I not be? Your excuse was Antonella, and now I know you did forget about her."
    amb "You just didn't forget about her for me but for this Arlette chick instead."
    mc_s "Like I said, I did not forget about her... Antonella I mean."
    amb "Yeah... yeah. It seems you're not the same guy I loved a long time ago when we were young."
    amb "You've changed. You're no longer the [mc_name] I once knew and adored."
    mc_s "So what does that mean for us now?"

    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(amber_theme, "music", 1, True, 3, 0)

    show ep03_ambertalk41 with vpunch
    amb "It means I'm not afraid of you anymore, [mc_name] like I used to be."
    mc_s "Huh what do you mean by that?"
    amb "When we were kids, you were everything to me. I was scared of you, in a way."
    amb "But now, I see a broken man, a man who wants to protect himself."
    amb "You're not the same strong, confident guy I fell in love with back then."
    mc_s "So you're over me, is what you're saying in a nutshell."
    amb "No. What I'm saying is, I'm not afraid to make a move on you now."
    mc_s "Uh... uh I don't know how to respond to that."
    amb "So this is gonna be interesting, huh between us?"
    show ep03_ambertalk42
    amb "I wanna know this broken man that you've become."
    amb "I wanna know the you, you don't show the rest of the world."
    amb "The you who's afraid of me, the you who's afraid of everything and everyone."
    amb "Because for the first time I can give you what you gave to me when we were young... someone to be feel safe with and loved by."
    mc_s "I--I don't know what to say to all of this."
    amb "Say nothing, then. And come with me... let's go talk outside under the stars.  It's not gonna be as awkward as you think I promise."
    $ show_walkthrough("ep03_amberinvpool_menu")
    menu:
        "Accompany Amber to the pool":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            $ ep03_talkaboutpast = True

            mc_s "Alright... but I'm not sure about this..."
            amb "Don't argue. You need some fresh air, and so do I to clear our heads."
            $ stopAllSubchannels(channel="music", fadeout=2)
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            $ stopAllSubchannels(channel="sfx", fadeout=1)
            jump ep03_poolnight


        "Decline Amber's invitation to the pool":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -15)
            $ check_levels("amber", "trust", -15)
            $ ep03_amberstrike = True

            mc_s "I don't think so Amber, I can't do this."
            amb "I'll be with you the whole time, [mc_name]. I'll keep you safe, I promise with all my heart."
            mc_s "I said no. Can I go to sleep now please?"

            $ stopAllSubchannels(channel="music", fadeout=2)

            show ep03_ambertalk51 with hpunch
            amb "Goddamn it, [mc_name]. I try to be nice, and you just... you just dismiss me like I'm nothing to you."
            amb "Of course, if I was Arlette, you'd do whatever I said without hesitation."
            show ep03_ambertalk52
            mc_s "I'm trying to be patient, but you're making it hard with all this pressure."
            mc_s "As you said, I'm not your [mc_name] anymore, so don't expect me to react like the old one would have."
            mc_s "All this drama and attention, it's tiring and overwhelming."
            mc_s "And I'm trying to be nice and kind, but you're making it really difficult for me to do so."
            mc_s "Believe me if you weren't my [si_full_r_low] I would totally throw you out of my room right now without a second thought."
            amb "[mc_name], just--"
            show ep03_ambertalk53
            amb "Fine. You win. Again like always."
            mc_s "I'm sorry, Amber. Really, I am but I can't give you what you want."

            show ep03_ambertalk54
            amb "Just so you know, [mc_name], I had lots of sex in the past few years while you were gone."
            amb "Like, a lot... Of sex with many different guys."
            amb "Like, a lot a lot of mind-blowing sex."
            mc_s "Uh, that's great. I guess good for you then?"

            show ep03_ambertalk55
            amb "You don't care... do you? You don't care that I--"
            mc_s "I'm glad you're able to enjoy your life. And I wouldn't expect you to be reserved for me after all this time, anyway."

            show ep03_ambertalk56
            amb "..."
            mc_s "What?! What's wrong now Amber?"
            amb "Just when I was starting to think things were getting better between us."
            mc_s "Better how exactly?"

            show ep03_ambertalk57
            amb "You see..."
            amb "I can't help feeling like a teenager when I'm next to you, [mc_name]."
            amb "And I don't want to feel that way anymore it's too painful."
            amb "We're not even teenagers anymore, and I hate that I keep acting like one."
            amb "Like, goddamn it, why can't I be normal and just-- get over you already!"
            amb "Just move on from you once and for all."
            mc_s "You're a great girl, Amber. I've always believed that about you."

            show ep03_ambertalk58
            amb "No, you're not being honest with me. And you're not saying that just to make me feel better. It's true isn't it."
            mc_s "Amber... please don't do this to yourself."
            amb "It's just... so hard to let go of these feelings."
            show ep03_ambertalk59
            amb "I'm so fucking pathetic. I don't deserve anything good in my life. I don't deserve your concern or your time or your love."
            mc_s "Amber... what--what are you saying?"

            show ep03_ambertalk60
            amb "Shut the fuck up... I don't need your pity either I've had enough of that."
            mc_s "Please, let me hug--"

            show ep03_ambertalk61 with vpunch
            amb "No. Get the fuck away from me don't touch me."
            amb "Do you really think I need you? After everything you've put me through, after everything you've done to me and made me feel?"
            mc_s "Amber, I--"

            show ep03_ambertalk62
            amb "No. You're not a part of my life anymore. You left me, remember?"
            amb "You knew how our [mo_full_r_low] hates me, you knew how I would suffer, and you just left me to deal with her by myself you abandoned me."
            amb "You only cared about yourself."
            amb "You knew our entire [fm_r_low] despises me, you saw me countless times begging for a little bit of understanding and not receiving anything in return from any of them."
            mc_s "I tried to help you, I--"

            show ep03_ambertalk63
            amb "Tried... Tried?! You call that trying? You abandoned me when I needed you the most, and you never looked back."
            amb "Oh... and you wonder why am I dramatic about you leaving me alone in this hellhole?"
            amb "You were that little branch I was holding on to when I was drowning, and you decided to take that away from me and give it to a ghost... a fucking ghost."
            show ep03_ambertalk64
            amb "Goodbye, [mc_name]... And welcome home I hope you're happy now."
            amb "I hope you have a miserable life just like I have all these years without you."
            $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
            scene eigengrau with dissolve
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            $ stopAllSubchannels(channel="music", fadeout=2)
            $ stopAllSubchannels(channel="sfx", fadeout=1)
            jump ep03_photofound




label ep03_reunion_left:
    show ep03_ambertalk43
    amb "Sorry for showing up out of nowhere, I didn't mean to impose on you like this."
    mc_s "It's fine. Don't worry about it."

    show ep03_ambertalk44
    amb "Sorry. I guess I'm just annoying, huh? I've always been too clingy and needy."
    amb "I'm sorry, I'll leave you alone for now."
    show ep03_ambertalk64
    amb "Good night, [mc_name]. Sleep well and sweet dreams."
    if not ep03_amberpastbehind:
        $ show_walkthrough("ep03_amberstop_menu")
        menu:
            mc_t "Is Amber gonna be okay? She looks so hurt and vulnerable..."
            "Stop Amber before she leaves":
                hide screen walkthrough_screen
                $ ep03_amberleft = False

                mc_t "Maybe I should stop her and try to talk to her, and, um... listen to what she has to say. She seems to really need this."
                mc_y "Amber, wait a second!"
                jump ep03_reunion_left_stop


            "Let Amber leave without saying anything":
                hide screen walkthrough_screen

                mc_t "Wait... why do I care? She's always been like this, dramatic and needy. I shouldn't be too concerned about her."
                mc_t "I'll just sleep it off and hope that she's fine by morning. It's not my responsibility to fix her problems."

                $ stopAllSubchannels(channel="music", fadeout=2)
                $ stopAllSubchannels(channel="amb", fadeout=1.5)
                jump ep03_photofound


    else:
        $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)
        scene eigengrau with dissolve
        $ stopAllSubchannels(channel="music", fadeout=2)
        $ stopAllSubchannels(channel="amb", fadeout=1.5)
        $ stopAllSubchannels(channel="sfx", fadeout=1)
        jump ep03_photofound




label ep03_reunion_left_stop:
    show ep03_ambertalk45 with hpunch
    amb "Huh?"
    mc_s "Wait a minute."
    amb "Why should I?"
    show ep03_ambertalk46
    amb "Do you actually need something, [mc_name]?"
    mc_s "Yeah... Yeah, I do. Come back inside with me."

    show ep03_ambertalk47
    amb "So suddenly I'm not annoying anymore?"
    mc_s "Just... come back, Amber. Please."
    amb "Why the sudden change of heart?"
    $ show_walkthrough("ep03_amberconvinc_menu")
    menu:
        mc_t "How should I convince her to come back inside?"
        "Try to convince Amber to stay by appealing to her emotions":
            hide screen walkthrough_screen
            $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
            $ playAudio(amber_sexy_theme2, "music", 2, True, 2.5, 0)
            amb "Well?"
            mc_s "I'm sorry for making you feel like I didn't care. Of course I care about you."
            mc_s "You're my [si_full_r_low], and you mean the world to me."
            amb "You... you do? Really mean that?"
            mc_s "Yes. Come on, let's go inside and talk. Please?"

            show ep03_ambertalk48 with vpunch
            amb "Oh! Oh!"
            amb "I can't believe this! You finally wanna talk to me!"
            mc_s "Your... chest is... quite exposed."
            amb "Huh?"
            show ep03_ambertalk49 at zoom_in
            mc_s "Nevermind."
            amb "What?! What about my chest? Is it really showing that much skin?"
            mc_s "Uhm... no, no, it's fine. Come on, let's go inside and chat."

            $ unlock_memory("m_ep03_talk")

            show ep03_ambertalk68 with vpunch
            amb "Aww, [mc_name]..."
            amb "I see I still have my touch, after all."
            amb "You can stare all you want, I don't mind one bit."
            amb "But can we go to the pool instead? I wanna see the stars while we talk and catch up."
            mc_s "The pool? Uh, we have one? I didn't know that."
            amb "Come on, [mc_name]. Where's your sense of adventure? Follow me and you'll see."
        "Attempt to make Amber stay by guilt-tripping her":
            hide screen walkthrough_screen
            amb "Well?"
            mc_s "Look, you caught me by surprise, okay? I wasn't ready for this. Can we start over, please and talk properly?"

            $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
            $ playAudio(amber_anger_theme, "music", 2, True, 2.5, 0)

            show ep03_ambertalk65
            amb "You didn't answer me... Am I not annoying anymore, or not in your eyes?"
            mc_s "Amber, you're my [si_full_r_low]. You're not annoying, you're just... you're just being like this."

            show ep03_ambertalk50
            amb "Oh, so I'm just like this. You're just like this, what does that even mean?"
            mc_s "You're being a bit dramatic, Amber."

            show ep03_ambertalk66
            amb "Dramatic?! Me?!"
            mc_s "A little, yes. Look, I'm sorry. Just come back inside with me, please."
            amb "Uh, okay, um..."
            show ep03_ambertalk67
            amb "Alright, fine. But not because you told me to. I'm only doing this for myself."
            mc_s "Yeah, sure. Come on then."
            amb "And I want us to talk at the pool under the starry sky."
            mc_s "The pool? Now of all times?"
            amb "Yes, now. I wanna see the stars while we talk and sort things out."
            mc_s "Fine, I'll show you the stars while we talk. Okay, Amber dearest?"
            amb "Shut up already."
            mc_s "Okay, okay. Calm down. Let's go and settle this."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_poolnight




label ep03_poolnight:
    scene eigengrau with dissolve
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7)
    $ playAudio(sfx_wind_pool, "amb", 1, True, 2, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_tokyo_residential, "amb", 2, True, 2, 0)

    show ep03_ambernight01 with circlewipe
    amb "So... uh, this is the pool."
    mc_s "I can see that, Amber."
    amb "You like it? You look a little lost there."
    mc_s "Sorry, it's just... my meds. I need to take them."
    amb "Right. Sorry about that."
    show ep03_ambernight02
    mc_s "It's alright. You know I'm still trying to wrap my head around the fact that we have a pool. And a huge yard."
    amb "Right? It's like walking into a different world compared to our old house."
    mc_s "You're telling me."
    amb "Remember our old home? And how small it was? Compared to this one, it was just..."
    show ep03_ambernight03
    mc_s "Seriously, where did they get the money for all this? I would never have believed we were so rich."
    amb "Beats me. I'm not asking too many questions, though."
    show ep03_ambernight04
    mc_s "It's strange, huh? This neighborhood... this house... it's just--"
    amb "Hey, I know, okay? It's all a little overwhelming sometimes. But [mo_r] and [da_r] must've made a lot of money somewhere... relax."
    mc_s "Maybe we can try and figure out where the money came from, you know, just to get an idea--"
    amb "Stop it, [mc_name]. You're always so paranoid. Seriously, we have a nice life, okay?"
    amb "Not everything is a police case for you to solve."
    mc_s "Alright, alright. I'm gonna drop it."
    amb "The police in you never stops investigating, huh? Always suspicious of everything and everyone."
    mc_s "Sorry, sorry. I just--"

    show ep03_ambernight06
    amb "In your eyes I must be a Yakuza princess or something, right?"
    mc_s "Because of your tattoos? They're cute, actually."
    amb "Cute?! Really? You think my tattoos are cute?"
    mc_s "They're pretty badass, actually. But not yakuza style tho."

    show ep03_ambernight07
    amb "Ha-ha, very funny."
    mc_s "Looks good on your type of body, that's all."
    amb "Really? And what type of body is that?"
    mc_s "Well, you know... you have a tall, voluptuous body."
    mc_s "And your tattoos, they add a certain edge, like you're a sort of metal goddess or something."
    amb "A metal goddess? Wow... [mc_name]."
    show ep03_ambernight08
    mc_s "Yeah, something like that. It's just... you've changed so much."

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.3)
    $ playAudio(sfx_glitch, "sfx", 1, True, 2, 0)

    show ep03_ambernight08 at animated_glitch
    amb "Well, it's been a long time. People change. We all do."
    show ep03_ambernight09 at animated_glitch
    mc_s "It's just weird. One moment you're here, looking like a metal goddess, and the next... it's like I'm seeing you as you were when we were younger."
    amb "What are you talking about?"
    mc_s "Your...you... your clothes. I can't believe it, Amber. It's like... they haven't changed. Not... not a bit."

    show ep03_ambernight10 at animated_glitch
    amb "Are you having a stroke or something? Don't joke around with me like that..."
    mc_s "I'm not joking. Your clothes, your face, everything, it's all the same. Like you're frozen in time."

    show ep03_ambernight11 at animated_glitch, dizzyness
    amb "[mc_name], look at me. You better not be joking, or I swear I'll--"
    mc_s "Uh.. I'm feeling a little dizzy. Maybe I should sit down."
    amb "You idiot, you are already sitting down! And don't you dare--"
    show ep03_ambernight12 at animated_glitch, dizzyness
    amb "[mc_name]?! No, no, no, no."
    mc_t "Huh? My body doesn't... What the hell is happening? And Amber, she's..."

    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    scene eigengrau with slowfade
    pause 1
    show screen mcpov_dying
    $ playAudio(sfx_splashpool, "sfx", 2, False, 0, 0)

    show ep03_ambernight13 with vpunch
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.7)
    $ playAudio(sfx_underwater, "amb", 4, True, 1, 0)

    mc_t "I can't move! It's like I'm paralyzed. And Amber... why does she look so young again? Is this a dream? It feels like one, but--"
    amb_y "[mc_name]! [mc_name]!"
    show ep03_ambernight14
    mc_t "Am I dying? Or... Am I reliving the past again?"
    amb_y"NO, NO, NO, NO! [mc_name]! [mc_name], PLEASE!"
    show ep03_ambernight15
    mc_t "It's so dark, I can barely see her... What a dumb way to die..."

    hide screen mcpov_dying
    $ setChannelVolume(channel="amb", subchannel=4, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    scene eigengrau with slowfade
    $ playAudio(sfx_pool_dive, "sfx", 7, False, 0, 0)

    show ep03_ambernight16 with vpunch
    amb_y "I'm not losing you, not again!"
    show screen mcpov_dying
    $ setChannelVolume(channel="amb", subchannel=4, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ playAudio(sfx_pool_moving, "sfx", 8, False, 0, 0)

    show ep03_ambernight17
    mc_t "Amber? Is she real? Am I dreaming?"

    hide screen mcpov_dying
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAudio(channel="amb", subchannel=4, fadeout=1.5)
    scene eigengrau with slowfade
    pause 1
    $ playAudio(sfx_pool_surfacing, "sfx", 3, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.7, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)
    show screen mcpov_dying
    show ep03_ambernight19 at dizzyness with bokeh
    mc_s "Ahhh... ohhhh.  I--I'm so, so confused."
    amb "You bastard! You'll pay for this, you'll pay for scaring me, [mc_name]!"
    mc_s "I--I feel... tired."

    show ep03_ambernight18 at dizzyness
    amb "Wait! Stop fading! STOP! Please, [mc_name], please!"
    amb "Fuck! Fuck, no! Not again, no, no, no."
    scene eigengrau with dissolve
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    hide screen mcpov_dying
    jump ep03_afterpool




label ep03_afterpool:
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)
    $ playAudio(sfx_bodydrag, "sfx", 2, False, 0, 0)
    $ playAudio(sfx_bodygrab, "sfx", 3, False, 0, 0)

    show ep03_afterpool01 with circlewipe
    amb "Come on, come on! Don't die, you idiot!"
    amb_t "Ugh! Oh my god, this is so hard."

    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)

    show ep03_afterpool02 with hpunch
    amb_t "Come on, come on, come on."
    amb "God damn it, [mc_name]! You're so fucking heavy!"
    $ stopAllSubchannels(channel="amb", fadeout=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 2, True, 1.5, 0)

    show ep03_afterpool03 with circlewipe
    mc_t "Uhhh... uhhh."
    mc_t "W-Where am I?"

    show ep03_afterpool04
    mc_t "Why am I on the floor? Why is it dark?"
    mc_t "I-- I don't remember anything after... after..."

    show ep03_afterpool05 at zoom_in
    mc_t "Amber? Why is she naked?"
    mc_t "What the hell happened?"
    mc_t "Holy shit... I've never seen boobs that big before."

    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)

    show ep03_afterpool06 with vpunch
    mc_t "I remember now! I was drowning! I was dying! And then Amber appeared and--"
    mc_t "Fuck. What the fuck happened after that?"
    mc_t "Did we fuck after that? Or is this part of the hallucination, too?"
    mc_s "Amber?"

    show ep03_afterpool07
    amb "Huh? [mc_name]? What the--"
    mc_s "Uhh... um... hi?"
    amb "Are you okay? Are you--"
    amb "Wait... what?"
    show ep03_afterpool08 with hpunch
    amb "Oh shit. I'm... we're... and you're..."
    mc_s "Wait, wait... I just woke up, I don't know anything! What did you--"
    amb "I'm sorry, [mc_name]. I just had to keep you warm, so I got you naked, and then I took my clothes off too because I was wet, and I didn't want you to freeze, so--"
    amb "I must've fallen asleep with you in my lap."
    mc_s "Right... but we didn't, you know..."

    show ep03_afterpool09
    amb "No! Of course not, what are you--"
    mc_s "It's okay, I just didn't want to assume anything."
    amb "Oh, okay. Yeah, we didn't. Don't worry."
    amb "Look, I know it's weird. But... I was worried about you, so I--"
    mc_s "It's okay, don't worry. I'll get up and..."
    amb "No, no! Don't move."
    mc_s "Um, why not?"
    amb "Because, I-- uh, I mean, you don't look so good, so just stay here and, you know..."
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)

    show ep03_afterpool10 with vpunch
    mc_s "It's okay, I'm fine. Besides I need to put some clothes on, so--"
    amb "You can't! Not yet, anyway."
    if ep01_first:
        mc_s "Why not? Is it because I'm naked? You forget you've seen me naked before."
    else:
        mc_s "Why not? Is it because I'm naked? You forget you're the one who stripped me--"
    amb "No, it's not that. It's--"
    show ep03_afterpool11
    mc_s "And besides when I woke up I had your breasts right on my face, so--"
    amb "Alright! Okay, look, you win. You can get up and get dressed."
    if ep01_first:
        mc_s "Great, thanks. Also, it's not like it was the first time we both have been naked, so--"
    else:
        mc_s "Great, thanks. Also, it's not like it was the first time I saw your tits anyway, so--"

    show ep03_afterpool12
    amb "Yeah, yeah, whatever. Just hurry up and get dressed."
    mc_s "Okay, just gonna grab my clothes, put them on, and--"

    scene eigengrau with dissolve
    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 2, 0)

    show ep03_afterpool13 with hpunch
    mc_s "Huh?!"
    amb "I thought you were going to die, [mc_name]. I was so scared."
    mc_s "I'm sorry, Amber. It was an accident."
    amb "Whatever, that's not what's important. I almost lost you tonight, and--"
    amb "But you're still here. With me."
    mc_s "Hey... I just realized I didn't thank you for saving my life."
    amb "It's okay. You don't need to thank me. I would do anything for you, [mc_name]."
    amb "Anything."
    mc_s "I, uh, I see."

    show ep03_afterpool14 with hpunch
    mc_s "So, uh, I guess I'll get dressed."
    amb "Did I say something wrong?"
    mc_s "No, I just... I just need some clothes, that's all."
    mc_t "She risked her life to save mine, and now we're alone in my bedroom... naked."
    mc_t "I know her feelings, I always have. She loves me. But I... I can't... or can I?"
    amb "Uhh... Is it me or... or you...?"
    amb "You're looking at me differently."
    show ep03_afterpool15
    mc_s "What? No, I'm just... uh...  I will look some clothes. Just give me a minute."
    amb "Okay... you can find me something too."
    mc_s "Uhm.... I don't think I have anything that would fit you, Amber."
    amb "Huh?! You saying I'm too big or something?"
    mc_s "I'm just saying, you know... You're tall and curvy, and... And I'm not. So we don't have the same size."

    show ep03_afterpool16
    mc_s "Alright, found some boxers."
    amb "Rrrggghhh. Just find me something I can wear."
    mc_s "I can go to your room and find some clothes. I'm sure you have--"
    amb "It's the one at the end of the hall, upstairs. Just go!"
    mc_s "Don't worry, I'll find something."
    amb "Get me a sweater, okay?! I'm cold!"
    mc_s "Sure, I will look for one. Don't worry."

    $ unlock_memory("m_ep03_night")
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_amberclothes




label ep03_amberclothes:
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_mc_room_night, "amb", 2, True, 1.5, 0)

    show ep03_caught1 with circlewipe
    $ ep03_madsuspicion = True

    mc_t "I'm an asshole. She just saved my life, and I'm treating her like she just gave me a cup of coffee or something."
    mc_t "Is it because I didn't want to be saved? Anyways... It isn't her fault, so I need to apologize."
    mad "Wow! Look at this! Boxer boy, walking around our house in his underwear, and no one notices him? Incredible."
    mc_t "Shit, I forgot about Madison."

    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(madison_theme, "music", 2, True, 2, 0)

    show ep03_caught2 with vpunch
    mc_s "Uhh, Madison, um..."
    mad "What the hell are you doing, [mc_name]? I thought you said you were gonna sleep."
    mc_s "I wanted to get something to eat."
    mad "Is that so? Why didn't you go to the kitchen and cook something, then?"
    mc_s "Um..."
    mad "You know, the kitchen is behind you, don't you?"
    mc_s "Oh, right."

    show ep03_caught3
    mad "Exactly. So, what about it? Why are you going upstairs? Are you hiding something?"
    mc_s "No, not really. I was just going upstairs to find, uh, um... some clothes."
    mad "Seriously? Now you wanna go to our rooms and steal our clothes? What happened to your clothes, huh?"
    mc_s "Uh, no. No, that's not--"
    mad "Or is it for other purposes, maybe? Hmmm?"
    mad "Come on, spit it out, [mc_name]."
    mc_s "Um, uh."

    $ show_walkthrough("ep03_maddiebod_menu")
    menu:
        "Check out Madison's body":
            hide screen walkthrough_screen
            $ rm.update("madison", "cor", 1)
            $ check_levels("madison", "cor", 1)
            $ ep03_madcheck += 1

            mc_t "Fuck it. I can't help myself."

            show ep03_caught4 at camera_zoom with dissolve
            mc_t "Damn, Madison's got a killer body. She may be petite, but she's still sexy as hell."
            mc_t "I can't take my eyes off her pussy. That thong is barely covering anything, and--"
            mad "So, are you gonna tell me? Where are you going or..."
            mad "Or... are you gonna keep checking me out?"
            mc_s "Uh, sorry, what?"
            mad "I saw you staring at me, [mc_name]. You thought I didn't see it, huh? You're an idiot."
        "Avert your gaze":
            hide screen walkthrough_screen

            mc_t "No. Not now. I need to focus. Besides, she's being annoying."
            mad "So, are you gonna tell me? Where are you going or..."
    show ep03_caught5
    mc_s "I... uh... look, Madison--"
    mad "Oh, shut up! Look, I don't give a fuck. Just go wherever you need to, and don't act like a creep next time."
    mc_s "Right, sorry about that. It won't happen again."
    mad "Remember, this isn't your house, okay? I always keep an eye on everyone here."
    mc_s "What do you mean by that?"
    mad "Oh, nothing. Just remember, I have my ways of finding out."
    mad "Now, go and find those clothes, alright?"
    show ep03_caught6 with hpunch
    mad "See ya, boxer boy."
    mad "You can thank me later for giving you a sexy view of my ass."
    mc_t "What the fuck?"

    $ show_walkthrough("ep03_maddieass_menu")
    menu:
        "Stare at Madison's ass as she leaves":
            hide screen walkthrough_screen
            $ rm.update("madison", "cor", 3)
            $ check_levels("madison", "cor", 3)
            $ ep03_madcheck += 2

            show ep03_caught7 at camera_zoom with dissolve
            mc_t "I can't believe I'm ogling Madison's ass like this. She may be smaller than Amber, but damn, she's got curves in all the right places."
            mc_t "I gotta admit, for such a tiny frame, her ass is absolutely mesmerizing. The way it jiggles with every step is hypnotic."
            mc_t "How the hell does a girl her age have an ass like that? It's almost too good to be true, and--"
            mad_y "YOU BETTER STOP STARING RIGHT NOW!"
            mad "Go get those clothes before I get mad."
            mc_s "Yes, sorry! I'm going upstairs, don't worry."
            mad "You're pathetic... Men."
            $ unlock_memory("m_ep03_green")
        "Resist the temptation to ogle Madison":
            hide screen walkthrough_screen

            mc_t "My sisters are fucking crazy."
            mc_t "Let's just get up and find something for Amber."

    $ stopAllSubchannels(channel="amb", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    pause 1.5
    $ playAudio(sfx_cardoor_open, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=7, volume=0.5)
    $ playAudio(sfx_midnightpast, "amb", 7, True, 1.5, 0)

    show ep03_caught8 with circlewipe
    mc_t "So this is Amber's room, huh?"
    mc_t "Looks so different from the one she had when she was a kid."
    mc_t "Anyway... Let's see what clothes I can find."
    mc_t "Alright, there's some underwear... and there's the sweater she asked me to get."

    $ show_walkthrough("ep03_amberroom_menu")
    menu:
        mc_t "Hm... Should I 'forget' about the sweater and come back with her underwear instead?"
        "Get the sweater":
            hide screen walkthrough_screen
            $ ep03_ambclothes += 2
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)

            mc_t "Nah, better not. I'm an asshole, but not THAT much of an asshole."
            mc_t "Anyway, I better hurry or else she's gonna kill me."
        "Forget about the sweater":
            hide screen walkthrough_screen
            $ ep03_ambclothes += 1
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)

            mc_t "Okay... I don't see any sweater, so I guess I'll have to come back with her underwear instead."
            mc_t "I know I'm being an idiot, but sometimes I don't understand my own actions."
            mc_t "Anyway... I'll bring the panties and surprise her."

            $ rm.update("amber", "trust", -2)
            $ check_levels("amber", "trust", -2)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_ambernite




label ep03_ambernite:
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 2, True, 1.5, 0)

    show ep03_night01 with circlewipe
    amb "About time! Did you get lost or something?"
    mc_s "I found something."
    amb "What's that?"
    if ep03_ambclothes == 2:
        mc_s "The stuff you asked me to bring."
        amb "Oh, that. Give it to me."
        mc_s "Sure. Here."
        amb "Thank you so much, [mc_name]! I was about to freeze here."
    else:
        mc_s "Remember you asked me to find you a sweater? Well, I couldn't find one, so--"
        mc_s "I brought you some panties instead."
        amb "...What?"
        mc_s "Just take them and get dressed."
        amb "Fuck! Alright, fine."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)

    show ep03_night02 with circlewipe
    if ep03_ambclothes == 2:
        amb "There, much better now."
        amb "The thong is a bit tight, but I can handle it for now."
        mc_s "That's good."
        amb "Hey, [mc_name]."
        mc_s "Yes?"
        amb "You're a great guy, you know that?"
        mc_s "Uh, what are you--"
        amb "I dunno. I just felt like I needed to say that. I had this feeling you thought about me differently, but... I know you care about me."
        mc_s "Um--"
        mc_t "Fuck, she's opening up to me... I wanna say something, but I don't wanna make things weird."
    else:
        amb "What the fuck, [mc_name]? I asked you to bring me a sweater, not--"
        amb "And you had me dress up like some fucking stripper!"
        mc_s "Sorry, okay? I couldn't find the sweater, so I brought the next best thing."
        amb "Bastard. Next time I'll let you drown."
        mc_s "Okay, okay! I'm sorry! But you do look good in that."
        amb "Pervert."
    show ep03_night03 with slowfade
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(amber_2nd_theme, "music", 1, True, 3, 0)
    if ep03_ambclothes == 2:
        amb "Okay, I better get back to my room."
        mc_s "I'm sorry... about earlier."
        amb "What do you mean?"
        mc_s "Amber, I acted like a total dick earlier. You risked your life to save my ass, and I didn't even properly thank you."
        mc_s "It means everything to me, and I need you to know how fucking grateful I am."
        amb "Don't worry, [mc_name]. You had a lot on your mind, I understand."
        mc_s "But--"
        amb "I... I don't know, [mc_name]. You don't need to apologize. I'd do it again in a heartbeat."
        mc_s "That's not the point. The point is--"
    else:
        amb "Anyway, it's late. I'm going to bed."
        mc_s "I'm sorry."
        amb "For what?"
        mc_s "My reaction... You know, I didn't properly thank you for saving my life."
        amb "Yes you did."
        mc_s "No, no. You saved my life. But I didn't tell you how much it really means to me."

    show ep03_night04
    if ep03_ambclothes == 2:
        amb "Alright, alright! You're forgiven, okay?"
        mc_s "Thank you."
        amb "So... umm... I should probably go. It's getting late and... umm... yeah. I need to sleep."
        amb "But maybe... um... I dunno since it's almost morning, I could..."
        amb "Never mind. Just forget it."
        amb "Anyway... goodnight, [mc_name]."
    else:
        amb "Oh, come on. You don't need to thank me--"
        mc_s "Just let me say this, I'm really grateful. Without you, I would've..."
        amb "Just stop, okay?"
        mc_s "No, seriously."
        amb "Don't..."
        amb "Umm... well."
        amb "I'll see you tomorrow, alright? I think I should... uh, go to my room, um... I don't think you want me sleeping here."
    $ show_walkthrough("ep03_ambersleep_menu")
    menu:
        mc_t "Huh? Does she want me to ask her to stay here?"
        "Invite Amber to spend the night":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)

            mc_s "I can make some space for you here, if you want to sleep together."
            amb "You mean...?"
            mc_s "It's not a king size bed, but we can make it work."
            mc_s "It's big enough for two people. Maybe."
            amb "Um..."
            amb "Are you sure...?"
            mc_s "Of course. You saved my life, the least I can do is share my bed with you."

            jump ep03_ambernite_sleep


        "Let Amber leave without inviting her to stay":
            hide screen walkthrough_screen

            mc_s ". . ."
            amb "Um... I'll just go."
            mc_s "Alright, see you tomorrow."
            amb "Yeah, sure."
            jump ep03_ambernite_bye




label ep03_ambernite_bye:
    show ep03_night05
    mc_s "Oh, by the way... Madison is watching tv in the living room. So, be careful."
    amb "Ugh... She's like a guard dog. Just what I need."
    mc_s "Alright. I'll see you tomorrow. And thanks again. I owe you one."
    if ep03_ambclothes == 2:
        amb "No problem, big [br_full_r_low]."
    else:
        amb "No problem, perv."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_photofound




label ep03_ambernite_sleep:
    show ep03_night06 with hpunch
    if ep03_ambclothes == 2:
        amb "Alright then."
        mc_s "You seem happy."
        amb "I am happy, [mc_name]. It means a lot to me."
        mc_s "It's no problem, really. That's the least I can do."
        mc_t "I hope she doesn't get the wrong idea or anything. Otherwise, I'm fucked."
        mc_t "Down boy. Remember, she's my [si_full_r_low]."
        amb "Alright, can I at least dry my hair or something?"
        mc_s "Sure, but I don't know how. I don't use a hair dryer."
    else:
        amb "Well... If you insist, I guess I can stay."
        mc_s "You seem pretty happy about it."
        amb "Stop it, you idiot."
        amb "Of course I'm happy about it."
        mc_t "I don't know if this is gonna be a good idea, but whatever."
        mc_t "I mean, just look at her lingerie... Damn, I should have brought that sweater."
        amb "Hey perv, can I at least dry my hair or something?"
        mc_s "Uh, yeah. Feel free to do whatever you want. But I don't have a dryer, so..."

    show ep03_night07
    if ep03_ambclothes == 2:
        amb "It's okay. I know there's one somewhere in your bathroom. Isabella uses it all the time."
        amb "Be right back."
        mc_s "Okay."
        mc_t "I'm so tired... I 'll just get into bed and wait for her."
    else:
        amb "That's okay, Isabella used to use your bathroom so there's probably one in there."
        mc_s "She did?"
        amb "Yeah. She did. Anyway, I'll be back in a minute."
        amb "You can stop staring at my butt in the meantime."
        mc_s "I wasn't looking at your butt."
        amb "Yeah, sure."
        mc_t "Don't get hard. I better just get into bed, and... calm down."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    pause 2
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep03_night08 with circlewipe
    if ep03_ambclothes == 2:
        amb "Okay, done! Ready to sleep."
        mc_t "Sometimes I forget how beautiful she is. I would tell her, but I don't want her getting the wrong idea."
    else:
        amb "Alright! I'm ready."
        amb "What should we do, uh... should I just get in?"
        mc_s "Yeah, just get in."
        mc_t "Sometimes I forget how gorgeous she is. And with that lingerie, I feel like I'm about to lose my mind and--"

    show ep03_night09
    if ep03_ambclothes == 2:
        amb "Thank you so much for this, [mc_name]. I mean, you didn't have to--"
        mc_s "It's no problem, Amber."
        amb "It'd be like old times, huh? You and I..."
        mc_s "Amber, please don't make this weird."
        amb "Huh?"
        mc_s "Look, you and I, we've had a complicated past, and I know you have certain, umm... 'feelings' for me. But--"
    else:
        amb "It's a little awkward, huh?"
        amb "Us in the same bed and everything."
        mc_s "Yeah, a little bit. But it's fine, don't worry."
        amb "Are you sure you want me to sleep here, [mc_name]?"
        mc_s "Yes, I'm sure. Just don't do anything weird, okay?"
        amb "Why would I do anything weird? Don't worry, I won't fucking touch you or anything."
        mc_s "Good, because I don't want you to--"

    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep03_night10 with vpunch
    if ep03_ambclothes == 2:
        amb "Ugh, I didn't mean it like that. I just meant that--"
        amb "You know what, never mind."
        amb "I'm just gonna crash, okay? I'm too tired to talk now."
        amb "Goodnight."
    else:
        amb "Why would you think that? Ugh! You're such a fucking asshole sometimes."
        amb "Can't I even stay here without you making dumbass comments?"
        amb "You didn't have to bring me that underwear, either. You could have brought me a sweater like I fucking asked you to."
        mc_s "Well, I'm sorry about that. But that's the first time I've been here in so long, and I didn't think about where anything was, and--"
        amb "Yeah, yeah. Whatever. I'm just gonna close my eyes and pass out. Good night."
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)
    $ playAudio(sfx_bedmove2, "sfx", 2, False, 0, 0)

    show ep03_night11 with hpunch
    if ep03_ambclothes == 2:
        mc_s "Amber?"
        amb "What?"
        mc_s "Nothing, just... are you okay?"
        amb "Yeah, I'm okay."
        mc_s "I just wanted to set some boundaries--"
    else:
        mc_s "Umm... can I ask you a question?"
        amb "About what?"
        mc_s "Are you mad at me?"
        amb "For what? Just stop, okay? I'm not mad at you, so just--"
        mc_s "Well, you seem pretty fucking angry, and--"
        amb "I'm not. Just drop it and let's just go to sleep, alright?"
    show ep03_night12
    if ep03_ambclothes == 2:
        amb "Look, just drop it, okay? Let's just get some sleep."
        mc_s "Alright, you're right. Sorry."
        amb "Good."
    else:
        mc_s "I didn't bring you the sweater because I wanted to see you in linger--"
        amb "Yeah, I figured."
        mc_s "You did? So--"
        amb "So... what? I'm not stupid, [mc_name]."
        amb "And I am not mad at you. Just let me sleep."
        amb "Night."
        mc_s "Really?"
        amb "Yeah, really. Fucking night."
        mc_s "Good night, then."

    $ show_walkthrough("ep03_ambersleep_menu2")
    menu:
        mc_t "Should I only turn off the lights and go to bed, or should I lock the door first?"
        "Turn off the lights and go to sleep":
            hide screen walkthrough_screen

            mc_t "I'm too beat to worry about the door."
            mc_s "I'm just gonna kill the lights, if you don't mind."
            amb "Go ahead."
            $ ep03_madcaught = True
        "Lock the door before turning off the lights":
            hide screen walkthrough_screen

            mc_t "Just to make sure no one barges in and catches me with Amber. Not that anything could happen, but..."
            mc_s "I'm just gonna lock the door first, that cool?"
            amb "Perfect. Do whatever you need."
            $ playAudio(sfx_doorclose, "sfx", 2, False, 0, 0)
            pause 1
    $ playAudio(sfx_lightswitchon, "sfx", 1, False, 0, 0)
    $ stopAllSubchannels(channel="amb", fadeout=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3)
    $ playAudio(sfx_nightsleep, "amb", 2, True, 1.5, 0)

    show ep03_night13 with circlewipe
    mc_s "Goodnight, Amber."
    amb "Yeah... Goodnight."
    if ep03_madcaught:
        show ep03_night14 with dissolve
        mad_t "What the hell is this? Are they... fucking or something? God damn it, Amber!"
        mad_t "So that's why he was prancing around in his boxers and trying to get clothes upstairs? What an asshole..."
        mad_t "I knew he was trouble! A pervert like all the rest, that's what he is."
        if ep03_madcheck == 1:
            mad_t "Undressing me with his eyes... what a bastard."
        elif ep03_madcheck == 2:
            mad_t "Eye-fucking my ass... what a bastard."
        elif ep03_madcheck == 3:
            mad_t "Undressing me with his eyes, eye-fucking my ass... what a bastard."
        mad_t "And now banging that fat old slut! I bet she wanted it... disgusting whore."
        mad_t "Whatever. But this info will be useful."
        mad_t "Sweet dreams, [mc_name] and Amber... until I make your lives a living hell."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_morningwithamber




label ep03_morningwithamber:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
    $ playAudio(sfx_morning, "amb", 5, True, 2, 0)

    show ep03_atmorning01 with circlewipe
    mc_t "Hmmm... what time is it?"
    mc_t "Looks like almost midday... Shit."
    mc_t "Oh, fuck! I forgot she was here."

    $ playAudio(sfx_bodyfall, "sfx", 1, False, 0, 0)

    show ep03_atmorning02 at zoom_in with vpunch
    mc_t "Oh, right."
    mc_t "Um, uh."
    if ep03_ambclothes == 2:
        mc_t "She looks so peaceful, it's kind of cute. Maybe I shouldn't wake her up yet."
        mc_t "She's definitely not the same girl anymore. She's grown up so much."
    else:
        mc_t "Oh my God. She's so fucking sexy."
        mc_t "She sure has changed a lot since she was younger. She's not the same girl anymore."
        mc_t "Just look at her tits, damn... they're fucking huge."

    $ playAudio(sfx_bedmove2, "sfx", 2, False, 0, 0)

    show ep03_atmorning03 with vpunch
    mc_t "Oh shit! She moved."
    if ep03_ambclothes == 2:
        mc_t "Wow... she looks like an angel when she's asleep."
        mc_t "Her skin seems so soft and smooth. I wonder how it appears under my touch."
        amb "Ummmmmmh."
        mc_t "Fuck! What the hell am I thinking?"
    else:
        mc_t "Holy shit, look at that body. She's in perfect shape."
        mc_t "Her skin appears so soft... I wish I could just run my hands all over her..."
        amb "Ummmmmmh."
        mc_t "Damn, she's waking up."

    show ep03_atmorning04
    if ep03_ambclothes == 2:
        mc_t "Looking at her like that, it's making me hard..."
        mc_t "I can't imagine if I hadn't brought the sweater for her..."
        mc_t "I wouldn't be able to resist fondling those tits, squeezing them, and sucking on them..."
        mc_t "Heh, what the fuck am I saying? This is my [si_full_r_low]! And I've already fucked up with Amber and--"
    else:
        mc_t "Okay, okay."
        mc_t "Relax. Just take a deep breath."
        mc_t "I fucking hate myself for not bringing her a sweater."
        mc_t "She's so hot... I would bang her right now if I could."
        mc_t "What the hell are you thinking, dude? Gotta get your shit together."

    $ show_walkthrough("ep03_ambersleep_menu3")
    menu:
        mc_t "Umm... But... Should I..."
        "Grope Amber":
            hide screen walkthrough_screen
            $ ep03_gropeamber = True
            jump ep03_morningwithamber_grope


        "Cover Amber up":
            hide screen walkthrough_screen
            jump ep03_morningwithamber_b2sleep




label ep03_morningwithamber_b2sleep:
    $ playAudio(sfx_bedmove2, "sfx", 4, False, 0, 0)

    show ep03_atmorning05 with hpunch
    mc_t "Alright. Better do this before she wakes up. She cannot know I was eye-fucking her."
    mc_t "I'll just go back to sleep... That should keep me distracted for a while."

    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_photofound




label ep03_morningwithamber_grope:
    $ setChannelVolume(channel="music", subchannel=1, volume=0.3)
    $ playAudio(mc_amber_x_theme, "music", 1, True, 3, 0)

    show ep03_atmorning06 with hpunch
    mc_t "I've got this urge to touch her breasts..."
    mc_t "If I'm slow and careful, maybe she won't wake up, and I can--"

    show ep03_atmorning07 at camera_zoom with flash
    mc_t "They're so... so big. Look at how perky they are, and--"
    mc_t "I can't believe I'm doing this, but I can't help myself..."
    mc_t "Those pink nipples, oh fuck..."

    show ep03_atmorning08
    mc_t "Maybe if I'm stealthy enough, she won't notice."
    mc_t "But her legs are in the way..."
    mc_t "I'll just fucking move them a little to the side and--"

    show ep03_atmorning09 with hpunch
    mc_t "Problem solved."
    mc_t "Now I just have to slide her panties down and--"

    show ep03_atmorning10 with hpunch
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.5)
    $ playAudio(sfx_breath_sleep_f, "sfx", 2, False, 0, 0)
    amb "Ummmm."
    mc_t "What the fuck, I almost got caught. Fuck..."
    mc_t "I gotta stop, or I'm gonna do something stupid."
    mc_t "But on the other hand, I'm really close to getting her panties down..."

    show ep03_atmorning11
    mc_t "Maybe if I change the angle a little bit..."

    show ep03_atmorning11 with hpunch
    mc_t "Sorry, [sis_r_low]. I'm just gonna hop in real quick and--"

    show ep03_atmorning11 with hpunch
    mc_t "They just need to come down a bit, and--"

    $ setChannelVolume(channel="sfx", subchannel=9, volume=1)
    $ playAudio(sfx_changeclothes_nozip, "sfx", 9, False, 0, 0)

    show ep03_atmorning12 with vpunch
    mc_t "There, got them."

    show ep03_atmorning12 at zoom_in
    if ep01_first:
        mc_t "Look at that... Long time, no see. Her pussy is still pink and tiny."
    else:
        mc_t "She has such a sweet little cunt. I wonder how it would feel wrapped around my cock..."

    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.7)
    $ playAudio(sfx_sighbreathfem, "sfx", 3, False, 0, 0)
    amb "Hmmm..."
    if not ep01_first:
        mc_t "Oh shit! She's awake!"
        amb "Huh? Uh--"
        $ setChannelVolume(channel="sfx", subchannel=5, volume=0.8)
        $ playAudio(sfx_recstop, "sfx", 5, False, 0, 0)
        $ stopAllSubchannels(channel="music", fadeout=0.5)

        show ep03_atmorning13 with vpunch
        amb "Huh?! What the fuck--"
        mc_s "Um, hey."

        show ep03_atmorning13 with hpunch
        amb_y "WHAT THE FUCK, [mc_name]?! ARE YOU FUCKING--??!!"
        $ setChannelVolume(channel="music", subchannel=7, volume=0.3)
        $ playAudio(amber_anger_theme, "music", 7, True, 2, 0)
        amb "You-- You--"
        amb "You tried to rape me while I was asleep?!?"
        mc_s "No, no! That's not--"

        show ep03_atmorning13 with hpunch
        amb_y "WHAT THEN?! WHAT THEN??"
        amb "Why did you spread my legs, and-- and--"
        amb "You were going to fuck me in my sleep, weren't you?!"
        mc_s "Look, calm down. It wasn't--"
        amb "No, fuck you! Move, and--"
        show ep03_atmorning13 with hpunch
        amb_y "Move!"
        jump ep03_morningwithamber_grope_sex_ruined


    else:
        mc_t "Oh shit! She's awake!"
        amb "Huh? Uh--"
        jump ep03_morningwithamber_grope_sex




label ep03_morningwithamber_grope_sex:
    show ep03_atmorning14 with vpunch
    mc_s "Um, hey."
    amb "What were you doing?"
    mc_s "Uhhh... Nothing, just--"
    amb "You don't have to say anything, I know what you did."
    if ep03_ambclothes == 2:
        amb "So this was your plan all along? This explains why you invited me to sleep with you."
    else:
        amb "So this was your plan all along? This explains why you didn't bring me a sweater yesterday."
    amb "But let me ask you this... Was it worth it? Hmm?"
    mc_s "I can explain--"
    amb "Oh, I bet you can. But don't worry, I'm not mad. Actually..."
    if ep03_ambclothes == 2:
        amb "Let me get rid of this sweater, so you can enjoy the view even more."
    else:
        amb "Let me get rid of this bra, so you can enjoy the view even more."
    mc_s "Wait, what?"

    scene eigengrau with slowfade
    pause 1
    show ep03_atmorning19 with circlewipe
    amb "Come on, get back to groping me or whatever you were doing."
    mc_s "What the--- Are you sure about this? I mean--"
    amb "We're adults now, [mc_name]. I want this. I've wanted this for so fucking long."
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.7)
    $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)

    show ep03_atmorning20 at camera_zoom with hpunch
    amb "Tell me, did you miss my wet pussy or what?"
    mc_s "Yeah..."
    amb "Yeah, you did. And look at this..."
    amb "This little thing here missed you too."
    mc_s "I--"
    amb "You can tell it's dripping wet. So, let's stop wasting time, okay?"
    mc_s "Sure! Whatever you want, [sis_r_low]."
    amb "So, do you have a condom or something? Just in case we--"
    mc_s "What? Really? You're joking."
    amb "Of course not! I may be older, but I'm not ready for kids yet."
    mc_s "Okay, okay. Well I don't have any condoms, but..."

    $ playAudio(sfx_bed_laying, "sfx", 4, False, 0, 0)

    show ep03_atmorning21 with hpunch
    amb "If you don't have a condom, then--"
    show ep03_atmorning21 with hpunch
    mc_s "Wait!"
    amb "What? What are you thinking?"
    $ show_walkthrough("ep03_ambersex_menu")
    menu:
        "Insist on having sex":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", -1)
            $ check_levels("amber", "cor", -1)
            $ ep03_insistamber = True

            mc_s "Just let me put it in first, and--"
            amb "No way! No fucking way I'm letting you fuck me raw."
            mc_s "But when we were younger--"

            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ stopAllSubchannels(channel="music", fadeout=2)
            jump ep03_morningwithamber_grope_sex_ruined


        "Respect Amber's wishes":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)

            mc_s "Umm..."
            amb "Maybe we don't need a condom after all."
            amb "Since you don't have any, and I don't have any... maybe we could try a different method."
            mc_s "What method? I'm all ears."

            $ rm.update("amber", "trust", 2)
            $ check_levels("amber", "trust", 2)

            show ep03_atmorning23 with vpunch
            amb "Well... you can fuck my tits. If you want to."
            amb "Or you can rub your cock against my clit... without actually putting it inside me. Would that work?"
            mc_s "Fuck yes! Of course!"

            $ show_walkthrough("ep03_ambersex_menu2")
            menu:
                amb "So which one do you want to try?"
                "Start with a titjob":
                    hide screen walkthrough_screen
                    $ ep03_ambersex_bbj = True

                    mc_s "Such a hard choice to make..."
                    mc_s "But I can't let my [si_full_r_low]'s massive tits go to waste."
                    amb "So you like them, huh? My big fucking titties?"
                    mc_s "Fuck yes, they're perfect."
                    amb "Get over here and start titty-fucking me."
                    $ stopAllSubchannels(channel="amb", fadeout=1.5)
                    jump ep03_morningwithamber_grope_sex_bbj


                "Skip the titjob and go for pussy play":
                    hide screen walkthrough_screen

                    mc_s "Umm... I guess we should start with the second option. Your tits are amazing, but--"
                    amb "Don't worry! My pussy is just as good. Here..."
                    amb "Let me turn around so you can have easy access."
                    $ stopAllSubchannels(channel="amb", fadeout=1.5)
                    jump ep03_morningwithamber_grope_sex_pj




label ep03_morningwithamber_grope_sex_bbj:
    scene eigengrau with dissolve
    pause 1.5
    show ep03_atmorning24 at zoom_in with slowfade
    amb "I've been dreaming about this moment for fucking ever."
    amb "My [br_full_r_low]'s thick dick between my huge boobs... How hot is that?"
    mc_s "Fuck, Amber... I can't believe we're actually doing this."
    amb "Believe it, [mc_name]. Your [si_full_r_low]'s tits are all yours."
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.4)
    $ playAudio(sfx_inhale_fem, "sfx", 3, False, 0, 0)

    show ep03_atmorning25 with hpunch
    amb "Ahhhh!"
    mc_s "Ahh... your tits feel so fucking good around my dick."

    show ep03_atmorning25
    $ setChannelVolume(channel="sfx", subchannel=4, volume=1)
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)
    amb "Don't worry, just keep going. It's alright."
    amb "Yeah... Fuck my titties, [mc_name]! Let me hear those balls slapping against my boobs."
    mc_s "God, your tits are so soft and warm... I could do this all day."
    amb "Mmm, yes... I love feeling your hard cock sliding between them."
    show ep03_atmorning26
    amb "Ahh... Do you like how tight my tits are? Huh?"
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)

    show ep03_atmorning26 at camera_zoom
    mc_s "I fucking love it."
    amb "That's right... Fuck me, [bro_r_low]! Fuck my big titties as hard as you want."
    mc_s "You like that, [sis_r_low]? You like it when I titty-fuck you hard and fast?"
    amb "Fuck yes! Give it to me, [mc_name]! Use my tits however you want!"
    show ep03_atmorning27 with hpunch
    $ playAudio(sfx_inhale_fem, "sfx", 3, False, 0, 0)
    amb "Ahhh! Oh God, yes!"
    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)

    show ep03_atmorning27 at camera_zoom
    amb "My tits are burning up with the heat of your cock."
    amb "Ahh... keep going! Faster, faster!"
    mc_s "Shit, Amber... You're driving me crazy..."

    show ep03_atmorning28 with hpunch
    mc_s "Fuck, my dick disappears in your tits, Amber..."

    $ playAudio(sfx_lick1, "sfx", 4, False, 0, 0)

    show ep03_atmorning28
    amb "It does... You can do anything you want to me, [mc_name]."
    mc_s "If that's true, then..."
    amb "Yes, what do you want me to do for you? Just tell me--"
    mc_s "Turn around and stick your fat ass out."

    jump ep03_morningwithamber_grope_sex_pj




label ep03_morningwithamber_grope_sex_pj:
    scene eigengrau with dissolve
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    pause 1.5
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep03_atmorning29 with vpunch
    amb "Like this?"
    mc_s "Yes, perfect."
    amb "Be careful, [mc_name]... Don't do anything you're gonna regret later."
    mc_s "Nah, don't worry."

    show ep03_atmorning31
    amb "I'm serious though! If you put it inside me, then we're gonna have a problem."
    mc_s "Oh? Is that so?"

    show ep03_atmorning30
    amb "Yes, so you better watch out. Or else I'll have to kill you myself."
    $ playAudio(sfx_gasp_female, "sfx", 3, False, 0, 0)

    show ep03_atmorning32 with vpunch
    mc_s "You sure?"
    amb "No! That's not... Please don't..."
    hide ep03_atmorning32
    if ep03_ambersex_bbj:
        mc_s "You said I could do whatever I want with you."
    else:
        mc_s "You said I could have easy access."

    $ setChannelVolume(channel="sfx", subchannel=5, volume=0.7)
    $ playAudio(sfx_femheavybreath, "sfx", 5, False, 0, 0)

    show ep03_atmorning32 with vpunch
    amb "I mean... I did say that, didn't I?"
    hide ep03_atmorning32
    mc_s "So come on..."

    show ep03_atmorning32 with vpunch
    amb "Fuck, [mc_name]... You're making it so hard to resist..."
    hide ep03_atmorning32
    mc_s "Just relax, [sis_r_low]... Let me make you feel good..."

    show ep03_atmorning33
    amb "I... I don't know if this is a good idea..."
    mc_s "We already started it, so might as well finish it, right?"
    amb "Please, I'm begging you..."
    amb "I'm horny but... maybe we shouldn't--"
    mc_s "Come on, Amber... Don't you want to feel my hard cock inside your tight little pussy?"
    amb "God, yes... But we can't, [mc_name]! We really shouldn't..."
    $ show_walkthrough("ep03_ambersex_menu3")
    menu:
        mc_t "Should I fuck her or not? Hmmm..."
        "Penetrate her":
            hide screen walkthrough_screen
            amb "Stop teasing me! It's not funny anymore!"
            $ ep03_amberpenetrate = True
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            jump ep03_morningwithamber_grope_sex_inside


        "Respect her boundaries":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            amb "Stop teasing me! It's not funny anymore!"
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            jump ep03_morningwithamber_grope_sex_pj_cont




label ep03_morningwithamber_grope_sex_inside:
    $ setChannelVolume(channel="sfx", subchannel=6, volume=0.25)
    $ playAudio(sfx_fem_surprised, "sfx", 6, False, 0, 0)

    show ep03_atmorning34 with hpunch
    amb "AHHH! OH MY GOD!"
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_femheavybreath, "sfx", 7, False, 0, 0)

    show ep03_atmorning34
    amb "FUCK! You really-- ughhhh."
    amb "Ahhh! Ahh... Get out of me!"
    mc_s "Just calm down, okay?"

    show ep03_atmorning35
    amb "Calm down? Seriously? You're fucking me without any condom!"
    amb_y "Get the fuck off me right now!"
    mc_s "Fine, I'll get out."

    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_morningwithamber_grope_sex_ruined




label ep03_morningwithamber_grope_sex_ruined:
    if ep03_amberpenetrate:
        scene eigengrau with dissolve
        $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
        $ playAudio(sfx_morning, "amb", 5, True, 2, 0)
        pause 1
        show ep03_atmorning22 with vpunch
        amb "Can't believe you fucked me! You asshole!"
        amb "Ugh... What a dick."
        amb "Of all the things you could have done to me, this is--"
        mc_s "Relax, okay? Don't worry."
        amb "Don't worry?! You think you're talking to an idiot?"
        amb "You know what? It's time to leave."
        mc_s "Amber, wait! I'm sorry, I got carried away..."
        amb "Carried away? You fucking crossed the line, [mc_name]!"
    elif ep03_insistamber:
        show ep03_atmorning22 with hpunch
        amb "Yes! When we were younger. But now we're not like that anymore."
        amb "I may be in love with you, but that doesn't mean I'm a dumb bitch."
        mc_s "Fine. You win."
        mc_s "Let's just forget about it."
        amb "That's it? I didn't say anything to offend you!"
        mc_s "You think it's easy for me? All night you were exposing your breasts and body to me, and--"
        amb "Huh?!"
        mc_s "I tried to control myself, but you just pushed me so hard."
        mc_s "So now you're saying no? Like it was so fucking hard for me to contain myself?"
        amb "Oh, so it's my fault now? For what, having a body? Fuck you, [mc_name]!"
    else:
        pass
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)

    show ep03_atmorning15 with vpunch
    if ep03_amberpenetrate:
        mc_s "What?"
        amb "Yeah, I'm leaving."
        mc_s "No, wait... I mean, look--"
        amb "I don't want to hear it."
        mc_t "Shit! Why did I fuck her? I mean, I wanted to but--"
        mc_s "I'm sorry, I--"
        amb "Sorry doesn't cut it, [mc_name]. You violated my trust."
    elif ep03_insistamber:
        amb "Fuck this! I'm just gonna grab my clothes and leave."
        mc_s "Whatever."
        amb "Asshole! Thinking like a fucking teenager."
        mc_s "Seriously? Now you're leaving me with blue balls?"
        amb "Oh, boo-fucking-hoo! Your blue balls are not my problem, dickhead."
        mc_s "Fuck! Alright, fine."
    else:
        amb "Fuck!!"
        amb "You're such an fucking asshole! I can't believe you would--"
        mc_s "I know, I know. I'm an asshole. I'm sorry."
        amb "Oh, really? Is that what you say now? And--"
        mc_s "Just listen to me! Listen, I was thinking--"

    show ep03_atmorning16
    if ep03_amberpenetrate:
        amb "Sorry?! Oh, you better be!"
        mc_s "Don't tell me you didn't like it too."
        amb "You think that makes it okay? I told you I didn't want to fuck without protection."
        amb "Think! Use that fucking head of yours for once!"
        mc_s "I know, but..."
        amb "But what, [mc_name]? You couldn't control your fucking urges for one second?"
    elif ep03_insistamber:
        amb "What?!"
        mc_s "Yeah, it's not fun."
        amb "You know what? You can just jerk off or something, whatever floats your boat. But I'm not helping you anymore."
        amb "Stop thinking with your fucking dick!"
        mc_s "... Alright, you win. I'm sorry, Amber. I shouldn't have pushed you like that."
    else:
        amb "Oh, you were thinking?! You better explain yourself or--"
        mc_s "I was thinking if we could, you know, just--"
        amb "I can't believe you did that. I mean, you reject me in every possible way, and now you--"
        mc_s "Amber, hear me out. I was thinking maybe we could--"

    show ep03_atmorning17
    if ep03_amberpenetrate:
        amb "Whatever, just forget it."
        mc_s "Look, can we try again? I promise I won't do anything stupid."
        amb "Hmm... You must think I'm an idiot."
        mc_s "But don't you wanna finish it? We started it and--"
        amb "Are you fucking serious right now? You just fucked me without a condom, and you want to go again?"
    elif ep03_insistamber:
        amb "I'm just gonna pretend nothing happened and that you're being an idiot right now because you're horny, and you can't think straight."
        mc_s "...Fair enough."
        amb "This whole fucking thing was a mistake anyway."
        mc_s "Amber, I'm really sorry. I let my hormones get the best of me."
    else:
        amb "Is raping sleepers your new kink or something?!?"
        amb "What kind of sick bastard are you?!?"
        mc_s "Jesus fucking Christ! I wasn't gonna rape you, alright??"
        amb "What were you doing then?!"
        mc_s "I was just looking at your... you know, I was trying to--"
        amb "Trying to what? Fuck me in my sleep? You're disgusting."
        mc_s "No, that's not what I meant! I just got carried away, I swear!"

    show ep03_atmorning18
    if ep03_amberpenetrate:
        amb "Finish it? Fuck off. I'm not doing this with you anymore."
        amb "I'm going back to my room. And don't you dare follow me."
        mc_s "Amber, please, can we talk about this?"
        amb "I don't want to talk to you right now, [mc_name]. Just leave me alone."
    elif ep03_insistamber:
        amb "Next time you try to fuck your [si_full_r_low], make sure you have a fucking condom with you."
        mc_s "Hey, I--"
        amb "Can it! I don't wanna fucking hear it."
        mc_s "I fucked up, Amber. I'm really sorry."
    else:
        amb "I can't believe you. You know what? Save it."
        mc_s "Amber, please listen--"
        amb "No, you listen to me!"
        amb "Don't ever try to touch me again. We're gonna talk about this, but not now."
        amb "I can't even fucking look at you right now."
        amb "Just--"
        amb "Just... Ugh! I'm outta here."
        amb "Have a nice day, asshole. I hope you're fucking happy with yourself."
    mc_t "Dammit! Now she's mad at me."

    $ ep03_amberangry = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_photofound




label ep03_morningwithamber_grope_sex_pj_cont:
    scene eigengrau with dissolve
    pause 1.5
    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.8)
    $ playAudio(sfx_femheavybreath, "sfx", 7, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.4)
    $ playAudio(sfx_sexslide1, "sfx", 2, False, 0, 0)

    show ep03_atmorning36
    mc_s "Don't worry, [sis_r_low]."
    amb "Ahhh! Aghh!"
    amb "I... Ahh!"
    amb "Fuck! I want your dick so badly..."
    amb "Oh God! Yes! That's what I wanted!"
    amb "Keep going!"
    amb "Fuck! I hate you for not bringing me a condom."
    mc_s "I know. Me too."
    mc_s "But this feels so fucking good, Amber... Your pussy is dripping wet."
    amb "Mmmm, yes... I love feeling your hard cock sliding against me."
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.5)
    $ playAudio(sfx_fem_surprised, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.4)
    $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)

    show ep03_atmorning41 with vpunch
    hide ep03_atmorning36
    amb "W-What are you doing?!"
    mc_s "Changing positions."
    amb "No, no, no... We agreed--"
    mc_s "It's okay. I'm not putting it inside you."
    amb "Then why did you turn me around? You said you weren't gonna--"
    mc_s "I just need to put it between your pussy and your ass."
    amb "Oh. Okay, um..."
    amb "Just be careful, [mc_name]. I don't want you to accidentally slip inside..."
    $ playAudio(sfx_bed_laying, "sfx", 3, False, 0, 0)
    $ playAudio(sfx_sighbreathfem, "sfx", 1, False, 0, 0)

    show ep03_atmorning42 with hpunch
    amb "Like this?"
    mc_s "Yes, perfect."

    $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)

    show ep03_atmorning43 with vpunch
    amb "Ahhhh!"
    amb "Oh God, I can feel your cock against my asshole!"
    show ep03_atmorning43 with vpunch
    mc_s "Just imagine if I was fucking you there."
    amb "I would love that... Fuck! What am I saying?"
    mc_s "You're saying what we both want, Amber. Don't be ashamed."

    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.9)
    $ playAudio(sfx_lick1, "sfx", 7, False, 0, 0)

    show ep03_atmorning45
    mc_s "You know... you can't get pregnant if I fuck your ass."
    amb "No! Please don't..."
    mc_s "Are you sure? Your body seems to be begging for it."
    amb "It's just... I--I... I've never done anything like that before, so..."
    mc_s "Hmmm..."
    mc_s "So my little [si_full_r_low] is a virgin, huh?"
    amb "Curse your perverted mind, [mc_name]!"
    mc_s "Looks like someone likes it."
    amb "Stop, please! If you keep doing that--"
    mc_s "What? You're gonna cum? Is that it?"
    amb "No! I will want you to fuck me, and then we'll both regret it later."
    mc_s "That's okay with me."
    amb "But not with me... Please, I beg you. Listen to me."
    $ show_walkthrough("ep03_ambersex_menu4")
    menu:
        amb "Let's just do this another day. Please."
        "Ignore Amber's pleas and fuck her":
            hide screen walkthrough_screen
            $ ep03_amberpenetrate = True
            $ rm.update("amber", "trust", -5)
            $ check_levels("amber", "trust", -5)
            $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)

            show ep03_atmorning44 with vpunch
            amb "Alright."
            amb "Thank you--"
            $ playAudio(sfx_gasp_female, "sfx", 3, False, 0, 0)

            show ep03_atmorning47 with hpunch
            amb "AHH!!!"
            amb "Haah, haaah, hahhh."
            $ playAudio(sfx_femheavybreath, "sfx", 7, False, 0, 0)

            show ep03_atmorning48
            amb "STOP! STOOOOOOOP! AAAAAGH!"
            mc_s "What? I thought you wanted this."
            amb "Get out of me! Ahhhhhhh!"
            mc_s "Shit, Amber! I'm sorry, I couldn't help myself!"
            amb "Fuck you, [mc_name]! You promised you wouldn't do this!"
            $ stopAllSubchannels(channel="music", fadeout=2)
            $ stopAllSubchannels(channel="sfx", fadeout=1)
            jump ep03_morningwithamber_grope_sex_ruined


        "Listen to Amber and stop":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 5)
            $ check_levels("amber", "trust", 5)
            $ rm.update("amber", "cor", 1)
            $ check_levels("amber", "cor", 1)
            pass
    $ playAudio(sfx_femexhale, "sfx", 1, False, 0, 0)

    show ep03_atmorning44 with vpunch
    $ ep03_ambersex = True

    mc_t "Fuck! Gotta control myself..."
    amb "Pretty please..."
    mc_s "Alright... I won't touch you anymore. Let's stop here."
    amb "Thank you, [mc_name]. I know it's not easy, but it means a lot to me."
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with dissolve
    pause 1.5
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
    $ playAudio(sfx_morning, "amb", 5, True, 2, 0)

    show ep03_atmorning49 with slowfade
    amb "Y-Yes... Thank you so much! I wouldn't be able to control myself if we kept going."
    mc_s "I understand."
    amb "You know, [mc_name]... I'm happy you came back. I missed you a lot."
    mc_s "What happened to my slutty [si_full_r_low]?"
    amb "I-I still am! But also... I don't know..."
    mc_s "Come on, out with it."

    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_bed_laying, "sfx", 1, False, 0, 0)

    show ep03_atmorning50 with vpunch
    amb "I think I still love you, [mc_name]..."
    mc_s "Why are you telling me this? We can't--"
    amb "We know that already. I'm just being honest with you and with myself. It doesn't hurt to say what I feel."
    $ setChannelVolume(channel="sfx", subchannel=2, volume=0.3)
    $ playAudio(sfx_bed_sitdown, "sfx", 2, False, 0, 0)

    show ep03_atmorning51
    amb "Anyway... Thank you for respecting my decision and not pushing any further."
    amb "Thank you for understanding me, and I hope we can have some more sexy times in the future."
    mc_s "I sure hope so, [sis_r_low]."
    amb "Now I better go back to my room before anyone notices I'm gone."
    mc_s "Sure."

    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)

    show ep03_atmorning52
    amb "Um, sorry about leaving you with blue balls, but..."
    mc_s "Don't worry about it. I can take care of them."
    amb "Maybe next time we can get that condom and go all the way."
    show ep03_atmorning53
    amb "Or perhaps you can use my backdoor?"
    mc_s "Backdoor?"
    amb "Yes... you can be the first one to fuck me up there. That sounds hot, huh?"
    mc_s "Hell yeah, it does!"
    amb "I can't wait to feel your big cock stretching my tight little asshole, [mc_name]."
    mc_s "Fuck, Amber... You're gonna make me cum just thinking about it."
    amb "I gotta go now. Bye, [bro_r_low]!"
    if ep03_ambersex and ep03_ambclothes == 1:
        $ ep03_ambersex_l = True
    elif ep03_ambersex and ep03_ambclothes == 2:
        $ ep03_ambersex_c = True
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    jump ep03_photofound




label ep03_photofound:
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.7)
    $ playAudio(sfx_digitalcamera3, "sfx", 1, False, 0, 0)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.5)
    $ playAudio(sfx_room_noise3, "amb", 1, True, 2, 0)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.6)
    $ playAudio(photos_theme, "music", 1, True, 2, 0)

    show ep03_antoback03 with ccirclewipe
    mad "So, do you think I'm ready for this?"
    eli "Almost, but you need to improve your poses."
    mad "And how do I do that?"
    eli "Just imagine yourself as a character. Like a princess, or a spy, or a fairy."
    eli "Remember, it's all about embodying a persona and telling a story through your expressions and body language."
    $ playAudio(sfx_digitalcamera1, "sfx", 1, False, 0, 0)

    show ep03_antoback04
    mad "That's a fucking weird idea. How am I supposed to--"
    eli "Language! And I don't care if you like it or not, you have to at least try it."
    eli "It's a common technique used by many successful models. Trust me, it works."
    isa "How much time is this gonna take? I wanna go home already..."
    mad "Shut up, Isabella! We're busy here!"
    eli "Of course, dear. Watch closely."
    show ep03_antoback05
    eli "Don't worry, sweetie. We'll be done soon."
    mad "Please, [mo_r]! Let's keep practicing."
    eli "Okay... as I was saying--"
    mad "Wait, [mo_r], can you show me an example of how to pose like a character?"
    show ep03_antoback07
    isa "[gra_r], I forgot my phone. Can you lend me yours? Pleaaaase?"
    eli "Yes, sure, honey."
    mad "Goddamn it, Isabella! Stop bothering us!"
    eli "I told you not to use that language in front of your [si_full_r_low], Madison! And why are you so upset over her using my phone?"
    mad "Ugh, whatever... And I'm her [aun_r_low], not her [si_full_r_low]! I have to have some power over her too, right?"
    show ep03_antoback09
    eli "Of course you don't!  You were raised as her [si_full_r_low], and now that's what you are."
    mad "Great, another fucking reminder that I don't have any control over anything."
    show ep03_antoback10
    eli "Alright, let me unlock my phone for you."
    isa "Thank you, [gra_r_low]." 
    eli "Here, honey. Be careful with it."
    show ep03_antoback11
    isa "Yes, thank you! You're the best!"
    mad "Oh, for fuck's sake! Can you please stop being so fucking perfect all the time?!"
    isa "It's not my fault I'm more lovable than you, Madison."
    eli "Girls, don't start fighting again!"
    mad "Whatever... Let's keep going with the photoshoot."
    isa_t "I think I will text my [da_r]."

    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    scene eigengrau with slowfade
    pause 2
    $ setChannelVolume(channel="amb", subchannel=5, volume=0.2)
    $ playAudio(sfx_morning, "amb", 5, True, 2, 0)
    $ playAudio(sfx_phone, "sfx", 1, True, 0, 0)

    show ep03_antoback01 with dissolve
    mc_t "Huh? Who could it be?"
    ##SMS WINDOW
    call screen phone_icons("ep03_sms01")
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)

    mc_t "Fuck it. I'm not in the mood."
    mc_t "Shit, I almost forgot! I got to grab all those boxes Isabella packaged from Osaka before someone throws them away."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep03_boxes




label ep03_boxes:
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.7)
    $ playAudio(sfx_earlypast, "amb", 2, True, 2, 0)

    show ep03_antoback13 with ccirclewipe
    mc_t "Yeah, definitely his."
    mc_t "How can they afford so many expensive things?"

    show ep03_antoback14
    mc_t "And this car must have cost a fortune."
    if not ep03_amberleft:
        mc_t "Anyways... as Amber said, not everything is a police case for me to solve."
    else:
        mc_t "Anyways... not everything is a police case for me to solve."
    mc_t "Let's find those boxes from Osaka."

    $ setChannelVolume(channel="sfx", subchannel=7, volume=0.6)
    $ playAudio(sfx_box_search, "sfx", 7, False, 0, 0)

    show ep03_antoback15
    mc_t "Ah yes! Here they are."
    if htl_episodes == 3:
        $ show_custom_notification("save_tip")

    mc_t "Wow. She really did pack everything by herself..."

    $ stopAudio(channel="sfx", subchannel=7, fadeout=0.5)
    scene eigengrau with dissolve
    pause 1
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.9)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)

    show ep03_antoback16 with vpunch
    mc_t "This can't be true. This..."
    mc_t "How did this get inside those boxes?! Did she pack this? I've never seen this picture before..."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(antonella_love, "music", 1, True, 2, 0)

    show ep03_antoback17 at camera_zoom
    mc_t "I mean, I remember taking this picture, but I never knew it still existed..."
    mc_t "I--I don't know what to think or say here. This is too strange..."
    mc_t "That moment was so perfect... So full of love and hope... I don't remember taking another photo with her after that one."

    show ep03_antoback18 with smoke
    mc_t "It was our last day together that summer, and we decided to take that picture... It was nice to be there with her."
    mc_t "She already had Isabella in her belly, but no one knew about it yet."
    mc_t "Not even us."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with smoke
    pause 2
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.4)
    $ playAudio(sfx_evenstreet, "amb", 2, True, 1, 0)
    $ setChannelVolume(channel="sfx", subchannel=3, volume=0.3)
    $ playAudio(sfx_footsteps_heelstile, "sfx", 3, True, 0, 0)

    show ep03_antoback19 with dissolve
    mc_t "I remember she telling me how much she hated taking pictures, and I thought it was funny because she looked like a model to me."

    show ep03_antoback20
    mc_t "I mean... I understood her, I disliked being photographed too."

    show ep03_antoback22
    mc_t "But how could I say no when I was so lost in her..."
    mc_t "Being part of her life made me feel so good... and freezing that moment forever in a photo felt right."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    scene eigengrau with dissolve
    pause 2
    $ setChannelVolume(channel="sfx", subchannel=4, volume=0.6)
    $ playAudio(sfx_doorclose, "sfx", 4, False, 0, 0)

    show ep03_antoback24 with slowfade
    mc_t "I guess this picture somehow survived all these years."
    mc_t "Seeing it now, after all this time, it's like a piece of my heart has been returned to me..."
    mc_t "But this photo... it isn't mine."

    show ep03_antoback25
    mc_t "This photo belongs to someone else."

    show ep03_antoback26
    mc_t "The only one who could have had this picture would be...  Antonella."

    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=2)
    $ update_htl_episodes()
    call hideNoise(transition=dissolve)
#-- End Episode 3
    if htl_episodes == 3:
        return


    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep04_title