# End game credits

label credits:
    $ _game_menu_screen = None
    $ credits_speed = 25 #scrolling speed in seconds
    scene black
    with dissolve

    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    $ _game_menu_screen = "save_screen"
    return

init python: # 
    credits = ('GUI and Graphics', 'Mugenjohncel'), ('Music', 'Kevin Macleod'), ('Programming', 'Leon Zavšek\nImperf3kt')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
    image cred = Text(credits_s, text_align=0.5, drop_shadow = (4, 4), drop_shadow_color = "#000000")
    image thanks = Text("{size=80}Thank You!", text_align=0.5, drop_shadow = (4, 4), drop_shadow_color = "#000000")
    
    
    #$ credits_speed = 25
    
    #scene black #replace with background#
    #with dissolve
    
    #show theend:
        #yanchor 0.5 ypos 0.5
        #xanchor 0.5 xpos 0.5
    #with dissolve
    #with Pause(3)
    #hide theend
    
    #show cred at Move((0.5,5.0),(0.5,0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    #with Pause(credits_speed)
    #show thanks:
        #yanchor 0.5 ypos 0.5
        #xanchor 0.5 xpos 0.5
    #with dissolve
    #with Pause(3)
    #hide thanks
    #return
    
    #init python:
        #credits = ('Backgrounds', 'IDK'), ('Sprites', 'Sophia'), ('Writing', 'Sophia'), ('Original Novel', 'John Steinbeck'), ('Programming', 'Sophia'), ('Music', 'Music from Jukedeck - create your own at http://jukedeck.com')
        #credits_s = "{size=80}Credits\n\n"
        #c1 = ''
        #for c in credits:
            #if not c1==c[0]:
                #credits_s += "\n{size=40}" + c[0] + "\n"
            #credits_s += "{size=60}" + c[1] + "\n"
            #c1=c[0]
            #credits_s += "\n{size=40}Engine\n{size60}" + renpy.version()
            
    #init:
        #image cred = Text(credits_s, text_align=0.5)
        #image theend = Text("{size=80}Adam End", text_align=0.5)
        #image thanks = Text("{size=80}Thanks for playing!", text_align=0.5)