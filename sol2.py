s = input().split(',')
s = sorted([str(i) for i in s], reverse = True)
print(s)
for i in range(1,len(s)):
    if(s[i-1][0] and len(s[i-1])>len(s[i])):
        t = s[i-1]
        s[i-1] = s[i]
        s[i] = t
b = ''
for i in range(0,len(s)):
    b = b+s[i]
    print(int(b))
