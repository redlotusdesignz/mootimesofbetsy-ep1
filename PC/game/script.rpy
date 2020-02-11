# The script of the game goes in this file.

define d = Character("Wife")
define r = Character("Husband")
define s = Character("Saleswoman")
define c = Character("Customer")

define b = Character("Betsy", image ="betsy", window_left_padding=100)

image side betsy = "side_betsy.PNG"
image side betsy mad = "side_betsy_mad.PNG"
image side betsy awe = "side_betsy_awe.PNG"
image side betsy confused = "side_betsy_confused.PNG"
image side betsy cry = "side_betsy_cry.PNG"
image side betsy gloat = "side_betsy_gloat.PNG"
image side betsy happy = "side_betsy_happy.PNG"
image side betsy love = "side_betsy_love.PNG"
image side betsy scared = "side_betsy_scared.PNG"
image side betsy unamused = "side_betsy_unamused.PNG"
image side betsy sleep = "side_betsy_sleep.PNG"

image splash = "images/splashscreen.png"

label splashscreen:
    show splash with fade
    pause
    scene black with fade

return


# The game starts here.
label start:

    # Start by playing some music.
    play music "music/Playful (Loop 1).wav"

    scene blue dots
    with fade

    b "August, 2010."

    b "It was the month I’ll never forget."

    b "Some plush animals don’t remember having an adoption date."

    b "For me, it was a day of freedom."

    scene betsytable
    with fade

    "For quite some time, I was living alone with my other plush animal counterparts."

    "The mall always had a lively feel, with some children singing and dancing around the escalators as
    they move their way to the toy stands."

    "Day in and out, the kids would stop by, admiring my plush animal friends.
    Some paid attention to me, but they never decided to take me home."

    scene blue dots
    with fade

    b "Many of them whom passed by said the same thing:"

    play sound "sound/ChildrenCrowd AR02_90_2.wav"

    show betsy unamused at truecenter

    "{i} What a funny looking cow.{/i}"
    "{i} She looks so...unordinary.{/i}"
    "{i} A cow? They’re only good for hamburgers. {/i}"

    hide betsy unamused

    b cry "Though I remained expressionless on the outside, I felt sad from those remarks."

    b mad "I have feelings! I know how to feel my emotions!"

    b mad "And they’re quite rude in making assumptions that plush animals don’t
    know what we’re talking about. Hmph!"

    stop sound

    scene betsyshelf2
    with fade

    "And so, I found myself being put in the corner by the sales person,
    only to be hidden from plain view."

    "While the others enjoyed the limelight of the viewers,
    I secretly envied my plush animal “friends” for being placed in new homes."

    "A part of me wished that they would be torn apart by some ruthless toddler or angry child
    for being given the wrong toy and either be placed in the garbage as part of their punishment."

    scene blue dots
    with fade

    b unamused "But then I thought to myself, {i} What if that were to happen to me?
    What if I was picked by a family who would do the same to me?{/i}"

    scene betsyshelf2
    with fade

    "And so, all hope in finding a good home was out of the question."

    "I was terribly convinced that I would sit in the corner,
    watching the folks pass by me like a blur while I stared at the consumer walls with a distance."

    scene blue dots
    with fade

    b "Going back to the date. August, 2010."

    b "I couldn’t remember what date it was exactly."

    b "I was lucky to find out the month and year when I overheard
    the sales person talking to a customer about her plush animal business."

    scene insidemall
    with fade

    show customer notalk at left
    show salesperson talking at right
    with dissolve

    s "I'm just so blessed to open up my business at a young age.
    Since early April, I managed to sell my animals without anyone's help!"

    show customer talk at left
    show salesperson notalk at right

    c "Great to hear! Got any plans for the upcoming holidays?"

    show customer notalk at left
    show salesperson talking at right

    s "Um...yeah. It's August, 2010...so, like, I got some time to spare until
    maybe around September when I'll do a bulk order on animals to sell for the customers
    at the mall."

    show customer talk at left

    c "Sounds awesome. Hope you have a successful year!"

    "The saleswoman chuckled and wished her well as the customer went pass by the stand."

    scene ceiling
    with fade

    b "I remember looking up at the glass ceiling (at least not to make it obvious from the bystanders;
    they would be freaked out in seeing a plush cow moving her head on her own). "

    scene clouds
    with dissolve

    b "I remember seeing the blue sky with some clouds rolling by."
    b "Peaceful, tranquil and just perfect."
    b cry "But my heart wasn’t. "

    play sound "sound/HumanCry 6032_09_2.wav"

    b confused "It didn’t help that my ears were shocked by a crazy woman screeching (or was it wailing?)
    in the near corner."

    scene insidemall
    with fade

    show wife crying open mouth at left
    show husband lowereye no talk neutral at right
    with dissolve

    stop sound

    d "Dearie, I’m so sad. I really miss her."

    show husband lowereye speaking neutral

    r "It’s okay, honey. She’ll always be a part of us."

    hide wife crying open mouth
    hide husband lowereye speaking neutral
    with dissolve

    "I noticed the young couple walking towards the stand."

    "From what I’m assuming, the woman with tears was holding a picture in her hand."

    "The man held her other hand as they took a stroll through the mall. "

    "They briefly stopped to see the current layout of the stores when the man suggested:"

    show husband lowereye speaking neutral at right
    show wife crying closed mouth at left
    with dissolve

    r "Look, honey, why don’t we take a look at the plush animal stand?"

    "She sniffed and held onto him."

    show wife crying open mouth mouth at left
    show husband lowereye no talk neutral at right

    d "Ok..."

    "As they came closer to the stand, the sales person was doing the same song and dance to every other customer -"

    show salesperson talking at truecenter
    with dissolve

    s "Pick whichever you like that is the cutest!"

    show salesperson notalk at truecenter
    show wife crying closed mouth at left

    "I don’t know why, but I felt sorry for the crying woman."

    "She looked like she was in pain. Wish there was a way I can get her attention."



    menu:

        "What should I do?"

        "Push the stuff animals on the floor to get noticed.":

            jump push

        "Sit still and hope she sees the forgotten corner.":

            jump wait


