# characters

define c = Character("Cathy")
define who = Character("???")
define a = Character("Adam")
define ch = Character("Charles")

# answers for questions
$ q1 = None
$ q2 = None
$ q3 = None
$ adamEnd = False
$ charlesEnd = False

# images for adam
image aNorm = "adam_norm.png"
image aNormB = "adam_normB.png"
image aAng = "adam_anger.png"
image aAngB = "adam_angerB.png"
image aCon = "adam_concern.png"
image aConB = "adam_concernB.png"
image aEx = "adam_excite.png"
image aExB = "adam_exciteB.png"
image aSad = "adam_sad.png"
image aSadB = "adam_sadB.png"
image aSadd = "adam_sadder.png"
image aSur = "adam_surprise.png"
image aSurB = "adam_surpriseB.png"

# images for charles
image cNorm = "charles_norm.png"
image cNormB = "charles_normB.png"
image cAng = "charles_angry.png"
image cAngB = "charles_angryB.png"
image cHapp = "charles_happy.png"
image cHappB = "charles_happyB.png"
image cSur = "charles_surprise.png"
image cSurB = "charles_surpriseB.png"

# background images
image bgGen = "intro.png"
image bgText = "textintro.png"
image bedrm = "bedroom.png"

# Start of the game

label start:
    
    stop music
    
    # Show background

    # Dialogue starts now
    
    scene bgText
    
    pause 10

    with Dissolve(.5)
            
    pause .5
    
    scene bgGen
    
    with Dissolve(.5)
            
    pause .5

    c "{i}Where am I?{/i}"
    c "{i}What happened to me?{/i}"
    c "{i}Oh, that's right. {/i}"
    c "{i}That man took me and beat me. I suppose it serves me right.{/i}"
    c "{i}For most of my life...I've always been an outcast. {/i}"
    c "{i}My parents hated me, and I ended up running away from my old life after they died.{/i}"
    c "{i}No one has even been there for me , so maybe a fresh start is good?{/i}"
    c "{i}The last thing I remember is being beaten by Mr. Edwards, the man I essentially sold myself to...{/i}"
    c "{i}He wasn't happy when I told him how I truly felt about him.{/i}"
    c "{i}But maybe I des-{/i}"
    
    who "Miss!"
    
    c "{i}Who's that? I don't recognize that voice...did someone find me?{/i}"
    c "{i}I'm not sure if taking in a girl like me is the best for anyone's wellbeing though.{/i}"
    
    who "Are you alright? Miss!"
    
    c "Mmm...who...who are you?"
    
    # play music
    play music "/audio/StepneyDesire.mp3" fadein 1 fadeout 2
    
    scene bedrm
    
    with Dissolve(.5)
            
    pause .5
    
    show aConB
    
    
    
    who "Oh, thank goodness!"
    who "I was so worried when we found you; there were bruises everywhere! You're terribly hurt."
    
    c "How long...how long have I been here?"
    
    hide aConB
    show aCon
    who "A few days. You suddenly started moving a little and making some noises, so I thought you'd wake up."
    hide aCon
    show aNorm
    who "And surely enough, you did!"
    
    hide aNorm
    show aNormB
    "The man's face grew more and more red, and Cathy could tell he was getting flustered just by being around her."
    
    c "Are you alright? You seem somewhat unwell yourself!"
    
    hide aNormB
    show aSurB
    c "{i}I might as well try to warm him up to me even more.{/i}"
    c "{i}It's already so clear that he's attracted to me, which isn't much of a surprise.{/i}"
    c "{i}He's probably had very little experience with women lately, if ever.{/i}"
    c "{i}I'll just do whatever I have to do to ensure I'll have a place to stay for a while longer.{/i}"
    
    who "Oh, I'm q-quite alright! I've just been so worried, you know?"
    hide aSurB
    show aNormB
    who "Seeing a b-beautiful woman so horribly hurt...it's enough to make any respectable man so upset!"
    
    "Cathy put on a sweet smile and giggled at the man's words."
    
    c "My, you're too kind! And may I perhaps learn the name of my sweet savior?"
    
    hide aNormB
    show aSur
    who "Right! Forgive me, I should have told you sooner!"
    hide aSur
    show aNorm
    a "It's Adam. Adam Trask. And...might I ask what your name is?"
    
    c "Cathy."
    
    hide aNorm
    show aNormB
    a "Cathy...what a fitting name for someone so striking."
    hide aNormB
    show aSurB
    a "Oh! Was that too out of line? Again, please forgive me!"
    a "I have a habit of sometimes saying my thoughts aloud."
    
    c "There's no need to be sorry, Adam."
    c "Hearing all of this is extremely heartwarming"
    
    hide aSurB
    show aNorm
    a "Well, in that case, I'm glad to have made you smile."
    
    c "{i}Just how easy is this guy? He's already eating out of the palm of my hand.{/i}"
    c "{i}Can't I have someone more difficult to manipulate? I like a challenge!{/i}"
    
    hide aNorm
    show aNorm at left
    show cAng at right
    
    stop music
    
    "The door suddenly burst open, and a tall, rougher looking man appeared."
     
    play music "/audio/CloisteredSpace.mp3" fadein 1 fadeout 2
     
    c "{i}Who's he? Is he glaring at me?{/i}"
    c "{i}He definitely looks a lot tougher than Adam.{/i}"
    
    who "You're awake? Good. Now you can leave. You don't need to stay here anymore."
    
    c "{i}Hmm...now HIM I could work with.{/i}"
    c "{i}At the very least, I could just have some fun.{/i}"
    
    hide aNorm
    show aAng at left
    a "Charles! Is that any way to speak to a woman?"
    
    ch "What does her being a woman have to do with the way I'm speaking to her?"
    ch "She doesn't live here, so she can leave."
    
    a "Charles, that's not fair to her. We have to let her stay here for at least a little while."
    
    c "Please, Adam. I've already intruded enough, haven't I? I'd hate to be in your way for any longer."
    c "It seems like no matter where I go, I'm always in someone's way..."
    
    hide aAng
    show aSadd at left
    a "Cathy, that's not true! Please don't say that!"
    a "You can stay here, and I'll make sure Charles doesn't say such ridiculous things anymore."
    
    ch "Fine. Do what you please."
    ch "I'm not being nice to her, though. I can already tell that she's just no good."
    
    hide cAng
    hide aSadd
    show aNorm
    "Charles turned around and slammed the door, leaving a stunned Adam and intrigued Cathy."
    "She had to stifle a pleased giggle and once again force her grimace."
    
    stop music
    play music "/audio/StepneyDesire.mp3" fadein 1 fadeout 2
    
    c "He doesn't like me...I get it. I'm truly a horrible person."
    
    hide aNorm
    show aSad
    a "Don't say that, please. You're wonderful."
    
    c "Thank you, Adam. I hope in time he may see me in a new light."
    c "I'm sure he's a very kind person!"
    c "{i}So...Charles can already see right through me.{/i}"
    c "{i}Interesting. Very interesting.{/i}"
    
    hide aSad
    show aNorm
    a "Cathy? Are you feeling well enough to get out of bed?"
    
    c "I think so! Why? What did you have in mind?"
    
    hide aNorm
    show aExB
    a "Well, I figured I may as well show you around the house and the farm a little bit."
    a "You'll be staying here for a while, after all!"
    
    c "That sounds fantastic, Adam."
    
    hide aExB
    
    stop music
    
    "Cathy had been slowly getting used to her new surroundings over the past month, but she still felt like she didn't know the two men well enough."
    "Adam clearly doted on her already, but Charles was tougher to get close to."
    
    c "It's the start of a new day! I wonder how I should spend my time today?"
    
    play music "/audio/PanoramicCourage.mp3" fadein 1 fadeout 2
    
    # FIRST CHOICE:
    menu:
        #Adam
        "Spend time with Adam.":
            $ q1 = "a"
            jump adamMorning1
            return
        
        "Spend time with Charles.":
            $ q1 = "c"
            jump charlesMorning1
            return
        
    
    # This ends the game.

    return
