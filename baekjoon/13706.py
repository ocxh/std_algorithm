n = int(input())


start=0
end=n
mid = (start+end)//2

while(start<=end):
    if n==(mid**2):
        print(mid)
        break
    elif n>(mid**2):
        start = mid+1
            
    elif n<(mid**2):
        end = mid-1
            
        
    mid = (start+end)//2

