define v = Character("Viola", image= "v")
define n = Character("Nora", image = "n")
define l = Character("Liam", image = "l")
define c = Character("Colin", image = "c")
define s = Character("Shouhei", image = "s")
define o = Character("Olly", image = "o")
define cl = Character("Clara", image = "cl")
define k = Character("Kinuko", image = "k")
define p = Character("Perrault", image = "p")
define pc = Character("Professor Corbet", image = "pc")
define pm = Character("Professor Marquez", image = "pm")
define bt = Character("Bonnie")
define mystery = Character("???")
define s1 = Character("Student 1")
define s2 = Character("Student 2")

define audio.dooropen = "Door Squeak.mp3"
define audio.magiceffect = "shootingstar.mp3"

default lpoints = 0
default spoints = 0
default npoints = 0
default cpoints = 0

image side v normal = "v normal.jpg"
image side v happy = "v happy.jpg"
image l normal = "l normal.jpg"
image l happy = "l happy.jpg"
image n normal = "n normal.jpg"
image c normal = "c normal.jpg"

label start:
   # 1.1 Atmospheric intro scene
   scene bg 1 # university birds-eye view 
   
   "Wyderwold University.  The premier applied magic college in the United States. Members of my family have attended for generations, and I've wanted to come, following in my sister's footsteps, since before I can remember."

   "Rumor has it that the school is afflicted with a very peculiar curse: that if you run across it, and you're lucky, you'll be marked for greatness, destined for a life of wealth and plenty."

   "If you're unlucky..."

   "Well."

   "After what happened to my sister, to my whole family, I've wanted to come to this school even more."

   "So I can find the source of the curse, and end it. For good."
   
   # 1.2 Viola moves into the dorms 
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
   
   "Back when we were younger, we'd all three planned to attend together. But then, well. That hadn't really worked out." 
   
   "We planned to both arrive at the same time, so we could help each other move in, but then my parents had a meeting that ran late, and there was a minor emergency of some sort, and--well, an on-time arrival just didn't happen." 
   
   l "I'm heading back downstairs for another load." 
   
   v happy "Thanks! Just--be careful if you grab the purple duffle bag, it's got some kinda fragile stuff inside." 
   
   l "Got it." 
   
   "Luckily, he doesn't seem to mind helping me out, even if I got here too late to return the favor. I should see if he'll let me buy him lunch sometime this week, as thanks."
   
   scene bg v dorm
   
   "It looks like I got here a lot later than my new roommate, too. Her side of the room is already set up." 
   
   "A computer on her desk with a large lamp looming over it; a bed carefully made up with a comforter in a lovely shade of light blue; a wardrobe with one door left slightly ajar is filled with clothes, and a stack of deconstructed cardboard boxes are stacked up behind the trash cans." 
   
   "I'd be a bit worried that she'd think I was some sort of slob--I'm truly not, but I also don't always keep everything 100 percent straightened 100 percent of the time--except for the stack of small objects scattered over the rest of her desk, a few of which appeared to have spilled over onto her bed and the floor." 
   
   "A couple of them look like old smartphones, or pieces of them, but most of them I have no idea what they are, or what they're for." 
   
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
   
   "The dorm administrators set up a station in the main hall of the dorms, where you can leave your boxes and they'll be dealt with appropriately." 
   
   "I'm sure if recycling is exactly the right word, given that I also heard that that was where you were supposed to go to get materials to pack up for the summer." 
   
   "It seems like a waste if they're going to end up breaking the boxes down at the beginning of the year just to reconstitute them into...more boxes, at the end of the year. But as far as I'm concerned, the boxes will be out of my dorm room and not my problem anymore, which is all I need to know."
   
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

   "He leaves, and I turn back to my side of the room. I've still got so much left to unpack before I can even think about collapsing into bed for the night." 

   "But at least I'm here now."

   # 1.3 Viola and Nora go to their first class 

   scene bg 2 # Nora and Viola's dorm room

