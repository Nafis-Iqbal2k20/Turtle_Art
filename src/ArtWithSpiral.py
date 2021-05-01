import turtle

artist = turtle.Turtle()
artist.speed(10)
artist.screen.bgcolor("black")
colors = ["red", "yellow", "purple", "green", "blue", "orange"]
# artist.screen.tracer(0, 0)
for x in range(300):
    artist.fd(x)
    artist.color(colors[x % 6])
    artist.left(59)
artist.screen.mainloop()
