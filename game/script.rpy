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
define j = Character("Janitor") # :D
define kc = Character("Ken", image = "kc")

define audio.dooropen = "Door Squeak.mp3"
define audio.magiceffect = "shootingstar.mp3"
define audio.forest = "Nature Ambiance.mp3"
define audio.crash = "mirror breaking.mp3"

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
image v upside down = im.Flip("v normal.jpg", vertical=True)

label start:

   "DEBUG CHOICE: IS COLIN'S ROUTE UNLOCKED?"

   menu: 

      "Yes.":

         $persistent.colin_route_unlocked = True

      "No.": 

         $persistent.colin_route_unlocked = False

   ### MONTH ONE BEGINS ###

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
   
   v normal "Oh, sorry! We're almost done. I'm your new roommate--Viola Ashmark." 
   
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

   v normal "Sorry, I should have introduced you earlier--this is Liam. We were friends when we were younger." 

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

   v normal "Yes, I'll be right there!"
   
   "Turns out we have two classes together--Magical Fields and Summoning 101. It'll be nice to know someone other than Liam in a few of my classes."

   v "Let's go! This is your first time on campus, right? Let's go by way of the gardens, I'll show you the way."

   n "As long as it doesn't make us late-–"
 
   # 1.4 First Magical Fields class

   scene bg mf_class 
   show n normal

   v normal "–-And the first rose bush was originally donated by one of my ancestors, though it's at the center of the garden, so we didn't see it this time."
  
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
   
   hide p

   "Perrault seems pretty laid back; he manifests in a sitting position and doesn't bother to either stand or open his wings. I hope this is a good sign that he and Nora will make good roommates. I really like Clara, but even if co-ed dorm rooms were allowed, I don't think I'd want to live with her."

   "Though who knows, maybe she's calmed down in the past few years."
   
   "I glance over at Colin, the only one of us who hasn't brought out their familiar yet. He notices, and his face turns sheepish."
   
   c normal "I actually don't have a familiar. Yeah, I know, whatever."
   
   v "Oh, that's fine."
   
   "Fine? I mean, it is fine, but it's not really my place to give approval or not, so why'd I say that? I needed to say *something*, right? He probably gets a lot of rude comments about it. Maybe I shouldn't have said anything. But then it would've been awkward, right?"
   
   "Plenty of people don't have familiars. Maybe he can't afford one. Maybe he doesn't want to talk about it."
   
   "Maybe I should stop thinking about this."
   
   "Thankfully, the professor comes in, and my conversational abilities are saved."
   
   pm "Welcome to Foundations 105: Magical Fields. I'm Professor Marquez!" 
   
   pm "As this is the first day for most of you at Wyderwold University, we can skim over the basics today before getting into the really fun stuff--"
   
   "Nora leans over from her desk, about to say something when--"

   play sound dooropen 

   mystery "Sorry for being late, Professor."

   scene bg #CG scene: Viola and Liam staring at the person standing in front of the door, nora and Colin confused in background

   v "That person is--" #I'm sure there's a way to show a character's name without showing their sprite, but actually, what do you guys think about showing sprites at Viola's location during CGs? It's especially useful for if the CGs don't show everyone's faces. We'd just have to make and define new side images.

   pm "Shouhei Utsurikawa, was it? Come in, come in--take a seat anywhere that's free!"

   "The chatter in the room starts up again, but I can barely hear it. His eyes skim the room before they stop to look at--me? Liam? Both?"
   
   "He doesn’t meet my glance, though. His eyes flicker away, and he takes a seat on the opposite side of the room. Without another word, he takes out his books and faces forward, away from us."
   
   scene bg mf_class
   show n normal at left

   n "You know that guy?" 

   "Before I can answer, suddenly--"
   
   hide n
   
   play sound magiceffect

   show k

   "A crane appears, gracefully gliding through an open window to rest by Shouhei’s desk. A physical familiar. The whispers around me get louder. Physical familiars are not unknown, but rarer now than they once were."
   
   hide k
   show pm normal
   
   #pm "All right, class, we have all year to make friends--which I very much hope you will--but let's get this show started."

   #"Nora’s desk isn’t too far away from mine. Unfortunately, Liam’s halfway across the room, and Colin’s off in the opposite corner. Shouhei is in the middle of the room." [Is there a reason they're all separated?]
   
   "I should pay attention to Marquez, but I'm still stuck on Shouhei. Neither I nor Liam have spoken to him since...it was a while ago. I shake off the thought. I can talk with Liam about this later. I turn to the board and Professor Marquez begins their lesson."

   pm "Summoning. Enchantment. Botany & Beasts. Healing. Artificing. These fields may be among the better-known arenas of magic, but this foundational course will look deeper than that."

   pm "How do we decide what makes one magical field separate from another? What factors--social, religious, cultural--shape and differentiate the developments of any magical field? Now can someone tell me--?"
   
   hide pm
   
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
            
   "The dorms" if persistent.colin_route_unlocked == True:
      $cpoints += 1
      jump dorms1
        
       
label health1:

   # 1.5a Lunch with Liam 
   
   hide o

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
    
   show l normal
    
   l "Viola! I thought you would be at lunch."
   
   v normal "I. Um. Thought you didn't have lunch yet. Do you want to eat together?"
   
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
   
   v happy "Yes! Sorry, I mean yes. I still like it. Thank you."
   
   show l happy

   "The nervousness disappears from Liam's expression and he smiles when I reach out to take the jello from his hand. I open the lid and take a spoonful. It's as good as the hundreds of times I had it before, as good as I remember it to be."
    
   jump postlunch
    
label lake1:
    
   # 1.5b Lunch with Shouhei

   hide o
   
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
   
   v normal "What do you mean, how I got here? I walked, just like everyone else would."
    
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
    
   show s angry
    
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
    
   "Shouhei’s expression doesn’t really match his words. But he does seem less cold than he was before. It’s polite, the things he's saying. That is all I can sense."
    
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
   
   hide o
   scene bg rosegarden

   "Walking to class through the rose gardens earlier reminded me how much I used to love them when I was younger. Liam and I would play tag or hide and seek in the hedge maze with...well, that part doesn't matter anymore. It's been a long time." 
    
   "I feel like I remember there being benches, too, carefully crafted from living wood. I used to lie on them sometimes, pretending I could feel the warmth of their life radiating from below me." 
    
   "I'm sure I can find a nice place to eat lunch there, and maybe I'll have time to wander around a bit more before my next class." 
    
   "Luckily, everyone else is gone now, so there's no waiting or arguing over the door. The last person left it on an eye-wateringly bright pink--wherever that goes--so I pull on it to reset to default grey, then turn it to exit the building." 
    
   "The sun feels nice on my face, but it's just warm enough that the intermittent shade once I enter the gardens feels good, too. I wander for a while, letting my feet go where they will." 
    
   "I've stopped to admire a particularly beautiful specimen--a blend of deep blues and purples that make me think of space, almost as big as my face and with thorns as long as my finger--when I hear faint, tuneless humming."
   
   show o normal at right
    
   o "What's that?" 
    
   v normal "Maybe the botanists have started experimenting with roses that sing?" 
   
   hide o
    
   "I'm only half joking, but the truth turns out to be much simpler: my new roommate, Nora." 
    
   "She's sitting on a bench in a half-shaded nook, sun warm on the fluff of her curls, but with her face hidden in shadow, bent over the phone she's placed on the bench in front of her. Perrault projects above it with an assortment of graphs scattered above his head." #CGI here?
    
   "The humming stops as Nora takes a bite from the sandwich she's holding in one hand, and pokes at one of the graphs with a finger." 
    
   "I realize I sort of miss it. Then I realize I should probably say something instead of just staring." 
    
   scene bg rose garden
   show n normal
    
   v normal "Um, hi?" 
   
   "Nora looks up, clearly startled. Her free hand spasms towards her mid-air display, but she arrests the motion halfway." 
    
   v "Sorry, I'm disturbing you, aren't I? I can go." 
    
   n "No, no, it's fine. I just wasn't expecting to see anyone. Do you want to join me? You're welcome to." 
    
   "She shifts over, pulling her phone into her lap, dismissing the rows of graphs, and leaving half the bench for me. I hesitate, but her invitation seems sincere and, well. I *am* hungry." 
    
   "I make it a whole two bites into my lunch before I can't hold my curiosity in anymore." 
    
   v "What was the, uh. Stuff? You had up earlier."
    
   "Smooth." 
    
   "Nora looks vaguely embarrassed, but she answers easily enough." 
    
   n "Diagnostic output. Perrault has been experiencing some hiccups the last few days--literally, if you can believe it?--so he asked me to take a look."
   
   show p normal at right
    
   "Perrault makes a hiccuping noise. It's strangely cute." 
   
   hide p
   
   show n embarrassed
    
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
    
label dorms1:

   # 1.5d Lunch with Colin

   c "y"
    
label postlunch:
   
   # 1.6 Viola seeks Liam out to talk about Shouhei

   # play sound footsteps.mp3 

   scene bg hallway

   "There's still an hour or two before my first Cursebreaking class of the year. It's only the third day of the school year and I don't want to give a bad impression by being late to any classes before we even turn in our first assignments." 
   
   "I still have time to find Liam. If I could only remember which room is his..."
   
   show o normal at right

   o "13...15...25...Viola! Is it this one? The green door!"

   "The front door of his shared dorm suite. Is that a doorbell?" 

   v normal "Oh, wait. Olly? The door, please?" 

   o "Of course!" 
   
   hide o

   "Olly swoops up from my phone, floating up to the doorknob and presses his snout against it. The door chimes. 'Viola Ashmark, first year' glows in silvery letters across the front of the door."

   "The letters dissolve into the wood. 'Please enter' flashes on the door a moment later."

   "Liam must be in. Outside of general sleeping hours, students can invite mostly anyone they like into their dorms. The security system at Wyderwold allows students to enter most places with a familiar. For those without one, a demonstrated spell would suffice."  

   play sound dooropen

   "Olly zips back into my phone and I dash inside, my bag swinging against my hip."

   v "Liam? You here? It took me a while to find the right door number, but I just wanted to see if we could talk a little more--"

   "I blink. It's Colin in front of me, a hoodie half-zipped up and a short towel draped around his neck. Droplets of water drip from his hair." # I think there should be a CG here. You know, for reasons.

   c "Hi. I'm going to go with my first guess that it's not me you're looking for."
   
   menu: 

      "Right. I'm looking for Liam, is he in?":
         $lpoints += 1
         jump liam1

      "Oh, I'm looking." if persistent.colin_route_unlocked == True:
         $cpoints += 1
         jump colin1
         
label colin1:
    
    v happy "Oh, I'm looking."
    
    "WHY'D I SAY THAT."
    
    c embarrassed "Um."
    
    v embarrassed "At. The...other doors, because Liam's probably behind one of them? Yeah."
    
    c "Yeah."
    
    "Remember me as I lived: good at standardized tests, bad at...this."
    
    l "Viola!"
    
    "Liam's head pokes out from behind another door. I'm saved! He smiles when he sees me and waves, the holograph of Clara nestling on top of his head."
    
    c "I'm gonna...let you two talk now."
    
    v "Yeah."
    
    "Deep breaths. I came here for a serious reason, after all. I should put this disaster out of my head."
    
    "For now."
    
    jump liampostcolin

