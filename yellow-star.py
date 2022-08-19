import turtle

ttl = turtle.Turtle()
ttl.back(100)
ttl.hideturtle()

# black bg
ttl.color('yellow', 'yellow')
ttl.getscreen().bgcolor('black')
ttl.begin_fill()
for i in range(5):
    ttl.fd(200)
    ttl.left(144)

ttl.end_fill()
turtle.done()
