import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 노드와 간선 개수 입력 받기
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 2차원 리스트 그래프를 무한으로 초기화

# 자기 자신과는 연결되어있음
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선을 입력 받아 a와 b가 연결되어있다는 표시로 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 0

# 플로이드 워셜 알고리즘을 통해 a->b가 아니여도 a->k->b 관계에 있어도 연결되어있다고 체크
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# a->b라면 b->a로 연결 되어 있다는 표시로 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 0:
            graph[j][i] = 0

# i번째 노드가 모든 노드에 연결되어있다면(0) res 증가
res = 0
for i in range(1, n + 1):
    if INF not in graph[i][1:]:
        res += 1

print(res)
