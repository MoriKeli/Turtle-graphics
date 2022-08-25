import turtle
# loadWindow = turtle.Screen()
ttl = turtle.Turtle()
ttl.getscreen().bgcolor('black')
ttl.speed(12)
ttl.hideturtle()
colors = ['red', 'blue', 'green', 'orange', 'yellow', '#fff', 'aqua', 'salmon']

for i in range(100):
    ttl.pencolor(colors[i % len(colors)])   # modulus prevents "IndexError: list index out of range"
    # ttl.getscreen().bgcolor(colors[i % len(colors)])
    ttl.circle(5*i/5)
    ttl.circle(-5*i/5)
    ttl.left(i/5)

turtle.done()