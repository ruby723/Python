n=int(input())
score=input().split()

max=0
sum=0

for i in range(n):
    score[i]=int(score[i])
    if score[i]>max:
        max=score[i]

for i in range(n):
    score[i]=score[i]/max*100
    sum+=score[i]

avg=sum/n
print(avg)