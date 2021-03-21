import sys

def apart(k,n):
    p=0
    if k==0:
        p+=n
    else:
        for i in range(1,n+1):
            p+=apart(k-1,i)
    return p

t=int(sys.stdin.readline())
k=[0]*t
n=[0]*t
for i in range(t):
    k[i]=int(sys.stdin.readline())
    n[i]=int(sys.stdin.readline())

for i in range(t):
    print(apart(k[i],n[i]))