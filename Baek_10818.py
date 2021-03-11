n=int(input())

a=input().split()
min=1000001
max=-1000001
for i in range(n):
    a[i]=int(a[i])

    if a[i]<min:
        min=a[i]
    if a[i]>max:
        max=a[i]
print(min,max)