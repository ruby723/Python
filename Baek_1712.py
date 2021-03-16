a,b,c=map(int,input().split())

def plus(a,b,c):
    n=1
    while True:
        n+=1
        pro=a+(b*n)
        sell=c*n
        if sell>pro:
            break
    return n

plus(a,b,c)
print(plus(a,b,c))