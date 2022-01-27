n = int(input())
arr = list(map(int, input().split()))


def bitonic(arr):
    maxValue = 0
    lis = [1] * n
    lds = [1] * n

    # 최장 증가 부분 수열
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)

    # 최장 감소 부분 수열
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1)

    # 최장 바이토닉 부분 수열
    for i in range(n):
        maxValue = max(maxValue, lis[i] + lds[i] - 1)

    return maxValue


print(bitonic(arr))
