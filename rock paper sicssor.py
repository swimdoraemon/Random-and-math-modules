import random

options = ["Rock", "Paper", "Scissor"]

user_choice = input("choose rock paper or scissor: ")

computer_choice = random.choice(options)

print("You chose:", user_choice)
print("computer chose:", computer_choice)

if user_choice == computer_choice:
    print("its a tie!")

elif user_choice == "Rock" and computer_choice == "Sissors":
    print("You win!!!")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!!!")

elif user_choice == "Sissors" and computer_choice == "Paper":
    print("You win!!!")

else:
    print("You LOSE! ")
