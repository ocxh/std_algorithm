n = int(input())
arr = list(map(int, input().split()))
lds = [1] * n

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i]:
            lds[i] = max(lds[i], lds[j] + 1)

print(max(lds))
