import turtle
artist = turtle.Turtle()
artist.color("green")
artist.goto(0, -100)
artist.left(90)
# artist.speed(10)  # 150 speed is perfect for this art
artist.screen.tracer(0, 0)


def tree(i):
    if i > 10:
        artist.forward(i)
        artist.left(30)
        tree(3 * i / 4)
        artist.right(60)
        tree(3 * i / 4)
        artist.left(30)
        artist.backward(i)
    else:
        for i in range(1):
            break


tree(100)
artist.screen.mainloop()
