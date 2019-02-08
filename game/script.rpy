define v = Character("Viola", image= "v")
define n = Character("Nora", image = "n")
define l = Character("Liam", image = "l")
define c = Character("Connor", image = "c")
define s = Character("Shouhei", image = "s")
define o = Character("Olly", image = "o")
define cl = Character("Clara", image = "cl")
define k = Character("Kinuko", image = "k")
define p = Character("Perrault", image = "p")
define pc = Character("Professor Corbet", image = "pc")
define lm = Character("Liam's mother")
define mystery = Character("???")
define audio.dooropen = "Door Squeak.mp3"
define audio.magiceffect = "shootingstar.mp3"

image side v normal = "v normal.jpg"
image side v happy = "v happy.jpg"
image l normal = "l normal.jpg"
image l happy = "l happy.jpg"
image n normal = "n normal.jpg"
image c normal = "c normal.jpg"

label start:
   scene bg 1 # university birds-eye view 
   
   "Wyderwold University.  The premier applied magic college in the United States. Members of my family have attended for generations, and I've wanted to come, following in my sister's footsteps, since before I can remember."

   "Rumor has it that the school is afflicted with a very peculiar curse: that if you run across it, and you're lucky, you'll be marked for greatness, destined for a life of wealth and plenty."

   "If you're unlucky..."

   "Well."

   "After what happened to my sister, to my whole family, I've wanted to come to this school even more."

   "So I can find the source of the curse, and end it. For good."
   
   scene bg hallway
   show l normal at left
   
   l "Hey Viola, where do you want this to go?" 
   
   v normal "That one's books--just put it on my desk for now, I'll unpack it later." 
   
   l happy "Oof, no wonder it was so heavy!" 
   
   "Well, here I am. After years of looking forward to this day, it's finally come: my first day of classes at Wyderwold University starts tomorrow." 
   
   "Which means that tonight is reserved for moving in." 
   
   "My parents dropped my stuff off at the entrance to the dorms, but they're too busy to stick around and help me move in properly, so we hugged at the entrance, they gave me the usual reminders to remember to make our family name proud, and left." 
   
   "Luckily for my back, on my second trip upstairs--because of course my dorm room is on the third floor--I ran into Liam, and he's been helping me move everything else up." 
   
   "Liam was one of my best friends when we were younger, but after...everything, my parents could no longer afford to retain his doctor mother's services, so he and his mothers had ended up having to move away." 
   
   "We'd kept in touch for a while, but we were also *twelve*; eventually we lost touch." 
   
   "Until a few weeks ago, when I'd received a message from him out of the blue, asking if I was still planning on attending Wyderwold, and mentioning that he'd managed to get in as well." 
   
   "(Back when we were younger, we'd all three planned to attend together. But then, well. That hadn't really worked out.)" 
   
   "We planned to both arrive at the same time, so we could help each other move in, but then my parents had a meeting that ran late, and there was a minor emergency of some sort, and--well, an on-time arrival just didn't happen." 
   
   l "I'm heading back downstairs for another load." 
   
   v happy "Thanks! Just--be careful if you grab the purple duffle bag, it's got some kinda fragile stuff inside." 
   
   l "Got it." 
   
   "Luckily, he doesn't seem to mind helping me out, even if I got here too late to return the favor. I should see if he'll let me buy him lunch sometime this week, as thanks."
   
   scene bg v dorm
   
   "It looks like I got here a lot later than my new roommate, too. Her side of the room is already set up: a computer on her desk with a large lamp looming over it; bed carefully made up with a comforter a lovely shade of light blue; wardrobe with one door left slightly ajar showing that it had been filled with clothes, and a stack of deconstructed cardboard boxes stacked up behind the trash cans." 
   
   "I'd be a bit worried that she'd think I was some sort of slob--I'm truly not, but I also don't always keep everything 100 percent straightened 100 percent of the time--except for the stack of small objects scattered over the rest of her desk, a few of which appeared to have spilled over onto her bed and the floor. A couple of them look like old smartphones, or pieces of them, but most of them I have no idea what they are, or what they're for." 
   
   "Liam and I are carrying my last two bags into the room when we almost bump into my new roommate." 
   
   show l normal at left
   show n normal at right
   
   v "Oh, sorry! We're almost done. I'm your new roommate--Viola Ashmark." 
   
   n "Nice to meet you, I'm Nora Galena." 
   
   "She steps out of the way to let us pass." 
   
   n "I was just about to run my boxes down to the recycling station--I'll be back upstairs in a few minutes." 
   
   v "Oh, good idea! I should probably finish unpacking first, though." 
   
   hide n
   scene bg hallway
   
   "The dorm administrators set up a station in the main hall of the dorms, where you can leave your boxes and they'll be dealt with appropriately. I'm sure if recycling is exactly the right word, given that I also heard that that was where you were supposed to go to get materials to pack up for the summer, and it seems like a waste if they're going to end up breaking the boxes down at the beginning of the year just to reconstitute them into...more boxes, at the end of the year. But I didn't bother to enquire too deeply into the process; as far as I'm concerned, the boxes will be out of my dorm room and not my problem anymore, which is all I need to know."
   
   scene bg v dorm
   
   "I've unpacked about half my clothes, and I'm taking a break to get Liam's help with making up my bed, when Nora returns." 
   
   show n normal at right
   
   n "And--your brother?" 

   "Liam and I look nothing alike, but I suppose it's not an unfair assumption to make--one of us could be adopted, after all." 
   
   show l normal at left

   v "Sorry, I should have introduced you earlier--this is Liam. We were friends when we were younger." 

   "Hopefully we still would be. We hadn't talked about much, yet, but if he wanted to pick up where we'd left off all those years ago, I'd be happy to do so too." 

   l happy "Nice to meet you." 

   n happy "Likewise." 

   l "I'll try not to invade your room in the future, it's just."
   
   v "I asked him to help."
   
   show l normal at left

   n normal "Moving in is pretty terrible, yeah. Even with my family helping, it took me most of the afternoon to get settled." 

   n "I don't mind if you drop by in the future--I'm sure you two will want to catch up, too. Just maybe let me know in advance? Just in case I'm not in a fit state for visitors."
   
   l "Of course. That's only polite." 

   l "Speaking of, I should probably be going." 

   v "Oh right--I probably interrupted your unpacking process, too, didn't I? Sure, go ahead--I'll see you in Magical Fields in the morning?" 

   "I hesitate. Back when we were kids, we'd usually hug each other before we went back home." 

   "But we're not kids anymore, a fact that is blatantly obvious just looking at Liam. He must be nearly a foot taller than me by now, and are those actual muscles? It's a far cry from the scrawny kid I remember."
   
   "I'm not complaining, but it's a lot to take in. And maybe he's beyond kid stuff now."

   "But before I can make up my mind for sure, the moment passes." 

   l happy "See you in the morning!" 

   hide l

   "He leaves, and I turn back to my side of the room. I've still got so much left to unpack." 

   "But at least I'm here now."

   scene bg 2 # Nora and Viola's dorm room

