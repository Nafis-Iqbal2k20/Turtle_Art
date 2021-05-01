import turtle

artist = turtle.Turtle()
artist.speed(10)
artist.screen.bgcolor("black")
colors = ["red", "yellow", "purple"]
# artist.screen.tracer(0, 0)
for x in range(100):
    artist.circle(x)
    artist.color(colors[x % 3])
    artist.left(60)
artist.screen.mainloop()
