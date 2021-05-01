import turtle

artist = turtle.Turtle()
artist.speed(5)
artist.color("red", "yellow")
artist.begin_fill()
for i in range(80):
    artist.forward(300)
    artist.left(168.5)
artist.end_fill()

artist.screen.mainloop()
