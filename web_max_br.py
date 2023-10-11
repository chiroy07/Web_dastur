from turtle import *
import random
import sys
def gul():
    tell=sys.stdout.tell

    for i in range(300):
        bgcolor('black')
        color('yellow')
        speed(500)
        circle(190-i,99)
        left(90)
        circle(190-i,99)
        left(900)

gul()
hideturtle()
mainloop()

from turtle import *
import random
import sys
def gul():
    tell=sys.stdout.tell

    for i in range(150):
        bgcolor('blue')
        color('yellow')
        speed(500)
        circle(180-i,99)
        left(90)
        circle(170-i,89)
        left(900)

gul()
hideturtle()
mainloop()
