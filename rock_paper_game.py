import random

user_wins = 0
computer_win = 0
option =  ["rock","paper","scissors"]
while True :
    user_input = input("Type Rock/Paper/Scissors or Q for Quit : ").lower()
    if user_input =="q":
        break
    if user_input not in option:
        continue
    random_number =random.randint(0,2)
    #rock :0, paper :1,scissors : 2
    computer_pick = option[random_number]
    print("computer pick",computer_pick)
    if user_input== "rock" and computer_pick=="scissor":
        print("you won! ")
        user_wins+=1
    elif user_input== "scissor" and computer_pick=="paper":
        print("you won! ")
        user_wins+=1
    elif user_input== "paper" and computer_pick=="rock":
        print("you win ! ")
        user_wins+=1
    else:
        print("you lost ! ")
        computer_win +=1
print("Goodbye!")
