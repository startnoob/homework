f=[0,1]
a=int(input())
for i in range(2,a+1):
    f.append(f[i-1]+f[i-2])
print(f[a])
