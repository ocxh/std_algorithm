n = list(map(int, input()))
n.sort(reverse=True)
if n[len(n) - 1] == 0 and sum(n) % 3 == 0:
    for i in n:
        print(i, end="")
else:
    print(-1)