label liam1: 

   # 1.7a Viola and Liam talk about Shouhei 

   v "Right. I'm looking for Liam, is he in? The copy of his schedule that he gave me says he should be free right now, but."

   c "You have his schedule, huh? He did tell me to expect you to show up round here a lot. He should be right in there." 

   l "Viola!"

   "Liam's head pokes out from behind another door. He smiles when he sees me and waves, the holograph of Clara nestling on top of his head." 

   c "Well, I see you two have things to talk about. I'm out, got things to do and all."
   
label liampostcolin:

   "Colin hangs his towel over the back of a chair and fully zips up his jacket. The door opens with a creak and closes behind him."

   "I walk into the room, to see their shared dorm room. Other than the small living area and kitchen area where Colin had been standing, the rest of the room is neat. In decent shape." 
   
   "Liam's space has a cheerful blue plaid quilt over his bed, some open textbooks on top of his desk, and no boxes to be seen anywhere on the floor."
   
   "There's another bed and desk opposite his, but with a honey-brown blanket instead. Colin's side, I think."  

   v normal "You got everything unpacked."

   "Some of mine still aren't. I make a mental note to clean more of it up after class today."
   
   show l normal

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

   v "I think--I don't know. You can talk to him, Liam, I don't think it's fair if I'm the one to tell you not to."

   "My chair spins, slowly. One circle, and another. My thoughts are, too. Honestly speaking though, I don't want to have to think about him." 
   
   "I do want to see him though, get some answers. Get to the truth. If Liam does become friends with him again...something in my stomach clenches at that."
   
   "I don't want to avoid Liam, I don't want to have to avoid both of them."

   l "Well."

   "I stop spinning. Liam's hand is on my shoulder, resting there, his grip sure and warm. The pressure is reassuring."

   l "He was my friend, once, before. But right now, you're the one who is here. Your friendship matters to me." 

   v happy "Thank you."

   "My hand reaches up to squeeze his hand on my shoulder. He smiles, and lets go. I want to say more than that. But I have to focus. The topic we were discussing..."

   v normal "I don't want to have to talk to him. I can be polite if I have to. And if there's something he knows about what happened. I want to find that out."

   l "That time all those years ago...It was a bad one for both of you. If there's something else you need to find about it, something you need, I'll help you the best I can, you know that?" 

   v "I'll remember that, Liam."

   "He nods, expression serious. Then he stands and rolls his shoulders."

   l happy "So. How about that dinner, before your class?"

   "And off we go, to the cafeteria. My steps are lighter now, hearing Liam's footsteps following me. No matter what, I think, I know I can count on him."

   jump common_nora1

label common_nora1:

   # 1.8 Viola and Nora chat in the evening

   scene bg v dorm

   $npoints += 1 # Does this need to be here? It's not a choice scene.

   "Liam and I talked for so long over dinner that the cafeteria personnel eventually had to politely ask us to leave. We kept the conversation carefully away from...certain topics, but luckily having known each other for (TK seven?) years means there's never a shortage of things to talk about." 

   "I'm glad we did. I'm feeling a bit better about this whole situation after having taken my mind off it for a while." 

   "I do feel a bit bad for coming back to the room so late, though. I'm not breaking curfew (yet) but I have no idea what sort of schedule Nora keeps. I'd hate to be the kind of inconsiderate person who barges in after her roommate is already asleep."

   "I turn the corner and see the door to our room, light clearly shining from the crack underneath the door into the dim corridor, and sigh in relief. Looks like I'm safe this time."

   "Nora is sitting at her desk, bent over--something small? I would have guessed her phone, but that's sitting off to the side, charging.  Perrault hovers above it, also peering at the device in Nora's hands."

   "After a moment's hesitation, I enter the room. I hang my jacket and scarf on the hooks near the door, set my bag on the floor next to my desk, and flop across the bed." 

   "It's been a long day." 
   
   show n normal

   n "Viola? Sorry, I didn't notice you coming in."

   v normal "I hope I didn't disturb you. You seemed really busy with--actually, what is it that you're working on, exactly?" 

   n "Oh, this? It's not really anything special. Just a little project for my parents that I didn't have a chance to finish before I came here." 

   "I lift my head. Nora looks a bit embarrassed, but pleased." 

   v "Your parents? Do they like fiddling with their familiars, too?" 

   n "Haha, you could say that--theirs and everyone else's! They run--you probably don't know it, but it's a little shop, in (TK major nearby city). Galena Gadgets." 

   "The name sounds vaguely familiar, but I can't quite place it." 

   v "Wait--it's near the Rainbow Fountain, right? I've never been inside, but I remember walking past it a few times. I always enjoyed looking at the window displays." 
   
   show n happy

   "The hesitance fades from Nora's face as she beams at me. She has a very nice smile--almost as nice as her laugh." 

   n "Yes, that's my parents' shop.  My little brother does the displays--he's the best of us at figuring out what will draw people in." 

   v happy "That's really cool. Is your entire family artificers?" 

   n "My grandfather started the business, and passed it down to my mom when he retired a few years ago. My dad claims she just married him because he has more patience with paperwork than she does, but he knows quite a bit too, even if he isn't as good at the really detailed work." 

   v "Wow, that's really cool." 

   "I can hardly imagine what it would be like, to have a life like that--growing up knowing exactly what you want to do, following in your parents' footsteps, with nothing hanging over your head. Even before--well, everything. I knew my place, but it had never really been a choice. Just the way things were." 

   n normal "Do you--" 

   v normal "What?" 

   "Nora looks like she's suddenly realized she made a terrible mistake, and despite myself, I find myself curious what awkward question she'd been about to ask. About my sister's supposed murder of her best friend? About my family's fall from grace? So many great choices, and she'd lasted longer than most before giving in to curiosity." 

   n "Sorry, it's not really my business." 

   v "Go ahead and ask. I can't promise I'll answer, though." 

   n "Okay. This is really rude, but, I was wondering--what does your family actually do? You're the heir, um, now, right? But what does that mean?" 

   "Oh. The question--the sheer normalcy of the question--catches me off guard, and I have to actually think a moment." 

   v "Not a whole lot, anymore, to be honest. It's usually a lot of networking--talking with the other high families, working together to solve issues in magical society. Or, you know, backstabbing each other and stealing the credit. That happens a lot, too." 

   v "No one really wants to work with the family whose heir got a life sentence for actually stabbing someone in the back, though. So." 

   "I close my eyes, take a deep breath and let it out. I shouldn't yell at Nora. It's not her fault that my family is a sensitive subject." 

   v "We have to do paperwork, too, of course. I suspect no one's entirely immune from that." 

   "Nora laughs quietly, and some of the tension in my shoulders eases. I like the sound of her laugh. It's...kind." 

   n "Sorry for prying. I get really curious, as you might have noticed, but I'm trying to be better about not getting into other people's business." 

   v "No, it was fine--I don't mind."

   "And I was surprised to find that it was true." 

   "I think I'm going to enjoy having Nora as my roommate. I hope she feels the same."

   scene bg mf_class

   # 1.9 Magical Fields introduces the group project 

   "Magical Fields is buzzing with speculation as Nora and I walk in a respectable five minutes before class starts. And no wonder--Professor Marquez told us on Wednesday that they hoped they would have some exciting news for us today." 

   "Liam waves us over--he's early, of course, and it looks like he saved us some seats. Colin is next to him, as usual." 

   show l normal at left
   show c normal at right

   l "Morning! So what's your guess about this mysterious announcement?" 

   v shrugging "No idea. It sounded like they weren't sure, though, so maybe it'll turn out to be nothing?" 
   
   show n normal at center

   n "It's probably something to do with the syllabus, don't you think? It's strange that this is the only class where we haven't received a grading rubric yet, when we're already nearly two weeks into the semester. The only class I'm taking, at least." 

   l thoughtful "No, you're right--my other classes all gave us that information on day 1." 

   v "Same here." 

   "Before we have a chance to speculate further, Professor Marquez walks in." 

   hide c
   hide n
   hide l 
   show pm

   pm "Good morning, class! Looks like you're all here already, good. Let's go ahead and get started." 

   pm "First, I have some excellent news for you all! I've finally gotten official sign-off on my proposed changes to the curriculum this year." 
   
   show l normal at left

   "I exchange a skeptical look with Liam. An experimental curriculum sounded like it could be fun, or could be a complete mess--and I knew which one I would bet on." 
   
   hide l

   pm "Aww, don't make those faces at me--this will be fun!" 

   pm "For those of you with older siblings who've told you all about how this class goes--well, first of all, shame on them, ruining the surprise! But you won't see a lot of changes from how it usually goes this semester. Next semester, however..." 

   "They pause dramatically, as though daring anyone to ask them what they mean. No one does." 
   
   show s normal at right

   "At least no one's staring at me after that mention of older siblings. Or at Shouhei, who as usual is sitting in the farthest corner away from where Liam and I are sitting." 

   "Just as well--Eliza must have taken this class, but she'd never told me anything about it, and I don't think that Mariko had ever said anything to Shouhei, either. He would have mentioned it, back then." 

   "Or at least, I think he would have."
   
   hide s

   pm "Next semester is when the fun really starts: I'm going to have you all pair up and do a group project!" 
   
   show l normal at left
   show n normal at right

   "Instantly, the classroom starts buzzing as everyone turns to comment to each other. I share another look with Liam and Nora." 

   "Maybe one of them will be my partner? Liam and I always used to do group projects together back in elementary school." 
   
   hide l
   hide n

   pm "If you're trying to talk your seatmates into teaming up with you, I regret to announce that you're wasting your time--I will be assigning everyone's partners."

   s1 "What are the group projects going to be about?" 

   pm "I'm glad you asked! *That*, each group will be allowed to choose, but it must be related to at least two of the magical fields we discuss in this class. Think of it as a...practical application of the skills you'll be gaining." 

   "Okay, I'd been pretty skeptical--and I still don't like that we won't get to pick our partners; what if I end up with someone I don't get along with?--but this sounds like it might actually be pretty fun."

   "I definitely want to do a project related to cursebreaking somehow, but what else?" 

   s2 "What if your partner is going into the same field as you are?" 

   pm "That's one of the reasons I'm reserving the right to assign partners--I'll be aiming for a good distribution of interests and skills. However, I will also note that the magical fields involved in your project do not necessarily have to correspond to your declared majors." 

   pm "In fact, I'd recommend everyone go into this project with an open mind. After all, what you think you're interested in now may change over the course of the year, or over the course of the next four years." 

   pm "This could be an excellent chance for you to test out a different field, and find out that you like it." 
   
   show c normal at left

   "Colin looks thoughtful. I try to remember if he mentioned what field he's going into. Maybe he's undeclared?"
   
   hide c
   show l normal at left
   show n normal at right

   "Liam and Nora look less convinced, and I'm sure I do as well. I'm sure there are plenty of good things about the various other majors, and that I'd do all right in some of them. But I'm going into cursebreaking for more reasons than just because I thought it would be fun." 
   
   hide l
   hide n

   "And regardless of what I learn this semester in this class, I doubt that will change." 

   pm "So get started thinking about what projects you might want to do! I'll assign your partners in November, and you'll have the rest of the semester after that to make a final decision on the subject of your project, and the entirety of next semester to work on it." 

   pm "Any other questions? No? All right, then let's get back to work. Continuing from where we left off on Wednesday, I'll be covering the basics of (TK subject) today..." 

   "I pull out my notebook and start taking notes." 

   scene bg outdoors 
   
   # 1.10 Viola enjoys the day, decides who to do homework with

   "The day's dawned bright and warm on the third week of the semester, the weather so nice it seems like a terrible waste to have spent most of my morning indoors." 

   "Admittedly, Magical Fields was fun today. We learned about a witch who turned a whole swarm of bees into her familiars and used them to chase away people from her orchard. Antisocial, but cool, especially since having multiple familiars can drain you dry if you're not careful."

   "Still, I'm glad that's over with, and now I'm sitting in a corner of the outdoor seating area of the dining hall, finishing up a sandwich." 
   
   show o normal at right

   o "What do you want to do this afternoon?" 

   v normal "I don't care, really, as long as it's not inside."

   o "Shouldn't you be working on homework? All your professors seem to like to assign a lot of it." 

   "That's definitely true. Most of them seem to be under the mistaken impression that their class is the only one we're taking, and they assign ridiculous amounts to prove it." 

   o "Would you like me to provide you with a list? I can order them by due date." 

   v "No, that's fine!" 
   
   hide o

   "I lean back in my chair and try to think. Olly's right about one thing--I really probably should make progress on something. Take advantage of my open Monday afternoons while I still had them, since I've heard that we'll start having more intense practicums as the semester goes on." 

   "It's such a nice day, though." 

   "Come to think of it--everyone else should have Monday afternoon free, too. Maybe I should see if I can find one of my classmates to do homework with?" 

