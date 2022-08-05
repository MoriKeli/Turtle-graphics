import turtle

ttl = turtle.Turtle()
COLOR = (0.60160, 0, 0.99920)
target = (0.86330, 0.47660, 0.31255)

turtle.Screen().tracer(False)
width = turtle.Screen().window_width()
height = turtle.Screen().window_height()

deltas = [(hue - COLOR[index]) / height for index, hue in enumerate(target)]

ttl.color(COLOR)

ttl.penup()     # lift turtle
ttl.goto(-width/2, height/2)
ttl.pendown()

direction = 1

for distance, y in enumerate(range(height//2, -height//2, -1)):
    ttl.forward(width * direction)
    ttl.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    ttl.sety(y)
    direction *= -1

turtle.Screen().tracer(True)
turtle.done()
