



label ep01_start:
    $ persistent.current_episode = 1
    scene eigengrau with watercolor
    $ stopAllSubchannels(channel="music", fadeout=1)
    pause 0.5
    $ quick_menu = True
    show screen stats_button
    show screen walkthrough_icon
    $ renpy.block_rollback()
## -- SCENE 01: ISABELLA INTRO TRAIN
    show ep01_1stdream00
    $ config.rollback_enabled = True
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(isabella_theme, "music", 2, True, 5, 0)

    show osaka_location zorder 2 with dissolve
    pause 4
    hide osaka_location with dissolve
    mc_t "Funny how a simple change of scenery can bring back memories I thought I'd left behind."
    mc_t "All those years ago, I had no idea how much my life was about to change..."
    if renpy.loadable("wt.rpyc"):
        $ show_custom_notification("wt_tip")
    $ playAudio(sfx_trainstationquiet, "amb", 1, True, 1, 0)

    show ep01_1stdream01
    mc_t "Years on this path, and yet, every morning feels like a new battle. But despite all the challenges I've faced, I'm still here."

    show ep01_1stdream03
    mc_t "I never thought I'd live to see you grow up, but life has a twisted sense of humor. And here you are, right in front of me."

    show ep01_1stdream02
    mc_t "You're the splitting image of your [mo_r_low] — those crystal blue eyes, that golden hair. Every soft curve of your face is a reflection of hers."
    mc_t "But look at what you've inherited from me... that lost, empty look in your eyes. The same one I see in the mirror every damn day."

    show ep01_1stdream04
    mc_t "Seeing you makes me think of all the moments we could have shared together if only I hadn't walked out on you."

    $ show_walkthrough("ep01_train_menu")
    menu:
        mc_t "What should I remember?"
        "Walking at the park":
            hide screen walkthrough_screen

            mc_t "I missed out on moments like taking you on your first walk in the park, watching you run towards me trying to say '[daddy_r]'..."
        "First steps":
            hide screen walkthrough_screen

            mc_t "I missed out on witnessing your first steps, watching you stumble towards me for support..."
    mc_t "I lost all of that because I was chasing a ghost"

    show ep01_1stdream05
    mc_t "Now, looking at you... you seem so different. Pieces of me... echoes of her. All intertwined in you."

    show ep01_1stdream06
    mc_t "Look at you, lost in your books... just like your [mo_full_r_low] was. When we first met, we could talk about everything under the sun. I miss her so much."

    show ep01_1stdream07
    mc_t "And look... you caught me staring at you, just like your [mo_full_r_low] did back then."

    $ stopAllSubchannels(channel="music", fadeout=2)
    $ stopAllSubchannels(channel="amb", fadeout=2)
    jump ep01_dream1




label ep01_dream1:
##RM.POINTS.TRACK (antonella, trust, +1, +2)
# --
## -- SCENE: MEETING ANTONELLA
    scene eigengrau with bokeh
    show ep01_1stdream09 with clouds_inverse
    $ playAudio(sfx_hshall, "amb", 1, True, 2, 0)

    "Girl" "Hey, what are you doing? You're blocking the light."
    mc_s "Huh? Blocking your light? How's that possible when the light is coming from the window behind you?"

    show ep01_1stdream08
    "Girl" "Fine, whatever! You're interrupting me by just staring. Seriously, go away!"
    mc_s "Wow, okay, take it easy. I'm going!"

    show ep01_1stdream10
    "Girl" "Wait! Why were you staring at me like that, huh?"

    $ show_walkthrough("ep01_antodemo_menu")
    menu:
        mc_t "Why was I staring?"
        "I've seen you before":
            hide screen walkthrough_screen

            mc_s "Well... you looked familiar to me. I'm pretty sure I've seen you around before."

            show ep01_1stdream11
            "Girl" "Yeah, right. I don't hang out with anyone in this stupid school."
        "You don't look from here":
            hide screen walkthrough_screen

            mc_s "You don't really seem like you're from here... I mean, from Japan."

            show ep01_1stdream11
            "Girl" "You don't look like you're from around here either, but I'm not asking you dumb questions or staring at you."
        "You look lonely":
            hide screen walkthrough_screen

            mc_s "It felt weird seeing you alone... I don't know, I wanted to say something charming, but I just stood there, staring at you."

            show ep01_1stdream11
            "Girl" "Okay... that's the dumbest line anyone's ever used on me, but I'll let it slide because at least you're honest."
    mc_s "Hmm, okay. If you say so."

    show ep01_1stdream12
    "Girl" "Is that it? You give up that easily just because a girl tells you to get lost?"

    $ show_walkthrough("ep01_antodemo_menu")
    menu:
        "Try again?":
            hide screen walkthrough_screen

            mc_s "Well... do you want me to? Because I can do that."
            "Girl" "Nah, if you don't want to talk, why waste time, right? Let's not bother."
        "Leave her be":
            hide screen walkthrough_screen

            mc_s "Nah, if you don't wanna talk, that's cool too."
            "Girl" "Okay... you can leave now."

    show ep01_1stdream13
    mc_s "Alright, nice chatting with you. See you later."
    "Girl" "{fii}\"That's the first time anyone has ever paid attention to me. Really noticed me. I mean it in a non-creepy way.\"{/fii}"
    "Girl" "{fii}\"It's not the usual gaijin-obsession or weird looks from everyone. He looked at me like I was human. Like I wasn't some outsider freak.\"{/fii}"

    show ep01_1stdream14
    "Girl" "{fii}\"Well he doesn't look Japanese either. So maybe he gets it. That feeling of not belonging.\"{/fii}"
    "Girl" "{fii}\"Urghhhh, what am I thinking? Why do I care? He's just some random kid who I'll never see again.\"{/fii}"
    "Girl" "{fii}\"Shit. Is this what people call 'having a crush?'\"{/fii}"

    show ep01_1stdream15
    "Girl" "{fii}\"Ugh. Maybe I should apologize to him. I was kind of a bitch when I met him.\"{/fii}"

    show ep01_1stdream16 with vpunch
    $ setChannelVolume(channel="music", subchannel=3, volume=0.8)
    $ playAudio(antonella_love, "music", 3, True, 2, 0)

    "Girl" "Hey! Uh, wait! You!"
    mc_s "Oh, hi again. What's up?"
    "Girl" "Can I talk to you for a bit? I just wanted to say... well... umm..."
    "Girl" "{fii}\"OH GOD! WHAT AM I DOING?? WHY CAN'T I SAY IT??\"{/fii}"
    "Girl" "{fii}\"GRRAAAAAGHHH!! SHIT! WHY ARE YOU SO NERVOUS? JUST SPIT IT OUT!!\"{/fii}"

    show ep01_1stdream18
    "Girl" "Well, I guess I just wanted to say that... ummm... you're cool. Okay? Bye."
    mc_s "Huh?!"
    "Girl" "{fii}\"IDIOT!!! WHY DIDN'T I JUST APOLOGIZE? AND NOW HE'S GONNA THINK I'M WEIRD FOR COMING BACK AND TELLING HIM HE'S COOL!\"{/fii}"

    show ep01_1stdream17
    "Girl" "What?"
    mc_s "You must have been worried about what I thought of you, since you were so adamant about talking to me."

    show ep01_1stdream19
    "Girl" "O-Oh... you figured me out, huh?"
    mc_s "Yeah, kinda. Don't worry about it though. I get it. We all have our moments."

    show ep01_1stdream20
    "Girl" "You see, I'm bad at this stuff. I never know how to act around people."
    mc_s "Well, if it helps, you're doing fine so far."

    show ep01_1stdream21
    "Girl" "Am I? For real?"
    mc_s "Yeah. A bit weird, but also... not."
    "Girl" "{fii}\"He's not afraid of me. He's not treating me differently. Just like...\"{/fii}"
    "Girl" "Ah, yeah... you must... I mean, I know it's not a lot to go by, but I'm actually... well, I'm not entirely Japanese."
    mc_s "No shit? Me neither. So we're both freaks, huh?"

    show ep01_1stdream22
    "Girl" "In a good way, I hope."
    mc_s "For sure."
    "Girl" "Are you always this... nice?"

    show ep01_1stdream23
    "Girl" "{fii}\"What the hell was that??? Oh god, I suck at this. Why can't I just act normal?!\"{/fii}"
    mc_s "Nice? Nah, not really. I'm just trying to be a decent guy."
    "Girl" "Right. Decent. I forget that word exists."
    mc_s "What do you mean?"

    show ep01_1stdream24
    "Girl" "Nothing. Anyway, uhhh, thanks for not being weird. I've had enough of that from other people."
    mc_s "Sure. Well, if you're ever around, you can come find me."
    "Girl" "One last question..."
    mc_s "Hmm?"

    show ep01_1stdream25
    "Girl" "Are you a jerk?"
    mc_s "Huh? A what?"
    "Girl" "I guess I must not have used the right word. You know, a douchebag, asshole, dick. I just wanna make sure I'm not dealing with one of those guys."

    $ show_walkthrough("ep01_dream1_menu")
    menu:
        mc_t "How should I respond?"
        "Honest":
            $ rm.update("antonella", "trust", 3)
            $ check_levels("antonella", "trust", 3)

            hide screen walkthrough_screen

            mc_s "Oh... yeah, no... I'm not like that. Honest."

            show ep01_1stdream28 with vpunch
            "Girl" "Only jerks would say they aren't."
            mc_s "Aha, true. Well, you got me there."
            "Girl" "Or they never realize they are jerks. So maybe you are one, and you're just being polite."
            "Girl" "{fii}\"Why can't I shut up??? Why can't I just compliment him???\"{/fii}"
        "Joke about it":
            $ rm.update("antonella", "trust", 5)
            $ check_levels("antonella", "trust", 5)

            hide screen walkthrough_screen

            mc_s "If I were, would I admit it?"

            show ep01_1stdream28 with vpunch
            "Girl" "Haha, good point. Maybe you're cleverer than the average jerk."
            mc_s "You got me there."
            "Girl" "{fii}\"At least he has a sense of humor.\"{/fii}"
    mc_s "Uhhh..."

    show ep01_1stdream27
    "Girl" "I was kidding, sorta. Sorry, that was a joke. Sometimes I get carried away with jokes. Especially when I'm nervous. And when I'm nervous, I start talking a lot."
    "Girl" "Speaking of which, I should probably stop talking and let you get on with your day."
    "Girl" "{fii}\"STOP TALKING!! STUPID STUPID STUPID!!!\"{/fii}"

    show ep01_1stdream26
    mc_s "Okay... yeah, I better go."
    "Girl" "I'll see you around, then. Ummm, I mean, maybe."
    mc_s "Sure, maybe."

    show ep01_1stdream29 with hpunch
    "Girl" "Goodbye, handsome."
    mc_s "Uhh, bye, I guess."

    show ep01_1stdream30
    "Girl" "{fii}\"SHIT, SHIT, SHIT, SHIIITTT!!!!\"{/fii}"
    "Girl" "{fii}\"WHY THE FUCK DID I BLOW HIM A KISS?! I DON'T EVEN KNOW THIS GUY! OH MY GOD, I AM SO STUPID!\"{/fii}"
    "Girl" "{fii}\"Poor guy. Probably thinks I'm some weirdo now.\"{/fii}"
    "Girl" "{fii}\"Ok, whatever, fuck it. Next time I see him, I'll apologize.\"{/fii}"

    show ep01_1stdream31
    "Girl" "Wait! You forgot something."
    mc_s "Huh? What?"

    show ep01_1stdream32
    "Girl" "My name!"
    "Girl" "My name is Antonella."
    mc_s "Oh, right! Sorry about that."
    anto "And yours is...?"
    mc_s "[mc_name]."
    anto "Cute. See you around, [mc_name]."
    show ep01_1stdream33 with dissolve
    $ stopAllSubchannels(channel="amb", fadeout=2)
    $ stopAllSubchannels(channel="music", fadeout=2)
    pause 1
#BACK TO REALITY
    scene eigengrau with clouds
    show ep01_1stdream34
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    $ rm.set_knows("isabella", True)
    isa "[da_r]?"
    isa "[da_r], are you okay?"
    mc_s ". . ."
    isa "Do you want some water?"
    mc_t "*nods*"

    show ep01_1stdream35
    mc_s "Thanks, sweetie."
    isa "Something else? Maybe you should lay down for a while. Take a nap. You don't look too well."
    mc_s "I'm alright... just give me a moment."

    show ep01_1stdream36
    isa "Take your time, [da_r_low]. I'll be here when you're ready."
    isa "We're almost to Tokyo, so we're almost home."
    show ep01_1stdream37
    mc_s "Yes. Almost home. That sounds nice."
    mc_s "I'm... I'm just gonna rest for a while, okay?"
    isa "You go ahead. I'll wake you up when we get there."
    $ stopAllSubchannels(channel="amb", fadeout=2)
    jump ep01_2nddream




label ep01_2nddream:
    scene eigengrau with clouds_inverse 
##RM.POINTS.TRACK (antonella, trust, +1/+2)
# --
## -- SCENE: ANTONELLA'S TREE
    $ playAudio(sfx_hshall, "amb", 1, True, 2, 0)

    show ep01_2nddream01 with clouds_inverse 
    mc_t "Huh? I'm at school? Um... I wonder where was the last time I saw her again? Let's see, if I keep heading this way, I should eventually..."

    show ep01_2nddream02
    mc_t "Jeez, these halls look the same everywhere. How did I not get lost in here before? And why is no one else around?"

    $ playAudio(sfx_footsteps_female_semirun, "sfx", 1, False, 1, 1)

    show ep01_2nddream03
    mc_t "Fine. I'll just have to wander around until I find her. She couldn't have gone far."

    show ep01_2nddream04
    anto "Don't you have classes to go to?"
    $ stopAudio(channel="sfx", subchannel=1, fadeout=0.5)

    show ep01_2nddream05 with vpunch
    mc_s "Huh? Oh, hello again!"

    $ setChannelVolume(channel="music", subchannel=3, volume=0.8)
    $ playAudio(antonella_love, "music", 3, True, 2, 0)
    anto "Hi, um... sorry about how I acted last time. I'm still new at this whole talking thing. Not sure how to sound more... human, I guess."
    show ep01_2nddream06
    mc_s "Human, huh? Well, you're definitely doing a good job. I didn't think you would even try to talk to me again."
    anto "Really? But I was a total mess when I talked to you before."
    mc_s "Nah, you were fine. Honestly."

    show ep01_2nddream07
    anto "Oh."
    mc_s "So, what are you up to? Skipping class or something?"

    show ep01_2nddream08
    anto "Actually, this might sound strange, but I've been looking for you."
    mc_s "Me? What for?"

    show ep01_2nddream09
    anto "Can we... go somewhere more private? Somewhere I can talk freely without worrying about other people listening?"
    mc_s "Um... We can't exactly leave school right now, right?"
    mc_s "But why would you need to talk privately about anything?"

    show ep01_2nddream10
    anto "Oh, um... I dunno... can you just come with me?"
    mc_s "Where? To another classroom or something?"
    anto "No... Oh, come on, don't be like that! Just trust me, okay? Just this once."
    show ep01_2nddream11
    anto "Please..."
    anto "I won't hurt you. I promise."
    mc_s "Uhm..."
    anto "If I wanted to, I would have done it already."
    mc_s "Alright, alright! Fine!"

    show ep01_2nddream12
    mc_s "Where are we going? A park or something?"
    anto "Let's just keep moving forward, okay? I know a spot near the school. It's safe."
    show ep01_2nddream13
    mc_s "Whoa, whoa, whoa! Stop! Look, I appreciate the gesture, but we're not supposed to be outside of school."
    anto "Come on, I'm not a kidnapper! I'm just trying to talk to you. Honestly."
    show ep01_2nddream14
    anto "Hey, you're not afraid of me, right? I'm not scary. Am I scary?"
    mc_s "Well... no, you're not really scary. But I can't help but feel a bit suspicious of you."
    anto "Sheesh, you're acting like I'm some kind of criminal. I'm just a kid, like you."
    mc_s "Then why do you keep insisting on sneaking out of school together? What if a teacher sees us?"

    show ep01_2nddream15
    anto "Screw the teachers! I need to tell you something important. Please."
    mc_s "Ugh, fine. But this better be good."
    anto "It is. I promise."
    show ep01_2nddream16 with slowfade
    anto "I'm sorry I made you miss class. You must be dying to know what I dragged you out for, right?"
    mc_s "Yeah, I am."
    mc_s "So, you said you had something important to tell me."
    anto "Right. I'm not really sure how to put this... but..."
    anto "Well, first, let me ask you a question."
    mc_s "Okay, I'm ready."

    show ep01_2nddream17
    anto "What do you think of me? Like, as a person?"
    $ show_walkthrough("ep01_2nddream_menu")
    menu:
        mc_t "What do I think of her?"
        "Odd but charming":
            $ rm.update("antonella", "trust", 5)
            $ check_levels("antonella", "trust", 5)

            hide screen walkthrough_screen

            mc_s "You're... a bit strange, but I guess that's just part of your charm."
            anto "Charm, huh? That's a new one."
        "Mysterious":
            $ rm.update("antonella", "trust", 3)
            $ check_levels("antonella", "trust", 3)

            hide screen walkthrough_screen

            mc_s "You're mysterious. Like there's a lot you're not telling me."
            anto "Mysterious? Well, aren't we all?"
        "You make me uncomfortable":
            mc_s "To be honest, you're making me uncomfortable."
            anto "I'm sorry, that's not my intention. I just really need to talk to you about something serious. Can we continue?"
            mc_s "Fine, but let's make it quick, okay?"
    mc_s "Um... before we continue, where are we going? If you had plans, I'd like to know."
    anto "Don't worry, it's nothing major. You'll see soon enough."
    show ep01_2nddream18 with slowfade
    mc_s "Is it some sort of secret hideout or something?"
    anto "Don't laugh, but... it's just somewhere I used to go when I needed to get away from everything."
    mc_s "Why are you being so cryptic about all of this?"
    anto "I used to come here a lot when I was a kid. It's nothing fancy, but it holds a certain kind of nostalgia for me, you know?"
    show ep01_2nddream19 with slowfade
    anto "Reminds me of a happier time, I guess."
    mc_s "You mean you've never been here since then? Why would you take me all the way out here for a little trip down memory lane?"
    anto "There's something you need to see. Something that might explain things a little better."
    mc_s "Go on."
    anto "Have you ever seen temples like this before? They're amazing, aren't they? So beautiful and peaceful."
    anto "Even as a kid, I remember thinking that there was something special about them. Like they held a power that most people didn't understand."
    show ep01_2nddream20 with slowfade
    mc_s "Well, they're pretty impressive. But what's that got to do with what you brought me here for?"
    anto "Here..."
    $ stopAudio(channel="music", subchannel=3, fadeout=2)
    $ playAudio(sfx_windyprairie, "amb", 1, True, 4, 0)

    show ep01_2nddream21 with vpunch
    anto "This is it."
    mc_s ". . ."
    anto "Ta-daah!"
    mc_s "The tree? What about it?"

    show ep01_2nddream22
    anto "Look closer, dummy. You'll see it."
    mc_s "See what? The leaves? The bark?"
    anto "Oh my god, just fucking look at it! Use your eyes!"
    mc_s "Geez, okay! I'm looking!"

    $ show_walkthrough("ep01_antodemo_menu")
    menu:
        "See nothing":
            hide screen walkthrough_screen

            mc_s "I still see nothing. Are you messing with me?"
            anto "Would I do that? Maybe your eyes just aren't attuned."
        "See something":
            hide screen walkthrough_screen

            mc_s "Alright, I think I see something. What is it?"
            anto "You can? Well, never mind then. Seems like you can't actually see it."
        "Same tree?":
            hide screen walkthrough_screen

            mc_s "Are you sure we're looking at the same tree?"
            anto "We are, but let's drop it."
    mc_s "There's nothing here, Antonella. Just a normal old tree."

    show ep01_2nddream23
    anto "You really can't see it, can you? Ah, that's disappointing."
    mc_s "What are you talking about? I'm telling you, there's nothing to see."
    anto "Forget it..."
    anto "You're right."
    anto "It's just a fucking tree."
    show ep01_2nddream24 with vpunch
    mc_s "Listen, Antonella. I came all the way out here with you, so what's this all about? What's going on?"
    anto "It's okay. Just sit here with me for a while, okay? Please. You don't have to say anything."
    show ep01_2nddream25
    mc_s "Um, alright. But you're acting awfully weird today."
    anto "So I'm weird now? I thought you liked that about me."
    show ep01_2nddream26
    mc_s "No, no, that's not what I meant. I just--"
    anto "--It's fine, [mc_name]. C'mon, hurry up and sit down."
    show ep01_2nddream27 with slowfade
    anto "God, this place never fails to take my breath away. I'm glad I got to share it with you, [mc_name]."
    mc_s "That's great, I guess. I still don't understand why we're so far away."

    $ playAudio(antonella_sad_theme, "music", 2, True, 1, 0)

    show ep01_2nddream28 with slowfade
    anto "Maybe one day, you will. One day, you'll understand. And you'll remember this moment."
    anto "Now, stop asking so many questions, okay? I just wanted a quiet place for the two of us. That's all."
    anto "You know... I don't know why, but I feel like I can talk to you."
    anto "Your kindness reminds me of... someone. Someone I knew long ago."
    mc_s "Well, you can talk to me anytime you want. I'm happy to listen."

    show ep01_2nddream29
    anto "Don't make me smile, you jerk! Just... stop trying to make me like you. Okay? Just stop."
    anto "Because ... umm.. I know you. And I don't want to... I can't... I just can't, okay? So please, just stop."
    anto "And once you know, once you really know, you'll hate me."
    mc_s "What? I don't get it. Hate you? Why would I hate you? I barely even know you!"

    show ep01_2nddream30
    anto "Yeah... Don't mind me. Remember I'm not very good at talking. I'm just... having trouble finding the words."
    anto "Tell you what. Let's make a deal."
    anto "One day, I'll tell you everything. Everything about me, everything that makes me who I am. And then, you'll finally understand why I'm acting this way."
    anto "For now, can you just... pretend that everything is okay?"
    mc_s "Uhm..."

    show ep01_2nddream31
    anto "Promise me you won't try to find out who I really am? You can do that, can't you?"
    mc_s "Well... I guess I can try."

    show ep01_2nddream32
    anto "Good. Thank you, [mc_name]. I really mean it. This place... it brings to me a lot of peace. That someone I mentioned earlier, he showed me this place."
    mc_s "He? Who showed you this place?"
    anto "I'm not going to talk about it. But... maybe one day."
    anto "Again, I apologize for bringing you out here for no reason. But... thank you for coming with me."
    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_2nddream33
    mc_t "She's been so quiet. Not a word from her for a while now. Is she still trying to figure out what she wants to say to me? Or does she just want me to leave her alone?"
    mc_t "What was that story she told me? Something about someone showing her this place? Or was that all nonsense? God, I wish I could read her mind."
    mc_t "Maybe I should try to start a conversation myself. I mean, she took me out here for a reason, right?"
    mc_s "Do you come here to read as well?"

    show ep01_2nddream34
    anto "Huh? What? No, I don't. Why?"
    mc_s "You don't seem like someone who spends a lot of time outdoors. Not judging, just an observation."
    anto "No, you're right. I prefer to spend my time indoors, usually. But... there's something about this place."
    anto "Like... it's my only way to escape the dull and simple people surrounding me."
    anto "Sounds pretentious, doesn't it? I can hear it in my own voice."
    mc_s "Uhm..."

    show ep01_2nddream35
    anto "What a terrible thing to say. Forgive me. I'm just... not used to sharing my thoughts with anyone."
    anto "Talking to you like this is so surreal. Like I'm... floating in space, or something. Does that make sense?"
    mc_s "Well, it's okay to say how you feel. Sometimes people don't understand that."
    mc_s "You can just... tell me what comes to your mind. Even if it's a bit off-putting, I'll always listen."

    show ep01_2nddream36
    anto "Heh. Thanks. You're pretty interesting yourself, you know. I'm starting to like you more than I should."
    mc_s "Am I?"
    anto "When I saw you, I thought you were just some ordinary guy."
    $ playAudio(antonella_love, "music", 2, True, 1, 0)

    show ep01_2nddream37
    anto "But after talking to you, I realized that you're so much more than that. You're..."
    anto "Like, when I see you, my heart races. And I can't help but stare at you."
    show ep01_2nddream38
    anto "Sometimes I wonder what it would be like to hold your hand, or even kiss you. Is that wrong?"
    anto "Can I just... hold your hand? Would you let me? I just... want to see how it feels."
    anto "I know it's weird. But, uh..."
    show ep01_2nddream39
    mc_s "I really like you, Antonella."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with clouds
    show ep01_2nddream40 with bokeh2
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    isa "[da_r]?"
    isa "Are you okay?"
    mc_s "Urghhhh, what is happening?"

    show ep01_2nddream41
    pause 1.0
    hide ep01_2nddream41
    show ep01_2nddream42
    isa "Do you want some water?"
    mc_s "Hmm... I'm okay. Just give me a minute."
    isa "Did you have a nightmare?"
    show ep01_2nddream43
    mc_t "Shiiit... my memories..."
    mc_s "Ahh... maybe... I don't know."
    isa "You're starting to worry me, [daddy_r_low]."
    mc_s "It's ok, honey. I just need... a bit more time."

    show ep01_2nddream44
    isa "Take your time. I'll be here when you're ready."
    isa "We're almost to Tokyo, so we're almost home."
    mc_s "Hmm... good..."
    isa "Try to sleep a little bit more, [da_r_low]. We have a few more hours ahead of us."
    mc_s "Alright..."

    show ep01_2nddream45 with slowfade
    mc_t "Isabella... so protective, so caring... she looks so much like Antonella sometimes..."

    show ep01_2nddream46
    isa "Rest well, [daddy_r_low]. I love you."
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_3rddream




