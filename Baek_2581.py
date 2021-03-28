import sys

m=int(sys.stdin.readline())
n=int(sys.stdin.readline())

min=10000
hap=0

for i in range(m,n+1):
    for j in range(2,(i//2)+2):
        if j==(i//2)+1:
            if i<min:
                min=i
            hap+=i
        elif i%j==0:
            break
if hap==0:
    print(-1)
else:
    print(hap)
    print(min)

