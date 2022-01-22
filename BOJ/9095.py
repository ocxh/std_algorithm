t = int(input())
max_n = 0
n = []
for i in range(t):
    n.append(int(input()))
    max_n = max(max_n, n[-1])

arr = [0] * 12
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in range(4, max_n + 1):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

for i in n:
    print(arr[i])
