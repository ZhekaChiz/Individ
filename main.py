import random

# Создаем карту размером 20x20
map = [[0 for x in range(20)] for y in range(20)]
# Размещаем случайные препятствия на карте
for i in range(30):
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    map[y][x] = -1
def set_robot_positions(robot_positions):
    for i, (start, end) in enumerate(robot_positions):
        # Проверяем, что начальная и конечная точки не находятся внутри препятствий и не пересекаются с другими роботами
        if map[start[1]][start[0]] != 0 or map[end[1]][end[0]] != 0:
            raise ValueError(f"Плохой путь для робота {i}")
        for j, (other_start, other_end) in enumerate(robot_positions[:i]):
            if start == other_start or start == other_end or end == other_start or end == other_end:
                raise ValueError(f"Робот под № {i} пересекается с роботом {j}")
        # Размещаем робота на карте
        map[start[1]][start[0]] = i+1
        map[end[1]][end[0]] = i+1
def move_robot(start, end, robot_num):
    path = []
    x, y = start
    dx = 1 if end[0] > start[0] else -1
    dy = 1 if end[1] > start[1] else -1
    while (x, y) != end:
        map[y][x] = robot_num
        path.append((x, y))
        if x != end[0]:
            x += dx
        elif y != end[1]:
            y += dy
    map[y][x] = robot_num
    path.append((x, y))
    return path
# Задаем начальные и конечные точки для трех роботов
robot_positions = [ ]
for i in range(3):
    start = eval(input(f"Задайте стартовую позицию для {i+1}: "))
    end = eval(input(f"Задайте конечную позицию для {i+1}: "))
    robot_positions.append((start, end))
# Перемещаем каждого робота
for i, (start, end) in enumerate(robot_positions):
    path = move_robot(start, end, i+1)
    print(f"Путь для робота № {i+1}: {path}")
# Отображаем карту с путями роботов
for row in map:
    for col in row:
        if col == 0:
            print(".", end="")
        elif col == -1:
            print("#", end="")
        else:
            print(chr(ord("1")+col-1), end="")
    print()