# The structure
# -------------------------------------------------------------------
# chapters = [
#     {
#         "texts": ["question_1", "gameover_1a", "gameover_1b"],
#         "choices": ["answer_1", "wrong_1a", "wrong_1b"],
#     },
#     {
#         "texts": ["question_2", "gameover_2a", "gameover_2b"],
#         "choices": ["answer_2", "wrong_2a", "wrong_2b"],
#     },
# ]
# Note that texts and choices should correspond, first (0) is reserved for the correct answer


chapters = [
    {
        "texts": ["""
You find yourself waking up in this eerie abode, desperately seeking
an escape. As you wake up, the creaking floorboards beneath your feet
seem to whisper a question. Which floor will you explore first? Will you
venture upstairs to the mysterious second floor or cautiously investigate
the ground floor below? Choose your fate wisely and type 'upstairs' or
'downstairs' to embark on your quirky escape adventure!
""", """
You ascend the stairs, your heart pounding with anticipation, only to be
greeted by the ominous darkness that envelops the upper floor. Your
imagination begins to play tricks on you as the shadows dance and whisper
eerie secrets. Suddenly, your heart skips a beat, and you clutch your
chest in terror. The darkness proves to be too much for your fragile
nerves, and you succumb to a sudden heart attack. Alas, your adventure
comes to an untimely end.

But fear not, brave adventurer! You can always start anew and make
different choices to conquer the challenges that lie ahead. Embrace the
mischievous spirit of the game and embark on another attempt to outwit
the perils of this peculiar house. Will you explore the ground floor
instead? The choice is yours to make!
"""],
        "choices": ["downstairs", "upstairs"],
    },
    {
        "texts": ["""
You step into the chilling kitchen, the stale air sending a shiver down
your spine. The flickering light casts eerie shadows across the room,
creating an atmosphere of uncertainty. As you survey your surroundings,
two intriguing points catch your attention. To your left is a rusted
refrigerator, emitting a low hum that reverberates through the room. To
your right is a creaking closet, beckoning you with an air of mystery.
It's time to make a decision.

Will you muster the courage to investigate the secrets concealed within
the kitchen, hoping to find a clue that leads you closer to your escape?
Or will your curiosity guide you towards the enigmatic closet, despite
the uncertainty of what lies within? Choose your path wisely and type
'fridge' or 'closet' to embark on the next chapter of this whimsical and
treacherous journey!
""", """
Curiosity gets the better of you, and you open the closet door, revealing
a chilling sight. A sight that stabs you with a knife that is, what else
did you expect?
"""],
        "choices": ["fridge", "closet"],
    },
    {
        "texts": ["""
As you open the rusty refrigerator door, a peculiar sight catches your
eye — a strange container nestled among the forgotten leftovers and
expired jars. Intrigued, you carefully reach inside and retrieve the
mysterious object. Its surface is adorned with intricate engravings,
radiating an aura of mystique. The weight of the container feels
significant in your hands, as if it holds secrets yet to be unveiled.

However, before you have a chance to examine its contents, a sudden,
spine-chilling, SPOOKY noise pierces the air, sending a shiver down your
spine. Panic grips your heart, urging you to find a means of escape.
With limited options, you scan the room for possible exits. The back
door and a window beckon, each offering a glimmer of hope amidst the
encroaching darkness. Although perhaps calming your nerves is a better
option?

Choose your path swiftly, adventurer. Will you make a daring dash through
the back door, risk a daring escape through the window, or just wait? The
decision is yours, and your destiny awaits. Type 'back door', 'window',
or 'wait' to determine your next move and discover the twists and turns
of this suspenseful adventure!
""", """
As you bolt towards the back door, desperation fueling your every step,
a horrifying realization dawns upon you. The once securely closed door
swings open with an eerie creak, revealing the sight you hoped to evade —
a headless lady, her ghastly figure standing ominously before you, the
knife glinting in the dim light. How she managed to escape the confines
of the closet remains a chilling mystery.

Before you can react, her spectral presence lunges towards you, a frenzy
of malevolence and otherworldly force. Your attempts to flee are futile
as the knife finds its mark, abruptly ending your valiant escape attempt.
Alas, your journey meets a grim and untimely demise at the hands of the
relentless headless lady.

Take solace in the knowledge that death is not the end of your adventure.
Rise again, intrepid explorer, and embark on a new path with newfound
wisdom. Will you find a way to conquer the perils of this enigmatic
house, or will you encounter a different fate in your next endeavor?
The choice is yours to make, for the haunting tale continues.
""", """
As you hastily make your way towards the window, a series of unfortunate
events unfolds in comical fashion. In your frenzied attempt to squeeze
through the narrow opening with a sizeble container, you misjudge your
own agility. With a clumsy misstep, you find yourself wedged halfway
through the window frame, arms flailing helplessly.

In this awkward and compromising position, the headless lady, having
escaped her previous confines, seizes the opportunity to strike. With an
almost comically precise swing of her knife, she nicks the back of your
pants, resulting in an embarrassing tear and what you imagine a
collective gasp from the onlooking spirits. Your valiant escape attempt
is thwarted by a wardrobe malfunction of the most unexpected kind.

While your intentions were noble, it seems that fate has conspired
against you in the most absurd manner. Alas, your journey reaches an
untimely end, leaving you stuck in the window, both physically and
metaphorically. Take solace in the knowledge that your comedic demise
won't be remembered by the crazy headless lady for years to come, as she
doesn't have a head to remember with.

Do not forget, even in defeat, the spirit of adventure persists. Reclaim
your resolve, brave soul, and forge ahead on a new path. Will you
discover the secret to overcoming the enigmatic house, or will you
encounter a different destiny in your subsequent attempts? The choice is
yours to make, as the haunting tale continues to unfold.
"""],
        "choices": ["wait", "back door", "window"],
    },
]


