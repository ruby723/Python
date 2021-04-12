import math
inf=math.inf
W=[[0,7,inf,11,inf,inf],
    [3,0,inf,inf,17,inf],
    [inf,6,0,inf,inf,inf],
    [inf,inf,inf,0,9,inf],
    [inf,5,15,16,0,2],
    [inf,inf,11,inf,8,0]]

def floydD(n):
    D=[[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            D[i][j]=W[i][j]
    P=[[0]*(n) for i in range(n)]

    for k in range (n):
        print('D({0})'.format(k+1))
        for i in range (n):
            for j in range (n):
                if D[i][k]+D[k][j]<D[i][j]:
                    P[i][j]=k+1
                    D[i][j]=D[i][k]+D[k][j]

                print(D[i][j],end='\t')
            print('')
        print('')

    print('P')
    for i in range(n):
        for j in range(n):
            print(P[i][j],end='\t')
        print('')
                
floydD(6)
