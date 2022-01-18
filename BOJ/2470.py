n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1

result = [0, 0]
ans = 2e9 + 1
while start < end:
    total = arr[start] + arr[end]

    if abs(total) < ans:
        ans = abs(total)
        result[0], result[1] = arr[start], arr[end]

    if total < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])