label ep01_3rddream:
    scene eigengrau with clouds_inverse
## -- SCENE: ANTONELLA'S LIBRARY
    show ep01_3rddream01 with clouds_inverse
    $ playAudio(sfx_library, "amb", 1, True, 1, 0)

    mc_t "I don't even wanna know how she got there."

    $ show_walkthrough("ep01_antolib_menu")
    menu:
        "Talk to her":
            hide screen walkthrough_screen

            mc_s "Uh..."
            mc_s "Antonella?"

            show ep01_3rddream02
            anto "[mc_name]???"
            anto "OMG!"
            mc_s "WATCH..."
        "Check her":
            hide screen walkthrough_screen

            mc_t "I think that if I move to the side a bit..."

            show ep01_3rddream03
            mc_t "Ha!"
            mc_t "Yeah, just as I thought... she's too reckless."

            show ep01_3rddream02
            anto "OMG!"
            anto "Eh..."
            anto "[mc_name]???"
            mc_s "WATCH..."

    $ playAudio(sfx_bodyfall_carpet, "sfx", 1, False, 0, 0)

    show ep01_3rddream04 with vpunch
    anto "AAAAHHHH!!!"
    mc_s "... Out."
    mc_t "Ouch, that must have hurt."

    show ep01_3rddream05
    anto "Ouch..."
    mc_s "Are you okay?"

    show ep01_3rddream06
    anto "I'm so embarrassed..."
    anto "I can't even look at you now."
    mc_s "No worries."
    mc_s "Hey..."

    $ playAudio(antonella_love, "music", 1, True, 2.5, 0)

    show ep01_3rddream07 with hpunch
    mc_s "Let me help you up."

    show ep01_3rddream08 with vpunch
    anto "Thank you, [mc_name]."
    mc_s "So... Uhm."
    mc_s "I know I'm gonna regret asking you this, but..."
    mc_s "What exactly were you trying to do up there?"
    anto "Falling down, did you not see?"
    mc_s "Oh, come on."

    show ep01_3rddream09
    anto "Let's see..."
    anto "I couldn't find the librarian in her seat."
    anto "So I started looking for her stamp to check out this book."
    mc_s "Wouldn't that get you into trouble?"
    anto "She knows me."
    anto "And she knows that I virtually live here, so it's fine."
    mc_s "Uhm..."

    $ unlock_memory("m_ep01_library")

    show ep01_3rddream10
    anto "Oh... I almost forgot."
    anto "Oh, and thanks for spooking me."
    mc_s "I'm sorry, I didn't mean it."

    show ep01_3rddream11
    anto "Next time I'll throw a book at you."
    mc_s "Okay..."
    anto "And what are you doing here anyway? Don't tell me you're actually here to read? Impossible."
    mc_s "Actually, I like to read."
    anto "Yeah, sure."
    show ep01_3rddream12
    anto "Nah-uh. I bet you came to find me."
    anto "Aren't you tired of chasing after me?"
    mc_s "You think highly of yourself, Antonella."
    anto "Why? Don't you? Admit it."
    anto "You want me, and it's driving you crazy."
    mc_s "Not really."

    show ep01_3rddream13
    anto "WHAT?!"
    anto "Excuse me???"
    mc_s "Well, you heard me."
    anto "Honestly... Boys these days."
    show ep01_3rddream14
    mc_s "Fine, then."
    mc_s "You're annoying."
    anto "BAH!!!"
    anto "Say whatever you want. I'm not listening."
    mc_s "Ok, bye then."

    show ep01_3rddream15
    mc_t "I guess I was a bit of a jerk... But I told her what was on my mind."
    mc_t "Oh... She's looking over here... maybe I should--"

    show ep01_3rddream16
    anto "One more thing."
    mc_s "Hmmm?"
    anto "Since we're talking about truth, I also have something to say to you."
    mc_s "Okay?"
    anto "You're a blind loser."
    mc_s "Huh?"

    show ep01_3rddream17
    anto "L-O-S-E-R. Got it?"
    anto "A complete idiot who can't see what's right in front of him."
    mc_s "Uhhh... Are you done?"

    show ep01_3rddream18
    anto "Stay away from me, okay?"
    anto "That's all."
    anto "Goodbye."
    mc_s ". . ."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with clouds
    show ep01_3rddream19 with bokeh
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)

    mc_t "Huh?"

    $ playAudio(sfx_phone, "sfx", 1, True, 0, 0)

    mc_t "Ugh... The fucking phone."
    ##SMS WINDOW
    call screen phone_icons("ep01_sms01")
    $ stopAudio(channel="sfx", subchannel=1, fadeout=1)

    show ep01_3rddream20 with slowfade
    mc_t "Fuck it! I wanna sleep..."

    jump ep01_smslater




label ep01_smslater:
    scene eigengrau with dissolve
    show ep01_3rddream22 with slowfade
    mc_t "Why was she looking at me? I just want... to...sleeeep...."
    mc_t ". . ."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_pregame




label ep01_pregame:
    scene eigengrau with clouds_inverse
##RM.POINTS.TRACK (antonella, trust, +1)
# --
## -- SCENE: ANTONELLA'S FAVOR
    show ep01_pregame01 with clouds_inverse
    $ playAudio(sfx_park2, "amb", 1, True, 1.5, 0)

    mc_t "Antonella asked me to meet her at the park today. She said she had something to tell me."
    mc_t "I don't understand why she wants me to meet her there, but I guess I'll find out soon."
    mc_t "I just hope she doesn't do anything crazy."
    mc_t "There's no telling with her."

    show ep01_pregame02 with slowfade
    mc_t "There's no sight of her anywhere."
    mc_t "Am I too early? Or did she change her mind?"
    mc_t "Maybe she decided not to show up.  I wouldn't blame her, to be honest."
    mc_t "Who wants to waste their time with a guy like me anyway?"
    mc_t "And why am I waiting for her anyway? It's not like she's my girlfriend or something."
    mc_t "Huh..."
    mc_t "This is stupid. She probably forgot about me already."
    mc_t ". . ."
    mc_t "Forget her, forget this. I should just head to school."
    mc_t "Stupid, Antonella... I never liked you in the first place."

    $ playAudio(antonella_love, "music", 1, True, 1, 0)

    show ep01_pregame03 with vpunch
    anto "Um, hey."
    mc_s "Hi..."

    show ep01_pregame04
    anto "You waited."
    mc_s "Yeah, I did."
    anto "Cool, that's, uhh... Impressive, I guess."
    mc_s "Where were you?"
    mc_t "Be careful, [mc_name]. You don't want to sound too desperate."
    mc_t "Have I been waiting for her for an hour? Yup. Definitely needy."

    show ep01_pregame05
    anto "Uh... I was dealing with something. And I'm sorry I made you wait."
    mc_s "Okay."
    mc_t "Wait, is she actually apologizing? Antonella?"

    show ep01_pregame06
    anto "Anyway, um... I called you here for a reason."
    anto "Ummm...."
    anto "Can I... just... sit here?"
    mc_s "Of course."

    show ep01_pregame07
    anto "Can you, umm, scoot over?"
    mc_s "Right, right! Sorry, Antonella."

    show ep01_pregame08 with slowfade
    mc_t "Crap... what is this feeling? I've never felt this way before."
    mc_t "Heart pumping, palms sweaty, the whole nine yards."
    mc_t "Surely she doesn't feel the same way, right? She's my friend. Well, sort of. But not like that."
    mc_t "Then again, when she looks at me like that, I can't help but feel like there's something else going on."
    mc_t "Alright, [mc_name]. Just play it cool, like a normal dude who isn't having an existential crisis."
    mc_s "Wait, what the hell? Why aren't you dressed for school?"

    show ep01_pregame11
    anto "I won't be going to school today. That's why I called you here."
    mc_s "Huh?"

    show ep01_pregame10
    anto "Neither are you, by the way."
    mc_s "Antonella, you can't be serious."
    anto "As a heart attack."
    mc_s "But we have exams!"

    show ep01_pregame09
    anto "Do I look like I care?"
    anto "Do you?"
    mc_t "Something inside me is telling me to say no and run to school. But... Antonella's smile... her eyes... her laugh..."
    anto "Do you care?"
    anto "Do you wanna stay and hang out with me? Just us two, all day long. No adults. No teachers. No one to bother us."
    mc_s "Actually..."

    show ep01_pregame12 with vpunch
    anto "Because I definitely do, [mc_name]."
    mc_s "But, where will we go?"
    anto "Let me handle that."
    mc_s "Antonella..."
    anto "Just follow my lead."
    show ep01_pregame13 with slowfade
    anto "Just trust me. Besides you owe me one, after what you did at the library."
    anto "We're friends, right? So... you can always trust me."
    anto "Or maybe... something else."
    anto "Hmmm..."
    anto "How about... you think about that while we walk?"
    anto "Hello? You awake there?"
    mc_s "Huh? Uh..."
    anto "[mc_name], cmon! Are you gonna make me drag you?"
    mc_t "Okay, keep it together, [mc_name]. It's not the end of the world if you skip a few classes."
    mc_t "Why is she so damn cute though? Maybe I like her more than I realized. Wait, I shouldn't even think about this. We're just friends."
    mc_t "AGAIN, just friends."
    mc_s "Alright, alright. I'm coming. Wherever we're going, just lead the way, Antonella."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    ## MOTHER'S OFFICE
    scene eigengrau with dissolve
    show ep01_pregame14 with slowfade
    $ playAudio(sfx_earlymor, "amb", 2, True, 2, 0)

    mc_s "So where are we?"
    anto "My [mo_r_low]'s work. And I figured, since we can't go to school, this would be a great place to spend  some time."
    anto "Isn't it awesome?"
    anto "This place is empty most of the time. Except when my [mo_r_low] has meetings or exhibitions."
    mc_s "It's nice."

    show ep01_pregame15
    mc_s "And quiet."
    anto "You better not ruin this with your sarcasm. Or I might have to kick your ass."
    mc_s "And I thought you invited me here to make amends."
    anto "Make amends???"
    anto "Oh please, don't make me laugh, [mc_name]."
    mc_s "Ahh, ok..."

    show ep01_pregame16 with hpunch
    mc_s "Why are you staring at me like that, Antonella?"
    anto " No reason. Just..."
    anto "Looking at you, I guess. Nothing else."
    mc_s "Uh, ok?"
    anto "Why? Do I make you uncomfortable? You know, we are alone here, and no one knows where you are. I could do anything to you and no one would stop me."
    mc_s "W-what???"

    show ep01_pregame17
    anto "Come on, I'm just playing."
    anto "Kinda... unless you want me to be serious."
    mc_s "Um..."
    anto "Don't worry, I'll keep my hands to myself."
    mc_s "That's good, I guess."

    show ep01_pregame18
    anto "Look. I'll be right back, okay?"
    anto "Give me five minutes, I got to grab something from my [mo_r_low]'s office."
    anto "You're not gonna die in that time, right? Hahaha."
    mc_s "Yeah, yeah, very funny."

    show ep01_pregame19 with slowfade
    mc_t "God, what I'm doing here?"
    mc_t "She makes me so confused and lost in my thoughts."
    mc_t "Do I... like her, like really like her? Or just as a friend?"
    mc_t "Man... I can't believe I'm having this conversation with myself."
    anto "Hey..."
    show ep01_pregame20 with hpunch
    anto "Here you go."
    mc_s "What is this?"
    anto "You like to read, don't you? Here you go. It's a book of mine. "
    show ep01_pregame21
    mc_s "Y-Yes, but..."
    anto "Just take it... and read the damn thing!"
    mc_s "Um..."

    show ep01_pregame22
    anto "Umm... Just trust me, okay? Please?"
    mc_s "O-okay... Did you read this book?"
    anto "Yeah, but... You saw me reading it, remember? On the floor. At the school hall."
    show ep01_pregame23 with slowfade
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(antonella_past_theme, "music", 2, True, 1.5, 0)

    mc_s "I remember. So why are you giving it to me?"
    anto "Umm... you'll find out if you read it."
    mc_s "Okay... but why me? Don't you like this book? Why not give it to someone else?"
    anto "Isn't it obvious? I wanted to give it to you. You're the one I wanted to share it with."
    mc_s "I just don't want this to be some sort of prank. That's all."

    show ep01_pregame24
    anto "No pranks. Trust me. "
    anto "But, you know what? Don't trust me. Find out for yourself if I'm lying or not. Just read the damn book."
    mc_s "Alright... I'll do that."
    mc_s "You just make me so confused sometimes, Antonella."

    show ep01_pregame25
    anto "Okay..."
    mc_s "Nonetheless it's a sweet gesture. Thank you, Antonella."
    anto "It's nothing."
    mc_s "Thank you, really. And did you like this book?"
    anto "Are you asking me that because you think I didn't?"
    mc_s "No, no, not like that..."

    show ep01_pregame26
    anto "Because you are right. I didn't."
    anto "I'm giving it to you because I didn't like the ending. That's it. And I want you to experience the same disappointment."
    mc_s "Wait, what???"
    anto "Um... yeah... Life sucks, and so do books sometimes--"
    mc_s "Okaaaaaay..."

    show ep01_pregame28
    anto "If you had let me finish what I was saying... I would have told you that I didn't like the ending because I found the way the author ended things so..."
    mc_s "Huh?"
    anto "The ending was all wrong. It was like the author took everything that mattered and just... twisted it. Perverted it. Until nothing made sense anymore."
    anto "But maybe that's the point... the world doesn't make sense... people aren't who you think they are."
    anto "They just wear masks, hiding their true selves. Until they've already destroyed everything you ever cared about."
    mc_s "Antonella, what's going on? You're not making any sense. It's just a book, right? Why are you getting so worked up about it?"

    show ep01_pregame27
    anto "O-oh... um, nothing. Just talking nonsense, as always. But uhm, keep the book anyways."
    mc_s "Can I ask you a personal question?"
    anto "Personal? Wait, uhm... sure..."
    mc_s "Ok... Before meeting me, were you always alone? I mean, because I've never seen you with other people besides me."
    anto "Yes... yes I was always alone... As far as I remember."
    mc_s "I don't think you have to be alone, Antonella. You could have friends, Antonella. Lots of them if you wanted to. You're smart, beautiful, and funny."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_pregame29 with hpunch
    anto "Thank you [mc_name], but no. My life is fine this way. Without any unnecessary complications, or relationships to worry about."
    anto "And I have a hard time trusting people, you know? Because there's no point in getting attached when they could turn around and leave you at any moment."
    mc_s "Why would they do that?"
    anto "Because that's what people do. Even if they say they'll be there for you, they don't mean it. So it's just easier for me to take care of myself instead of waiting around for someone else."
    anto "What about you, though? Why did you spend so much time with me? Especially after I kept pushing you away?"
    mc_s "Hmmmm..."
    anto "Come on! There must be some reason."
    mc_s "Maybe it's because I knew how lonely it could feel to be without friends."

    show ep01_pregame30 with hpunch
    mc_s "And I thought that if I stayed by your side, maybe one day you'd let me in and see who you really were beneath all of that anger and sarcasm."
    anto "Wow.... [mc_name]...."
    anto "That's amazing... And unexpected."
    anto "Just kidding hahaha, we're best buddies now, right?"
    $ show_walkthrough("ep01_pregame_menu")
    menu:
        "Hug tenderly":
            $ rm.update("antonella", "trust", 3)
            $ check_levels("antonella", "trust", 3)
            $ ep01_hug = True
            hide screen walkthrough_screen
            show ep01_pregame31 with hpunch
            mc_s "I like you the way you are."
            mc_s "And you're not alone anymore."

            show ep01_pregame32
            anto "Let's stay like this for a bit."
            mc_t "I can't imagine what it's like to live her life with so little trust. I will show her she can rely on me no matter what. "
        "Hesitate awkwardly":
            hide screen walkthrough_screen
            show ep01_pregame33 with vpunch
            mc_t "Goddammit. We were having a moment! Why couldn't I just hug her? Ughhh."
            mc_t "\"Maybe one day you'd let me in and see who you really were\"????? What the hell was that supposed to mean?"
            mc_t "Oh man..."
            mc_t "Lots of words, no action."
            anto "Anyways... Where were we before... Oh, right..."
            mc_s "Uhm..."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    ## PHONE CALL #2
    scene eigengrau with clouds
    show ep01_pregame34 with bokeh
    $ playAudio(sfx_train_ext, "amb", 1, True, 1, 0)
    $ playAudio(sfx_phone, "sfx", 1, True, 0, 0)

    mc_t "What?"
    mc_t "Again?"
    mc_t "Damn it... Now, who is it?"
    ##SMS WINDOW
    call screen phone_icons("ep01_sms02")
    show ep01_pregame35 with slowfade
    $ stopAllSubchannels(channel="sfx", fadeout=1.5)

    mc_t "Fuck! I'm not in the mood for this!"
    mc_t "I..."
    mc_t "I just wanna see HER again..."
    mc_t ". . ."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_pregame2




label ep01_pregame2:
    scene eigengrau with clouds_inverse
    ##BACK TO DREAM
    show ep01_pregame37 with clouds_inverse
    nvl clear
    $ playAudio(sfx_earlymor, "amb", 2, True, 2, 0)
    anto "You know... This book is not really free. There's one condition."
    mc_s "I knew it! There's always a catch with you."
    anto "What's that supposed to mean?"
    mc_s "Nothing, just tell me. What's the condition?"
    anto "Asshole..."
    show ep01_pregame38
    anto "Okay... It's simple. Next month is my birthday and my parents are forcing me to have a party."
    anto "So they want me to invite my friends."
    mc_s "You don't have any friends."

    show ep01_pregame39
    anto "I know that already... but they don't."
    anto "So I decided to ask you to come with me and pretend like we're the best of friends and stuff."
    anto "I mean, you're the only friend I have. So yeah..."
    anto "Please don't let me down and help me seem normal or whatever."
    mc_s "Nope."

    show ep01_pregame40
    anto "OMG!!! Why? You won't even help me with my problem?!"
    anto "Am I such an annoying bitch? Is that what it is?"
    mc_s "No, no, that's not why I said no. It's just that you forgot to add another condition to this... If I help you out at your birthday, then you owe me something in return."

    show ep01_pregame41
    anto "Fuck you, dude. Don't blackmail me."
    mc_s "So are you inviting me to your birthday or not?"
    anto "Ughh! Fine! My birthday is October 11th, a Saturday, at 3 pm. Come dressed appropriately and no presents. Got it?"
    mc_s "As friends, right? Or more than that? Haha."
    ##ADD POINTS... LOW POINT NO THE GAME, 5 POINTS GO TO  THE GAME
    if rm.get("antonella", "trust") < 2:
        anto "Not funny! Now let's get out of here before my [mo_r_low] comes back and asks who you are."
        jump q3_date


    else:
        anto "Don't get any funny ideas in your head. It's not like that, ok? Not yet at least."
        pass
    show ep01_pregame42
    anto "But now that you mention it..."
    anto "We could pretend to be together in front of my parents... Wouldn't that be hilarious?"
    mc_s "Uhmm... What about later on? After the birthday?"

    show ep01_pregame43
    anto "Later? Hmmm... I don't know. That will depend on your behavior..."
    mc_s "Oh... I didn't expect that."

    show ep01_pregame44
    anto "Alright... let's say that if you're good at this birthday thing, I might actually kiss you. Maybe."
    mc_s "Seriously??"
    anto "Why not? But don't get excited, I might end up hating it."
    mc_s "Thanks for the honesty, I can live with that."

    show ep01_pregame45
    anto "Good. Now let's stop talking about it. You're making me feel awkward."
    mc_s "You know, for someone who is a loner, you seem to care a lot about appearances."
    anto "You wouldn't get it. When you're me, you need to worry about shit like that. Okay? So don't judge me. So if I can make them see what I want, then it's fine, ok?"
    mc_s "Huh? I mean, I guess I see your point..."

    show ep01_pregame46  with slowfade
    mc_s "Anyway, if that's all you wanted to ask me..."
    mc_s "I'll get going."
    anto "Umm, actually..."
    show ep01_pregame47
    anto "Would you um, wait a little? Please? I wanted to ask you something else..."
    anto "I, umm. Just um..."
    anto "Would you, like, uhh, stay for a bit longer? Here, at my [mo_r_low]'s office, I mean... with me? If you're not in a hurry or anything... I just need um, a friend right now, you know... you... you're not gonna say no, right?"
    mc_s "What are you planning now, Antonella? It sounds really suspicious, you know?"

    show ep01_pregame48
    anto "Planning something? Who? Me? Nah... but I was thinking..."
    mc_s "Antonella...?"
    anto "We could use my [mo_r_low]'s office here for other purposes..."
    mc_s "I see... Is this one of your jokes again?"
    anto "Do you think so? Hmmm... How about you check it out for yourself then?"
    show ep01_pregame49
    anto "My idea of doing it there looks pretty tempting to me."
    mc_s "Are you kidding me??? Do what???"
    anto "Silly [mc_name], what do you think we're gonna do together at this time of the day on a sofa?"
    show ep01_pregame50
    anto "But that's only if you want to, of course."
    anto "Unless that scares you, and then you can go home..."
    mc_s "Antonella, is this seriously what you want from me?"
    anto "Obviously yes! Cmon [mc_name]. Why wouldn't I want it?"
    mc_s "I... uhmmm..."

    show ep01_pregame51
    anto "Already feeling uncomfortable now that things are getting interesting, huh?"
    mc_s "Not really. But... aren't we moving a bit fast right now? This is kind of sudden..."
    anto "Fast? What are you talking about?"
    mc_s "Don't get me wrong... I'm just trying to say that I didn't expect us to end up like this today... So yeah, it's quite surprising..."

    show ep01_pregame52
    anto "So.... Let me understand this correctly... You don't want to..."
    mc_s "No! No! I never said that!"

    show ep01_pregame53
    anto "Well, fine then. Don't blame me if you miss out on the best game ever created."
    mc_s "Huh? A game? What game? I thought you meant we were going to... well... you know..."

    show ep01_pregame54
    anto "Wait... what? Wow... YOU thought that I would be doing THAT with you?"
    mc_s "Of course! How was I supposed to know it was just one of your stupid games?!"
    anto "And you still agreed to it...?? Oh my God..."
    mc_s "Okay... fine. What's the stupid game anyway?"

    $ playAudio(antonella_game_theme, "music", 2, True, 2.5, 0)

    show ep01_pregame55
    anto "Took you long enough to ask. It's really simple. It's called... 'Let's Improvise Something.' I came up with the name myself. It's kinda genius if you ask me."
    anto "Basically, we both have to ask each other three questions..."
    anto "First, you do it, then I do it, and so on. Get it?"
    jump ep01_thegame