# I kinda wanna put a fade in here. 

   show n normal

   n "Viola, are you about ready? It's almost time for Magical Fields to start."

   v "Yes, I'll be right there!"
   
   "Turns out we have two classes together--Magical Fields and Summoning 101. It'll be nice to know someone other than Liam in a few of my classes."

   v "Let's go! This is your first time on campus, right? Let's go by way of the gardens, I'll show you the way."

   n "As long as it doesn't make us late-–"
 
   scene bg 3 # Classroom 
   show n normal

   v "–-And the first rose bush was originally donated by one of my ancestors, though it's at the center of the garden, so we didn't see it this time."
  
   n "Wow, that's, what--several hundred years ago?  And it still blooms?"

   #v "Magic."
   
   #n happy "Fair point." [I feel like this banter fits a little less in a world where magic is normal.]
   
   v "Miranda Ashmark wasn't big on entropy."

   show l normal at right
   show n normal at left 
 
   l "Viola! Long time no see." 

   v "Oh yes, a whole 15 hours. Come on, come sit with us."
   
   "Liam's with someone I don't recognize. Another classmate, maybe?"

   l "Oh, and this is my roommate, Connor."
   
   show l normal at center
   show c normal at right

   c "Nice to meet you, Viola, Nora."

   v "Watch out--Liam bites."

   l "That was one time! We were five!"

   show n laughing at left
   show c laughing at right
                                                                                                            
   c "I'll keep an eye out."  
   
   v "Oh, right--and this is my familiar, Oleander." 

   "I pull out my phone--Olly can manifest through my pocket too, but it's only polite to show your phone when introducing familiars. He appears with a bit of a twirl, spreading his wings wide and puffing his chest out proudly." 
   
   "He's about twice the size of the phone, which is pretty common for dragon familiars, and his coloration--a darkish green with gold accents--is still one of my favorite things about his appearance." 

   show o normal #We'll have to define new locations to show four characters at once. Right now he's overwritten Liam.

   o "Nice to meet you! Please call me Olly." 
   
   "Liam and Nora pull their phones out, too. Liam's is an older model, though clearly well cared for, and Nora's looks brand new." 
   
   l "This is Clara." 
   
   show cl normal #For this scene I think we can swap out the familiar sprites, so we don't end up with seven people on screen, which is a little crowded.
   
   cl "Olly! Good to see you again." 
   
   "Clara is a jackalope familiar. A rabbit with sleek brown fur and bright eyes, outwardly no different from other rabbits, except for one tiny detail. I feel a twinge of something sharp, maybe something sad--it's been so long since I had last seen her, and Liam."

   o "Likewise! Your antlers look great--have they grown?" 

   show cl preening

   cl "They sure have!"

   n "And this is Perrault." 

   show p normal

   p "Greetings, all. It is a pleasure to meet you." 

   "Perrault seems pretty laid back; he manifests in a sitting position and doesn't bother to either stand or open his wings. I hope this is a good sign that he and Nora will make good roommates. I really like Clara, but even if co-ed dorm rooms were allowed, I don't think I'd want to live with her."

   "Though who knows, maybe she's calmed down in the past few years."
   
   "We all turn to Connor, but before he has a chance to introduce his familiar, the professor comes in, and we all hastily sit down."
   
   pc "Welcome to Foundations 105: Magical Fields. I'm Professor Corbet." 
   
   pc "And as this likely the first class for many of you, I would like to formally welcome you to Wyderwold University as well."
   
   "Nora leans over from her desk, about to say something when--"

   play sound dooropen 

   mystery "Sorry for being late, Professor."

   scene bg #CG scene: Viola and Liam staring at the person standing in front of the door, nora and connor confused in background

   v "That person is--" #I'm sure there's a way to show a character's name without showing their sprite, but actually, what do you guys think about showing sprites at Viola's location during CGs? It's especially useful for if the CGs don't show everyone's faces. We'd just have to make and define new side images.

   pc "Shouhei Utsurikawa, was it? How nice of you to join us. Take a seat anywhere you like."

   "The chatter in the room starts up again, but I can barely hear it. His eyes skim the room before they stop to look at--me? Liam? Both?"
   
   "He doesn’t meet my glance, though. His eyes flicker away, and he takes a seat on the opposite side of the room. Without another word, he takes out his books and faces forward, away from us."
   
   scene bg 3 # Classroom
   show n normal at left

   n "You know that guy?" 

   "Before I can answer, suddenly--"
   
   hide n
   
   play sound magiceffect

   show k

   "A crane appears, gracefully gliding through an open window to rest by Shouhei’s desk. A physical familiar. The whispers around me get louder. Physical familiars are not unknown, but rarer now than they once were."
   
   hide k
   show pc normal
   
   #pc "All right, class, it’s nice you’re all becoming such good friends, but we have things to learn, and we don’t have all day to do it in. Everyone back to their desks, please."

   #"Nora’s desk isn’t too far away from mine. Unfortunately, Liam’s halfway across the room, and Connor’s off in the opposite corner. Shouhei is in the middle of the room." [Is there a reason they're all separated?]
   
   pc "As I was saying..."
   
   "I should pay attention to Corbet, but I'm still stuck on Shouhei. Neither I nor Liam have spoken to him since...it was a while ago. I shake off the thought. I can talk with Liam about this later. I turn to the board and Corbet begins their lesson."

   pc "Summoning. Enchantment. Botany & Beasts. Healing. And Artificing. These fields may be among the better-known arenas of magic, but this foundational course will delve deeper than that. How we decide what makes a magical field separate from another, how certain fields are defined in different countries in a historical, religious, and sociocultural context. Now can someone tell me...?"
   
   hide pc
   
   "The chimes ring, signalling the end of the lesson. I stand and stretch, feeling stiff from sitting at the desk for so long. I pack up my bag and head towards the door with the rest of the class."

   #"The chimes ring, signalling the end of the lesson. I stand and stretch, feeling stiff from sitting at the desk for so long. I pack up my bag and head towards the door with the rest of the class, before I almost trip on something."

   #v "That looks like..."

   #show bracelet

   #"I pick up the bracelet from the floor. It looks a little bit familiar. Oh, right. Wasn’t Connor wearing this, when I first met him? It looks sort of expensive. If he dropped it, I probably should return it to him."

   #hide bracelet [All of this will be hidden until we figure out what the code is for unlocking it.]
   show o at right

   o "It’s lunchtime! Where are you going to go now?" 

   "Most of the class has filed out already. Nora waved cheerfully to me as she left, Liam dashed off to his after-class job. Connor looked like he was heading back to his room. Shouhei's left too, Kinuko gliding behind him."

   "I think I’ll go eat lunch at..."