# I kinda wanna put a fade in here. 

   show n normal

   n "Viola, are you about ready? It's almost time for Magical Fields to start."

   v "Yes, I'll be right there!"
   
   "Turns out we have two classes together--Magical Fields and Summoning 101. It'll be nice to know someone other than Liam in a few of my classes."

   v "Let's go! This is your first time on campus, right? Let's go by way of the gardens, I'll show you the way."

   n "As long as it doesn't make us late-–"
 
   # 1.4 First Magical Fields class

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

   l "Oh, and this is my roommate, Colin."
   
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
   
   "We all turn to Colin, but before he has a chance to introduce his familiar, the professor comes in, and we all hastily sit down."
   
   pc "Welcome to Foundations 105: Magical Fields. I'm Professor Corbet." 
   
   pc "And as this likely the first class for many of you, I would like to formally welcome you to Wyderwold University as well."
   
   "Nora leans over from her desk, about to say something when--"

   play sound dooropen 

   mystery "Sorry for being late, Professor."

   scene bg #CG scene: Viola and Liam staring at the person standing in front of the door, nora and Colin confused in background

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

   #"Nora’s desk isn’t too far away from mine. Unfortunately, Liam’s halfway across the room, and Colin’s off in the opposite corner. Shouhei is in the middle of the room." [Is there a reason they're all separated?]
   
   pc "As I was saying..."
   
   "I should pay attention to Corbet, but I'm still stuck on Shouhei. Neither I nor Liam have spoken to him since...it was a while ago. I shake off the thought. I can talk with Liam about this later. I turn to the board and Corbet begins their lesson."

   pc "Summoning. Enchantment. Botany & Beasts. Healing. Artificing. These fields may be among the better-known arenas of magic, but this foundational course will delve deeper than that."

   pc "How do we decide what makes one magical field separate from another? How are certain fields defined in different countries in a historical, religious, and sociocultural context? Now can someone tell me--?"
   
   hide pc
   
   "Eventually, the chimes ring, signalling the end of the lesson. I stand and stretch, feeling stiff from sitting at the desk for so long. I pack up my bag and head towards the door with the rest of the class."

   #"The chimes ring, signalling the end of the lesson. I stand and stretch, feeling stiff from sitting at the desk for so long. I pack up my bag and head towards the door with the rest of the class, before I almost trip on something."

   #v "That looks like..."

   #show bracelet

   #"I pick up the bracelet from the floor. It looks a little bit familiar. Oh, right. Wasn’t Colin wearing this, when I first met him? It looks sort of expensive. If he dropped it, I probably should return it to him."

   #hide bracelet [All of this will be hidden until we figure out what the code is for unlocking it.]
   show o at right

   o "It’s lunchtime! Where are you going to go now?" 

   "Most of the class has filed out already. Nora waved cheerfully to me as she left, Liam dashed off to his after-class job. Colin looked like he was heading back to his room. Shouhei's left too, Kinuko gliding behind him."

   "I think I’ll go eat lunch at..."
   
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

   # 1.5a Lunch with Liam 

   "I head downstairs from the classroom, towards the health center. One of Liam's moms is a healer, and he’s been interested in healing since before I can remember. It's nice to see that some things haven’t changed."
    
   scene bg 4 # school hallway with an open door
    
   #[First closeup of Liam. Liam is helping someone with their familiar. Viola possibly has a flashback of when Liam helped her also when they were young. Back to present.]
    
   "He’s with someone else. Another student. It looks like their bird familiar has some kind of issue."
    
   l "Just remember to let him rest after every 3 cycles or so, and he will be fine. Come back again if he starts having issues later. You’ll both be all right now."
    
   "The familiar--a grey plover--nuzzles Liam’s hand before sinking back into its phone. It’s easy for many people (and their familiars) to trust Liam, with his calm presence and his reassuring voice. That reminds me..."
    
   #Do we want to have child sprites for Viola, Liam, and Shouhei? If so, we should use them here. If not, maybe we should keep the whole scene black; it'd need a few different CGs to convey the progression of events, and it's short enough that that's not really practical.
    
   scene bg black
    
   l "Viola! Viola! Where are you?"
    
   v "What happened?"
    
   l "Quickly! I think it’s hurt!"
    
   "I look down. Liam is crouched down, trying to reach out his hand to something small and white-furred. I crouch down too."
    
   v "It’s a weasel. What are you trying to do?"
    
   l "Its front leg is--"
    
   "I lean forward. It’s hard to see the weasel against the snow we’re kneeling in, but. There. A red slicing scratch on one of its legs, as it tries to skitter away from Liam’s fingers."
    
   l "If I could just bring it back with me, then maybe one of my mothers could help it. Ow!"
    
   v "Liam!"
    
   "Liam rocks back from his position, holding his hand. The weasel slips around Liam’s foot and jumps into the snow, disappearing from sight."   
    
   "We look around for awhile but the weasel is nowhere to be seen. We hurry back to Liam’s house." 

   "Inside, one of his mothers, Mrs. Bonnie, is studying an array of vials on a table. On seeing our faces, she wastes no time in whisking her vials off to a counter and asking us both to sit down."
    
   l "I don’t understand. I just wanted to help it get better."
    
   bt "Oh, Liam. It’s not a bad thing to want to help something that has been hurt. But it was scared and didn’t know who you were. That’s the only reason why it bit you."
    
   l "But, but what else can I do to help someone if I can help them, but they’re scared?"
    
   bt "Staying calm would be the first thing. They have more reason to be scared than you do, if they’re hurt. You can come visit my other patients with me later tomorrow, if you want to learn more."
    
   l "Can’t I go today?"
    
   bt "Not that fast. We should clean your scratch first. I’ll go find the disinfectant."
    
   "Mrs. Bonnie walks out of the dining room, towards the upstairs."
    
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
   
   v "I. Um. Thought you didn't have lunch yet. Do you want to eat together?"
   
   "The words hang awkwardly in the air for a second. I would be fine if he didn't want to, but it would be nice. To catch up."
   
   l "Yes! Just let me clean up here for a second. I'll be right out."

   "We both get bags of sandwiches from a little stand outside the health center. Liam seems to take a lot longer to choose his sandwich and pay."
   
   "We eat sitting against the wall of the building, and chat a bit about our majors and schedules."
   
   "There are other topics--other people--we could be talking about too, but it's the first time I have seen him in a while. A long while."
   
   "I make a mental note to bring it up to him later. Olly and Clara don't show up--well, it might be better to let them conserve their energy for classes later on in the day."

   "I'm folding up some used paper napkins into my paper bag to throw away when Liam taps something against my hand."
   
   v "Liam, what...?"

   l "So. Um. Do you want this? This was your favorite before, and I saw it hidden away under some drinks at the stand we were at. But, uh, I don't know if you still like it."

   "It's a little container of green jello, with a green apple on the lid. I complained a lot when I was smaller, I think, at how many times I tried something green, only to find out it was lime-flavored and not apple."

   "Liam's face is looking at mine. His hand holding the jello moves down a little, like he wants to put it back into the paper bag."

   v "No! Wait!"
   
   v "Yes! Sorry, I mean yes. I still like it. Thank you."

   "The nervousness disappears from Liam's expression and he smiles when I reach out to take the jello from his hand. I open the lid and take a spoonful. It's as good as the hundreds of times I had it before, as good as I remember it to be."
    
   jump postlunch
    
