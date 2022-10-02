n=int(input())
s=0
p=1
while n>0:
    s=n%10+s
    p=n%10*p
    n=n//10
print(p-s)