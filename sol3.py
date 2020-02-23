n = bin(int(input()))
print(n)
a = []
count = 1
for i in range(1, len(n)):
    if(n[i-1]==n[i]):
        count+=1
        a.append(count)
    else:
        count = 1
print(max(a))
