# Demo


![demo](https://github.com/90shree/desktop-pet-bunny/assets/163702108/98449337-0f59-48c3-8cd1-03ae2e51b6cc)

A desktop pet bunny companion created with Python! It eats carrots, sleeps, and walks at random intervals across the bottom of your screen. 

# How was it made?
The program is essentially a series of gif-animations ontop of a fitted transparent window, made with the help of the Python module "tkinter" to manipulate GUI aspects of the window. Object Oriented Programming was also used to define the window as its own class.
Each animation was also drawn by hand using a pixel-art program, then converted into readable gif files. 

Gravity/Drop physics was implemented through declaring variables for velocty, acceleration and gravity.. then adding the gravity variable to the y-velocity (using a plus-equals operator) when the user is not dragging the window, and applying this logic to both acceleration and velocity as well.



# How to run
## 1. Firstly, ensure that you have Python3 installed.
## 2. pip install the following modules in Command Prompt if you do not already have them installed:
 'pip install random'
 
 'pip install tk'
 
 'pip install time'
 
 'pip install ctypes'
## 3. Once completed, run the code in Command Prompt by first changing the directory to where the "code" folder is installed on your desktop.
This can be done by using "cd", followed by a space, then your directory.
## 4. Now you can run the code using the command "virtualpet.py"
