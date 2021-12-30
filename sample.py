# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())  # 노드, 수색범위, 간선 개수
arr = [[INF] * (n + 1) for _ in range(n + 1)]
item = list(map(int, input().split()))

for i in range(1, n + 1):
    arr[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)
    arr[b][a] = min(arr[a][b], c)


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

get = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] <= m:
            get[i] += item[j - 1]

print(max(get))
