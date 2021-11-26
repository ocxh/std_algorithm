# 파이썬 문법에 익숙하지 않아 헷갈리는 코드는 이곳에서 테스트합니다
# 알고리즘 공부중 풀이한 문제는 이곳에서 풀이합니다. (풀이를 따로 기록할 경우 별도 파일 만듬)

import sys
from collections import deque

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def bfs(v):
    q = deque([v])

    while q:
        buf = q.popleft()
        for i in graph[buf]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