label lake1:
    
   # 1.5b Lunch with Shouhei

   "It’s a nice day. The outdoors would be a great spot to relax and eat lunch, especially after the crowded classroom. I jiggle the doorhandle of the exit until the door turns from red to rust-orange to blue, and push it open. The air is cool, and smells like sun-warmed grass, a hint of pine."
    
   "The school tries to keep the environment comfortable for students most of the time, so the weather tends to be more temperate. I have heard there was some tricky spellwork that cordoned off a certain lab building on campus to include about ten different kinds of land and habitat types. The BB students sure love that feature." 
    
   "I jog forward, until the blue line that I see in the distance expands into the lake. The Wishing Well is its official name, but I don't think any student actually calls it that."
    
   "A cold wind rushes past and my hair flies forward, fluttering past my face. I shake my head and look up."
   
   play sound magiceffect
    
   "My stomach drops."
    
   "I recognize that bird. And I recognize that face."
    
   mystery "How did you get here?"
   
   show s normal at left
   show k normal at right
    
   "Kinuko, Shouhei’s familiar, is now resting on the lake in a spot two feet away from the shore. She raises her head to regard me with one black eye." 
   
   v "What do you mean, how I got here? I walked, just like everyone else would."
    
   s "I mean this spot by the lake. I had a spell set up to warn me if anyone else had come here." 
    
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
    
   "Shouhei’s expression doesn’t really match his words. But he does seem less cold, than he was before. It’s polite, the things he's saying. That is all I can sense."
    
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

    
   jump postlunch

