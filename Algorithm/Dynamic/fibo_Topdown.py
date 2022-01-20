arr = [0] * 99


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if arr[x] == 0:
        arr[x] = fibo(x - 1) + fibo(x - 2)

    return arr[x]
