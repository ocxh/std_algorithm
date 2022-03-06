n = int(input())


def hanoi(num, start, mid, end):
    if num == 1:
        print(start, end)
    else:
        hanoi(num - 1, start, end, mid)
        print(start, end)
        hanoi(num - 1, mid, start, end)


cnt = 2 ** n - 1
print(cnt)
if n <= 20:
    hanoi(n, 1, 2, 3)
