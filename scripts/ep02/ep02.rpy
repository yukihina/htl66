



label ep02_start:
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    call showNoise(0.1, 0.15, transition=dissolve)
    $ quick_menu = True
    $ renpy.block_rollback()
## -- INTRO SCENE HOME
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)

    show ep02_home1 with slowfade
    $ config.rollback_enabled = True
    show screen stats_button
    show screen walkthrough_icon

    mc_t "Their lives went on, even thrived while I was gone."
    mc_t "Kinda ironic how it shows how unimportant I am."
    mc_t "But hey, at least my kid's got it better than I did..."

    show ep02_home2
    mc_t "Being here... feels like I'm trying to fit into someone else's life that ain't mine."
    mc_t "I was used to how my old place in Osaka felt... but this one's so... bright and empty."

    show ep02_home3
    mc_t "But when I shut my eyes, there's only Osaka... the one spot where I belong."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_lovehotel


## -- AOI SEX SCENE HOME




label ep02_lovehotel:
    scene eigengrau with clouds_inverse
    show ep02_osaka1 with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_nightroad, "amb", 2, True, 1.5, 0)

    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    mc_t "At night, Osaka's streets came to life."
    mc_t "The city glowed with neon signs, lighting up the buildings and streets."
    mc_t "You could hear sirens and people talking as crowds wandered around the busy roads, each lost in their own world."

    show ep02_osaka2
    mc_t "Back then, I was a cop, a regular day for me meant patrolling the city, watching out for any shit going down."
    mc_t "But at night... I was different."

    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(mc_theme, "music", 2, True, 2.5, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.4, fade_duration=1.5)
    $ playAudio(sfx_midnightpast, "amb", 1, True, 1.5, 0)

    show ep02_hotel01
    aoi "Y'know, you're the only cop I've met who doesn't wanna talk about his day."
    show ep02_hotel02
    mc_s "Maybe that's 'cause my day ain't worth talking 'bout."

    $ unlock_memory("m_ep02_friend")
    $ stopAudio(channel="amb", subchannel=2, fadeout=10)

    show ep02_hotel03
    aoi "Or maybe you just don't like opening up."
    mc_s "Opening up means someone else gives a damn. Why would you care?"

    show ep02_hotel04
    aoi "I dunno, maybe 'cause I'm human?"
    mc_s "Well, don't. I'm not into getting too personal."

    show ep02_hotel05
    aoi "Alright then. What do you want?"
    mc_s "Just shut your mouth and blow me."

    show ep02_hotel06
    aoi "I can open my mouth and legs, which one you want me to open first, officer?"
    mc_s "Quit calling me that."
    aoi "What? Officer? Oh, you want me to call you [daddy_r]?"
    mc_s "Nah, just shut it."

    show ep02_hotel07 with ccirclewipe
    aoi "Ahh! Don't stop! Please...[daddy_r]...!"
    mc_s "Stop fucking calling me that."

    show ep02_hotel08
    aoi "Does it make you feel shitty? Liking it?"
    mc_s "Fuck off."

    show ep02_hotel09
    aoi "Why are you being so aggressive, [daddy_r]? Did I do something wrong?"
    mc_s "I'm gonna gag you if you don't shut up."

    show ep02_hotel10
    aoi "And then what, [daddy_r]? You gonna punish me?"
    mc_s "Jesus fucking Christ... just let me tongue-fuck your cunt."

    show ep02_hotel11
    aoi "Ahhh!!!! Oohhh!!!!! Ooohhh!!!!!! Daaaddddyyyyyyy!!!!"
    mc_s "Fuck! I told you to shut the fuck up!"

    show ep02_hotel12 with vpunch
    aoi "Hey! Why'd you stop? I was almost there..."
    mc_s "'Cause you won't shut your trap."

    show ep02_hotel13 with hpunch
    aoi "You like 'em, huh?"
    mc_s "Just keep your mouth shut and let me do what I want with you."

    show ep02_01_anim2
    aoi "Do they remind you of your [mommy_r]'s big ol' titties, [daddy_r]?"
    mc_s "Don't. Fucking. Call. Me. That."
    aoi "Well, why not? Does it turn you on?"
    mc_s "You don't know shit about me."
    aoi "Oh no, baby boy? I bet you loved suckin' on 'em, didn't you?"
    mc_s "You're fucking sick."

    show ep02_hotel14 with hpunch
    aoi "Wait--whoa...you're...so rough..."
    show ep02_hotel14 with hpunch
    mc_s "Shut the fuck up."

    show ep02_hotel15 with hpunch
    aoi "Please, I thought we were--ahhh!...having fun...this ain't...aghhh!!"
    show ep02_hotel15 with hpunch
    mc_s "Your pussy feels good...just let me fuck you..."

    show ep02_01_anim1 with hpunch
    aoi "But you're hurting me..."
    show ep02_01_anim1 with hpunch
    mc_s "That's the point. You want me to nut, don't you?"

    show ep02_01_anim1 with hpunch
    aoi "Yeah..."
    show ep02_01_anim1 with hpunch
    mc_s "Then shut the fuck up and take it."

    show ep02_hotel16 with hpunch
    aoi "Aaargh!!! Ahh!! Oohhh!! Daaaadddd!!"
    show ep02_hotel16 with hpunch
    mc_s "Shit!! Fuck!!"

    show ep02_hotel16 with hpunch
    aoi "Daadd!!! DADDDYYYYYYY!!!!!!!!"
    show ep02_hotel17
    aoi "What's up? Why'd you stop again?"
    aoi "You alright? Did I say something wrong?"
    show ep02_hotel18
    aoi "Wait, was it something I said about your momma's tits? My bad, I won't--"
    mc_s "Nah. It ain't you."
    aoi "Then what's the problem?"
    show ep02_hotel19
    mc_s "Aoi... I already said I'm not gonna share my personal shit with no one."
    mc_s "So please, don't ask me nothing else."
    aoi "Okay, I won't push it."
    aoi "Just get back inside me."
    aoi "I promise you'll forget everything when you're deep in my pussy."
    scene eigengrau with dissolve
    show ep02_hotel20 with circlewipe
    aoi "Ha.... HAA!!!"
    show ep02_hotel20 with vpunch
    mc_s "Fuuuuck!!"

    show ep02_hotel20 with vpunch
    aoi "Can't...breathe...!"
    show ep02_hotel21 with vpunch
    aoi "You're being too rough, I can't take it..."
    show ep02_hotel21 with vpunch
    aoi "Aaahhh!!"
    show ep02_hotel21 with vpunch
    mc_s "Rough? You want rough?"

    show ep02_hotel22
    mc_s "You asked for this shit! You wanted me to fuck you like this!"

    show ep02_hotel22 with vpunch
    aoi "Too much! Too rough!"
    show ep02_hotel23
    mc_s "Is this what you want, Antonella?"

    show ep02_hotel23 with vpunch
    aoi "Hnnngg!!! W-what'd you say??"
    show ep02_hotel23 with vpunch
    mc_s "Did you miss me, Antonella?? Is this what you been dreamin' about?"

    show ep02_hotel23 with vpunch
    aoi "Ahhhh! I don't know what the fuck you talking about!"
    show ep02_hotel24
    mc_s "You shouldn't have left, Antonella! You should have stayed with me!"

    show ep02_hotel24 with vpunch
    aoi "I-I ain't who you think I am!"
    show ep02_hotel24 with vpunch
    mc_s "No one else could ever come close to you, Antonella!"

    show ep02_hotel24 with vpunch
    aoi "Who is she?? Who you trying to find in me?!"
    show ep02_hotel25
    mc_s "Huh? The fuck you saying?"
    aoi "Antonella?! Who the fuck is she?!?!?"
    mc_s "She's... She's no one."

    show ep02_hotel26 with slowfade
    aoi "[mc_name]... you ain't yourself tonight..."
    aoi "It's like there's something inside you... trying to get out..."
    mc_s "Leave me the fuck alone, Aoi. I pay you to fuck, not to be my shrink."

    show ep02_hotel27 with dissolve
    aoi "I-I know that. But I can't help worrying--"
    mc_s "Just shut the fuck up and let me do my thing. You want the cash or not?"

    show ep02_hotel28 with slowflash
    mc_s "Aaahh, that's better. I feel like myself again."
    mc_s "The fuck's this? Why you showing me your asshole now?"

    show ep02_hotel29
    aoi "Oh... this?"
    aoi "I wasn't sure if you'd like my pussy or my ass better, so I figured I'd show you both."
    aoi "You can pick whichever one you want."
    mc_s "Hmmm... you gonna let me fuck your ass? Thought you didn't do anal."

    show ep02_hotel30
    aoi "I don't usually, but since you were acting so weird earlier, I thought you might need a change."
    mc_s "Wow... that's... real thoughtful of you."

    show ep02_hotel31
    aoi "[daddy_r], this hole needs some love too, don't ya think? Will you give it some attention?"
    show ep02_hotel32
    aoi "Your babygirl wants you to fuck her ass, [daddy_r]. Would you do that for me?"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_mc_depression




label ep02_mc_depression:
#WALKKING TO HOME
    scene eigengrau with dissolve
    $ playAudio(sfx_raining_ext, "amb", 1, True, 2.5, 0)

    show ep02_booze01 with slowfade
    mc_t "Osaka at night, a city of shadows. Even the rain can't wash away its dirt."

    show ep02_booze02
    mc_t "Walking those empty streets, it was like I was the only one left. Like I was the last man standing."
    mc_t "But even the trains had called it quits for the night, so I guessed I was stuck with my own damn thoughts."
    mc_t "I was so done with that life... hookers, drugs, booze. All were just ways to kill time until the next high."
    mc_t "I didn't even know why I was still a cop."
    mc_t "I used to want to help people, but then all I could think about was the next night so I could get some pussy and drugs."

    show ep02_booze03
    mc_t "I felt like I was no better than the scumbags I was chasing."
    mc_t "When I became a cop, I thought I had finally found a reason... to find Antonella."
    mc_t "I thought it would give me some closure... or at least a reason to drag my ass out of bed in the morning."
    mc_t "But nothing went how I thought it would. Chasing her memory, it was like chasing a ghost... always out of reach."
    mc_t "And each time I came up short, I just ended up feeling empty... hollow."

    show ep02_booze04
    mc_t "In the past few years, I did some shit... real bad shit... Shit I can never take back."
    mc_t "I knew I was hooked on drugs, on booze, but it was the only way I knew how to deal. With all of it."
    mc_t "What else did I have? Oh... yeah, my [dau_r_low]. But she was better off without me. I wasn't fit to be a [da_r]. I never was."

    show ep02_booze05
    mc_t "Look at them, so carefree... so damn happy. Makes me wanna puke. I used to have that dumb dream... with Antonella."
    mc_t "But now? Now I know better. There are no happy endings, just people faking it 'til it all goes to shit. And in the end, everyone's just... alone."

    show ep02_booze06
    mc_t "Every step felt like a ton of bricks. I couldn't wait to crash in my bed and drift off into nothing."
    mc_t "I meant it wasn't just the booze and the drugs... it was every damn thing."
    mc_t "The job, the past, Antonella... all weighing me down."
    mc_t "Sometimes I thought I should just turn around, walk away from all that bullshit, start over somewhere else."
    mc_t "Somewhere I didn't have to constantly remind myself what a fuckup I was."

    show ep02_booze07
    mc_t "But then again, what kind of life would that have been?"
    mc_t "Without any meaning... without a point."
    mc_t "Maybe that was the shitty life I deserved."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_booze08 with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_evening_pool, "amb", 2, True, 2.5, 0)

    mc_s "Ah, Paz... waiting there like she owns the place. What speech am I gonna get tonight?"
    mc_s "Whatever she's pissed about, I can't bring myself to give a shit."

    show ep02_booze09
    $ rm.set_knows("paz", True)

    pa_s "Where the hell were you? You had me worried sick! You can't just vanish like that."
    mc_s "Yeah... my bad."

    show ep02_booze10
    pa_s "My bad? That's all you gotta say?"
    pa_s "Look at you... you reek like a sewer, and you're wasted too!"
    mc_s "Just leave me alone, Paz. I can handle my own shit."

    $ show_walkthrough("ep02_pazmctits_menu")
    menu:
        "Check her tits":
            hide screen walkthrough_screen
            jump ep02_paz_tits


        "Check her legs":
            hide screen walkthrough_screen
            jump ep02_paz_legs




label ep02_paz_tits:
    show ep02_booze12
    $ ep02_checkpaz += 1

    mc_t "That sports bra she's got on ain't doing shit."
    mc_t "Those tits are practically busting outta their cage, begging me to set 'em free."
    pa_s "Stop staring at my tits, you freak! Just 'cause you're drunk and horny don't mean you can disrespect me like that."
    if ep02_checkpaz == 3:
        mc_s "My bad. Again, my mind just... wandered."

        jump ep02_mc_paz_fight


    else:
        mc_s "My bad. My mind just... wandered."

        jump ep02_paz_legs




label ep02_paz_legs:
    show ep02_booze11
    $ ep02_checkpaz += 2

    mc_t "Mmmm... Damn, those curves."
    mc_t "My hands would look fine as hell wrapped around that waist."
    pa_s "Weirdo. Quit checking me out. Nasty."
    if ep02_checkpaz == 3:
        mc_s "Sorry. Just got distracted for a sec. Again..."

        jump ep02_mc_paz_fight


    else:
        mc_s "Sorry. Just got distracted for a sec."

        jump ep02_paz_tits




label ep02_mc_paz_fight: 
    mc_t "You ain't making it easy. Showing up here, with your sexy body and that sweet face... making me feel things I shouldn't."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(mc_broken_theme, "music", 1, True, 4, 0)

    show ep02_booze13 with vpunch
    pa_s "Are you even listening to me?"
    pa_s "The guys at the station been asking where you are. They want answers, and so do I."

    $ show_walkthrough("ep02_mc_paz_fight_menu1")
    menu:
        mc_t "What a hassle... now what do I tell her?"
        "I'll talk to them":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 1)
            $ check_levels("paz", "trust", 1)

            mc_s "Yeah, yeah... I hear you. I'll talk to the guys at the station."
            pa_s "That's all I want, [mc_name]. Take this seriously and don't throw away your future."
            mc_s "Yeah... I get it. I'll handle it."

            show ep02_booze14
            pa_s "Always. Just don't make me regret it, okay?"
            mc_s "I won't, I promise. Now get outta my way. I don't wanna talk anymore."
        "I don't care":
            hide screen walkthrough_screen

            mc_s "Tell 'em whatever you want. I don't give a damn anymore."
            pa_s "[mc_name], quit messing around. Your job's on the line here!"
            pa_s "This is your future we're talking about."

            show ep02_booze14
            mc_s "Maybe I don't want a future. Not a job, not anything. Now get the fuck outta my way before I lose my shit."

    show ep02_booze15 with hpunch
    pa_s "What the hell is going on with you? Talk to me. Don't shut me out. We're partners, remember?"
    mc_s "Just drop it, Paz. We're just coworkers, not buddies. So quit acting like you give a damn."
    pa_s "Do you really think that? That you're just a coworker to me?"

    show ep02_booze16
    mc_t "Christ... If Paz wasn't a cop, I'd bang her brains out right now. I bet she's dynamite in the sack."
    pa_s "[mc_name]... I know what you're thinking. Stop thinking with your cock and listen to me!"

    show ep02_booze17
    pa_s "Look... I'm worried about you. I know you're hurting. Please, don't push me away. Let me help you."
    mc_s "There's nothing you can do for me, Paz. Nothing anyone can do."
    pa_s "Bullshit. You can tell me anything, I won't judge. Whatever it is, we'll figure it out together."

    show ep02_booze18
    mc_s "You wouldn't get it."
    pa_s "Try me. Please. Just gimme a chance."
    mc_s "I-- I can't. Now just... get outta my way. I need some shut-eye."

    show ep02_booze19 with vpunch
    pa_s "Goddamnit, [mc_name]! Why are you being so damn stubborn? Are you that scared to let someone in?"
    mc_s "Forget it."
    mc_s "You know what, fuck this! Move!"

    scene eigengrau with dissolve
    $ setChannelVolume(channel="sfx", subchannel=1, volume=1)
    $ playAudio(sfx_slamdoor, "sfx", 1, False, 0, 0)

    show ep02_booze20 with vpunch
    pa_s "You're a fucking coward!"
    pa_s "Why won't you let me in?! You need me, you just don't wanna admit it!"
    pa_s "When you finally get your head outta your ass and see that, I'll be here waiting for you."
    mc_t "What a pain in the ass. But hot..."
    mc_t "Shit, she's so hot."

    show ep02_booze21
    mc_t "Well, whatever. I'll just rub one out to some porn or something."

    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_tobita_sinchi




