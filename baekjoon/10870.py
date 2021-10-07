def self(n):
    if n<= 1:
        return n
    return self(n-1) + self(n-2)

n = int(input())
print(self(n))
