a,d,n=map(int,input().split())
if a>=0 and a<=100 and d>=0 and d<=100 and n>=0 and n<=100:
    for i in range(1,n):
        a=a+d
    print(a)
        