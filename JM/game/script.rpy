# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jamie", image ="j")
define m = Character("Marley", image ="m")

##### The game screen.
screen fifteen_scr:


    ##### Game field.
    frame:
        xalign 0.5 yalign 0.5
        background Solid("#ccc") #Frame("pic_1.png", 5, 5) # The background might be set as a solid color or a frame, that uses predefined displayable or file name, also you can delete this line to have default frame background.

        grid grid_width grid_height spacing 0:
            for every_tile in tiles_list:
                if every_tile["tile_value"] == empty_tile_value and not fifteen_is_solved:
                    null

                else:
                    button:
                        #####
                        #
                        # To use just numbers (classic fifteen game) - uncomment next 4 lines and comment out lines that are used to show an image.
                        # It is neccessary to set the size of buttons.
                        # (The background might be set as a solid color or a frame, that uses predefined displayable or file name, also you can delete this line to have default button background.)
                        #xminimum 70 xmaximum 70
                        #yminimum 70 ymaximum 70
                        #background Solid("#c00")
                        #text str(every_tile["tile_value"]) xalign 0.5 yalign 0.5
                        #
                        #####


                        #####
                        #
                        # Next lines are used to show an image.
                        left_padding 0 right_padding 0 top_padding 0 bottom_padding 0
                        left_margin 0 right_margin 0 top_margin 0 bottom_margin 0
                        add LiveCrop( ( (every_tile["tile_value"]-1)%grid_width*tile_width,
                                        (every_tile["tile_value"]-1)//grid_width*tile_height,
                                        tile_width,
                                        tile_height),
                                        chosen_img)
                        #
                        #####


                        action [ If (every_tile["tile_number"] not in top_row,
                                   true = If (tiles_list[every_tile["tile_number"]-grid_width]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[every_tile["tile_number"]-grid_width], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None),
                                 If (every_tile["tile_number"] not in bottom_row,
                                   true = If (tiles_list[min(len(tiles_list)-1, every_tile["tile_number"]+grid_width)]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+grid_width))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None),
                                 If (every_tile["tile_number"] not in left_column,
                                   true = If (tiles_list[every_tile["tile_number"]-1]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[every_tile["tile_number"]-1], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None),
                                 If (every_tile["tile_number"] not in right_column,
                                   true = If (tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))]["tile_value"] == empty_tile_value,
                                     true = [SetDict( tiles_list[min(len(tiles_list)-1, (every_tile["tile_number"]+1))], "tile_value", every_tile["tile_value"] ), SetDict( tiles_list[every_tile["tile_number"]], "tile_value", empty_tile_value ) ],
                                     false = None),
                                   false = None), Return("smth")
                               ]

    ##### A button that will let player quit the game (especially useful if there will be no timer to finish the game).
    textbutton "Stand back" action Jump("quit_fifteen_game") xalign 0.5 yalign 0.9
    #textbutton "Continue" action Jump("failtile") xalign 0.5 yalign 0.8

    ##### A button that will show the whole image, should be used only if game uses images (not numbers).
    #textbutton "Show/hide image" action If( renpy.get_screen("full_image"), Hide("full_image"), Show("full_image") ) xalign 0.5 yalign 0.1


##### Screen that contains an image to show (not useful in classic fifteen game).
#
screen full_image:
    add chosen_img xalign 0.5 yalign 0.5 at pic_trans


transform pic_trans:
    alpha 0.0 zoom 0.7
    on show:
        parallel:
            linear 1.0 alpha 1.0
        parallel:
            linear 0.6 zoom 1.2
            linear 0.4 zoom 1.0
    on hide:
        linear 0.5 alpha 0.0
#
#####


