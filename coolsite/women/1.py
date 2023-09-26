import math

x=float(input())

if x>0:
    y=x-0.5
    print("y=",y)
elif x==0:
    y=0
    print("y=",y)
elif x<0:
    y=math.fabs(x)
    print("y=",y)
