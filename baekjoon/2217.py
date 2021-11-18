import sys

n = int(input())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
data.sort(reverse=True)
result = 0

for i in range(n):
    total = data[i] * (i + 1)
    if total > result:
        result = total
print(result)