label fifteen_game:

    ##### Game settings.
    #
    # Let's set the size of game field in tiles, for example 9 tiles (3 x 3).
    $ grid_width = 3
    $ grid_height = 3

    # Next 4 lines are used to set an image to solve (could be deleted for clasic fifteen game).
    # It is recommended that all images will be smaller than screen size.
    $ chosen_img = "flower.png"
    $ chosen_img_width, chosen_img_height = renpy.image_size(chosen_img)
    $ tile_width = chosen_img_width/grid_width
    $ tile_height = chosen_img_height/grid_height
    #

    # Some useful calculations:
    $ top_row = []
    python:
        for i in range(0, grid_width):
            top_row.append (i)
    $ bottom_row = []
    python:
        for i in range(0, grid_width):
            bottom_row.append ( (grid_width*(grid_height-1)+i) )
    $ left_column = []
    python:
        for i in range(0, grid_height):
            left_column.append (grid_width*i)
    $ right_column = []
    python:
        for i in range(0, grid_height):
            right_column.append (grid_width*(i+1)-1)


    # Let's set the game field - all the tiles are on their places.
    $ tiles_list = []
    python:
        for i in range (0, grid_height):
            for j in range (0, grid_width):
                tiles_list.append ( {"tile_number":(i*grid_width+j), "tile_value":(i*grid_width+(j+1))} )


    # Let's set a missed tile - it can be a random one or the last one (as in classic fifteen game).
    #$ empty_tile_value = renpy.random.randint ( 1, grid_width*grid_height )
    $ empty_tile_value = 2*2
    #

    # Some variables:
    # will let us control if the missed tile should be shown
    $ fifteen_is_solved = False

    # This will show the game screen.
    show screen fifteen_scr

    # To be sure that puzzle can be solved, just randomly move some tiles.
    # This process could be shown to player - uncomment the line that sets the pause between moves.
    # The number of moves should be great enought to shuffle tiles good,
    # also it should be odd to avoid situation when random moves will bring all the tiles back on their starting positions.
    $ shuffle_moves = 7
    label tiles_shuffle:
        if shuffle_moves >0:
            python:
                possible_moves_list = []
                for j in tiles_list:
                    if j["tile_value"] == empty_tile_value:
                        if j["tile_number"] not in top_row:
                            possible_moves_list.append ("top")
                        if j["tile_number"] not in bottom_row:
                            possible_moves_list.append ("bottom")
                        if j["tile_number"] not in left_column:
                            possible_moves_list.append ("left")
                        if j["tile_number"] not in right_column:
                            possible_moves_list.append ("right")
                        move_tile = renpy.random.choice (possible_moves_list)
                        if move_tile == "top":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-grid_width]["tile_value"]
                            tiles_list[j["tile_number"]-grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "bottom":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+grid_width]["tile_value"]
                            tiles_list[j["tile_number"]+grid_width]["tile_value"] = empty_tile_value
                        elif move_tile == "left":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]-1]["tile_value"]
                            tiles_list[j["tile_number"]-1]["tile_value"] = empty_tile_value
                        elif move_tile == "right":
                            tiles_list[j["tile_number"]]["tile_value"] = tiles_list[j["tile_number"]+1]["tile_value"]
                            tiles_list[j["tile_number"]+1]["tile_value"] = empty_tile_value
                        shuffle_moves -= 1
                        #renpy.pause(0.1)           # If used pause should be not so long.
                        renpy.jump("tiles_shuffle")


    # The game loop.
    label fifteen_game_loop:
        $ result = ui.interact()
        python:
            for j in tiles_list:
                if j["tile_value"]-1 != j["tile_number"]: # will continue the game if at least one tile is not in its place
                    renpy.jump("fifteen_game_loop")
        jump fifteen_win

label fifteen_win:
    #textbutton "Continue" action Jump("failtile") xalign 0.5 yalign 0.8
    "yes"
    hide screen fifteen_scr
    jump choice1_yes

label quit_fifteen_game:
    #hide screen fifteen_scr
    "I don't know what good standing back would do. We need to solve this."
    jump fifteen_game

label start:

scene bg first cg

menu:
    "No puzzle":
        jump start2

    "Slide puzzle":
        call fifteen_game

label start2:

    play music "opening2.mp3"

    "I'm Jamie. I'm twelve years old and I like scary stories, free candy, and cheesy horror movies my parents don't want me to watch. I think I'm an okay person, maybe."

    "An okay person who definitely did not lie to their parents about where they're going tonight."

    "...maybe I'm not always that great."

    "Or maybe I just need a different best friend. But that's a completely different argument that my parents have never managed to win."

    "...his parents haven't won yet either."

    "*knocking sounds*"

    j "Coming!"

    "*louder knocking sounds*"

    j "COMING!"

    scene bg first cg

    j "Hi, Marley."

    m "Are you ready to go?"

    menu:

        "Yeah, let's do it!":
            jump choice1_yes

        "Actually... (If you're not the creator, please don't pick this without permission.)":
            jump choice1_no

label choice1_no:

    scene bg street
    show j normal at left
    show m normal at right

    stop music

    j "This will lead to the bonus end, when the creator gets that far. You have her permission to read this, right?"

    j "I don't know, man. I'm not really feeling it. Can we do something else?"

    m ominous " "

    j "It's pretty cold out, and I'm not really an outdoors kind of person. Plus we'd get in big trouble if anyone caught us."

    j "I just think it'd be a better idea to stay inside, eat too much candy, and watch bad horror movies."

    m " "

    play music "bonus end.mp3"

    m happy "You know what? That actually sounds pretty fun. Sure, let's do it."

    j "Are you sure? I know you were really looking forward to this."

    m "Nah, this is way better. Besides, if you're not having fun, I'm not having fun."

    j happy "Thanks, man. Go ahead and grab the candy bucket and come inside."

    m "You mean the bucket with the \"please take one\" sign taped to it?"

    j "This house gets like three trick-or-treaters every year. I'll just tell my parents some jerk must've ignored the sign."

    m "And hide the wrappers in the bottom of the garbage bin?"

    j "Dude, you know it."

    j "Maybe we can do it next year instead?"

    m "Nah, it's not a big deal. I don't mind ditching it. Probably wouldn't have been all I was expecting anyway. I'd rather just hang out with you."

    "I lightly punch Marley's shoulder."

    j "Aww, you big nerd."

    m "Says the guy who wrote an essay on splatterhouse cinematography."

    j "Those movies are ART, Marley."

    scene bg bonus cg

    "I don't even know the name of this movie. We found it on a random channel and I think it's already halfway over. The acting and effects are terrible, the plot doesn't make sense, and I'm pretty sure the camera operator was drunk."

    "I wonder if I can get it on DVD."

    m "You know, if you eat all that candy too fast, you're gonna get sick."

    j "What are you, my mom?"

    m "Hey, I'm taking it easy too."

    j "Yeah, but you're all sickly and stuff. I'm perfectly healthy and therefore I can do whatever I want."

    m "Is it weird for me to care about your safety?"

    j "I mean, I'm usually the one saying that stuff."

    m "Not much point in being safe if you're not there too."

    j "Dude."

    m "Just try not to choke on a candy bar, Jamie."

    j "I'll do my best."

    "Marley's acting kinda weird, but he seems to be enjoying himself, so whatever. It's not important."

    "We probably shouldn't stay up too late, since there's school tomorrow. Did we have homework? I'm pretty sure we didn't have homework. I'm choosing to believe we didn't have homework."

    "Anyway, it's nice to just hang out like this. Maybe it's not all that exciting, but life doesn't have to be exciting to be fun. As long as I'm with Marley, I don't mind being normal."

    "Tomorrow's another day. I wonder what we'll do?"

