#All Adam ending
label adamEnding:
    
    $ adamEnd = True
    
    c "{i}Suddenly, it seems so clear to me.{/i}"
    c "{i}How can I not love this man?{/i}"
    c "{i}He's shown concern for my well being since before I even knew him.{/i}"
    c "{i}He's one of the only genuinely kind men I've met...{/i}"
    c "{i}...is what I'd like to say.{/i}"
    c "{i}But how can I ever consider being in love with someone when they don't know who I really am?{/i}"
    c "Of course I love you, Adam."
    
    play music "/audio/StepneyDesire.mp3" fadein 1 fadeout 2
    
    hide aCon
    show aSurB
    "Cathy held his hands in hers, smiling shyly up at her fiancee who's face was ecstatic."
    
    a "Thank goodness. I'm not sure how well I'd fare without you in my life, Cathy."
    a "You're everything to me, you know?"
    a "I never thought that I'd ever be so taken with a woman."
    
    hide aSurB
    show aNormB
    c "And I never thought I'd fall in love!"
    c "Adam, I'm so sorry about how difficult I've been acting lately."
    c "I really haven't given you enough thanks for everything you've done for me."
    
    a "Cathy, you haven't been difficult. You just needed space to figure things out, I understand."
    a "Spending time with my brother often was sort of an escape for you, I think."
    a "We all need that sometimes, and I understand."
    a "I'm just happy we're now on the same page."
    
    "Adam pulls Cathy into his arms, and strokes her head softly, whispering something Cathy could barely manage to hear."
    
    a "I'm so glad I've finally chosen my own path in life..."
    
    c "Adam? What did you say?"
    
    hide aNormB
    show aSurB
    a "Nothing, darling. Nothing at all."
    hide aSurB
    show aNormB
    
    "Adam pulls away from Cathy, kissing her forehead."
    
    a "Now, how about we go and plan a wedding?"
    
    c "Adam, that sounds lovely."
    
    stop music
    
    "Cathy forces another smile, and dreads what the future has in store."
    
    hide aNormB
    
    call credits
    
    #END
    
    return
