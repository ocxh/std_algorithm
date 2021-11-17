# 사용자에게 입력
n = int(input())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
result = 0
an.sort()
bn.sort(reverse=True)

# an[0]*bn[0]+ ''' +a[n-1]*b[n-1]
for i in range(n):
    result += an[i] * bn[i]
print(result)  # 최종출력