menu: 

   "I'll see if I can find Nora":
      $npoints += 1
      jump nora2

   "I think I'll go study with Liam.":
      $lpoints += 1
      jump liam2

   "Maybe Colin's around somewhere?" if persistent.colin_route_unlocked == True:
      $cpoints += 1
      jump colin2

label nora2:

   # 1.11a Viola and Nora do homework

   v normal "I think I'll see if I can find Nora." 

   "She seems to really like the rose gardens, and I've been struggling a bit in Magical Law--if she's there and willing, I'll get to make progress on homework AND stay outside. Win-win!" 
   
   scene bg rosegarden

   "I head over to the gardens, and wander the rose maze until I'm almost lost in its depths, then I start hearing her humming. After that, I just need to turn a few more corners and I'm there." 

   show n normal

   n "Oh, Viola, hi! Were you looking for me?"

   "Now that I'm here, I'm suddenly having second thoughts. What if she comes here specifically so that she won't be bothered by people coming and trying to talk to her?" 

   "On the other hand, it would be even more awkward to back out now, and I really do need the help." 

   v normal "Actually, yes. I was wondering if you wanted to work on homework together for a while? I can leave if I'm bothering you, though." 

   n "It's no bother! I'd actually been meaning to ask you the same, but it seemed like too pretty of a day to waste inside."

   v laughing "My thought exactly!" 

   "Nora shifts, making more room on the bench, and I take a seat too. It feels wider than last time. I wonder if the benches in the garden are alive, too. It wouldn't surprise me." 

   n "What did you want to work on?"

   v normal "Would you mind if we looked at Magical Law? I'm terrible at it, honestly. It just puts me to sleep." 

   n laughing "Professor Prasad is rather...soothing, isn't he?" 

   n normal "And sure! I'm about halfway through the assignment for tomorrow; I think I understand it pretty well but it's been slow going. Do you have your textbook with you?" 

   "Oops. I have my assignment--it's synced to my phone like everything else--but the textbook itself is still back in our room." 

   "My consternation must be pretty obvious, because Nora grins sympathetically." 

   n happy "I'm guessing that's a 'no'. Perrault, if you don't mind?" 
   
   show p normal at right

   p "An Introduction to Magical Law, 1813 - 1897, right? Coming right up!" 
   
   hide p

   "Perrault was hovering in the air a few inches above Nora's phone, but now he spreads his wings wide, brings them forward to cover his head, and begins to glow." 

   "I have to look away as his glow brightens with a flash, and when I look back, what looks like a book--a very familiar textbook, in fact--now hovers in the air in his place." 

   "I lean in to take a better look. Aside from being vaguely translucent, it--he?--looks exactly like the text I had left on my desk." 

   v "Wow, I had no idea that familiars could do this. Olly, can you become one of my textbooks too?" 
   
   show o normal at right

   o "If so, no one's ever told me!" 
   
   hide o

   n normal "I'd have been surprised if you said anything else. It's an experimental feature that Perrault and I have been working on." 

   "She reaches out and appears to touch one of the pages, running her finger along it to pick it up and flip it." 

   n "I don't have the tactile sensations quite right yet--the pages still feel kind of furry, like Perrault's body does--but it mostly works otherwise? Would you like to try?" 

   v "Does it--he?--work for someone else? I thought phone familiars only physically manifested for their users." 

   "And even that isn't guaranteed--there's a setting you can modify to determine whether your familiar manifested physically as well as visually." 

   "Olly and I mostly leave it turned off, since he's just large enough that he has a tendency to accidentally bump into stuff, and it *does* make the phone's battery drain more quickly."

   n "Oh, that part's pretty easy to fix! The functionality is mostly supported even in base model familiars, it's just that it's not surfaced in a terribly user-friendly manner." 

   n "My family has a patch that gives people an easier way to work with that and a few other settings; it's one of the first things I've built that we actually sell." 

   v happy "That's really cool!" 

   n "It sounds cooler than it is--not very many people have actually bought it, to be honest." 

   v "Still ..." 

   "I reach over to touch the textbook, and can't suppress my laughter at the sensation." 

   v laughing "You're right, it really does feel like fur!" 

   "Nora helpfully moves her phone closer to me, making it easier for me to experimentally flip a few pages. I can feel the edges of the pages just barely well enough to move them, but they feel more like a wrinkle in a very fluffy rug than anything else."

   n "I'm really hoping I can get this working--I feel like it'll be really useful! All the convenience of an electronic book, but still with the physicality of a paper one. I know I tend to learn better if I can flip pages back and forth instead of trying to remember percentage completion." 

   v happy "Haha, same here. So, wait--does that mean that things like search and bookmarking still work?" 

   n "Of course! And narration, using either the standard electronic reader or, since your familiar is *right there*, and effectively holding the entire book in their memory anyway, they can read it to you instead." 

   "She turns to Perrault, taking a breath as though to start demonstrating some other cool feature, then pauses and looks back at me." 

   n "I um, should probably warn you that it's not complete yet? You don't need to worry about explosions, or anything, but things might not work, or might work kind of strangely." 

   v normal "That makes sense. I'll try not to be too disappointed if it doesn't work." 

   "I hope she can tell that I'm joking--and from her quick grin, I think it worked." 

   n happy "All right, here goes! Perrault, find--let's see, tomorrow afternoon's homework was from Chapter 2, wasn't it? Find 'War of 1812'." 
   
   show p normal at right

   p "You got it!" 
   
   hide p

   "I realize that I was expecting some sort of movie special effect--wind blowing, pages flipping wildly--when I brace myself, but then am almost disappointed that nothing happens, aside from the book perhaps glowing a bit more brightly." 

   "Instead, after a moment, what looks like one of the diagnostics panels that I'd seen Nora using before pops up, swiftly populating itself with a list of chapter, page numbers, and small excerpts of text." 

   "Nora scans the list briefly, then selects the third on the list. The book glows brightly for a moment, and when the glow subsides, I see that we are now on that page." 

   v happy "Wow!" 

   n "I'd like to make the interface cleaner, and animate the pages flipping. Though maybe that would get annoying after a while? I still need to think about that some more. I still need to work a lot on bookmarks, too." 

   "She runs her finger across a line of text about halfway down the page." 

   n "Perrault, could you bookmark that for me, please?" 
   
   show p normal at right

   p "Done!" 
   
   hide p

   "The line now looks like it's been highlighted, and a second window has popped up beside the search window. Nora casts a dissatisfied look at it." 

   n "And I'd really like to make my bookmarks look like actual bookmarks, you know? Make the window available for people if they need it, but otherwise they ought to just be able to touch a bookmark that's stuck in the book and flip to that page manually, like you'd do with a real book."

   v normal "That *would* be really cool. Not that this isn't! It seems really useful--I'm always leaving my textbooks behind, but I really don't like using the electronic ones if I don't have to." 

   "Nora ducks her head, looking almost embarrassed." 

   n embarrassed "Thanks. If you want, I could let you and Olly try a beta version, once I have it working a little bit better?" 

   v "Olly? Would you mind?" 
   
   show o normal at right

   o "No, it sounds like fun!" 
   
   hide o

   v "Then we'll happily take you up on that offer--I'm looking forward to it!" 

   v "And let me know if you want any help...I don't know what I'd be able to do, actually, but any second opinions on something?" 

   n normal "Thanks, I will." 

   n "...For now, we probably ought to be working on homework, though." 

   v embarrassed "Right." 

   n "Perrault, please turn to page 28." 

   "We spend a few hours in the gardens, reading and talking and working on our assignments, before the setting sun finally drives us back inside. Nora had completely finished her assignment, and mine was, well. Mostly done. Close enough that I'm pretty sure I'll be able to complete it on my own without too much trouble." 

   "Nora's really good at making the history sound interesting, and connecting the laws of the time period to things that were going on then." 

   "She says it's because her dad really likes history--apparently when they were younger, he'd read them children's books about a particular subject, then come back the next day with three new stories related to that subject that he'd found out about by looking it up online." 

   "It sounds...nice. My parents hadn't really had the time for that sort of thing, but had left strict instructions for my nanny that meant she was only allowed to read boring stories with morals about Duty and Honor and Responsibility." 

   "Occasionally, when Eliza had the time, she'd show up and overrule my parents' instructions. I'd loved those nights the best--my nanny would tell *amazing* stories about little girls who got to go on fantastic adventures and do amazing deeds." 

   "But they'd been uncommon to start with, and only grew more so as we grew up and Eliza had to spend more and more time on preparing to be a proper heir to our family."

   "Maybe I should look into history a bit more, though. It sounds like it might be interesting, and if it can help me stay awake in Magical Law, it'll be more than worth the time spent!" 

   jump posthomework

