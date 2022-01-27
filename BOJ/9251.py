a = list(input())
b = list(input())


def LCS(a, b):
    length = [0] * len(b)

    for i in range(len(a)):
        now = 0
        for j in range(len(b)):
            if now < length[j]:
                now = length[j]
            elif a[i] == b[j]:
                length[j] = now + 1

    return max(length)


if len(a) > len(b):
    print(LCS(a, b))
else:
    print(LCS(b, a))
