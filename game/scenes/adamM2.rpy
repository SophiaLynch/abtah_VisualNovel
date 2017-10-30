#Spend the second choice with Adam
label adamMorning2:
    "Cathy decides to spend time with Adam today."
    
    show aCon
    a "Hello, Cathy."
    
    stop music
    
    "Adam seems slightly distraught about something."
    
    c "Adam, is something wrong? You don't seem well."
    
    a "Sorry, I don't mean to worry you. I've just been thinking more about my past since our talk."
    
    c "Are you comfortable sharing with me, Adam? I don't want to intrude."
    
    hide aCon
    show aSur
    a "Of course! You could never intrude, Cathy."
    hide aSur
    show aSad
    a "I just..."
    play music "/audio/StepneyDesire.mp3" fadein 1 fadeout 2
    a "I've just been thinking about my father a lot. He was a unique person, to say the last."
    a "He often encouraged me and Charles' to compete for his affection, and that's why things are often so tense between us two."
    a "Did you know that Charles was the one who wanted to go to the army, but our father wouldn't allow it?"
    
    c "Really?"
    
    hide aSad
    show aCon
    a "Yeah, it was really frustrating for Charles. The only thing he ever really wanted was for out father to be proud of him."
    a "We both had different mothers actually, and even his own mom liked me more."
    a "I never really knew how to act about it since I looked up to her a lot, but Charles was unhappy."
    a "After our father told me to join the army, Charles started beating me. Hard."
    a "He always would hurt me a little bit every now and then, but he was furious after that."
    a "I nearly died, but he stopped right before I reached my limit."
    a "I think the disappointment of our father would have been worse for him than my death."
    hide aCon
    show aSad
    a "But I forgive him for that. He can't help it."
    a "Wouldn't you feel the same way if no one ever loved you?"
    
    stop music
    
    c "Right..."
    c "{i}I think I do understand...Maybe Charles and I aren't so different after all.{/i}"
    
    hide aSad
    
    jump month3
    
    return