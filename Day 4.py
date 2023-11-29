# Python docs https://www.askpython.com/
# import random 
# x = random.randint(range1, range2)
# e.g random_integer.rantint(1,10) --random number between 1 to 10

# random_float = random.random() -- random float between 0.00 to 1.00
# random_float * 5  -- expand range to 0.00 to 5.0000  

# You can create list using "[]" -- e.g x = [item1,item2,item3,item4]
# To print the 3rd item on you list you use an index list[index] -- e.g. "x[2]" --remember programs begin from 0
# Able to change item in list by ListName[IndexNumber] ="NewItemName" -- e.g. Dogs[1] = "Chow Chow"
# Able to add single item to list using ".append("pitbull")" -- e.g. Dogs.append("pitbull")
# **Many more methods for lists on https://docs.python.org/3/tutorial/datastructures.html **
# when getting the amount in a list using len(list) we must add -1 as python list start at 0 
# e.g list_amount = len(list)-1
# nested lists can be written as newlist = [list1, list2]

# ------------------------

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # B3 # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇
# letter = position[0].lower() # b

# abc = ["a", "b", "c"]
# # index of b in abc = 1
# letter_index = abc.index(letter) # letter_index = 1
# # position[1] = 3
# number_index = int(position[1]) - 1 # number_index = 2

# map[number_index][letter_index] = "X" # map[1][2] = 1


# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

# -------------------
import random
Rock = '''
     Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Papar & scissors")
user_pick =input("what do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors\n")
cpu = random.randint(0, 2)
game = [Rock, Paper, Scissors]

player_chosen = game[int(user_pick)]
cpu_chosen = game[cpu]

choice = [player_chosen, cpu_chosen]

win_condition = [[Rock, Scissors], [Paper, Rock], [Scissors, Paper]]


if choice[0] == choice[1]:
    print(f'Draw! Try again\n{player_chosen}\n{cpu_chosen}')
else:
    if choice in win_condition:
        print(f'You won!\n{player_chosen}\n{cpu_chosen}')
    else:
        print(f'You lost! Try Again\n{player_chosen}\n{cpu_chosen}')
        