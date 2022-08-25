import sys
import turtle

ttl = turtle.Pen()
ttl.hideturtle()
ttl.speed(30)

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
ttl.getscreen().bgcolor('black')

for radius in range(300):
    ttl.pencolor(colors[radius % 6])
    ttl.forward(radius)
    ttl.left(59)

turtle.done()
turtle.exitonclick()
