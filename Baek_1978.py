import sys

n=int(sys.stdin.readline())

p=list(map(int,sys.stdin.readline().split()))

count=0

for i in range(n):
    for j in range(2,p[i]+1):
        if j==p[i]:
            count+=1
        elif p[i]%j==0:
            break

print(count)