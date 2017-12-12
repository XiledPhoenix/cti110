#CTI-110
#M6LAB - SnowFlake
#Guillermo Ayerbe
#12-4-2014

#I tried to change up the format of the snowflake to make it more my own.
#Every time i tried to stray away, i ruined the nested loop, and jacked up
#the snowflake. I apologize for the almost copy pasta assignment. I will not
#be doing this again.

import turtle
import random

wn = turtle.Screen()
bill = turtle.Turtle()
wn.bgcolor('Black')

colors = ('purple', 'white')

for n in range(11):
    for n in range(2):
        bill.forward(100)
        bill.right(60)
        bill.forward(100)
        bill.right(120)
    bill.right(36)
    bill.color(random.choice(colors))

wn.exitonclick()