label ep02_tobita_sinchi:
    scene eigengrau with dissolve
    $ playAudio(sfx_raining_ext, "amb", 1, True, 2.5, 0)
    $ playAudio(sfx_nighttobita, "amb", 2, True, 2.5, 0)

    show ep02_tobita1
    show tobita_location zorder 2 with dissolve
    pause 4
    hide tobita_location with dissolve
    mc_t "Tobita Shinchi, Osaka. This fucking place, man..."
    mc_t "At night, it was like nothing else mattered. The streets were full of people looking for an escape, but the deeper you went, the more fucked up it got."
    mc_t "You could smell the sex and sweat in the air, and everywhere you looked, there was some wild shit you never even knew was possible."
    mc_t "This was where the prostitutes made their living, selling their bodies and souls to any fucker with cash."

    show ep02_tobita2
    mc_t "So there I was, another goddamn night, trying to feel something... anything."
    mc_t "I kept telling myself it was just one more night, but who was I kidding?"
    mc_t "This shit was like a drug, a damn disease that wouldn't let go, no matter how hard I tried to quit."

    show ep02_whore01
    mc_t "Every drag of the cigarette gave me a moment of peace, wishing I could fill that emptiness inside me."
    mc_t "But nothing ever did. Not the booze, not the drugs, not even the sex."
    mc_t "But what the fuck was I even looking for?"

    show ep02_whore02
    aya "Well look who's back. Becoming a regular here, huh?"
    mc_s "Just needed to get my head straight. Doubt you'd get what that's like."
    aya "Nope, sure don't. Men come here to forget, women to make more problems. Don't see why you're any different."
    mc_s "Because I'm a cop, that's why. I'm not here for some quick fix like them. I just want... peace."

    show ep02_whore03
    aya "You think you're better than us? Out here every night, lurking around whorehouses. You're more like a yakuza than a cop these days."
    mc_s "You always stand in the rain? Or just when I'm around?"
    aya "Maybe I like the rain. Or maybe I'm just curious about a lost soul like you."
    show ep02_whore04
    mc_s "Lost? Nah, I know right where I am. Problem is, it ain't where I thought I'd be."
    aya "Listen, I'm just some old whore."
    aya "You want my two cents? Find someone who can actually help instead of coming around here every night."
    $ show_walkthrough("ep02_whore_menu1")
    menu:
        mc_t "What should I say to her?"
        "Got it, thanks":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 1)
            jump ep02_tobita_sinchi_good


        "Fuck off":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -1)
            jump ep02_tobita_sinchi_bad




label ep02_tobita_sinchi_bad:
    show ep02_whore06
    mc_s "Don't need advice, Aya. Couldn't help me if you tried."
    aya "Suit yourself then."
    aya "But your past will catch up with you someday."
    aya "And when it does, you'll regret the choices you made."
    show ep02_whore05
    mc_s "That so? We'll see."
    aya "We've all got debts, [so_r]. Some in money, others in the shit we chose."
    mc_s "And what's your debt, Aya? Running this whorehouse?"
    aya "None of your damn business. My life's my own. I don't owe nobody nothing."
    mc_s "Convenient excuse to justify pimping out your own [dau_r_low]."

    hide ep02_whore05
    aya "Wasn't my choice to bring Aoi into this world, you know that. What about you?"
    aya "Hiding behind that badge to cover your vices."
    mc_s "My badge isn't a shield... it's a liability."
    aya "Yet here you are, half-naked with me instead of doing your job."
    jump ep02_tobita_sinchi_aoicomes




label ep02_tobita_sinchi_good:
    show ep02_whore08
    mc_s "Guess you helped more than you know. Made Aoi, remember?"
    mc_s "Your girl makes me forget myself. So... nope, you helped plenty."
    aya "Maybe someday I'll return the favor."
    show ep02_whore07
    aya "Everything Aoi does, she learned from her mama. She's a reflection of me."
    aya "So whatever she does to you, that's me doing it. Got it?"
    mc_t "Not what I meant..."

    hide ep02_whore07
    mc_s "Are you flirting with me, Aya? Cuz if so, I might just take you up on it."
    aya "Ha! In your dreams!"
    aya "I'm old enough to be your [gra_r_low]. Besides, you couldn't afford me!"
    jump ep02_tobita_sinchi_aoicomes




label ep02_tobita_sinchi_aoicomes:
    show ep02_whore09 with hpunch
    aoi "Well well, what's this? Am I interrupting? Should I be jealous?"
    mc_s "Jealous? Of what?"
    aoi "I dunno, maybe of you two getting all cozy. [mo_r]'s not usually this into someone."
    show ep02_whore10
    aya "Just talking, Aoi. Nothing else."
    aoi "If you say so. Let's head inside. Getting chilly, and I know ways to warm up."
    hide ep02_whore10
    aya "That's my cue. Night, you two."
    aoi "No, [mo_r]! Stay! Let's all go in and have drinks!"
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.3, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1.5)

    show ep02_whore11 with ccirclewipe
    aoi "Quiet as the grave tonight. What's eating you?"
    mc_s "Hmm..."
    aya "Probably thinking about work, or lack of it..."
    aoi "[mo_r]! Rude! Ignore her. You look like you need that drink, hmm?"
    mc_s "Nah, I'm good. Thanks though."

    show ep02_whore12
    aya "So much for being friendly. Thought you came here to forget your troubles. That's what you said."
    mc_s "I'm not here to..."

    show ep02_whore13
    aoi "No need to explain, hun. No judgment. We just provide... relief."
    aya "Or release, depending what you need."
    mc_s "Fine. Get me a beer."
    aoi "One beer, coming up!"
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(tobita_theme, "music", 1, True, 4, 0)
    scene eigengrau with dissolve
    show ep02_whore14 at dizzyness with circlewipe
    mc_s "You know, this is... nice."
    mc_s "Don't know why, but it almost feels... homey. Like we're some kinda [fm_r_low]."

    show ep02_whore15 at dizzyness with slowfade
    aya "[fm_r]?! An old whore, a cop, and a--"
    aoi "I think it's sweet."
    aoi "Almost like you belong with us. Maybe you will someday."
    show ep02_whore16 at dizzyness
    mc_s "Pathetic, ain't it?"
    mc_s "Coming here night after night, just to... feel something. Don't even know anymore."
    aya "Well, you won't feel nothing talking about it. Why not try my remedy?"
    mc_s "Your remedy?"
    aoi "Ah yeah, her... remedy. Tell him, [mo_r]!"
    show ep02_whore17 at dizzyness with hpunch
    aya "Simple, really. You've wandered so long, looking for something you can't find."
    aya "Let me show you what you've been missing. Then you decide if you wanna keep chasing the past or embrace the future."
    aoi "[mo_r], you're brilliant! Look at his face, he's thinking about it!"
    show ep02_whore18 at dizzyness
    aya "Trust me, [so_r], there's things in life's dark corners you won't find nowhere else."
    aya "And who better to show you than me, a woman who knows the shadows?"
    mc_s "So you're suggesting we...?"

    show ep02_whore19 at dizzyness
    aoi "Yep, she's saying you should fuck her..."
    aoi "If you want."
    mc_s "You're not mad? Or jealous?"
    mc_s "You're basically pimping your own [mo_r_low] to me."

    show ep02_whore20 at dizzyness
    aoi "Why would I be jealous?"
    aoi "[mo_r]'s right, sex is the best way to find escape and relief from everything."
    show ep02_whore21 at dizzyness with vpunch
    aya "So... you want to start... or should I?"
    mc_s "Huh?"

    show ep02_whore22 at dizzyness with hpunch
    aoi "I'm offering myself to you too. You can fuck me. Right here, right now, and forget the world."
    $ unlock_memory("m_ep02_reunion")

    show ep02_whore23 at dizzyness
    aya "Mhmm, and I'm here too. I'm the appetizer, Aoi's the main course. Either way, you win."
    show ep02_whore24 at dizzyness
    aoi "Ha! [mo_r], you're such a poet. You'll make him blush!"
    show ep02_whore25 at dizzyness with slowfade
    mc_s "Honestly, I don't know what to do. You're both so..."
    aya "Then take us both. Why choose when you can have it all?"
    aoi "It's your lucky day. An offer like this won't come twice!"
    mc_s "Uhh..."

    scene eigengrau with dissolve
    show ep02_whore26 at dizzyness with circlewipe 
    aya "Speechless, huh? We're quite the sight."
    aoi "Take your pick. Whatever you want, we'll do."
    aya "But remember, whoever you choose, you win either way."
    show ep02_whore27 at dizzyness
    aoi "Let's make it fun. Answer a question right, you can have us one at a time or together."
    mc_s "Um... okay."

    show ep02_whore28 at dizzyness
    aya "[mc_name], you ever bang two yakuza chicks?"
    mc_s "Huh? Where'd that come from?"

    show ep02_whore29 at dizzyness
    aoi "Well, you're about to, right?"
    aya "Two yakuza, [mo_full_r_low] and [dau_r_low], and you haven't blinked."
    aoi "That get you going? Banging yakuza women at the same time?"
    aya "Your blood running hot knowing we could be dangerous?"
    show ep02_whore30 at dizzyness
    aya "You didn't know? We're both yakuza!"
    aoi "But don't worry, you're safe with us."
    mc_s "Like I care. Had worse. Least you two are hot."
    aya "Hear that, Aoi? He thinks we're hot! Now you know which way this is going."
    aoi "Which way you want, [mc_name]? The three of us or just you and me?"
    $ show_walkthrough("ep02_sexwhorescene_menu")
    menu:
        mc_t "What should I pick?"
        "Just Aoi":
            hide screen walkthrough_screen
            $ ep02_tobitabj += 1
            jump ep02_tobita_sinchi_bj


        "Both of them":
            hide screen walkthrough_screen
            $ ep02_tobitabj += 2
            jump ep02_tobita_sinchi_bj




label ep02_tobita_sinchi_bj:
    show ep02_whore31 at dizzyness
    if ep02_tobitabj == 1:
        mc_s "Sorry Aya, I don't like GILFs."
        aya "Your loss. Coulda had a wild ride."
        aoi "Relax [mo_r], he picked me. You can go."
        aya "Okay, fine. Have fun."
    else:
        mc_s "Actually, I choose both. Can we start?"
        aoi "Damn, eager much? Can't wait to get your hands on us."
        aya "Easy tiger. How 'bout a little taste test first?"
    scene eigengrau with dissolve
    show ep02_whore33 at dizzyness with circlewipe
    if ep02_tobitabj == 1:
        aoi "You've made [mo_r] mad."
        aoi "She don't like being rejected. So I'mma punish you now."
        aoi "Make you come so hard you won't walk for a week."
    else:
        aya "You were right, Aoi. He is big. Perfect for us."
        aoi "This guy's got stamina, [mo_r]. He'll last longer than most."
    show ep02_whore34 at dizzyness
    if ep02_tobitabj == 1:
        aoi "Let's see what you got, [mc_name]. Give me your worst."
    else:
        aoi "Do you mind if we take turns sucking your cock?"
        mc_s "Please... don't mind me. Please continue."

    show ep02_whore35 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "Ugh... UGH! Oh god, you taste so good!"
    else:
        aya "Mmm, you like that, huh? You like how my [dau_r_low] sucks your cock like a whore?"
        aya "Look at her. She's really into it, like she hasn't sucked a dick in months. It's so hot."
        mc_s "Yeah... Oh fuck!"

    show ep02_whore36 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "God damn, I can't breathe! Your dick is so big!"
    else:
        aya "She's such a... cum-hungry slut for you. Are you gonna cum all over her face, [mc_name]? You wanna cover her in your jizz?"
        show ep02_whore37 at dizzyness with hpunch
        aya "It looks like he's almost ready to pop. You ready, baby girl?"
    show ep02_whore38 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "Fuck, I'm drooling all over your dick. I can barely swallow!"
    else:
        aya "That's right, suck that cock harder! Make him explode!"
    show ep02_whore39 at dizzyness with hpunch
    if ep02_tobitabj == 1:
        aoi "Mmm, mmmm, mmmmmmm, oh, oh, mmm, ohhhh!"
    else:
        aya "That's it! Keep sucking! Make him cum all over your face, you filthy slut!"
    show ep02_whore40 with dissolve
    if ep02_tobitabj == 1:
        aoi "So hot, so big, so much! I can't wait to feel it all inside me!"
        aoi "Give it to me, please! I need it!"
    else:
        aya "Aoi, you made him cum!"
        aya "Such a mess. I better help you clean up, baby girl."
        aya "C'mere, [mc_name]. I want my turn."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_yakuza_club




label ep02_yakuza_club:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.7)
    $ playAudio(sfx_evenstreet, "amb", 3, True, 2.5, 0)

    show ep02_dotonbori1 with slowfade
    show doton_location zorder 2 with dissolve
    pause 4
    hide doton_location with dissolve
    mc_t "You know, Osaka isn't like Tokyo."
    mc_t "The bright lights here, they hide a lot more than you'd think."
    mc_t "The Yakuza, they ain't just some street thugs."

    $ stopAudio(channel="amb", subchannel=3, fadeout=1.5)

    show ep02_hostclub01 with slowfade
    $ playAudio(dotonbori_theme, "music", 2, True, 2.5, 0)

    mc_t "Nah, they're like a whole other government, running shit from the shadows."
    mc_t "They own the night in this city, and they don't fuck around."
    mc_t "You step outta line, and they'll make you wish you were never born."

    show ep02_hostclub02
    hid "Rina! Get your ass over here!"
    rin "I... I'm not sure what you want, Mr. Hideo. I already gave you what you asked for."
    show ep02_hostclub03
    hid "Yeah, and you did good. But I need you to do something else for me."
    rin "W-What do you need?"
    show ep02_hostclub04
    hid "I need you to bring me some new girls. Young ones, okay?"
    rin "New girls? Don't you have enough already?"
    show ep02_hostclub05
    hid "More than enough, but I'm craving some fresh meat."
    hid "All these girls here, they're too used up. I want tight young pussy who hasn't been touched, get it?"
    hid "You seen anyone like that lately?"
    rin "I don't know where to find girls like that."
    show ep02_hostclub06
    hid "Not even a hint of where they might be at? Don't you got a friend who's looking for work?"
    rin "My friends all work here."
    show ep02_hostclub07
    hid "Look, don't let me down."
    hid "If you don't find me something in the next few weeks, I'mma have to find someone else who can help me out."
    hid "And you know how that goes, don't you?"
    rin "Yes... Yes, I get it. I'll do what I can."
    show ep02_hostclub08
    mc_t "The red-light district, it's their playground."
    mc_t "Every pleasure you can imagine, it's all there."
    mc_t "But it comes at a price. Not just cash, but... something deeper."
    mc_t "In Tokyo, things are more... clinical."

    show ep02_hostclub09
    mc_t "But here in Osaka, the Yakuza, they're part of the city's DNA."
    mc_t "You can feel them everywhere, like a cancer you can't shake."

    show ep02_hostclub10
    mc_t "The Yakuza, they don't just run the night; they control the fear, the respect, the very lives of anyone ballsy enough to step into their turf."

    show ep02_hostclub11
    rin "Hey! Cut it out!"
    show ep02_hostclub12
    "Bodyguard" "Mind your own business. Stay out of it, or you're next."

    show ep02_hostclub13
    hid "..."
    hid "Shut the hell up, both of you!"
    hid "If you two can't play nice, I'll toss your asses out on the street. We clear?"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_the_day_after




label ep02_the_day_after:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_earlymor, "amb", 1, True, 2.5, 0)

    show ep02_nxtbooze01 with slowfade
    mc_t "I... I didn't know it then..." 

    show ep02_nxtbooze02
    mc_t "But there was a link between that story and mine..."

    show ep02_nxtbooze03
    mc_t "A link that would lead me to the truth and uncover the dark secret hiding in the shadows of Tobita Sinchi."

    show ep02_nxtbooze04
    mc_t "A girl... an innocent, caught in the middle of all this chaos."

    show ep02_nxtbooze05
    mc_t "She was like a flower trying to bloom in a concrete jungle."
    mc_t "So delicate and pure, but surrounded by darkness and decay."

    show ep02_nxtbooze06
    mc_t "But she didn't know it yet, and neither did I."
    mc_t "I was just starting to wake up to the reality of what was going down around me."

    show ep02_nxtbooze07
    mc_t "I was barely a cop, barely human, barely alive."

    show ep02_nxtbooze08
    mc_t "Waking up around whores, alcohol and drugs was just another day for me."

    $ unlock_memory("m_ep02_hangover")

    show ep02_nxtbooze09
    mc_t "My head was pounding, and I didn't know what to do."

    show ep02_nxtbooze10
    mc_t "All I knew was that I needed to remember who I was, or who I thought I was."

    show ep02_nxtbooze11
    mc_t "But that didn't happen. Not yet. Not until I found her."

    show ep02_nxtbooze12
    mc_t "The girl of the night... the lost lamb in the valley of wolves."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_arle_intro