label liam2:

   # 1.11b Viola and Liam do homework

   "I sit up straighter in my chair. That looks like Liam, walking past the Larks Library with a crumpled lunch bag in one hand and a paper coffee cup in another. I stand up and wave in his direction."
   
   "He stops. He is standing a bit far to see me--is he doing the 'do I know this person?' calculation in his head right now?"
   
   "I pull a textbook out of my bag and wave that in the air also, with my other hand pointing at it. He jogs over."
   
   show l normal
   
   l "Viola! Are you studying now?" 
   
   v normal "Yeah. Thinking of getting started at least. Are you free?"
   
   l "Right now is fine. What's giving you trouble today?"
   
   v "This chapter of our Magical Fields reading. Something about famous botanists and their histories--I'm fine with reading that, but it feels like half of them have the same names!"
   
   l "Well, I can't say you're wrong there. A lot of them were from the same family lines, or adopted into them, after all."
   
   "Liam's face brightens." 
   
   l happy "I know exactly where we should go. Come on."
   
   "He tosses his lunch trash into a nearby trash bin, and catches the book I was waving around to tuck it under his elbow. Before I realize it, his other hand closes around my right hand, and we're running along."
   
   "We go past the dining hall, a library, and make a few turns. We go up one set of stairs. Then another."
   
   l "We're here!"
   
   "He lets go of my hand. I look to where he's pointing. The stairs lead out onto a type of...balcony? It does look like a quiet spot."
   
   l normal "You want to be careful here."
   
   "He walks out onto the balcony, leans an elbow against the white columned railing while staring into the distance." 
   
   "After a moment, he puts one hand down on the railing and swings one leg up--"
   
   v worried "LIAM!" 
   
   v "What are you doing??"
   
   "I've rushed up closer to him, but not too close. We have to be at least three stories up. Liam looks at my face."
   
   "His expression turns apologetic. He slips down from the railing, and walks back from the edge."
   
   l worried "I didn't mean to scare you. Sorry Viola. I thought--we could study at the tree down there? You could ask Olly to check if it's safe, if you want to?"
   
   "I set back my shoulders, and walk along the balcony to where Liam was standing before. There's a ladder there--a fire escape?"
   
   "I look down past the ladder." 
   
   "There's a tree there. I don't know what kind exactly. It's big. Old. The branches are just about high enough to touch the last rungs of the ladder."
   
   "I look a bit closer. There's a big wooden platform there, built right between the tree branches. Enough to fit about five or six people sitting comfortably on it."
   
   v normal "Who made this?"
   
   l normal "I don't really know. Some graduate students? I've just been here once or twice, and if we were studying a chapter on botanists, I thought it would make more sense."
   
   l "If we were outdoors and it was supposed to be a good idea but I ended up worrying you, which I didn't plan to do. At all. Really, really sorry about that."
   
   "I don't think Liam was even breathing when he said all that."
   
   v "Okay! Okay, Liam. I forgive you. I think it looks safe enough. Let's get down there."
   
   l "Oh. Okay. If it's alright with you--ladies first?"
   
   "It doesn't take long for both of us to get down there."
   
   "I don't think Liam's feet even stayed on the ladder for more than two seconds. It only takes him two jumps to get down after I reach the platform."
     
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

label colin2: 

   # 1.11c Viola and Colin do homework

   jump posthomework

