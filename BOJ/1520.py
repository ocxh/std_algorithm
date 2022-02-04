import sys

sys.setrecursionlimit(10 ** 9)
sys.stdin.readline

m, n = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split())))
dp = [[-1] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if y == m - 1 and x == n - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[ny][nx] < arr[y][x]:
                dp[y][x] += dfs(nx, ny)
    return dp[y][x]


print(dfs(0, 0))
