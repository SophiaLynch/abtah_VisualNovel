#Make a choice for month 2
label month2:
    
    stop music
    play music "/audio/PanoramicCourage.mp3" fadein 1 fadeout 2
    
    "Another month had passed since Cathy's arrival at the Trask residence, and she was spending more and more time with the two men."
    
    c "Who should I be with today?"
    
    menu:
        "Spend time with Adam.":
            $ q2 = "a"
            jump adamMorning2
            return
        "Spend time with Charles.":
            $ q2 = "c"
            jump charlesMorning2
            return
    
    return