import random
playing = True
number = str(random.randint(10,20))

print(" i will genarate a number form 10 to 20, and you have to guess the number 1 digit at a time.")
print("The games ends when you get 1 hero!")

while playing:
    guess = input(" give me your best guess! \n")
    if number == guess:
        print("you win")
        break
    else:
        print("try again")