label ep02_arle_intro:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_eveningtraffic, "amb", 2, True, 2.5, 0)

    show ep02_friends01 with slowfade
    show kama_location zorder 2 with dissolve
    pause 4
    hide kama_location with dissolve
    arl "Ugh, this heat is killing me. I feel like I'm melting."
    rin "Tell me about it, girl. It's hotter than hell out here. I can barely breathe."
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.15, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.4)
    $ playAudio(arlette_theme, "music", 3, True, 2.5, 0)

    show ep02_friends02
    arl "And to make matters worse, I still haven't heard back from that modeling agency. It's been weeks."
    rin "Seriously? Those bastards don't know what they're missing. You're a total smoke show, Arlette."
    arl "Thanks, Rina. But sometimes I wonder if I'm just wasting my time chasing this dream."
    show ep02_friends03
    rin "Goddamn girl, you're straight-up fine as hell. I don't think I've ever seen someone so perfect."
    show ep02_friends04
    arl "Oh, stop it. There's nothing special about me."
    show ep02_friends05 with hpunch
    rin "I'm dead serious! Look at yourself."
    rin "Your body is like a goddamn sculpture, and your eyes are so intense they could make anyone bust a nut."
    rin "Like, I'm not even kidding. If I was into girls, I'd be all over you in a heartbeat."
    arl "Oh my god, shut up!"
    rin "Say, have you ever thought about being a host?"
    show ep02_friends06
    arl "Sometimes. But I don't know..."
    rin "Why not?"
    rin "You're a total pro at chatting people up and making them feel good."
    rin "Plus, you've got that whole mysterious European thing going on. People would be throwing themselves at you."
    arl "Yeah, you're right... and I could definitely use the cash. But still..."
    show ep02_friends07
    rin "What's holding you back?"
    arl "I don't know, it just feels kind of scummy. Like I'm using my looks to play people or something."
    rin "It's not like you're taking advantage of anyone."
    rin "It's just flirting and conversation. No different than being a bartender or a waitress."
    show ep02_friends08
    arl "I guess...but isn't that how you got started as a call girl?"
    show ep02_friends09
    rin "Yeah, but that was different. I had debts up to my eyeballs, and I was out of options."
    rin "This would just be a temporary gig while you get your shit together."
    show ep02_friends10
    rin "Trust me, you'd kill it as a host. The customers would be eating out of the palm of your hand."
    arl "Alright, I'll think about it."
    arl "But if I do this, you better have my back."
    show ep02_friends11
    rin "Of course, babe. I'll be there to guide you every step of the way. We'll make a killing together."
    arl "Okay... But if things get too crazy, I'm out."
    rin "Deal. We're gonna run this town, just you wait and see."
    $ unlock_memory("m_ep02_friendship")
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_the_talk




label ep02_the_talk:
    scene eigengrau with dissolve
    $ playAudio(sfx_japanday_cross, "amb", 2, True, 2.5, 0)

    show ep02_partners01 with slowfade
    pa_s "You ever wonder about all the stories behind those windows?"
    pa_s "People just living their lives, dealing with their own shit."
    mc_s "I just see a bunch of assholes trying to survive."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.7)
    $ playAudio(paz_theme, "music", 1, True, 2.5, 0)

    show ep02_partners02
    pa_s "But that's the thing, isn't it? We're all trying. You, me, everyone."
    mc_s "Trying to what?"
    pa_s "Trying to get better, man. Trying to live a life."
    pa_s "To find some happiness, help others out, keep our shit together. You know what I mean?"
    mc_s "You always had a knack for making everything sound deep, Paz."

    show ep02_partners03
    pa_s "Osaka's got us all by the balls."
    pa_s "But you... it's like you're diving headfirst into the abyss, no fight left in you."
    mc_s "Maybe some battles aren't worth the scars, Paz."
    pa_s "That's just it, isn't it? You think you don't deserve to win."

    show ep02_partners04
    pa_s "You've got this whole brooding lone wolf thing going on, but it's getting stale, [mc_name]."
    pa_s "People give a damn. I give a damn."
    mc_s "And you think I don't?"
    mc_s "That I don't wish things were different, that I had more power to change shit?"
    mc_s "Just give me some space, Paz. Please."

    show ep02_partners05
    pa_s "So what, you're just gonna shut everyone out? Is that your master plan?"
    mc_s "..."
    pa_s "You know, there's more to life than this... whatever this is. You don't have to keep running. Not from me."

    show ep02_partners06
    mc_s "Don't make this about us, Paz. Just don't."
    pa_s "It is about us!"
    pa_s "We're partners, we've got each other's backs, and you're shutting me out for what? Some one-man war against the world?"
    pa_s "Come on, [bro_r_low]."

    show ep02_partners07
    pa_s "Look, I don't know what's eating at you, but I can tell something's off."
    pa_s "Open up to me, [mc_name]. Let me in."
    mc_s "Just stop. Please, stop pushing, stop trying to fix me, and just let me handle my own shit. You got that?"
    pa_s "I keep thinking, [mc_name]. About all the bullshit we face, you know? Makes me question why we even try."

    show ep02_partners08
    mc_s "What are you getting at?"
    pa_s "When my [sis_r_low] got messed up, and the system did jack... That's when I knew. I had to do something, be something more."
    mc_s "And you think that badge actually changes anything?"

    show ep02_partners09
    pa_s "I gotta believe it does. Otherwise, what's the point, right?"
    mc_s "You sure about that? I used to think that way too. Now, I'm not so sure."

    show ep02_partners10
    pa_s "Don't you get it? I'm tired of fighting solo. This badge, it stands for something. It has to."
    mc_s "..."

    show ep02_partners11
    pa_s "My trust in the system might be shaky, but it's still there. It's the only way forward. Without it, what's left?"
    mc_s "Nothing. Not a damn thing."

    show ep02_partners12
    pa_s "My [si_full_r_low]... after what went down with her, I vowed to never let anyone feel that helpless again. The badge, it's a commitment, isn't it?"
    mc_s "Commitments get broken, Paz. All the damn time."

    show ep02_partners13
    pa_s "Not by me, [mc_name]."
    pa_s "And deep down, I don't think you break them either. You're just... lost right now."
    mc_s "Maybe."

    show ep02_partners14
    pa_s "Then let me help you find your way back. I've been in that dark place, thinking it's all pointless. But we're in this together."
    mc_s "You're a stubborn one, aren't you?"

    show ep02_partners15
    pa_s "Always have been. Got it from my [mo_r_low]. She hustled day in and day out for us, never asking for a thing in return."
    mc_s "Must be nice, having something to fight for."
    pa_s "You've got something too. You just gotta see it again. I'll help you, starting tonight..."
    mc_s "What are you talking about?"

    show ep02_partners16
    pa_s "Let's hit the town, knock back a few, talk a little shop. Nothing heavy, just two friends out on the town."
    mc_s "Paz--"
    pa_s "Come on, man. One drink ain't gonna kill you. Besides, you owe me for dragging my ass out on patrol during my break."
    mc_s "Alright, but only 'cause I owe you. Not like I had plans anyway."
    pa_s "Awesome! See, you can't brush me off that easily."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_mc_meet_arle




label ep02_mc_meet_arle:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.7)
    $ playAudio(sfx_evenstreet, "amb", 3, True, 2.5, 0)

    show ep02_dotonite1 with slowfade
    show doton_location zorder 2 with dissolve
    pause 4
    hide doton_location with dissolve
    pa_s "Here we are..."
    mc_s "Fuck, Paz!"
    mc_s "I forgot how packed these places can get."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.5)
    $ playAudio(sfx_nightclub, "amb", 1, True, 2.5, 0)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.2)
    $ playAudio(dotonbori_theme, "music", 2, True, 2.5, 0)

    show ep02_arlehost01 with slowfade
    pa_s "Well, yeah, this is the hottest spot in the district."

    show ep02_arlehost02
    "Host" "Welcome! Looking for a table? Someone special to chat with?"
    pa_s "He could use the company."
    mc_s "Paz, seriously..."
    "Host" "Okay, just follow me."

    $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=1, volume=1, fade_duration=1.5)

    show ep02_arlehost03
    pa_s "I'll be honest, [mc_name], I'm kinda jealous of you right now."
    mc_s "What are you on about?"

    show ep02_arlehost04
    pa_s "All these girls are checking you out, and you're barely noticing. You could have your pick of the room."
    mc_s "I don't see anyone looking my way."

    hide ep02_arlehost04
    pa_s "Then you must be blind as a bat."
    mc_s "Sometimes I forget you swing both ways. You're probably more interested in hooking up with a girl than watching my back."
    pa_s "Hey, I'm a multitasker!"

    show ep02_arlehost05 with hpunch
    $ rm.set_knows("arlette", True)
    arl "Good evening. I'm Arlette. May I join you?"
    pa_s "Hell yeah!"

    show ep02_arlehost06
    pa_s "You been hosting long, Arlette?"
    arl "This is my first night."
    show ep02_arlehost07
    pa_s "For real? Well, I'm sure you'll kill it."
    arl "Thank you. I'm glad to have your support."
    show ep02_arlehost08
    pa_s "You alright, Arlette? You seem a little... uneasy."
    arl "I'm fine. Just getting used to the atmosphere, that's all."
    show ep02_arlehost09
    pa_s "[mc_name]! Aren't you gonna say something to her? Don't be a jerk!"
    mc_s "Uh, you look nice tonight, Arlette."

    show ep02_arlehost10
    arl "Thank you."
    pa_s "She looks amazing! Her hair, her skin, her body..."
    pa_s "She's a total knockout, [mc_name]. Be nicer!"
    mc_s "Okay, okay, I get it. Arlette, my bad. I know I can be... distant."

    show ep02_arlehost11
    arl "It's quite alright, truly. I appreciate your kind words."
    pa_s "Wow, [mc_name]."
    pa_s "Maybe I should be worried about you instead of helping you meet new people."
    pa_s "You're hopeless."
    mc_s "Yeah, yeah. Chill out, Paz."

    show ep02_arlehost12
    "Host" "Can I get you anything to drink?"
    mc_s "Sure... this one. Looks good."
    pa_s "None for me, thanks."
    arl "Thank you, [mc_name]."
    show ep02_arlehost13
    mc_s "So, Arlette, what's your story?"
    arl "Huh?"
    show ep02_arlehost14
    arl "My story? What do you mean?"
    mc_s "You know, how you ended up here, what your dreams are, that kinda thing."

    show ep02_arlehost15
    arl "Oh, um, it's not very exciting, I'm afraid."
    arl "And I don't know if I should talk about it while I'm working."
    arl "You know the rules... I cannot talk about personal matters or about other clients' lives with anybody. I'm so sorry."
    mc_s "Alright, then don't tell me anything."

    show ep02_arlehost16
    arl "Excuse me, I need to freshen up. Will you excuse me for a moment?"
    pa_s "Go ahead, hon. We'll be here."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep02_arlehost17 with slowfade
    pa_s "[mc_name], seriously, what's your deal?"
    pa_s "You don't have to grill the poor woman. Just chill, will you?"
    mc_s "Uhm..."

    show ep02_arlehost18
    pa_s "Okay, listen up."
    pa_s "Arlette seems like a sweet girl. Try to behave yourself, alright?"
    mc_s "Paz, I know she's pretty, but I'm not interested in her."

    hide ep02_arlehost18
    mc_s "Besides, what do I need to talk to her about?"
    mc_s "She's a host. I'm not good at small talk anyway, so..."

    show ep02_arlehost19
    pa_s "Quit being a wimp and talk to her!"
    pa_s "She's gonna be back any second, and if you don't put in the effort, I swear to god, I'll whoop your ass myself."
    mc_s "Alright, alright... I'll try to make conversation."

    show ep02_arlehost20
    pa_s "Not everything has to be about sex, booze, and drugs, [mc_name]."
    pa_s "Try to step outside your comfort zone a bit."
    mc_s "Huh? I don't know what you're talking about."
    pa_s "Oh, don't play dumb. We both know you've got baggage, I'm not stupid."

    show ep02_arlehost21
    pa_s "But seriously, Arlette's not gonna bite you or anything. You've got nothing to be afraid of."
    pa_s "Remember, she's here to entertain guests, and that means talking to you, making you feel at ease, and maybe getting you to spend some cash, too."
    pa_s "Just keep that in mind, okay?"
    pa_s "Treat her with respect, and maybe she'll open up a little more."
    pa_s "Who knows, maybe you two will hit it off and become friends, hm?"
    mc_s "I don't get this whole hostess thing..."
    mc_s "I can't bang 'em, I can't touch 'em or anything, but I'm still supposed to flirt with 'em, or something? How's that make any damn sense?"

    show ep02_arlehost22
    pa_s "You've already had your fill of that kinda stuff. Now you got a chance to just be a person for a while."
    mc_s "I don't follow. What do you mean, just be a person?"
    pa_s "Exactly what I said, just be human."
    pa_s "Enjoy yourself, have fun, knock back a few, chat a little, then head home. You know, like a regular person would."
    mc_s "Just talking, huh? So, that's all you do with them?"
    pa_s "Yeah, that's it. Nothing else."
    mc_s "I still don't see the appeal."
    pa_s "Fine. I'll handle the rest of the night, but let me tell you something..."
    pa_s "It's a hell of a lot better than spending your whole night alone getting wasted in your shitty apartment."
    pa_s "Now shut your trap, she's coming back."

    show ep02_arlehost23 with slowfade
    arl "Sorry for taking so long."
    pa_s "It's okay, Arlette. This guy's still gonna take some time to warm up to you, I guess."
    arl "Why? What's wrong?"
    mc_s "Huh, nothing... Really, I don't even know why I'm here. This isn't really my scene."
    pa_s "I'll... be back. Don't have too much fun without me."
    mc_s "Huh? What?!"
    pa_s "I know you can be a gentleman, [mc_name]. Make me proud, alright?"

    show ep02_arlehost24
    mc_s "You doing okay, Arlette?"
    arl "Huh? Yeah!"
    arl "I think so."
    show ep02_arlehost25
    mc_s "I still don't really get how any of this works, honestly. I guess you'll have to break it down for me."
    arl "Guests come here and buy drinks from me so they can chat with me about anything they want."
    mc_s "I mean, that still doesn't sound all that exciting."
    arl "So, you've never been to a place like this before, huh? I mean, just to chat?"
    $ show_walkthrough("ep02_arlehost_menu1")
    menu:
        mc_t "Should I be straight with her? Or just bail on this situation?"
        "Tell the truth":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)

            mc_s "Yeah, but... never mind."
            arl "Alright, let me see."
            arl "How about this: you ask me a question, any question you want. After you do, I'll ask you a question back. Sound like fun?"
            mc_s "I guess. You're not going to tell me not to cross the line again, right?"
            arl "Sure, I'll cross the lines, too. That should make it fair for you."
            mc_s "Um, okay, I'll ask..."
        "Avoid answer":
            hide screen walkthrough_screen

            mc_s "Not really. Look, I'm not here to make friends or have heart-to-heart conversations."
            arl "Oh... I see. Well, I'm sorry if I made you uncomfortable."
            mc_s "It's fine. I just don't see the point in all this small talk."
            arl "I understand. But you know, sometimes it's nice to just connect with someone, even if it's only for a little while."
            mc_s "..."
            arl "How about this? Give me one chance to change your mind. If you still don't enjoy our conversation, you can walk away, no hard feelings."
            mc_s "Fine. One chance. But don't expect too much."
            arl "Deal. Now, let me think of a good question to start with..."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ playAudio(arlette_love_theme, "music", 1, True, 2.5, 0)

    show ep02_arlehost26 with slowfade
    mc_t "You never really know when a moment's gonna change you."
    mc_t "I didn't, not until Arlette walked into my life."
    mc_t "She was something else, that's for sure. There was something about her... a kinda sincerity you don't expect in places that trade on illusion."

    show ep02_arlehost28
    mc_t "We talked, really talked."
    mc_t "Not about the weather or the latest idol song, but about dreams, regrets, the hard truths we try to hide..."
    mc_t "The kind of things you don't share with just anybody, especially not in a host club."
    mc_t "She knew the rules, knew she wasn't supposed to get personal with clients. But there we were, breaking every one of them."

    show ep02_arlehost27
    mc_t "Arlette laughed at my jokes, shared stories of her own, and for a night, it felt like we'd known each other forever."
    mc_t "The music, the lights, the noise, it all faded away. It was just us, lost in time."

    show ep02_arlehost29 with dissolve
    mc_t "Paz watched us, a silent guardian angel with a touch of envy in her eyes."
    mc_t "Couldn't tell if it was for me or for Arlette. Maybe both."

    show ep02_arlehost30 with dissolve
    mc_t "But it didn't matter."
    mc_t "Arlette made me feel... human."
    mc_t "Like I had value, that I mattered."
    mc_t "That maybe I wasn't just a worthless piece of shit who couldn't save anyone."
    mc_t "I'd forgotten what it felt like. Forgotten what it felt like to dream, to hope."
    mc_t "She brought that back, along with so many other things."

    show ep02_arlehost32
    mc_t "I saw her again, night after night."
    mc_t "It wasn't about the drinks or the company anymore."
    mc_t "It was about seeing her face, hearing her laugh, sharing those moments that changed us both."
    mc_t "She made me want to be a better person, to fight for something instead of wallowing in misery and regret."

    show ep02_arlehost31 with slowfade
    mc_t "All my past filled with drugs, whores, and alcohol disappeared."
    mc_t "It all seemed so trivial compared to what I felt for Arlette."
    mc_t "She brought something I thought was gone forever, something I thought I'd never have again - a second chance."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_arle_past




