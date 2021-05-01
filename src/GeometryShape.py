import turtle


def square():
    artist = turtle.Turtle()
    for i in range(4):
        artist.forward(100)
        artist.left(90)


def triangle():
    artist = turtle.Turtle()
    artist.penup()
    artist.forward(200)
    artist.pendown()
    for i in range(3):
        artist.forward(100)
        artist.left(120)


def circle():

    artist = turtle.Turtle()
    artist.penup()
    artist.backward(160)
    artist.pendown()
    artist.circle(60)


def rectangle():
    artist = turtle.Turtle()
    artist.left(90)
    artist.penup()
    artist.forward(150)
    artist.pendown()
    artist.right(90)
    for i in range(2):
        artist.forward(200)
        artist.left(90)
        artist.forward(100)
        artist.left(90)


def point():
    artist = turtle.Turtle()
    artist.right(90)
    artist.penup()
    artist.forward(50)
    artist.pendown()
    artist.hideturtle()
    artist.dot(10, "black")


square()
triangle()
circle()
rectangle()
point()
turtle.Turtle().screen.mainloop()
