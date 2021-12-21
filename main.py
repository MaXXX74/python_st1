# функция для печати поля
def print_field(f, rows, cols):
    for i in range(rows):
        for j in range(cols):
            cell = f[i][j]
            if cell == 0:
                print(".", end=" ")
            elif cell == -1:
                print("*", end=" ")
            else:
                print(f[i][j], end=" ")
        print()


rows, cols, mines = (int(i) for i in input().split())  # вводим коли-во строк поля, ячеек и мин
field = [cols * [0] for i in range(rows)]  # заполняем поле 0-ми
for i in range(mines):  # вводим координаты мин с 1
    mine_row, mine_col = (int(j) - 1 for j in input().split())
    field[mine_row][mine_col] = -1

for curr_row in range(rows):  # пробегаем по всему полю
    for curr_col in range(cols):
        if field[curr_row][curr_col] == -1:  # если найдена мина -
            for check_row in range(curr_row - 1, curr_row + 2):
                for check_col in range(curr_col - 1, curr_col + 2):
                    if (0 <= check_row < rows) and (0 <= check_col < cols) and (field[check_row][check_col] != -1):
                        field[check_row][check_col] += 1

print_field(field, rows, cols)
