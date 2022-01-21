A = int(input())
arr = list(map(int, input().split()))
res = [1] * A

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j]:
            res[i] = max(res[i], res[j] + 1)


print(max(res))
