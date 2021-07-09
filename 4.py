a,ans=int(input()),0
for i in range(1,a):
    ans+=i*(a%i==0)
if ans==a:
    print("yes")
else:
    print("no")