$lpoints = 0
$spoints = 0
$npoints = 0
$cpoints = 0
   
menu:

    "The health center":
            $lpoints += 1
            jump health1
            
    "The lake":
            $spoints += 1
            jump lake1
       
    "The rose garden":
            $npoints += 1
            jump garden1
            
    #"The dorms":
            #$cpoints += 1
            #jump dorms1
        
       
label health1:
    
    "I head downstairs from the classroom, towards the health center. One of Liam's moms is a healer, and he’s been interested in healing since before I can remember. It's nice to see that some things haven’t changed."
    
    scene bg 4 # school hallway with an open door
    
    #[First closeup of Liam. Liam is helping someone with their familiar. Viola possibly has a flashback of when Liam helped her also when they were young. Back to present.]
    
    "He’s with someone else. It looks like their bird familiar has some kind of issue."
    
    l "Just remember to let him rest after every 3 cycles or so, and he will be fine. Come back again if he starts having issues later. You’ll both be all right now."
    
    "The familiar--a grey plover--nuzzles Liam’s hand before sinking back into its phone. It’s easy for many people (and their familiars) to trust Liam, with his calm presence and his reassuring voice. That reminds me..."
    
    #Do we want to have child sprites for Viola, Liam, and Shouhei? If so, we should use them here. If not, maybe we should keep the whole scene black; it'd need a few different CGs to convey the progression of events, and it's short enough that that's not really practical.
    
    scene bg black
    
    l "Viola! Viola! Where are you?"
    
    v "What happened?"
    
    l "Quickly! I think it’s hurt!"
    
    #play sound "running footsteps.mp3"
    
    "I look down. Liam is crouched down, trying to reach out his hand to something small and white-furred. I crouch down too."
    
    v "It’s a weasel. What are you trying to do?"
    
    l "Its front leg is..."
    
    "I lean forward. It’s hard to see the weasel against the snow we’re kneeling in, but. There. A red slicing scratch on one of its legs, as it tries to skitter away from Liam’s fingers."
    
    l "If I could just bring it back with me, then maybe TK- his healer mom could help it. Ow!"
    
    v "Liam!"
    
    "Liam rocks back from his position, holding his hand. The weasel slips around Liam’s foot and jumps into the snow, disappearing from sight."   
    
    "We look around for awhile but the weasel is nowhere to be seen. We hurry back to Liam’s house."
    
    l "I don’t understand. I just wanted to help it get better."
    
    lm "Oh, Liam. It’s not a bad thing to want to help something that has been hurt. But it was scared and didn’t know who you were. That’s the only reason why it bit you."
    
    l "But, but what else can I do to help someone if I can help them, but they’re scared?"
    
    lm "Staying calm would be the first thing. They have more reason to be scared than you do, if they’re hurt. You can come visit my other patients with me later tomorrow, if you want to learn more."
    
    l "Can’t I go today?"
    
    lm "Not that fast. We should clean your scratch first. I’ll go find the disinfectant."
    
    "Liam’s mother walks out of the dining room, towards the upstairs."
    
    v "Liam? Does it still hurt?"
    
    l "Not that badly."
    
    v "Okay. I’ll just sit here for a little while."
    
    "I see Liam’s other hand, the uninjured one, is squeezed into a fist. I reach out and tug on his sleeve." 
    
    v "You shouldn’t do that to your other hand. Here." 
    
    l "What?"
    
    v "If you need to hold something, you can hold my hand. Just until your mother comes back." 
    
    "Liam doesn’t look at me, but he reaches across our chairs, and his fingers squeeze around mine."
    
    l "Thanks."
    
    scene bg healthcenter
    
    show l normal at center
    
    l "Viola! I thought you would be at lunch."
    
    jump postchoice
    