return

label choice1_yes:

    j "You've only been talking about this for literal years, Marley. I'm pretty sure I've prepared enough by now."

    m "I'm just making sure. Wouldn't want you to get cold feet at the last minute."

    "Marley's been my best friend since kindergarten. He can get kinda...intense, sometimes, but he's a good guy."

    m "But even if you did have cold feet we'd still be going."

    "Generally."

    m "So come on, let's go!"

    j "Yeah, yeah."

    scene bg street
    show j normal at left
    show m normal at right

    "We leave the front porch and walk out into the street. It's late enough that there aren't any cars driving by. There really isn't much of a nightlife here."

    "Probably other neighborhoods are full of trick-or-treaters right now, but this one's kinda low on kids. Just me and Marley, really."

    "...that last sentence kind of sums up a lot about my life."

    j "It's a good thing my parents are busy tonight, because that lie would fall apart the moment they called your house to check on me."

    m "It's a good thing my parents don't care, because the odds of them calling *your* house to check on *me* are really, really low."

    j worried "...I don't know if that's a good thing, Marley."

    m "Whatever, it works."

    show j normal

    "It's cold and dark out, and only getting worse as time passes. I'm usually not one for the outdoors, but this is really important to Marley, so I don't complain."

    "I'm really looking forward to coming back, though."

    m happy "Great weather, too."

    j "Marley, I can see my breath in the air."

    m "But it's not raining, which is a big step up from last year."

    j "And neither of us has food poisoning from the cupcakes at the nondenominational harvest celebration party at school, which is a big step up from the year before that."

    m "And my parents have finally given up on the idea of throwing me a birthday party, which is just a big step up in general."

    j "Are you sure you don't want anything besides this? We could at least get some candy or something. Since we're never eating at those nondenominational harvest celebrations again."

    m "Jamie, as far as I'm concerned, finally getting to do this is the best birthday present I could get. Thanks for coming with me. It means a lot."

    j "Like I'd let you wander off into the woods at night by yourself."

    m "Hey, I haven't randomly fainted in over a year. I'm practically healthy these days."

    j "Did you bring your inhaler?"

    m normal "I'm fine, Jamie. You don't need to worry so much."

    j "You know, it's weird, but you only need one time where your best friend cracks a rib coughing during a sleepover before worrying about them becomes a habit."

    m "I'm *fine*, Jamie. Jeez."

    j "And I never did get your bloodstains out of that one sweater--"

    m annoyed "JAMIE. I AM FINE."

    j "I know, I know, sore subject."

    show m normal at right

    "As we walk, we get farther out of the suburbs and towards the woods. We're nearly at the spot where we'll turn off the road."

    j happy "...almost as sore as your head after you passed out during gym and faceplanted directly onto the wall--"

    m annoyed "JAMIE."

    j "Oh look, it's the turn! Better get your flashlight out!"

    m "*disgruntled noises*"

    hide j
    hide m

    "We step off the road and onto the grass by the side. Now that we're officially walking away from the streetlamps, we'll need to bring our own light."

    "Fortunately, my parents keep a few flashlights in case of power outages. I'm pretty sure at one point they specifically told me not to use them to wander outside at night without an adult, but what they don't know won't hurt them."

    "I'm not actually sure where Marley got his."

    "...he still looks annoyed."

$points = 0

menu:

        "Apologize":
            $points += 1
            jump apologize

        "Don't apologize":
            $points += 0
            jump dontapologize

label apologize:

    show j worried at left
    show m normal at right

    j "Sorry. I was just teasing."

    m "Yeah, I know. I guess I'd worry about you too if you were a medical disaster."

    j happy "I wouldn't say you're a *disaster*. Just, you know. In the vicinity."

    m "A 4.0 on the Richter scale of human frailty."

    j "Nerd."

    m happy "I'm not the one who maintains the Wikipedia entry for Bela Lugosi."

    j "I need to make sure people get the right information!"

    jump enterforest

