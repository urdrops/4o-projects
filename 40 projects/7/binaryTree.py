import random as r
import string as s
data = []
#collect data
for i in range(10000):
    data.append(i + 1)
high_answer, low_answer, correct, low, high, = "больше","меньше","да",0,len(data)
start = input('загадайте любое число от 1 до 10000 и я попробую угадать O(log) время \n Загадали ? да/нет ')
while low <= high:
    middle = (low+high) // 2
    if start == correct :
        answer = input(f'Ответ {middle}? или больше/меньше? \n')
    else:
        print('окей, нет так нет') 
        break
    if  answer.lower() == correct or answer.lower() == 'yes':
        print('я просто гений ;)')
    if answer.lower() == high_answer :
        low = middle + 1
    elif answer.lower() == low_answer:
        high = middle - 1
