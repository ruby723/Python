# codeup 6083_ r,g,b 색깔값 계산하기
r,g,b=input().split()
r=int(r)
g=int(g)
b=int(b)
if r>=0 and r<=127 and g>=0 and g<=127 and b>=0 and b<=127:
    for i in range(r):
        for j in range(g):
            for k in range(b):
                print(i,j,k,end="\n")
    print(r*g*b)