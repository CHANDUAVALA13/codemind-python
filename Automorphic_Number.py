n = int(input())
s = str(n)
sq = str(n*n)
if sq[-len(s):] == s:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")