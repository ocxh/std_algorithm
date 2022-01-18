arr = input()
arr = list(arr)
t = input()
visited = [False] * len(arr)

count = 0
for i in range(len(arr)):
    buf = ""
    if i + (len(t) - 1) >= len(arr):
        break
    for j in range(len(t)):
        if visited[i + j] == True:
            break
        buf += arr[i + j]

    if buf == t:
        count += 1
        for j in range(len(t)):
            visited[i + j] = True

print(count)
