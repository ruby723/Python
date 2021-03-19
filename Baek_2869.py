import sys
a,b,v=map(int,sys.stdin.readline().split())

day=v//a
now=a

while True:
    day+=1
    now+=(a-b)
    if now>=v:
        break
    now-=b



print(day)