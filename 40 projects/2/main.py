import random as r
str = "Choise your option(rock,paper,scissor): \n"
user = input(str)
rock, scissor, paper = range(3)
winner = [{'scissor'},{'paper'},{'rock'}]
var = [rock,scissor,paper]
varstr = ['rock','scissor','paper']
turn = False
while turn == False:
    computer = r.choice(var)
    if user in winner[computer]: #надо попробовать использовать лямбду
        print("lose cause computer chose " + varstr[computer])
        user = input(str)
    elif user == varstr[computer]:
        print("draw cause computer chose " + varstr[computer])
        user = input(str)
    else: 
        print("win cause computer chose " + varstr[computer])
        turn = True
print("URDROPS IS THE BEST!") 
print("...")