label push:

    scene betsyshelf3
    with dissolve

    play music "music/SafeAndWarm_98_Loop_JHungerX.wav"

    "I took a leap of chance and decided to push the stuff animals in hopes she’ll notice me."

    play sound "sound/Crash 6010_95_2.wav"

    "I shifted my weight and eventually, the stuff animals fell down to the floor."

    "The sales person saw it and quickly apologised to the man and woman."

    stop sound

    "As I saw the sales person picking up the plush animals (with me laughing in joy on the slight revenge of my counterparts),
    I met face to face with my soon-to-be owner."

    show wife talking raised brow at left
    with dissolve


    d "HONEY, LOOK AT THIS COW! She reminds me of my late cat that passed! LOOK! LOOK COME HERE DEARIE!"

    "Now I see why she was crying."

    "She holds the photograph right next to my face and the resemblance was uncanny:"

    show moo moo at truecenter
    with dissolve

    "Large black patch on the right side of the eye with a wide smile that can make anyone heart’s melt. "

    "The man followed right behind her. With wide eyes, he exclaimed:"

    show husband smiling talk at right
    with dissolve

    r "Honey, she looks exactly like her. What a coincidence!"

    "Immediately, the woman grabbed me out of my spot."

    scene betsyhug
    with dissolve

    "I felt a surge of warmth as she held me in her arms."

    "A soft, peach scent filled my embroidered nostrils."

    "And yes, us plush animals do smell things. We’re just good at keeping quiet."

    scene insidemall
    with fade

    "The man asked the sales person:"

    show husband smiling talk at right
    with dissolve

    r "How much for the cow plushie?"

    "In the midst of putting the stuffed animals away, she sighed and said:"

    show husband lowereye no talk neutral at right
    show salesperson lowereye talk at truecenter
    with dissolve

    s "That cow isn’t popular on my stand. But if you want her, it’ll be $35."

    "The woman glared at the sales person."

    show salesperson sneering no talk at truecenter
    show wife upset open mouth at left with hpunch


    d "Not popular? Don’t you know that cows are precious! Here - I’ll give you $35.
    And a dust cloth. I don’t know how you take care of them, but this cow is too sweet to be dirtied up."

    b happy "Something tells me my new owner lived a colourful life."

    b scared "Also...not the type of person that you want to get on her bad side."

    b happy "Still, I love her sass. That stupid sales woman got what she deserved. "

    "After the sales person handed my new owner a receipt,the man nervously smiled at her."

    show husband lowereye speaking neutral at right
    show wife lowereye upset closed mouth at left

    r "I’m so sorry ma’am...my wife is still grieving over the loss of her cat after she passed away from cancer."
    r "Her cat was her companion since she was six years old and it’s been a rough time for all of us."

    "The salesperson looked at the couple with no emotion."

    show husband lowereye no talk neutral at right
    show salesperson sneering talking at truecenter

    s "Sorry to hear. Thanks for purchasing the cow. Hope it’ll provide comfort during her grieving time."

    b mad "What a heartless sales woman. If only I could punch her in the - "

    show husband smiling talk at right

    r "All right honey, let’s go take your cow back to the car and take her home with us."


    scene blue dots
    with fade

    b awe "Home. "

    b awe "I finally have a home to go to. "

    scene mall
    with fade

    "As they carried me to the car, I found myself waving goodbye to the mall."

    "I didn’t have any other elaborate words other than whispering the following to the mean sales person."

    show betsy gloat at truecenter

    "So long, lady! I hope you rot in plushie animal hell!"

    "Just then, my owner stopped in the middle of the parking lot."
    "She looks at me with bewildered eyes."

    stop music fadeout 1.0
    play sound "sound/record-scratch.mp3"

    show wife talking raised brow at left with hpunch

    d "YOU CAN TALK?!!"

    show betsy scared at truecenter

    "Oh dear. Looks like there’s no turning back. "

    scene black
    with fade

    "{b}Good Ending{/b}."

    stop sound

    return

