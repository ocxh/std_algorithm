n, k = map(int, input().split())

cnt = []


def hanoi(num, start, mid, end):
    if num == 1:
        cnt.append([start, end])
    else:
        hanoi(num - 1, start, end, mid)
        cnt.append([start, end])
        hanoi(num - 1, mid, start, end)


hanoi(n, 1, 2, 3)

print(cnt[k - 1][0], cnt[k - 1][1])
