INF = int(1e9)

n = int(input())  # 노드의 개수
m = int(input())  # 간선의 개수

arr = [[INF] * (n + 1) for _ in range(n + 1)]  # 그래프를 무한으로 초기화

# 자기 자신에게 가는 비용은 0
for i in range(1, n + 1):
    arr[i][i] = 0

# 간선을 입력 받을 때 기존에 있던 값과 비교하여 더 작은 값을 넣는다
# arr[a][b]는 기존의 값, c는 새로운 값
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)

# 플리이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF:
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()
