
""" 
mov = 0
count = 0
for i in range(v):
    mov+=a
    count+=1
    if mov>=v:
        print(count)
        break
    mov-=b 
"""
a, b, v = map(int, input().split())
dif = a-b
offset=a*(v//a)

#an = a+(n-1)*dif
#(an/dif-a/dif+1)=n

n = int(offset/dif)-int(a/dif)+1

while True:
    if offset>=v:
        break
    offset+=dif
    n+=1

print(n)