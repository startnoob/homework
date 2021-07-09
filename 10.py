for x1 in range(1,100):
    for x2 in range(1,100):
        for x3 in range(1,100):
            for x4 in range(1,100):
                if x1*10+x2*5+x3*2+x4==100 and x1+x2+x3+x4==40:
                    print(x1,x2,x3,x4,sep=' ')
