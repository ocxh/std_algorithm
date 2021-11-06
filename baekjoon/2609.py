n, m = map(int, input().split())

max1=0 #최대공약수
max2=0 #최소공배수
a=min(n,m)
b=max(n,m)
def gcd(a, b):
    r=b%a
    if r==0:
        return a
    else:
        return gcd(r,a)

max1=gcd(n, m)
max2=int((n*m)/max1)

print(max1) 
print(max2)