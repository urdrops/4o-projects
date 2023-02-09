import string as s
import random as r
import time as t
with open('C:/Users/NOTEBOOK/Desktop/4o-projects/40 projects/5/guess_words.txt', encoding='utf-8') as file:
    for i in file:
        array_of_words = i.split(', ')
    random_words = r.choice(array_of_words)
hiden = ("_ " * len(random_words)).split()
print("Добро пожаловать в Поле чудес! \n  тебе надо будет угадать слово методом перебора! \n начинаем!")
t.sleep(0.5)

while ''.join(random_words) != ''.join(hiden) : 
    answer = input(f' *_* попробуй угадать загадонное слово! \n подсказка кол букв: {len(random_words)} \n спойлер: {random_words} \n угаданные буквы: {hiden} \n  твой ответ: ')
    print(f' \n {"_"* 90} \n ')
    t.sleep(0.5)
    b = 0
    c = 0
    for i in random_words:
            b += 1
            if i == answer:
                c += 1
                hiden[b - 1] = answer
    if c > 0:
        print(f"верный ответ! \n Ты угадал {c} букв в загаданном слове {hiden} \n продолжай! \n {'_'* 90} \n ")
    else: 
        print('увы не угадал( \n попробуй снова!')
        print(f' \n {"_"* 90} \n ')
        t.sleep(0.5)
print(f"ты угадал целое слово! Это было слово {''.join(hiden)}")
print("БАХТИ ТЫ ГЕННИЙ ТЫ ВЫИГРАЛ!")

            
        

