n=int(input())
a=0
s=n*n
while s>0:
    r=s%10
    a+=r
    s=s//10
if a==n:
    print("Neon Number")
else:
    print("Not Neon Number")