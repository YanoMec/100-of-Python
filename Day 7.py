#Day 7 - Creating Hang man Game. 

#Flow chart Programing. (use drawio)

word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')
display = ["_"] * len(chosen_word)
     
print(display)
user_guess = input("Guess a letter?\n").lower()

for index in range(len(chosen_word)):
    if user_guess == chosen_word[index]:
        display[index] = user_guess
print(display)

    

    
