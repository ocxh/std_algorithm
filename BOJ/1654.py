import sys

k, n = map(int, input().split())
data = [int(sys.stdin.readline().strip()) for i in range(k)]

start = 1
end = max(data)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in data:
        total += i // mid

    if total >= n:
        if mid > result:
            result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
