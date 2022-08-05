import turtle

ttl = turtle.Turtle()

ttl.speed(15)
ttl.hideturtle()
ttl.getscreen().bgcolor('skyblue')

ttl.color('red', 'black')
ttl.begin_fill()

ttl.circle(100)
ttl.circle(80)
ttl.end_fill()

turtle.done()