label garden1:
    
   # 1.5c Lunch with Nora

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

   jump postlunch
    
#label dorms1:

   # 1.5d Lunch with Colin

    #c "y"
    
label postlunch:
   
   # 1.6 Viola seeks Liam out to talk about Shouhei

   # play sound footsteps.mp3 

   scene bg hallway

   "There's still an hour or two before my first Cursebreaking class of the year. It's only the third day of the school year and I don't want to give a bad impression by being late to any classes before we even turn in our first assignments." 
   
   "I still have time to find Liam. If I could only remember which room is his..."

   o "13...15...25...Viola! Is it this one? The green door!"

   "The front door of his shared dorm suite. Is that a doorbell?" 

   v "Oh, wait. Olly? The door, please?" 

   o "Of course!" 

   "Olly swoops up from my phone, floating up to the doorknob and presses his snout against it. The door chimes. 'Viola Ashmark, first year' glows in silvery letters across the front of the door."

   "The letters dissolve into the wood. 'Please enter,' flashes on the door a moment later."

   "Liam must be in. Outside of general sleeping hours, students can invite mostly anyone they like into their dorms. The security system at Wynderwold allows students to enter most places with a familiar. For those without one, a demonstrated spell would suffice."  

   play sound dooropen

   "Olly zips back into my phone and I dash inside, my bag swinging against my hip."

   v "Liam? You here? It took me a while to find the right door number, but I just wanted to see if we could talk a little more--"

   "I blink. It's Colin in front of me, a hoodie half-zipped up and a short towel draped around his neck. Droplets of water drip from his hair."

   c "Hi. I'm going to go with my first guess that it's not me you're looking for."

# menu: There will be a menu here once we figure out how to hide/show Colin's route 

#     "Right. I'm looking for Liam, is he in?":
#            $lpoints += 1
#            jump liam1
            
#    "I'm looking. You know me, I always appreciate a nice view.":
#            $cpoints += 1
#            jump colin1

