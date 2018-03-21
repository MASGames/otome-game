define v = Character("Viola")
define n = Character("Nora")
define l = Character("Liam")
define c = Character("Connor")
define p1 = Character("Professor") 

label start:
   scene bg 1 # university birds-eye view 
   
   "Wyderwold University.  The premier magic college in the United States. Members of my family have attended for generations, and I've wanted to come, following in my brother's footsteps, since before I can remember."

   "Rumor has it that the school is afflicted with a very peculiar curse: that if you run across it, and you're lucky, you'll be marked for greatness, destined for a life of wealth and plenty."

   "If you're unlucky ..."

   "Well."

   "After what happened to my brother, to my whole family, I've wanted to come to this school even more."

   "So I can find the source of the curse, and end it. For good."

   # TODO: Add scene with Viola meeting Nora for the first time as they're moving in
   # - Liam's helping her move idk a chair, so they get their first introduction + some 
   #   implications that he's the osananajimi character
   # - Nora has some artificing equipment that Viola asks about, fleshing her character out some

   scene bg 2 # Nora and Viola's dorm room

   show n normal at center

   n "Viola, are you about ready? It's almost time for (intro class TK) to start."

   show v normal at left # vspot

   v "Yes, I'll be right there!"

   "Nora (last name TK) is my roommate; we met last night while we were finishing moving in. She said she's planning on majoring in artificing – apparently her entire family are artificers"
   
   "That means that we'll have (intro class TK) and (artificing 101?) together. It'll be nice to know someone other than Liam in a few of my classes."

   v "Let's go! This is your first time on campus, right? Let's go by way of the gardens, I'll show you the way."

   n "As long as it doesn't make us late –"
 
   scene bg 3 # Classroom 

   show v normal at left # vspot
   show n normal at center

   v "– And the first rose bush was originally donated by one of my ancestors, though it's at the center of the garden, so we didn't see it this time."
  
   n "Wow, that's, what – several hundred years ago?  And it still blooms?"

   show v normal at left # happy at vspot

   v "Magic."

   show n normal at center # TODO: laughing or should it just be happy?  
   
   n "Fair point."

   show l normal at left
   show n normal at right 
 
   l "Viola! Long time no see." 

   v "Oh yes, a whole 24 hours. Come on, come sit with us. This is Nora, my roommate. Nora, this is Liam -- we've been friends since we were ..."

   l "Infants?" 

   v "Close enough."

   l "Nice to meet you, Nora. This is my roommate, Connor."

   show c normal at left

   c "Nice to meet you, Viola, Nora."

   v "Watch out -- Liam bites."

   l "That was one time! We were five!"

   # TODO: characters laughing? 

   c "I'll keep an eye out."

   Nora waves again from her desk and leans over, about to say something when--

   [play sound “door opening”]

   ???: Sorry for being late, Professor.

   [show CG scene: Viola and Liam staring at the person standing in front of the door, nora and connor confused in background]

   [show shouhei at right]

   v “That person is--”

   p1 "Shouhei TKlastname, how nice of you to join us. Take a seat anywhere you like."

   v "The chatter in the room starts up again, but I can barely hear it. His eyes skim the room before they stop to look at--me? He doesn’t meet my glance though. His eyes flicker once to the other side of the room- to Liam? - before he moves forward past the lines of desks. He sits down, on the third seat in the middle column of chairs and takes out his books."

   n "Who is that?"

   Before I can answer, suddenly…

   [play sound “TK magic sound”]
   [show: kinuko, a crane familiar, flying through the window, at center]

   v "A crane appears, gracefully gliding through an open window to rest by Shouhei’s desk. A physical familiar. The whispers around me get louder. Physical familiars are not unknown, but rarer now than they once were.

   p1 "All right, class, it’s nice you’re all becoming such good friends, but we have things to learn, and we don’t have all day to do it in. Everyone back to their desks, please." 

   Nora’s desk isn’t too far away from mine. Unfortunately, Liam’s halfway across the room, and Connor’s off in the opposite corner. Shouhei is in the middle of the room.

   v "Shouhei. Neither I nor Liam have spoken to him since…it was a while ago. I shake off the thought. I can talk with Liam about this later. I turn to the board and Professor begins their lesson."

   p1 [TKsome magical canon facts stuff here, like 3 sentences]

   v "The chimes ring, signalling the end of the lesson. I stand and stretch, feeling stiff from sitting at the desk for so long. I pack up my bag and head towards the door with the rest of the class, before I almost trip on something."

   v "That looks like…"

   [show: TKbracelet, at the center]

   v "I pick up the bracelet from the floor. It looks a little familiar. Oh, right. Wasn’t Connor wearing this, when I first met him? It looks sort of expensive. If he dropped it, I probably should return it to him."

   [show: olly, viola’s familiar projecting from her phone at right]

   Olly "It’s lunchtime! Where are you going to go now?" 

   v "Most of the class has filed out already. Nora waved cheerfully to me as she left, Liam had dashed off to his after-class job. Connor looked like he was heading back to his room. Shouhei had left too, his familiar gliding behind him."

   I think I’ll go eat lunch at:

#TODO TK code these choices
Choice 1: The health center (to keep company with Liam)
Choice 2: The rose gardens (Nora)
Choice 3: The dorms (Connor)
Choice 4: The lake (Shouhei)
Choice 5: The cafeteria (common route- she gets food, talks more to Olly about her classes)

   # Next steps: 
   # - Shouhei dramatic entrance Viola and Liam exchange looks but can't actually say anything 
   # - he and Viola snipe at each other a bit before the professor takes contrl? 
   # 
   # After class: 
   # - Notice Connor's bracelet on the floor; decide to go after him to return it 
   # - Happen upon him explaining the curse to some other freshmen -- piques Viola's interest because 
   #   she really wants to know more about the curse
   # - Return the bracelet; he seems shocked to realize he lost it, is a bit overly effusive with his thanks

   return
   
