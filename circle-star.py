import turtle
import math

ttl = turtle.Turtle()
ttl.speed(15)
ttl.hideturtle()
ttl.color('red')

ttl.begin_fill()
for i in range(70):
    ttl.forward(math.sqrt(i)*i)
    ttl.left(150)

ttl.end_fill()

turtle.done()