# label liam1: 

   # 1.7a Viola and Liam talk about Shouhei 

   v "Right. I'm looking for Liam, is he in? The copy of his schedule that he gave me says he should be free right now, but."

   c "You have his schedule, huh? He did tell me to expect you to show up round here a lot. He should be right in there." 

   l "Viola!"

   "Liam's head pokes out from behind another door. He smiles when he sees me and waves, the holograph of Clara nestling on top of his head." 

   c "Well, I see you two have things to talk about. I'm out, got things to do and all."

   "Colin hangs his towel over the back of a chair and fully zips up his jacket. The door opens with a creak and closes behind him."

   "I walk into the room, to see their shared dorm room. Other than the small living area and kitchen area where Colin had been standing, the rest of the room is neat. In decent shape." 
   
   "Liam's space has a cheerful blue plaid quilt over his bed, some open textbooks on top of his desk, and no boxes to be seen anywhere on the floor. 
   
   "There's another bed and desk opposite his, but with a honey-brown blanket instead. Colin's side, I think."  

   v "You got everything unpacked."

   "Some of mine still aren't. I make a mental note to clean more of it up after class today."

   l "I could come over and help if you needed me to. Did you want to get an early dinner today or--?"

   v "That's not what I wanted to talk about."

   "Liam's smile falls. On his head, Clara lifts up her ears and opens her eyes. Her nose twitches, once, twice. She drops to his shoulder, then without a word, shimmers and fades into his phone."

   "In my own phone, Olly is silent. I'm grateful, to the both of them."

   v "I couldn't believe it, you know. That Shouhei would go here."

   l "I know. I know."

   "Liam is silent still, watching me. He pats his hand on the chair next to the one he is sitting in."

   "I sit down. Kick at the bottom of my chair legs, just to see the wheels move over the floor.."

   v "It's just…"

   "I still don't know what to say. Liam remembers. He's one of the few who would remember, who would understand."

   l "Did you want to talk to him? Or do you want him to--do you want us to stay away from him?"

   v "I think--. I don't know. You can talk to him, Liam, I don't think it's fair if I'm the one to tell you not to."

   "My chair spins, slowly. One circle, and another. My thoughts are, too. Honestly speaking though, I don't want to have to think about him." 
   
   "I do want to see him though, get some answers. Get to the truth. If Liam does become friends with him again...something in my stomach clenches at that."
   
   "I don't want to avoid Liam, I don't want to have to avoid both of them."

   l "Well."

   "I stop spinning. Liam's hand is on my shoulder, resting there, his grip sure and warm. The pressure is reassuring."

   l "He was my friend, once, before. But right now, you're the one who is here. Your friendship matters to me." 

   v "Thank you."

   "My hand reaches up to squeeze his hand on my shoulder. He smiles, and lets go. I want to say more than that. But I have to focus. The topic we were discussing..."

   v "I don't want to have to talk to him. I can be polite if I have to. And if there's something he knows about what happened. I want to find that out."

   l "That time all those years ago...It was a bad one for both of you. If there's something else you need to find about it, something you need, I'll help you the best I can, you know that?" 

   v "I'll remember that, Liam."

   "He nods, expression serious. Then he stands and rolls his shoulders."

   l "So. How about that dinner, before your class?"

   "And off we go, to the cafeteria. My steps are lighter now, hearing Liam's footsteps following me. No matter what, I think, I know I can count on him."

jump common_nora1

# label colin1: 

# 1.7b Viola and Colin flirt 

# jump liam1 <= going back to the Liam scene

