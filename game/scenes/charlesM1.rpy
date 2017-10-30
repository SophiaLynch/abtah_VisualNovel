#Spend the first morning with Charles
label charlesMorning1:
    "Cathy decides to spend her time with Charles today."
    
    c "{i}Might as well try and warm up to Charles. He's pretty distrustful of me, but for good reason.{/i}"
    
    "Cathy catches Charles right as he comes back from a hunt."
    
    stop music

    show cNorm
    ch "What do you want, whore?"
    
    c "I'm just going to let that one slide and pretend you greeted me like a civil person."
    c "Wait...were you just hunting?"
    c "You know you shouldn't kill innocent animals. That's just cruel."
    
    play music "/audio/TenuousThunder.mp3" fadein 1 fadeout 2
    
    hide cNorm
    show cAng
    
    ch "I could say the same about you."
    ch "The way you have my brother wrapped around your finger...now THAT's cruel."
    ch "Wouldn't you agree?"
    ch "At this rate, you could drive him to an early grave with how head over heels for you he is."
    ch "He'd do anything for you, and it's barely been a month."
    
    "Cathy smiles at Charles."
    
    c "You're not as thick headed as you look."
    
    hide cAng
    show cSurB
    
    c "Apparently, we have at least one thing in common."
    
    hide cSurB
    show cAngB
    
    ch "W-whatever. I've talked to you enough, woman. Now leave me alone."
    
    "Charles returns to his business, and Cathy feels somewhat satisfied."
    
    hide cAngB
    
    stop music
    
    jump month2
    
    return