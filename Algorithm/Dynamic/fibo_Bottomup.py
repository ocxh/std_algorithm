n = 99
arr = [0] * 100

arr[1] = 1
arr[2] = 1

for i in range(3, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2]
