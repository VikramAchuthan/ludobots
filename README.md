# ludobots - Vikram Achuthan, Artificial Life - CS 396, Northwestern University - Assignment 7 

This week, I created a create a program that generates a 3d morphology building up from the randomized snake I built last week. 
My goal was to create a figure that resembled a creature performing an activity, much like those we saw when studying Karl Sims' work, some of which is listed here: https://www.karlsims.com/evolved-virtual-creatures.html

After experimenting with how joints can be manipulated in pyrosim and pybullet, I settled on manipulating the rpy configuration (rpy = "roll pitch yaw") in joints.py, a file that is part of the pyrosim library. The creature I eventually evolved to create was a pig with a long tail and arms, which in future assignments and the final project, I want to enable to smell food and move closer to it. This is why the nose is a defining feature of the creature. 

Links with and without sensors are colored green and blue, respectively. Sensors are currently only able to sense movement, as they have been throughout the ludobots project, but I hope to build them to sense objects of a specific nature. Note the images below that describe how the joints and links were formed, and the variation possible with my program:

I introduced randomness into the program by utilizing the random() library, which generated a random number of sensor and motor neurons each time the simulation ran. Randomness also exists through the links that develop from the "face" block, including in their direction, size, rpy angle (measured in radians), and length. 

In order to see the randomized simulations, download the code and run the search.py file, once you have pyrosim and pybullet installed. 

Citation: https://www.reddit.com/r/ludobots/wiki/finalproject/



![assignment7](images/assignment7.jpeg)
