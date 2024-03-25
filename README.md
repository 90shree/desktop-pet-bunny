# Demo


![demo](https://github.com/90shree/desktop-pet-bunny/assets/163702108/98449337-0f59-48c3-8cd1-03ae2e51b6cc)

A desktop pet bunny companion created with Python! It eats carrots, sleeps, and walks at random intervals across the bottom of your screen. 

# How was it made?
The program is essentially a series of gif-animations ontop of a fitted transparent window, made with the help of the Python module "tkinter" to manipulate GUI aspects of the window. Object Oriented Programming was used to define the window as its own class, and each animation was also drawn by hand using a pixel-art program, then converted into readable gif files. 

Gravity/Drop physics was implemented through declaring variables for velocity, acceleration and gravity.. then adding the gravity variable to the y-velocity (using a plus-equals operator) when the user is not dragging the window, and applying this logic to both acceleration and velocity as well.



# How to run
Simply extract the 'Bunny.zip' file and run the python executable :)

***Right click the bunny and select "Close Bunny" to close the program!*

# If, for any reason, this is not possible:

## 1. Ensure that you have Python 3 installed.

## 2. Install the necessary modules needed to run this program with the following commands:

'pip install tk'

'pip install win32gui'

'pip install win32com'

'pip install random'

## 3. Now you can run the program in Command prompt by:

First changing the directory to where this program is stored by using the 'cd' command, followed by a space, then your directory.

Then simply the command, "Bunny.py"
