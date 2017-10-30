#Didn't stick to one character
label badEnding:
    
    "...Cathy tries to say what she wants to, but she can't."
    
    play music "/audio/CloisteredSpace.mp3" fadein 1 fadeout 2
    
    c "Adam...of course you're the only one for me."
    
    "She grimaces and feels frozen in place."
    "Why can't she say how she really feels?"
    "Why can't she tell Adam that she despises him and would rather drop dead than marry him?"
    "But Adam can't sense how she really feels."
    
    hide aCon
    show aNormB
    a "Thank goodness. I'm not sure how well I'd fare without you in my life, Cathy."
    a "You're everything to me, you know?"
    a "I never thought that I'd ever be so taken with a woman."
    
    c "And I never thought I'd fall in love!"
    c "Adam, I'm so sorry about how difficult I've been acting lately."
    c "I really haven't given you enough thanks for everything you've done for me."
    
    a "Cathy, you haven't been difficult. You just needed space to figure things out, I understand."
    a "Spending time with my brother often was sort of an escape for you, I think."
    a "We all need that sometimes, and I understand."
    a "I'm just happy we're now on the same page."
    
    "Adam pulls Cathy into his arms, and strokes her head softly, whispering something Cathy could barely manage to hear."
    
    a "I'm so glad I've finally chosen my own path in life..."
    
    hide aNormB
    show aSurB
    c "Adam? What did you say?"
    
    a "Nothing, darling. Nothing at all."
    
    hide aSurB
    show aNormB
    "Adam pulls away from Cathy, kissing her forehead."
    
    a "Now, how about we go and plan a wedding?"
    
    c "Adam, that sounds lovely."
    
    stop music
    
    "Cathy forces another smile, and dreads what the future has in store."
    
    hide aNormB
    
    window hide dissolve
    call credits from _call_credits
    call credits
    
    #END
    return