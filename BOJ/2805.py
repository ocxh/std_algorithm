n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
mid = (start + end) // 2
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    total = sum([i - mid for i in arr if mid < i])
    if total == m:
        result = mid
        break
    elif total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