label ep02_arle_past:
    scene eigengrau with dissolve
    $ playAudio(sfx_beach, "amb", 1, True, 2.5, 0)

    show ep02_arlestory01 with slowfade
    show taniwa_location zorder 2 with dissolve
    pause 4
    hide taniwa_location with dissolve
    mc_t "So there we were, at Taniwa beach, the city behind us and the ocean in front."
    mc_t "Never thought I'd find silence in Osaka, but with Arlette, silence spoke louder than anything."

    show ep02_arlestory02
    mc_t "Walking alongside Arlette was a whole different ballgame."
    mc_t "All her attention was on me, no host club tricks or superficial charm. We were just... being with each other."

    $ stopAudio(channel="amb", subchannel=1, fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_beach2, "amb", 2, True, 2.5, 0)
    scene eigengrau with dissolve
    show ep02_arlestory03 with circlewipe
    mc_t "Even though we'd already talked a lot about each other, I asked Arlette once again."
    mc_s "Arlette, how'd you end up doing this for a living?"
    arl "You really curious about that?"
    mc_s "I, well, uh..."
    arl "I'm just messing with you. To be honest, I'm still trying to figure it out myself."
    mc_s "Why don't you do something you actually like for a living?"
    arl "It's... complicated."
    mc_s "Complicated how? I mean, you're smart, talented, beautiful... you could do anything you wanted."

    show ep02_arlestory04
    arl "Yeah, I've heard that before. You know, I wasn't always like this... a host, I mean."
    arl "Back in Paris, life was full of freedom..."
    mc_s "What brought you from Paris to... this? If you don't mind me asking."

    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    $ playAudio(arlette_nostalgia_theme, "music", 1, True, 2.5, 0)

    show ep02_arlestory05 with slowfade
    arl "I grew up in Paris, you know. My parents had this little café near Montmartre, all artsy and alive."
    arl "After school, I'd be there sketching people, dreaming of becoming a fashion designer or a painter."
    arl "It was... magical."
    mc_s "Sounds nice."

    show ep02_arlestory06 with slowfade
    arl "It was. Until I was fifteen."
    arl "This one car crash... just like that, no more parents."
    arl "Just me and my [gra_r_low]."
    mc_s "I'm sorry."

    $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)

    show ep02_arlestory08
    arl "It's okay, really."
    arl "They say time heals all wounds, and that's true."
    arl "After the accident, it was just me and [gra_r_low], you know?"
    arl "We kinda clung to each other, trying to make sense of it all."
    arl "She taught me everything I know: cooking, cleaning, sewing, you name it."
    arl "I was there for her, and she was there for me."
    mc_s "What about the café?"
    arl "We lost it. Everything."
    arl "There were debts, paperwork, legal stuff, and in the end, we just didn't have the money to keep it going."
    arl "So I got this idea in my head, fueled by the fashionistas at the café, that I could be a model, even make it big."
    arl "Yeah, I know, dumb, but..."
    mc_s "It's not dumb. You wanted to do something to help, right? But... Osaka? How'd you end up here?"

    show ep02_arlestory07
    arl "Well, the modelling thing didn't work out. Not for me, at least."
    arl "But there was this photographer, a regular back home, always raving about Japan's entertainment scene. Made it sound like a land of opportunity."
    arl "And I was desperate, you know? Ma Mamie was getting sick, and we didn't have insurance or anything."
    arl "So I decided, what the hell, and packed up and left. Landed in Osaka, started modelling, and it was great, for a while."
    mc_s "So, you both just packed up and left?"

    show ep02_arlestory09
    arl "Yeah. It was... nice, I guess."
    arl "A fresh start, you know? New country, new life, no debts or problems following me..."
    arl "But turns out, Osaka didn't care much for a French girl trying to make it as a model."
    arl "I started to fall into debt, my [gra_r_low] started getting worse, and she had to be hospitalized."
    arl "They told me she needed surgery, but I didn't have enough. So, I started doing whatever I could to make ends meet, modelling wasn't cutting it anymore."
    arl "I took a roommate, cut my expenses, and did whatever I could. But the bills just kept coming, and I knew I couldn't keep it up."
    show ep02_arlestory10
    mc_s "Is she okay? Your [gra_r_low], I mean."
    arl "Yeah, she's okay. They caught it in time, and she's doing better..."
    show ep02_arlestory11
    mc_t "It was strange, hearing her talk about her past, her real past."
    mc_t "I started to feel like we were connected somehow, that our lives weren't that different."
    mc_t "Two people struggling to find their way..."

    show ep02_arlestory12
    arl "I don't usually share this much. With anyone."
    mc_s "Why me then?"
    arl "Because I think you see the world like I do... a bit broken, a bit beautiful."
    mc_s "Broken, sure. But beautiful? I'm not so sure."
    arl "Maybe you just needed someone to point it out."
    mc_s "And that's you? My guide to the broken beauty?"

    show ep02_arlestory13
    arl "I don't know, you tell me."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_arle_mc_sex




label ep02_arle_mc_sex:
    scene eigengrau with dissolve
    show ep02_arlehotel19 with slowfade
    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_beach2, "amb", 2, True, 2.5, 0)
    arl "I never thought a day like this would come."
    mc_s "What are you talking about?"

    $ setChannelVolume(channel="amb", subchannel=2, volume=0.1, fade_duration=2.5)

    show ep02_arlehotel01
    arl "The day I could trust someone with my mind, my soul, and now... my body."
    $ playAudio(arlette_theme, "music", 1, True, 2.5, 0)

    show ep02_arlehotel02
    arl "I'm all yours, [mc_name]. You can do whatever you want with me. I won't stop you."
    mc_s "Are you sure about this, Arlette? I mean... are you ready for this?"
    arl "I should be asking you the same thing. I know you've been waiting for me, and I'm so grateful for that."
    show ep02_arlehotel03 with vpunch
    arl "Come here, you..."
    arl "I can't wait any longer, and you shouldn't hold back either. There's no reason to."
    show ep02_arlehotel04 with vpunch
    mc_s "You... are so beautiful."
    arl "And you've been waiting for this moment, haven't you?"
    mc_s "I might have pictured it a few times, yeah."
    arl "And what exactly were you picturing?"
    show ep02_arlehotel05 with vpunch
    mc_s "You, underneath me, just like this."
    arl "So you were dreaming about being with me, huh."
    $ show_walkthrough("ep02_arlehotel_menu1")
    menu:
        "I thought about it a few times":
            hide screen walkthrough_screen

            mc_s "I... I mean, yeah, I thought about it a few times. But I didn't want to pressure you or anything."
            arl "That's very sweet of you, [mc_name]. But you don't have to hold back anymore."
        "Yeah, I was...":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)

            mc_s "Y-Yeah, I was..."
            arl "I made you wait quite a while, didn't I? Did you fantasize about me like this often?"
        "I've jerked off thinking about you.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)

            mc_s "You have no idea how many times I've gotten off thinking about you, Arlette."
            arl "Oh, you naughty boy. I guess I'll have to take responsibility for all that pent-up desire."
    show ep02_arlehotel06 with hpunch
    mc_s "Yes..."
    arl "Aww, I'm sorry babe. Let me make it up to you."
    show ep02_arlehotel07
    arl "AHH...!"
    arl "You fill me so nicely."
    mc_s "Oh Arlette..."

    show ep02_arlehotel08
    arl "Yeah, like that."
    arl "Fuck me, do me hard."
    show ep02_arlehotel09
    arl "Harder!"
    arl "Ah... hmh..."
    show ep02_arlehotel10
    arl "Getting distracted?"
    mc_s "I'm sorry, but they're so big and perfect."
    arl "Do you like them?"
    show ep02_arlehotel11
    mc_s "How could I not?"
    arl "Oh God... go on!"
    mc_s "Arlette! You're so tight."

    show ep02_arlehotel12
    arl "Ahhh!"
    arl "This feeling ... You feel good! You're making me crazy."
    arl "I... I want more."
    show ep02_arlehotel13
    mc_s "You're so fucking hot... I can't hold it in."
    arl "I want your cum. But please, [mc_name], don't cum inside me."
    mc_s "Fuck! Fuck! I'm cumming!"

    show ep02_arlehotel14 at concentrate
    $ show_walkthrough("ep02_arlehotel_menu2")
    menu:
        "Cum on her face":
            hide screen walkthrough_screen
            $ ep02_beachcum += 1
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)
            pass
        "Cum on her tits":
            hide screen walkthrough_screen
            $ ep02_beachcum += 2
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            pass
    show ep02_arlehotel15 with flash
    show white zorder 1.0 at ejaculation_flash
    mc_s "Hah! Ah! Arlette!"
    arl "Hmm... So warm."
    show ep02_arlehotel16
    arl "It's a lot ..."
    arl "Lucky me."
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_arlehotel17 with slowfade
    arl "Come lie down next to me."
    arl "I want to feel you close."
    mc_s "Hmmm..."
    arl "What, are you surprised that I want to cuddle with you?"
    show ep02_arlehotel18
    mc_s "We're not exactly cuddling at the moment..."
    arl "Not yet, we're not. But we're not done having fun..."
    if ep02_beachcum ==2:
        arl "Come, put your head on my boobs."
    else:
        arl "Kiss me."
    mc_s "But you've got a little..."
    arl "Oh, right. Things got a bit messy, huh."
    arl "Give me a second to freshen up, mon amour."
    scene eigengrau with dissolve
    show ep02_arlehotel20 with circlewipe
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.6, fade_duration=2.5)
    arl "I've never felt so... so free before. Not since Paris."
    mc_s "I feel it, too."
    arl "Maybe... Maybe this is our chance."
    mc_s "To start over."
    arl "Yes."
    show ep02_arlehotel21
    arl "Tout est possible avec nous..."
    mc_s "I-- I... don't speak french."
    arl "[mc_name], may I stay like this a little longer?"
    $ show_walkthrough("ep02_arlehotel_menu3")
    menu:
        "You mean in lingerie?":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)

            mc_s "You mean in lingerie?"
            arl "No, silly. Just with you."
            mc_s "I won't stop you."
        "I wouldn't mind if you stayed in less":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)

            mc_s "I wouldn't mind if you stayed in even less clothing, or none at all."
            arl "Oh, [mc_name], tu es un vilain garçon. I like that about you."
            mc_s "What? I guess you liked what I said, since you're not mad at me."
        "Stay as long as you like.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)

            mc_s "Stay as long as you like, Arlette. I'm happy just being with you."
            arl "You're so sweet, [mc_name]. I feel so safe when I'm with you."
            mc_s "That's because you are loved, Arlette. Very much so."

    $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)

    mc_t "Just like that, a phone call yanked her away from me."

    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2, fade_duration=2.5)

    show ep02_arlehotel22
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)

    mc_t "I didn't even have to ask."
    mc_t "Her voice, her face - it was written all over."
    mc_t "Something bad had gone down."
    mc_t "The way she was acting, I knew it had to be about her [fm_r_low]."
    mc_t "And her [gra_r_low]'s the only [fm_r_low] she's got left."

    scene eigengrau with dissolve
    show ep02_arlehotel23 with slowfade
    arl "That was Rina... Ma Mamie collapsed. She's in the hospital."
    arl "I-- I gotta go. I gotta be there for her."
    mc_s "You want me to come with you?"
    arl "I-- I just can't lose her, [mc_name]... She's all I have."
    mc_s "I'm coming with you, Arlette. No way I'm letting you deal with this alone."
    arl "I'm sorry. I shouldn't be dumping all this on you... You always do so damn much for me and... and I just--"
    mc_s "Hey, cut that out. You got nothing to apologize for."
    arl "Thank you, [mc_name]. Thank you."
    mc_s "C'mon, let's get moving. Every minute counts."
    arl "[mc_name]..."
    arl "Je t'aime..."
    arl "... Thank you."
    $ unlock_memory("m_ep02_hotel")
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_grandma




label ep02_grandma:
    scene eigengrau with dissolve
    show ep02_hospital1 with slowfade
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.8)
    $ playAudio(sfx_japansirens, "amb", 3, True, 2.5, 0)

    mc_t "On the drive to the hospital, my mind was spinning out. Something about Rina's call just didn't add up."
    mc_t "I've always had this hunch that she was bad news, but Arlette's got a total blind spot when it comes to her so-called friend."
    mc_t "I should've seen this coming."

    $ stopAudio(channel="amb", subchannel=3, fadeout=1.5)

    show ep02_hospital2 with slowfade
    $ setChannelVolume(channel="amb", subchannel=4, volume=1)
    $ playAudio(sfx_hospital_hall, "amb", 4, True, 2.5, 0)

    mc_t "Seeing her [gra_r_low] like that, all frail and fading... it was a harsh reality check."
    mc_t "I couldn't help it, I blurted out..."
    mc_s "You gotta break free from all this."
    mc_t "But shit, that was a dumb move. I totally put my foot in my mouth."
    rin "Are you for real right now, [mc_name]?"
    show ep02_hospital3
    mc_s "I am, Rina..."
    mc_s "C'mon, Arlette, you can't keep going like this. It's eating you alive."
    mc_t "The second those words left my mouth, I knew I'd fucked up."
    mc_t "It was like I'd lit a match and tossed it straight into a powder keg."
    mc_t "All her anger, all her frustration, it just exploded out..."
    arl "Eating me alive?"
    arl "You don't know what the hell you're talking about."
    mc_s "I know exactly what I'm talking about."
    mc_s "You're stuck in this vicious cycle, Arlette."
    mc_s "The debt, the desperation - it's a trap. You've gotta break free, get out while you still can."

    show ep02_hospital4
    arl "You say that like it's so damn simple. But it's not, not for me."
    arl "You don't understand."
    mc_s "Then help me understand. We can figure this out, together."
    mc_s "I'm here for you."

    show ep02_hospital5 with vpunch
    arl "And how exactly are you gonna help me, huh?"
    arl "By buying me a few drinks and letting me vent?"
    show ep02_hospital6
    arl "Wake up, [mc_name]. I need the money. I need the tips."
    arl "I don't have a choice!"
    hide ep02_hospital6
    mc_s "There's always another way. We'll find it. I promise you that."
    arl "Don't make promises you can't keep, [mc_name]. Just drop it, alright?"
    mc_s "Drop it? Drop you? Is that what you want?"

    show ep02_hospital7 with hpunch
    arl "[mc_name], stop. Just stop!"
    arl "This is my life we're talking about here. My choices. Don't you dare tell me what to do."
    mc_s "I'm just trying to help, Arlette. I care about you."
    arl "Maybe you should take a good hard look at yourself, [mc_name]."
    arl "Maybe you should focus on your own damn problems before you start lecturing me about mine."
    show ep02_hospital8 with slowfade
    mc_s "Arlette, please--"
    mc_t "Damn. I really screwed that up."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_arle_hell




