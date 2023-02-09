import random as r
answer = r.randint(1,10)
while True :
    lamb = lambda x : print("you won") if x == answer else print("the answer is bigger")
    guess = lambda x : print("the answer is smaller") if x > answer else lamb(x)
    print(guess(int(input('input your answer:'))))