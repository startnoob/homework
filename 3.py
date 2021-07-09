def check(x):
    for i in range(2,x):
        if x%i==0: return "No"
    return "Yes"

print(check(int(input())))
