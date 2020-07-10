import random
# Write a function is_even that will return true if the passed-in number is even.
def mult2(x):
    return x * 2
print(mult2)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def iseven(num):
    if num % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)
#print(iseven(num))

# doubling function that passes arg by reference
l = [1, 2, 3, 4]
print(l)

def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
    return l
y = mult2_list(l)
print(y)

# or
# def mult2_list(x):
#     for i in l:
#         i *= 2

# rock paper scissors
wins = 0
losses = 0
ties = 0

# possible_choices = ["rock" : 1, "paper": 2, "scissors": 3]
choices = ["rock", "paper", "scissors"]
user_choice = input("Choose rock, paper, or scissors")
computer_choice = random.randint(0,2)
print(computer_choice)

if user_choice == "rock":
    if computer_choice == "rock":
        print("it's a tie")
        ties += 1
    elif computer_choice == "paper":
        print("you lose!")
        losses += 1
    else:
        print("You won!")
        wins += 1