label dontapologize:

    show j normal at left
    show m annoyed at right

    "Well, it's all true. You'd think he'd be less sensitive about it by now."

    m "Let's just keep going."

    jump enterforest

label enterforest:

    scene bg forest

    play music "forest.mp3"

    "It's even darker once we get into the trees. The street was pretty quiet, but here I can hear the light wind rustling through the remaining leaves, the occasional creaking branch, the crunch of the dead leaves beneath our feet."

    "It's the sort of thing you'd find on a nature CD, except those are supposed to be calming, and this is just creepy as hell."

    show m normal at right
    show j normal at left

    j "You sure you can still find the way?"

    m "Don't worry, I've been here plenty of times."

    j "During the day. When there's light. And the shadows look like trees, not lurking monsters."

    m "Are you doubting my incredible navigation skills?"

    j "I'm saying there is actually a reason our parents don't want us out here at night, and it's not because they're cramping our style."

    m "Relax. It's a pretty straight shot to the caves. As long as we keep moving forward, we'll get there."

    j "If you say so."

    hide j
    hide m

    "There might be more noise here than on the street, but it's all from us and the trees. There aren't any animals here. The locals are pretty used to it. The sky is blue, water is wet, nothing lives in the forest."

    "Every now and then, someone on the news tries to make a big deal out of it. I guess it *is* kind of improbable. But what can anyone do about it? You can't force animals to move in. The plants seem to be getting by, so whatever. It's just another weird fact in an article somewhere."

    "\"Top 10 Unexplainable Phenomena That Don't Actually Affect Anyone's Life In Any Way\"."

    "Besides making the atmosphere even more eerie, I guess."

    show j normal at left
    show m normal at right

    j "Man, I have never liked this place."

    m "What, too creepy for you? You're supposed to be all about the scary stuff."

    j "Scary *stories*, yeah. Actually being somewhere that feels like a monster's going to grab me at any moment? Not really my thing."

    "Marley immediately grabs my shoulder. I only flinch a little bit, because I was expecting that."

    j happy "Jerk."

    m happy "You're smiling, though."

    j "It's a defense mechanism born from spending over half my life with a jerk for a best friend."

    m "Hey, I'm a great friend! Remember that time in third grade when Trevor Holderman tripped you and I punched him in the face and got grounded for a week?"

    j "I still don't know why they didn't suspend you."

    m "Probably because it was such a drastic change in behavior for such a well-mannered student who is never a jerk at all."

    m "Also because I broke my hand."

    j normal "Anyway, this place gives me the creeps. I don't know why you're so into it."

    m normal "It's just cool, you know? Mostly life is so boring, but stuff like this that can't be explained--it just makes the world seem a little bigger. Like there's more than school and parents and going to the hospital ten times in one year."

    j "I guess that makes sense. It's still creepy, though."

    m "Creepy and life-affirming. We're almost there, c'mon."

    hide j
    hide m

    "The sound of our footsteps seems louder now. I wonder how many people come here, even during the day. Not many, I think."

    "One time, I heard my mom talk about how when she was a kid, no one would even come near the place. She went here on a dare and left after five minutes because she got so dizzy she almost passed out. But that was before my time. I don't think that happens anymore."

    stop music fadeout 4.0

    "And now we're finally here."

    scene bg cave entrance
    show j normal at left
    show m happy at right

    play music "sigils.mp3"

    "The big KEEP OUT, DANGER sign is usually a deterrent to the few people who ever get this close to the caves. I don't know if anyone's ever actually been hit by falling rocks, but I guess it could happen. The caves are really old, and there's not exactly a lot of upkeep here."

    "But there is one reason people come here sometimes, even if they usually don't go inside."

    m "Finally! And it's almost time, right?"

    "I check my phone."

    j "8:46. A minute left."

    m "Oh mannn, I can't even believe it. I've wanted to see this *forever* and now it's finally happening."

    j happy "You're like a kid in a candy store."

    m normal "I've never actually been to one so I don't know what they're like."

    j normal "Me neither. I could go for some candy right now, though. I kinda miss trick-or-treating."

    m happy "Maybe next year. Look! There it is!"

    hide j
    hide m

    "The clock on my phone ticks to 8:47, and on cue, the faint lines covering the inside of the cave begin to glow a deep, unearthly red. The floor, walls, and ceiling are filled with pulsing sigils. No one knows what they're from--they're not in any historical record we can find."

    "Even the local pagans don't recognize them. Whatever they are, the carvings have gotta be hundreds of years old, and the designs are probably even older."

    show j normal at left
    show m happy at right

    j "Are we going inside, or are we just gonna stay out here? The view's probably way better up close."

    "Marley still seems ecstatic, but when I look closer, I see he's actually trembling a little. Is it really that big a deal? Life-affirming or no, it's just a bunch of carvings."

    "Unless he's sick again. Man, please don't let it be that. He was looking forward to this so much."

    m "...yeah, let's--let's go inside. C'mon."

    "I try not to pay attention to the sign. We won't be going *that* far in. And it only lasts for a few minutes anyway. We'll be fine."

    scene bg cave interior

    "Up close, the sigils look even eerier. I've never been inside before, so I've only seen them this close in photos."

    "The photos don't do them justice. Marley was right about one thing--they do make the world seem a little bigger. No one knows anything about them, but here they are. And here we are, close enough to touch."

    "Not that I actually want to touch them, but it's pretty hard to walk around in here without stepping on them. I just hope whatever made them isn't a clean freak."

    "The farther we get into the cave, the more sigils we can see. They really are all over the place. It's pretty impressive. I wonder how much work it was to carve all of these."

    show j normal at left

    j "So, is it everything you were hoping for?"

    "Marley doesn't respond."

    stop music

    j "Marley?"

    show m coughing at right

    m "*cough, hack*"

    show j worried at left

    "Oh no."

    play music "cave drama.mp3"

    "I rush to grab him. His skin's pale, and he's shaking harder than before. This is really bad. I shouldn't have let him walk this far in the cold."

    j "Okay, we're leaving now, c'mon, it's gonna be okay."

    hide j
    hide m

    "I take hold of his arm. I can feel how much he's shaking. Should I call an ambulance? I usually call his parents, but an ambulance would be faster. I really hope he doesn't need it, though."

    "Besides, cell service is spotty in the mountains. I probably wouldn't be able to call anyone until we're back by the road."

    "I realize that Marley isn't the only thing that's shaking."

    "The cave ceiling rumbles above us. I look up to see large cracks forming. It's going to come down any second--we need to get out of here NOW."

    "But there are more cracks towards the exit than there are away from it."

