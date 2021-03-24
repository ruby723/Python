import sys
import math

t=int(sys.stdin.readline())

hap=[0]*t
for i in range(t):
    x,y=map(int,sys.stdin.readline().split())
    dis=y-x
    n=int(math.sqrt(dis))-1
    while True:
        n+=1
        if dis>(n-1)*(n-1) and dis<=(n*(n-1)):
            hap[i]=2*(n-1)
            break
        elif dis<=n*n and dis>(n*(n-1)):
            hap[i]= n+(n-1)
            break
    
for i in range(t):
    print(hap[i])