label wait:

    scene betsyshelf2
    with dissolve

    play music "music/Sad Feelings (30-sec Version).mp3"

    "Fearing that I’ll cause too much attention to myself, I silently prayed that she’ll look my way."

    "I saw the steps pacing around the stand and held out hope that she’ll see me in the dark corner."

    "There was a bunch of chattering, some oohs and aahs from the couple, laughter and finally the words I didn’t want to hear:"

    show wife crying open mouth mouth at left
    show husband lowereye no talk neutral at right
    with dissolve

    d "Dearie...I know you tried but I’m tired. Let’s go home."

    "I felt myself deflate after realising that my one chance to go didn’t work out."

    hide wife crying open mouth
    hide husband lowereye no talk neutral
    with dissolve

    "As I hear the sales woman said her goodbye to the couple, all I’ve felt was numbness."

    "Any chance of hope left out the door. "

    scene mall
    with fade

    b "Later in the evening, the sales woman packed us away in her van after the day was over."
    b "Before she placed me with the rest of them, she looked at me squarely and said:"

    show salesperson lowereye talk at truecenter
    with dissolve

    s "You know, maybe I’ll keep you to myself."
    s "It’s a shame no one wanted you."
    s "Ah well, some plush animals don’t have all the luck."

    scene black
    with fade

    play sound "sound/truck-door-close.mp3"


    "As she shut the heavy van doors behind us, there was total darkness."

    stop sound

    show betsy sleep at truecenter
    with dissolve

    "I can hear the plush animals talking amongst themselves while I sat by myself in the corner of the van."

    play sound "sound/CartoonLaugh_DIGIJ04-41-02.wav"

    "{i}“Sucks to be that cow.”{/i}"

    "{i}“No one wants a smelly cow.”{/i}"

    hide betsy sleep

    b sleep "Perhaps this is my freedom."
    b unamused "I realised that I shouldn’t rely on others to find me a home."
    b unamused "So long as the saleswoman keeps her promise, it’ll make due."
    b sleep "Even if the other plush animals didn’t like me."

    "{b}Bad Ending{/b}."

    stop sound

    return
