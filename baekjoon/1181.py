import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for i in range(n)]

arr.sort(key=len)
ot_arr = arr.sort()

for i in range(n):
    for j in range():
    if len(arr[i]) == len(arr[i+1]):
