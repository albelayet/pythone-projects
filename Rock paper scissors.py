

# import random
# #p>r r>s s>p
# def play():
#     user = input("Please Choice (R) for Rock (P) for paper and (S) for Scissors ")
#     computer = random.choice(['r', 's', 'p'])

#     if user == computer:
#         return "It's Tie!!"

#     if is_win(user, computer):
#         return "You Won"    

#     return "You Lost"


# def is_win(player, opponent):
#     if (player == 'p' and opponent == 'r') or (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p'):
#         return True

# print(play())


import random


def game():
    user = input("What's Your choice (R) for Rock (P) for Papers (S) for scissor: ")
    computer = random.choice(['r', 'p','s'])

    if user == computer:
        return "It's Tie...!!"

    if win(user, computer):
        return "You WOOOOOOON!!"
    
    return " You  LOOOOST"




def win(player1, player2):
    if (player1 == 'p' and player2 == 'r') or (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p'):
        return True

print(game())