label ep01_thegame:
    scene eigengrau with slowfade
## -- SCENE: ANTONELLA'S GAME REVEAL
    show ep01_game01 with dissolve
    mc_s "Sorta."
    anto "Right. But there's a twist. Whoever makes a mistake--"
    mc_s "--Is the loser, I guess."

    show ep01_game02
    anto "Yep, but not only that, they have to do a penalty task ..."
    anto "Wanna know what the penalty is?"
    mc_s "Do I have a choice?"

    show ep01_game03
    anto "For every mistake made, you have to take off one piece of clothing."
    mc_t "What????? She wants me to get naked? In front of her?"
    mc_t "On the other hand, if I win, she will do the same. It wouldn't hurt to try."
    mc_s "Ok, fine. I'll play."

    show ep01_game04
    anto "Sweet, I'm really excited. This is gonna be fun!"
    mc_s "Go ahead then. Ask whatever question you want."

    show ep01_game05
    anto "Not so fast, dude.  You don't even know what topic we're going to quiz each other on, right? It has to be a topic we're both familiar with, doesn't it?"
    anto "And I think we know the perfect topic."
    anto "Literature... We both like books after all, right?"
    mc_s "Of course... how could I forget..."

    show ep01_game06
    anto "Awww... You don't seem too happy about this little game."
    anto "Ummm... Now that I think about it... maybe you should choose something else as our subject?"
    anto "What do you say?"
    mc_s "Hell no! Literature is fine with me. Let's do it."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_game07
    anto "Yes! Excellent. Ok then. Time to begin, I guess."
    mc_s "Just one quick question before we start though... Who goes first?"
    anto "Since I suggested this game, it's only fair if you go first..."
    mc_s "Wow, I didn't expect you to be so nice."
    anto "Think you can handle the pressure, [mc_name]?"
    anto "Anyway, I'm ready."
    $ playAudio(mc_thinking_theme, "music", 2, True, 2.5, 0)
##1ST QUESTION BY MC
    show ep01_game08 with slowfade
    mc_t "What kind of question can I ask that would make her take something off if she fails?"

    $ show_walkthrough("ep01_game_menu1")
    $ ep01_q1 = random_menu(
        # The character who speaks before the menu. If none, use None.
        mc_s,
        "My first question is...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Ask about an American writer", "q1_usa"),
            (True, "Ask about an Argentine writer", "q1_arg"),
            (True, "Ask about an English writer", "q1_uk"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q1 == "q1_arg":
        hide screen walkthrough_screen

        mc_s "Do you know the name of the person who wrote \"Hopscotch\"?"

        $ ep01_mcquestion += 1
        jump ep01_mcpoint_1


    elif ep01_q1 in ["q1_usa", "q1_uk"]:
        hide screen walkthrough_screen
        if ep01_q1 == "q1_usa":
            mc_s "Who was the author of \"The Murders in the Rue Morgue\"?"
        else:
            mc_s "Who wrote \"Othello\"?"

        show ep01_game18 with vpunch
        anto ". . ."
        mc_s "So? What's your answer?"
        mc_t "I think I got her."

        show ep01_game19
        if ep01_q1 == "q1_usa":
            anto "Edgar Allan Poe."
            anto "I think you better be more creative than that, [mc_name]."
        else:
            anto "William Shakespeare."
            anto "I think you better step up your game or else I might win before we even get started..."
        show ep01_game20
        mc_s "Ahhhh... You're enjoying this a bit too much. But alright."
        mc_s "I guess this will do for now."
        mc_t "Damn, I fucked up..."

        $ ep01_mcquestion += 1
        jump ep01_thegame_q2




label ep01_mcpoint_1:
    scene eigengrau with slowfade
##MC WINS 1 POINT FOR THE FIRST TIME
    show ep01_game09 with hpunch
    mc_t "Got her?"
    mc_t "Yes!"
    mc_t "I see her confident look beginning to fade."
    if ep01_mcquestion == 1:
        mc_s "What happened?"
    elif ep01_mcquestion == 2:
        mc_s "Who's the main character in \"Demian\""
    else:
        pass
    show ep01_game10 with vpunch
    if ep01_mcquestion == 1:
        anto "Uhm... Well, I think his name was Adolfo Bioy."
        mc_s "Wrong! The author was Julio Cortazar..."
        mc_s "Give me your shirt. And no arguments about it. You know the rules, Antonella..."
    elif ep01_mcquestion == 2:
        anto "Uhm... Well, obviously Max Demian."
        mc_s "I'm amazed at your guessing skills... And... you blew it!"
        mc_s "Close, but no cigar. It's Emil Sinclair."
    else:
        anto "Shit!"
        anto "I have no idea... Sherlock Holmes?"
        mc_t "YES!!! I got a point!."

    show ep01_game11 with hpunch
    mc_t "Trying to be sweet and cute won't work on me this time."
    mc_t "Should I feel sorry for her? As if."
    mc_t "I bet she will definitely think of a way to trick me now..."

    $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.5)
    $ playAudio(antonella_sexy_theme, "music", 4, True, 1.5, 0)

    show ep01_game12 with slowfade
    anto "Well... I won't take my shirt off. I will take off my sweater. Because it does count as clothing, right?"
    mc_t "I knew it! She always looks for loopholes."

    show ep01_game13 with flash
    anto "Oh, by the way... you got lucky this time."
    anto "Don't think I didn't notice."
    show ep01_game14 with flash
    anto "I noticed your shitty little grin when you got one point against me."
    if ep01_mcquestion <= 2:
        anto "Next time won't be so easy."
    show ep01_game15 with flash
    if ep01_mcquestion <= 2:
        anto "Besides, now my question for you will be even more difficult..."
    else:
        anto "I let you win, so don't get any ideas."
    show ep01_game16  with flash
    if ep01_mcquestion <= 2:
        anto "So I would take this opportunity to start thinking of some really, really hard questions. Or you're going to suffer the consequences."
    mc_t "She's so cute when she gets all pouty after a loss..."

    show ep01_game17
    $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
    anto "Got it?"
    if ep01_mcquestion <= 2:
        mc_s "Yes, yes... Whatever you say, princess. Ask your stupid question so I can beat you again."
        anto "Okay, my turn."
    else:
        mc_s "Yeah... sure."

    $ ep01_anto_clothing += 1
    if ep01_mcquestion == 1:
        jump ep01_thegame_q2


    elif ep01_mcquestion == 2:
        jump ep01_thegame_q4




label ep01_thegame_q2:
    scene eigengrau with dissolve
##1ST QUESTION BY ANTONELLA
    show ep01_game21 with slowfade
    anto "I'll start with something relatively easy!"
    anto "Just because I'm a good girl."
    mc_t "I know I can do it!"
    anto "Who wrote \"The Prince\"?"
    $ show_walkthrough("ep01_game_menu2")
    $ ep01_q2 = random_menu(
        # The character who speaks before the menu. If none, use None.
        mc_t,
        "Who the hell wrote that...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Niccolò Machiavelli", "ep01_q2_1"),
            (True, "Dante Alighieri", "ep01_q2_2"),
            (True, "Umberto Eco", "ep01_q2_3"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q2 == "ep01_q2_1":
        hide screen walkthrough_screen

        mc_s "Was it Niccolò Machiavelli?"

        show ep01_game23
        anto "You surprise me, [mc_name]."
        mc_s "I told you so."

        jump ep01_thegame_q3


    elif ep01_q2 in ["ep01_q2_2", "ep01_q2_3"]:
        hide screen walkthrough_screen
        if ep01_q2 == "ep01_q2_2":
            mc_s "Was it Dante Alighieri?"
        else:
            mc_s "Was it Umberto Eco?"

        show ep01_game25
        if ep01_q2 == "ep01_q2_2":
            anto "Ehhh... wrong answer. You know what to do."
        else:
            anto "No! How can you say that. Anyways, you know what to do."
        mc_s "Damn it!"
        anto "I think I'm starting to enjoy this game."
        $ ep01_mc_clothing += 1
        jump ep01_thegame_mc_nude




label ep01_thegame_mc_nude: ##*
    scene eigengrau with slowfade
##MC NUDE ANIMATION
    if ep01_mc_clothing == 1:
        show ep01_game27 with dissolve
        mc_s "Can't see why you're so happy."
        mc_s "Guess I'll ditch my sweater."
        if ep01_mcquestion == 1:
            jump ep01_thegame_q3


        elif ep01_mcquestion == 2:
            jump ep01_thegame_q5


        else:
            hide ep01_game94
            hide ep01_game107
            jump ep01_endgame


    elif ep01_mc_clothing == 2:
        show ep01_game28 with dissolve
        mc_s "Really? You like what you see?"
        mc_s "Christ, this game blows."
        if ep01_mcquestion == 2:
            jump ep01_thegame_q5


        else:
            hide ep01_game94
            hide ep01_game107
            jump ep01_endgame


    else:
        show ep01_game29 with dissolve
        mc_s "Fuck!" 

        show ep01_game32 with hpunch
        anto "Didn't expect you to be hiding such a smokin' bod."
        mc_s "Not cool."

        jump ep01_endgame




label ep01_thegame_q3:
    scene eigengrau with slowfade
##2ND QUESTION BY MC
    show ep01_game33
    anto "Well, throw me the next question..."
    if ep01_anto_clothing == 1:
        anto "Now that the sweater is out of the way... I won't show any mercy to you."
    else:
        anto "Ask me a tricky one so I can watch you squirm..."
    $ show_walkthrough("ep01_game_menu3")
    $ ep01_q3 = random_menu(
        # The character who speaks before the menu. If none, use None.
        mc_t,
        "What should I ask?",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Ask about \"A Tale of Two Cities\"", "q3_2city"),
            (True, "Ask about \"The Little Prince\"", "q3_lilprince"),
            (True, "Ask about \"Demian\"", "q3_demian"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q3 == "q3_demian":
        hide screen walkthrough_screen
        if ep01_anto_clothing == 0:
            $ ep01_mcquestion += 1
            jump ep01_mcpoint_1


        else:   
            $ ep01_mcquestion += 1
            jump ep01_mcpoint_2


    elif ep01_q3 in ["q3_2city", "q3_lilprince"]:
        hide screen walkthrough_screen
        show ep01_game45
        if ep01_q3 == "q3_2city":
            mc_s "Which cities are important in \"A Tale of Two Cities\"?"
        else:
            mc_s "Who lived on asteroid B612?"
        if ep01_anto_clothing >= 1:
            mc_t "You're gonna mess up again. Just watch."
        else:
            mc_t "Hope you screw up this time, Antonella."

        show ep01_game47
        if ep01_q3 == "q3_2city":
            anto "London and Paris, my friend."
            anto "Your strategy didn't work this time, dude."
        else:
            anto "That is so easy... The Little Prince."
            anto "Outsmarted you, didn't I?"
        show ep01_game49
        mc_t "Fuck! That cockiness of hers is one of her biggest strengths."
        mc_s "You impress me!"

        $ ep01_mcquestion += 1
        jump ep01_thegame_q4




label ep01_mcpoint_2:
    scene eigengrau with slowfade
##MC WINS 2 POINTS (or 1 if failed)
    if ep01_anto_clothing == 0:
        jump ep01_mcpoint_1


    else:
        show ep01_game35 with dissolve
        mc_s "Who's the main character in \"Demian\"?"
        mc_t "Putting a lot of thought into it, huh?"
        mc_s "So?"

        show ep01_game36
        anto "Uhm... Well, obviously Max Demian."
        mc_s "I'm amazed at your guessing skills..."
        mc_t "Gotcha!"

        show ep01_game37 with hpunch
        mc_s "And... you blew it!"
        anto "Wha-?!"
        mc_s "Close, but no cigar. It's Emil Sinclair."
        mc_t "YES!"
        mc_t "Another point for [mc_name]!"

        $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=4, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)

        show ep01_game38 with slowfade
        anto "You know..."
        anto "Starting to think this wasn't a great idea."
        show ep01_game39 with flash
        anto "This was supposed to leave YOU naked, not me."
        anto "And now look at me!"
        show ep01_game40 with flash
        anto "I am one question away from being in my underwear."
        show ep01_game41 with flash
        anto "And I'm pretty sure you're enjoying it..."
        anto "Or am I wrong?"
        show ep01_game42 with flash
        mc_s "Can't deny it!"

        $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)

        show ep01_game43
        anto "You know? Deep down, I'm glad you're happy."
        show ep01_game44
        anto "But this ends now..."
        anto "Got it??!!"
        mc_t "She's so hot... But kinda intimidating too..."
        mc_s "Got it."

        $ ep01_anto_clothing +=1
        jump ep01_thegame_q4




label ep01_thegame_q4:
    scene eigengrau with slowfade
##2ND QUESTION BY ANTONELLA
    show ep01_game51 with dissolve
    anto "Alright, let's see if you've got this one!"
    anto "Tell me... Who wrote \"Lolita\"?"
    mc_t "Ah, damn, what was his name again?"
    anto "Well???"
    $ show_walkthrough("ep01_game_menu4")
    $ ep01_q4 = random_menu(
        # The character who speaks before the menu. If none, use None.
        mc_t,
        "I remember it was a Russian dude...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Nikos Kazantzakis", "ep01_q4_1"),
            (True, "Vladimir Nabokov", "ep01_q4_2"),
            (True, "Fyodor Dostoevsky", "ep01_q4_3"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q4 == "ep01_q4_2":
        hide screen walkthrough_screen

        mc_s "Was it Vladimir Nabokov?"

        show ep01_game52 with hpunch
        anto "Ha, I thought you were gonna mess this one up..."
        anto "Guess I was wrong..."
        mc_s "Wrong indeed, haha!"

        jump ep01_thegame_q5


    elif ep01_q4 in ["ep01_q4_1", "ep01_q4_3"]:
        hide screen walkthrough_screen
        if ep01_q4 == "ep01_q4_1":
            mc_s "Was it Nikos Kazantzakis?"
        else:
            mc_s "Was it Fyodor Dostoevsky?"

        show ep01_game59 with hpunch
        anto "You're crazy!"
        anto "Now, it's your turn to lose something..."
        show ep01_game56
        mc_s "God damn it!!"

        $ ep01_mc_clothing += 1
        jump ep01_thegame_mc_nude




label ep01_thegame_q5:
    scene eigengrau with slowfade
##3RD QUESTION BY MC
    show ep01_game64 with dissolve
    mc_t "Alright... It's my last question for her, I gotta make this really good."

    $ show_walkthrough("ep01_game_menu5")
    $ ep01_q5 = random_menu(
        # The character who speaks before the menu. If none, use None.
        mc_s,
        "Ughh... Okay... Here goes nothing...",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "Something about Agatha Christie", "q1_agatha"),
            (True, "Something about \"The Count of Monte Cristo\"", "q1_mcrist"),
            (True, "Something about \"War and Peace\"", "q1_warpeace"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q5 == "q1_agatha":
        hide screen walkthrough_screen

        mc_s "What's the name of the detective in Agatha Christie's works?"
        mc_t "Well... If God exists, he'll give me this one."

        $ ep01_mcquestion += 1
        jump ep01_mcpoint_3


    elif ep01_q5 in ["q1_mcrist", "q1_warpeace"]:
        hide screen walkthrough_screen
        if ep01_q5 == "q1_mcrist":
            mc_s "Did Marcel Proust write \"The Count of Monte Cristo\"?"
        else:
            mc_s "Was \"War and Peace\" written by Fyodor Dostoevsky?"
        mc_t "Please... screw up this time."

        show ep01_game67
        if ep01_q5 == "q1_mcrist":
            anto "Are you kidding? Alexandre Dumas wrote it!"
        else:
            anto "Obviously not. It was by Leo Tolstoy."
        mc_s ". . ."

        show ep01_game71 with hpunch
        mc_s "Congratulations."
        mc_t "I blew my last chance."

        $ ep01_mcquestion += 1
        jump ep01_thegame_q6




label ep01_mcpoint_3:
##MC WINS 3 POINTS (or less if failed)
    if ep01_anto_clothing == 0:
        jump ep01_mcpoint_1


    elif ep01_anto_clothing == 1:
        jump ep01_mcpoint_2


    else:
        show ep01_game70 with vpunch
        anto "Shit!"
        hide ep01_game64
        anto "I have no idea... Sherlock Holmes?"
        mc_t "YES!!! I win."
        mc_s "Ha..."
        mc_s "I suggest you stand up and remove the last piece of clothing you're wearing."

        show ep01_game64 with hpunch
        anto "..."
        $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=4, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)

        show ep01_game72 with slowfade
        anto "I'm standing up because I really don't know his name."
        show ep01_game73 with flash
        mc_s "His name is Hercule Poirot."

        show ep01_game74 with flash
        anto "Fucking Hercule."
        mc_s "He's not at fault, haha."

        show ep01_game75 with flash
        anto "You must be so pleased with yourself, huh?"
        anto "Embarrassing me in my own game..."
        show ep01_game76 with flash
        anto "With my own rules!"
        anto "I feel so humiliated..."
        show ep01_game77 with flash
        mc_s "You shouldn't."
        anto "Sure... says the one who's not almost completely naked."
        show ep01_game78 with flash
        mc_s "Anyway, I'm not going to mock you..."
        mc_s "You have an amazing body!!"

        show ep01_game79 with flash
        anto "Do you really mean that?"
        mc_s "You have to be blind not to see it..."

        $ ep01_anto_clothing += 1
        $ setChannelVolume(channel="music", subchannel=4, volume=0, fade_duration=1.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=1.5)
        $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)
        jump ep01_thegame_q6




label ep01_thegame_q6:
    scene eigengrau with slowfade
##3RD QUESTION BY ANTONELLA
    show ep01_game80 with dissolve
    anto "This is the last one, so I'm gonna think it over a bit more."
    anto "Part of me really wants to see you strip down a bit more."
    anto "Alright, here it goes..."
    anto "What's the oldest known piece of literature in the whole damn world?"
    hide ep01_game67
    if ep01_mc_clothing == 0:
        mc_t "If I nail this with a perfect score, she's gotta respect me."
        mc_t "She won't have a choice."
    elif ep01_mc_clothing >= 1:
        mc_t "I've gotta hang onto the clothes I've got left. I can't screw this up."

    $ show_walkthrough("ep01_game_menu6")
    $ ep01_q6 = random_menu(
        # The character who speaks before the menu. If none, use None.
        mc_t,
        "Which one is it?",
        None,  # You can add a prompt here if needed.
        [
            # Add or modify these tuples for your menu options.
            (True, "The Mahabharata", "ep01_q6_1"),
            (True, "The Epic of Gilgamesh", "ep01_q6_2"),
            (True, "Book of the Dead", "ep01_q6_3"),
        ]
    )
    #Replace `response_character_name` with your character's name or variable for the response.
    if ep01_q6 == "ep01_q6_2":
        hide screen walkthrough_screen

        mc_s "Gilgamesh, right?"

        show ep01_game84
        anto "Fuck... I thought you'd mess up."
        mc_s "Haha, you couldn't take me down!"
        anto "Whatever..."
        jump ep01_endgame


    elif ep01_q6 in ["ep01_q6_1", "ep01_q6_3"]:
        hide screen walkthrough_screen
        if ep01_q6 == "ep01_q6_1":
            mc_s "The Indian one?"
        else:
            mc_s "The Dead one?"

        show ep01_game67
        if ep01_q6 == "ep01_q6_1":
            anto "No! That's the longest poem, not the oldest work."
            mc_s "Shit!"
        else:
            anto "You're nuts. That's a mortuary, not literature."
            mc_s "God damn it!!"

        $ ep01_mc_clothing += 1
        jump ep01_thegame_mc_nude




label ep01_endgame:
    scene eigengrau with dissolve
    if ep01_anto_clothing == 3 and ep01_mc_clothing == 0:
        $ ep01_bestprize = True
        jump ep01_endgame_w


    else:
        jump ep01_endgame_f




label ep01_endgame_w:
#THE GAME, BEST SCENARIO#THE GAME, BEST SCENARIO
    $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=1.5)
    $ setChannelVolume(channel="music", subchannel=4, volume=0.5, fade_duration=5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0, fade_duration=1.5)

    show ep01_game87 with hpunch
    anto "Okay..."
    anto "You've been such a good boy, so smart and interesting."
    anto "I think you deserve a prize, don't you think?"
    mc_s "I..."
    mc_t "Is this really happening?"
    mc_s "A... a prize? For real?"

    show ep01_game88
    anto "Yeah, absolutely."
    anto "Why don't you come a little closer?"
    mc_t "She can't be serious. This has gotta be one of her tricks, right?"

    show ep01_game89
    mc_s "Do you actually mean it?"
    anto "Of course I mean it, silly."
    anto ". . ."
    anto "[mc_name]."
    show ep01_game92
    anto "Here, lemme get a bit closer."
    mc_t "Oh my god, my heart's about to burst outta my chest!!"
    mc_s "Wha-"
    mc_s "What are you gonna do?"

    show ep01_game93
    anto "I. . ."
    anto "really. . ."
    anto "like. . ."
    show ep01_game94
    anto "YOU."
    show ep01_game99
    mc_t "Am I dreaming? There's no way this is real..."
    mc_t "Is she really gonna..."

    show ep01_game100
    mc_t "Holy shit, am I actually about to see her totally naked?!"

    show ep01_game101 with slowfade
    anto "They're not as big as I'd like, but---"
    mc_s ". . ."
    mc_s "Are you kidding me right now?"
    mc_s "I..."
    mc_s "I freakin' LOVE them!!!"
    mc_s "I still can't believe they're just... right here in front of me like this."

    show ep01_game103
    anto "So... you really like 'em, huh?"
    anto "You can touch 'em if you want..."
    mc_t "I cannot believe this is happening to me!!!"

    show ep01_game106
    mc_s "I..."
    anto "[mc_name]..."
    anto "I meant my boobs, silly."
    mc_s "Oh, shit!"
    mc_s "My bad."

    show ep01_game110
    anto "But hey, I'm cool with you touching my ass too."
    show ep01_game107
    anto "Go on, don't be shy..."
    show ep01_game111
    anto "Don't hold back on me now."
    mc_t ". . ."

    show ep01_game115 with slowfade
    anto "So...?"
    anto "You don't think they're too small?"
    mc_s "What? No way, not at all..."
    mc_s "They're perfect if you ask me."
    anto "Would you... like a taste?"
    mc_s "Wait, what do you mean?"
    mc_t "Is this really about to go down?"
    mc_t "Could this be the day I finally have my first time?"
    mc_t "Am I seriously gonna have my first time with her, right here, right now?"

    show ep01_game116
    anto "I dunno..."
    anto "You wanna feel 'em?"
    anto "Put 'em in your mouth, see how they taste?"
    mc_t "This is it! Today's the day!!!"

    show ep01_game118
    anto "Please be gentle though."
    show ep01_game119
    anto "I've never done this with anyone before..."
    show ep01_game120
    mc_t "My time has come."

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=1, fade_duration=1.5)

    show ep01_game121
    $ playAudio(sfx_keys, "sfx", 1, True, 0, 0)
    anto "Oh shit! That's my [mo_r_low]!!"
    mc_s "But you said..."
    anto "Shhh... Shut up!!"
    mc_s ". . ."

    show ep01_game122
    anto "[mc_name]..."
    anto "We gotta go..."
    anto "NOW!"
    show ep01_game123
    anto "Quick, hand me my clothes!"
    show ep01_game124
    anto "{size=15}shit ...{/size}"
    show ep01_game125
    anto "{size=25}shit ...{/size}"
    show ep01_game126
    anto "{size=35}SHIT ...{/size}"
    anto "Okay... everything's back where it should be."
    show ep01_game127
    anto "Hey!"
    anto "[mc_name]!"
    anto "What are you waiting for??!!"
    anto "Get up and keep quiet!"
    jump q3_date




