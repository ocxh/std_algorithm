n = int(input())
arr = []
res = [0] * n
for i in range(n):
    arr.append(int(input()))

res[0] = arr[0]

if n > 1:
    res[1] = arr[0] + arr[1]
if n > 2:
    res[2] = max(arr[0] + arr[2], res[1], arr[1] + arr[2])

if n > 3:
    for i in range(3, n):
        # 현재를 제외, 현재와 이전, 현재와 전전
        res[i] = max(res[i - 1], arr[i] + arr[i - 1] + res[i - 3], arr[i] + res[i - 2])

print(res[-1])
