def sum(x):
    ans=0
    for i in range(0,3):
        ans+=(x%10)**3
        x//=10
    return ans
a=int(input())
su=0
for i in range(100,a+1):
    if sum(i)==i:
        print(i)

