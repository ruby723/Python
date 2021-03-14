def han(n):
    a=int(n/100)
    b=int(n/10)%10
    c=n%10
    if n<100:
        return True
    else:
        if (a-b)==(b-c):
            return True
        else:
            return False

count=0

n=int(input())

for i in range(1,n+1):
    if han(i)==True:
        count+=1

print(count)
