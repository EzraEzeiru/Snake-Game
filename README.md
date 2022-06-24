# Snake-Game
The classic snake game built using pythons in-built turtle module and Object Oriented Programming.

• food.py:
This document contains code that generates "food" after the snake object has come in contact with previous food.
It places the food randomly in the floor area using the turtle coordinate system.

• scoreboard.py:
This document contains code that increments the score by 1 as soon as the snake comes in contact with food.

• snake.py:
This document contains code that is responsible for moving the snake using the listen() function in turtle. It
listens for keyboard press and moves the snake accordingly. It is also responsible for incrementing the length of the snake as the snake comes in contact with food.

• data.txt:
This is a text file that stores the highest score from the game. It compares the current score with the highest score in the text file and replaces it if current score is greater than high score. 

• main.py:
Utilized object oriented design so the snake object can inherit methods and attributes from each of these Classes and direct the entire operation between them. 
