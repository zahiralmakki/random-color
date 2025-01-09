# 100 Days of Code
# Day 18: lec 134
# Trutle Challenge 4: Python Tuples and How to Generate a random RGB Colors
# 9 Jan 2025, Thrusday

import random
import turtle as t


zug = t.Turtle()
t.colormode(255)

def random_color():
    """"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    rand_color =  r, g, b
    return rand_color

directions = [0, 90, 180, 270]
zug.pensize(15)
zug.speed("fastest")


for _ in range(200):
    zug.color(random_color())
    zug.forward(30)
    zug.setheading(random.choice(directions))
