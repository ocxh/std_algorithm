n=int(input())
result=list()
def gcd(a, b):
    r=b%a
    if r==0:
        return a
    else:
        return gcd(r,a)

for i in range(n):
    a, b = map(int, input().split())
    result.append(int((a*b)/gcd(a,b)))

for i in range(n):
    print(result[i])