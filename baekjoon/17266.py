n = int(input())  # 굴다리의 길이
m = int(input())  # 가로등의 개수
arr = list(map(int, input().split()))  # 가로등의 x좌표들

# 가로등 사이의 거리중 최대 거리
dis = 0
if m != 1:
    for i in range(1, m):
        bf = arr[i] - arr[i - 1]
        if bf % 2 != 0:
            bf = bf // 2 + 1
        else:
            bf = bf // 2

        if bf > dis:
            dis = bf


maxn = max(arr[0], n - arr[m - 1], dis)  # 3가지 측정거리중 가장 큰 거리
print(maxn)
