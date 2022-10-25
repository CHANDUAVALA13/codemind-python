n=int(input())
d=0
while True:
    c=0
    while n:
        d=n%10
        n=n//10
        c+=d
    n=c
    if n>=0 and n<=9:
        break
print(n)