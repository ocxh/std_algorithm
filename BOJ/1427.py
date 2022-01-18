n = list(map(int, input()))
n.sort(reverse=True)
for i in range(0, len(n)):
    print(n[i], end="")
