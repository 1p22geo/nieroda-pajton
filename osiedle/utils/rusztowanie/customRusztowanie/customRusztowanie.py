import lib.move


def customRusztowanie(t, x=50, y=40, step=10, circle_radius=5, horizontal_length=100):
    # Draw horizontal line and vertical lines
    lib.move.move(t, x, y)
    t.goto(x + horizontal_length, y)
    t.goto(x + horizontal_length - 10, y)
    t.goto(x + horizontal_length - 10, y - 40)
    t.goto(x + horizontal_length - 20, y - 40)
    t.goto(x + horizontal_length - 20, y)

    # Draw circles along the horizontal line
    for i in range(10, horizontal_length + 1, step):
        lib.move.move(t, x + i, y)
        t.right(180)
        t.circle(circle_radius, 180)