menu:

    "Run out of the cave":
        jump badend1

    "Run farther into the cave":
        jump intocave

label badend1:

    "If we stay here, we'll be trapped. We have to make it to the exit before the ceiling collapses."

    "I tighten my hold on Marley's arm and run as fast as I can. The sigils are pulsing faster and brighter, almost in time with the staccato beat of my heart. Dust is already falling, but we're almost there--"

    "With a sound almost like a roar, the rocks begin to fall."

    "The first one lands right in front of us, parts of it breaking on impact. Then more, all around us, hitting the ground, piling up in mounds of rock."

    "It only takes a few seconds before one of them lands on my head."

    scene bg black

    "My skull cracks instantly, and I fall to the ground, my vision swimming for a moment before vanishing completely. I can't tell what's happening to Marley. I can't tell anything."

    stop music fadeout 4.0

    "There's not enough time to have any last thoughts before the rocks crush us both."

return

label intocave:

    "There isn't enough time to make it to the exit. If we want to get away from the collapse, we have to run deeper inside."

    "Ohhh this is a bad idea. This is a really bad idea. But right now, it's a choice between what will definitely kill us and what at least won't kill us immediately. I tighten my hold on Marley's arm and run away from what is probably the only way out."

    "Behind us, the rocks fall onto the ground with a heavy crash. I don't stop to look. I just keep running."

    play music "forest.mp3"

    scene bg cave collapse

    "As the sounds start to die down, so does the light from the entrance. I glance back to check. The area behind us might as well be a solid wall of rock now. The collapse seems to have stopped, but now we've got a new problem."

    show j worried at left

    j "Marley?"

    show m normal at right

    m "Are we alive?"

    j "Technically?"

    m "Oh. That's good."

    j "But we are also now trapped in a cave with the only exit blocked by a wall of rock possibly over twenty feet thick, and the only light source is our flashlights."

    m "That's less good."

    j "Just a little, yeah."

    j normal "Can you stand?"

    m "I can try."

    "I carefully let go of Marley. He's stopped shaking, and there's no more coughing, but he still looks a little dazed. I can't blame him."

    j "You good?"

    m "Yeah."

    j "Okay, because standing feels like a lot right now so I'm gonna have some floor time."

    m "Just because I *can* stand doesn't mean I don't agree with you there."

    scene bg second cg

    "We both slump onto the floor. It's dirty and uncomfortable, but that's the least of our problems right now."

    m "So...there probably isn't any way we can move those rocks, huh."

    "I realize something very, very important."

    j "Marley, you know how my parents think I'm at your house and your parents think you're at my house?"

    m "Yeah?"

    j "That means nobody knows we're here."

    m "Oh."

    j "Yeah."

    m "I know there's almost definitely no service here, but we could at least try to call someone, right? Just to be sure?"

    j "Yeah. Doesn't hurt to try."

    "I don't get my hopes up. Being in the mountains is bad enough for getting a signal, but being in a cave makes it even worse. Still, I pull out my phone and try to dial. So does Marley."

    "Nothing."

    "Marley puts down his phone."

    m "Nothing for you too, huh?"

    j "Yeah."

    "I'm trying not to panic. Panic would not be helpful. It wouldn't make me feel any better, either."

    m "Well, we're still alive, and we've got the flashlights. That's something."

    j "Not that flashlights will help us much if there's another cave-in and we can't get away in time."

    m "Maybe there was, I don't know, some structual instability at the entrance? I think we'll probably be okay now that it's settled."

    j "I'm going to agree with you, because if I don't I'm just going to freak out even more, and that'll just get really awkward."

    scene bg cave collapse
    show j worried at left
    show m normal at right

    m "Hey. We'll be okay."

