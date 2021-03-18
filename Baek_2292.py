n=int(input())

value=1

for i in range(n):
    value+=(6*i)
    if value>=n:
        print(i+1)
        break
