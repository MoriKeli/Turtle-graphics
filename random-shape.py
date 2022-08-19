import turtle
import math

ttl = turtle.Turtle()
ttl.speed(15)
ttl.hideturtle()
ttl.getscreen().bgcolor('blue')
ttl.fillcolor('white')

ttl.begin_fill()
for i in range(300):
    ttl.forward(100)
    ttl.left(math.sin(i/10)*50)
    ttl.left(100)

ttl.end_fill()
turtle.done()
