num=int(input())
n=num
sum=0
ans=0
while sum!=1 and sum!=4:
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**2
        n=n//10
    n=sum
    if sum==1:
        ans=1
if ans==1:
    print("True")
else:
    print("False")