#All Charles ending
label charlesEnding:
    
    $ charlesEnd = True
    
    hide aCon
    show aSad
    c "I'm sorry, Adam."
    
    hide aSad
    show aCon
    "Adam awkwardly smiles"
    
    a "I figured. It seemed too good to be true, you know?"
    a "And to be honest, you seem to genuinely enjoy being around Charles more than being with me."
    a "I get it. This is probably for the best."
    a "I've wanted to leave this place for a long time, maybe move somewhere sunny? Like California."
    hide aCon
    show aSad
    a "Now is the perfect opportunity."
    
    c "Adam, you're an amazing per-"
    
    a "Say no more. I'll take my leave."
    
    hide aSad
    
    "Adam exits the room, leaving Cathy in shock."
    
    c "Wait...Charles?"
    c "Was he implying that I...?"
    
    "And then it all made sense."
    
    play music "/audio/PanoramicCourage.mp3" fadein 1 fadeout 2
    
    "Cathy rushes out of the house, searching desperately for Charles."
    
    c "Charles! CHARLES!"
    
    show cAngB
    ch "Jesus, pipe down."
    ch "What's so important that you have to go screaming about it for the whole world to hear?"
    
    "Cathy's face lights up as she embraces him and plants her lips on his."
    hide cAngB
    show cSurB
    "Charles' eyes widen in surprise as all he can do it simply gape once she removes herself."
    
    ch "W-What was that about??"
    ch "You're engaged to my brother! You can't just kiss me in public!"
    
    c "Charles, we're not engaged anymore! Adam called off the wedding!"
    
    ch "Oh? {i}Oh.{/i}"
    hide cSurB
    show cNormB
    ch "So, the first thing you did when he called it off...was come and kiss me?"
    
    c "I thought about what you said, and I realized that you're right."
    c "I was hiding my own feelings from myself. Charles, I've always loved you."
    c "Well...loved and hated. It’s complicated, but at least it’s not entire hatred, right?"
    hide cNormB
    show cSurB
    c "You're the one I have fun being around. "
    c "You're the one who didn't fall for me without getting to know me first."
    c "Although I guess it's a little presumptuous that you'd fall for me at all, I really just wanted to be honest for once and that's enough for me."
    
    hide cSurB
    show cHappB
    "Charles grips Cathy's shoulders and kisses her like she had done to him before."
    "They pull away after a minute."
    
    c "I take it you feel the same way?"
    
    ch "Cathy, you have no idea."
    ch "You're stubborn and selfish. You're often a complete brat."
    ch "...but I can't stop thinking about you."
    ch "And let's be honest, I'm probably the only person who can put up with your personality."
    
    c "What?!"
    c "Don't be rude! Being honest was a big step for me, okay?"
    c "Let's just be nice to one another for one day. It's the least we can do."
    
    ch "I can manage that."
    
    stop music
    
    "Cathy and Charles grin at one another, both somehow unaware of the messy and chaotic future they'd have in store."
    
    hide cHappB
    
    call credits
    
    return