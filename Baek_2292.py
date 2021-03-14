n=int(input())

a=[0]*n
a[1]=1
a[2]=2

for i in range(3,n):
    a[i]=a[i-1]+(6*(i-2))

for i in range(n-1,1,-1):
    if n>=a[i]:
        count=i
        break

print(count)