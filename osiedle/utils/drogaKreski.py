import lib.move


def drogaKreski(t, x=-250, y=-12.5, step=20, lines=25):
    # Horizontal lines
    for i in range(lines):
        lib.move.move(t, x + step * i, y)
        t.goto(x + step * i + step * 1 / 2, y)

    # Vertical lines
    vertical_start_points = [-112.5, 87.5]
    vertical_step = 20
    vertical_lines = 8

    for start_x in vertical_start_points:
        for j in range(vertical_lines):
            lib.move.move(t, start_x, y - vertical_step * (j + 1))
            t.goto(start_x, y - vertical_step * (j + 1.5))