label posthomework:

   # 1.12 Viola investigates the ~haunted~ vending machine

   scene bg outdoors

   "It's a sunny Sunday afternoon, the weather having been kind enough to remain nice all week, and I'm *finally* done with all of my homework. Which means I finally have a chance to do a little extra exploring!" 

   "I've been visiting Wyderwold off and on for as long as I can remember, but it's always been accompanied by someone: my parents, when I was younger; when Eliza was attending school here they let me come stay with her once, for a weekend, but even then I spent most of my time with her." 

   "So I know most of the big-name parts of the university pretty well; the parts that get shown off to prospective parents and donors. The rose garden, the library, the immense greenhouse out behind the Botany building." 

   "(Home to at least eight entirely separate biomes, including the largest collection of magical Arctic species in the Western Hemisphere.)" 

   "(Yes, I've heard the talks given to parents and donors more than once, too.)"

   "But I still don't know a whole lot about the smaller things, the ones that don't make it onto the school president's list of Top 20 Reasons You Should Donate Money To Us." 

   "And there are always rumors swirling around. *Probably* most of those rumors are caused by someone's class project gone wrong, but some of them might not be. And if I want to find out what *really* happened to my sister, I need to find out everything I can."

   "Besides, if I come across a cursed object or something, maybe I can practice some of what I've been learning in Cursebreaking 103. It's mostly been about verbal curses so far, but hey, maybe there's crossover?" 

   "First stop for the day: I overheard a couple of juniors talking in the cafeteria the other day about a vending machine out near the lake that might be haunted. Or cursed. There was some disagreement." 

   "One of them had claimed that she'd heard voices coming from it late at night, and another had said that no matter what button she pushed, and what sort of soda appeared to be dropped down the chute, the only thing it dispensed was bottled sparkling water." 

   "Not exactly the most dramatic of curses, if cursed it is, but I figure it's not a bad idea to start small."

   "I take the shortcut door from the dorm to the lake--it's a nice day for a walk, but I don't want to waste precious daylight hours that I could be using for investigating. The lakeside door leads to the small dock that rents boats for traveling across it; that's not my aim for today, so instead I head outside." 

   "The vending machine is supposedly a short way down the path; I pass a couple of upperclassmen loudly discussing some enchantment gone hilariously wrong. (At least to them--I wouldn't want to be the person who had to clean up that toilet after the fact!)"

   "I pass a small copse of trees and turn to see it. One of the custodial staff is just finishing up emptying out the trash cans as I approach; I step off the path to let him pass." 

   j "Appreciated, ma'am." 

   "He tips his cap to me as he walks by." 

   "Disappointingly, the vending machine looks, well. Like a vending machine. Five rows of wire racks hold five different types of drink each--none of which, I notice, are sparkling water--and a panel off to the side requests that you enter your desired row and column number, and pay the price shown." 

   "I stand there for a few minutes--partly listening for the suspicious voices that one person had mentioned, partly just trying to decide what to order." 

   "I hear nothing, of course, and eventually decide on an orange soda. I select it, hold my phone up to the panel to pay, and watch as the wire mechanism rotates and one of the bottles from the orange soda row drops." 

   "I realize I'm holding my breath as I reach in to pick it up, and make myself start breathing again." 

   "I pick the bottle up, and--" 

   "--it's just orange soda. As far as I can tell, exactly the same as what's being advertised." 

   "I sigh. Probably it was just someone's school project gone wrong, then, and they cleaned it up already. Or maybe the people talking had just been confused to begin with." 

   "Ah, well. I'll take the soda back to my room and run some additional tests on it. It'll be good practice. And if I find nothing, well. At least I have some delicious soda to drink?" 

   "It's disappointing, to have found nothing, but I suspect I'll be running into that a lot, so maybe it's good that I'm getting practice dealing with disappointment early?" 

   "I'm sure there will be other leads--I just need to keep my ears open." 

   ### MONTH TWO BEGINS ###

   # 2.1 Viola and Liam talk about Viola's family

   scene bg patio # patio outside the cafeteria

   "I'm eating lunch on the outdoor patio next to the cafeteria, trying to take advantage of the good weather while it lasts, when Liam walks up." 
   
   show l normal

   l "Mind if I join you?" 

   v normal "Not at all! Go ahead." 

   "He sits down, and we eat in companionable silence for a while. Suddenly, his phone buzzes."

   l "Clara, who is it from?" 
   
   show cl normal at right

   cl "It's from Mom. It's been a while since you last called her, you know." 
   
   hide cl

   l "Yeah, you're right--remind me tonight?" 

   "He looks at the text, and then laughs, and turns to show it to me." 

   "One of his mothers is standing next to what looks like a giant Venus flytrap, grinning broadly. Her head's far closer to those teeth than *I* would ever want to get, but then, I'm not a botanist." 

   v "Your moms are still doing well?" 

   l "They are--Mum's got steady work at the local hospital, and takes the occasional specialized client on the side, and Mom's, well, you saw--she's still at home most of the time, but she's gotten a few grants that have let her make a few more trips recently."

   v happy "That's good! I remember how much she used to enjoy those trips." 

   l "And...your family?" 

   "I grimace. I hate talking about this, but--if anyone deserves to know, and if anyone would actually *understand*, it's Liam." 

   "His family was affected by everything that happened too." 

   l "Sorry. You don't have to talk about it if you don't want to." 

   v normal "No, it's fine." 

   v "And things are about the same as ever, honestly. No one talks about any of...well, you know. If they can help it."

   l "Has she called at all?"

   "He has to mean Eliza."

   v "The usual stilted family calls on major holidays, though I think my parents would stop having them if they thought they could get away with it. Otherwise, not really." 

   "I'm aware I sound bitter, and part of me wants to rein myself in. Politically speaking, it makes total sense that my parents would not want to continue to associate themselves overly much with someone who had theoretically besmirched the family's name as much as my sister had." 

   "But I know Eliza wouldn't do something like that, and I hate the fact that they just took everything at face value. That the only reason they maintain contact at all is because it would reflect even worse on our family if we were seen as abandoning our own." 

   l "That sucks. I'm sorry."

   "I smile weakly at Liam. It helps that he understands my bitterness, at least. It feels nice to know that I still don't have to rein myself in around him." 

   l "...Do you mind if I ask you something...kind of personal?" 

   v "Of course not!" 

   l "Back then, you were convinced that Eliza didn't do anything wrong. Do you still think--?" # TK "didn't do anything wrong" implies that she did do something. Maybe "was innocent"?

   v "Yes." 

   "I know I sound short, and that's probably unfair to Liam, but did he really think that would have changed?" 

   "I loved--love--my sister, and I know her, and I had recognized nothing of her in the lurid media portrayals of her during the trial." 

   "She and Mariko--they'd been even closer friends than Shouhei, Liam, and I, back before everything. Almost all of the stories she'd told of Wyderwold had featured Mariko, and I'd hung on every one." 

   "Back then, I'd dreamed of coming here with Liam and Shouhei, the three of us together, having all sorts of fun adventures like Eliza and Mariko did." 

   "I guess all three of us made it here in the end, at least." 

   "But the trial--all the descriptions of rooms covered in blood, Eliza with Mariko's blood on her hands and face..." 

   "No, that is not the sister I know." 

   "So I don't care if she pled guilty. Maybe she was taking the fall for someone else. Maybe it was an accident and she felt responsible because there was nothing she could have done." 

   "But I refuse to believe that my sister would have killed her best friend in cold blood." 

   l "Has she ever said anything to you about it?" 

   "It's only his non-judgmental tone--and the fact that this is Liam--that keeps me from lashing out further. He's not the sort to lead me around in circular arguments. At least, he always used to be willing to tell me straight out when he thought I was wrong." 

   v "No. But we never get a chance to talk alone, either."

   "I tried to smuggle her my phone number early on, so she'd be able to contact me privately, but she never used it. So who knows if she even received it?"

   l "And you think she'd want to keep hiding it--whatever happened--from your parents?" 

   v "There must be a reason why she pled guilty, right? If someone was blackmailing her, or if something about the truth would have besmirched our family somehow...our parents are the last people she'd tell." 

   l "What if it is something like that?" 

   "I hesitate. It's something I've tried to avoid thinking about, to be honest. If proving Eliza's innocence means destroying our family from the inside..." 

   v "...I don't know." 

   v "But I need to know the truth." 

   "Liam meets my eyes, the solemn sincerity hitting me with an almost physical force." 

   l "You know I'll do everything I can to help you, right? Just let me know." 

   "And with Liam on my side, somehow the path ahead of me feels a little bit less steep than before." 

   scene bg v dorm

   # 2.? Viola and Nora talk about Nora's side projects

   "Cursebreaking today was fantastic! We talked about (TK something cool). I don't know if it'll come in handy at all for my immediate goals, but it's days like this that remind me that this really is what I want to do, even after breaking the curse on the school." 

   "There's just so much interesting stuff there." 

   "Plus! Professor Reynell gave each of us a small box at the end of class, and said that it was our homework for Friday." 

   "The box itself doesn't seem to be cursed--at least, not anything that activates with touch. Although I'm pretty sure I caught him laughing to himself as he watched all of us run through all the analyses we could think of as a group before someone finally gave in and picked a box up." 

   "I'm almost certain that whatever is inside the box--and there's definitely *something* inside; I can feel it sliding around when I'm not careful to keep the box steady--*is* cursed, though. It should be a fun puzzle to figure out." 

   "Nora was hard at work on something when I left for class, but I'm kind of hoping that she's wrapped it up by now. I don't want to disturb her with my homework, if the contents of the box end up involving loud noises or flashing lights or other similar annoyances." 

   "Unfortunately, when I stick my head into our room, it looks like she's still there." 

   "And, in fact, looks like she's leaning over the same fiddly device she was when I left, Perrault equally engrossed at her shoulder." 

   "I pad quietly into the room, putting my book bag by the side of the bed and the box next to it, for now, then sit down and watch for a little bit." 

   "If she wasn't breathing, and occasionally shifting position slightly, I'd have started wondering if she had been frozen somehow." 

   v normal "Hard assignment?"
   
   show n normal

   n "What? Oh, no, this isn't for class. I've already finished all my homework for tomorrow." 

   "And when she says all, she really means *all*--I intentionally tried to give myself a fairly balanced schedule, but as far as I can tell, Nora scheduled every class she possibly could in Tuesday/Thursday blocks." 

   "I occasionally envy how much free time that gives her on Wednesdays and Fridays, but seeing how worn out she gets after running around to class all day Tuesday and Thursday?" 

   "No thanks, I'll stick to my more balanced schedule." 

   "She's also way better than me at getting her homework done well ahead of time. Though that's probably my fault, for spending so much time out wandering, trying to find out more about the curse on the school." 

   v "A personal project, then?" 

   n "You could say that." 

   "She sounds sort of frustrated--more than I can remember hearing from her before."

   v "I'll let you get back to it, then. Sorry for interrupting." 

   n "No, it's fine."

   "She leans back in her chair and sighs, rubbing at her forehead." 

   n "I haven't made hardly any progress all day, anyway." 

   v "You've been working on this all day?" 

   "I saw her at Magical Fields today, so I know she'd at least broken away to attend that. But that was only ten to noon; she's almost always up long before I woke up, and it's almost 5 now."

   v "You have eaten, right?" 

   "I grabbed lunch at the cafeteria, using all the extra time I had to pore over my Cursebreaking text for the quiz that Professor Reynell had given in the first part of class." 

   "(Which, as far as I can tell, I aced. Another reason today's class was great!)" 

   "I hadn't seen Nora at the cafeteria, but that could just mean that I hadn't been paying enough attention." 

   n amused "Yes, mother, I did." 

   "She gestures towards the corner of the room near the door, where our trash cans live--one each for food scraps, easily recyclable material, and everything else, with a tray to the side for dishes and silverware." 

   "All of them are spelled to transport their contents to the appropriate locations. I know that food scraps go to the Botany greenhouses, and the dish tray back to the cafeteria, but I'd never bothered to ask about the other two." 

   "The transport spell can be invoked manually, but it's a somewhat complex and intensive spell. I wanted a nap after the first time I tried to cast it."
   
   "So since we very rarely fill any of them more than half full, much less full enough to need to do a mid-week empty, most of the time we just let them do their weekly auto-invocation. (Daily for the dish tray.) Generally that happens sometime either late at night Sunday or early in the morning Monday." 

   "I've never seen it, although Nora's also sometimes up later than me, so maybe she has." 

   "And right now, although the cans aren't full enough for me to see into them, I can clearly see a plate and silverware stacked in the dish tray." 

   v "Sorry, I guess that did kind of come off as patronizing, didn't it?" 

   n "Haha, no, it's a reasonable question. I have been known to forget to eat in the past, so a reminder never hurts."

   v "What are you working on? If you don't mind me asking." 

   n normal "It's not all that interesting, honestly. Just something my mom asked if I could look into, the last time we chatted." 

   v "Something for the shop?" 

   n happy "Not one of our production models, thankfully. But it's something I'd been working on before I got here--Mom said she'd take the project over if she had time, since she wants me to be able to concentrate on my studies, but she hasn't been able to make much progress either."

   "It's on the tip of my tongue to ask if it does interfere, but I stop myself." 

   "First, because it's just more mother-henning, and I know how much I hate it when other people try to tell me what to do, or act like I don't know my own mind perfectly well." 

   "And second, because...who am I kidding? Whenever I see Nora, she's always working on something. And she's always ahead on me when it comes to homework for the classes we share. She clearly has her studies well under control." 

   v "Is it a new kind of phone?--Um, feel free not to tell me if it's a secret or something like that." 

   n "Haha! No, it's fine. We sell familiar-phone combos because a lot of people like the convenience, but we don't do a whole lot of work with the underlying hardware. Mostly just integrating the familiars in, and providing some additional helpful software." 

   v "Like the textbook visualization you and Perrault have been working on?" 

   n "Yes, exactly! Which reminds me, I need to get back to that, too. I still can't figure out how to keep the pages from feeling furry." 

   n normal "Anyway. This is another little add-on utility--or hopefully will be, eventually." 

   "She gestures me over, and lifts the device slightly, pressing a button that causes paragraphs of nonsense text to appear in mid-air. If I look more closely at the device, it's got a screen about the same size and shape as my smartphone, currently displaying the same set of text." 

   n "We get a lot of different variety in our clientele, as you might imagine.  Plenty of young children, coming in to get their first familiar. Those are always fun--their wide-eyed awe at the process kind of...reminds me just how magical this all is, you know?" 

   "I nod. I barely remember the circumstances surrounding when I got my first smartphone, but a few things remain, and the glorious flash of green and gold scales as Olly manifested for the first time in front of me is definitely one of them." 

   n "Then there's a lot of people looking to upgrade their hardware. Technically they can buy the new phones from the manufacturer's stores directly, and they should be able to transfer the familiars without any problem." 

   n "But not everyone trusts that, and especially with people who've bought our other add-ons--we guarantee free replacements for anything that gets broken unexpectedly by an upgrade, but in those cases it's often easier on both them and us to just let us do the entire upgrade." 

   n "And then there are our oldest customers, who've had the same familiar for decades, but can no longer see or hear them as well anymore--or the phone, either. Those break my heart the most." 

   "I nod again. My grandparents are still alive and in good health, my grandmather happily telling my father all the things she would be doing differently if she was still in charge of the family." 

   "(One minor side benefit to proving Eliza's innocence: I won't have to deal with my dad doing the exact same thing, when he decides it's time to retire and hand down the reins.  Because I already know that he absolutely will.)" 

   "But my great-grandmother passed away a year or two after everything happened with Eliza, and her sight and hearing were both almost entirely gone by that point."

   "When Eliza and I went to visit her, she'd always ask us to reassure her that her familiar was still there, and to tell him that she still appreciated him. Because most of the time, she could still tell he was there. But sometimes...she couldn't." 

   n "Sometimes, they're just not aware of existing smartphone functionality, so we can help them connect their familiar to the screenreading software, so their familiar can more easily read to them what's happening on the phone." 

   n "But most existing smartphones have pretty simplistic software in that respect, so we've been trying to see if we can come up with a suite of tools that we can provide that'll make these things easier." 

   n "Like this? As you can see, I've lifted the text from the screen into mid-air, so that you don't have to squint down at the phone, which helps some people. But the real thing I'm working on is..." 

   "She pinches two of her fingers over one of the sentences, and then spreads them apart."

   "First the text increases in size, until only a few words at a time show up in each row. Then the roughly phone-sized patch of air abruptly expands to two, three times its previous size, but the text shrinks back down to normal." 

   "And then it all disappears. Nora sighs, but she doesn't look terribly surprised." 

   n "...As you can see, it's very much still a work in progress." 
   
   show o normal at right

   o "Fascinating." 

   "I jump. I hadn't noticed that Olly had left the immediate confines of the phone to come hover at my shoulder, spectral claws digging into my shirt in a way that thankfully would not leave any real holes." 

   o "You're combining text zoom, screen projection, and screen expansion?" 
   
   hide o

   n "Yes, exactly. Most newer phones support all three, but they're not well-integrated with each other. Or at all, really. So I want to build an application that will allow controlling all three in a smooth fashion." 
   
   show p normal at right

   p "And not just with gestures, either." 
   
   hide p

   n "Right--once I have it integrated, we can make it a familiar command, too, so that our older customers, or customers with limited eyesight, can just ask their familiars to zoom text for them." 

   n "I've mostly been working with gestures so far, because I figure that's less annoying than hearing me say 'Perrault, special zoom' over and over." 

   v happy "I appreciate the consideration, though as long as I'm not trying to sleep, I'm pretty good at tuning that sort of thing out." 

   v "And that's really cool. I'm sure my great-grandmother would have loved to have something like that. She used to love reading, before her eyesight got too bad." 

   v "I assume you're working on something for people who are hard-of-hearing, too?" 

   n "I guess it's pretty obvious, huh? Yes, that's what I'd like to try to build something for next." 

   n "Most people like to keep their familiars at a normal conversational volume or lower, because it's just polite, you know? But I've been looking through some of the documentation, and it looks like there are ways to make it so that you're the only one who can hear your familiar." 

   n "So if we were to combine that with a big volume boost, or with adjustable pitch, people who still have some hearing will be able to still hear their familiar talking to them without feeling like they're inconveniencing everyone else." 

   "Nora suddenly pauses her explanation, looking a bit hesitant." 

   n "Sorry, I'm boring you, aren't I? I tend to go on and on about things I like, if given an excuse, as you may have noticed." 

   n "You can tell me to stop if you ever want me to. I promise I won't be offended." 

   v happy "No, you're not boring me at all! I obviously don't know all that much about artificing, so I have no idea how you'd go about doing...all the things you're describing. But you're really good at saying things in a way I can follow." 

   v "And all the things you've been working on--they seem really neat and really useful. I'm incredibly impressed that you somehow manage to find time to do all that and your schoolwork, though." 

   "To be honest--if I hadn't already been so focused on cursebreaking, for a variety of reasons, knowing Nora might have made me seriously consider switching my major to Artificing."

   "I hadn't ever really thought much about how my phone and Olly did the things they did, and what sort of things they might be able to do instead, but. Listening to Nora speak kind of made me want to learn." 

   n embarrassed "Thanks. I like to think that what I'm doing will be helpful to people, but sometimes I get so caught up in the problem-solving aspects that it can be hard to see."

   v normal "I'm still really looking forward to trying out the textbook-reading app, once that's ready, too." 
   
   show o normal at right

   o "Yeah, me too!" 
   
   hide o

   n "Thanks, both of you." 

   v "Just, make sure you take care of yourself, too?" 

   n happy "I will." 

   # 2.? Viola and Shouhei have an encounter, it's a bit awkward.

   $spoints += 1
   
   scene bg outdoors
   
   "I can't believe it. I thought by now I would have had a handle on the quickest routes to my classes."
   
   "But what with the surfing elephants fiasco blocking some of the dorm exits--all illusions, thanks to some mischievious first-year Enchantment students, I'm running late to class."
   
   "To my Magical Law and History class, to be exact. It's still--a bit heavy on the timeline charts and names sometimes."
   
   "And yes, I did have a basic grounding in it, thanks to the nannies we had, but when we were kids, running outside exploring trees and secret rooms was way more appealing than going through centuries of famous figures and old court transcripts."
   
   "Nora has been pretty helpful. She knows more about the modern laws and up-to-date inventors than the early bits, and it's better to have a study buddy to review with anyways."
   
   "Professor Prasad did promise a much more exciting lesson today. Something about how the rise of the law came about after catastrophic overlapping curses were cast on rulers during periods of power struggles?"
   
   "Agh! It would take too long for me to get to class from here on foot. If only--"
   
   #show swan boat at center
   
   "The boats."
   
   "Of course."
   
   "Many years ago, the early campus was founded in a heavily forested area. Plenty of rivers running around. The professors didn't want too many magical teleportation accidents, so to let the students to travel quickly from class to class, the boats were set up."
    
   "They say the first boats used to be pulled by actual swans, but not anymore. I suppose the swans had other things they would rather be doing."
   
   "The boat is still swan-shaped though. The head and beak is gracefully sculpted, and the wings are arched high to block out the sun and rain from students' heads. I don't remember exactly how the boats keep moving and know how to start or dock without any obvious instructions."
   
   "I must have missed hearing that at the tour at the beginning of the year."
   
   "The swan boat drifts closer to shore and stops. The wing swings open."
   
   "I jump forward, and slide into a seat, relieved that I wouldn't have to run to class. The door clicks shut behind me."
   
   "A sound of water rippling as the boat meanders away from shore."
   
   "I wipe my hand over my face, and look up. To the back is a little shelf for student's bags. To the front, a shimmering image is floating as a silvery hologram of a structure. It looks like the boat is floating past one of the buildings for Cursebreaking exams."
   
   "And to my right--"
   
   show s normal
   
   "I see Shouhei."
   
   s "..."
   
   "I turn my head slowly to the left, to peek through window carved--no, combined--with the wing. The boat is clearly already in the middle of the river."
    
   "The space feels small. Even if the boat was meant to carry up to 4 students, Shouhei and I are the only ones in here right now."
   
   hide s
   
   "I don't see Kinuko around either. She must be resting in a holding space, or flying around outside."
   
   "A sound seems to echo in our space as Shouhei shifts to lean an elbow against one side of the boat."
   
   "I can't see his expression. I don't know what to say."
   
   "Too many words to choose from, too many choices to make. Should I say something?"
   
   v "So, why are you going this way?"
   
   "It sounds ridiculous after the question leaves my mouth. Why doesn't magic have an undo button?"
   
   show s normal 
   
   s "To Magical Law & History class."
   
   v "That's--"
   
   s "The same class as you. Yes."
   
   "He looks back to his side of the window, and doesn't seem to want to say much more. He did answer me with a whole sentence at least."
   
   hide s
   
   "That's a little better than I expected."
   
   "The image at the front shifts into a familiar sight of the Magical Law & History building, with its high archway and cornices."
   
   s "We're here."
   
   "He gets his bag, and gets out first."
   
   "I stand too. My knees feel stiffer than they should be after that short ride. I must have been sitting too tensely."
   
   "I grab my bag, and take a step out--"
   
   "My foot catches against the edge of the boat and my balance is wobbling--"
   
   "A hand catches my wrist before I fall onto my face."
   
   s "Watch it!"
   
   "I breathe in. His hand is still holding mine and my pulse is still going fast. I pull away, take two steps farther from him. Solid ground."
   
   v "Thanks. We should go."
   
   show s sad
   
   "I see Shouhei's lips press together, before his hand goes to his glasses, steadying them."
   
   s "Fine."
   
   v "Fine."
   
   hide s
   
   "Talking like this is fine. We can talk normally, can't we? Act like any two normal students would act?"
   
   "We were just heading to the same class today. This...will probably happen again, won't it? I won't be unprepared, next time." 
   
   # 2.? Possibly a scene about other NPCs having fun playing with magic?

   scene bg outdoors

   "I'm walking home from a study session at the library--it doesn't seem fair to lean on Nora to help me figure out Magical Law all the time--when I catch sight of a familiar figure up ahead."

   v normal "Colin, hey!" 

   "Happily for my stamina, he hears me, and stops to wait for me to catch up."

   c normal "Viola! It's been a while. Heading home from class?"

   v "No, I was just studying at the library. How about you?"

   c "Just heading home from Calc. I'm not looking forward to this week's problem set."

   v "I'm glad I managed to skip out on math completely, to be honest. Does your major require it? Nora was mentioning that Artificing does."

   c "I...haven't declared a major yet, actually. So I figured I should get as many of the general education requirements out of the way as I can, while I'm making up my mind."

   v "That makes sense. Do you have any ideas about what you might want to pick? Types of magic you're interested in?"

   c "Hmm, not really. I like a little bit of almost everything, to be honest."

   "Sudden shouting draws my attention--and Colin's too, by the way he stiffens. We exchange a concerned look, and run in the direction of the shouting."

   "We turn the corner around a building, and I skid to a stop."

   "There's a giant--plant, I guess? It's at least very large and very green, waving around some knobby, ropey-looking tentacles that look sort of like roots."

   "And it looks like it's standing on someone! Though from the expletives they're shouting, they sound more angry than injured."

   s1 "Would you get this thing off me?! This is not funny anymore!"

   s2 "It wasn't supposed to do that! I'm not sure how to make it stop!"

   # 2.?? More on Viola and her major 

   $npoints += 1

   "It turns out that Professor Reynell really likes mystery boxes." 

   "And while I really enjoyed the first several he assigned to us, well. almost three months into the semester, they've gotten a lot harder to unravel, and the consequences for not doing so rather more...interesting." 

   n "...Should I ask why you're sitting on the ceiling?" 

   scene bg v dorm
   
   # can we flip Viola's sprite upside down in the scene? That would be hilarious and appropriate
   show v upside down: 
      xalign 0.5
      yalign 0.05

   v "Cursebreaking homework." 

   n laughing "Again?" 

   "I suppose it's not the first or even the worst thing she's seen happen to me as a result of making a mistake with one of these boxes. The day I spent with my skin glowing slowly rotating shades of purple was just embarrassing." 

   "Though at least most of my other classmates ended up looking the same way." 

   n normal "Want me to toss you the box?" 

   v "Yes please! I accidentally dropped it a few minutes ago, and I'm getting bored, to be honest." 

   n "Here you go." 

   "At first, when I had...mishaps, I'd been reluctant to let Nora touch the box. Luckily, it seems that Professor Reynell isn't completely sadistic--the traps all appear to have been set to only react when interacted with by someone from the class." 

   n "Should I be stacking pillows beneath you or something?" 

   v "No, it's fine--there's a height limit, and apparently when it wears off we drift slowly back down." 

   "No one's box is quite the same, but the traps tend to be more similar than the solutions to the puzzles, so pretty early on in the class, most of us had set up a group chat where we can share warnings and tips with each other. If Professor Reynell knows, she clearly doesn't mind." 

   n "...Your homework is a lot more exciting than mine." 

   v laughing "Only if I do it wrong." 

   n happy "I'm glad you're having fun?" 

   v "I mean, you have to admit, being stuck to the ceiling is pretty cool, aside from the inconvenience of being unable to go anywhere." 

   n "I'll stick to the ground, thanks." 

   n normal "You know--it occurs to me, I've never really asked before--why did you choose Cursebreaking? Is this really that interesting to you?" 

   "I hesitate. I'm not sure I'm ready to share the full reason. I don't want Nora to start thinking I'm some sort of conspiracy theory-chasing nut."
   
   "But there are some things I can say." 

   v "Yeah, it is. I guess it started when I was younger--my nurse liked telling tales of valor and cunning that often involved the protagonist having to solve some riddle or break through some lock, and it...always seemed like real magic to me, you know?"

   v "I dragged Liam and--well, my friends at the time, into so much trouble, running around our property trying to find puzzles to solve and treasure to rescue."

   n amused "Did you ever find any?"

   v "We did! Not always, and sometimes the puzzles were too hard and we had to come back and try again. One took us an entire month of adventures before--we finally cracked it."

   "It had been Shouhei who'd had the idea to send Kinuko up into the tops of the trees to see if there was anything up there that we were missing."

   "And the clue had been right there, clear as day."

   "Maybe I shouldn't have started talking at all. It's been so long since I've talked about those times that I sometimes forget just how full of painful reminders even the happy memories are."

   n "That's really cool. Are most old houses like that? Making sure the coming generations are worthy by starting their training while they're young?"

   "I get the feeling that she's teasing me. Though, to be fair, I wouldn't put it past some of the really proud old houses to do just that."

   v amused "Sadly, no. At the time, of course, we just thought they magically appeared, but later, my s--"

   "I stop. More than anything, I don't want to make this about what other people think about Eliza right now."

   "Nora lets the silence lie for a moment, clearly trying to figure out something to say. I guess even without saying it, it's pretty obvious who and what I meant."

   "I scramble to come up with something else to say. Anything else, to change the topic. But my mind is empty of everything except the nostalgia and the pain." 

   n "That was a really nice thing for your sister to do for you and your friends."

   "I wait, expecting something more. Incredulity, that a murderer could be kind to her kid sister. Or anything, really, commenting on who--and where--Eliza is now."

   "But Nora doesn't say anything else, just waits patiently to see if I'll pick the story back up where I left off."

   "Smiling hurts, too, but I do it anyway." 

   v happy "It was."

   v normal "Solving the puzzles was fun, but the best part was the stories we made up about the process. I guess it sounds childish now, but we were always gallant knights, seeking out the cure for our prince's terrible ailment."

   v "Or princes and princesses, whose parents had been trapped by a terrible curse that only we could fix."

   n happy "My brother and I used to play games like that, too. Although ours usually involved fewer puzzles and more monsters to defeat."

   v happy "We did some of that too, when we were in larger groups. But Liam's mom would worry over us if we accidentally injured each other, so we mostly stuck to the puzzles that we liked more anyway, when we were alone."

   v normal "And I guess it stuck with me?"

   v "In old myths and legends, sometimes the curse is inflicted on someone who deserves it, and they have to overcome it themselves, by learning an important lesson about life that they'd missed. Professor Reynell calls those Inward-Oriented Curses."

   v "But most curses--Outward-Oriented Curses--are a lot more indiscriminate than that. They'll just attack anyone who's conveniently in range, or they'll have been badly built to begin with, and cause a lot more damage to more people that the caster originally intended."

   v "And that just seems wrong to me, you know? People shouldn't have to worry about being struck down by something they can't see coming, just because they happen to have the wrong ancestor or say the wrong thing in the wrong place."

   v "So I really like solving puzzles, but I think even more than that, I like having the knowledge that by deconstructing some curse, I'm making the world a little bit safer."

   v "And if the person who originally set the curse has a problem with that, well, that's their problem. And maybe next time they'll go after the person they're actually mad at, instead of randomly hurting anyone who might be in the way."

   "I don't know who put the school curse in place. I don't know why. I don't even really know the details of what it does, since the legends are frustratingly long on poetry and short on concrete details."

   "But I refuse to believe that Eliza deserved what happened to her. That Mariko deserved to die, by whoever's hand did the deed."

   "I don't even care that the curse has done well for some people. I've always thought that being on the curse's 'good side' meant you hadn't really earned what it gave you, anyway."

   "I just really want it gone, so it can't hurt anyone like it hurt my sister, ever again."

   n "I think that's really admirable."

   "I wonder if she'd say the same, if she knew how much anger I carried with me, and how personal my vendetta against the school curse in particular is."

   v "Haha, thanks? I don't think I'd do it if I didn't also really like solving puzzles, though. I'm not that good of a person."

   n "Does that really matter? I wouldn't do all this if I didn't really love fiddling with phone programming, either."

   "Her gesture takes in the array of projects scattered across her desk." 
   
   "After a month and a half of rooming together, it's kind of neat to realize that I recognize and can describe in at least basic terms what most of them do."

   v "I guess so. It's not as altruistic as playing knights and princesses, though."

   n "Was that really altruism either? You said that you were generally trying to cure or save a loved one, or someone you felt beholden to. And I think it's entirely reasonable to want your loved ones to be safe and happy."

   v "Heh. True."

   "I wonder if she'd say the same if she knew about Eliza, and how convinced I am that she's innocent."

   "It's funny, though, to consider that in some ways, I guess I am just re-enacting our childhood games all over again. Just with Eliza in the role of cursed princess this time."

   "I hope I'm as successful at unraveling this puzzle as we were (eventually) at solving the ones she prepared for us."

   v "Speaking of solving puzzles, I probably ought to go ahead and try to solve this one."

   n laughing "I guess you should. I don't think you'd do too well trying to eat up there, and it's almost dinner time."

   v happy "I don't really want to sleep up here, either. The ceiling's not that comfortable."

   n "Want me to throw you a pillow to sit on?"

   v "Ask me again if I'm still up here in an hour."

   "Heart a little bit lighter, I turn back to the box."
   
   hide v

   # 2.? Kinuko seeks out Liam and Viola 
   
   show l normal
   
   l "...and that's why that particular town developed a tradition of wearing hats with a chicken sitting on it."
   
   v normal "...You're serious."
   
   l "They might always be under fowl weather, but they sure do sell delicious meringues."
   
   l "That's what Mom said in her letter, anyways. She was trying to see if she could ship us some in the mail."
   
   "I want to swat at Liam for the pun, but I don't have the energy."
   
   "There's a light misty haze in the air, the clouds curling close to each other. We had been studying for a little while, but were taking a break."
   
   "Just a brief one."
   
   "Okay, maybe not that brief. We were both wearing warmer clothes--a long-sleeved hoodie for Liam, a jacket for myself--for the weather. The afternoon had been cool and languid."
   
   "I sit up, the grass underneath me shifting. There, in the distance, a faint white shape. Was that--?"
   
   play sound magiceffect
   
   show k normal at right
   
   "Why was she here?"
   
   "I'm standing on my feet, before I remember even getting up. A vague dread spills over me like ice. Was Shouhei--?"
   
   k "He wants to see you."
   
   k "The two of you."
   
   "I sense Liam has stood up too, just right behind my shoulder. I breathe out, more slowly."
   
   l "Did he say why?"
   
   "Kinuko doesn't shrug, not exactly. She lifts a wing up, then brings it down, a subtle arc of feathers."
   
   k "He had a message."
   
   "I look back at Liam, and our eyes meet once. He nods, almost encouragingly."
   
   play sound magiceffect
   
   hide k
   hide l
   
   "Kinuko has already taken off. She's expecting us to follow her, then. Liam and I take two seconds to grab our bags, and jog on."
   
   "We move from the grassy area just outside the library. I keep my eyes on Kinuko, her glowing winged shape tracing a soft line into the mist."
   
   play sound forest
   
   "The area in front of us gives way from fields to a denser wood. We pass spruce and maple, hemlock and white ash. Leaves go about their quiet business of falling."
   
   "There's the smell of dried flowers, mosses, and damp earth from beneath our feet. Things that have grown and withered. At some point on our walk, Olly and Clara have slipped out of their phones."
 
   "They haven't said anything yet. But Olly hovering next to my right elbow is a comforting thought."
   
   "Oh. Kinuko has stopped."
   
   s "Thank you, Kinuko."
   
   show s normal at right
   
   s "You both came."
   
   show l normal at left
   
   l "Hello, Shouhei."
   
   l "Of course we did."
   
   "Liam's voice is still friendly. Just about managing to edge up to cheerful. I don't think mine is, though."
   
   v "My question is why."
   
   "Look, it's a fair question."
   
   s "..."
   
   s "Just a request, if you would hear me out."
   
   v "We're here already. Can you get to it?"
   
   "It's shadowy in these woods. Shouhei's face, even while it is in front of me, is even harder to read."
   
   s "I was impolite last time, in my wording. I just wanted to be clearer, between all of us."
   
   s "We may be at the same school, now."
   
   s "But I don't want us to get in each other's way. That might be better, just for all of us."
   
   l angry "Which means what."
   
   "His voice has lost the 'cheerful' and just got to all 'edge' now."
   
   hide l
   hide s
   
   "I can't help remembering the times when Kinuko would come find us, just like this, when we were smaller. We don't look the same as we did then."
   
   "This is all. Backwards. Like players acting in costumes two sizes too small for them, in a scene they once knew well."
   
   "I get his point, even if it does hurt. What can I even say now?"

   menu: 

      "Fine. Come on, Liam, let's go.":
         $lpoints += 1
         jump liam4

      "Hey, can I talk to you for a minute first?":
         $spoints += 1
         jump shouhei3
        
        
