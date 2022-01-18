import sys

n, c = map(int, input().split())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
data.sort()

result = 0
start = 1
end = data[-1] - data[0]

while start <= end:
    count = 1
    mid = (start + end) // 2
    now = data[0]
    for i in range(1, len(data)):
        if now + mid <= data[i]:
            count += 1
            now = data[i]

    if count >= c:
        start = mid + 1
        result = mid
        print(result)
    else:
        end = mid - 1
print(result)
