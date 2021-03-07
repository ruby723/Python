w,h,b=map(int,input().split())
mb=w*h*b/8/1024/1024

if w>=1 and w<=1024 and h>=1 and h<=1024 and b<=40 and b%4==0:
    print("{0:.2f} MB".format(mb))