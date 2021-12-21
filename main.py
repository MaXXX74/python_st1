n = int(input())
sch = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if sch >= n:
            break
        else:
            print(i, end=" ")
            sch += 1
