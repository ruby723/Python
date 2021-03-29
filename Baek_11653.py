import sys

n=int(sys.stdin.readline())
i=1
# if n!=1
while True:
    i+=1
    if n%i==0:
        print(i)
        n=n/i
        i=1
    elif i==(n//4)+1:
        print(int(n))
        break