label liam4:

   v normal "Fine."
   
   v "I get it. I get what you're saying. Come on, Liam. Let's go."
   
   show l normal at left
   show s normal at right
   
   l "Viola, what--"
   
   v "Shouhei. Thank you for your honesty, this time. You don't have to worry too much about it."
   
   v "We'll see you around in class."
   
   "Shouhei's eyes look up, just to meet with mine. He nods once, slowly and then steps back. Steps away from us."
   
   s "All right. I have to get somewhere soon."
   
   hide s
   
   "This is it, then. I turn around, and start walking, one step, one more, and another, away from the forest."
   
   "My hand, somehow, has reached up to hold onto the elbow of Liam's sleeve. I feel a jerking motion, like Liam wants to tug away."
   
   v "Please. He's busy, and already said what he wanted to tell us."
   
   v "Please, Liam."
   
   "I'm sorry, just a little, that we couldn't talk more with Shouhei. More than a little."
   
   "I imagine if things had happened the other way around. No. I can't even think of it like that."
   
   "I feel just a bit relieved, beneath all that, to be absolutely honest. We know where we stand now."
   
   "I'll study Cursebreaking, Liam has his Healing, and Shouhei will learn what he came here to learn. We're not going to stay the same as we were when we were small."
   
   l "Viola."
   
   l "I'm sorry."
   
   v "It'll be okay."
   
   "On one side, Liam walks with me, nearly shoulder to shoulder. Olly, resting on my other side, almost pats my shoulder, or attempts to make the same motion with his tail."
   
   "I can't really quite feel it, but it does cheer me up just slightly."
   
   jump postforest