label common_nora1:

   # 1.8 Viola and Nora chat in the evening

   scene bg v dorm

   $npoints += 1

   "Liam and I talked for so long over dinner that the cafeteria personnel eventually had to politely ask us to leave. We kept the conversation carefully away from … certain topics, but luckily having known each other for (TK seven?) years means there's never a shortage of things to talk about." 

   "I'm glad we did. I'm feeling a bit better about this whole situation after having taken my mind off it for a while." 

   "I do feel a bit bad for coming back to the room so late, though. I'm not breaking curfew (yet) but I have no idea what sort of schedule Nora keeps. I'd hate to be the kind of inconsiderate person who barges in after her roommate is already asleep."

   "I turn the corner and see the door to our room, light clearly shining from the crack underneath the door into the dim corridor, and sigh in relief. Looks like I'm safe this time."

   "Nora is sitting at her desk, bent over--something small? I would have guessed her phone, but that's sitting off to the side, charging.  Perrault hovers above it, also peering at the device in Nora's hands."

   "After a moment's hesitation, I enter the room. I hang my jacket and scarf on the hooks near the door, set my bag on the floor next to my desk, and flop across the bed." 

   "It's been a long day." 

   n "Viola? Sorry, I didn't notice you coming in."

   v "I hope I didn't disturb you. You seemed really busy with--actually, what is it that you're working on, exactly?" 

   n "Oh, this? It's not really anything special. Just a little project for my parents that I didn't have a chance to finish before I came here." 

   "I lift my head. Nora looks a bit embarrassed, but pleased." 

   v "Your parents? Do they like fiddling with their familiars, too?" 

   n "Haha, you could say that--theirs and everyone else's! They run--you probably don't know it, but it's a little shop, in (TK major nearby city). Galena Gadgets." 

   "The name sounds vaguely familiar, but I can't quite place it." 

   v "Wait--it's near the Rainbow Fountain, right? I've never been inside, but I remember walking past it a few times. I always enjoyed looking at the window displays." 

   "The hesitance fades from Nora's face as she beams at me. She has a very nice smile--almost as nice as her laugh." 

   n "Yes, that's my parents' shop.  My little brother does the displays--he's the best of us at figuring out what will draw people in." 

   v "That's really cool. Is your entire family artificers?" 

   n "My grandfather started the business, and passed it down to my mom when he retired a few years ago. My dad claims she just married him because he has more patience with paperwork than she does, but he knows quite a bit too, even if he isn't as good at the really detailed work." 

   v "Wow, that's really cool." 

   "I can hardly imagine what it would be like, to have a life like that--growing up knowing exactly what you want to do, following in your parents' footsteps, with nothing hanging over your head. Even before--well, everything. I knew my place, but it had never really been a choice. Just the way things were." 

   n "Do you --" 

   v "What?" 

   "Nora looks like she's suddenly realized she made a terrible mistake, and despite myself, I find myself curious what awkward question she'd been about to ask. About my sister's supposed murder of her best friend? About my family's fall from grace? So many great choices, and she'd lasted longer than most before giving in to curiosity." 

   n "Sorry, it's not really my business." 

   v "Go ahead and ask. I can't promise I'll answer, though." 

   n "Okay. This is really rude, but, I was wondering--what does your family actually do? You're the heir, um, now, right? But what does that mean?" 

   "Oh. The question--the sheer normalcy of the question--catches me off guard, and I have to actually think a moment." 

   v "Not a whole lot, anymore, to be honest. It's usually a lot of networking--talking with the other high families, working together to solve issues in magical society. Or, you know, backstabbing each other and stealing the credit. That happens a lot, too." 

   v "No one really wants to work with the family whose heir got a life sentence for actually stabbing someone in the back, though. So." 

   "I close my eyes, take a deep breath and let it out. I shouldn't yell at Nora. It's not her fault that my family is a sensitive subject." 

   v "We have to do paperwork, too, of course. I suspect no one's entirely immune from that." 

   "Nora laughs quietly, and some of the tension in my shoulders eases. I like the sound of her laugh. It's … kind." 

   n "Sorry for prying. I get really curious, as you might have noticed, but I'm trying to be better about not getting into other people's business." 

   v "No, it was fine--I don't mind."

   "And I was surprised to find that it was true." 

   "I think I'm going to enjoy having Nora as my roommate. I hope she feels the same."

   scene bg 3 # Classroom

   # 1.9 Magical Fields introduces the group project 

   "Magical Fields is buzzing with speculation as I walk in a respectable five minutes before class starts. And no wonder--Professor Marquez told us on Wednesday that she hoped she would have some exciting news for us today." 

   "Liam waves me over--he's early, of course, and it looks like he saved me a seat." 

   show l normal

   l "Morning! So what's your guess about this mysterious announcement?" 

   show v shrugging

   v "No idea. It sounded like she wasn't sure, though, so maybe it'll turn out to be nothing?" 

   "A few rows ahead, Nora turns to look at us." 

   show v normal 
   show n normal

   n "It's probably something to do with the syllabus, don't you think? It's strange that this is the only class where we haven't received a grading rubric yet, when we're already nearly two weeks into the semester. The only class I'm taking, at least." 

   show l thoughtful 

   l "No, you're right--my other classes all gave us that information on day 1." 

   v "Same here." 

   "Before we have a chance to speculate further, Professor Marquez walks in." 

   hide v 
   hide n
   hide l 
   show pm

   pm "Good morning, class! Looks like you're all here already, good. Let's go ahead and get started." 

   pm "First, I have some excellent news for you all! I've finally gotten official sign-off on my proposed changes to the curriculum this year." 

   "I exchange a skeptical look with Liam. An experimental curriculum sounded like it could be fun, or could be a complete mess--and I knew which one I would bet on." 

   pm "Aww, don't make those faces at me--this will be fun!" 

   pm "For those of you with older siblings who've told you all about how this class goes--well, first of all, shame on them, ruining the surprise! But you won't see a lot of changes from how it usually goes this semester. Next semester, however ..." 

   "She pauses dramatically, as though daring anyone to ask her what she means. No one does." 

   "At least no one's staring at me after that mention of older siblings. Or at Shouhei, who as usual is sitting in the farthest corner away from where Liam and I are sitting." 

   "Just as well--Eliza must have taken this class, but she'd never told me anything about it, and I didn't think that Mariko had ever said anything to Shouhei, either. He would have mentioned it, back then." 

   "Or at least, I thought he would have."

   pm "Next semester is when the fun really starts: I'm going to have you all pair up and do a group project!" 

   "Instantly, the classroom started buzzing as everyone turned to comment to each other. I shared another look with Liam and Nora." 

   "Maybe one of them would be my partner? Liam and I always used to do group projects together back in elementary school." 

   pm "If you're trying to talk your seatmates into teaming up with you, I regret to announce that you're wasting your time--I will be assigning everyone's partners."

   s1 "What are the group projects going to be about?" 

   pm "I'm glad you asked! *That*, each group will be allowed to choose, but it must be related to at least two of the magical fields we discuss in this class. Think of it as a … practical application of the skills you'll be gaining." 

   "Okay, I'd been pretty skeptical--and I still didn't like that we wouldn't get to pick our partners; what if I ended up with someone I didn't get along with?--but this sounded like it might actually be pretty fun."

   "I definitely wanted to do a project related to cursebreaking somehow, but what else?" 

   s2 "What if your partner is going into the same field as you are?" 

   pm "That's one of the reasons I'm reserving the right to assign partners--I'll be aiming for a good distribution of interests and skills. However, I will also note that the magical fields involved in your project do not necessarily have to correspond to your declared majors." 

   pm "In fact, I'd recommend everyone go into this project with an open mind. After all, what you think you're interested in now may change over the course of the year, or over the course of the next four years." 

   pm "This could be an excellent chance for you to test out a different field, and find out that you like it." 

   "A few rows away, Colin looked thoughtful. I tried to remember if he'd mentioned what field he was going into. Maybe he was undeclared?" 

   "Liam and Nora looked less convinced, and I'm sure I did as well. I'm sure there were plenty of good things about the various other majors, and that I'd do all right in some of them. But I was going into cursebreaking for more reasons than just because I thought it would be fun." 

   "And regardless of what I learned this semester in this class, I doubted that would change." 

   pm "So get started thinking about what projects you might want to do! I'll assign your partners in November, and you'll have the rest of the semester after that to make a final decision on the subject of your project, and the entirety of next semester to work on it." 

   pm "Any other questions? No? All right, then let's get back to work. Continuing from where we left off on Wednesday, I'll be covering the basics of (TK subject) today …" 

   "I pull out my notebook and started taking notes." 

   scene bg outdoors 
   
   # 1.10 Viola enjoys the day, decides who to do homework with

   "The day had dawned bright and warm, the weather so nice it seemed like a terrible waste to have to spend most of my morning in Summoning 101." 

   "Admittedly, for once it hadn't been a complete waste of time. " # [TK interesting factoid here.]

   "Still, I was glad that was over with, and now I was sitting in a corner of the outdoor seating area of the dining hall, finishing up a sandwich." 

   o "What do you want to do this afternoon?" 

   v "I don't care, really, as long as it's not inside."

   o "Shouldn't you be working on homework? All your professors seem to like to assign a lot of it." 

   "That was definitely true. Most of them seem to be under the mistaken impression that their class is the only one we're taking, and they assign ridiculous amounts to prove it." 

   o "Would you like me to provide you with a list? I can order them by due date." 

   v "No, that's fine!" 

   "I lean back in my chair and try to think.  Olly's right about one thing--I really probably should make progress on something. Take advantage of my open Monday afternoons while I still had them, since I've heard that we'll start having more intense practicums as the semester goes on." 

   "It's such a nice day, though." 

   "Come to think of it--everyone else should have Monday afternoon free, too. Maybe I should see if I can find one of my classmates to do homework with?" 

