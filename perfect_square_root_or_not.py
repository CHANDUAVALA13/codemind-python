import math
n=int(input())
a=math.sqrt(n)
if int(a+0.5)**2==n:
    print("True")
else:
    print("False")