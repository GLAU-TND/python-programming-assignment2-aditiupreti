a = input().split(',')
b = a
c = d = 0
r = []
e = b[0][-1]
r.append(b[0])
b.remove(b[0])
b.sort()
for i in range(len(a)):
    for j in b:
        c = 0
        if e == j[0]:
            r.append(j)
            b.remove(j)
            e = j[-1]
            c += 1
        if c == 1:
            break
print(r)  
            

