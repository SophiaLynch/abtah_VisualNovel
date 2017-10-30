#Spend the first choice with Adam
label adamMorning1:
    "Cathy decides to spend time with Adam today. Charles hasn't quite warmed up to her yet..."
    
    show aEx
    a "Cathy! Just the person I wanted to see!"
    hide aEx
    show aNorm
    a "Would you mind helping me in the garden? It's a lovely day."
    
    c "Of course!"
    
    "Cathy follows Adam to the garden, and he starts handing her some seeds."
    
    a "I was hoping to plant some new flowers today, but they may take a little while to grow."
    
    c "Do you like flowers, Adam?"
    
    a "I guess so."
    a "I think you could say I've always been the more sensitive and quiet one between me and Charles, so I found hobbies that suited my interests."
    hide aNorm
    show aCon
    
    stop music
    
    a "It also helps me take my mind off of bad memories."
    
    c "Bad memories? Like what?"
    c "{i}I doubt they can be as bad as my past.{/i}"
    c "{i}I can't imagine Adam having been assaulted by every man he's ever met.{/i}"
    c "{i}Or being forced to sell his body.{/i}"
    c "{i}Or having parents who restricted him from everything and who never believed him.{/i}"
    c "{i}Or being forced to burn the house those parents lived in...{/i}"
    
    hide aCon
    show aSad
    a "I was a soldier for a while."
    
    c "{i}Oh. I guess that sort of compares.{/i}"
    
    play music "/audio/StepneyDesire.mp3" fadein 1 fadeout 2
    
    a "I did some terrible things during the time that I served, but I'm glad to be done with it."
    a "I never even wanted to join in the first place, but my father was very enthusiastic about the idea."
    a "I try not to think about it."
    
    c "Oh, Adam. I'm so sorry for bringing it up."
    
    hide aSad
    show aSur
    a "No! Don't be sorry! You didn't bring it up at all, that was entirely my fault!"
    hide aSur
    show aSadB
    a "Cathy, you never have to apologize for anything. You're perfect. Don't worry about it."
    
    c "Thanks, Adam..."
    
    hide aSadB
    
    stop music
    
    jump month2
    
    return