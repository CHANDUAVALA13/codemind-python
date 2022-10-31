n = input()
p = 0
for i in n:
    if n.count(i) > 1:
        p += 1
        break
if p == 0:
    print("Unique Number")
else:
    print("Not Unique Number")