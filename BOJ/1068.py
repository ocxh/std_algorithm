import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

k = int(input())


def dfs(num):
    arr[num] = -2
    for i in range(len(arr)):
        if arr[i] == num:
            dfs(i)


dfs(k)

count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1

print(count)
