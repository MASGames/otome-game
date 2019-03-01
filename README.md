# otome-game
An otome game created by us.

## Developer setup

1) Download [Ren'Py](https://www.renpy.org/latest.html) and follow the [installation instructions](https://www.renpy.org/doc/html/quickstart.html#the-ren-py-launcher)

2) I recommend installing [GitHub Desktop](https://desktop.github.com/) as a convenient UI for 
    interacting with Git. It will ask you to sign in with your GitHub credentials.

    After installing, go to File -> Clone Repository. It should already provide you with a list of repositories you own -- select "MASGames/otome-game", and set the local location to wherever you've set Ren'Py to look for projects.  

## Making changes

1) In the Ren'Py Launcher, select the 'otome-game' project, and then select a file under the 'Edit File'
    menu such as 'script.rpy'. This should prompt you to install an editor (the Ren'Py website recommends 
    Editra) if you haven't already. 

2) Alternately, you can load the files directly in your preferred editor. 

## Code structure 

1) Script.rpy is the entrypoint to the game. If you're not sure where to start, here is a good place! 

2) Common route content should all written directly in script.rpy. This includes character-specific choice
    scenes that occur in the common route, e.g. Viola picking who to eat lunch with. 

3) Individual route content should be written in \[charactername\].rpy. For example, a scene in month 5 on 
    Liam's route should be written in liam.rpy. 

4) For ease of searching, add a comment with a scene number (generally of the format \[month\].\[scene\],
    e.g. 1.11 is the eleventh scene in month 1) and a short description of the scene to both the top of 
    the scene and the table in the work log. 

5) If the start of a scene is marked by a label, add that label to the table in the work log as well. If 
    you're adding a new label, please check the work log to make sure the one you're thinking of using isn't
    already taken!

## Running the game 

1) From the Ren'Py Launcher, select the 'otome-game' project and then select 'Launch Project'!
