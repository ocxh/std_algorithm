n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 1
bf = arr[0]

for i in range(1, n):
    if arr[i] - bf >= l:
        bf = arr[i]
        cnt += 1

print(cnt)
