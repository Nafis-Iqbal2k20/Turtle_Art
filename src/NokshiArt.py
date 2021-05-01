import turtle
import math
artist = turtle.Turtle()
artist.speed(10)
# artist.screen.tracer(0, 0)
for i in range(1800):
    artist.forward(math.sqrt(i))
    artist.left(i % 180)

artist.screen.mainloop()
