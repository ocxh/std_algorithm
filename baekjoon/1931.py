n = int(input())
wl = []
last_index = 0
count = 0

for i in range(n):
    wl.append(list(map(int, input().split())))

wl.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    if wl[i][0] >= last_index:
        last_index = wl[i][1]
        count += 1

print(count)