label ep01_endgame_f:
#THE GAME, WORST SCENARIO FOR MC#THE GAME, WORST SCENARIO FOR MC
    show ep01_game94 with slowfade
    anto "Looks like you didn't really try in this game. What a letdown..."
    mc_s ". . ."
    mc_s "Seriously?"

    show ep01_game107
    anto "Yep, you totally missed out!"
    mc_s ". . ."
    anto "Guess it's time to get dressed again."
    mc_t "Damn, I fucked up..."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_game95 with fade
    mc_s "Awww... man."
    if ep01_anto_clothing == 0:
        anto "Pity you didn't get to see me strip..."
        anto "Stayed fully clothed the entire time..."
    elif ep01_anto_clothing >=1:
        anto "Lucky me, kept all my essential clothes on, what a shame!"
    show ep01_game96
    anto "I was kinda hoping to lose a bit more..."
    anto "Don't you think?"
    mc_t ". . ."

    show ep01_game97 with hpunch
    mc_s "Oh, shit!"
    anto "Hahaha!"
    show ep01_game98
    anto "Hahaha. Are you alright???"
    mc_s "WTF..."
    anto "You tripped."
    mc_s "Oh, I tripped, huh? Felt more like you pushed me!"

    show ep01_game102 with vpunch
    anto "Is that right?"
    anto "My apologies, then."
    mc_s ". . ."
    anto "Something wrong?"
    mc_s "You're all over me."
    anto "Bother you much?"
    mc_s "No, not really. It's just..."

    show ep01_game104 with slowfade
    anto "Shhh..."
    show ep01_game105
    mc_t "She's so damn gorgeous."
    mc_t "And I'm such a... freakin' coward."

    show ep01_game108
    anto "There's that dumbstruck look again..."
    anto "What's going through your head, [mc_name]?"
    mc_s "You..."
    anto "I..."
    mc_s "You're just too damn beautiful..."

    show ep01_game109 with vpunch
    anto "Do you really think so?"
    mc_s "Yeah."
    mc_t "Did I actually just say that out loud?"

    show ep01_game112
    anto "Does that mean you're into me?"
    mc_s "I..."
    anto "So you're not into me?"
    mc_s "I..."
    anto "Do you like me or not?"
    mc_t "Fuck, why can't I just say it!"

    show ep01_game113 with hpunch
    anto "Because I do, I really like you... a lot."
    mc_t "Oh, come on... say something, don't be a pussy!"

    show ep01_game114
    mc_s "Antonella..."
    anto "YES??!!"
    mc_s "I..."
    mc_s "I--"

    $ playAudio(sfx_keys, "sfx", 1, True, 0, 0)

    show ep01_game117 with hpunch
    anto "Huh?"
    mc_s "Anto-"
    anto "Shhh... my [mo_r_low]'s back!"
    mc_s "But you said..."
    anto "Shhh... Shut up!!"
    jump q3_date




label q3_date:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (antonella, trust, -1)
# --
#THE DATE
    if not rm.get("antonella", "trust") < 2:
        show ep01_game128 with vpunch
        anto "Hurry up! She's coming! Quick! Follow me!"
        mc_s "Uh?! What?"

    $ stopAllSubchannels(channel="sfx", fadeout=1)

    show ep01_game129 with slowfade
    mc_s "Where are we going? Antonella?"
    anto "Trust me. It'll be fun..."
    show ep01_game130
    anto "Over here..."
    mc_s "Okay..."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep01_postgame01 with slowfade
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(antonella_past_happy_theme, "music", 2, True, 8, 0)
    mc_y "Slow down! You're leaving me behind!"
    anto_y "Run faster then! Come on! This way!"
    show ep01_postgame02
    anto "Cool, isn't it? And there's no one else here."
    mc_s "Did you plan all of this?"
    anto "I don't know... Let's find out."
    show ep01_postgame03
    anto "C'mon, let's play!"
    mc_t "She so much likes doing everything she wants."

    show ep01_postgame04 with hpunch
    mc_t "Wow..."

    show ep01_postgame06 with vpunch
    anto_y "Yes! A strike! Awesome!"
    mc_t "She is smart, attractive, funny, and competitive as hell. And now she just proved she's a badass at bowling."

    show ep01_postgame05
    anto "Hey! Did you see that? I got a strike!"
    anto "On my first throw!"
    anto "Isn't it cool??"
    $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=2.5)
    $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4)
    $ playAudio(sfx_glitch, "sfx", 1, False, 2.5, 0)

    show ep01_postgame05 at animated_glitch
    mc_s "Yeah! It was impressive... "
    mc_t "Look at her... smiling like a kid at Christmas."
    mc_t "Huh? What is happening?"
    mc_t "Why is everything..."
    if not rm.get("antonella", "trust") < 2:
        $ setChannelVolume(channel="sfx", subchannel=1, volume=0, fade_duration=2.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=2.5)

        show ep01_postgame07 with vpunch
        anto "What are you thinking about, hmm? Aren't you having fun?"
        anto "Come on now. Just for today... Try to have some fun with me..."
        show ep01_postgame08
        mc_t "Uhhh..."
        mc_t "Wh--what?! She just kissed me!"

        show ep01_postgame09
        anto "HAHAHAH! OH MY GOD!! You look sooooooo cute when you're embarrassed!!"
        $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4, fade_duration=2.5)
        $ setChannelVolume(channel="music", subchannel=2, volume=0, fade_duration=2.5)
    scene eigengrau with slowfade
    show ep01_postgame10 at animated_glitch
    mc_t "Why are we suddenly having a normal conversation now?"
    anto "Anyway, since we're still here. Do you mind if we talk for a bit?"
    mc_s "Sure... What do you want to talk about?"
    mc_t "What is happening...??"
    mc_t "This doesn't feel right..."

    $ stopAllSubchannels(channel="sfx", fadeout=1)
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5, fade_duration=2.5)

    show ep01_postgame11
    anto "Guess nothing ever really goes as planned, right?"
    mc_t "Time skipped... what's wrong with me...?"
    mc_s "Sorry, what? Did you say something?"

    show ep01_postgame12
    anto "Oh, nevermind. Wanna go to a candy shop after this?"
    mc_s "Um... sure?"
    anto "Great! I love that place!"
    show ep01_postgame13 with slowfade
    anto "This shop is great! Look at this!"
    mc_s "Um... okay."
    anto "It's so good I could just lick it all over."
    show ep01_postgame14
    mc_s "Huh?"
    anto "Bet it would taste delicious if it were you instead of the lollipop, [mc_name]."
    mc_s "Uhhh... "
    anto "Hahaha! You're such a cutie when you get all shy! Sooooo adorable!"
    anto "So... Wanna go check some clothes out next? That will be fun!"
    $ show_walkthrough("ep01_postgame_menu")
    menu:
        "Yes":
            hide screen walkthrough_screen

            mc_s "Sure."
            anto "Great! Let's go! Let's go!"
            $ ep01_clothstore = True
            $ stopAllSubchannels(channel="music", fadeout=1.5)
        "No":
            hide screen walkthrough_screen

            mc_s "I don't think so... I don't like shopping."
            anto "Hmmmm, well, that's too bad for you!"
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            jump ep01_park_situation


    scene eigengrau with dissolve
    $ playAudio(sfx_mall, "amb", 1, True, 1.5, 0)

    show ep01_clothing01 with slowfade
    mc_t "The day just kept on rolling... And with every word, every chat, we got closer and closer."
    mc_t "Was I falling for this girl? Or had I already fallen head over heels, and this was just making it official?"

    show ep01_clothing02
    mc_t "Antonella's checking out skirts, and I'm just standing here like an idiot."
    mc_t "Whoa, that goth chick is smokin'. Wonder if I should go talk to her..."
    mc_t "But I should probably ask the clerk about a gift for Antonella's birthday. Show her I care, right?"

    $ show_walkthrough("ep01_clothing_menu")
    menu:
        mc_t "Fuck, what do I do? Chat up the goth girl or stay focused on Antonella?"
        "Chat with goth girl":
            hide screen walkthrough_screen

            mc_t "Screw it, I'm gonna say hi to her."

            $ rm.update("antonella", "trust", -3)
            $ check_levels("antonella", "trust", -3)
            jump ep01_proleather


        "Find perfect gift":
            hide screen walkthrough_screen

            mc_t "Nah, can't ditch Antonella like that. We've had a great day. Gotta find her the perfect present."

            jump ep01_proseller




label ep01_proleather:
#THE CLOTHING_1
    show ep01_clothing03 with slowfade
    mc_t "Hold up..."
    mc_t "What am I doing? This is crazy."
    mc_t "I shouldn't even be thinking about anyone but Antonella right now."

    show ep01_clothing04
    mc_t "But... uhm... Ain't nothing wrong with looking... right?"
    mc_t "Maybe I could find some cool stuff for Antonella around here."

    show ep01_clothing05
    mc_t "I think I... Already see something I could get for her."

    show ep01_clothing06
    mc_t "I mean..."
    mc_t "Check out those..."

    show ep01_clothing07
    mc_t "Damn."
    mc_t "Fuck it! I'm just going to talk to her."
    mc_s "Hey there..."
    "Goth girl" "Huh?"

    show ep01_clothing08 with vpunch
    "Goth girl" "Hi kid..."

    show ep01_clothing09 with hpunch
    "Goth girl" "Hey, your girl over there is a real catch. Don't be dumb!"
    "Goth girl" "So, next time watch where you're looking, 'cause not all of us chicks are this chill, got it?"
    mc_s "I..."
    mc_s "My bad."
    "Goth Girl" "No sweat, cutie."

    $ unlock_memory("m_ep01_clothes")

    show ep01_clothing10
    mc_t "Fuck!"
    mc_t "Oh well... I'll just find something else for Antonella then."

    $ ep01_gothgirl = True
    jump ep01_proseller




label ep01_proseller:
#THE CLOTHING_2
    show ep01_clothing11 with slowfade
    "Salesgirl" "Hi! How can I help you today?"
    mc_s "Uh... Hello, actually... I'm here to find a birthday present for my friend Antonella."
    "Salesgirl" "Okay, sir! Do you have any ideas in mind already? What kind of gifts does she like?"
    mc_s "Um... Actually, no idea! Maybe books?"
    "Salesgirl" "Oh sure! Sadly we don't sell any here. But I think I got something perfect for her!"
    "Salesgirl" "Follow me, please!"

    show ep01_clothing12
    "Salesgirl" "What about these? They're great for every girl!"
    "Salesgirl" "My ex-boyfriend always gave me this kind of stuff when he screwed up and wanted to make it up to me."
    mc_s "Wow, they look super nice..."

    show ep01_clothing13
    "Salesgirl" "We have earrings, necklaces, rings, bracelets, and more! Any piece you choose will surely win your friend's heart!"
    mc_s "Umm... But... Is this really the best thing to give her? It seems a bit expensive and not really worth it."
    "Salesgirl" "I disagree! Jewelry is always worth it! Besides, if she likes it, it will be a lasting gift that she can wear all the time."

    show ep01_clothing14 with hpunch
    anto "Thinking of buying something?"
    mc_s "Oh! I... Uh... Wasn't planning to, but... If you want--"
    anto "Forget about it! You don't need to get anything for me."
    anto "But if you ever do have the urge, I wouldn't say no to something small. Just saying..."
    show ep01_clothing15 at concentrate with dissolve
    anto "Like that necklace over there..."
    mc_t "So she likes jewelry huh? Never would have thought it..."

    show ep01_clothing16 with vpunch
    if ep01_gothgirl:
        anto "By the way, I saw you checking out that goth chick earlier... Should I be jealous or...?"
        mc_s "Uhm..."
        anto "It's okay... I forgive you..."
    else:
        anto "Just kidding! Don't actually buy me anything!"
        anto "Also... if you get me anything, I'll probably throw it away, so you might as well not even try."
        anto "But thank you for offering anyway. It's sweet of you."
    show ep01_clothing17
    anto "Hey, I wanted to show you something. Come with me!"
    mc_s "Huh? What do you want me to see?"
    anto "Just come with me to the dressing room!"
    show ep01_clothing18 with vpunch
    "Saleswoman" "Please stop right there! We don't allow anyone in the dressing room unless they're trying on clothes!"
    anto "Oops! Silly me. So sorry!"
    show ep01_clothing19
    anto "Just wait for me outside and I'll let you see everything you want later. Got it?"
    mc_s "Um... sure... Whatever you say, Antonella!"

    show ep01_clothing20 with slowfade
    $ playAudio(antonella_game_theme, "music", 2, True, 2.5, 0)

    mc_t "Wow! I can see her body perfectly through the mirror! Oh shit! Am I... getting hard?"

    show ep01_clothing21 with slowfade
    mc_t "Damn it... I thought she was gonna take off more clothes..."

    show ep01_clothing22 at concentrate
    anto "Look, look! This dress looks so good on me!"
    mc_s "It really does, Antonella! You look amazing!"
    if ep01_anto_clothing >=1:
        show ep01_clothing24
        anto "Thank you! You know, since I'm wearing this dress now, I won't mind you taking it off me later..."
        mc_s "Huh?"
        anto "Hahaha! Just kidding! Cmon, let's check out these other clothes before I get changed again!"
    else:
        anto "Anyway, shall we go? I don't have money to buy this."
        mc_s "Oh, sorry."
        anto "No worries!"
    show ep01_clothing23 with slowfade
    mc_t "Shit... I might as well admit it. Antonella really turns me on..."
    if ep01_anto_clothing >=2:
        anto "Don't go anywhere! I have something to show you!"
        mc_s "Okay!"
        anto "You're gonna love it!"
    if ep01_anto_clothing >= 2:
        show ep01_clothing25 at concentrate with hpunch
        anto "So? What do you think of it?"
        mc_s "Woah! It's so sexy!"
        anto "I told you you were gonna love it!"
        mc_s "Oh, sorry! I meant-- I mean--"
        anto "Your brain works overtime sometimes, [mc_name]! You always try to find an excuse not to be honest! That's your problem! You need to loosen up and admit what you actually feel."
        mc_t "Fuck! She caught me red-handed!"

        show ep01_clothing26
        anto "What about this part? How's my ass? Cute right?"
        mc_s "Antonella! Can you please stop teasing me? You're driving me crazy here!"
        anto "Hahaha! Oh no! But this is fun! I love seeing you all flustered! It's cute!"
        if ep01_anto_clothing == 3 and ep01_mc_clothing == 0:
            anto "Alright! I got one more thing to show you..."
        else:
            anto "Okay, this is the last one. I don't have any more dresses left, so I'm going to put my normal clothes back on. Don't leave yet!"
    if ep01_anto_clothing == 3 and ep01_mc_clothing == 0:
        show ep01_clothing27 with slowfade
        anto "Hey! [mc_name]! Get your ass in here! Now!"
        mc_s "But the lady doesn't allow anyone except those who are trying on clothes--"
        anto "Forget that shit! Just come over here!"
        mc_s "But... there's barely any space for two people inside there!"
        anto "For fucks sake! Just come over here before I change my mind and leave!"
        mc_s "Alright, alright... Here I come!"

        show ep01_clothing28 with vpunch
        anto "Now... can you tell me what you really think of me?"
        mc_s "Damn, Antonella... You're smokin' hot!"
        anto "Yeah?"
        mc_s "Umm... yeah... you look good."

        show ep01_clothing29
        anto "So um... only good? Or how would you rate me if I was on a scale of 1-10?"
        mc_s "100... actually."

        show ep01_clothing30
        anto "Awesome! You don't know how happy I am to hear you say that!" 
        anto "Well... you better get out of here before the clerk gets angry."
        $ show_walkthrough("ep01_antochangeclothes_menu")
        menu:
            mc_t "Should I ask her to show me her ass?"
            "Ask for a booty shot":
                hide screen walkthrough_screen

                mc_s "Okay... but uh... could you do me a favor?"
                anto "What?"
                mc_s "Could you turn around and let me see your ass again?"
                anto "What? Why do you want to see it?"
                mc_s "Well, cause it's your best feature so far. And I'm kind of curious."
                anto "[mc_name]..."
                show ep01_clothing31 with hpunch
                anto "Happy now, perv? What a dirty request."
                mc_s "Can you blame me?"
                anto "Seriously though... You better go."
            "Don't risk it":
                hide screen walkthrough_screen
                pass
        mc_s "Ok... sorry!"

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_clothing32
    anto "Alright! That was fun, wasn't it?"
    mc_s "Sure..."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_park_situation




label ep01_park_situation:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (amber, trust, +1)
# --
#THE PARK SITUATION
    $ playAudio(sfx_evenpark, "amb", 2, True, 2.5, 0)

    show ep01_thepark01 with slowfade
    anto "Thank you for coming with me today. I had fun."
    mc_s "Likewise... It was nice spending time with you..."
    anto "[mc_name] there's something I've been wanting to tell you..."
    $ setChannelVolume(channel="music", subchannel=2, volume=0.5)
    $ playAudio(antonella_love, "music", 2, True, 2.5, 0)

    show ep01_thepark03 with slowfade
    anto "Um... I know you think I am weird and all... And probably you are tired of my jokes and all... But... uhm... I-- I have feelings for you."
    anto "And you might find this stupid or disgusting... But I want us to be more than friends. I don't know why or how but... I have grown very fond of you..."
    anto "So yeah... I'm saying that I am in love with you."
    anto "And all I ask from you is... Don't hate me for what I feel... or who I am. Okay? Promise me that?"
    mc_s ". . ."
    anto "Please..."
    mc_s "Okay. I promise."

    show ep01_thepark02
    anto "Thank you, [mc_name]. I will remember that."
    mc_t "What was that all about? Antonella's acting super strange today."
    mc_t "And why did she feel the need to tell me how I shouldn't hate her for who she is?"
    mc_t "Anyway, all in all, it was still an enjoyable day with her."

    show ep01_thepark04 with hpunch
    mc_t "Huh?!"
    mc_t "A hug?!"
    if ep01_hug:
        anto "Now it's my turn to hug you! Hehe!"
        anto "I'm sorry, it's just that... for me, a hug means so much more than a kiss or any other gesture."
    else:
        anto "Sorry... for hugging you out of the blue like that."
        anto "It's just that... for me, a hug means so much more than a kiss or any other gesture."
    anto "It's like being protected and, at the same time, becoming a part of the other person."
    anto "When you hold me in your arms, I feel safe, cherished, and connected to you in a way that words can't describe."
    mc_s "I--"

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_thepark05 with slowfade
    mc_t "Oh... shit."

    $ setChannelVolume(channel="music", subchannel=4, volume=0.5)
    $ playAudio(amber_theme, "music", 4, True, 3, 0)

    mc_t "It's Amber! What's she doing here? Fuck! This can't end well..."

    show ep01_thepark06 with vpunch
    amb "Hey!! [mc_name]!!"
    amb "WTF is this??!!"
    show ep01_thepark07
    mc_s "Oh... Hi! How are you?"
    amb "Don't 'hi' me, you asshole!!! You two-timing dickhead!!"
    show ep01_thepark08
    anto "Hello! What's going on?"
    amb_y "Shut up, bitch! You slutty whore!"
    amb_y "How dare you touch my [br_full_r_low]?! Are you cheating on me, [mc_name]?!?"
    mc_s "Cheating? What do you mean? You're my [si_full_r_low], not my girlfriend!"
    amb "I am your girlfriend, stupid! Or are you playing dumb?!"
    show ep01_thepark09
    anto "Your girlfriend? But that makes no sense."
    amb_y "You better shut up right now, you tramp!"
    anto "Whoa, whoa! Hold on a minute!"
    amb_y "Stay out of this, you homewrecker!"
    anto "What kind of cheap porno cosplay outfit is this?"
    anto "Like, wow! So original!"
    anto "What character are you even supposed to be? Bride of Chucky? Wednesday Addams? Is that the look you're going for?"
    show ep01_thepark10
    amb_y "WHAT THE FUCK DID YOU SAY ABOUT MY CLOTHES, YOU FATASS BITCH?!?"
    anto "Awwwwwww... Did I hurt your widdle feewings?"
    mc_t "Fuck... This can't get any worse."
    mc_y "STOP! Both of you, stop arguing! Just calm down for a minute!"
    show ep01_thepark11
    mc_s "Alright, Antonella... This is my little [si_full_r_low]. She has a crush on me."
    amb "Shut it! It's true!"
    show ep01_thepark12
    anto "So she's jealous because her big [br_full_r_low] is all grown up and she can't have him to herself anymore. I can totally understand that."
    amb "You bit--"
    mc_s "Stop it! Antonella, please don't say stuff like that. It's not helping."

    show ep01_thepark13
    amb "Yeah! Stop saying that, bitch!"
    amb "[mc_name] and I are soulmates! We've been together since we were kids!"
    mc_s "Goddamnit!"

    show ep01_thepark14
    mc_s "Look, Amber. Listen. You and me, we're siblings. Nothing else. That's all."
    anto "What about me, then?"
    mc_t "Fuck..."
    anto "Who am I to you?"
    mc_s "You... You are--"
    amb "You better not finish that sentence, [mc_name]! If you say you're in love with this bimbo, I swear to God--"
    mc_s "Amber, listen. I'm sorry, but there's something you need to understand--"

    show ep01_thepark15
    amb_y "No!!"
    amb_y "You don't have to say anything."
    amb_y "I know what's happening here... You and Antonella are lovers. But you didn't want me to find out so you kept it a secret from me."
    show ep01_thepark16
    $ stopAllSubchannels(channel="music", fadeout=5)
    amb_y "FUCK YOU! AND FUCK YOUR LITTLE WHORE TOO!"
    amb_y "I hope you're happy together, you assholes..."
    show ep01_thepark17
    anto "What an over-the-top reaction! What's wrong with her??"
    mc_s "Can you not add salt to the wound, Antonella?"
    mc_t "Damn it, this situation is a complete mess."
    mc_t "Should I go after Amber and try to explain things to her, or should I stay here with Antonella and make sure she's alright?"

    $ show_walkthrough("ep01_thepark_menu1")
    menu:
        mc_t "I need to make a decision, and fast."
        "Go after Amber":
            hide screen walkthrough_screen

            mc_t "I can't let Amber leave like this. She's my [si_full_r_low], and I need to make things right with her."
            mc_t "Antonella will understand; I'll apologize to her later and explain everything."
            mc_s "I'm sorry, Antonella. We can talk about this later."

            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            $ ep01_park += 2
            jump ep01_chaseamb


        "Comfort Antonella":
            hide screen walkthrough_screen

            mc_t "Antonella is my priority right now. She just confessed her feelings to me, and I can't leave her alone after what just happened."
            mc_t "Amber will have to wait; I'll deal with her later when she's calmed down a bit."
            mc_s "Don't worry about her... Let's just move on."

            $ ep01_park += 1
            jump ep01_stayanto




