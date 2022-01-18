import sys

n = int(input())
data = [int(sys.stdin.readline().strip()) for i in range(n)]
data.sort()
rdata = list()
for i in range(1, n + 1):
    rdata.append(i)
angry = 1000000000000000000
now = 0
for i in range(n):
    buffer = data[i] - rdata[i]
    if buffer < 0:
        buffer *= -1
    now += buffer
if angry > now:
    angry = now
print(angry)