label ep02_arle_hell:
    scene eigengrau with dissolve
    show ep02_temptation1 with slowfade
    $ playAudio(sfx_japancrossing, "amb", 1, True, 2.5, 0)
    rin "Arlette, honey, you need to chill out. It's all gonna work out, you'll see."
    show ep02_temptation2
    arl "I don't know, Rina."
    arl "I just... I feel like I've screwed everything up so bad."
    rin "Don't even go there."
    rin "You're smart, you're talented, and you're fucking gorgeous. You're gonna be just fine."
    rin "Maybe what you really need is a big change, you know? A fresh start."
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.5, fade_duration=4)
    $ playAudio(arlette_sad_theme, "music", 1, True, 2.5, 0)

    show ep02_temptation3
    arl "What, like quit the club? Try to get a normal job?"
    rin "Not exactly."
    rin "Just... you know, switch things up a bit."
    rin "Make some changes. Changes that'll put more cash in your pocket, if you know what I mean."
    arl "Changes like what?"
    rin "You're hurting for money, right?"
    rin "And you're sick of the same old grind at the club."
    rin "Well, there's another way to bring in steady cash without busting your ass every single night."
    arl "How?"
    show ep02_temptation4
    rin "You remember that friend I mentioned?"
    rin "He can make all your debt just... disappear."
    rin "All you gotta do is... give him what he wants."
    arl "Which is?"
    rin "Sex, Arlette. Sex."
    arl "Oh. You mean like... being a prostitute? Like what you do?"
    rin "Hey, it's not as bad as you think."
    show ep02_temptation5 with slowfade
    rin "Believe me, once you get the hang of it, it's like fucking printing your own money."
    arl "I-- I don't know if I can do that."
    rin "What about your [gra_r_low]?"
    rin "Don't you want to help her out? You know she's barely getting by."
    arl "Of course I do! But--"
    rin "Listen, I'll have a chat with my friend."
    rin "Set up a little meeting."
    rin "You don't have to decide anything right now. Just... think it over, okay?"
    rin "Do it for your [gra_r_low], if nothing else."
    show ep02_temptation6
    arl "I don't know, Rina. This is a lot to take in."
    arl "I need some time to wrap my head around it."
    rin "Hey, I get it. It's a big decision."
    rin "But just remember, this could be your ticket out of all this bullshit. A way to finally get ahead."
    arl "I'll think about it. But I'm not promising anything."
    rin "That's all I'm asking, babe. You think about it, and I'll make some calls."
    rin "We're gonna get you out of this mess, one way or another."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_escort01 with ccirclewipe
    mc_t "I didn't know back then, but I could feel it in my gut, something was off."
    mc_t "Arlette, she had this look on her face, like she was about to make a choice that would change everything."
    arl "Is this really happening?"
    arl "Am I actually about to sell my body for money?"
    arl "Is this the only option I have left?"
    arl "No, no, I can't go through with this. This isn't who I am, I'm not a prostitute, I'm not--"
    show ep02_escort02 with hpunch
    rin "You ready to go, Arlette? We gotta bounce."
    arl "Oh, um, yeah. Sure."
    show ep02_escort03
    arl_t "I want him to reach out, to stop me from making a mistake I can't take back."
    arl_t "I hope, pray, that he senses something is wrong, that he'll call or text, give me a reason to turn back."
    arl_t "Why is my phone silent?! I don't want to face this alone."

    show ep02_escort03 with vpunch
    rin "Let's go!!"
    arl_t "I'm sorry, [mc_name]. I hope you can forgive me."
    arl_t "But I have to do this. For my [gra_r_low]. I just pray this isn't the end for us."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_room_noise3, "amb", 1, True, 2.5, 0)

    show ep02_escort04 with ccirclewipe
    $ playAudio(yakuza_theme, "music", 1, True, 2.5, 0)
    yas "Welcome ladies..."
    rin "Thank you, baby."
    yaw "Alright, let's get down to business."
    arl "Um..."
    show ep02_escort05
    rin "Just let him do the talking, Arlette. Follow his lead."
    arl "Okay..."
    show ep02_escort06 with slowfade
    yaw "You see, Arlette, in our line of work, what you know can tie you down just as much as any contract."
    yaw "Once you're in on certain things, there's no turning back."
    yas "We've got a proposition for you, Miss Arlette."
    yas "We're willing to wipe out your debts in exchange for your... services."
    arl "Services? What kind of services?"
    rin "Arlette...!"
    show ep02_escort07
    yas "Surely you know what our business entails."
    yas "You'd be providing companionship and sexual favors to clients, both here and abroad."
    arl "Abroad?"
    yas "That's right."
    yas "We've got connections all over Asia and beyond."
    yas "We'll set you up with luxury digs, access to the best restaurants and clubs, and of course, a generous compensation package."
    arl "Who... who the hell are you people?"
    rin "Arlette!!!"
    rin "I'm sorry, I apologize for my friend's behaviour."
    show ep02_escort08
    yas "That's none of your concern, Miss Arlette. All that matters is whether you're in or out."
    arl "So if I..."
    arl "If I say yes, my debts are gone? I can pay off my [gra_r_low]'s bills and start fresh?"
    yaw "You got it."
    arl_t "What am I doing?"
    arl "And all I have to do is... is...?"
    $ unlock_memory("m_ep02_revelation")

    show ep02_escort09
    yas "In simple terms, Miss Arlette, you'll become an high-end escort for us."
    yas "We have a strict code of conduct, of course."
    yas "We take good care of our girls, and we expect the same in return." 
    show ep02_escort10
    arl "But... But what if I don't want to do this anymore? What if I want out?"
    yaw "Decide?"
    yaw "Oh, the luxury of choice isn't a given in our world. Consider this a... lifelong commitment."
    yaw "You understand, Arlette, sitting at this table, hearing what you've heard, it's as binding as any signature."
    yaw "There's no going back now. In our eyes, you're already involved, and that... that changes everything."
    show ep02_escort11
    arl_t "Holy fucking shit..."
    rin "Just say yes, Arlette. This is your shot. Don't blow it."
    arl_t "Fuck, fuck, fuck... this can't be happening..."
    arl_t "I can't do this, I just can't."
    arl_t "But... what other choice do I have? What else can I do? Fuck, fuck, fuck."
    arl "I-- I don't know--"
    yaw "Alright."
    yaw "Show it to her."
    show ep02_escort12
    arl "What the hell is this?"
    yas "Open it."
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ playAudio(sfx_heartbeatfast, "sfx", 1, True, 0.5, 0)

    show ep02_escort13 with vpunch
    arl "Mon Dieu... ma grand-mère! [mc_name]! Us..."
    arl_t "I've never felt so helpless, so betrayed, so... broken."
    arl_t "How the fuck did I end up here? How did I let this happen?"
    arl "I..."
    arl "Rina... I--"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)
    $ playAudio(sfx_femalerun, "sfx", 2, True, 0.5, 0)

    show ep02_escort14 with hpunch
    arl "I-- I can't do this. I'm-- I'm sorry."
    rin "Arlette! Come back here!"
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1)
    $ playAudio(sfx_punch, "sfx", 3, False, 0, 0)

    show ep02_escort15 with hpunch
    yas "Hey! What are you--"
    arl "Get your fucking hands off me!"
    rin "Arlette, just do it! Please, don't fuck this up for me."
    show ep02_escort16
    arl "Fuck you, Rina! And fuck these bastards, too!"
    scene eigengrau with dissolve
    show ep02_escort17 with slowfade
    yas "She'll be back. They always come back."
    rin "And if she doesn't?"
    yaw "Then we'll make her regret it. No one walks away from us. No one."
    rin "Shit, what have I done?"
    rin "Hey, guys, I'm sorry... I'm so sorry."
    yas "Yeah... you will be."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_nightroad, "amb", 4, True, 2.5, 0)
    $ playAudio(sfx_windyprairie, "amb", 5, True, 2.5, 0)

    show ep02_sadness1 with circlewipe
    mc_t "Hours had passed since Arlette's call, and the worry was starting to eat at me."
    mc_t "I paced back and forth, my mind racing, trying to come up with a plan."
    arl "[mc_name]..."
    $ setChannelVolume(channel="music", subchannel=1, volume=0.4)
    $ playAudio(arlette_sad_theme, "music", 1, True, 2.5, 0)

    show ep02_sadness2 with hpunch
    mc_s "Arlette, what the hell? Are you alright? What happened?"
    arl "It's... it's all fucked up, [mc_name]. Everything. I'm in deep shit."
    mc_s "Just tell me what you need. Anything, I mean fucking anything at all."

    show ep02_sadness3
    arl "I... I can't do this anymore, [mc_name]."
    arl "I can't be a fucking sex worker, a prostitute. It's not me, it's not who I am."
    arl "I need to get the fuck away from these sick bastards, this entire fucking nightmare."
    mc_s "Whoa, slow down. What guys?"
    mc_s "Arlette, you're not... you're a hostess, right?"

    show ep02_sadness4
    arl "Yeah."
    arl "A fucking hostess."
    arl "And they offered me more, so much more than just... just being a hostess."
    arl "And I... I almost said yes."
    arl "God, what's wrong with me?"
    mc_y "Goddamn, Arlette. Fuck!"
    arl "[mc_name], I don't have anywhere to go."
    arl "I can't go back to my place, can't go back to that fucking club. I'm stranded."
    arl "You... you're all I've got."
    mc_s "Hey, listen to me. You're safe with me. Okay?"
    mc_s "I'm here. Whatever this shit is, you can count on me."

    show ep02_sadness5
    arl "Really? You mean that?"
    mc_s "Really. Now, what do you want to do?"
    arl "I... I don't know. God, I don't know."
    mc_s "First things first, let's get you the hell out of here."
    mc_s "We'll go to my place, lay low, and figure this shit out."
    mc_s "Together..."

    show ep02_sadness6
    arl "Okay."
    mc_t "As I looked at her, I couldn't shake the feeling that this was just the beginning."
    mc_t "Whatever Arlette had gotten herself into, it was big. And dangerous."
    mc_s "Don't worry, Arlette. We'll get through this. I promise."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep02_lovemaking




label ep02_lovemaking:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=7, volume=0.2)
    $ playAudio(sfx_eveningtraffic, "amb", 7, True, 2.5, 0)

    show ep02_arlesex01 with ccirclewipe
    mc_s "God, Arlette, you're so fucking beautiful. So, so beautiful."
    arl "But..."
    mc_s "Shh, no buts. Just be here with me, in this moment."

    show ep02_arlesex02
    arl "I think... I think I'm in love with you, [mc_name]. I really am."
    mc_s "I-- I think I love you too, Arlette."
    mc_s "You make me feel... human."
    mc_s "Like I'm not some worthless piece of shit, like I'm not a total fuck-up."
    mc_s "Like there's hope."

    show ep02_arlesex03 with vpunch
    arl "You're the best thing that's ever happened to me, [mc_name]. And I want to be with you, no matter what it takes."
    arl "I'm just... I'm just worried about my [gra_r_low]."
    arl "Those bastards know who she is, where she is, and they could use her to get to me."
    arl "I can't let that happen, [mc_name]. I just can't."
    mc_s "I know, Arlette. I know."
    mc_s "We'll figure this out, okay? We'll fix this, somehow."

    show ep02_arlesex04
    arl "They know about you too, [mc_name]."
    arl "They saw us together, saw... everything."
    arl "They could hurt you too."
    mc_s "Don't worry about me, Arlette."
    arl "You're not tough enough to take on these guys. These people are dangerous, [mc_name]. And I don't want to drag you into danger too."
    arl "I can't do that to you."
    mc_s "We'll figure it out. We'll come up with a plan. And we'll keep your [gra_r_low] safe."
    mc_s "I promise."
    arl "Okay. I'm sorry for pulling you into this shitshow, [mc_name]."
    mc_s "It's okay. I'm just glad you're safe."

    scene eigengrau with dissolve
    show ep02_arlesex05 with circlewipe
    mc_s "You alright, Arlette?"
    arl "Mmm hmm, I'm fine. I'm... I'm just thinking, you know?"
    mc_s "Yeah, I get it. This shit is pretty fucking stressful."
    arl "[mc_name]... uh... could you... would you mind... maybe, um..."
    mc_s "Come on, Arlette. Whatever it is, just say it. It's okay."

    show ep02_arlesex06 with vpunch
    arl "Could you... uh..."
    arl "I mean... Would you mind..."
    arl "... Fucking me..."
    arl "... In the ass?"
    arl "Please?"
    mc_s "Uh..."

    show ep02_arlesex07 with hpunch
    arl "I'm sorry, it's just... I need you to fuck me in the ass."
    mc_s "[renpy.substitute(dialogues['E01S24_d046'])]"
    mc_s "[renpy.substitute(dialogues['E01S24_d052'])]"
    arl "I know it's sudden, but it's something I really need."
    arl "Right now, I mean..."
    arl "I don't know, I just... I feel like... if you fuck me in the ass, I can escape for a minute, you know?"
    mc_s "Escape?"

    show ep02_arlesex08
    arl "Yeah. From everything."
    arl "Just for a little while, I want to forget."
    show ep02_arlesex09
    arl "And anal sex is... it's so intense, so deep, so... liberating."
    arl "I know it sounds crazy, but... I don't know, maybe you could just do it for me?"
    $ show_walkthrough("ep02_arlesex_menu1")
    menu:
        "Agree":
            hide screen walkthrough_screen
            $ ep02_anal = True
            $ rm.update("arlette", "cor", 5)
            $ check_levels("arlette", "cor", 5)

            show ep02_arlesex10
            mc_s "Well, shit, I mean... If that's what you want, I can definitely do that for you."
        "Deny":
            hide screen walkthrough_screen

            mc_s "Sorry... I can't."

    show ep02_arlesex11
    if ep02_anal:
        arl "Yes! Thank you, [mc_name]! You have no idea what this means to me."
        mc_s "Hey, if it helps you feel better, even for a little bit, I'm all for it. I'd do anything for you, Arlette."
    else:
        mc_s "I mean, I really wouldn't feel comfortable doing that... I see you with different eyes... and, uh, just don't ask me again."
        arl "Oh.. It's alright. Sorry for asking."
        jump ep02_arlette_mc_story


    show ep02_arlesex12 with vpunch
    arl "I know you would, [mc_name]. That's why I love you so fucking much!"
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    $ playAudio(arlette_sexy_theme, "music", 1, True, 2.5, 0)

    show ep02_arlesex13
    mc_s "Ready, Arlette?"
    arl "Yeah, just fuck me in the ass, [mc_name]! Fuck me in the ass, please!"
    show ep02_arlesex14
    arl "C'est bon, [mc_name]? Do you want my ass, [mc_name]? C'est l'heure!"
    mc_s "I don't know what you're saying, but... Fuck yes!"

    show ep02_arlesex16 with hpunch
    mc_s "Fuck, Arlette, you're so tight..."
    mc_s "Can't even fit my cock in..."
    arl "Sssh!"
    mc_s "Maybe we need some extra lub--"

    show ep02_arlesex15 with vpunch
    arl "No! Just fuck me already!"
    mc_s "Fuck Arlette... it's so tight in there..."

    show ep02_arlesex17
    arl "Hmngg... Mmph... mph... hmgg..."
    mc_s "Are you... alright, Arlette?"
    arl "Oh god, deeper... I need you deeper in my ass!"
    show ep02_arlesex18
    arl "Ah... c'est trop bon!"
    arl "Talk dirty to me, [mc_name], I want to hear how much you enjoy fucking my ass!"
    mc_s "W--What am I supposed to say?"

    show ep02_arlesex19
    arl "Anything!"
    arl "Tell me how much you're enjoying pounding my ass!"
    arl "Tell me what it feels like, tell me how dirty my asshole feels around your cock!"
    arl "Treat me like a real bitch, [mc_name]! Take out all your dirty thoughts and tell me!"
    $ show_walkthrough("ep02_arlesex_menu2")
    menu:
        "Talk dirty":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            $ ep02_talkdirty = True

            mc_s "You want me to take out my thoughts on you?"
            mc_s "Fine! You wanna feel like a real bitch, do you? I'm gonna treat you like one, Arlette!"
        "Talk with love":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)
            pass
    show ep02_arlesex20
    if ep02_talkdirty:
        arl "Oh oui, oui! S'il vous plait!"
        mc_s "Look at you... This is what you are, a lustful bitch!"
        arl "Oh, putain, tu me fais mal, mais c'est incroyable...!"
    show ep02_arlesex21
    if ep02_talkdirty:
        arl "Ahh..."
        arl "How rough ..."
        arl "C'est bon... Baise-moi!"
        mc_s "Can't help getting kinky, huh? You fucking slut!"
        arl "AHHH!"
        arl "D-damn... That feels good..."
        arl "It hurts a lot but... it also feels good!"
    show ep02_arlesex23
    if ep02_talkdirty:
        $ ep02_talkdirty = False
        $ show_walkthrough("ep02_arlesex_menu3")
        menu:
            "Keep talking dirty":
                hide screen walkthrough_screen
                $ rm.update("arlette", "cor", 2)
                $ check_levels("arlette", "cor", 2)
                $ ep02_talkdirty = True

                mc_s "What sort of a slut does something like that, huh?"
                arl "Ooh, pardonne-moi! S'il vous plaît, pardonne-moi!"
            "Talk with love":
                hide screen walkthrough_screen
                $ rm.update("arlette", "trust", 1)
                $ check_levels("arlette", "trust", 1)
                pass
    else:
        $ show_walkthrough("ep02_arlesex_menu4")
        menu:
            "Talk dirty":
                hide screen walkthrough_screen
                $ rm.update("arlette", "cor", 1)
                $ check_levels("arlette", "cor", 1)
                $ ep02_talkdirty = True

                mc_s "What sort of a slut does something like that, huh?"
                arl "Ooh, pardonne-moi! S'il vous plaît, pardonne-moi!"
            "Keep talking with love":
                hide screen walkthrough_screen
                $ rm.update("arlette", "trust", 2)
                $ check_levels("arlette", "trust", 2)
                pass
    show ep02_arlesex24
    if ep02_talkdirty:
        mc_s "I told you I don't know what you're saying, but your words sound sexy as fuck!"
        arl "D-Don't ... m, make me cum, [mc_name]!"
        mc_s "A--are you close...?"
        arl "Turn around... I wanna see your face when I cum from taking it up my ass."
    scene eigengrau with dissolve
    show ep02_arlesex25 with vpunch
    arl "Ugh! It's sliding in all the way in!"
    if ep02_talkdirty:
        arl "Yeah... like that. This is the best position to get my ass reamed."
    show ep02_arlesex26
    if ep02_talkdirty:
        arl "Like it, baby?"
        arl "Love the feel of a French girl's tight little asshole?"
        mc_s "Yes!"

    show ep02_arlesex27
    arl "Mmmmmmmhh!"
    arl "Aahhh!"
    arl "Your dick's so big it's hitting deep inside my stomach!"
    arl "My pussy's squeezing it tight, too !"
    show ep02_arlesex28
    mc_s "Oh... ah... uuhh..."
    arl "My asshole is getting worn out...!"
    show ep02_arlesex29
    arl "I can feel myself breaking down!"
    arl "Keep fucking me! Make me cum, make me cum!"
    show ep02_arlesex30 with flash
    show white zorder 1.0 at ejaculation_flash
    arl "C'est trop bon..."
    arl "Baise-moi!!! Prenez-moi!!! Prenez-moi!!!"
    arl "Plongez-la en moi!!! Au plus profond!!"
    arl "M... Mi... C..."
    arl "Ohh! Cum... Cumming!"
    arl "Hmmm... C--cumming!"
    show ep02_arlesex31
    arl "Yes... love it... cum... cumming, yeah... love it!"
    mc_s "Fuck! Did I break you?"
    arl "Ah! Ahhh..."
    arl "It hurts..."
    show ep02_arlesex32
    arl "It's burning... It's on fire..."
    arl "It hurts so much but..."
    arl "It feels so good at the same time..."
    arl "So embarrassing..."
    mc_s "Want me to pull out?"
    arl "Oh, no. Please... keep going... don't pull out... pound my ass, please!"
    show ep02_arlesex33
    arl "Your wish is my command"
    arl "Ugh. Mm, it's so big, ahh, you're so rough! Love it!"
    arl "Pound me so much I can't stand..."
    arl "Break me!"
    mc_s "I... I'm close, Arlette."
    arl "Cum where you want, babe..."
    $ show_walkthrough("ep02_arlesex_menu5")
    menu:
        mc_t "Sh, should I...?"
        "Cum inside her":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 2)
            $ check_levels("arlette", "cor", 2)

            mc_s "I'm gonna... I'm gonna cum inside..."
            arl "Yes... Yes, cum inside!"
            jump ep02_lovemaking_inside


        "Cum all over her ass":
            hide screen walkthrough_screen
            $ rm.update("arlette", "cor", 1)
            $ check_levels("arlette", "cor", 1)
            jump ep02_lovemaking_over