label lake1:
    
    "It’s a nice day. The outdoors would be a great spot to relax and eat lunch, especially after the crowded classroom. I jiggle the doorhandle of the exit until the door turns from red to rust-orange to blue, and push it open. The air is cool, and smells like sun-warmed grass, a hint of pine."
    
    "The school tries to keep the environment comfortable for students most of the time, so the weather tends to be more temperate. I have heard there was some tricky spellwork that cordoned off a certain lab building on campus to include 10 or 12 different kinds of land types, though not every student will visit all those areas. The BB students sure love that feature though." 
    
    "I jog forward, until the blue line that I see in the distance expands into the lake. The Wishing Well is its official name, but everyone else just calls it  (the Waffle (great place to eat pastries and stare at the water) some funny name here- The Lake of Mistakes, 3 AM Regrets, the Oubliette)."
    
    "A cold wind rushes past and my hair flies forward, fluttering past my face. I shake my head and look up."
    
    "My stomach drops."
    
    "I recognize that bird. And I recognize that face."
    
    mystery "How did you get here?"
    
    show s normal at left
    show k normal at right
    
    "Kinuko, Shouhei’s familiar, is now resting on the lake in a spot two feet away from the shore. She raises her head to regard me with one black eye." 
    
    v "What do you mean, how I got here? I walked, just like everyone else would."
    
    s "I mean this spot by the lake. I had a spell set up to warn me if anyone else had come to this spot." 
    
    v "You always did like to find the quiet spots away from everyone else, except for..."
    
    "I stop myself before I finish the sentence. 'Except for when you were bored, and wanted to see me and Liam,' I almost said." 
    
    "Oh. The silence is getting awkward, now. I’m not sure if I still want to eat lunch here."
    
    s "I need to get to my next class. You can stay here if you want."
    
    hide s
    hide k
    
    "That’s definitely a lie. It’s barely been ten minutes since lunch started. The phone in my pocket shakes, and Olly slips out, landing on my shoulder."
    
    show o normal at right
    
    o "Viola! Aren’t you going to say anything to him?"
    
    hide o
    
    "Shouhei and Kinuko are getting farther and farther away. My fists clench."
    
    v angry "I’m not that hungry, Shouhei! You don’t need to trouble yourself because of me. So don’t act like you’re doing me any favors."
    
    "Shouhei turns around. He takes one step forward, and another."
    
    show s angry at center
    
    s "I just needed to be somewhere else. You don’t have to take it personally, Viola."
    
    v "I’m taking it personally? Me? You have to go because you can’t stand to see me or something?"
    
    show o normal at right
    
    o "I thought you two were just going to talk, Viola." 
    
    hide o
    
    "Olly sounds nervous. It’s been a long time since Shouhei and I have talked, I know. Not just days or weeks. It’s been years. I know that. But he can’t even give me a 'hello?'" 
    
    "Something in Shouhei’s face stiffens. The light is bouncing off at a strange angle from his glasses, a glare slashing through the sight of his dark eyes."
    
    s angry "I don’t like lying. You know that." 
    
    v "If you have to say something, then just say it to me straight out. Don’t dance around the topic."
    
    s "Fine. You had to ask it. Yes."
    
    v "Yes, what?"
    
    s "I don’t want to see you."
    
    "I can’t speak. The anger that rushes to my head isn’t red, but stronger than that, burning like ice on skin."
    
    v "Why--how could you say that? Did you even think about how Liam would feel? How I would feel? We didn’t hear from you for so long, it was like you had di--"
    
    s "Like I had died, you mean."
    
    v sad "..."
    
    v "Did you. Did you not talk to us because your family asked you not to?"
    
    "It sounds desperate. I’m just trying, trying hard to get answers from Shouhei. I trust that he’ll still answer me truthfully, even after our long silence, even after everything that has happened."
    
    s "I decided not to answer any letters or calls, on my own. Liam’s. And yours. It’s not like they keep me locked up in my own home."
    
    v "I never said I thought that--"
    
    s "If it’s skeletons you’re looking for, Viola, I would check your own backyard first."
    
    "I draw back, with a visible flinch. A rush of wind passes between us again, this time not from Kinuko. My eyes close, briefly. Now I’m the one who doesn’t want to look at Shouhei’s face anymore."
    
    show k at left
    
    "I open my eyes. Kinuko is next to Shouhei, and he has his head tilted towards her. She must be speaking, but it’s not loud enough for me to hear."
    
    s normal "I didn’t mean what I said earlier."
    
    "Shouhei’s expression doesn’t really match his words. But he does seem less cold, than he was before. It’s polite, the thing he is saying. That is all I can sense."
    
    s "I really am sorry for being rude. I hope--"
    
    "His voice stops, just for a moment."
    
    s "I hope we can both do well this year. Have a good semester."
    
    hide s
    hide k
    
    "He leaves then. Kinuko seems to turn to look at me, just once. Then she follows, as she always does."
    
    show o normal at right
    
    o "Viola? Are you all right?"
    
    "I drop down to sit on the grass and rest my head on my knees. Olly’s next to me and there’s no other sounds now other than the water moving over the lake and my own breathing. I have to keep it together. I just need a couple seconds."
    
    v normal "I’ll be fine. I’m glad we could talk to him, at least. I still have a little bit of time to finish lunch, so we can talk about something else."
    
    "So we do. Well, I eat lunch. Olly chatters away, until our next class bell rings."

    
    jump postchoice

