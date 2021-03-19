#달팽이
import sys
a,b,v=map(int,sys.stdin.readline().split())

now=(v-a)//(a-b)

if (v-a)%(a-b)==0:
    print(now+1)
else:
    print(now+2)