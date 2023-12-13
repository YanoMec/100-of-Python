#Day 7 - Creating Hang man Game. 

#Flow chart Programing. (use drawio)

word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')
display = ["_"] * len(chosen_word)
     
print(display)
user_guess = input("Guess a letter?\n").lower()

for letter in chosen_word:
    if user_guess in chosen_word:
        print("Right")
    else:
        print("Wrong")
