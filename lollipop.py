import turtle

ttl = turtle.Turtle()
ttl.speed(15)
ttl.hideturtle()
ttl.color("black", "red")

ttl.begin_fill()
ttl.goto(0, 70)
ttl.circle(100)


def draw_lollipop(radius, pos_y):

    for i in range(4):
        radius -= 20
        pos_y += 20
        ttl.penup()
        ttl.goto(0, pos_y)
        ttl.pendown()
        ttl.circle(radius)


draw_lollipop(100, 70)

ttl.end_fill()

turtle.done()