label ep01_chaseamb:
##RM.POINTS.TRACK (amber, trust, +1, -1)
##RM.POINTS.TRACK (antonella, trust, -5)
# --
#PICKING AMBER
    show ep01_thepark18 with hpunch
    mc_y "Amber! Wait!"
    show ep01_thepark19 with slowfade
    $ playAudio(amber_sad_theme, "music", 2, True, 2.5, 0)
    amb "Go away, [mc_name]. I don't want to talk to you."
    mc_s "Look, I'm sorry you had to find out this way. But you need to know--"
    amb "What? That you fell in love with some bimbo?"
    mc_s "Well... yeah... I mean--"

    show ep01_thepark20 with vpunch
    amb "Then just tell me one thing: did you ever care about me? Or was I always just a burden to you?"
    mc_s "Why are you making an issue out of this? We've always been siblings and that's never gonna change."
    amb "You think that means nothing to me?"
    amb "All those years we spent together meant something, [mc_name]!"
    amb "And now you throw all that away for a girl you barely know?!"
    mc_s "Do you realize we're siblings? So what years are you talking about?!? We don't have a choice in the matter!"

    show ep01_thepark21
    amb "No... You're right. We don't have a choice in anything at all. Not even love..."
    mc_s "Oh my God! Really?! Love?!? You're not serious, are you?"
    amb "Be honest, [mc_name]. Is she your girlfriend or not?"
    mc_t "Shit, she's putting me on the spot here. What am I supposed to say?"
    mc_t "I don't want to hurt her, but I can't just lie about my feelings for Antonella either."

    $ show_walkthrough("ep01_thepark_menu2")
    menu:
        "Lie to Amber":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)
            $ ep01_lieamber = True
            $ stopAllSubchannels(channel="music", fadeout=2.5)

            mc_t "I hate lying to Amber, but what choice do I have?"
            mc_s "I promise, we're just friends."
            amb "Are you sure?"
            mc_s "Of course."

            show ep01_thepark22
            amb "Then why didn't you tell me about her?"
            mc_s "Because it wasn't any of your business, okay? She's a friend and nothing more."

            show ep01_thepark24 with vpunch
            amb "Alright then... If that's how it is, I believe you. Thank you for telling me the truth."
            mc_s "It's alright, [sis_r_low]. We're good now."

            show ep01_thepark25
            amb "I just wanted us to be together forever, like always."
            mc_s "Hey, I'm still here."
            amb "You're the only one in the [fm_r_low] who actually cares about me, you know? Everyone else just treats me like a joke."
            mc_s "It's okay... I will always be here for you. Just remember that."
            amb "Well..."
            mc_s "However you need to apologize to Antonella too."

            show ep01_thepark26
            amb "She's really important to you, isn't she?"
            mc_s "Yeah."
            amb "Okay. I'll do my best not to say anything rude this time."
            show ep01_thepark27 with slowfade
            amb "Hey there! Sorry for making such a scene earlier. I was being a bit immature, so... yeah..."
            mc_t "Wow! Didn't expect her to change so quickly. Please don't screw things up, Amber..."
            anto "No worries! As long as everyone's happy in the end, right?"
            amb "Right! And by the way, [mc_name] said that he considers you a close friend, so I hope we can get along from now on!"
            anto "Uhm... Okay? Sure."
            amb "Alright, I'm gonna get going. Take care, okay?"
            mc_s "I'll see you at home. I'm gonna stay with Antonella a bit longer."
            amb "Love you!"
            mc_s "Love you too, Amber."

            show ep01_thepark28 with slowfade
            anto "Um... Why did you lie to your [si_full_r_low]? That's not good, you know."
            mc_s "Yeah, I know. But how was I supposed to explain our relationship to her?"
            mc_s "You've seen how she can be. She won't understand."

            show ep01_thepark30
            anto "Yeah, yeah... Well, at least you got her to calm down in the end."
            mc_s "I'll make it up to you later, okay? Promise."
            anto "Hmmmm..."
            $ show_walkthrough("ep01_thepark_menu3")
            menu:
                mc_t "Is she angry?"
                "Make excuses":
                    hide screen walkthrough_screen
                    $ ep01_losttrust = True

                    mc_s "Antonella, I know lying was wrong, but I panicked. Can you blame me? I couldn't stand the thought of losing my [si_full_r_low] over something so trivial."
                "Be honest and apologize":
                    hide screen walkthrough_screen

                    mc_s "Antonella, I lied to protect you from Amber's anger. Don't get upset. I didn't mean to hurt you."

            show ep01_thepark29
            if ep01_losttrust:
                $ rm.update("antonella", "trust", -5)
                $ check_levels("antonella", "trust", -5)
                anto "That's not trivial! Your feelings for me matter just as much as your feelings for Amber, right?"
                mc_s "What do you want me to do, Antonella? Tell her I love you and ignore her reaction? That's not a good idea."
                anto "Alright, alright! Anyway, I better go now. Bye-bye!"
                mc_s "Are you mad? I'm sorry--!"
                mc_s ". . ."
            else:
                anto "Nah... I understand, [mc_name]. It's alright. And thank you for sticking up for me."
                anto "Anyway, I better go now."
                mc_s "Are you mad? I'm sorry--!"
                anto "No, no... It's just... I have to deal with something. Later!"
                mc_s "Okay... Bye."

            jump ep01_postpark


        "Tell Amber the truth":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -1)
            $ check_levels("amber", "trust", -1)
            $ stopAudio(channel="music", subchannel=2, fadeout=2.5)

            mc_t "Fuck it, I can't lie to Amber. She deserves the truth, even if it hurts like hell."

            $ playAudio(amber_anger_theme, "music", 4, True, 2.5, 0)

            mc_s "Okay... No point in hiding it anymore... The truth is, Antonella and I have feelings for each other."

            show ep01_thepark23 with vpunch
            amb_y "WHAT?!?"
            amb "Like fuck! That bitch doesn't deserve you!"
            mc_t "Shit... Amber isn't going to accept this at all."
            mc_s "Look, Amber. Can you just stop being stubborn for one fucking minute?"
            mc_s "Who Antonella is or what she means to me is none of your concern. She's my girlfriend, okay?"

            show ep01_thepark32 with hpunch
            amb_y "FUCK THAT BITCH! FUCK YOU TOO! YOU ASSHOLE!!!!"
            amb "Why did it have to be her? Why couldn't you just love me instead?!?"
            mc_s "Amber, listen... you know this can't happen between us, right? It's not normal."

            show ep01_thepark33 with hpunch
            amb "I-- I know..."
            amb "But I can't help it... You're the only one in the [fm_r_low] who actually cares about me..."
            amb "And now you've taken that away from me too..."
            mc_s "Listen, Amber..."

            show ep01_thepark34
            amb "Just... Shut up. I'll just leave you two alone..."
            $ stopAllSubchannels(channel="music", fadeout=1.5)

            show ep01_thepark28 with slowfade
            anto "So... How did it go?"
            mc_s "Not well..."
            anto "She will come around eventually."
            show ep01_thepark36
            anto "Thank you for not rejecting me back there... That was hard enough as it was."
            mc_s "Of course not... You know I care about you, Antonella."
            mc_s "Sorry you had to see that..."

            show ep01_thepark38
            anto "Oh don't apologize, silly. I'm just happy I got to spend the day with you. It's just a shame about your [si_full_r_low]."
            anto "Maybe we can work something out with her in the future. Right?"
            mc_s "Yeah... Well, I better go home. We'll talk later, okay?"

            show ep01_thepark31
            anto "See ya, [mc_name]."
            mc_s "Love you!"
            anto "Oh."
            jump ep01_postpark




label ep01_stayanto:
#PICKING ANTO
    $ playAudio(antonella_past_theme, "music", 2, True, 2.5, 0)

    show ep01_thepark35 with slowfade
    anto "Sorry for causing all of this drama, [mc_name]. Maybe... maybe it was a mistake telling you how I feel."
    anto "I never meant for your [si_full_r_low] to get hurt like that. In my head, it was going to be a lot more romantic."
    mc_s "It's okay. There was nothing romantic about this whole thing anyway."
    mc_s "Listen, Antonella. You didn't do anything wrong here."
    mc_s "She was bound to find out about us eventually. So let's not waste time worrying about it, okay?"

    show ep01_thepark36
    anto "Find out about us? Does that mean... You..."
    mc_s "Ahh-- umm... Uh... It means--"

    show ep01_thepark37
    anto "Forget it! It's okay, [mc_name]. You don't have to say anything."
    mc_s "No, no... Wait. Listen... I--"
    anto "Really! You don't have to say it!"
    mc_s "I love you, Antonella! And I want to be with you!"

    show ep01_thepark38
    anto "Ohhh, [mc_name]..."
    mc_s "We'll work something out with my [si_full_r_low]. Don't worry."
    anto "Wow! This is crazy! I didn't think you would actually..."
    mc_s "Uhm... but I think I should check on Amber first before we plan anything else."
    anto "Yeah, sure! Go ahead!"
    show ep01_thepark31
    mc_s "So... I guess I'll talk to you later? Can I call you later tonight?"
    anto "Sure! Talk to you later then."
    mc_s "Okay. Bye!"

    $ stopAllSubchannels(channel="music", fadeout=1.5)
    jump ep01_postpark




label ep01_postpark:
#THE TAXI INCIDENT
    scene eigengrau with dissolve
    show ep01_thepark39 with slowfade
    $ playAudio(sfx_footsteps_male_semirun, "sfx", 1, True, 1, 0)
    if ep01_park == 1: #MC picked Antonella
        mc_t "Well, that was a total disaster! Amber's probably never gonna speak to me again, and I bet she hates Antonella's guts now too."
        mc_t "Wait, she's still here?! I thought she'd be home by now! Maybe I can catch her before she goes inside and try to explain things better."
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            if ep01_losttrust: #MC made excuses to Antonella
                mc_t "Damn, how the hell did Antonella misunderstand what I said so badly? And why didn't I just keep my mouth shut instead of making stupid excuses?"
                mc_t "Oh, there she is... Should I talk to her?"
            else: #MC was honest to Antonella
                mc_t "Ah, fuck me! Why's everything gotta be so complicated? I finally find a girl who's into me, and of course my [si_full_r_low] has to fuck it all up!"
                mc_t "Shit, there's Amber... maybe I should talk to her again."
        else: #MC told the truth to Amber
            mc_t "I mean, what was I supposed to say to Amber? That I don't have feelings for Antonella? That'd be a straight-up lie! It's not like I picked Antonella over Amber on purpose or anything..."
            mc_t "Oh... That's Amber. Maybe I can explain myself better this time around?"

    show ep01_thepark40
    mc_s "Amber! Hey! Wait!"

    $ stopAudio(channel="sfx", subchannel=1, fadeout=0)
    $ playAudio(sfx_taxihorn, "sfx", 2, False, 0, 0)

    show ep01_thepark41 with vpunch
    mc_t "Oh, fuck!"

    show ep01_thepark42 with hpunch
    amb "[mc_name]! Watch out!"
    $ playAudio(sfx_carhit, "sfx", 3, False, 0, 0)

    show ep01_thepark43 with vpunch
    mc_s "Ow!"

    show ep01_thepark44
    mc_s "My bad, didn't see that coming!"
    amb_y "Oh my God! [mc_name]... You okay?"
    show ep01_thepark45 with slowfade
    mc_s "Yeah, I'm good."
    amb "You sure? You're not hurt or anything?"
    mc_s "Nah, I'm fine."

    $ playAudio(sfx_punch, "sfx", 4, False, 0, 0)

    show ep01_thepark46 with vpunch
    amb_y "You could've been killed, you dumbass!"
    mc_s "Ow, hey!"

    show ep01_thepark47
    amb "Pull that shit again, and I'll fucking end you myself!"
    mc_s "So you care about me after all huh?"
    amb "Shut the fuck up!"
    mc_s "Alright, alright. Let's head home, yeah?"
    amb "Don't tell me what to do!"
    show ep01_thepark48
    mc_s "C'mon, princess! Time to go!"
    amb "Put me the fuck down, right now!"
    mc_s "No way! We're going home!"
    amb "Ugh! You're such a dick!"
    mc_s "Nah, you know you love me!"
#HOME SWEET HOME
    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    scene eigengrau with dissolve
    show ep01_home01 with slowfade
    $ playAudio(sfx_midnightpast, "amb", 1, True, 2.5, 0)

    mc_s "Aw! Don't be mad, Amber!"
    amb "I'm not even wearing panties, you asshole! You must have seen my pussy!"
    mc_s "What are you talking about? I didn't see anything."
    amb "Don't play dumb with me, you perv!"
    $ playAudio(amber_theme, "music", 2, True, 2.5, 0)

    show ep01_home02 with slowfade
    amb "Uhm..."
    amb "[mc_name], I gotta ask you something."
    mc_s "What is it?"
    amb "About what went down... with Antonella..."
    mc_s "What about her?"

    show ep01_home03
    if ep01_park == 1: #MC picked Antonella
        amb "Antonella means more to you than I do?"
        mc_s "What are you talking about?"
        amb "I'm talking about how you ditched me to go after that bitch!"
        $ show_walkthrough("ep01_home_menu")
        menu:
            "Reassure Amber":
                hide screen walkthrough_screen
                $ rm.update("amber", "trust", 1)
                $ check_levels("amber", "trust", 1)

                mc_s "You know you're my [sis_r_low] and I'll always love you. But Antonella... she's special to me in a different way."
                amb "So what, I'm not special?"
                mc_s "Look, it's complicated. I'm not good with words."
            "Stand your ground":
                hide screen walkthrough_screen
                $ rm.update("amber", "trust", -1)
                $check_levels("amber", "trust", -1)

                mc_s "Look, Amber, I'm not a kid anymore, okay?  I have a right to my own life, just like you have yours."
                amb "That's not the fucking point!"
                mc_s "Then what is the point?"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "So, Antonella's just a friend? Swear there's nothing else going on between you two?"
            mc_s "Nothing at all."
            amb "You sure about that?"
            $ show_walkthrough("ep01_home_menu")
            menu:
                "Reassure Amber":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", 1)
                    $ check_levels("amber", "trust", 1)

                    mc_s "Yeah, Amber, I promise. You're my [si_full_r_low], and I'd never lie to you. Trust me, she's not really my type. I prefer my girls a little more... wild."
                    amb "Alright, I guess I believe you."
                    mc_s "If it makes you feel any better, I think you're way hotter than her anyway."
                "Be evasive":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", -1)
                    $ check_levels("amber", "trust", -1)

                    mc_s "I already told you we're just friends. Why do you keep bugging me about it? Don't you trust me?"
                    amb "So you're saying you don't have a thing for her?"
                    mc_s "No way! That's ridiculous. Why would I be into her anyway? You know me better than that!"
        else: #MC told the truth to Amber
            amb "I can't fucking believe you're dating that bitch, [mc_name]. What the hell's wrong with you?"
            mc_s "What? What's the big deal? She's actually really cool once you get to know her."
            amb "Why the fuck would you date someone like her?!"
            $ show_walkthrough("ep01_home_menu")
            menu:
                "Explain calmly":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", 1)
                    $ check_levels("amber", "trust", 1)

                    mc_s "I know it's hard to get, but Antonella makes me happy. That's all that matters."
                    amb "Why? She's such a fucking slut! How can you be happy with a bitch like that?"
                    mc_s "Amber, listen. I love you, okay? You're my little [sis_r_low]. There's nothing I wouldn't do for you, but you need to understand this."
                "Be defensive":
                    hide screen walkthrough_screen
                    $ rm.update("amber", "trust", -1)
                    $ check_levels("amber", "trust", -1)

                    mc_s "It's none of your damn business who I date, Amber. So just stay out of it."
                    amb "You should stay the fuck away from her. She's nothing but trouble, I'm telling you."
                    mc_s "Amber, please don't start this shit again."

    show ep01_home04 with vpunch
    if ep01_park == 1: #MC picked Antonella
        amb "That girlfriend of yours doesn't have tits like these or a bangin' body like mine, does she?"
        mc_s "Jesus, Amber! What's gotten into you?"
        amb "What? You know it's true!"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "Good to know that! Besides, how could she compare with me, your perfect [si_full_r_low], huh? Look at me! There's no way that bitch is hotter than this!"
            mc_s "Yeah... um... it doesn't really matter, Amber..."
            amb "Well... it kinda does matter, [mc_name]. A girl's gotta feel safe to do something really fucking important, you know?"
        else:
            amb "So I'm not fucking good enough for you? Is that it?"
            mc_s "Huh? What are you talking about?"
            amb "Just look at me. My tits are way bigger than hers, and my ass is fucking perfection!"
            mc_s "Uh...I-I..."

    show ep01_home05 with hpunch
    if ep01_park == 1: #MC picked Antonella
        amb "C'mon, be honest! You think I'm way hotter than Antonella, right? Just admit it!"
        mc_s "Amber, cut it out! What are you trying to do?"
        amb "What's the matter, big [bro_r_low]? Is your little [sis_r_low] getting under your skin?"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            mc_s "What the hell are you talking about?"
            amb "Don't you get it? Do I need to spell it out for you?"
            mc_s "I seriously don't understand!"
            amb "I mean, I'm not wearing any panties, dumbass! We could get into some real fun..."
            mc_s "What the fuck?!"
        else:
            amb "Besides, she doesn't know you like I do... And I'm damn sure we could have way more fun together than you and that bitch ever could..."
            mc_s "W-what are you doing Amber?"
            amb "Haven't you ever wondered what kind of shit you could get up to with your little [si_full_r_low], who just so happens to not be wearing any panties right now?"
            amb "Remember when you carried me earlier? When my legs were spread wide open..."
            mc_s "Stop! I can't deal with this!"

    show ep01_home06
    if ep01_park == 1: #MC picked Antonella
        amb "You may be older, but when it comes to this stuff, you're like a scared little boy!"
        mc_s "Wh-What do you mean by that?"
        amb "I bet she's the one calling the shots. She's probably got you wrapped around her finger, huh?"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "God, sometimes I swear I'm the older one here! You're so damn clueless..."
            mc_s "Hey! Don't treat me like a fucking idiot! It's not my fault you're acting like a freak."
            amb "I bet if you were with Antonella, you wouldn't do shit either... She'd have to make all the moves."
        else:
            amb "For fuck's sake... sometimes I wonder if you're really a man at all. Can't even handle a little teasing from your own [si_full_r_low]."
            mc_s "Hey! What the hell is wrong with you, Amber?!"
            amb "Nothing's wrong with me. Just spitting straight facts..."
    show ep01_home07
    if ep01_park == 1: #MC picked Antonella
        mc_s ". . ."
        amb "Relax, big [br_full_r_low]!  I know how shy you are around girls! Even if your own [si_full_r_low] was throwing herself at you, you wouldn't have a clue what to do!"
        mc_s "I can't believe such a young girl can have such a dirty mind!"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            mc_s ". . ."
            amb "Chill out, [mc_name]! It was just a joke! No need to get your panties in a twist. Oh wait, I'm the one not wearing any!"
            mc_s "Seriously, what the fuck is wrong with you? I can't believe how dirty your mind is!"
        else:
            mc_s ". . ."   
            amb "Relax! It was just a joke, big [bro_r_low]. Not that I didn't mean every single word of it, though..."
            mc_s "Sometimes I don't even know why I bother talking to you anymore..."

    show ep01_home08
    if ep01_park == 1: #MC picked Antonella
        amb "Ha! What can I say? I'm a bad girl! And I'm not a little girl anymore, as you can clearly see!"
        mc_s "Yeah, I suppose you're right about that."
        amb "Hold up! So you have been checking me out then?"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "What can I say? That's just how I roll! I like being a naughty little girl... Besides, it's not my fault I'm not wearing panties and I've got this bangin' body. Don't you think?"
            mc_s "I'm not touching the panties thing, but yeah, I guess you've got a nice body for your age."
            amb "So you have been checking me out? Be fucking honest!"
        else:
            amb "Yeah, well... What can I say? You're stuck with this sweet little [si_full_r_low] of yours... With her big, perky tits..."
            mc_s "Fucking hell..."
            amb "You should see me without this top on. Maybe then you'd realize just how amazing they really are..."
    show ep01_home09
    if ep01_park == 1: #MC picked Antonella
        mc_s "Well, sure. I mean, you do have a... developed figure for your age."
        amb "Why, thank you, big [br_full_r_low]! Looks like you do have an eye for beautiful women!"
        mc_s "Don't tease me! Just because I said you look good doesn't mean I see you that way!"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            mc_s "Yes! Fine, I admit it, okay? You're hot as hell! Happy now?"
            amb "I fucking knew it! See? You want me so bad! I'm totally your type!"
            mc_s "No! It doesn't mean shit! Just drop it already!"
            amb "Then why are you blushing?"
            mc_s "Shut up!"
        else:
            amb "Ooh! I think someone's interested..."   
            mc_s "N-No, that's not it at all..."
            amb "Alright, whatever you say! If you wanna see them so bad, I'll show you! Here goes!"
            mc_s "Huh? What're you-"

    show ep01_home10 with slowfade
    if ep01_park == 1: #MC picked Antonella
        amb "Either way, it makes me happy that my big [bro_r_low] thinks I'm hot!"
        mc_s "That's not what I meant and you know it!"
        amb "Yeah, yeah. Anyway, I'm gonna go to my room. Later, [bro_r]!"
        mc_s "Hold on! So... About Antonella? We're good now, right?"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "One thing's for sure. My [br_full_r_low] can't get enough of this body and he's thirsty as hell for me."
            amb "I always knew this is how it would go down between us... I was just waiting for you to pull your head out of your ass and realize it yourself."
            mc_s "No! I mean... well, that's not what I fucking meant..."
            amb "Sorry, [bro_r]. You're cute when you try to lie, but you're shit at it. Anyway, I'm gonna go take a bath. Try not to jerk off thinking about me too much!"
            mc_s "Wait! About what happened at the park... We're cool, right? Nothing's gonna change?"
        else:
            amb "Gotcha!"   
            mc_s "Very funny... Jeez..."
            amb "I love that even though you say you're with her, I can still get you all flustered and shit. At least some things never change..."
            mc_s "...It's not like that, Amber. She really is important to me, okay?"
            amb "Yeah... whatever you say. Anyway, I'm heading to my room."
            mc_s "Amber, wait... About what happened today..."

    show ep01_home11
    if ep01_park == 1: #MC picked Antonella
        amb "Yeah, we're cool. But be real with me - you'd pick me over her any day, wouldn't you?"
        mc_s "I... Uh..."
        amb "Pussy!"
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "Nothing will ever change between us, big [bro_r_low]!"
            mc_s "Good!"
            amb "You'll always be my favorite big [br_full_r_low] in the whole fucking world, and I'll always be your favorite little [si_full_r_low] who wants to jump your bones! Deal?"
            amb "Say it with me: I love my naughty little [si_full_r_low] and I always fucking will!"
            mc_s "I... Uh..."
            amb "Pussy!"
        else:
            amb "Yeah, don't worry about it. I know now that you're a total pussy, so nothing needs to be said."
            mc_s "That's not it! I meant about Antonella. Are you gonna try and fuck things up for us?"
            amb "Meh... I guess I'll leave you two lovebirds be for now. Not like I need to worry anyway."
            amb "After all, I know I've got you wrapped around my little finger. Just look at you, practically drooling all over me like a dog."
            mc_s "W-What?! I'm not-"
            amb "Alright! Bye, bye... Pussy!"
    show ep01_home12
    $ stopAllSubchannels(channel="music", fadeout=4)
    if ep01_park == 1: #MC picked Antonella
        amb "*kisses*"
        mc_s "Hey! What did you call me? Amber!"
        mc_s ". . ."
    elif ep01_park == 2: #MC picked Amber
        if ep01_lieamber: #MC lied to Amber
            amb "*kisses*"
            mc_s "Hey! Don't say that!"
            mc_s ". . ."
        else:
            amb "*kisses*"
            mc_s "Hey! That's not fair! Wait a minute, Amber!"
            mc_s ". . ."

    $ unlock_memory("m_ep01_home")
#ALONE AT LIVINGROOM
    scene eigengrau with dissolve
    show ep01_home13 with slowfade
    mc_t "Quite an interesting title..."
    mc_t "Why would she give me something like this...?"

    show ep01_home14
    mc_t "\"The Darkest Hour\"... And she says she didn't like the ending..."
    mc_t "Maybe I should check the first page--"
    amb_y "[bro_r]! Get your ass over here! I need to talk to you about some shit! It's important!"
    eli_y "[so_r], come here! I need your opinion on something! Hurry up!"
    mc_t "Talk about bad timing..."
    mc_y "Ugh... I'll be right there!"
    $ show_walkthrough("ep01_home_menu2")
    menu:
        mc_t "Where should I start?"
        "Answer Mom's call":
            hide screen walkthrough_screen
            $ ep01_elicall = True
            jump ep01_bath


        "Answer Amber's call":
            hide screen walkthrough_screen
            $ ep01_ambcall = True
            jump ep01_home