menu:

        "Yeah, we'll be okay.":
            $points += 1
            jump okay

        "We are definitely going to die.":
            $points += 0
            jump goingtodie

label okay:

    j normal "Yeah. Negative thinking isn't going to help us any."

    m "Even though it's really tempting."

    j "SO tempting."
    jump postokaydie

label goingtodie:

    j "Marley, this is literally the worst situation we've ever been in. I'm not seeing a whole lot of reasons here to stay positive."

    m "We'll think of something. We're alive, we can walk, and we've got light. Don't give up yet."

    j normal "Easier said than done."
    jump postokaydie

label postokaydie:

    j "So do we have any kind of plan?"

    m "How far back do the caves go, anyway?"

    "Marley shines his flashlight down into the darkness ahead of us. It shows the walls fine, but the end of the cave isn't within view."

    m "It doesn't look like it's close."

    j "Nobody knows, right? Not between the local superstition and the danger sign. Which, if we ever do get out of here, I'm gonna pay a lot more attention to that kind of thing."

    m "So there might be another exit back in the mountains somewhere. We just have to look for it."

    j "Sounds good to me. Or, well, it doesn't, but I can't think of anything else. Can't hurt to try, at least."

    j worried "Probably."

    m happy "That's the spirit! C'mon, your dad's always saying you need to get out more. A long walk through the mountains is totally healthy, right?"

    j happy "Nothing like terror and oxygen deprivation to get the blood moving."

    show j normal at left
    show m normal at right

    "I stand up, bracing myself against the wall of the cave with one hand. It's pretty cold. I doubt much heat gets into this place, especially not this time of year."

    "I can probably handle it, but Marley really shouldn't be out here. I should've at least made him wear gloves. Not that I really expected anything like this."

    j "Let's get going. We don't want to stay here too long."

    m "I'd make some crack about the atmosphere but actually I'm pretty cold right now so yeah, let's get a move on."

    "He stands up too, a little slower than I did, and with our flashlights aimed ahead of us, we set out into the dark."

    "Not that we get very far before we stop in our tracks."

    show j worried at left
    show m worried at right

    "A voice comes, not from ahead or behind us, but all around us, like an intercom. I can't tell what language she's speaking. I'm not really an expert or anything, but it doesn't sound like any language I've heard before."

    "Whatever she's saying, she doesn't sound happy."

    m "Who's there?"

    "We move our flashlights around, but the area in front of us is still dark. No one to be seen. And there wasn't anything behind us. There must be some kind of speaker system in the walls."

    "I'm trying not to think about the likelihood of there being a speaker system in a cave filled with unrecognizable glowing symbols."

    "If she responds to Marley's question, we can't tell. She just keeps talking."

    "Her voice is strong and firm. She kind of sounds like she's giving a speech, or maybe monologuing. The occasional pauses are short enough that they're probably for effect, not so someone can respond."

    "Is she going to stop anytime soon? Maybe we should just keep going."

    "I'm about to suggest that we keep going when she sighs. With a few more lines of whatever it was, she stops. And then the only sound in the cave is our breathing."

    j "I don't suppose you know what that was about?"

    m "Hey, I only know the carvings are really cool-looking, I never heard anything about a voice."

    j "So there's not like...legends or anything? It could just be some random lady trying to mess with us?"

    m "Yeah. The mysterious voice in the cave with the unrecognizable glowing symbols has a perfectly rational explanation."

    "I don't wanna jinx it or anything. But I'd really like it if horror movies were just movies."

    "As if on cue, the ground starts to shift."

    play music "fall drama.mp3"

    show j scared at left
    show m scared at right

    j "An earthquake? Seriously?"

    m "This doesn't feel like a--"

    "And then it vanishes."

    scene bg black

    "One moment it's shaking and then it's just gone. The air rushes from my lungs as we suddenly plummet into nothingness, a freefall out of nowhere."

    "I grab Marley's arm. I don't know why. It's not like it'll help. But we're falling so fast, and the bottom's nowhere in sight, so...I don't know. I just want to."

    "The wind pulled up my other arm, the one holding the flashlight, so I can't see his face. I don't know what he looks like right now."

    "It doesn't seem fair, that I can't see him when I'm about to die."

    "And then, just as suddenly as it disappeared, the ground's at our feet again."

    play music "forest.mp3"

    scene bg cave path

    "We didn't really land on it. It's just...there. We were falling, and now we're standing. The whole thing must've taken fewer than ten seconds. I'm still holding Marley's arm."

    "What can we even say after that? My heart's beating a mile a minute. I have no idea what's going on."

    "After a long, long moment, Marley speaks up."

    show m worried at right
    show j worried at left

    m "Was that just someone trying to mess with us too?"

    j "...I don't know."

    "I can guess, though. Vaguely. I'm pretty sure I know what it wasn't, at any rate."

    "Anything normal."

    "I let go of Marley's arm and shine my flashlight behind us. It's just a big dirt wall, stretching up and up, farther than the light goes."

    "The width of the cave seems about the same. It's like there's just a big dropoff."

    "Marley shines his flashlight ahead of us. More cave. More dark."

    m normal "...guess we should just keep walking, huh?"

