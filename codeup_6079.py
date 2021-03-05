sum=0
max=int(input())
for i in range(1,1000):
    if sum>=max:
        print(i-1)
        break
    sum+=i