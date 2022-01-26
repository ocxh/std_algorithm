import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
arr = [1] * n
res = []

# DP를 사용한 최장거리 구하기
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            arr[i] = max(arr[i], arr[j] + 1)

max_len = max(arr)
print(max_len)

# n-1부터 0까지 최장거리 요소에 해당하는 값 구하기
for i in range(n - 1, -1, -1):
    if max_len == arr[i]:
        res.append(a[i])
        max_len -= 1


for i in range(len(res) - 1, -1, -1):
    print(res[i], end=" ")
