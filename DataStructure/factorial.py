#반복문 팩토리얼
def iterative_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)

#재귀함수 팩토리얼
def recursive_factorial(n):
    if n<=1:
        return 1
    return n * recursive_factorial(n-1)

print(recursive_factorial(3))