#단어장

# word=input()
# word=word.upper()

# max=0

# for i in range(len(word)):
#     count=0
#     for j in range(i,len(word)):
#         if word[i:i+1]==word[j:j+1]:
#             count+=1
#     if count>max:
#         max=count
#         maxal=word[i]
#     elif maxal!=word[i] and count==max:
#         maxal='?'

# print(maxal)

# 위에꺼 시간초과 됨

from string import ascii_uppercase

word=input()
word=word.upper()

al=list(ascii_uppercase)
count=[0]*26
max=0

for i in range(len(word)):
    for j in range(26):
        if word[i:i+1]==al[j]:
            count[j]+=1
            if count[j]>max:
                max=count[j]
                maxal=al[j]
            elif al[j]!=maxal and count[j]==max:
                maxal='?'
            break

print(maxal)
