# 바둑알 십자 뒤집기
a=[[0]*19 for n in range(19)]

for i in range(19):
    b=input().split()
    for j in range(19):
        b[j]=int(b[j])
        a[i][j]=b[j]

n=int(input())

for i in range(n):
    m=input().split()
    for j in range(2):
        m[j]=int(m[j])
    w=m[0]-1
    h=m[1]-1
    for k in range(19):
        if a[w][k]==0:
            a[w][k]=1
        else:
            a[w][k]=0

        if a[k][h]==0:
            a[k][h]=1
        else:
            a[k][h]=0

for i in range(19):
    for j in range(19):
         print(a[i][j],end=" ")
    print("")