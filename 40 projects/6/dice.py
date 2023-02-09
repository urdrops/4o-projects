import random as r
while True:
    user = input('бросить кость go/cancel: ')
    if user == "go":
        side = r.randint(1,6)
        print(f' _____\n\n|  {side}  |\n _____ ')
    elif user == "cancel":
        break
    else: 
        print("я не понял запрос. Попробуй снова")
print('игра окончена!')