menu: 

   "I'll see if I can find Nora":
      $npoints += 1
      jump nora2

   "I think I'll go study with Liam.":
      $lpoints += 1
      jump liam2

   #"(Colin)":
      #$cpoints += 1
      # jump colin2

label nora2:

   v "y"

   jump posthomework

label liam2:

   v "I sit up straighter in my chair. That looks like Liam, just walking out of the Larks Library. I stand up and wave in his direction."
   
   "He stops. He is standing a bit far to see me--is he doing the 'do I know this person?' calculation in his head right now?"
   
   "I pull a textbook out of my bag and wave that in the air also, with my other hand pointing at it. He jogs over."
   
   show l normal
   
   l "Viola! Are you studying now?" 
   
   v "Yeah. Thinking of getting started at least. Are you free?"
   
   l "Right now is fine. What's giving you trouble today?"
   
   v "This chapter of our Magical Fields reading. Something about famous botanists and their histories--I'm fine with reading that, but it feels like half of them have the same names!"
   
   l "Well, I can't say you're wrong there. A lot of them were from the same family lines, or adopted into them, after all."
   
   "Liam's face brightens." 
   
   l "I know exactly where we should go. Come on."
   
   "He catches the book I was waving around to tuck it under his elbow. Before I realize it, his other hand closes around my right hand, and we're running along."
   
   "We go past the dining hall, a library, and make a few turns. We go up one set of stairs. Then another."
   
   l "We're here!"
   
   "He lets go of my hand. I look to where he's pointing. The stairs lead out onto a type of...balcony? It does look like a quiet spot."
   
   l "You want to be careful here."
   
   "He walks out onto the balcony, leans an elbow against the white columned railing while staring into the distance." 
   
   "After a moment, he puts one hand down on the railing and swings one leg up--"
   
   v "LIAM!" 
   
   v "What are you doing??"
   
   "I've rushed up closer to him, but not too close. We have to be at least three stories up. Liam looks at my face."
   
   "His expression turns apologetic. He slips down from the railing, and walks back from the edge."
   
   l "I didn't mean to scare you. Sorry Viola. I thought--we could study at the tree down there? You could ask Olly to check if it's safe, if you want to?"
   
   "I set back my shoulders, and walk along the balcony to where Liam was standing before. There's a ladder there--a fire escape?"
   
   "I look down past the ladder." 
   
   "There is a tree there. I don't know what kind exactly. It's big. Old. The branches are just about high enough to touch the last runs of the ladder."
   
   "I look a bit closer. There is a big wooden platform there, built right between the tree branches. Enough to fit about five or six people sitting comfortable on it."
   
   v "Who made this?"
   
   l "I don't really know. Some graduate students? I've just been here once or twice, and if we were studying a chapter on botanists, I thought it would make more sense"
   
   l "if we were outdoors and it was supposed to be a good idea but I ended up worrying you, which I didn't plan to do. At all. Really, really sorry about that."
   
   "I don't think Liam was even breathing when he said all that."
   
   v "Okay! Ok, Liam. I forgive you. I think it looks safe enough. Let's get down there."
   
   l "Oh. Ok. If it's alright with you--ladies first?"
   
   "It doesn't take long for both of us to get down there."
   
   "I don't think Liam's feet even stayed on the ladder for more than two seconds. He practically seems to just leap down in two jumps after I reached the platform."
     
   "Olly does leave my phone after a while, zipping off in short loops around branches. Clara jumps out too, eventually. Scares off some butterflies that were flapping around the tiny blossoms on the tree."
   
   "It is autumn, but the weather this time of the day still carries the lingering warmth of summer. We sit cross-legged from each other on the platform, and I watch Liam add some diagrams to my notes."
   
   "His drawings are careful, detailed. Each part precisely labeled. The different flowers he sketches over the page look almost real."
   
   v "I think I get it now! Thanks!"
   
   l "Fair's fair, Viola. You think you could quiz me on this chapter?" 
   
   v "For which class? Healing?"
   
   l "Yeah." 
   
   "Liam closes his eyes. I take the book from his hand and adjust my position, so we're sitting back to back. I read aloud each marked word slowly, waiting for his voice to speak and supply the definitions."
   
   "It's a nice afternoon. We get a lot of our assignments done, and I get to see him. All in all, a productive day." 
  
   jump posthomework

label posthomework:

   v "a"

   return