label ep01_bath:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (elizabeth, trust & cor, +1)
##RM.POINTS.TRACK (elizabeth, cor/trust, +1)
# --
#MOM'S CONUNDRUM
    show ep01_elidress01 with dissolve
    mc_s "[mo_r]?"
    mc_s "Everything alright?"
    mc_s ". . ."
    mc_y "I'm coming in!"
    $ playAudio(sfx_dooropen, "sfx", 1, False, 0, 0)

    show ep01_elidress04 with slowfade
    $ playAudio(elizabeth_theme, "music", 2, True, 2.5, 0)

    mc_t "! ! !"
    mc_t "Damn, I'll never get tired of seeing this..."
    mc_t "If [da_r] ever finds out about this, I'm so fucked..."

    show ep01_elidress03
    mc_t "Holy shit, [mo_r]..."
    eli "What do you think, sweetie?"
    show ep01_elidress02
    mc_s "Huh?!"
    eli "Do you like it? Your [da_r] got it for me for our anniversary next week."
    mc_s "Sorry! I didn't mean to-"
    eli "Don't worry about it, honey. I don't mind showing off a bit!"
    mc_t "Here we go..."

    show ep01_elidress05
    eli "So tell me, sweetie. What do you think? Do you like it?"
    mc_s "Uh..."
    eli "Yeah, I figured you wouldn't approve... It doesn't look good at all, does it?"
    mc_s "Well, it looks..."
    mc_t "Breathe, [mc_name]... Just breathe..."
    mc_t "Let's hope this time I say what she wants to hear..."
    mc_s "It looks really pretty, [mo_r]!"

    show ep01_elidress06
    eli "That's so sweet of you to say, darling. Thank you!"
    mc_s "So... uhm.. is this why you called me in here?"
    eli "Hm? Oh no, sweetie! I wanted to talk to you about something else. I had already bought some dresses before you got home."
    eli "I've got this audition scheduled with a new modeling agency, and they asked me to wear a dress for the interview, but I'm not sure if it looks good or not..."
    mc_t "I can't think straight with her standing there practically naked..."
    mc_t "Why does she always have to be so careless about her nudity? This woman, I swear..."

    show ep01_elidress07 with vpunch
    eli "Hey! Sweetie, are you listening to me?"
    eli "Are you staring at something in particular?"
    mc_s "Mom! I-I'm sorry!"

    show ep01_elidress08
    eli "Ah! There's no need for that, darling! I'm a model, right?"
    eli "It's not weird that people check me out, and I certainly don't mind showing myself off a little bit! After all, beauty is meant to be admired, isn't it?"
    mc_s "Eh...yes! Right..."
    eli "And it's okay, sweetie... You can stare... If you want to..."
    mc_s "W-What?!"

    show ep01_elidress09
    eli "You're my [so_r_low], darling. I don't mind you staring at me. Plus, as long as you're respectful and don't touch without permission, it's all good."
    mc_t "Without permission?! What the actual fuck?!"
    eli "Besides, it's not like you've never seen or touched my breasts before, right? When you were a baby, you used to suck on my titties every day!"
    mc_s "What?"
    eli "Yeah, you would always get upset when I had to put them away! You loved them so much, sweetie."
    mc_s "Seriously?!"

    show ep01_elidress10
    eli "It was so cute how attached you were to them! You didn't want anything else except [mommy_r]'s breasts!"
    eli "Sometimes when I fed you, you'd play with my nipples while you were breastfeeding!"
    mc_t "Okay [mo_r]...that's enough...Please stop talking about this..."
    eli "Remember, sweetie? Oh... well, you were only a baby, so of course you wouldn't remember all of that!"
    eli "Unless... you do remember those things?"
    $ show_walkthrough("ep01_elidress_menu")
    menu:
        "Play along":
            hide screen walkthrough_screen
            $ ep01_elimemories = True
            $ rm.update("elizabeth", "cor", 2)
            $ check_levels("elizabeth", "cor", 2)

            mc_s "Ha! No...nope...totally forgot everything..."

            show ep01_elidress12 with vpunch
            eli "Oh come on, sweetie! I'm sure if you think hard enough, some memories might come back to you!"
            eli "Maybe you remember when we used to take baths together in the tub?"
            eli "We were both naked then too, weren't we? But now that I think about it..."
            eli "Can't you remember anything, honey? The hot water... our bodies pressed against each other... the steam rising up into the air... how close we got as we touched each other..."
            eli "Just the two of us alone, lying together under the bubbles... skin on skin..."
            mc_s "Urgh... Hm..."
            eli "What's the matter, sweetie? Are you okay?"
        "Stop her":
            hide screen walkthrough_screen
            $ rm.update("elizabeth", "trust", 1)
            $ check_levels("elizabeth", "trust", 1)

            mc_y "[mo_r]! Enough is enough!"
            show ep01_elidress11 with hpunch
            eli "Excuse me? What's wrong with you, young man?!"
            mc_s "Just please stop talking about it, [mo_r]!"
            eli "There's no need to yell, mister!"
            eli "Geez! Why are you getting so defensive about this? What's there to be embarrassed about?"
            mc_s "Me? Embarrassed? Nothing! It's--It's just...ugh!"
            eli "Ugh?! Ugh?! Seriously, sweetie? Now you're saying ugh?"
            mc_s "No! What I mean is... Well..."
            eli "Well what? Spit it out, darling!"
            mc_s "I'm not trying to be rude [mo_r], but why would you talk about your breasts and stuff like that?!"
            mc_s "Aren't mothers supposed to keep these sorta things private?!"
            eli "And aren't sons supposed to respect their parents?! Why don't you, mister?!"
    show ep01_elidress13 with vpunch
    if ep01_elimemories:
        eli "Oh... I see..."
        mc_t "Well shit... She noticed my boner."
        eli "You know I didn't mean to make you hard, right sweetie?"
        eli "And I didn't want you to look at me like that either. I was just remembering old times between us... Not thinking about anything else..."
        eli "Though... you did used to stare at [mommy_r]'s titties quite a lot..."
        mc_t "Well... she kinda led me down this road."
        mc_s "I didn't want this! It's not my fault!"
    else:
        eli "Oh..."
        mc_t "Fuck! She noticed my hardon..."
        eli "Is this... a normal reaction, sweetie?"
        mc_t "Rrfkjsdhdsjkfjskdjhdjsk! I'm so dead..."
        mc_s "Yes...?"
        eli "That's not normal, darling."
        mc_s "Okay...?!"

    show ep01_elidress14 with vpunch
    if ep01_elimemories:
        eli "Hey, relax sweetie! There's nothing wrong with getting an erection, it happens all the time! Especially when you're young."
        eli "Hell, even [mommy_r] gets horny sometimes!"
        mc_s "[mo_r]!"
        eli "All I'm saying is that you shouldn't do anything perverted with [mommy_r]."
        eli "At least, not without asking permission first, alright sweetie?"
        mc_s "[mo_r]! What the fuck!"
        eli "Oh come on, darling! I'm not serious!"
        eli "Now turn around, I gotta take this thong off and put on the dress. Unless you wanna watch [mommy_r] while she changes...?"
        show ep01_elidress16 with hpunch
        mc_s "Uh... I think I'm fine... just fine here... thanks..."
        eli "Very well then, suit yourself, sweetie! This won't take long."
        mc_t "Anyone else in my place would be fucking their own [mo_r_low] already. Why aren't I doing the same?"  
        mc_t "I mean, I would if she wasn't my own [mo_r_low] and this was a porno or something... but come on!"
        mc_t "But a little peek won't hurt anyone, right?"

        show ep01_elidress15
        mc_t "OMFG that ass"

        hide ep01_elidress16
        eli "Darn... Where did I put that thing...? Oh!" 
        mc_t "Fuck [mo_r], if only you knew what I'm thinking..."
        eli "Hey! What are you doing, sweetie?! Don't look! Turn back around!"
        show ep01_elidress16
        mc_s "S-Sorry! I... uh..."
        eli "Just a little bit longer, okay darling?"
        mc_t ". . ."
        eli "I'm ready now, sweetie... You can look."
    else:
        eli "Well mister, what kind of [so_r_low] are you?! Standing there having naughty thoughts about your own [mo_full_r_low] while she's talking to you?"
        mc_t "Once again I must ask... What the actual fuck, [mo_r]?!"
        mc_t "After that little show, you expect me NOT to pop a boner?"
        eli "II know you're growing up, sweetie, and these things are natural. But this is going a bit too far, darling."
        mc_s "Uhm..."
        eli "Well, enough of this, honey. Are you gonna help [mommy_r] choose a dress or not? We can finish this conversation later!"
        mc_s "Huh? Yes! Yeah, of course! Show me the dress, [mo_r]!"
        eli "Turn around please, sweetie."
        mc_s "Huh?! [mo_r], I-- Ok."

        $ show_walkthrough("ep01_elidress_menu2")
        menu:
            eli "What? Aren't you afraid that your naughty bits will get even more excited? Hurry up and turn around, darling!"
            "Check her":
                hide screen walkthrough_screen
                $ rm.update("elizabeth", "cor", 1)
                $ check_levels("elizabeth", "cor", 1)

                show ep01_elidress15
                mc_t "Well, I'm already going to hell, so what do I have to lose?"
                mc_t "This ass though... So much for me trying to keep calm."
                eli "Are you staring at [mommy_r]'s butt, sweetie? Didn't I tell you to turn around?"
                eli "You've already gotten hard once, darling! Now behave!" 
                mc_s "N-No [mo_r]!"
                mc_t "Fuck! How did she notice?!"

                show ep01_elidress16
                mc_t "Ok dumbass, breathe! Don't be nervous and think about something else..."
                eli "I can't believe my own [so_r_low] would look at his [mo_full_r_low] like that. Have you no shame, young man?"
                mc_s "Sorry, [mo_r]! I couldn't help it... I swear."
                eli "Alright, alright, sweetie... Let's just forget about it and move on... For now anyway."
                eli "Okay, I'm ready, darling... You can turn back now."
            "Turn around":
                hide screen walkthrough_screen
                $ rm.update("elizabeth", "trust", 1)
                $ check_levels("elizabeth", "trust", 1)

                show ep01_elidress16
                mc_t "This is going to scar me for life..."
                mc_t "I mean... if she wasn't my [mo_r_low], I'd be more than happy to check out her body... but this is... I can't deal with it!"
                mc_t "My [si_full_r_low], my [mo_r_low]... Why the fuck do I have such crazy women in my [fm_r_low]?"
                eli "Alright, sweetie. Here's the first one..."
    $ stopAudio(channel="music", subchannel=2, fadeout=1.5)

    show ep01_elidress17 with slowfade
    $ playAudio(elizabeth_sexy_theme, "music", 4, True, 2.5, 0)

    mc_t "Wow."
    eli "So... What do you think, sweetie? How does [mommy_r] look?"
    mc_t "Absolute perfection"
    eli "Does it look good on me? Do you think they'll like this outfit?"
    mc_s "[mo_r]..."
    eli "Yes, honey...?"
    eli "Do you think it looks alright?"
    mc_s "It's stunning, [mo_r]..."

    show ep01_elidress18
    eli "Do you think this part here is too much, sweetie?"
    mc_t "So big.. and heavy..."
    mc_s "No...no not at all"
    mc_s "Actually...it makes you shine even more..."
    eli "It does...? Aww, aren't you just the sweetest!"
    show ep01_elidress19
    eli "What about my legs, honey? Do they look good in this?"
    mc_s "I mean, you always have amazing legs, [mo_r]..."
    mc_s "If anything, the dress just enhances them..."
    eli "Really, sweetie...?"
    eli "That's such a relief! I was worried that maybe it made [mommy_r] look too fat!"
    mc_t "Too fat? Is she crazy? Her body is insane..."

    show ep01_elidress20
    eli "How about back here, darling? Does it look too... revealing?"
    eli "After all, we don't want people to be distracted during [mommy_r]'s interview, do we?"
    mc_t "No! No... Of course not. They'll be just like me... with their jaws on the floor..."
    mc_s "Don't worry [mo_r], it looks perfect!"
    eli "You're such a sweetheart! Thanks, honey! Now, just one more dress and I'll let you go, okay?"
    mc_t "Let me go? I could stay here staring at her all day..."

    scene eigengrau with circlewipe
    show ep01_elidress21 with circlewipe
    mc_s "Ah yes [mo_r]! This one suits you perfectly!"
    eli "Perfect? Are you sure? It doesn't look bad at all? I'm not trying too hard or anything?"
    eli "Or do you think this might be a bit too much for an interview, darling?"
    mc_s "Well... I guess it depends on what type of modeling you're auditioning for, [mo_r]."
    eli "You know, it's for a European brand and they're looking for more daring models like [mommy_r]!"
    eli "This isn't something that could come up for them in any other agency around here, sweetie!"
    mc_s "You'll be fine, [mo_r]!"
    mc_t "More than fine... They'd be crazy not to hire her on the spot!"

    show ep01_elidress23
    eli "Don't you think it's too tight on my legs, honey? My thighs look too big..."
    mc_s "Oh no... no, they look great, [mo_r]."
    eli "The other one was way better... Don't you think, sweetie?"
    mc_s "[mo_r], c'mon! It's hard to tell!"
    eli "Well, I still need your opinion on it, darling!"
    mc_t "My opinion? I think you look hot as fuck in anything, [mo_r]..."

    show ep01_elidress22
    eli "And what about these, sweetie? I mean, I can't wear a bra with this dress... it kills the whole effect! Don't you think it looks good without it?"
    mc_s "Y-yeah... It does, [mo_r]..."
    eli "I'm glad, honey! Although it kinda shows [mommy_r]'s nipples every time she moves... That's not something we want them to see during the interview, right?"
    mc_s "Umm...eh...n-no...?"
    eli "Now if only we had something that could cover them. Oh well!"
    show ep01_elidress24
    eli "Isn't it too tight, sweetie? What about here? Doesn't [mommy_r]'s ass look weird?"
    mc_t ". . ."
    eli "Is it okay, darling?"
    mc_s "Yeah [mo_r], it's fine..."
    eli "Hm... it feels a bit snug on me but I think it might work..."
    mc_s "I g-guess it's okay, [mo_r]..."
    mc_t "Okay? It's more than okay... That ass is a work of art..."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_elidress25
    $ show_walkthrough("ep01_elibathdress_menu")
    menu:
        eli "Awesome, sweetie! So which one should [mommy_r] wear?"
        "Pick black dress":
            hide screen walkthrough_screen
            $ ep01_elidress += 1

            mc_s "Ack! U-uhm...how about that black one?!"
            mc_t "The black one hugs her curves so perfectly..."
        "Pick red dress":
            hide screen walkthrough_screen
            $ ep01_elidress += 2

            mc_s "Ack! U-uhm...how about that red one?!"
            mc_t "That red one makes her look so sexy and confident..."
    eli "Honey, have you really thought this through or are you just saying whatever pops into your head?"
    eli "Because don't think for a second that I didn't notice you focusing on [mommy_r]'s body instead of the dresses."
    eli "It's okay to stare, sweetie, I'm used to it. But the least you could do is actually comment on the dresses and not just my figure, don't you think?"
    mc_s "I... I just don't know anything about fashion, [mo_r]."

    show ep01_elidress26
    eli "For someone who doesn't know about fashion, you sure do like to ogle tits and ass a lot, young man."
    mc_s "I'm sorry, [mo_r]! But why didn't you ask Amber to help you then?"
    eli "I'd rather have a man's opinion on this, sweetie. Besides, your [si_full_r_low] knows nothing about clothes. Just look at the way she dresses."
    mc_s "What?! What's wrong with what she wears?"
    eli "You wouldn't understand, darling... you're not a woman. Trust me, these things are important and they make a huge difference between a woman looking beautiful or just being plain and boring."
    mc_s "Hmmm... you shouldn't judge people by their appearance, [mo_r]..."
    mc_t "Shit, why did I have to bring up Amber? [mo_r] always gets so worked up about her..."

    show ep01_elidress27 with hpunch
    if ep01_elidress == 1:
        eli "Well! Whatever, sweetie! I guess it doesn't matter anymore since we already picked [mommy_r]'s outfit. I'm going to wear the red one now and you can run along."
        mc_s "Actually... the black one looks really good on you t--"
        eli "Red one, final decision. Now scoot, young man."
        eli "I don't want to hear another word about your [si_full_r_low] or her horrible fashion sense."
    elif ep01_elidress == 2:
        eli "Well! Whatever, honey! I guess it doesn't matter anymore since we already chose [mommy_r]'s outfit. I'm going to wear the black one now and you can run along."
        mc_s "Actually... the red one looks really good on you t--"
        eli "Black one, final decision. Now scoot, young man."
        eli "And no more talk about Amber, okay? She always ruins everything."
    mc_s "Alright... see you later, [mo_r]..."
    mc_t "Why did I have to mention Amber? I think talking about Amber pissed her off somehow. Weird..."
    if not ep01_ambcall:
        mc_t "Oh well, I will just check up on Amber and see what she wanted."
    if ep01_ambcall:
        jump ep01_station


    else:
        jump ep01_home




label ep01_home:
    scene eigengrau with dissolve
##RM.POINTS.TRACK (amber, trust, +1)
##RM.POINTS.TRACK (amber, trust, -1)
# --
#AMBER CALLOUT
    show ep01_amberfail01 with hpunch
    $ playAudio(sfx_slamdoorhard, "sfx", 1, False, 0, 0)

    mc_s "Hey [sis_r]! I'm here! What's up?"
    if ep01_elicall:
        mc_s "Sorry for being late, I was with [mo_r] in the bath--"
    else:
        mc_s "I came as soon as I--"

    show ep01_amberfail02
    mc_s ". . ."
    amb "What the--"
    if ep01_elicall:
        mc_t "Oh fuck, why does this keep happening to me?!"
    else:
        mc_t "Oh shit, why does this always happen to me?!"
    mc_t "Brace yourself... Amber is definitely going to rip your balls off."

    show ep01_amberfail03
    mc_s "I-- I'm sorry! I didn't mean to see--"
    if ep01_elicall:
        amb "What the fuck, [bro_r]?! I called you forever ago! I thought you were busy or some shit!"
    else:
        amb "What the hell, dipshit?! Don't you know how to fucking knock?!"
    mc_s "Uh... You called me, remember? You told me to come..."
    amb "Get the fuck out, pervert! Can't you see I'm doing laundry?"
    show ep01_amberfail04
    mc_s "Who the hell does laundry half-naked?!"
    amb "Someone who doesn't want your pervy eyes all over her, asshole!"
    mc_s "And what happened to the girl who was all over me just a while ago, huh?"
    amb "Fuck you, dickhead!"
    mc_s "Whoa, whoa! Chill out, okay?"

    $ playAudio(amber_anger_theme, "music", 2, True, 2.5, 0)

    show ep01_amberfail05
    amb "Get the fuck out of here, now!"
    mc_s "Hey! Hey! Wait! I'm leaving, just give me a sec! Didn't you say you needed my help?!"

    show ep01_amberfail06
    $ unlock_memory("m_ep01_laundry")
    amb "Fine..."
    amb "I won't kill you this time, but next time..."
    mc_s "So? What do you want from me?"
    amb "Go wait in my room. I'll be there in a sec."
    mc_s "Seriously?"
    amb "Just fucking go, alright?"
    mc_s "Okay... okay. But seriously, put some clothes on before [mo_r] sees you like this."
    amb "Shut the fuck up."
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    show ep01_amberconfess01 with slowfade
    mc_s "Hmm... You look really worried..."
    amb "Huh... Wanna know what's bothering me?"
    mc_s "Nope."

    show ep01_amberconfess02 with hpunch
    amb "Shhh... You wanna get your ass kicked out? I'm trying to open up here. Don't fucking ruin it."
    mc_s "Ugh..."

    show ep01_amberconfess03
    mc_t "Ehhh... this doesn't look good."
    mc_s "Hey uhm... Come on!"
    amb "You think everything I say is just some dumb fucking joke, right? You think I'm just screwing around."
    amb "But if you could just listen and understand for once, maybe you'd see shit differently."
    mc_s "I--Uhm..."
    amb "I'm more than just a fucking problem, you know? I mean, I can think! I'm not some drooling moron who doesn't get how the world works!"
    mc_s "Hey, I didn't--"
    amb "Just fucking go... it's nothing, really."
    amb "It's not like you actually give a shit anyway..."
    $ show_walkthrough("ep01_amberconfess_menu")
    menu:
        "Stay":
            hide screen walkthrough_screen
            $ ep01_ambtalk = True
            $ rm.update("amber", "trust", 1)
            $ check_levels("amber", "trust", 1)

            mc_t "She looks really sad right now... maybe I should stay for a bit and see what happens."
            mc_s "Hey, calm down and tell me what happened, alright?"
            amb "Are you sure? You're not gonna bail on me?"
            mc_s "Hey! If you need to talk, I'm here for you, okay? It's all good!"
            mc_t "I can't just leave her like this... Even if she's a pain in the ass sometimes, she's still my [si_full_r_low]."
            amb "...Thanks, [bro_r]. I... I appreciate it."
        "Leave":
            hide screen walkthrough_screen
            $ rm.update("amber", "trust", -1)
            $ check_levels("amber", "trust", -1)

            mc_t "Nope. Not dealing with this drama and mood swings today. I'm out."
            mc_t "I've had enough of this shit. I'm gone."
            mc_s "Alright, sorry... I'm heading out then..."
            amb "Okay... Whatever... just fucking go."
            mc_s "Sorry, bye..."
            amb "...Figures. No one ever sticks around when I need them."
            amb "...Story of my fucking life."
            if ep01_elicall:
                jump ep01_station


            else:
                jump ep01_bath


