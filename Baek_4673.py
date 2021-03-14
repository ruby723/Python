def sum(num):
    a=int(num/1000)
    b=int(num/100)%10
    c=int(num/10)%10
    d=num%10
    new_num=num+a+b+c+d
    return new_num

s=set(i for i in range(1,10001))
not_self=set()

for i in range(1,10001):
    sum(i)
    not_self.add(sum(i))

self=list(s-not_self)
self.sort()
for i in range(len(self)):
    print(self[i])