n=int(input())
rev=0
fc_n=0
fc_rev=0
n1 = n
while n1>0:
    r=n1%10
    rev=rev*10+r
    n1=n1//10
for i in range (1,n+1):
    if n%i==0:
        fc_n=fc_n+1
for i in range (1,rev+1):
    if rev%i==0:
        fc_rev+=1
if fc_n==fc_rev==2:
    print("circular prime")
elif fc_n==2:
    print("prime but not a circular prime")
else:
    print("not prime")