#AMBER CONFESSION (ep01_ambtalk = True)
    $ playAudio(amber_sad_theme, "music", 2, True, 2.5, 0)

    show ep01_amberconfess04 with slowfade
    amb "I... I wanted to tell you..."
    mc_s "What's going on? This isn't like you at all."
    if ep01_park == 1:
        amb "By the way, this has fuck all to do with your girlfriend Antonella."
    elif ep01_park == 2:
        if ep01_lieamber:
            amb "By the way, this shit has nothing to do with your 'friend' Antonella."
        else:
            amb "By the way, this crap has nothing to do with your girl Antonella."     
    amb "While I was in the laundry room, I was thinking about something... just before you barged in and saw my pussy, of course!"
    mc_s "You always manage to turn the most serious things into some kind of sexual joke."
    amb "Anyway... The thing is, what if I'm just confused? What if what I feel isn't really love, but just like, gratitude or some shit?"
    amb "And you know... because I don't have any fucking experience with this kind of stuff, maybe I'm just mixing up those two feelings and calling it love or whatever..."
    mc_s "You're too dense for your age, [sis_r]..."

    show ep01_amberconfess05
    amb "You wanna fucking go, [bro_r]? Or would you rather shut your goddamn mouth and listen for once?"
    mc_s "Not at all..."
    amb "As I was saying... Am I just confused or is this all I've got left because no one else gives a shit about me? Not even our own fucking [mo_full_r]."
    mc_s "Don't say that... [mo_r] loves you. She's just... different."
    mc_s "Different people have different ways of showing love, you know."

    show ep01_amberconfess06
    amb "Oh, yeah? Well, it sure as hell doesn't look that way to me..."
    mc_s "But I really think she cares about you, Amber. Even if she doesn't say it much..."
    amb "You see it that way 'cause she treats you like you're some precious little prince. But to her, I'm just a walking, talking sin she has to put up with."
    mc_s "Hmmm..."
    amb "I don't think you can see the world the way I do... or should I say, the way the world sees me. You've had it pretty fucking easy so far, haven't you?"
    mc_s "I-- I don't know what to tell you, honestly..."

    show ep01_amberconfess07
    amb "Why are you being so nice to me, [bro_r]? Why aren't you a total dick like everyone else?"
    amb "Everyone thinks I'm trash, like some worthless piece of garbage that nobody wants around."
    amb "Am I really that shitty of a person...?"
    mc_s "Woah woah! You're not a bad person at all, Amber!"
    mc_s "I'm nice to you because I care about you. I'm not like them because I actually know you, and the girl I know is pretty incredible."
    mc_s "You're not garbage, and you're sure as hell not some worthless piece of shit."
    mc_t "Even if you act like a total bitch sometimes, I know that's not who you really are deep down..."

    show ep01_amberconfess08
    amb "You... you really mean that?"
    mc_s "Of course I do! I have no idea what their problem is, but if they can't see how awesome you are, then fuck 'em!"
    amb "Thank you... thank you... I really fucking appreciate what you just said, you know? hehe"
    mc_s "You're welcome... Just be yourself, and don't worry about those assholes, okay?"

    show ep01_amberconfess09
    mc_t "Now I get it... as aggressive and crazy as my [si_full_r_low] is... she's still just a girl who desperately wants to be loved... as cliché as that sounds."
    mc_t "But who cares... just look at her, finally smiling for once..."
    mc_t "She's actually pretty cute when she's happy like this..."
    mc_t "I wish I could see this side of her more often..."

    show ep01_amberconfess10 with hpunch
    amb "See? This is why I like you so much, [bro_r]. You're the only one with the balls to talk to me straight like this. But you're not scared of me."
    amb "When you're around, I feel... different. Like my heart starts going crazy in my chest."
    show ep01_amberconfess11
    $ unlock_memory("m_ep01_confession")
    amb "You're always telling me how insane and terrible I am, and yeah, I know I'm all those things, I really fucking am... But your words, I... I like them... hehe."
    amb "Don't get it twisted though. You're still a fucking asshole most of the time. But... that's what makes you so damn likeable, I guess."
    mc_s "I don't know if I should feel flattered or offended by that..."
    amb "Just shut up and take the compliment, dickhead."
    show ep01_amberconfess12
    amb "Well, maybe all this was just a way for me to get my head straight..."
    amb "I mean... whatever Antonella is to you, and yeah... I said this had nothing to do with her, 'cause, well, it really fucking doesn't..."
    amb "Her being around just made me want to sort out my own feelings for you."
    mc_s "Huh?!"

    show ep01_amberconfess14 with vpunch
    amb "What I'm trying to say is, I want to know if what I feel for you is love, but not the [br_full_r_low]-[si_full_r_low] kind... like a different kind of love..."
    amb "The kind you might have with Antonella, if you do feel that way about her... you know what I'm saying?"
    mc_s "Uh-huh..."
    amb "So... do you love me, [mc_name]?"
    amb "But like, real love, not just [sib_r] love. The genuine thing, the grown-up kind... the kind between a man and a woman. And I'm not just talking about fucking."
    amb "I mean, that would be amazing too, but I'm more interested in the other stuff right now."
    amb "I can't take this uncertainty anymore, I just need to know so I can stop feeling so lost and stupid about it!"
    show ep01_amberconfess15
    amb "Be straight with me, [mc_name]. What's your answer? Do you love me or not?"
    if not ep01_elicall:
        $ show_walkthrough("ep01_amberconfess_menu2")
    else:
        $ show_walkthrough("ep01_amberconfess_menu2b")
    menu:
        mc_t "Do I actually love her that way?"
        # WILL SKIP ELIZABETH
        "Yes":
            hide screen walkthrough_screen
            $ ep01_amblove = True
            $ stopAllSubchannels(channel="music", fadeout=8)

            mc_t "Fuck, this feels like some kind of ultimatum, doesn't it?"
            mc_t "She's my [si_full_r_low], I can't love her the way she wants me to. But maybe, if I take it slow, I can guide her away from twisting it into something else."
            mc_s "Yes, I do love you, Amber."
            mc_s "I love you so much..."
            mc_s "But not in the way you're hoping for... at least, not yet."
            amb "Not yet, huh? The fuck's that mean?"
            mc_s "I get where you're coming from, [sis_r]. You don't really know what love is, right? It's easy to mix up your feelings."
            mc_s "And if you're confused, I'm sorry, but I can't take advantage of that confusion. But let's work it out together, and see if those are the kind of feelings you're really looking for."
            mc_s "Then you can decide what you want to do, and whatever you choose, I'll respect it."
            mc_t "What the fuck have I gotten myself into? What if I end up regretting this?"

            show ep01_amberconfess16 with hpunch
            amb "Oh my fucking god! Yes! Yes! Absolutely, let's do this together!"
            amb "Thank you, [mc_name]. Thank you so damn much."
            mc_s "Why are you thanking me? I didn't do anything special..."
            amb "Because you were straight with me, dumbass. You didn't just tell me what I wanted to hear, but what you actually feel."
            amb "I promise you, I won't fuck this up! And if it works out, you'll have the best goddamn girlfriend you've ever had!"  
            amb "Also... hehe... who says you're the one who's gonna be 'taken advantage of' here? Hahaha!"
            mc_s "Wha--?!"
            amb "Oh, sorry, but that's how I deal with stress! Deal with it, [mc_name]. It's either that, or I'll kick your balls into orbit, I'm warning you! Take your fucking pick."
            mc_s "Alright! Alright! Fine! But get off me, you're crushing me. This is starting to get really uncomfortable."
            amb "Hmph! Then let me rest my head on your arm, that way we can both be comfy, jerk."
            show ep01_amberconfess17
            mc_t "Why the fuck did I get myself into this mess...?"
            amb "Thank you... thank you, I love you so much, [mc_name]..."
            mc_s ". . ."
            mc_t "What the hell am I doing? Am I really going to let this happen? With my own [si_full_r_low]?"
            mc_t "But seeing her like this, so vulnerable and open... I can't just crush her heart. Not now."
            amb "You have no idea how happy you've made me, [bro_r]. I've never felt like this before..."
            amb "Please don't let this be a dream. Please let this be real. I need this... I need you."
        "No":
            hide screen walkthrough_screen
            $ stopAllSubchannels(channel="music", fadeout=8)

            mc_t "How the fuck am I supposed to break her heart? She'll never leave me alone after this... I need to be direct and crush her hopes once and for all."
            mc_s "Look, [sis_r]..."
            mc_s "These feelings you have for me... I mean, you probably don't even understand what you're really feeling..."
            mc_s "Maybe the kind of love and affection you're looking for... isn't actually romantic or sexual."
            mc_s "I bet you're just desperate for any kind of love and affection, and maybe... just maybe... I'm the closest thing you have to that right now."
            mc_s "What you're craving is just some affection from anyone who will give it, and I'm just a convenient option for you."

            show ep01_amberconfess13 with vpunch
            amb "Shhhh..."
            mc_s "I mean, hey... I'm no better than you in that regard! Maybe I'm confusing my own feelings too, right?"
            amb "Shut the fuck up... Just... shut up..." 
            mc_s "C'mon, [sis_r]... You wanted me to be honest with you, and this is the truth. The harsh, ugly truth."
            amb "Yeah, but you don't have to be so goddamn cruel about it."
            amb "I've never been more sure of anything in my life, and you're turning what could be the happiest moment I've ever had into my worst fucking nightmare."
            mc_s "I'm sorry, I--"
            amb "Just get the fuck out... please, just leave me alone. Go away and leave me the hell alone."
            mc_t "I'm sorry [sis_r], but this is for your own good. It's what's best for both of us."
            if ep01_elicall:
                $ stopAllSubchannels(channel="amb", fadeout=1.5)
                jump ep01_station


            else:
                mc_t "I'll just go check on [mo_r] and see what she wanted from me earlier."

                jump ep01_bath


#AMBER NIGHT
    scene eigengrau with dissolve
    $ stopAllSubchannels(channel="amb", fadeout=1.5)

    show ep01_amberconfess18 with ccirclewipe
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.1)
    $ playAudio(sfx_night_cicada, "amb", 2, True, 2.5, 0)

    amb_t "Oh shit, I fell asleep... What time is it?"
    amb_t "Did I dream all that or was it real? Was it just a fucking dream?"
    amb_t "Uhm... well, he's still here sleeping and I'm hugging him, so..."

    show ep01_amberconfess19
    amb "Hey, [mc_name]... You awake?"
    amb ". . ."
    amb_t "Fuck yes... This is perfect!"
    amb_t "I wonder... What would happen if I pulled his underwear down, just a bit... You know, just to get a little peek..."
    amb_t "Uhm... but he's still in his school clothes..."
    amb "Last warning, [bro_r]... If you're awake, say something now, got it?"
    amb ". . ."
    show ep01_amberconfess20 with vpunch
    amb "Well, since you're not answering, I'll just use you to rub myself off, okay? Hehehe."
    show ep01_amberconfess20 with vpunch
    amb ". . ."
    show ep01_amberconfess20 with vpunch
    amb_t "This feels fucking amazing..."
    amb_t "My dreams are finally coming true and I don't have to just fantasize about it anymore..."

    show ep01_amberconfess21 with vpunch
    amb_t "Feels so good... So damn good..."
    amb_t "If you only knew how many times I've gotten myself off thinking about you... How I touched myself dreaming it was you doing it..."

    show ep01_amberconfess21 with vpunch
    amb "Mmm... mmm... mmm... mmm... Mmm"
    amb_t "Umh... My big [br_full_r_low]... Such an innocent, naive man..."

    show ep01_amberconfess21 with vpunch
    amb_t "Don't blame me for being a bad girl... You're the reason I'm like this..."
    amb_t "Fuuuccckkk... I can't take it anymore."

    show ep01_amberconfess22
    amb_t "It's not gonna hurt... I promise... I just wanna see it..."
    amb_t "Ugh... Let me move you a little bit so you don't notice I'm on top of you."

    show ep01_amberconfess23
    amb_t "Alright, there we go... That should do it."
    amb_t "Oh... I can smell you from here... Such an intoxicating scent..."
    amb "Don't mind me now, okay?"
    amb_t "Alright... Now let's get a better look at this..."

    show ep01_amberconfess24
    amb_t "Ha... Here we go"

    show ep01_amberconfess24 with hpunch
    amb "Stop whimpering, [mc_name].. You don't even know what I'm doing... This will only take a little while, okay?.. Just a bit."
    amb_t "Ah, perfect... Let's check this thing out up close."

    show ep01_amberconfess26 with slowfade
    amb_t "Wow... Look at what my big [bro_r_low] has been hiding from me all this time... This thing is fucking huge..."
    amb_t "So thick and hard... It's like a goddamn iron bar..."
    amb_t "Fuck! Why is my mouth suddenly watering...?"

    show ep01_amberconfess26 with vpunch
    mc_s "Huh?... What is-- huh? Am-ber?"
    mc_s "What the--?! What the fuck are you doing?!"

    show ep01_amberconfess25
    amb "Uhm, hi..."
    mc_s "Why are you on top of me?! Where the hell are my pants?!"
    amb "What? Ehh...! You were having a nightmare! And when I tried to calm you down, you pulled them off and threw them away... and, and I'm here on top of you because..."
    amb "Because...!"
    amb "B-because...! ...I was going to give you mouth-to-...!"
    mc_s "--Mouth? Mouth-to-what? And why are you half-naked?!"
    amb "B-becaaauuuse, you were having nightmares about girls giving you mouth-to-mouth and..."
    amb "And... you were rolling around so much, I tried to catch your underwear before you ended up putting your dick in my mouth--!"
    mc_s "That's the worst fucking lie I've ever heard..."
    amb "Alright! Okay! The truth is... I might have gotten a bit crazy and, maybe, just maybe, I touched you and, kinda, did a bit of exploring and, um, a little bit of sniffing and--"
    mc_s "What the actual fuck, Amber?!"
    amb "Now don't look at me like that, okay!? I'm only gonna say this once, so pay attention!"
    $ show_walkthrough("ep01_amberconfess_menu3")
    menu:
        amb "Do you want me to continue or not?!"
        "Yes":
            hide screen walkthrough_screen
            $ rm.update("amber", "cor", 3)
            $ check_levels("amber", "cor", 3)
            $ ep01_first = True

            mc_t "Think... think, what's the best solution to all this...?"
            mc_s "Continue..."
            mc_t "Fuck! My dick spoke for me!"

            $ playAudio(amber_sexy_theme2, "music", 2, True, 2.5, 0)

            show ep01_amberconfess32 with vpunch
            amb "Oh, big [br_full_r_low]... I didn't expect that answer from you... Where's my [bro_r_low] who usually tells me to fuck off, hmmm?"  
            amb "Tell me, do you want me naked too?"
            mc_t "I'm so dead... Can't think straight."
            mc_s "Ehmm... um..."
            amb "You don't? Because I'm already half-naked... it wouldn't be fair to leave me like this, would it?" 
            show ep01_amberconfess33 with circlewipe
            amb "See? This is better, don't you think?"
            mc_s "!!"
            amb "Mmmmm? You like what you see...? No words for your naughty little [sis_r_low]?" 
            mc_s "...!"
            amb "Mmmmhmm... I see you're talking with something else!"
            mc_s "Oh, shit!!"
            mc_s "Seriously! I--- I think we've taken this too far...!! We need to stop."

            show ep01_amberconfess34
            amb "Stop? After everything that's happened up until now? It's too fucking late for that." 
            amb "Besides, if I stop right now, I'm not gonna be able to handle the hunger between my legs and I'll end up biting one of your arms off in my sleep... and neither of us wants that, right?"
            mc_t "How the actual fuck is she able to say those things at her age?!"
            mc_t "I feel like a total retard next to her..."
            amb "Listen, I'll make you a deal..."
            mc_s "Okay..." 

            show ep01_amberconfess35
            amb "Uhmmmm... I really... really wanna fuck you right now... but you know, I'm a little nervous, so, if you let me put just the tip in, then, and only then, I'll stop. I promise."
            mc_t "My god! I can feel her heart racing and her tits pressing against me, even through my clothes."

            show ep01_amberconfess37
            amb "So? Can I..? I promise you're gonna fucking love it." 
            mc_t "She talks like she's been fucking all her life... and I haven't even kissed anyone yet."

            show ep01_amberconfess36
            amb "Come on... come on... put my big [br_full_r_low]'s huge cock in my hungry pussy, will ya...?"
            mc_s "Amber... listen to me, I--"
            amb "Argh! What is it now?!"
            mc_s "It's-- it's my first time... you know...?"
            amb "Oh...! Ohhh! Really?! For fucking real?!"  
            mc_s "Yes..."

            show ep01_amberconfess40 with vpunch
            amb "Wow! I-I guess now I've got the upper hand in this, don't I?"
            mc_s "Ehm... Don't tell me you've already had sex?"
            amb "Hmmm...? Maybe I have..."  
            amb "If I told you I already fucked someone, would it make you feel better about fucking me? I mean, to think that at least you're not popping my cherry or some shit..." 
            mc_s "Agh, no. I'm telling you this because I don't want you expecting more from me than what you're gonna get... Also... how and who the fuck did you have sex with?!"
            amb "Aww... why are you asking all this? Are you jealous? Is my big [bro_r_low] jealous that someone else got his little [sis_r_low]'s cherry before he could? Aww!"
            mc_s "When, where, why, and with who did you fuck, Amber?!" 
            amb "Okay, okay, chill out. Let's see, my pussy will answer your questions..."
            show ep01_amberconfess38
            amb "First.." 
            show ep01_amberconfess38 with vpunch
            amb "Ahh...." 
            amb "I didn't have sex!"
            show ep01_amberconfess38 with vpunch
            amb "Second... Ahh... I haven't been with any guy before!"
            show ep01_amberconfess38 with vpunch
            amb "And third... the one popping my cherry is under me right now! Ahh..."  
            mc_s "What?!"

            show ep01_amberconfess41 with vpunch
            amb "No one has ever fucked me before, until now... Ahh... Ahhh!"
            amb "Can you feel it? Can you feel my cherry tearing apart? Can you feel my heartbeat going crazy with pain and pleasure? You feel it?"
            show ep01_amberconfess41 with vpunch
            mc_t "Fuck! It feels so fucking good! It's so hot and wet inside!"
            mc_t "Fuck! Fuck! Fuck! Focus! You gotta put a stop to this!" 

            show ep01_amberconfess41 with vpunch 
            mc_s "Am-ber... Amber..."
            amb "Ahh... Big [bro_r_low]..."
            show ep01_amberconfess41 with vpunch
            eli_y "Amber? [mc_name]? Dinner's ready!"
            show ep01_amberconfess42
            mc_s "OH SHIT!"
            amb "Shhhhhh... Let me handle this..." 
            amb_y "I don't fucking know where he is! And don't bother me! I'm busy!!"
            mc_s "Amber... what the actual fuck?!"
            amb "Just relax and trust me..."
            amb_y "NOW FUCKING LEAVE ME ALONE!!! UGH!!!"  
            mc_s "What are you doing?!"
            eli_y "Well, do whatever you want! The food will be here when you decide to have a civilized meal! Not that you need it, fatass!"
            amb_y "I HEARD THAT, YOU OLD HAG!!!"
            eli_y "WHAT DID YOU JUST SAY TO ME?! YOU KNOW WHAT?! DO WHATEVER THE FUCK YOU WANT, YOU LITTLE SHIT!"  
            mc_s "...!"  

            show ep01_amberconfess39
            mc_s "WHAT THE FUCK IS WRONG WITH YOU?! YOU'RE MAKING IT WORSE!"
            amb "See? I told you to trust me. Now she won't bother us, and we can do whatever the fuck we want." 
            amb "Now, where were we...? Mmm...?"
            mc_s ". . ."

            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            $ stopAllSubchannels(channel="music", fadeout=1.5)
            jump ep01_station


        "No":
            hide screen walkthrough_screen

            mc_s "No! What the fuck, Amber!"

            show ep01_amberconfess28 with hpunch
            mc_s "Are you out of your fucking mind? What if [mo_r] finds us like this?!"
            mc_s "No, we have to stop... We're not in some sleazy love hotel and if someone catches us, we're totally screwed. So just stop!"

            show ep01_amberconfess27
            amb "Just one minute! Come on...! Just one fucking minute! I really need this!... Please."  
            mc_s "No, no... Think about the consequences! Where the hell did you put my pants?!"

            show ep01_amberconfess29 with vpunch
            amb "Hey! Stop squirming around!"  
            mc_s "Where did you put them?! Hurry!"  
            amb "You're gonna fall--"
            show ep01_amberconfess30 with vpunch
            mc_y "GAAHHH!"
            amb "--off the bed if you keep moving around like that..."
            show ep01_amberconfess31 
            mc_s "Unnngghh..."
            amb "I told you you'd fall off the bed, didn't I?!"
            amb "I bet that was a hard fall... But it's not too late... I can still kiss it better."
            $ stopAllSubchannels(channel="amb", fadeout=1.5)  
            jump ep01_station




label ep01_station:
    scene eigengrau with clouds
##RM.POINTS.TRACK (isabella, trust, +1)
# --
#ARRIVING TO TOKYO
    show ep01_antobd01 with bokeh
    $ playAudio(sfx_stationbeep, "amb", 2, True, 2.5, 0)
    $ playAudio(sfx_trainstationquiet, "amb", 1, True, 2.5, 0)
    isa "[daddy_r]... are you awake? We've arrived."
    mc_s "Hm... we're here already?"
    isa "Yes. Come on, get up!"
    mc_s "Did I doze off?"
    isa "More than dozing off! You were fast asleep and snoring so loudly!"
    mc_s "Really!?"

    show ep01_antobd02
    isa "And drooling too! Haha..."
    mc_s "Nonsense... What time is it?"
    isa "It's almost 9 PM. We should get going!"
    show ep01_antobd03 with ccirclewipe
    $ stopAudio(channel="amb", subchannel=1, fadeout=1.5)
    $ setChannelVolume(channel="amb", subchannel=2, volume=0.5, fade_duration=1.5)

    mc_t "How many years has it been... It felt more like a dream than memories, although I'm not sure if they're real or not..."
    mc_t "I mean... they are, right? ... Right...?"
    isa "--and there are also other anime conventions throughout Japan, like in Hiroshima or Nagoya, so maybe one day I can attend those too--"
    mc_s "Huh? What?"

    show ep01_antobd05
    isa "Awww... And here I thought you were listening to me, [daddy_r]!"
    isa "You left me talking to myself while you were lost in your own thoughts! [daddy_r]!!"
    mc_s "I'm sorry, sorry! I didn't mean to ignore you... I was just a little distracted."
    isa "What could possibly be more important than your only [dau_r_low]?"
    mc_s "It's just... I think I dreamt about the past, but I'm not sure... It might have been something else, although those things felt real..."
    mc_s "I mean, they did, but I still wonder... It's so confusing!"

    show ep01_antobd04
    isa "The past? Do you mean... when you were still living in Osaka, [daddy_r]?"
    mc_s "No, no... way before that... When you weren't even born yet. Back then."
    isa "And why do you think you dreamt of that? Who was in your dream?"
    $ show_walkthrough("ep01_antobd04_menu1")
    menu:
        "Mention Antonella":
            hide screen walkthrough_screen
            $ rm.update("isabella", "trust", 1)
            $ check_levels("isabella", "trust", 1)

            mc_s "Why? ... Hmmm, maybe because this city reminds me of those times... In a way. And who was there...? Well... your [gra_r_low], your [aun_r_low] Amber... and, uhm... your [mo_full_r_low]."
            mc_t "I don't like mentioning her [mo_full_r_low], I should have lied or changed the subject."

            show ep01_antobd06
            isa "Aww... was my [mo_r_low] in your dreams? Was she beautiful?"
            mc_s "Eh... yes... just like in the pictures you have..."
            isa "Was she cosplaying too?!"  
            mc_s "Umm... No, I don't think so."
            isa "She would've looked amazing in cosplay!"
            mc_t "Antonella... in cosplay? I can't even imagine..."
        "Don't mention Antonella":
            hide screen walkthrough_screen

            mc_s "It doesn't matter... I probably dreamt that because I'm getting old and my memory is starting to play tricks on me..."
            mc_t "I don't like mentioning her [mo_full_r_low]... It's for the best."
            isa "Yeah, right..."
            show ep01_antobd08
            isa "Uhm... [da_r]... why don't you want to tell me? Do you not trust me enough?"
            mc_s "What? Of course I trust you, Isabella!"
            isa "Really? So you would tell me then?!"  
            mc_s "It's really nothing, just some silly things about your [gra_r_low] and [aun_r_low] Amber..."
            isa "But [da_r], if it's nothing, why won't you tell me? I want to know about your past too..."
            mc_s "I know, sweetheart. It's just... some memories are harder to talk about than others."
            mc_s "Give your old man some time, okay? I promise I'll tell you about it someday."

    show ep01_antobd07
    isa "Uhm... and what was that dream about, [daddy_r]? Why was [aun_r_low] Amber there? And [gra_r] too?"
    mc_s "Hehe... Why so curious, little one?"
    isa "Well! It wasn't anything bad, right?"
    mc_s "Oh! No! Of course not, sweetheart!"
    isa "[da_r]! Please tell me!"
    mc_s "Uh! Isabella... We better hurry up; it's getting quite late!"
    isa "Okay, okay! You win this time, [da_r]! Let's go then..."
    show ep01_antobd09 with slowfade
    isa "But [da_r], you have to promise to tell me everything later, okay?!"
    mc_s "Alright, alright! I'll tell you all about it... Now let's get out of here!"
    mc_t "What the... Could it be...?"

    show ep01_antobd10
    mc_t "Good god, I'm overthinking everything... It's impossible for her to be here... Ridiculous..."

    $ show_walkthrough("ep01_antobd_menu2")
    menu:
        "Look at girl":
            hide screen walkthrough_screen
            $ ep01_antobday = True

            mc_t "No... It can't be. After all these years, there's no way..."

            $ stopAllSubchannels(channel="amb", fadeout=1.5)

            show ep01_antobd11 with vpunch
            $ setChannelVolume(channel="sfx", subchannel=1, volume=0.4)
            $ playAudio(sfx_glitch, "sfx", 1, True, 2.5, 0)

            show ep01_antobd11 at animated_glitch
            mc_t "Huh?!"
            mc_t "Antonella?! Are you really here? In Tokyo?"

            jump ep01_birthday


        "Don't look at her":
            hide screen walkthrough_screen

            mc_t "Nah, there's no way that girl could be her... After all these years... How stupid of me..."
            mc_t "I need to stop living in the past. That chapter of my life is over."

            $ stopAllSubchannels(channel="amb", fadeout=1.5)
            jump ep01_newhome




