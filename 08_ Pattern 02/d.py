r = int(input("number:"))
q = r
w = r - r + 1
for i in range(0,q):
    for j in range(0,w):
        print("*",end="")
    print()
    w += 1
    if w == q + 1:
        break
