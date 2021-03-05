# codeup 6081_16진수 구구단
a=input()
a=int(a,16)

for i in range(1,16):
    b=int(a*i)
    print("%X*%X=%X"%(a,i,b))
