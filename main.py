n = int(input())
field = [n * [0] for i in range(n)]
row = step = 0        # тек.строка, номер шага
col = -1              # тек.колонка
move = "right"        # тек.направление движения
while step < n * n:
    if (move == "right"):
        if col < n-1 and field[row][col+1] == 0:
            step += 1
            field[row][col+1] = step
            col += 1
        else:
            move = "down"
    if (move == "down"):
        if row < n-1 and field[row+1][col] == 0:
            step += 1
            field[row+1][col] = step
            row += 1
        else:
            move = "left"
    if (move == "left"):
        if col > 0 and field[row][col-1] == 0:
            step += 1
            field[row][col-1] = step
            col -= 1
        else:
            move = "up"
    if (move == "up"):
        if row > 0 and field[row-1][col] == 0:
            step += 1
            field[row-1][col] = step
            row -= 1
        else:
            move = "right"
for row in range(n):
    for col in range(n):
        print(field[row][col], end=" ")
    print()