label shouhei3:
   
   show l normal at left
   show s normal at right
   
   v normal "Shouhei. Can I talk to you for a minute?"
   
   "I look back at Liam, who looks puzzled now. I mouth some words in the air, hold up one, two fingers, to let him know I would be back after a moment."
   
   "He seems to get it."
   
   "Shouhei looks taken aback. Kinuko has turned her head to study me intensely. Then her beak reaches forward, taps against Shouhei's wrist in a light motion."
   
   show o normal at center
   
   o "Viola, do you know what you'll say to him?"
   
   hide o
   
   "Good question, Olly. I'm wondering that myself."
   
   "We walk a little away from Liam, to between two giant pine trees. There's a clump of bluish-purple flowers blooming under one of them."
   
   s "So. What is it?"
   
   v "I understand, all right?"
   
   v "We all came here to study well. You're busy, you have things to do. So do I. And I get why you don't want to talk with me more than you need to."
   
   v "We can be polite to each other in class. Say hi, even, eventually."
   
   v "But for everything you just said, after all of it. I think you should talk to Liam."
   
   v "If you want to. And if he wants to talk to you."
   
   v "You're not. Not being very fair to him. He didn't actually have anything to do with...all of that. I know it. You know it."
   
   "Shouhei hasn't said anything while I'm speaking. When I look at him, he does look like he has been listening closely."

   s "Very well. I think."
   
   s "I think you may have a point."
   
   v "Okay. That's all I wanted to say."
   
   v "He would be happy, if you did want to talk to him again."
   
   s "Perhaps."
   
   "I don't think there's anything else I can say at this point. I should go."
   
   s "I'm..."
   
   "I can't really hear his next words after that, over the soft chirping of birds and shifting pine needles. I stop walking and turn my head."
   
   v "Yes?"
   
   s "You can make a left at the grove of maple trees on the way back instead of a right."
   
   s "The bridge there will get you to the classrooms faster."
   
   v "Thanks for the tip."
   
   hide s
   
   "I wander back, wondering if Shouhei will decide to talk to Liam again. Liam isn't really the type to hold onto a grudge against people."
   
   "I can't hope for much on that front. I decide not to worry too much about it now. There's lot of other things I have to think about, right now anyways."
   
