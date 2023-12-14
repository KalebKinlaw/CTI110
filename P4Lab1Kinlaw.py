
"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html

Kaleb Kinlaw
CTI - 110
P4Lab1A - Turtle Shapes in Loops
10/12/23
"""

import turtle
import random 
t = turtle.Turtle()
t.pensize(3)
#Set our variables
COLORS =["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
REPEAT = 10
for time in range(REPEAT):
  x = random.randrange(-200, 200)
  y = random.randrange(-200, 200)
  t.goto(x,y)
  PEN_COLOR = random.choice(COLORS)
  SIDES = 3
  LENGTH = 100
  FILL = True
  FILL_COLOR = "yellow"
  
  SIDES = random.randrange(3, 12)
  LENGTH = random.randrange(10, 50)
  ANGLE =  360 / SIDES 
  
  if FILL == True:
    t.begin_fill()
    t.fillcolor(FILL_COLOR)
    t.pencolor(PEN_COLOR)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(SIDES):
      t.forward(LENGTH)
      t.right(ANGLE)
    t.end_fill()