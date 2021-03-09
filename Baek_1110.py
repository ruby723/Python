n=k=int(input())
i=0

while True:
    a=n//10
    b=n%10
    
    m=(b*10)+((a+b)%10)
    i+=1
    n=m
    if n==k:
        break

print(i)