label ep01_birthday:
    scene eigengrau with dissolve
#ANTONELLA BDAY
    show ep01_antobd12 with clouds_inverse
    show ep01_antobd12 at animated_glitch
    mc_s ". . ."
    anto "Come on! Get in!"
    mc_s "Oh... Huh?! Antonella? What are we doing here?"

    $ stopAllSubchannels(channel="sfx", fadeout=2.5)

    show ep01_antobd13
    $ setChannelVolume(channel="amb", subchannel=1, volume=1)
    $ playAudio(sfx_restaurant, "amb", 1, True, 1.5, 0)
    anto "What do you mean what are we doing here? It's my birthday, silly!"
    $ playAudio(antonella_past_happy_theme, "music", 2, True, 5, 0)

    mc_s "Birthday?"
    anto "Don't you remember?"
    mc_t "Hold on!! Wait!!! It was Antonella's birthday!?"
    mc_t "This has happened before... Hasn't it?"

    show ep01_antobd14 with vpunch
    anto "I reserved a table. So c'mon in, before they cancel our reservation!"
    mc_s "Eh... I kinda remember you told me your parents and friends would join us here..."
    anto "Well! They changed their plans, so it will just be the two of us!"
    mc_t "Right... This all happened already... We met in that park and then came here! And then --"
    anto "Can we sit already? I'm starving!"
    show ep01_antobd15 with slowfade
    anto "Why are you looking at me like that? Is there something wrong?"
    mc_s "Huh?! No, nothing. It's just... I don't understand... this... this place... this date."
    anto "What are you talking about?"
    mc_s "Me! Us! Why is it happening? The last thing I remember is being with--"

    show ep01_antobd16
    anto "Wait... what do you mean? You're worrying me, [mc_name]."
    mc_s "Sorry, sorry! It's alright, I think I just zoned out a little... Must be tired."
    anto "Oh! Phew, you scared me... Maybe you're just as hungry as I am."
    show ep01_antobd17
    anto "Oh look, the waiter is coming."
    mc_t ". . ."
    mc_t "Isabella! That's it... I was with Isabella when I woke up in the train! What happened to me?"
    mc_t "Then this girl passing by earlier looked exactly like Antonella! And now here I am back at this date... It makes no sense!"

    $ stopAllSubchannels(channel="music", fadeout=2.5)

    show ep01_antobd18
    $ playAudio(sfx_glitch, "sfx", 1, True, 2.5, 0)

    show ep01_antobd18 at animated_glitch
    mc_t "Could it be that I'm losing my mind?! Must be that mix: zolpidem and sertraline!!"
    anto "--we'll have one salmon nigiri and one maki sushi please..."
    show ep01_antobd19 at animated_glitch
    mc_t "The food is already here... It's like it's playing a recording."
    mc_t "And skipping scenes... And for some reason, I don't have any control over anything, as if I had to play the role I played back then!"

    $ stopAllSubchannels(channel="sfx", fadeout=1.5)

    show ep01_antobd20 with slowfade
    anto "Aren't you hungry?"
    mc_s "Not really... Why? Am I acting weird?"
    anto "Well! Since we got here you've been a bit spacey."
    mc_s "Sorry... I feel a little strange today... It must be something I ate."

    show ep01_antobd21
    anto "Can we still make this date fun, or is something bothering you?"
    mc_s "No, of course not!"
    anto "You sure? You know you can tell me anything, right?"
    anto "I'm here for you, [mc_name]. Always."
    mc_t "If only that were true... If only you knew what I know now, Antonella."
    mc_s "Actually, there's something I want to tell you--"

    show ep01_antobd22 with hpunch
    mc_t "And here comes this part... the first and only time I saw Antonella seriously upset."
    mc_t "I never knew what upset her so much... and it's only now that I recall this happening..."

    show ep01_antobd23 with slowfade
    $ playAudio(antonella_mistery_theme, "music", 3, True, 1.5, 0)

    mc_s "Is something wrong?"
    mc_t "She didn't say anything... Just sat there with that look on her face... staring off into the distance..."
    mc_t "I didn't say anything either... I guess I wanted her to tell me, or I simply had no idea what to say..."
    mc_t "If I had known then what I know now... Would it have made a difference?"

    show ep01_antobd24
    mc_s "Did something happen?"
    anto "...It's nothing. Don't worry about it."
    show ep01_antobd25
    mc_s "Antonella, talk to me. What's going on?"
    anto "I said it's nothing, okay? Just drop it, please."
    mc_s "You don't seem alright..."

    show ep01_antobd26
    anto "I'm good... yeah, everything is fine..."
    anto "You know how life throws you curveballs and you just gotta roll with the punches? It's like... I've been carrying this heavy burden, and suddenly, it's just... gone."
    anto "Feels liberating, like I can finally breathe easy for the first time in forever. Can't quite put my finger on why though, it's strange as hell."
    mc_s "How long have you been feeling this way?"

    show ep01_antobd27
    anto "Let's not dwell on that now, okay? Let's just enjoy this dinner. Besides, it's my birthday after all."
    mc_s "Uh... Right."
    mc_t "I should have pressed her for more answers. I didn't know better back then. Now I do."

    $ stopAllSubchannels(channel="music", fadeout=1.5)

    show ep01_antobd28
    mc_s "So, if it's your birthday, does that mean you get to make a wish, or do I get a wish for putting up with your mood swings today?"
    anto "How about we both make a wish? Mine's already come true, though. Your turn. But make it a good one, no wishing for more wishes—that's cheating. Ready?"
    mc_s "Alright then, I wish for the power to read minds. Starting with yours."

    show ep01_antobd29
    anto "You said it out loud! That doesn't count! Your wish is null and void!"
    mc_s "Seriously? Damn! And here I thought I'd finally unlock the mystery that is Antonella..."
    anto "Besides, you wouldn't like what's inside my head anyway. You might not be able to handle the chaos in there."
    mc_s "Chaos can be exciting. Besides, that's just another way of saying I'd be seeing a side of you that no one else ever gets to see."

    show ep01_antobd30
    anto "Haha... I never thought about it like that... You really are a sweet guy..."
    anto "Thank you, [mc_name]... Sometimes I forget how kind you truly are. Anyway, since your wish is a bust now... Is there anything you want from me instead?"
    mc_s "Uhm..."
    mc_s "For you to forgive me."
    anto "Huh?"
    mc_s "I know you said you didn't want gifts today, but..."

    $ playAudio(antonella_love, "music", 2, True, 2.5, 0)

    show ep01_antobd31
    mc_s "Would you accept this one as a present?"
    anto "A... present? Uhm..."
    mc_s "Maybe I'm overstepping, sorry"

    show ep01_antobd32
    anto "Ah?! No! Don't apologize! I just... wasn't expecting you to ask for something like that. It caught me a bit off guard."
    mc_s "Uhm..."
    anto "It's just... so unexpected..."
    show ep01_antobd33
    anto "Why...? Why would you want to give me something? Of all things..."
    mc_s "Because you mean so much to me, Antonella..."
    mc_s "In this short time we've known each other... you've made me realize what's been missing in my life..."
    mc_s "Someone who inspires me to be a better man than I was yesterday."

    show ep01_antobd34
    anto "Ehhh... You really know how to tug at a girl's heartstrings, don't you? Haha..."
    mc_s "I'm not finished. I guess what I'm trying to say is... I feel like you've become someone special in my life now--"

    show ep01_antobd36
    anto "[mc_name]... You don't know anything about me. If you did..."
    mc_s "Then help me understand you, Antonella... Help me get to know you and let me judge for myself."

    show ep01_antobd37
    anto "I... think you're making this hard for me, handsome."
    mc_s "Is that a bad thing?"
    anto "Bad? No, not at all. A bit challenging? Maybe... but I'll do my best to open up to you one day."
    mc_s "It makes me happy to hear you say that... So what are you waiting for? Are you gonna open your present or what?"
    anto "What--! Oh, right! The present!"
    scene eigengrau with dissolve
    show ep01_antobd35 with hpunch
    anto "That's..."
    mc_s "Heh... Looks like that memory is still fresh in your mind..."
    mc_s "That day, I thought the necklace would suit you, so I asked the clerk to hold it for me, hoping I'd get to see you wear it someday."
    anto "Uhm... [mc_name]... I don't know what to say... This must've cost you a fortune..."
    mc_s "Hah! Well... I'm in debt now, so, yeah... but that doesn't matter."
    anto "You're kidding, right? But why!?"
    mc_s "It's simple... Because you mean that much to me."

    show ep01_antobd38
    anto "You... you make this so difficult... But I love that about you too. You're so different from... everyone else."
    mc_s "Huh? Difficult? How so?"
    anto "Oh... Haha! Uh... it's nothing... Forget I said that... It doesn't matter now."
    mc_t "Even back then, she was hiding something from me... But what? What burden was she carrying?"
    mc_t "If only I had pushed harder, dug deeper... Maybe things could have been different."

    show ep01_antobd39 with slowfade
    mc_t ". . ."

    show ep01_antobd40 with flash
    mc_t "Kissing her... touching her... hearing her voice and inhaling her sweet scent..."
    mc_t "She felt like home. Now it's all gone... And I can't go back anymore."
    mc_t "The only path left is forward..."
    mc_t "But how can I move on when my heart is still stuck in the past?"

    show ep01_antobd41 with hpunch
    mc_s "Huh? Why did you stop? Did I do something wrong?"
    anto "No... That's the problem. Everything feels so right when we're together... And I don't want that feeling to fade away."
    mc_s "Then don't let it fade."
    anto "Hehe, sometimes you make it sound so easy... and that scares me a little."
    mc_s "Sometimes you're so cryptic... I don't know how I'm supposed to respond to that..."
    anto "That's also one of the reasons why I love you, [mc_name]."
    anto "Even if... even if I don't think I deserve your love."
    mc_s "Huh?!"

    show ep01_antobd42
    anto "Now then, could you do me a favor?"
    mc_s "Huh? What kind of favor?"
    anto "Haha! Well, could you be a gentleman and help me put on the necklace?"
    mc_s "Oh! Yes, of course!"

    show ep01_antobd43 with slowfade
    anto "Oh... Your hands are so warm... it feels nice."
    mc_s "T-Thank you."
    anto "Well... you know what happens after you give a girl a gift... Don't you?"
    mc_s "Huh?"
    anto "A reward!!"
    show ep01_antobd44 with hpunch
    anto "Let's go. I'm full of energy now! And you have a reward to claim, if you catch my drift!"
    anto "Today, let's forget about everything else... and just be together."
    mc_t "Antonella... I wish I could freeze this moment forever."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with clouds
    show ep01_backhome01 with bokeh
    $ playAudio(sfx_stationbeep, "amb", 2, True, 2.5, 0)
    isa "[da_r]?! [da_r]! Are you alright? Did you have a stroke or something?!"
    mc_s "Uh... huh...? Oh, Isabella... Sorry, I must've zoned out for a bit..."
    isa "No way, you were completely out of it!! Like frozen in time!!"
    mc_s "I... had some sort of dream... or memory, I guess, but I'm not really sure..."
    isa "Again, [da_r]? How long will these dreams keep happening??"
    mc_s "To be honest, I don't know myself... I guess it's the effect of some meds I'm taking..."
    isa "Meds? [da_r], what meds are you on!!"
    mc_s "Easy, sweetheart. Meds for the pain from my surgery."

    show ep01_backhome02 with slowfade
    mc_t "That necklace... Antonella's necklace, now around Isabella's neck. A gift that meant everything and led me to nothing."
    isa "You're looking at the necklace... [mo_r] loved it, didn't she?"
    mc_s "Yeah, she did. She looked stunning wearing it."
    mc_s "Just like you do now, Isabella. You remind me so much of her sometimes..."
    isa "And what about the dream, [da_r]? What was it about?"
    mc_s "Huh?? Oh... uh... I don't remember. It just got triggered when I saw that girl who looked like..."

    show ep01_backhome03
    isa "What girl? Looked like who, [da_r]?"
    mc_s "Ehh... Well, never mind. Probably just someone else... Just forget it, okay? It was nothing."
    isa "Forget it? No way, [da_r]! Tell me everything, pretty please!"
    isa "I want to know what's going on with you. I worry about you, you know?"
    mc_s "Come on, Isabella. We really should get going..."
    isa "[da_r]!!! Please, just tell me!"
    mc_s "Yes, yes! We're going, we're going!"
    mc_t "I can't burden her with my past. It's not fair to her. She deserves better than that."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    jump ep01_newhome




label ep01_newhome:
    scene eigengrau with dissolve
#TRAVEL TO NEW HOME
    $ playAudio(sfx_taxidoor, "sfx", 5, False, 0, 0)

    show ep01_backhome04 with circlewipe
    $ playAudio(sfx_taxiint, "amb", 1, True, 2.5, 0)
    isa "Are you feeling okay, [da_r]? You look a little pale..."
    mc_s "What do you mean, sweetheart? I'm fine."
    isa "It's just... you've been acting a bit off ever since we left Osaka. Are you sure you're alright?"
    mc_s "Oh, don't worry about it, little one. It's probably just side effects from the meds they gave me when I was discharged."
    mc_s "It's no big deal. It'll pass soon enough, I promise."

    show ep01_backhome05
    isa "It better. You really had me worried there, [da_r]."
    mc_s "I'm sorry for not being awake during the trip. You must have been so bored."
    isa "Awww... don't worry, [daddy_r]! I had my books to keep me company. I wasn't bored at all!"
    mc_s "You seem to really love those books..."
    isa "They've been my constant companions while you were away. They made me feel less alone."
    show ep01_backhome06
    isa "They remind me of [mo_r]..."
    mc_s "Huh...? Antonella?"
    isa "Yeah. Even though you never really talked about her, [gra_r] told me lots of stories..."
    mc_s "She did? Like what?"

    $ playAudio(isabella_theme, "music", 2, True, 2.5, 0)

    show ep01_backhome07
    isa "Oh, just a few things... She said [mo_r] was really nice, loved to read, and dressed way better than [au_r_low] Amber."
    mc_s "Yeah... your [gra_r] never did approve of Amber's fashion sense, I suppose."
    isa "Did [mo_r] and [au_r_low] Amber get along?"
    mc_s "Well, when your [mo_full_r_low] and I first started dating, Amber wasn't too thrilled about it... But after seeing how much Antonella meant to me, she came around in the end."
    isa "Really? Hmmm..."
    mc_s "So... What's with the sudden interest in all this?"
    isa "No reason... What about [mo_r]'s [fm_r_low]?"
    mc_s "To be honest, I never met her parents, and she didn't tell me much about them either."

    show ep01_backhome08
    isa "Isn't that kind of strange? Wouldn't she have mentioned them to you at least once?"
    mc_s "I'm not sure... She always avoided the topic whenever it came up."
    mc_t "Huh... I've never seen Isabella so curious about her [mo_full_r] before."
    mc_t "It's not like we've had many heart-to-hearts... I guess you could say I pretty much failed her as a [da_full_r_low]."
    mc_t "This whole conversation feels like uncharted territory for me."

    show ep01_backhome12 with vpunch
    isa "Maybe she was hiding something! Or maybe she had some super-secret power or ability!"
    mc_s "Yeah, sure! You do know those kinds of things don't exist in real life, right?"
    isa "Huh!! Well then, you're probably hiding your superpowers too, [da_r]!"
    mc_t "And there's the Isabella I know and love, haha..."

    show ep01_backhome11 with hpunch
    isa "Oh, I almost forgot to tell you!"
    isa "Since there wasn't any room for you in the main house - I share a room with Madison..."
    isa "The grandparents have their room too..."
    isa "And [au_r_low] Amber didn't want to be disturbed..."
    isa "So [gra_r] and I fixed up the guesthouse for you. I hope that's okay."
    mc_s "Of course, sweetheart. Thank you both for thinking of me."
    mc_t "They went through so much trouble for me... After everything I put them through. I don't deserve their kindness."

    show ep01_backhome13 with vpunch
    isa "And [da_r]... I wanted to apologize for not writing or visiting you in Osaka for so long. I'm really sorry..."
    mc_s "Hey, hey! What are you talking about? If anyone should be apologizing, it's me. I'm the one who lost touch with you. You have nothing to be sorry for, Isabella."
    mc_t "I'm the one who abandoned her... And yet she's the one apologizing to me?"
    isa "Really? But... why didn't you come visit us or call more often?"
    mc_s "Well..."

    show ep01_backhome14
    isa "Our house..."
    mc_s "Yes... Of course."
    mc_t "This... might be harder than I thought. I spent so many years avoiding this moment... And now that it's here... I'm not sure I'm ready..."
    mc_t "How can I face them after everything I've done? I don't know if I'm strong enough for this..."

    show ep01_backhome15
    isa "You know, [gra_r] never blamed you... for not wanting to come back home to see us."
    mc_s "What do you mean? Blame me for what?"
    isa "For staying away... for burying yourself in your work."
    mc_s "I-I never... My job just kept me really busy, that's all!"
    isa "I know that, [da_r]... [gra_r] knows it too, but... still."
    isa "But now you're a detective, right? You finally achieved your dream!"
    mc_t "That was never my dream..."
    mc_s "Yeah... that's right. That was always the plan."
    mc_s "I'm going to spend some quality time here with you and your [gra_full_r_low] until I'm fully recovered, and then I'll go back to work."
    isa "Back to Osaka??"
    mc_s "Tokyo... I'll be here with you."

    show ep01_backhome16 with hpunch
    isa "Wha--! Wait!! What?!"
    mc_s "Huh? Is something wrong?"
    isa "I just assumed you'd go back to Osaka once you were better! What about your job there?"
    mc_s "It's over. After I got shot... I wasn't deemed fit for fieldwork anymore. They sent me a notice: I was being transferred to another department, more suitable for my current condition."
    mc_s "I wasn't thrilled about it at first, but I understood their reasoning and accepted it without a fight. This will be good for us... I think."

    show ep01_backhome18
    isa "So... does this mean I've got my [daddy_r_low] back? For real this time?"
    mc_s "Yeah! You bet, sweetie."
    isa "All... to myself?"
    mc_s "I can't promise you 24/7, but yes. You've got me all to yourself while we're here together. All the time. So you'd better make the most of it!"
    isa "Yaaay!"
    show ep01_backhome17
    isa "I missed you so much, [daddy_r]... Welcome home..."
    mc_s "I'm glad to be here too, babygirl."
    isa "[da_r]... can I curl up in your lap and sleep for a bit? Like I used to when I was little?"
    mc_s "Of course you can... You'll always be my little girl, no matter how big you get..."

    show ep01_backhome09 with slowfade
    isa "Thank you, [da_r]... Thank you for coming home..."
    mc_s "I love you, Isabella. More than anything."
    mc_t "I wasn't glad to be back... I lied... And I hate myself for feeling that way."
    mc_t "My little girl needed me, and I wasn't there for her... What kind of [da_full_r_low] abandons his own [dau_r_low]?"
    mc_t "I'm a pathetic excuse for a man who abandoned his own [fm_r_low]... Why would I ever want to come back to this place? This wasn't my home anymore..."

    show ep01_backhome10
    mc_t "Not only was I a shitty [da_full_r_low], but I purposely hid the truth about her [mo_full_r_low] from her... Not just now, but every time she asked... Do I really have so little faith in my own child?"
    mc_t "The story I told Isabella... It wasn't like that at all."
    mc_t "Whenever I brought up Antonella's parents, Antonella looked at me like I had just stabbed her in the heart. After getting that reaction a few times, I stopped asking altogether..."
    mc_t "Later, after she disappeared, I tried to investigate her past on my own, to understand why the mere mention of her [fm_r_low] caused her so much pain."
    mc_t "But I found nothing. It was like she had been wiped from existence before anyone realized she was gone."

    show ep01_backhome19 with slowfade
    mc_t "I became a cop to find Antonella, but in the end, all I found was a void of emptiness and self-loathing..."
    mc_t "And along the way, I lost sight of who I was and turned into this hollow shell of a man, filled with nothing but hatred... Hatred that I took out on everyone around me..."
    mc_t "But sometimes life gives you second chances. Sometimes it takes them away, sometimes it doesn't. This time, it decided to give me another shot."
    mc_t "Which is why... now that we've finally made it back home, Isabella... This time, I'm going to do better. No matter what happens. For your sake and mine..."

    $ stopAllSubchannels(channel="amb", fadeout=1.5)
    $ stopAllSubchannels(channel="music", fadeout=1.5)
    scene eigengrau with dissolve
    $ playAudio(sfx_glitch, "sfx", 1, True, 2.5, 0)

    show eigengrau at animated_glitch
    pause 1
#THE BABY
    show ep01_backhome23 with slowfade
    show ep01_backhome23 at animated_glitch
    mc_s "[mo_r]... [da_r]..."
    mc_s "I can explain..."

    $ stopAudio(channel="sfx", subchannel=1, fadeout=1.5)
    $ playAudio(sfx_heartbeatfast, "sfx", 5, True, 2.5, 0)
    $ playAudio(mc_broken_theme, "music", 2, True, 2.5, 0)

    show ep01_backhome23
    mic "Get the fuck out."
    mc_s "What--!"
    eli "Darling!! Why are you being so cruel!! He's your [so_r_low]! He has his own child! A baby!! Where's the poor boy going to sleep?!"
    mic "He's made his fucking choice already, and this place ain't suitable for him anymore."
    eli "Then where the hell is he supposed to go?"
    mic "That's none of our damn business anymore..."
    show ep01_backhome29
    amb "Are you seriously gonna kick him out, just like that?!"
    mic "It's none of your fucking business, Amber! If he wanted to stay here, then he shouldn't have knocked up some bitch!"
    amb "But--"
    mic "Enough, Amber! Shut your damn mouth!"
    mc_s "Amber did nothing wrong, don't talk to her like that..."

    show ep01_backhome27
    mic "Who the fuck gave you permission to speak? You're a goddamn disgrace to this [fm_r_low]! How the hell could I have raised someone as despicable as you!?"
    mc_s "I... I'm sorry, I never meant to cause any trouble..."
    mic "Your mere existence is trouble!! To think that my [so_r_low] would grow up to be such a pathetic failure!!"
    mic "I should've beaten some sense into you when I had the chance! Maybe then you wouldn't have turned out to be such a worthless piece of shit!"
    show ep01_backhome24
    eli "Please, stop it Michael! That's enough!"
    mic "Don't you dare interfere with me, woman, or you'll find yourself out on the streets with him."
    show ep01_backhome25
    eli "But!-"
    mic "Did you know about this? About the whore?? The bastard child?! Why the fuck didn't you tell me before?!?"
    eli "Yes!! I mean... I had no idea about the baby..."
    mic "This is the result of your piss-poor parenting! This is why I told you to discipline him properly! But you let him run wild like a fucking animal!"
    eli ". . ."
    mc_t "My parents were at each other's throats. And it was all because of me... I was terrified. My [da_full_r_low] had always hated me, but this... this was different."
    mc_t "But the look of utter disappointment on my [mo_full_r_low]'s face... it cut me deeper than anything else. Seeing her eyes filled with such sorrow shattered something inside me..."

    show ep01_backhome28
    mc_t "And while they continued their vicious argument, my [si_full_r_low] and I locked eyes. Her gaze held something different than the others... It looked... agonized."
    mc_t "But even with all her love and sympathy for me, she stayed silent... perhaps because she too, realized how things would end for us if she dared to speak out again..."
    mc_t "I couldn't blame her for her silence. In this [fm_r_low], defiance only led to more pain. We had both learned that lesson the hard way."

    show ep01_backhome26
    mc_t "And then, suddenly, Amber, catching my gaze, moved closer to me. Her eyes bore into mine as if she desperately needed to tell me something... Something meant only for my ears..."
    amb "What the fuck did you do, [mc_name]...!? What the hell were you thinking!?"
    mc_s "I... I don't know, Amber. I'm sorry. I'm so fucking sorry..."

    $ stopAllAudio(3.0)
    $ resetAllVolumes()
    scene eigengrau with rose
    pause 2
#-- End Episode 1
    jump ep02_title


