#지그재그 분수

import sys
n=int(sys.stdin.readline())

i=0
c=0
tf=True
while tf:
    i+=1
    for j in range(1,i+1):
        a=j
        b=i-a+1
        c+=1
        if c==n:
            tf=False
            break
if i%2==0:
    print("{0}/{1}".format(a,b))
else:
    print("{0}/{1}".format(b,a))