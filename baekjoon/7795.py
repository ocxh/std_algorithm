t = int(input())
result = list()


def binary_search(num, am):
    start = 0
    end = len(am) - 1
    total = 1.5
    while start <= end:
        mid = (start + end) // 2
        if am[mid] < num:
            total = mid
            start = mid + 1
        else:
            end = mid - 1

    if total == 1.5:
        total = 0
    else:
        total += 1
    return total


for i in range(t):
    n, m = map(int, input().split())
    an = list(map(int, input().split()))
    am = list(map(int, input().split()))
    am.sort()
    alls = 0

    for j in an:
        alls += binary_search(j, am)
    result.append(alls)

for i in range(t):
    print(result[i])
