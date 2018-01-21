import time, random
import sound
sound.set_volume(0.7)
input("Hit RETURN to Start a Lectio Divina Session")

time.sleep(3)

print('''

Step 1: Find a piece of scripture,
anywhere from 1 sentence to 1 paragraph. Ideally, one where Jesus is doing something.
''')

input('''

Hit RETURN when you've found one

''')

time.sleep(1)

print('''

Sit down and relax...

''')

time.sleep(2)

print('''

Let's begin by relaxing. Do a 4-7-8 breathing for a bit.

''')

time.sleep(70)

sound.play_effect('rpg:HandleCoins')



print('''

Part 1: Lectio (Reading)

Read the verse several times. Focus on one word or phrase intensely.
If anything jumps out to you, dwell on that.

''')

time.sleep(250)
sound.play_effect('rpg:HandleCoins')

print('''

Part 2: Meditatio (Meditation)

Put yourself into the scene. Does this scripture apply to you today?
Ask the Holy Spirit to interpret this to you.

''')
time.sleep(300)

print('''

Part 3: Oratio (Prayer)

Take all the thoughts, fears and ideas that have came up
and offer them to the Lord.

If there is a specific anxiety, offer it to the Lord.

If you are especially thankful, pray a prayer of thanksgiving.

''')

time.sleep(250)
sound.play_effect('rpg:BookFlip1')

print('''

Part 4: Contemplatio (Contemplation)

Sit in silence with God

''')

time.sleep(250)
sound.play_effect('rpg:BookFlip1')

print('''

Now go out and live for Christ

''')
time.sleep(2)
sound.play_effect('rpg:BookFlip1')


