#Second choice is Charles
label charlesMorning2:
    
    "Cathy decides to spend time with Charles today."
    "She finds him in the yard, deep in thought."
    
    stop music
    
    show cNorm
    
    c "What's wrong, Charles?"
    c "Or do you hate me too much to answer?"
    
    hide cNorm
    show cAng
    "Charles glares at her slightly, but soon looks away and doesn't seem as hostile."
    
    play music "/audio/CloisteredSpace.mp3" fadein 1 fadeout 2
    
    hide cAng
    show cNorm
    ch "I've been thinking about my father."
    
    c "Your father? What about him?"
    
    ch "I’ve spent my entire life trying to live up to him and make him proud of me, but he’s always loved Adam more than me."
    ch "Adam never even had to try, and our father just automatically decided that he’d be the favorite son."
    hide cNorm
    show cAng
    ch "I had tried so hard to make him give me a chance, but he died hating me...even though I was the one always by his side. Adam just left him. I’ll never understand why."
    
    "Cathy is silent for a minute"
    
    hide cAng
    show cSur
    c "...I try really hard, and people just end up not liking me for me."
    c "They like a version of me that I put up as a front, and as a result no one has ever actually liked the real me."
    hide cSur
    show cNormB
    c "I guess it’s for the best. It’s what my goal is, after all. No one can know the real me."
    c "Adam adores the person he thinks I am, and I doubt he’d change his mind if he started to get to know me for real."
    c "He’d be too blinded by the virtuous person he thinks I am. It’s laughable, really."
    
    "Cathy pauses and begins to suddenly chuckle."
    
    c "I guess we really are pretty similar, huh? No one likes who we really are."
    
    stop music
    
    hide cNormB
    show cHappB
    "Charles smiles softly in return."
    
    ch "Yeah...I guess you're right about that."
    
    hide cHappB
    
    jump month3
    
    return