label ep02_lovemaking_inside:
    $ AddView("ep02_arlesex40", "ep02_arlesex41", "ep02_arlesex42")
    show screen camera_view with flash
    show white zorder 1.0 at ejaculation_flash
    arl "Warm..."
    $ show_custom_notification("multicam_tip")
    arl "So warm!"
    arl "I can feel it... Pouring out..."
    arl "I'm done... I've never been fucked like this before."
    hide screen camera_view
    pause 1
    jump ep02_arlette_mc_story




label ep02_lovemaking_over:
    $ AddView("ep02_arlesex34", "ep02_arlesex35", "ep02_arlesex36")
    show screen camera_view

    mc_s "Ok... here it comes, Arlette!"

    $ show_custom_notification("multicam_tip")
    arl "Yes! That's it! Come on my ass !"
    mc_s "Here... it goes!"

    hide screen camera_view
    $ AddView("ep02_arlesex37", "ep02_arlesex38", "ep02_arlesex39")
    show screen camera_view with flash
    show white zorder 1.0 at ejaculation_flash
    arl "Yes! That's so warm..."
    arl "Mon dieu! Tu m'as gâché le cul, [mc_name]!"
    arl "Look at all of this..."
    arl "Such a mess..."
    hide screen camera_view
    pause 1
    jump ep02_arlette_mc_story




label ep02_arlette_mc_story:
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(arlette_love_theme, "music", 1, True, 2.5, 0)

    show ep02_lovestory1 at concentrate with slowfade
    mc_t "It's crazy, isn't it? How time can just slip through your fingers like that."
    mc_t "Arlette and I, we were building something beautiful, getting closer every single day, trying to carve out some kind of normal life in a world that had been pretty fucking cruel to us."

    show ep02_lovestory2 at concentrate with flash
    mc_t "Our little apartment, it was like our sanctuary, you know?"
    mc_t "Away from all the dark shit that was lurking in the underbelly of Osaka."
    mc_t "She was working part-time, and I was still at the police department."

    show ep02_lovestory3 at concentrate with flash
    mc_t "It was a simple life, something I'd been craving for so damn long."
    mc_t "I felt like I could finally breathe, like I could just... exist."
    mc_t "It was good, really fucking good."

    show ep02_lovestory4 at concentrate with flash
    mc_t "It was like we'd finally turned over a new leaf."
    mc_t "Those bastards who tried to drag Arlette into that fucked up life... Gone."
    mc_t "Maybe they got bored, maybe they moved on to some other poor girl."

    show ep02_lovestory5 at concentrate with flash
    mc_t "Meanwhile, her [gra_r_low] was doing alright, and Arlette was there for her, no matter what."
    mc_t "And us? What we had, it grew into something so fucking deep, the kind of love you don't see every day."
    mc_t "Life was good, peaceful..."
    mc_t "And as the sun went down over Osaka, we realized that no matter how much darkness we'd been through, none of it mattered as long as we had each other."

    show ep02_lovestory6 at concentrate with flash
    mc_t "But in those days, my obsession with keeping Arlette safe, it had turned into something else, something darker."
    mc_t "I was fucking consumed by it, this need to find out who had threatened her - the yakuza."
    mc_t "I threw everything I had at it, every spare second, just trying to stay one step ahead of those sons of bitches."
    mc_t "It started to eat away at everything else... My job, my time with Arlette."

    show ep02_lovestory7 at concentrate with flash
    mc_t "She could feel it, of course she could, but I couldn't seem to stop."
    mc_t "I was trying to protect her, but I was just... I was pushing her away."
    mc_t "I knew I was losing myself in it, but the thought of what might happen if I let my guard down... it was fucking terrifying."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_nightclub, "amb", 1, True, 2.5, 0)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.2)
    $ playAudio(sfx_evenstreet, "amb", 2, True, 2.5, 0)

    show ep02_arlefight1 with slowfade
    rin "Hey, Arlette. Thanks for meeting me. I know things have been... fucked up between us."
    arl "Yeah, you could say that. What do you want, Rina?"
    show ep02_arlefight2
    rin "I'm in some deep shit, Arlette. Like, seriously fucked up shit with the yakuza."
    arl "What kind of shit are we talking about here?"
    rin "The... the bad kind. The 'you better fucking help me or else' kind, you know?"
    arl "Shit, Rina. I'm sorry. I never meant for this to happen to you."
    rin "Yeah, well, it did. And I need your help, Arlette. I need you to talk to them, tell them I had nothing to do with you leaving."
    arl "I... I don't know, Rina. I don't want to get involved with the yakuza again. I've worked so hard to build a new life..."
    rin "Look, I get it. This ain't your problem, and I'm the dumbass who got tangled up with them in the first place."
    rin "But I need your help, Arlette. Just this once. Please."
    show ep02_arlefight3
    arl "I'm sorry, Rina. I can't help you with that."
    rin "You... you can't? But why--"
    arl "I don't want to be a part of that world anymore."
    arl "I've got a new life now, a better one. I'm not gonna fuck that up."
    rin "Fuck, Arlette, please--"
    arl "No, Rina. It's not going to happen."
    arl "And you know what? You should get the fuck out of that world, too. Before it's too late."
    $ playAudio(sfx_tablehit, "sfx", 1, False, 0, 0)

    show ep02_arlefight4 with vpunch
    rin "So you're just going to leave me to rot? After everything we've been through? You selfish bitch."
    arl "Selfish? I'm selfish?"
    arl "Fuck you, Rina."
    arl "You're the one who got me into this mess in the first place. You're the one who pushed me to do things I didn't want to do."
    show ep02_arlefight5
    rin "Fuck you, Arlette! Fuck you and your holier-than-thou bullshit!"
    arl "What--"
    rin "You left me behind, and now you're telling me to get out?"
    rin "You're so full of shit."
    rin "No one gives a fuck about me, Arlette, no one."
    rin "And if you're not going to help me, I'll do what I gotta do."
    rin "Fuck you, Arlette! Just... fuck you!"
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.4)
    $ playAudio(sfx_mc_room_night, "amb", 3, True, 2.5, 0)
    $ playAudio(arlette_love_theme, "music", 1, True, 2.5, 0)

    show ep02_arledeath01 with slowfade
    mc_s "You know, I never thought I'd actually enjoy chopping veggies this much."
    arl "Well, you're surprisingly good at it."
    mc_s "You were right, you know. About the whole living in the moment thing."

    show ep02_arledeath02
    arl "Yeah?"
    mc_s "We've got each other, and that's all that fucking matters. As long as we're together, I'm happy...."
    mc_s "Really fucking happy."
    arl "Me too, [mc_name]. Me too."
    show ep02_arledeath03
    mc_s "I like this... us, here. Together. It's nice."
    arl "You're such a sap, [mc_name]."
    $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)

    mc_s "You know, I never thought I'd be capable of feeling like this. It's nice, really fucking nice. Like..."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.7, fade_duration=1.5)

    show ep02_arledeath04 with slowfade
    $ stopAudio(channel="sfx", subchannel=1, fadeout=0.5)
    arl "Hello? Yeah, this is she... What? When did this happen?"
    arl "No, no, that can't be right."
    arl "I-- I was just gonna visit her tomorrow..."
    arl "Oh my god..."
    $ playAudio(sfx_tablehit, "sfx", 1, False, 0, 0)

    show ep02_arledeath05 with vpunch
    mc_s "Arlette, what is it? What the fuck happened?"
    arl "Ma Mamie..."
    arl "My [gra_r_low]... she's gone, [mc_name]."
    arl "She just... died."
    arl "It can't be true... She can't be dead..."
    mc_s "I'm so sorry, Arlette. I'm so, so sorry."
    arl "I don't understand... I just don't fucking understand."
    mc_s "I'm so sorry. This is... this is terrible."
    mc_s "Did they say what happened? Was it a disease or--"
    arl "They didn't say much, just that it wasn't natural. And that I need to get down there right away..."
    arl "Fuck, [mc_name], what am I gonna do?"
    mc_s "We'll get down there, talk to the docs, and sort this shit out. It's gonna be okay, I promise."
    arl "Okay."
    $ unlock_memory("m_ep02_kitchen")
    $ stopAllSubchannels(channel="amb", fadeout=2.5)
    scene eigengrau with dissolve
    $ playAudio(arlette_nostalgia_theme, "music", 1, True, 2.5, 0)

    show ep02_arledeath06 with slowfade
    mc_t "This was it."
    mc_t "The moment that would throw our lives back into fucking chaos."
    mc_t "After all the shit we'd been through, all the crap we'd managed to overcome, this was the gut punch that would set off a shitstorm."

    show ep02_arledeath07
    mc_t "Something didn't add up."
    mc_t "It was too sudden, too fucking convenient."
    mc_t "Could the yakuza have been behind this? Or Rina? I couldn't let my guard down, not even for Arlette's sake."
    mc_t "Because if some serious shit was about to go down, I needed to be ready."

    $ setChannelVolume(channel="amb", subchannel=2, volume=1)
    $ playAudio(sfx_windyprairie, "amb", 2, True, 2.5, 0)
    $ playAudio(sfx_birds1, "amb", 1, True, 2.5, 0)

    show ep02_arledeath08 with slowfade
    mc_t "At her  [gra_full_r_low]'s funeral, Arlette was visibly shattered, almost ghost-like."
    mc_t "I was by her side, offering support, but my mind was also elsewhere, consumed by thoughts of vengeance and justice."
    arl "She was everything to me, [mc_name]."
    arl "She was all I had left of my old life. And now she's fucking gone..."
    mc_s "I know, Arlette. I know. And I promise you, we'll find out who did this."

    show ep02_arledeath09
    arl "[mc_name], it's not just about finding out who did this. It's about... us."
    mc_s "Us? What the hell are you talking about?"
    arl "I'm broken, [mc_name]. And I'm afraid that... that I'm breaking you too."
    mc_s "Arlette, don't say that. You're not--"

    show ep02_arledeath10
    arl "After all this time, all this fucking rollercoaster, you've been so good to me."
    arl "But I think it's time for you to walk away. Before it's too late."
    arl "I'm not worth it, [mc_name]. And you deserve better."
    mc_s "Arlette, no. I'm here for you. We can get through this, together."

    show ep02_arledeath11
    arl "Look at me, [mc_name]."
    arl "Look at what's happening to me."
    arl "I'm a fucking mess. I can barely function, barely sleep, barely eat."
    arl "You need to be free of this. You don't owe me a damn thing."
    mc_s "Arlette, don't say that. I'm here for you, I want to be here for you. I--"

    show ep02_arledeath12 with hpunch
    arl "I know. I know."
    arl "And that's what makes it so fucking hard."
    arl "So please, please don't make this any harder than it already is."
    mc_s "Are you--"
    arl "[mc_name], I love you. But my world has become too dangerous."
    arl "And I can't... I won't drag you down with me."
    mc_s "Arlette..."

    show ep02_arledeath13
    arl "It's better if... if we go our separate ways."
    mc_s "But--"
    arl "Désolé, [mc_name]. Putain, je suis tellement désolé. Mais c'est la fin."
    arl "Goodbye, [mc_name]. You'll always have my heart."
    mc_t "This was it."
    mc_t "The breaking point..."
    mc_t "I could see it in her eyes, feel it in the finality of her words."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep02_arledeath14 with slowfade
    mc_t "It was over. She was leaving me."
    mc_t "And there was not a damn thing I could do to stop her. Nothing I could say to change her mind."
    mc_t "Arlette turned and walked away, her shoulders shaking with silent sobs"
    mc_t "I stood there, watching her go, feeling the weight of her words with my heart shattering into a million pieces."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ resetAllVolumes()
    jump ep02_revenge_night




