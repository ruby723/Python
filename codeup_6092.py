n=int(input())
a=input().split()
b=[]
for i in range(23):
    b.append(0)
for i in range(n):
    a[i]=int(a[i])
    b[a[i]-1]+=1
for i in range(23):
    print(b[i],end=" ")