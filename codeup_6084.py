# code up 6084_ 소리파일 저장용량 계산
h,b,c,s=input().split()
h=int(h)
b=int(b)
c=int(c)
s=int(s)
#h,b,c,s=map(int,input().split())
if h<=48000 and b<=32 and b%8==0 and c<=5 and s<=6000 and h>0 and b>0 and c>0 and s>0:
    sum=h*b*c*s/8/1024/1024
    print(round(sum,1),"MB")
