a=input()
if a[0]=='-':
    print('-',a[-1:-len(a):-1],sep='')
else:
    print(a[-1:-len(a)-1:-1])
