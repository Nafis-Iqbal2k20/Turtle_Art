import turtle

artist = turtle.Turtle()
artist.begin_fill()
artist.color('red')
artist.left(155)
artist.forward(175)
artist.circle(-90, 175)
artist.setheading(60)
artist.circle(-90, 175)
artist.forward(175)
artist.end_fill()

artist.screen.mainloop()
