#설탕공장

n=int(input())

if n%5==0:
    print(n//5)
elif n//5==0:
    if n%3!=0:
        print(-1)
    else:
        print(n//3)
else:
    five=n//5
    for i in range(five,-1,-1):
        if i==0 and n%3==0:
            print(n//3)
            break
        if i==0 and n%3!=0:
            print(-1)
            break
        three=n-(5*i)
        if (three)%3==0:
            a=i
            b=(three)//3
            print(a+b)
            break
