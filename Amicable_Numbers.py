a=int(input())
b=int(input())
#proper factor sum of a
pfs_a=0
for i in range (1,a):
    if a%i==0:
        pfs_a+=i
#proper factor sum of b
pfs_b=0
for i in range (1,b):
    if b%i==0:
        pfs_b+=i
#condition
if pfs_a==b and pfs_b==a:
    print("Amicable")
else:
    print("Not Amicable")