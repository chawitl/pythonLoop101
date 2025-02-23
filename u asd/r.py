p = input().split()
c = input()
co = 0
for i in range(len(p)):
    if c == p[i]:
        co += 1 
print(co)