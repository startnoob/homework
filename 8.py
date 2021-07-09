def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=int(input())
for i in range(2,a+1):
    if a%i==0 and prime(i):
        print(i,end=' ')


