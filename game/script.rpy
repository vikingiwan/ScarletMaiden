# You can place the script of your game in this file.
init:
    ###Characters:
    
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

                    
                    

###IMAGES

#Colors:
image black = "#000000"
image white = "#FFFFFF"

##Characters:
image ak_vhappy = "res/characters/Akane/Akane_VeryHappy.png"
image ak_surprised = "res/characters/Akane/Akane_Surprised.png"

##Backgrounds
image bg_cherryblossomdojo = "res/bg/cherryblossomdojo.jpg"
image bg_akanebedroom = "res/bg/akanebedroom.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
#define ak = Character('Akane', color="#a6a6a6")

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
   scene black with Dissolve (3)
   stop music fadeout 1
   pause (1)
   return
