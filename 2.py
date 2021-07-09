a,b=map(int,input().split())
ans=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        ans=i
print(i)
