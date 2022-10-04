n=int(input())
s=str(n)
m=""
rev=""
for i in s:
    m=i+m
p=int(m)*int(m)
org=n*n
a=str(p)
for i in a:
    rev=i+rev
if (org==int(rev)):
    print("True")
else:
    print("False")