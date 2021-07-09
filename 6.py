a,b=map(int,input().split())
sum1,sum2=0,0
for i in range(a,b+1):
    temp=i
    for i in range(0,3):
        if temp%10==1:
            sum1+=1
        if temp%10==5:
            sum2+=1
        temp//=10
print(sum1,sum2,sep=' ')