logo = """
                               *-*       %%
                         _______|________%%__
                        |%%%%%%%%%%%%%%%%%%%%%|
                   _____|%%%/^\%%%/^\%%%/^\%%%|_____
                  /%/^\%|%%%|-|%%%|-|%%%|-|%%%|%/^\%\ 
                 /%%|-|%|%%%%%%%%%%%%%%%%%%%%%|%|-|%%\ 
                /%%%%%%%%| __  __ ___ __  __ |%%%%%%%%\ 
                 |_|-|-|_||__||__|.|.|__||__||_|-|-|_| 
                 IIIIIIII|       |_|_|       |IIIIIIII 
                 ~^    ^"@@@@@@@@|   |@@@@@@@@"^    ^~
  ___________ _____  _____ _   ____   __  _   _ _____ _   _ _____ _____ 
 /  ___| ___ \  _  ||  _  | | / /\ \ / / | | | |  _  | | | /  ___|  ___|
'\ `--.| |_/ / | | || | | | |/ /  \ V /  | |_| | | | | | | \ `--.| |__  
  `--. \  __/| | | || | | |    \   \ /   |  _  | | | | | | |`--. \  __| 
 /\__/ / |   \ \_/ /\ \_/ / |\  \  | |   | | | \ \_/ / |_| /\__/ / |___ 
 \____/\_|    \___/  \___/\_| \_/  \_/   \_| |_/\___/ \___/\____/\____/ 
"""

welcome = """
Welcome to the Spooky House of misadventures! Beware, for this house holds
more surprises than meets the eye. There's one notable thing about it,
a crazy headless lady with a knife in a closet, but don't worry, she
appears to be stuck. However, your path to freedom might be hindered by
other sometimes mundane, yet perilous, challenges.
"""

win = """
As you bravely decide to wait, your heart pounding with a mixture of
apprehension and curiosity, the spooky noise that had unsettled you
earlier begins to subside. Gradually, the unsettling atmosphere
dissipates, and a newfound calm washes over you. You take a deep breath,
realizing that perhaps there is a rational explanation for the eerie
occurrences in this house.

With nerves steadied and a sense of determination, you make your way
towards the front door, which was open the whole time, eager to put this
harrowing ordeal behind you. As you step out into the fresh air, a wave
of relief washes over you. You reach for your phone and dial the
emergency number, alerting the authorities to the peculiar events you
have witnessed.

The police arrive swiftly, and with your detailed account, they spring
into action. The container you found in the fridge proves to be a crucial
piece of evidence, as it contains that lady's severed head! In a stroke
of medical marvel, her head is successfully reattached at a local
hospital, finally restoring her to a state of wholeness.

Your courageous actions have brought an end to the haunting and set in
motion a resolution for all involved. The town marvels at the bizarre but
ultimately heartwarming tale that unfolded within the walls of that
mysterious house.


            ^^                   @@@@@@@@@
       ^^       ^^            @@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@              ^^
                           @@@@@@@@@@@@@@@@@@@@
 ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
 ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
   ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
   ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
 ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
       ~             ~        ~      ~      ~~   ~             ~

With the ordeal behind you, you can finally breathe a sigh of relief. The
haunted house is no longer a place of dread, but rather a reminder of
your resilience and ability to conquer the unknown. As you walk away from
the house, a sense of triumph fills your heart, knowing that you have not
only escaped its clutches but also brought justice and restoration to the
headless lady.

Congratulations, valiant adventurer, on your triumphant escape and the
newfound peace you have brought to this peculiar town. May your future
endeavors be filled with less supernatural entanglements, but always
remember the courage you exhibited in the face of the unknown.
"""
