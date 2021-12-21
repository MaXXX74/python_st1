# вводим первоначальные значения
matrix = []
while True:
    s = input()
    if s != "end":
        matrix.append([int(i) for i in s.split()])
    else:
        break
# расчет и вывод
rows = len(matrix)
cols = len(matrix[0])
for x in range(rows):
    for y in range(cols):
        print(matrix[x-1][y] + matrix[(x+1) % rows][y] + matrix[x][y-1] + matrix[x][(y+1) % cols], end=" ")
    print()
