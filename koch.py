# Created by Malachi English 21/2/23
# Program that draws a Koch Snowflake with a variable amount of iterations

from turtle import *
from math import *


# turtle settings
hideturtle()
speed(0)
title("Koch Snowflake")

def main():
    # Gets user input for number of iterations. Makes sure that the value is an integer.
    while True:
        try:
            iterations = int(textinput("Iterations input", "How many iterations? (Recommended no higher than 8)"))
            break
        except:
            pass
    
    # Draws the koch triangle
    draw_koch(600, iterations)

    # Keeps the window open until clicked on.
    exitonclick()

def draw_koch_side(size, iterations):
    # Defines the current iteration as the 'iterations' parameter
    current_iteration = iterations

    # For each side, if the current iteration is greater than 0, run the draw_koch_side function
    # This will decrease the current iteration for that side, and if it is still greater, repeats.
    # This is an example of recursion, as the function is calling itself multiple times.
    # Eventually, the current iteration of that side will equal 0, which will cause it to draw a straight line for that side.
    # After that, the program moves onto the next side, and repeats this same process. 
    if current_iteration > 0:
        # start straight
        draw_koch_side(size/3, current_iteration-1)

        # turn and start drawing the 'branch' of the side
        left(60)
        draw_koch_side(size/3, current_iteration-1)

        # tip of the branch. turn and draw the rest of the 'branch'
        right(120)
        draw_koch_side(size/3, current_iteration-1)

        # end straight (same direction as started)
        left(60)
        draw_koch_side(size/3, current_iteration-1)
    else:
        forward(size)

def draw_koch(size, iterations):
    # speeds up the process for more complex koch triangles
    if iterations >= 4:
        tracer(100)

    # Thickens the line for less complex koch triangles.
    if iterations <= 4:
        pensize(2)
    
    # Defines the height of the Koch snowflake
    if iterations == 0:
        # If iterations == 0, then it is just a single triangle 
        height = size*(cos(pi/6))
    else:
        # If is more iterations, a smaller triangle is placed below the original triange.
        # We must add the height of the smaller triangle to correctly calculate the height
        height = size*(cos(pi/6)) + (1/3)*size*(cos(pi/6))

    # Moves the 'pen' to the starting position (at the top of the koch snowflake)
    penup()
    left(90)
    forward(0.5*height)
    right(150)
    pendown()

    # Draws 3 Koch sides, for the 3 sides of the original triangle. 
    for i in range(3):
        draw_koch_side(size, iterations)
        right(120)
    update()

main()