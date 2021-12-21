lst = [int(i) for i in input().split()]
find_num = int(input())
if find_num not in lst:
    print("Отсутствует")
else:
    for i in range(len(lst)):
        if find_num == lst[i]:
            print(i, end=" ")