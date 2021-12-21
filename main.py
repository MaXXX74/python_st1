sum = square = 0
while True:
    num = int(input())
    square += num ** 2
    sum += num
    if sum == 0:
        break
print(square)
