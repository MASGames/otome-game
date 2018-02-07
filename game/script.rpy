define v = Character("Viola")
define n = Character("Nora")
define l = Character("Liam")
define c = Character("Connor")
define p1 = Character("Professor") 

label start:
   scene bg 1
   
   "Wyderwold University.  The premier magic college in the United States. Members of my family have attended for generations, and I've wanted to come, following in my brother's footsteps, since before I can remember."

   "Rumor has it that the school is afflicted with a very peculiar curse: that if you run across it, and you're lucky, you'll be marked for greatness, destined for a life of wealth and plenty."

   "If you're unlucky ..."

   "Well."

   "After what happened to my brother, to my whole family, I've wanted to come to this school even more."

   "So I can find the source of the curse, and end it. For good."

   scene bg 2

   show n normal at center

   n "Viola, are you about ready? It's almost time for (intro class TK) to start."

   show v normal at left # vspot

   v "Yes, I'll be right there!"

   "Nora (last name TK) is my roommate; we met last night while we were finishing moving in. She said she's planning on majoring in artificing – apparently her entire family are artificers"
   
   "That means that we'll have (intro class TK) and (artificing 101?) together. It'll be nice to know someone other than Liam in a few of my classes."

   v "Let's go! This is your first time on campus, right? Let's go by way of the gardens, I'll show you the way."

   n "As long as it doesn't make us late –"
 
   scene bg 3

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

   p1 "All right, class, it's nice you're all becoming such good friends, but we have things to learn, and we don't have all day to do it in. Everyone to their desks, please."

   "Nora's desk isn't too far away from mine. Unfortunately, Liam's halfway across the room, and Connor's off in the opposite corner."
