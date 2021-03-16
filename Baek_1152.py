word=input()

count=0

for i in range(len(word)):
    if word[i:i+1]==' ':
        count+=1

if word[0:1]==' ':
    count-=1
if word[len(word)-1:]==' ':
    count-=1

print(count+1)