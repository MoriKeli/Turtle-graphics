import turtle
import random

ttl = turtle.Turtle()
ttl.speed(30)

bg_colors = ['cyan', 'blue', 'green', 'black']
c = random.choice(bg_colors)
font_color = ['black', 'white', 'red', 'yellow']
x = random.choice(font_color)

ttl.back(100)
for c, x in zip(bg_colors, font_color):
    ttl.getscreen().bgcolor(c)
    ttl.color(x)
    for i in range(50):
        ttl.forward(200)
        ttl.left(167)

ttl.hideturtle()    # hides the black pointer(i.e.turtle)
turtle.done()
