from random import choice

size = int(input("Введите размеры поля: "))
M = int(input("Введите количество поколений (шагов): "))
dead = "."
live = "*"


def neighbors_xy(x, y):
    for dx, dy in (
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ):
        yield x + dx, y + dy


def show_field(field):
    for y in range(size):
        print(" ".join(field[y]))


def get_empty_field():
    return [[dead for x in range(size)] for y in range(size)]


def is_live(field, neighbor_x, neighbor_y):
    return (
        0 <= neighbor_x < size
        and 0 <= neighbor_y < size
        and field[neighbor_x][neighbor_y] == live
    )


field = [[choice([dead, live]) for x in range(size)] for y in range(size)]

for _ in range(M):
    input("Нажмите любую клавишу для следующего шага: ")
    show_field(field)
    buffer = get_empty_field()
    for y in range(size):
        for x in range(size):
            c = field[y][x]
            live_neighbors = 0
            for neighbor_x, neighbor_y in neighbors_xy(x, y):
                live_neighbors += 1 if is_live(field, neighbor_x, neighbor_y) else 0
            if c == dead:
                buffer[y][x] = live if live_neighbors == 3 else dead
            else:
                buffer[y][x] = live if live_neighbors in (2, 3) else dead

    if field == buffer:
        print("done")
        break
    field = buffer
