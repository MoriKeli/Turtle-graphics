import turtle
import math

ttl = turtle.Turtle()
ttl.speed(15)
ttl.hideturtle()
ttl.fillcolor('red')

ttl.begin_fill()
for i in range(300):
    ttl.forward(math.sqrt(i)*30)
    ttl.left(150)

ttl.end_fill()

turtle.done()