label ep02_revenge_night:
    scene eigengrau with dissolve 
    $ playAudio(sfx_nightroad, "amb", 1, True, 2.5, 0)

    show ep02_revenge01 at concentrate with circlewipe
    mc_t "I couldn't just let it go."
    mc_t "Arlette was out there, alone, broken. And those fucking bastards, the ones who'd done this to her, to us... they weren't going to stop."
    mc_t "I had to do something. I had to take control, no matter how much it fucking cost me."
    mc_t "So, I did what I do best. I started digging."

    show ep02_revenge02 at concentrate
    mc_t "I dug and dug, looking for answers, clues, anything that could lead me to the fucking truth."
    mc_t "I searched for hours on end, poring over every damn bit of information I could find."
    mc_t "I traced Arlette's calls, her messages, her emails, her accounts."
    mc_t "I called in favors at the station, reached out to my contacts in the fucking underworld."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ setChannelVolume(channel="music", subchannel=1, volume=0.5)
    $ playAudio(mc_broken_theme, "music", 1, True, 2.5, 0)
    scene eigengrau with dissolve 
    show ep02_revenge03 with circlewipe
    mc_t "And then, after weeks of searching, I found something... A clue."
    mc_t "This might be the last fucking time I see this place. But it's worth it."

    show ep02_revenge04 with flash
    mc_t "It's worth it to know that she's safe."
    mc_t "And if I can make that happen... Well, that's all I fucking need."

    show ep02_revenge05 with flash
    mc_t "This is it. I'm going to end this, one way or a-fucking-nother."

    $ playAudio(sfx_slamdoorhard, "sfx", 1, False, 0, 0)

    show ep02_revenge06 with vpunch
    mc_s "We need to talk. About Arlette."

    $ stopAllSubchannels(channel="music", fadeout=4)
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_extnight, "amb", 1, True, 2.5, 0)
    $ playAudio(sfx_heartbeatslow, "sfx", 2, True, 4, 0)
    hid "Arlette?"
    hid "Ah, the little bird has flown away, hasn't she?"
    hid "What the fuck do you want with her?"
    mc_s "I want you to leave her the fuck alone. For good."

    show ep02_revenge07
    hid "And if I don't? You'll shoot me, is that it?"
    mc_s "If that's what it fucking takes."
    mc_t "This old bastard, surrounded by his fucking lapdogs."
    mc_t "They're all getting off on this, on seeing me here. First things first, I gotta check my surroundings..."
    menu ep02_shootingcheck:
        "Check left" if not ep02_checkleft:
            $ ep02_checkleft = True
            jump ep02_shootleft


        "Check right" if not ep02_checkright:
            $ ep02_checkright = True
            jump ep02_shotright


        "Check back" if not ep02_checkback:
            $ ep02_checkback = True
            jump ep02_shootback




    label ep02_shotright:
    show ep02_revenge09 with dissolve
    mc_t "Bleach boy over here..."
    mc_t "He's eyeing me like a fucking piece of meat. Probably itching to use that knife."
    if ep02_checkleft and ep02_checkright and ep02_checkback:
        jump ep02_shootcontinue


    else:
        jump ep02_shootingcheck




    label ep02_shootback:
    show ep02_revenge10 with dissolve
    mc_t "Fuck, this one's trouble. That piece on her thigh..."
    mc_t "Not sure I can take her if she brings out that gun."

    show ep02_revenge08
    mc_t "The way she's watching me..."
    mc_t "I bet she's just waiting for an excuse to put a bullet in me."
    if ep02_checkleft and ep02_checkright and ep02_checkback:
        jump ep02_shootcontinue


    else:
        jump ep02_shootingcheck




    label ep02_shootleft:
    show ep02_revenge11 with dissolve
    mc_t "Suits. Always with the fucking suits."
    mc_t "And of course, one of them's got a goddamn uzi. Probably compensating for something."
    mc_t "The other one, though... he's looking at me kinda nervous, keeps checking the window."
    if ep02_checkleft and ep02_checkright and ep02_checkback:
        jump ep02_shootcontinue


    else:
        jump ep02_shootingcheck




    label ep02_shootcontinue:
    show ep02_revenge12 with hpunch
    hid "Such a brave little gaijin fool."
    hid "You're nothing to us, do you understand? Fucking nothing."
    hid "And so is your precious Arlette."
    hid "So run along now, before we decide to make a fucking example of you, white boy."
    mc_t "Oh there she is... Rina. Fucking Judas in a G-string."
    mc_t "I should've known she'd be here, cozied up to this scumbag."
    mc_t "This is getting complicated... What should I do? Fuck it, I'm already here... no time for doubts."
    mc_t "Fuck them. Fuck all of them."

    $ playAudio(sfx_tablehit, "sfx", 1, False, 0, 0)

    show ep02_revenge13 with vpunch
    mc_s "If you hurt her, I'll--"
    hid "You'll what?"
    hid "You're weak, pathetic."
    hid "You don't have the balls for this, not like we do."
    hid "Now get the fuck out of here. While you still can."
    $ stopAudio(channel="sfx", subchannel=2, fadeout=1.5)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(mc_suspense_theme, "music", 2, True, 2.5, 0)
    $ playAudio(sfx_heartbeatfast, "sfx", 3, True, 2.5, 0)

    show ep02_revenge14 with hpunch
    mc_s "I'm not here to play games, Hideo."
    hid "You've got some fucking nerve, coming in here like this."
    hid "You think you're some kind of hero? You're just a pathetic little cop playing in the big leagues."
    mc_s "I don't give a fuck what you think of me."
    mc_s "I'm here for Arlette. And I'm not leaving until I know she's safe."
    hid "Safe?"
    hid "You really are a fucking idiot."
    hid "No one's safe. Not her, not you."
    hid "Especially not you."
    hid "Come on, tough guy. Make a move."
    hid "I dare you."
    hid "My people here, they're just itching for an excuse to put you down."
    mc_t "Fuck, this is bad. They're all armed to the teeth."
    mc_t "And Rina... what the hell is she doing? Is she trying to bail?"

    show ep02_revenge15
    rin "Hideo, baby, come on... This isn't worth it."
    rin "Let's just let him go, okay? For me?"
    hid "And who the fuck are you to tell me what to do, you fucking whore?"
    hid "Your mouth only has one good use and it's not for fucking talking."
    rin "[mc_name], please. Just go. Don't do this. It's not worth it."
    hid "I said shut up!"
    hid "One more word and I'll put a fucking bullet in you myself."
    hid "Do I make myself clear, you stupid fucking bitch?"
    rin "...Yes. Sorry. I-I'll be quiet..."
    show ep02_revenge16
    hid "You really love her, don't you? This Arlette."
    hid "Too bad she's just another whore. Like all the rest. Like Rina here."
    mc_s "Don't you fucking talk about her. Don't you even say her name."
    hid "Or what? What are you going to do, cop?"
    hid "You gonna shoot me? In front of all my men?"
    hid "You wouldn't make it to the fucking door."
    mc_t "He's right. I'm outgunned, outnumbered."
    mc_t "If I make a move now, I'm dead."
    mc_t "But if I walk away... Arlette... Fuck!"

    $ show_walkthrough("ep02_revenge_menu1")
    menu:
        mc_t "What do I do? What the fuck do I do?"
        "Walk away":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 5)

            mc_t "Damn it! I better not regret this."

            $ stopAllSubchannels(channel="sfx", fadeout=1.5)
            $ stopAllSubchannels(channel="music", fadeout=2.5)

            mc_s "Forget it."
            mc_s "You win. This time."
            mc_s "Just know that if you or any of your men touch Arlette, I'll come for you."
            mc_s "Every single one of you. And not even this fucking building will be enough to hide you from me."
            hid "I'd like to see you try. Now get the fuck out."
        "Attack him": 
            hide screen walkthrough_screen
            $ ep02_shootout = True
            $ rm.update("mc", "integrity", -5)

            mc_t "Fuck it. I'm doing it."
            mc_t "It's a fucking suicide play, but so is waiting around for these bastards to put a bullet in me."

            $ stopAllSubchannels(channel="sfx", fadeout=3.5)

            mc_s "I'm leaving. Just... promise me she won't get hurt."
            hid "Yeah, sure. I promise. Cross my heart and hope to die, right?"
            mc_s "Swear to me, Hideo."
            hid "Fine. Fine. Whatever you say."
            hid "Now get the fuck out of here. Before you embarrass yourself any more."
    show ep02_revenge17
    if ep02_shootout:
        yaw "Keep moving, dipshit."
        rin "[mc_name], I'm sorry... I didn't mean for..."
        mc_s "Shut the fuck up, Rina."

        $ stopAllSubchannels(channel="music", fadeout=2.5)

        show ep02_revenge17 with vpunch
        yaw "What are you waiting for? Get the fuck out."
        $ playAudio(mc_action_theme, "music", 1, True, 2.5, 0)

        mc_t "Three... two... one..."
    else:
        yaw "Get moving. Fucking pig."
        rin "[mc_name], thank you..."
        mc_s "Fuck you too, bitch."

        jump ep02_consequences


    show ep02_revenge18 with hpunch
    $ playAudio(sfx_bedmove2, "sfx", 1, False, 0, 0)
    $ playAudio(sfx_bodyfall, "sfx", 2, False, 0, 0)
    $ playAudio(sfx_sofa_move, "sfx", 3, False, 0, 0)

    mc_t "This was it. The moment of truth."
    mc_t "Timing had to be perfect. One wrong move and I'd be dead before I hit the ground."
    yaw "Fuck! Take him out!"
    mc_t "Getting to Hideo was crucial. He was the key to all of this. Taking him down meant the rest would scatter."
    mc_t "I had to act fast, use the element of surprise. Threw my coat over the yakuza next to me, blinding him for a moment."

    $ playAudio(sfx_gunshots_glock, "sfx", 4, False, 0, 0)

    show ep02_revenge19 with hpunch
    rin "[mc_name], please! Stop this!"
    mc_s "Shut up, Rina! Just stay down!"
    mc_t "But the other one, the knife-wielding bastard, he was on me in a flash."
    mc_t "I didn't hesitate. I couldn't. I pulled the trigger. It was chaos, pure fucking chaos."

    show ep02_revenge20
    hid "You fucking idiot! Kill him! Kill him now!"
    "Bodyguard" "Hideo, we need to go. Now!"

    $ playAudio(sfx_gunshot_beretta, "sfx", 5, False, 0, 0)

    show ep02_revenge21 with vpunch
    mc_t "I kept firing, kept moving. The one with the knife, he was down but not out."
    mc_t "And the other one, the one I'd blinded, he was reaching for his uzi."
    mc_t "I had to stop him, had to end this before it got any worse."

    $ playAudio(sfx_gunshots_glock, "sfx", 4, False, 0, 0)

    show ep02_revenge22 with vpunch
    mc_t "I put two in the chest of the uzi yakuza. He went down hard, his gun clattering to the floor."
    mc_t "The knife guy, he was still."

    $ playAudio(sfx_celldoor, "sfx", 1, False, 0, 0)

    mc_t "And the other one, the coward, he was pissing himself in the corner. He wasn't a threat."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve 
    show ep02_revenge23 with circlewipe
    $ playAudio(sfx_hallwalkmale, "sfx", 2, True, 1, 0)

    mc_t "The room was quiet, too quiet."
    mc_t "Hideo and his bodyguard, they were gone. Vanished into thin fucking air."
    mc_t "I knew he had an escape route, some sort of hidden exit. I just had to find it."
    mc_t "I started tearing through his desk, looking for a switch, a button, anything."

    $ stopAudio(channel="sfx", subchannel=2, fadeout=1)

    show ep02_revenge24
    mc_t "I was frantic, my eyes darting around the room. The desk, the safe, the walls... where the fuck did they go?"
    mc_t "How did they slip away in the middle of all that gunfire? I was losing it, losing my grip on the situation."
    mc_t "I had to find them, had to end this."
    rin "[mc_name]... what... what are you doing?"
    mc_s "Shut up, Rina. Just shut the fuck up. I need to think."
    mc_t "Come on, come on... where are you, you bastard? You can't hide forever..."

    $ setChannelVolume(channel="music", subchannel=3, volume=0.5)
    $ playAudio(mc_suspense_theme, "music", 3, True, 2.5, 0)

    show ep02_revenge25
    rin "[mc_name], please... you have to understand. I didn't mean for any of this to happen."
    rin "Arlette, she... she was my friend. I was just trying to help her, trying to get her out of this life..."
    mc_t "Her words, they were like poison in my ears."
    mc_t "She was playing the victim... But I knew better. I knew what she was, what she'd done."
    mc_s "Shut the fuck up, Rina. Just shut up."
    mc_s "I don't want to hear your bullshit."
    mc_s "You're not a victim here. You're a fucking accomplice."

    $ show_walkthrough("ep02_revenge_menu2")
    menu:
        "Threaten her":
            hide screen walkthrough_screen
            $ ep02_hitrina = True
            $ rm.update("mc", "integrity", -2)

            mc_t "I could feel it, the urge to lash out, to make her hurt like she'd hurt Arlette."
            mc_t "I wanted to scream at her, to tell her all the things Arlette had been too kind to say."
            rin "[mc_name], please... Don't hurt me..."
            $ playAudio(sfx_bodygrab, "sfx", 1, False, 0, 0)
            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)

            show ep02_revenge26 with hpunch
            mc_s "Give me one good reason why I shouldn't put a bullet in you right now. One fucking reason."
            rin "I-- I..."
            mc_s "Where the fuck is Hideo? How did he escape? Talk!"
            rin "I don't know, I swear! I've never seen anything like that before... the way he just--"
            mc_s "What about Arlette's [gra_full_r_low]? Did you have anything to do with her death? Don't you fucking lie to me, Rina."
            rin "I... I only told them where she was staying. That's all, I promise! I didn't know they were going to... Oh God, I'm so sorry..."
            mc_t "The rage, it was boiling inside me."
            mc_t "She was there, right in front of me, confessing to her part in all of this."
            mc_t "I wanted to do it, to pull the trigger and watch her bleed. But I couldn't."
            mc_t "I was still a cop. Even if every fiber of my being screamed for vengeance."

            $ playAudio(sfx_bodygrab, "sfx", 1, False, 0, 0)
            $ playAudio(sfx_bodyfall_carpet, "sfx", 2, False, 0, 0)

            show ep02_revenge26 with hpunch
            mc_s "You listen to me, you backstabbing bitch."
            mc_s "If anything happens to Arlette, if she's hurt in any way... I'll come for you. I'll hunt you down and make you pay."
            mc_s "That's not a threat, it's a fucking promise."

            $ stopAllSubchannels(channel="music", fadeout=1.5)
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
        "Let her go":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 2)

            mc_s "You're a real piece of work, you know that?"
            mc_s "You sit there. whining and expecting me to what? Feel sorry for you? After everything you've done?"
            rin "[mc_name], please... Don't hurt me..."
            mc_t "I could feel it, the urge to lash out, to make her hurt like she'd hurt Arlette."
            mc_t "I wanted to scream at her, to tell her all the things Arlette had been too kind to say."
            mc_t "But I was a cop. I had a duty, a code. And I held back..."
            mc_s "Get the fuck out of here, Rina. I don't want to lay eyes on you again."
            mc_s "Please, just go, I'm on the verge of a  mental meltdown."

            $ stopAllSubchannels(channel="music", fadeout=1.5)
            $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep02_consequences




