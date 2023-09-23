

# import random

# def guess(x):
#     random_number=random.randint(1, x)
#     guess=0
#     while guess !=random_number:
#         guess=int(input(f"Guess a number Between 1 and {x}: "))
#         print(guess)

# guess(10)



# import random

# def guess(x):
#     random_number=random.randint(1, x)
#     guess=0
#     while random_number!=guess:
#         guess=int(input(f"Guess a Number Between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry!! Guess Again Too low")
#         elif guess > random_number:
#             print("Sorry!! Guess Again Too High")

#     print(f"Yay! Yoy select the number {random_number} correctly!!")

# guess(10)



import random
from tokenize import maybe

def guess(x):
    random_number=random.randint(1, x)
    maybe=0
    while maybe != random_number:
        maybe=int(input(f"Guess a number 1 and {x}: "))
        if maybe < random_number:
            print("Sorry Guess again, Too low")
        elif maybe > random_number:
            print("Sorry Guess Again Too High")
    
    print(f"Yay You Selected the number {random_number}!!!")

guess(20)


