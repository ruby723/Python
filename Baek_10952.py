a=1
b=1
i=0
sum=[]
while (a!=0 or b!=0):
    a,b=map(int,input().split())
    sum.append(a+b) 
    i+=1

for j in range(i-1):
    print(sum[j])




    