label postforest:
   
   "Placeholder dialogue!"
  
   # 2.? Scene involving either Eliza or Viola's family contacting her, more family history? 

   ### MONTH THREE BEGINS ###

   # 3.? Worldbuilding / friendly interaction scene? Nods to alternate paths history took? 

   # 3.? Scene with Liam at the health center 

   $lpoints += 1

   # 3.? Encounter with Shouhei after reprimanding an NPC 
   
   scene bg school hallway
   
   "I look up from the textbook I had been skimming through. Now where did I end up walking to?"
   
   "I'm standing on some type of second-story platform, a winding bridge-like thing overlooking part of the campus. There's a hallway with a row of doors to my right."
   
   "Project Room 1. Project Room 2. Project Room 3. And so it goes, with each door further down."

   "Huh. I think I can guess what's inside each one."
   
   "It's quieter around this side of the campus. The sky overhead is melting into dusky blues and purples. Most people must be at one of the dining halls now, or eating at one of the food stands near the dorms."
   
   "I should figure out where I am and head back to the dorms. Nora or Liam or somebody could tell me what the best dinner special was today."
   
   v "What's that?"
   
   "I don't know why, but I just take a step back from the hallway, so my right shoulder is resting against the wall. I shift to look around the corner."
   
   "Footsteps. Someone slips up to one of the doors. I don't get a good look. Male, I think. Middling height."
   
   v "He doesn't look like a teacher."
   
   "The figure bends close to one of the doors. He whispers something, and there's a clicking noise. A burnt smell wafts through the air."
   
   "He looks down one way of the hallway, then the other side. And goes inside the room."
   
   "Hmm. Curious."
   
   menu: 

      "Walk downstairs.":
       jump walkaway

      "Follow him.":
         $spoints += 1
         jump shouhei4
         
label walkaway:

   "Some people seem to do their work best at odd times. And I guess he preferred a time with more privacy for his research."
   
   "Anyways, I don't really have a reason to stick around here."
   
   "It takes me some time looping around two sets of stairs, but eventually I find my way back to the dorms and get dinner."
   
   "I'll think about my Cursebreaking assignment from today after that. Food first." 
   
   jump schoolcursediscuss
   
label shouhei4:

   v "That's...definitely not normal behavior."
   
   "I run down the hallway, right up to the room he had gone into."
   
   play sound dooropen
   
   scene bg school lab
   
   v angry "What are you doing?"
   
   s1 "What?"
   
   show kc at right
   
   "The student has an unlabeled green bottle of something in his hand."
   
   "His other hand holds a clear glass flask, with several yellow butteflies fluttering inside."
   
   show v at center
   
   v "Are you supposed to be here?"
   
   s1 "Who are you?"
   
   "I look over at the little signpost on the right side of the wall next to the door."
   
   "There's a name labeled there and a set of dates that the project room is booked for."
   
   v "Unless your name is Camellia, I think you should leave."
   
   s1 "It's none of your business what I'm doing."
   
   "The student's hair is a faint blonde shade, with a grayer tint to it than Liam's. He's wearing a cream-colored sweater and navy slacks."
   
   "He's not wearing any of the safety aprons or gloves that most students are reminded to wear when handling projects."
   
   v "You want to rethink this and go, before you get in trouble?"
   
   s1 "No."
   
   "He flicks off the lid of the green bottle and moves it towards the flask."
   
   v "Stop!"
   
   "I rush up and grab his hand."
   
   s1 "Oh, give up!"
   
   show bg school lab with hpunch 
   
   "A jolt to my side, and a shove. I almost lose my footing."
   
   "My elbow bangs onto something hard. I grit my teeth."
   
   "I have to think. I have been getting some physical strength training in our Cursebreaking classes. But I don't know how good I would be in a hand-to-hand fight."
   
   v "Olly! Go get someone! Hurry!"
   
   "My phone vibrates in my pocket. The familiar sound of something whooshing out."
   
   show o at left
   
   o "Viola! What...?"
   
   v "Just go!"
   
   hide o
   
   "I hope Olly listens this time."
   
   show bg school lab with hpunch   #i want to make this effect last at least 3 seconds long how do i add that
  
   "The student and I are still grappling. I'm trying to get to the bottle he's holding, and he's still trying to push me away."
   
   "I've managed somehow to get him towards the doorframe, pressing one of his arms against the wall. Maybe I can pull him away from the project."
   
   "His arm flails. I see a greenish blur coming towards me and I duck. But not quick enough."
   
   "Whatever it is collides into me with a thunk, and my jaw rattles."
   
   hide v
   
   "The student mutters something panickedly."
   
   play sound crash
   
   "And then, a crash."
   
   "I jump away instinctively."
   
   "There's glass on the ground. The student and I stop. We stare at the mess."
   
   "The flask had broken apart. Around us, two, three, and more butterflies released from the flask are floating around the room, glowing faintly."
   
   v "You. You broke her research."
   
   s1 "...I didn't."
   
   "His eyes dart around the room. Then he leaps towards the door."
   
   v "Hey! You can't tamper with someone's project and just leave!"
   
   "How would I explain this mess? It looks. Bad. It would be bad."
   
   s "She's right about that."
   
   "The student doesn't make it out the door."
   
   "Shouhei's there."
   
   show s angry at left
   
   s "Crossley. Ken Crossley, wasn't it?"
   
   s "You dropped out of one of the courses we both had, ah, about a week ago?"
   
   kc "This is annoying. I didn't plan to break anything! This girl here just doesn't know when to leave something alone!"
   
   kc "It was just a prank, that was all."
   
   s "Damaging school property? Intefering with a fellow student's research? Injuring another student?"
   
   show s at center
   
   s "All for a simple prank, according to you? I've already told a professor there was trouble here."
   
   s "And if you don't want to inform the student council what you did, that's fine. I can go put in the report myself."
   
   "The student, Ken, is looking less angry now. And much more worried."
   
   kc "Fine! Fine, I'll go report it myself. Just my bad luck today."
   
   "He places the green bottle he was holding down on the nearby table. Shoots one last glare at Shouhei and me, and leaves."
   
   hide kc
   
   v "What a mess. I didn't even know what he was thinking."
   
   s "That was a bad idea, running into here."
   
   v "I wasn't the one sneaking around doing something bad!" 
   
   s normal "Fine. You had a reason for doing what you did."
   
   s "And got hurt on top of that."
   
   v "Really."
   
   "Shouhei, looking uncomfortable, lifts one of his hands to touch his cheek."
   
   "I mirror his action. Oh. Ow."
   
   v "It's not bleeding?"
   
   "Shouhei turns from the door. Takes one step, two steps closer to me, his eyes glancing over my face."
   
   hide s
   show s normal at center:
      zoom 1.0
      linear 1.0 zoom 1.15
   
   "He shakes his head."
   
   "That side, the spot against my cheekbone that I'm touching, aches fiercely."
   
   v "And for what happened here..."
   
   s "I told you, I informed one of the professors already. You better go to the health center. Get that checked on."
   
   v "Right. I'll go."
   
   hide s
   
   "I walk out and Olly floats next to me, hovering, the rest of the way to the health center."
   
   "Yeah. I'll have an exciting explanation for this the next time I see Nora. Or Liam. Whoever sees me first."
   
   jump schoolcursediscuss

   if persistent.colin_route_unlocked: 

      # 3.? People practicing spellcasting with their familiars; Colin admits he doesn't have one. 

      $cpoints += 1
      
label schoolcursediscuss:

   # 3.? More detailed discussion of the school curse.

   # 3.? "What would you do if you got the school curse?"

   v "Placeholder text for this scene here."

   v "Characters are asked what they'd do if they got the school curse."

   menu:

      "Ask Colin first" if persistent.colin_route_unlocked == True:
         $cpoints += 1
         
         "Some thoughts about why she's picking Colin."

         jump postpick

      "Ask Nora first":
         $npoints += 1
         
         "Some thoughts about why she's picking Nora."

         jump postpick

      "Ask Shouhei first":
         $spoints += 1
         
         "Some thoughts about why she's picking Shouhei."

         jump postpick

label postpick: 

   # 3.? More detailed discussion of the break between Viola and Shouhei's families.

   scene bg mf_class

   # 3.? Group project partners announced in Magical Fields

   # background crowd noise sound? 

   "The last Magical Fields class of the semester."

   "We're finally going to learn who our partner is for next semester's group project. In my excitement, I made a point of arriving early, and looking around, it looks like I wasn't alone."

   "Five minutes to the start of class, and the room is almost full already."

   pm "So punctual! It's almost like you think something interesting is happening today."

   s1 "There's always something interesting happening in your class, Professor!" 

   "I share an amused glance with Liam. He's not entirely wrong, though I admit I'm surprised that he hasn't figured out by now that Professor Marquez doesn't care about brown-nosing."

   pm "Good try, but your partners have already been decided."

   "They hold up the sheaf of papers that they'd brought into the room with them. I hadn't paid it much attention, since they're often carrying papers or occasionally a small bound notebook. But this particular stack does look larger than usual." 

   pm "Speaking of, I assume that's what you're all here to find out, yes?"

   pm "First, a few ground rules."

   pm "Please wait until I'm finished announcing all of the groups before doing anything. Afterwards, you can go say hi to your new partner, and start discussing ideas for your projects."

   pm "If you absolutely must appeal to me to change your assigned group, please wait until after the announcements to do that as well."

   pm "I prefer if appeals are presented to me in written form, and placed in the proper receptacle."

   "They gesture to the small trash can by their desk, as a handful of the other students stifle snickers."

   pm "Everyone understand? Good."

   pm "First group: Aguilar, you're with Cohen."

   "I'm tempted to zone out, but I force myself to keep paying attention. If Professor Marquez is giving out assignments in alphabetical order, then my name should be coming up soon."

   "I just hope that my partner is someone I already know and get along with. It'll be pretty painful next semester if I have to work with someone I dislike."

   "Especially given how much else I want to do with my time, too. I already feel like I haven't made enough progress this semester; I really need to buckle down and focus in January."

   pm "Allen, you're with Williams."

   "I tense. I should be next."

   pm "Ashmark, you're with ..."

   if persistent.true_route_unlocked: 

      "Flynn, Galena, Thomas, and Utsurikawa."
      jump true_start
   
   elif cpoints > max(lpoints, max(npoints, spoints)) and persistent.colin_route_unlocked:

      "Flynn."
      jump colin_start

   elif lpoints > max(cpoints, max(npoints, spoints)): 

      "Thomas."
      jump liam_start
   
   elif npoints > max(cpoints, max(lpoints, spoints)): 

      "Galena."
      jump nora_start

   elif spoints max(cpoints, max(lpoints, npoints)): 

      "Utsurikawa."
      jump shouhei_start

   else:

      "ERROR: we should never get here. C: [cpoints] L: [lpoints] N: [npoints] S: [spoints]"

   return
