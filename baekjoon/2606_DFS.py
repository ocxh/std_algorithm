coms = int(input())  # 컴퓨터 대수
n = int(input())  # 노드 개수

# 그래프 만들기
graph = [[] for i in range(coms + 1)]

# 각 노드 입력받아 그래프에 넣기
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리 초기화
visited = [False] * (coms + 1)


def dfs(v, graph, visited):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, graph, visited)


dfs(1, graph, visited)
print(visited.count(True) - 1)
