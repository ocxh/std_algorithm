import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
buf = [0]

for i in arr:
    if buf[-1] < i:
        buf.append(i)
    else:
        start = 0
        end = len(buf)

        while start < end:
            mid = (start + end) // 2

            if buf[mid] < i:
                start = mid + 1
            else:
                end = mid
        buf[end] = i

print(len(buf) - 1)

