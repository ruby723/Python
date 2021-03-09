# 설탕과자 뽑기
h,w=map(int,input().split())
a=[[0]*h for _ in range(w)]
n=int(input())

for i in range(n):
    l,d,x,y=map(int,input().split())

    for j in range(l):
        if d==0:
            a[y-1+j][x-1]=1
        elif d==1:
            a[y-1][x-1+j]=1

for i in range(h):           
    for j in range(w):
        print(a[j][i],end=" ")
    print("")