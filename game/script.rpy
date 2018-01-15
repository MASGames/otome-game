
# Define characters 
define v = Character("Viola")

label start:

   scene bg 1

   show v normal at left

   v "The game is starting? This is so exciting!"
   
   v "This is example text."
   
   hide v normal
   
   v "This is something Alex added."
   
   v "Another test line"

   v "Test line from Sara"

menu: 

   "Nora's route": 
      jump Nora

   "Finn's route":
      jump Finn

   "Liam's route":
      jump Liam

label Finn:

   "sample text"

   return