label ep02_consequences:
    scene eigengrau with dissolve
    $ resetAllVolumes()
    $ playAudio(sfx_eveningtraffic, "amb", 1, True, 2.5, 0)

    show ep02_aftermath01 with slowfade
    if ep02_shootout:
        mc_t "I'd gone in there, guns blazing, thinking I could take on the whole fucking yakuza."
        mc_t "But what had I achieved? Nothing."
        mc_t "Hideo was gone, Arlette was still missing, and all I'd done was poke the hornet's nest."
        mc_t "I'd failed her. I'd failed myself."
        mc_s "Look at you, a big fucking hero. Reduced to this. What would Arlette think if she could see you now?"
    else:
        mc_t "I'm such a fucking coward."
        mc_t "All that time, I was so damn sure I could handle it."
        mc_t "That I could just bust in there and save the day. Take Arlette back, bring her home, fuck her senseless. We'd live happily ever after."
        mc_t "How fucking naive. And now..."
        mc_t "Look at me, laying out here like a piece of shit. Can't even be bothered to stand up."
        mc_t "And Arlette..."
        mc_t "God damn it. Please, Arlette. Be alright. Please."

    $ stopAudio(channel="amb", subchannel=1, fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.35)
    $ playAudio(sfx_evenbalcony, "amb", 2, True, 2.5, 00)

    show ep02_aftermath02 with ccirclewipe
    if ep02_shootout:
        mc_t "I knew that I'd lost everything. My job... my dignity and my future."

        $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)

        mc_t "And yet, strangely, I didn't give a fuck. Not anymore. All that mattered was Arlette."
    else: 
        mc_t "I knew I fucked up big time... they already knew about me, even before showing up there..."
        mc_t "But now I had given them every reason to make me disappear, and especially, to kill Arlette."

        $ playAudio(sfx_phonering, "sfx", 1, False, 0, 0)

        mc_t "I should have just sacrificed myself right there and not run away like a coward."

    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)

    show ep02_aftermath03
    pa_s "Where the hell are you?"
    pa_s "Why aren't you here working?"
    pa_s "And what the fuck is wrong with you?"
    mc_s "It's over, Paz. Every-fucking-thing is over."

    show ep02_aftermath04
    pa_s "What are you talking about?"

    $ show_walkthrough("ep02_aftermath_menu1")
    menu:
        "Everything's over...":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 2)
            $ check_levels("paz", "trust", 2)

            mc_s "It's just... it's just over. Everything..."
            mc_s "And I don't know what the fuck to do anymore."
            mc_s "I hate myself, Paz. I'm a fucking failure."
        "I screwed up bad":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 1)
            $ check_levels("paz", "trust", 1)

            mc_s "I screwed up, Paz. Real bad."
            mc_s "I thought I could handle it, but I was wrong."
            mc_s "Now everything's gone to shit."
        "I'm done, Paz":
            hide screen walkthrough_screen

            mc_s "I'm done, Paz. With all of it."
            mc_s "The job, the life, everything."
            mc_s "I can't do this anymore."

    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1)
    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6)
    $ playAudio(sfx_eveningtraffic, "amb", 3, True, 1, 0)

    show ep02_aftermath05
    pa_s "Tell me where you are. Are you hurt? I'm coming to get you."
    mc_s "No. Don't come."
    mc_s "Just... stay the fuck away from me, okay?"

    show ep02_aftermath06
    pa_s "Are you at home? At your apartment?"

    $ show_walkthrough("ep02_aftermath_menu2")
    menu:
        "Don't--":
            hide screen walkthrough_screen

            mc_s "Don't--"
            mc_t "I didn't want her to see me like this. Broken... a fucking shell of a man."
            mc_t "But I knew Paz. She was stubborn as a mule and twice as determined. She wouldn't let this go."
        "I need you, Paz.":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", 1)
            $ check_levels("paz", "trust", 1)

            mc_s "I... I need you, Paz. But I don't want you to see me like this."
            mc_s "I'm a fucking mess."
            mc_t "I hated admitting it, but I needed her. I needed her strength, her support."
        "I said stay away!":
            hide screen walkthrough_screen
            $ rm.update("paz", "trust", -1)
            $ check_levels("paz", "trust", -1)

            mc_s "I said stay the fuck away, Paz! I don't need your help."
            mc_s "I can handle this on my own. I don't want you involved."
            mc_t "I pushed her away, not wanting to drag her into my mess. But deep down, I knew she wouldn't listen."
    mc_t "She'd come for me, whether I wanted her to or not."

    $ stopAudio(channel="amb", subchannel=3, fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.3, fade_duration=1)

    show ep02_aftermath07 with ccirclewipe
    pa_s "Can you tell me now what's going on? Why are you acting like this?"
    mc_s "They'll come for me, you know."
    mc_s "The Yakuza. They'll want revenge."
    pa_s "God, [mc_name]. What happened. Now."

    show ep02_aftermath08
    mc_s "Yeah... yeah... In a minute."
    mc_s "I'll get changed for work so you won't keep bothering me. I'll be right back."
    pa_s "Wait, it's not nece--"
    pa_s "Meh... Alright."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_eveningtraffic, "amb", 3, True, 2.5, 0)
    $ setChannelVolume(channel="music", subchannel=3, volume=0.5)
    $ playAudio(mc_theme, "music", 3, True, 2.5, 0)

    show ep02_aftermath09 with ccirclewipe
    mc_s "Okay, let's start at the beginning..."
    mc_t "And I told her everything..."
    mc_t "Every fucking detail of what had happened, every emotion that had led me to that point."
    mc_t "She listened, without judgment or pity, just as she had always fucking done. And when I finished, she sat there, quietly, thinking it over."

    $ setChannelVolume(channel="amb", subchannel=3, volume=0.1, fade_duration=1)

    show ep02_aftermath10
    if ep02_shootout:
        pa_s "I regret what I'm about to say, but I agree with you."
        mc_s "You... you do?"
        pa_s "Yes. You killed those bastards in self-defense, and I'll stand by you on that."
        mc_y "You know that's bullshit, Paz!"
        mc_y "I wanted them dead, and I went after them like a fucking madman!"
    else:
        pa_s "I hate to say it, but I think you did the right thing by walking away."
        mc_s "You... you do?"
        pa_s "Yes. Escalating the situation would have only made things worse."
        pa_s "You showed restraint, and that takes strength."
        mc_s "But it doesn't feel like strength, Paz. It feels like weakness."
        mc_s "Like I've just painted a big fucking bullseye on my back. On Arlette's back."

    show ep02_aftermath11
    if ep02_shootout:
        pa_s "Like I said, I agree with you."
        mc_s "Why? How the fuck could you agree with me after what I've done?"
        mc_s "I've brought shame to the police, to you, to everything we stand for."
        pa_s "Because I know you, [mc_name]."
        pa_s "I know the goodness in your heart. And I trust that you did what was necessary."
        mc_s "Paz, if anyone finds out about this, you could be implicated too. And I don't fucking want that."
        pa_s "Don't worry about me. I can take care of myself."
    else:
        pa_s "I understand why you feel that way, [mc_name]. But sometimes, walking away is the bravest thing you can do."
        mc_s "Brave? How the fuck is it brave to let them win? To let them think they can just push me around?"
        pa_s "It's brave because you put Arlette first. Because you knew that fighting back would only put her in more danger."
        mc_s "But now they know, Paz. They know I'm a threat."
        pa_s "And we'll deal with that, [mc_name]. We'll find a way to protect you, to protect Arlette."
        mc_s "I don't want you caught up in this, Paz."
        mc_s "If they come after me, if they find out you're involved..."
        pa_s "I'm a big girl, [mc_name]. I can handle myself. And I'm not going to let you face this alone."

    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6, fade_duration=1)
    $ playAudio(sfx_car_racing, "sfx", 1, False, 1, 0)

    show ep02_aftermath12 with hpunch
    mc_t "It was over."
    mc_t "They had come for me. They had tracked me down, and now I was going to pay for what I had done."
    mc_t "But Paz was there, with me, and I couldn't let any-fucking-thing happen to her."

    $ setChannelVolume(channel="amb", subchannel=3, volume=0.1, fade_duration=1)

    show ep02_aftermath13
    $ show_walkthrough("ep02_aftermath_menu3")
    menu:
        "I couldn't let her stay":
            hide screen walkthrough_screen
            $ ep02_distraction = False
            $ rm.update("mc", "integrity", 1)

            mc_t "I couldn't let her stay. Couldn't let her risk her life for my mistakes."
            mc_t "I had to get her out of there."
            mc_s "You need to go. Right fucking now."
            pa_s "Uh? What? Why?"
        "I needed a distraction":
            hide screen walkthrough_screen
            $ ep02_distraction = True
            $ rm.update("mc", "integrity", -1)

            mc_t "I needed a distraction. Something to draw Hideo's attention..."
            mc_t "And Paz... she was the perfect bait."
            mc_s "Paz, listen to me. I need you to do something for me."
            pa_s "What is it, [mc_name]? What's going on?"

    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6, fade_duration=1)

    show ep02_aftermath14
    if ep02_distraction:
        mc_s "I need you to trust me, Paz. No matter what happens, just follow my lead."
        pa_s "You're scaring me, [mc_name]. What's this about?"
    else:
        mc_s "Paz, look. Across the street. That red car..."
        pa_s "What about it?"
        mc_s "I think... I think it's them. The yakuza."

    show ep02_aftermath15
    pa_s "Shit, [mc_name]. Is that...?"
    mc_s "Hideo. The yakuza boss. And he's armed."
    pa_s "What the fuck is he doing here?"
    mc_s "He must have followed me. Or tracked me down somehow."

    $ setChannelVolume(channel="amb", subchannel=3, volume=0.1, fade_duration=1)

    show ep02_aftermath16
    mc_s "Paz, you need to go. Now."
    pa_s "Fuck that! I'm not leaving you."
    if ep02_distraction:
        mc_s "You have to, Paz. It's the only way."
    else:
        mc_s "I'm not letting you get caught up in this."
    pa_s "No! I'm not leaving you."
    mc_s "God-fucking-dammit, Paz, you--"
    mc_t "I had to get Hideo's attention..."

    $ setChannelVolume(channel="amb", subchannel=3, volume=0.6, fade_duration=1)
    $ playAudio(sfx_cardoor_open, "sfx", 1, False, 0, 0)
    $ playAudio(sfx_punch, "sfx", 2, False, 0, 0)
    $ playAudio(sfx_bodyfall_carpet, "sfx", 3, False, 0, 0)

    show ep02_aftermath17 with hpunch
    pa_s "AHHH!"
    pa_s "What the hell are you doing?! [mc_name], you fucking asshole!"
    if ep02_distraction:
        mc_s "Forgive me, Paz. But I have to do this."
    else:
        mc_s "I'm sorry, Paz. I'm so fucking sorry. But it's better this way."

    show ep02_aftermath18 with vpunch
    hid "You! You fucking cop!"
    hid "Hey, take care of the bitch. I'll handle the cop."
    $ playAudio(sfx_carcrash, "sfx", 5, False, 0, 0)

    show ep02_aftermath19
    mc_t "Had to draw him away from Paz, I had to keep his focus on me."
    hid "You fucking bastard!"
    pa_s "[mc_name]! [mc_name], come back! Don't do this!"
    hid "You're dead, cop. You hear me? Fucking dead!"
    $ playAudio(sfx_car_driveaway, "sfx", 1, False, 0, 0)

    show ep02_aftermath20
    pa_s "Goddamnit, [mc_name]!!"
    pa_s "You stubborn, violent [so_r_low] of a bitch!"
    pa_s "Don't get yourself killed!!"
    mc_t "I could hear Paz's shouts fading behind me as I sped away."
    mc_t "I hated leaving her like that... But I didn't have a choice."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    $ setChannelVolume(channel="music", subchannel=2, volume=0.7)
    $ playAudio(mc_broken_theme, "music", 2, True, 2.5, 0)
    $ playAudio(sfx_car_idle_to_off, "amb", 4, False, 2.5, 1.5)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 2.5, 0)
    $ playAudio(sfx_extnight, "amb", 2, True, 2.5, 0)

    show ep02_aftermath21 with slowfade
    hid "Look at you, pathetic little shit."
    hid "So much for the big tough cop. The great white fuckin' savior of the city."
    show ep02_aftermath23
    hid "Was it worth it, hero? Was it?"
    hid "'Cuz all you ever did was get yourself killed. And for what? A piece of ass?"
    hid "A tight cunt that wasn't worth dyin' over?"
    $ show_walkthrough("ep02_aftermath_menu3")
    menu:
        "I did what was right.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", 1)

            mc_s "I did what was right, Hideo. What any decent man would do."
            mc_s "Protecting the innocent, standing up to scum like you - that's what being a cop is about."
            hid "Hah! Listen to yourself, you self-righteous white fuck."
        "Yeah, I'm a fucking idiot.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -1)

            mc_s "Yeah, yeah. That's me. I'm a fucking idiot. I get it."
            mc_s "Is that what you want, to hear me admit it? To watch me beg?"
            hid "Maybe. I gotta say, it's not as satisfying as I thought it'd be."
    show ep02_aftermath22
    mc_s "Just get it over with, will you? Stop dragging this out."
    hid "Fine. You want me to put you out of your misery? I'll be happy to oblige."
    mc_s "Always with the fucking speeches. How about just a nice clean execution?"

    $ playAudio(sfx_guncock9mm, "sfx", 1, False, 0, 0)
    show screen mcpov_dying
    show ep02_aftermath24 with vpunch
    hid "Tsk, tsk. You should show me some respect, seeing as how you're about to fucking die and all."
    hid "You know what's wrong with this country?"
    hid "They let any fucking gaijin with a badge think they can play cop. Like you."
    hid "You don't know shit about how things work here. About the way it's always been between us and the police."
    mc_t "Isabella... I'm sorry."
    mc_t "I was just trying to do the right thing. I never wanted to leave you. I hope you can forgive me."
    hid "Time to put you down, gaijin."
    scene eigengrau with dissolve
    $ playAudio(sfx_cardoor_open, "sfx", 2, False, 0, 0)

    show ep02_aftermath25 with slowfade
    hid "What the fuck? What are you doing?"
    $ playAudio(sfx_guncock9mm, "sfx", 3, False, 0, 0)

    "Bodyguard" "I'm afraid your role in this story has come to an end."
    hid "What the fuck are you saying, you crazy bitch? Do you know who the fuck I am?"
    "Bodyguard" "You've always been so focused on your own power, your own importance. But you don't realize we're nothing."
    hid "Do you have any idea who I am? You can't just--"
    "Bodyguard" "A speck of dust. Your life, your death... meaningless."
    hid "I'll fucking kill you for this! You have no idea who you're fucking with!"
    $ playAudio(sfx_gunshot_beretta, "sfx", 5, False, 0, 0)
    scene eigengrau with dissolve
    $ playAudio(sfx_bodyfall_carpet, "sfx", 6, False, 0, 0)

    show ep02_aftermath26 with slowfade
    $ playAudio(sfx_footsteps_heelstile, "sfx", 7, True, 0, 0)

    mc_t "Holy shit... what the hell is happening? Who the fuck is this woman?"
    mc_t "Is this it? Is this how I go out? Bleeding in a tunnel, next to a dead yakuza?"

    $ stopAudio(channel="sfx", subchannel=7, fadeout=1)
    scene eigengrau with dissolve
    show ep02_aftermath27 with slowfade
    "Bodyguard" "[mc_name], you still have so much to do. Your story, your plan... it's far from over."
    mc_s "Who... the fuck... are you? How do you... know me?"
    "Bodyguard" "I've been watching you, [mc_name]. For a long time."
    "Bodyguard" "You have a purpose. And I'm here to make sure you fulfill it."

    show ep02_aftermath28
    "Bodyguard" "In the end, we're all just corpses waiting to happen."
    "Bodyguard" "Hideo's time came sooner than most."
    "Bodyguard" "But it changes nothing. Not yet."
    mc_t "I need... answers... who is she... why... can't... think..."

    show ep02_aftermath29
    "Bodyguard" "Rest now, [mc_name]. Help is coming. I made sure of it."
    mc_s "I--"
    "Bodyguard" "We'll see each other again soon."
    "Bodyguard" "And don't worry about the haircut... I always did like you better with longer hair... Handsome."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)
    hide screen mcpov_dying
    jump ep02_arlette_breakup




label ep02_arlette_breakup:
    scene eigengrau with dissolve
    $ setChannelVolume(channel="amb", subchannel=1, volume=0.2)
    $ playAudio(sfx_hospital_hall, "amb", 1, True, 2.5, 1)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5)
    $ playAudio(sfx_midnightpast, "amb", 2, True, 2.5, 1)

    show ep02_breakup1 with slowfade
    arl "[mc_name], what have you done?"
    mc_s "Arlette? You're here?"
    arl "Of course I'm here!"
    arl "Your partner called me, and I came as fast as I could."
    arl "But [mc_name], attacking the yakuza? What were you thinking?"
    mc_s "I had to do something, Arlette. For you."

    show ep02_breakup2
    mc_s "For weeks, I've been trying to find out what happened to your [gra_r_low]."
    if ep02_hitrina:
        mc_s "I was convinced that the yakuza were behind her death... Rina... those fuckers you met... they were all involved."
    else:
        mc_s "I was convinced that the yakuza were behind her death... those fuckers you met... they were all involved."
    mc_s "I couldn't just sit back and let them get away with it."

    $ setChannelVolume(channel="music", subchannel=1, volume=0.7)
    $ playAudio(arlette_nostalgia_theme, "music", 1, True, 1, 0)
    arl "[mc_name], I appreciate what you've done, but you can't keep doing this."
    arl "You can't keep putting yourself in danger for me."
    if ep02_shootout:
        mc_s "I took out the yakuza, Arlette. Most of them, anyway."
    else: 
        mc_s "I got rid of the yakuza, Arlette. At least their leader, anyway."
    mc_s "I had to. If they ever laid a fucking finger on you, or hurt you in any way--"
    arl "And what about you, [mc_name]? What about the consequences for you?"
    if ep02_shootout:
        mc_s "I'll tell them it was self-defense, that those bastards attacked me first."
    else:
        mc_s "I'll tell them it was self-defense, that Hideo attacked me first."
    mc_s "And Paz... well... she'll back me up on it."

    show ep02_breakup3
    arl "You did all this for me?"
    $ show_walkthrough("ep02_breakup_menu1")
    menu:
        "I'd do anything for you.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 1)
            $ check_levels("arlette", "trust", 1)

            mc_s "Of course I did it for you, Arlette. I'd do anything for you."
            mc_s "I love you more than life itself. I couldn't bear the thought of losing you."
            mc_s "You're everything to me. I'd go to the ends of the earth to keep you safe."
            arl "[mc_name]..."
        "I had to protect you.":
            hide screen walkthrough_screen
            $ rm.update("arlette", "trust", 2)
            $ check_levels("arlette", "trust", 2)
            $ rm.update("mc", "integrity", 1)

            mc_s "I did it to protect you, Arlette. That's all that matters to me."
            mc_s "I care about you deeply. I couldn't just stand by and let them hurt you."
            mc_s "Your safety is my top priority. I'll always do whatever it takes to keep you out of harm's way."
            arl "[mc_name], I..."
        "It needed to be done.":
            hide screen walkthrough_screen
            $ rm.update("mc", "integrity", -2)

            mc_s "It wasn't just for you, Arlette. It needed to be done."
            mc_s "Those bastards had to pay for what they did. I couldn't let them get away with it."
            mc_s "Justice had to be served, one way or another. That's all there is to it."
            arl "But [mc_name]..."
    arl "[mc_name], you can't keep risking everything for me. Your job, your freedom... your life."
    mc_s "They won't fucking hurt you now..."
    arl "But don't you see, [mc_name]? This... this thing between us... it's not good for you. I'm not good for you."
    mc_s "What are you talking about, Arlette? I fucking love you."
    arl "I love you too, [mc_name]. More than you know."
    show ep02_breakup4
    arl "But we can't keep doing this. We can't keep hurting each other."
    mc_s "Arlette, please. Don't do this."
    arl "You'll always be my hero, [mc_name]. You saved me in so many ways."
    arl "But I can't let you destroy yourself for me. I won't let you."
    mc_s "Arlette, don't leave me. Please."
    arl "I'm sorry, [mc_name]. I'm so sorry. But this is goodbye. I have to let you go."
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    show ep02_breakup5 at concentrate with circlewipe
    mc_t "She was gone, really gone this time."
    mc_t "And despite everything I had done, all the risks I had taken... I couldn't make her stay."
    mc_t "I felt a heaviness settle over me. It wasn't just heartbreak, it was... exhaustion."
    mc_t "I was tired, so fucking tired of pouring my heart into someone, only to end up alone."
    mc_t "Again and again, the story played out the same way. I loved, I fought, I bled... and in the end, I was left with nothing but the bitter taste of abandonment."

    show ep02_breakup6
    if htl_episodes == 2:
        $ show_custom_notification("save_tip")

    mc_t "Maybe this was a sign. A cruel, painful sign that it was time for me to focus on something else, anything else..."
    mc_t "My job, my [dau_r_low], my own fucking sanity. I had spent so long chasing after love, after that elusive connection... and where had it gotten me?"
    mc_t "A hospital bed and a shattered heart."
    mc_t "If Antonella came back, if Arlette changed her mind... well, I'd cross those bridges when I came to them."
    mc_t "But I wasn't going to hold my breath. I wasn't going to put my life on hold, waiting for a love that might never come."

    scene eigengrau with dissolve
    $ playAudio(sfx_doorclose, "sfx", 1, False, 0, 0)

    show ep02_breakup7 with slowfade
    isa "[da_r]! [daddy_r]! Are you okay?"
    mc_t "Love... it was a beautiful thing. But it was also messy, complicated, and so fucking hard."
    mc_t "Maybe, just maybe, it was time for me to step back. To focus on healing, on rebuilding, on finding a purpose that didn't revolve around another person."

    $ stopAllSubchannels(channel="amb", fadeout=1)
    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ stopAllSubchannels(channel="music", fadeout=1)
    $ update_htl_episodes()
    call hideNoise(transition=dissolve)
    #-- End Episode 2
    if htl_episodes == 2:
        return


    else:
        scene eigengrau with rose
        pause 2
        $ resetAllVolumes()
        jump ep03_title