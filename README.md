# Snake-Game-Using-Python
Python code for generating the Snake Game with various options.


############# Gilberto Jimenez 00261433 #############



### Game Description:

## Main Menu:

**Start:** This will start the game to play. The snake keeps moving, and the user will 
control the snake to find its food to grow in size, while avoiding obstacles. The games 
ends when the snake hits an obstacle or eats itself, then the user is prompted to choose
to play again or get back to the main menu for exiting or changing game options.

**options:** The user can change the playing board or the snake's speed parameters:

1. board: The user can choose between three default built-in boards, or draw a custom one.
2. speed: The user can choose, according to certain limits, the initial speed of the snake,
and the amount of speed increment for each unit size growth.

**Help:** This will give the user some tips about how to control the game and change options.

**Exit:** The user can exit the game either using this button or hitting the window 'X' button anytime.



## Game Controls:

**Left Arrow Key:**  Turn the snake to the left. No action when the snake is moving to the right.

**Right Arrow Key:** Turn the snake to the right. No action when the snake is moving to the left.

**Up Arrow Key:**  Turn the snake upward. No action when the snake is moving downward.

**Down Arrow Key:**  Turn the snake downward. No action when the snake is moving upward.

**P Key:**  Pause/resume the game.

**Window Exit Button:** Exit.


### Install and Running Instructions:

This game is available as a python script and as an installer for Windows.

## Windows installer:

For Windows 64bit. (Tested on Windows 10)
Just extract the installer and run, game files will be installed on your
device, and the game can run without installing Python.
Go to the folder in which you choose to install in, and run **main_game.exe**.

## Running the Python Script:

The following must be installed on your device:

**Python:** Version 3+. Multiple versions for multiple OSes can be downloaded from:
		
		https://www.python.org/downloads/releases

**Pygame:** After installing Python, install pygame using pip on the command line:

		pip install pygame


The game also depends on built-in modules that come with python and do not have
to be installed manually: **Random**,**time**, and **sys**.

After installing all the above, open the command line and go to the directory
containing the script PLAY.py using the **cd** command. Type:

		python3 PLAY.py

or( This may differ according to your platform)

		python PLAY.py

to start the game.


### Further Work:

The game can be developed to have more advanced features and flexible options:

1. Let the user choose initial snake body size and position.
2. Saving scores of games played, and congratulating the user when a new high score
is achieved.
3. Making various types of food portions for the snake, each has its different score increment.
