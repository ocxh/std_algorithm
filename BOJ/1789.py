s = int(input())

for i in range(1, s + 1):
    offset = (i * (1 + i)) // 2
    if offset == s:
        print(i)
        break
    elif offset > s:
        print(i - 1)
        break
