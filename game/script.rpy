init:
##Characters:
    
    #Akane
    $ a = Character(_('Akane'),
                    color="#a6a6a6",
                    what_slow_cps=50,
                    #what_outlines=[ (1, "#a6a6a6") ],
                    ctc=anim.Blink("res/arrow.png"))
                    
    $ k = Character(_('Kurukato'),
                    color="#ff0000",
                    what_slow_cps=50,
                    ctc=anim.Blink("res/arrow.png"))
    $ mystery = Character(_('???'),
                    color="#FFFFFF",
                    what_slow_cps=50,
                    ctc=anim.Blink("res/arrow.png"))

##Character Images:
#Akane
image ak_vhappy = "res/characters/Akane/Akane_VeryHappy.png"
image ak_surprised = "res/characters/Akane/Akane_Surprised.png"
image ak_embarrassed = "res/characters/Akane/Akane_Embarrassed.png"
#Kurukato
image k_happy = "res/characters/Kurukato/Kurukato_happy.png"
image k_worried = "res/characters/Kurukato/Kurukato_worried.png"
image k_blush = "res/characters/Kurukato/Kurukato_blush.png"
image k_happy2 = "res/characters/Kurukato/Kurukato_happy2.png"
image k_serious = "res/characters/Kurukato/Kurukato_serious.png"
image k_sad = "res/characters/Kurukato/Kurukato_sad.png"
image k_surprised = "res/characters/Kurukato/Kurukato_surprised.png"

##Colors:
image black = "#000000"
image white = "#FFFFFF"

##Backgrounds
image bg_cherryblossomdojo = "res/bg/cherryblossomdojo.jpg"
image bg_akanebedroom = "res/bg/akanebedroom.png"

# The game starts here.
label start:

   stop music fadeout 1
   scene black
   centered "I......"
   centered "I....I love you"
   scene white with Dissolve(.5)
   pause (.5)
   play music "res/music/morning.ogg"
   scene black with Dissolve(.5)
   mystery "Akane..."
   mystery "Akane wake up, it's time for school"
   mystery "Hey, come on, get out of bed"
   scene bg_akanebedroom with Dissolve (1)
   show ak_surprised with Dissolve (.5)
   a "H-huh?"
   a "....."
   a ".........."
   a "K-Kurukato? Is that you?"
   scene bg_akanebedroom
   show k_happy with Dissolve (.5)
   k "Who else would it be?"
   stop music fadeout 1
   scene black with Dissolve (1)
   play music "res/music/lighthearted.ogg" fadein (.5)
   scene bg_cherryblossomdojo with Dissolve(1)
   show k_worried with Dissolve (.5)
   k "I really hope we'll make it to school on time. You remember what happened last time we were late, don't you?"
   scene bg_cherryblossomdojo
   show ak_embarrassed
   a "Don't remind me..."
   jump endoftest

label endoftest:
   stop music fadeout 3
   scene black with Dissolve (3)
   centered "*END OF TEST*"
#   pause (1)
   return