menu:

        "Guess so.":
            $points +=1
            jump guessso

        "Are we not going to talk about that?":
            $points +=0
            jump arewenot

label guessso:

    j normal "Can't really do anything else, I guess."

    jump postguess

label arewenot:

    j "Are we not going to talk about what just happened?"

    m "What's there to say? I don't know what it was, do you?"

    j "No, but...it was really weird, right?"

    "Marley aims his flashlight up the wall."

    m "However it happened, we can't get back up. All we can do is keep going. Unless you just want to stand here forever."

    j normal "Yeah, I know. Let's go."

    jump postguess

label postguess:

    hide j
    hide m

    "And so we go."

    "The path ahead of us stretches far into the darkness. Even besides how there's definitely something supernatural going on, it looks man-made. It's too even and uniform. Kind of like an old mining tunnel, except I think those usually have support braces and stuff."

    "There's none of that here. Just rock walls and a dirt path. No light besides our flashlights, and no sound besides our footsteps and our breathing."

    "I'm not going to say it feels like a tomb. Those are usually better-decorated."

    show j normal at left
    show m normal at right

    j "I wonder if there's anyone else down here."

    m "Like, whoever that woman was?"

    j "Maybe. Or anyone else who got trapped here. Or things to get trapped here with."

    m "Just being here is bad enough, you want to add monsters to it?"

    j "I don't *want* to! But it's hard not to think about that stuff right now, right?"

    "I've seen way too many horror movies to not be imagining all the stuff that could happen here. Maybe my dad was right and they've rotted my brain. Why couldn't I be obsessed with something like musicals or horses?"

    m "I've never heard of anyone disappearing here. Or any murders or anything. So I don't think we'll find anyone else here."

    "I've never heard anything either. Maybe it's because people don't go inside the cave much; the only actual picture of the sigils glowing is only about five years old. The \"keep out\" sign does its job, I guess."

    m "That rules out vengeful spirits, probably. And anything that eats people, or it probably would've starved by now."

    j "Evil cultists?"

    m "Overrated. Who thinks it's a smart idea to make an ancient evil notice you, anyway."

    j "Demons?"

    m "Because there's so many people to torment here?"

    j "Well, there's gotta be a reason this place exists. That woman probably had something to do with it."

    "We go silent for a while. It's too much to think about. The sigils, the voice, the fall--it's all more than I know how to handle."

    j "Hey."

    m "Yeah?"

    j "Is the world big enough for you now?"

    m "This stuff's not as cool when it's actually happening, huh."

    j "I liked it better when it was just a weird cave we could look at and then leave and go back home."

    "I read an article once about how horror comforts us because it lets us explore dangerous subjects in a safe environment, or something. But this isn't safe at all. It's not comforting or cathartic or thought-provoking."

    "I just want to go home."

    hide j
    hide m

    "The long tunnel turns left, leading into a small room. It's made of dirt, and there don't seem to be any exits in it."

    "Marley shines his flashlight towards one of the walls."

    show j normal at left
    show m normal at right

    m "What's that thing?"

    "We both walk closer to get a better look. There's a square carving set into the wall, maybe a few feet wide, with a bunch of tiles in it. It looks like there's supposed to be a pattern on them, but it's all jumbled up."

    j "It looks kinda broken. The patterns don't match up."

    "I can't tell what they're supposed to show. It's just a bunch of lines to me."

    m "I don't know if it's broken. Maybe--"

    # click sound

    "Marley puts his fingers around one of the tiles, and rotates it."

    m "Yeah, see? We can make the pattern line up if we move them."

    j "For all the good it'd do. It's just a carving."

    m "I guess we should look around some more first."

    "We look around some more. The walls are all tightly-packed dirt, no obvious ways out besides the one we came in. The only thing here is the carving."

    j "I guess it won't hurt to see what it does."

    "We go back to it. The pattern isn't any easier to figure out than it was last time, but I think if we moved the tiles around some more we'd be able to see it."

    "What that'd do for us, I don't know. But it's literally the only thing here."

menu:

        "Bad end":
            $points +=0
            jump failtile

        "Continue":
            $points +=0
            jump passtile

label failtile:

    m "It looks like the sigils, doesn't it?"

    j "Yeah. Is it gonna do anything, though? Maybe it's just a--"

    # symbol lights up and circle turns black, click-chunk noise

    scene bg black

    "There's a metallic flash from the circle under the carving, and then something is sticking out of my chest."

    "For a second, it doesn't hurt. I stare at the metal spear going through me, dumbfounded, while Marley's face fills with horror."

    "Then the pain hits. It flares through my body like a wildfire, radiating from the center. There's blood in my mouth, spreading across my shirt, slowly dripping down."

    "I'm too shocked to scream. For a moment, my mind overloads with wordless, incoherent panic."

    "And then all of my thoughts fade, and even the pain does. The room around me is gone. Marley is gone."

    "And then there's nothing."

