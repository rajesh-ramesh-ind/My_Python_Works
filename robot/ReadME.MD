This documentation refers to the ROBOT PROGRAM.

This documentation was created by Rajesh Ramesh without cloning from any web sources.
Contact: rajeshramesh38@gmail.com

                        (((    """ PLEASE READ THE DOCUMENT THOROUGHLY """  )))

##### Problem Statement:
    We have to calculate the co-ordinates of the robots after the given movement and 
    group them based on the co-ordinates.

##### Given:
1. Robots which can only move in four directions, UP(U), DOWN(D), LEFT(L), RIGHT(R).
2. The movements of robots are given in a file (robots.txt) and it is in the following format

Name|X|Y|Move
----|-|-|----
R1|5|5|UDDLRL
R2|0|0|UDDLLRUUUDUURUDDUULLDRRRR
R3|5|5|U2DL1R1L
|...|...|...|....|

3. First column (Name) is Robot name, Second column (X) is Current X position of robot, Third column (Y) is Current Y position of robot, Fourth column (Move) is the movement command

4. Each movement, if not prefixed with a number say "U", is considered as 1 movement upwards.If the movement is prefixed with a number say "2D", is considered as 2 movements downwards.

##### Output:
    Output should be a file [output.txt] containing the coordinates and the list of robots (delimited by :) in that position:
   | X|Y|Robots |
   |--|-|-------|
   |4|4|R1:R3|
   | 2|3|R2|
   | ...|...|...|
   | ...|...|...|
   
#### Problem-Solving Approach:

1. This programs consider all the robot data with a Robot: Object
2. It contains the Name of the Robot,  X_Position, Y_Position, Movement
3. All the input to the program are given in the "input.txt" with a format :> NAME,X_POS,Y_POS,MOVEMENT
4. The input.txt file is opened and all the lines are read and unpacked respectively and saved as list Robot objects.
5. Now all the movements are applied with desired step for each robot respectively using up,down,left,right methods defined in the Robot class.
6. Now all the robot objects are groups based on their co-ordinates
7. Now the groupings are saved in the "output.txt" file in the format :> X,Y,Robots
