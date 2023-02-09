import random as r
a = ''
text = input('write your text:').split(' ')
with open('C:/Users/NOTEBOOK/Desktop/40 projects/3/badwords.txt', encoding='utf-8') as file:
    for i in file: 
        last_txt = i.split(', ')
for i in text:
    a += i + " " + r.choice(last_txt) + " "
print(a)