return

label passtile:

    # step away

    "I'm almost done with the tiles. I still don't really know what the pattern is, but it looks a lot like the sigils from the cave entrance. It isn't glowing, though."

    m "Just one more. Here we--"

    j "Hold on. Something doesn't feel right."

    m "What do you mean? There's still nothing else in the room."

    j "Yeah, but...doesn't it look like the sigils?"

    m "I guess it does. Is that weird? Whatever this place is, the sigils are probably part of it."

    j "I know, but when the sigils lit up, didn't the cave collapse?"

    "I thought it was just coincidence. Structural instability or whatever. Our footsteps setting it off. But with the stuff that happened after that, it doesn't feel coincidental anymore."

    m "...you're right. Do you think this room's gonna collapse too?"

    j "Maybe?"

    "But the fact remains that there is literally nothing else here."

    "We spend a couple minutes searching the room again, then the end of the tunnel. Nothing. All we have to go on is the carving."

    "I could be overthinking things, maybe."

    "It doesn't feel like I'm overthinking things."

    m "So are we gonna finish it or not?"

    "I take a closer look at the carving. There's a circle on the bottom of it, like something's embedded in it. I kinda thought maybe if we finished putting the tiles together, something would pop out that'd help us find a way forward."

    "This is a wild shot in the dark here. I'm literally just guessing. I don't have any evidence for this."

    "But maybe I was only half-right about that."

    j "I know this sounds weird, but...can you step away from it?"

    "Marley makes a questioning face, but he steps to the side anyway."

    "I follow him. When I'm not in front of the carving anymore, I carefully reach my arm out and move the final tile."

    # click-chunk, whoosh, thud

    "The circle slides to the side, exposing a hole, and something like a metal spear shoots out from inside it."

    "The spear goes straight through the wall on the other side. If one of us was standing in front of it--"

    m scared "Holy shit."

    j scared "I, uh....."

    m "That almost killed you! You almost died!"

    "My heart's beating faster and faster. Adrenaline courses through me, even though all I did was walk a couple feet away and push a tile."

    m "How'd you figure that out?"

    j "...lucky guess?"

    m "When we get out of here, you should buy a lottery ticket."

    "I manage a shaky smile. That's three times now, something almost killed us. I'm torn between not liking the trend and liking it a lot more than the alternative."

    "I glance at the opposite wall. I can't see the spear; it must've embedded itself pretty deep into the dirt."

    "Then I remember that after it went in, I heard something like a thud."

    "Did it hit something? Or did it fall down?"

    j normal "Let's check out the wall."

    show m normal at right

    "We walk over and peer through the hole. Dark. I shine a flashlight towards it."

    "I can't see the spear at all. The walls might be dirt, but they're still pretty solid; if they just kept going, the spear would've stopped. So if the spear isn't visible..."

    m "Is there a room behind here?"

    "The hole isn't huge, and we don't have any tools with us. It takes us a while to pull away the loose dirt and widen the hole."

    "Marley has to take a few breaks. I don't blame him. My arms are getting pretty tired too."

    "By the end of it, our hands are absolutely covered in dirt, and we're both exhausted, but we've got a wide enough hole to step through."

    "There *is* a room behind the wall. Or rather, another tunnel. The spear lies on the floor just in front of us. I gingerly step over it."



    stop music

    j "We're skipping ahead a whole bunch here! If you're not the creator, please stop here unless you have permission."

label trueend:

    play music "true end.mp3"

    show j normal at left
    show m normal at right

    m "Come with me?"

    j "Huh?"

    m "I mean, it wasn't really in the plan or anything. Not at first. I just wanted to find a way out and be done with this stupid dimension."

    m "But spending three hundred years by yourself kinda gets to you, you know? And sure, I was really angry all the time. There wasn't much in me besides anger. Then I finally got a body again, and everything was even harder, because now I *had* an outlet for it, but I couldn't let myself use it."

    m "People probably get alarmed when their baby tries to kill them, yeah?"

    m "So I was a real mess. There was no way I was gonna pass for human. All I was was this big mess of seething hatred."

    m "Then I met you."

    m "Everyone else in our class was either too scared to go near me or didn't care enough to try. But you wanted to be friends, because you saw that I was unhappy and you wanted to fix it."

    m "I didn't know just how lonely I was until that moment. I didn't even know what loneliness *was*, really. Human emotions are complicated. But after hundreds of years of isolation, here was someone reaching out to me with no obligation to do so."

    m "And I just thought, well, sure, let's see how this goes."

    m happy "And it went pretty well, all things considered."

    j "So...that was all you needed? Some random kid being nice to you?"

    m normal "I know, right? I didn't get it at all. Emotions are weird, I guess."


# This is a reminder that the way to state points within dialogue is %(points)d points.

return
