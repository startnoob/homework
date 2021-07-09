n,k=map(int,input().split())
sum1=n
while n>=k:
    sum1+=sum1//k
    n%=k
print(sum1)
