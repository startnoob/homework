n=int(input())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(' ',end='')
    for j in range(1,2*i):
        print(j,end='')
    for j in range(0,n-i):
        print(' ',end='')
    print(' ')
   

