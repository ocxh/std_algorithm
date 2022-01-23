buf = [0, 1, 2, 7, 12]
print(buf)
i = int(input())

start = 0
end = len(buf)
while start < end:
    mid = (start + end) // 2

    if buf[mid] < i:
        start = mid + 1
    else:
        end = mid
buf[end] = i

print(buf)
