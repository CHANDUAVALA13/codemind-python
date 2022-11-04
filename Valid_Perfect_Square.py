n=int(input())
for i in range (n):
    a=int(input())
    b=a**0.5
    if int(b+0.5)**2==a:
        print("True")
    else:
        print("False")