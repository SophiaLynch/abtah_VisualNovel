#Make a choice for month 3
label month3:
    
    "Days, weeks and finally just about another month had passed since Cathy's arrival at the Trask residence."
    "Adam and Cathy had spent lots of their time with one another, but Cathy was still quite taken with Charles' ambiguity and coldness."
    "This has become more evident to Adam."
    
    show cNorm
    
    ch "So."
    
    c "So?"
    
    hide cNorm
    show cAng
    
    ch "When are you finally going to leave?"
    
    c "Well, I doubt I'll ever leave; Adam proposed to me."
    
    hide cAng
    show cSur
    
    ch "He proposed to you?? And you said yes?!"
    
    c "Yes, Charles. I didn't expect it to come as a shock to you."
    c "You've seen us spending plenty of time together. It's only natural we'd get married."
    
    hide cSur
    show cAng
    
    ch "You don't love him."
    
    c "Maybe."
    
    ch "He adores you, for whatever reason."
    
    c "I suppose he does."
    
    hide cAng
    show cNorm
    
    ch "Look...I'm just going to ask you to not let him get hurt."
    ch "If you were to do something stupid, it'd really break him."
    
    c "We'll see what happens, Charles."
    c "{i}Do we need to talk about this anymore?{/i}"
    c "{i}I'd rather just argue with Charles about meaningless things like we usually do.{/i}"
    
    ch "Cathy, you know-"
    
    c "Wow! I think that's the first time I've ever heard you call me by my name."
    c "What an incredible day! We ought to celebrate."
    
    ch "Cathy, I need to say something. Please be serious."
    
    c "Alright, alright. Go ahead."
    
    ch "Cathy, you know I don't hate you, right?"
    ch "You've been through some rough situations, I can tell."
    ch "You've probably been surrounded by tons of assholes for most of your life."
    ch "I get it."
    ch "You don't trust people."
    ch "But I wish you'd be more honest. Not honest with me or Charles."
    ch "Hell, live a lie with Charles. Tell him you love him and act like you do, but hate him inside all you like."
    ch "Or don't! That's not the point, though."
    ch "I want you to be honest with yourself."
    
    c "With...myself?"
    c "{i}What does that even mean?{/i}"
    c "{i}Is he implying that I'm in love?{/i}"
    c "{i}That's ridiculous.{/i}"
    
    ch "Just think about it, Cathy."
    ch "Think about what's really important to you, and think about who you really are."
    
    play music "/audio/CloisteredSpace.mp3" fadein 1 fadeout 2
    
    c "Charles...I don't know how I feel."
    c "Everything is so confusing right now."
    
    hide cNorm
    show cSur
    
    "Cathy's vision starts to blur as she forces tears to roll down her cheeks."
    
    c "{i}Tears can make me seem more fragile, right?{/i}"
    c "{i}I'm sick of playing the sweet, innocent Cathy...but I need to keep up the facade for a little longer.{/i}"
    
    hide cSur
    show cSurB
    
    ch "Cathy, are you alright?!"
    
    "She places her head against his chest, and continues to softly cry."
    "Charles, confused, decides to put his arms around her in an attempt to comfort the girl"
    
    ch "Is this...is this okay?"
    
    c "Charles...I feel so much more comfortable in your arms."
    c "I can't stand keeping up this front to Adam when you're the only one who really sees me for me."
    
    "She looks up at him, and begins to move in closer."
    
    ch "C-Cathy? What are you doing??"
    
    "His face grows flushed as she closes in on him, lips pressed against one another."
    "He does nothing at first, but then hesitantly begins to kiss Cathy back."
    hide cSurB
    show cNormB
    
    "Eventually, his kisses grow passionate and the two spend the night together..."
    
    hide cNormB
    
    stop music
    
    "The next day, the air feels different and Charles is nowhere to be seen."
    "Cathy leaves the bedroom, and tries to find him but sees Adam instead."
    
    show aSurB
    
    a "Oh!"
    a "Cathy, dear! I'm so glad I ran into you!"
    
    hide aSurB
    show aCon
    
    a "There's actually something I've really been meaning to ask you about. Care to sit down for a moment?"
    
    c "Of course, Adam darling. Anything for my husband-to-be!"
    
    a "Yeah, actually...it's about the wedding."
    
    c "The wedding? Well, we {i}do{/i} need to discuss the formalities and all."
    
    a "No, it's not that."
    a "Cathy, do you actually love me?"
    
    c "{i}Oh{/i}"
    c "{i}I think I understand Charles now.{/i}"
    c "{i}I need to realize for myself how I actually feel about Adam.{/i}"
    c "{i}He's kindhearted, yes. Charming, handsome, and very sincere.{/i}"
    c "{i}But Adam being a near perfect man doesn't mean I love him, does it?{/i}"
    c "{i}How do I really feel about Adam?{/i}"
    
    menu:
        "Of course I do.":
            $ q3 = "a"
            if (q3 == "a" and q1 == "a" and q2 == "a"): #all Adam options
                jump adamEnding
                return
            else: #didn't do all Adam
                jump badEnding
                return
            return
        "I'm sorry":
            $ q3 = "c"
            if (q3 == "c" and q1 == "c" and q2 == "c"): #all Charles options
                jump charlesEnding
                return
            else: #didn't do all Charles
                jump badEnding
                return
            return
    
    return