label garden1:
    
    "Walking to class through the rose gardens earlier reminded me how much I used to love them when I was younger. Liam and I would play tag or hide and seek in the hedge maze with...well, that part doesn't matter anymore. It's been a long time." 
    
    "I feel like I remember there being benches, too, carefully crafted from living wood. I used to lie on them sometimes, pretending I could feel the warmth of their life radiating from below me." 
    
    "I'm sure I can find a nice place to eat lunch there, and maybe I'll have time to wander around a bit more before my next class." 
    
    "Luckily, everyone else is gone now, so there's no waiting or arguing over the door. The last person left it on an eye-wateringly bright pink--wherever that goes--so I pull on it to reset to default grey, then turn it to exit the building." 
    
    "The sun feels nice on my face, but it's just warm enough that the intermittent shade once I enter the gardens feels good, too. I wander for a while, letting my feet go where they will." 
    
    "I've stopped to admire a particularly beautiful specimen--a blend of deep blues and purples that make me think of space, almost as big as my face and with thorns as long as my finger--when I hear faint, tuneless humming."
    
    o "What's that?" 
    
    v "Maybe the botanists have started experimenting with roses that sing?" 
    
    "I'm only half joking, but the truth turns out to be much simpler: my new roommate, Nora." 
    
    "She's sitting on a bench in a half-shaded nook, sun warm on the fluff of her curls, but with her face hidden in shadow, bent over the phone she's placed on the bench in front of her. A small, golden-brown creature projects above it--a griffin, I think?--with an assortment of graphs scattered above its head." #CGI here?
    
    "The humming stops as Nora takes a bite from the sandwich she's holding in one hand, and pokes at one of the graphs with a finger." 
    
    "I realize I sort of miss it. Then I realize I should probably say something instead of just staring." 
    
    scene bg rose garden
    show n normal
    
    v "Um, hi?" 
    
    "Nora looks up, clearly startled. Her free hand spasms towards her mid-air display, but she arrests the motion halfway." 
    
    v "Sorry, I'm disturbing you, aren't I? I can go." 
    
    n "No, no, it's fine. I just wasn't expecting to see anyone. Do you want to join me? You're welcome to." 
    
    "She shifts over, pulling her phone into her lap, dismissing the rows of graphs, and leaving half the bench for me. I hesitate, but her invitation seems sincere and, well. I *am* hungry." 
    
    "I make it a whole two bites into my lunch before I can't hold my curiosity in anymore." 
    
    v "What was the, uh. Stuff? You had up earlier."
    
    "Smooth." 
    
    "Nora looks vaguely embarrassed, but she answers easily enough." 
    
    n "Diagnostic output. Perrault has been experiencing some hiccups the last few days--literally, if you can believe it?--so he asked me to take a look."
    
    v "Perrault--your familiar? Mine's name is Oleander, but I just call him Olly." 
    
    o "Hello, Nora, Perrault. It's nice to meet you." 
    
    show p normal at right
    
    p "Likewise. *hic* Sorry." 
    
    "Nora definitely looks embarrassed now. I don't see why, though." 
    
    v happy "It's really cool that you can figure out problems like that on your own! Olly and I are useless--we always end up having to go to a shop if he has any problems. Are you planning on majoring in Artificing?" 
    
    "That would explain why there were so many little mechanical and electronic things scattered across her desk and side of the room when I moved in earlier." 
    
    show n happy
    
    "Nora smiles, looking more relaxed now." 
    
    n "Perrault lets me experiment on him sometimes, so I figure it's only fair I fix my mistakes." 
    
    p "Avenues of discovery." 
    
    n "Yes, yes, avenues of discovering that I did something wrong. Anyway, Artificing is my plan.  How about you? Do you know what you want to major in yet?" 
    
    "I hesitate. Even though it's no big secret--I had to fill it in on my admission form!--saying it out loud feels like a confidence, even if I'm not going into all the reasons *why*." 
    
    v "I want to study Cursebreaking, if I can make it through all the prerequisites with high enough grades." 
    
    n "Wow! That's also pretty intense. Good luck to both of us!" 
    
    "She grins, and I grin back. I have a feeling that I'll enjoy having her as a roommate this year." 
    
    n "And, hey--if Olly has any problems, I'd be happy to take a look at him. I promise I won't tinker with anything without getting your permission first." 
    
    "I glance at Olly. He shrugs, wings rising and falling in a single fluid motion." 
    
    v "Sure, I think I'd like that." 
    
    n "And if I run into any curses, I'll be sure to call on you." 
    
    v "Haha, I'll do my best to get rid of them." 
    
    "Hopefully, before anyone else runs afoul of them." 
    
    "I shake off my dark thoughts. There will be a time for that, but for now I just want to concentrate on enjoying good food, the warmth of the sun, and pleasant conversation with my roommate." 
    
    "And so I do, until it's time for us to head to our next class."

    
#label dorms1:

    #c "y"
    
label postchoice:
   
   v "y"

   return
   
