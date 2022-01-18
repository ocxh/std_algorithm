INF = int(1e9)

# 노드의 개수
n = int(input())
# 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신의 경로
for i in range(1, n + 1):
    graph[i][i] = 0
# 연결 관계 입력 받기
while True:
    a, b = map(int, input().split())
    if a + b == -2:
        break
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == 0 or graph[a][b] == 1:
                continue
            if graph[a][b] > (graph[a][k] + graph[k][b]):
                graph[a][b] = graph[a][k] + graph[k][b]

r = []
for i in range(1, n + 1):
    r.append(max(graph[i][1:]))

m = min(r)
print(m, r.count(m))
for i, v in enumerate(r):
    if v == m:
        print(i + 1, end=" ")
