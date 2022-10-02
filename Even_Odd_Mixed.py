n=int(input())
s=str(n)
a=0
b=0
for i in s:
    if(int(i)%2==0):
        a+=1
    else:
        b+=1
if (a==len(s)):
    print("Even")
elif(b==len(s)):
    print("Odd")
else:
    print("Mixed")