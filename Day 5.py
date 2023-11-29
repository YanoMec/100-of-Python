#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

print("Welcome to the PyPassword Generator!")
wanted_letters= int(input("How many letters would you like in your password?\n")) 
wanted_numbers = int(input(f"How many numbers would you like?\n"))
wanted_symbols = int(input(f"How many symbols would you like?\n"))

# for index_letters in range(wanted_letters):
#     x = random.randint(0, len(letters))   
#     password += letters[x]

    
# for index_numbers in range(wanted_numbers):
#     x = random.randint(0, len(numbers))   
#     password += numbers[x]

# for index_symbols in range(wanted_symbols):
#     x = random.randint(0, len(symbols))   
#     password += symbols[x]
# print(password)

while(wanted_letters or wanted_numbers or wanted_symbols > 0):
    char_type = random.randint(0,2)
    if char_type == 0 and wanted_letters > 0: 
        x = random.randint(0, len(letters) - 1)   
        password += letters[x]
        wanted_letters -= 1

    elif char_type == 1 and wanted_numbers > 0: 
        x = random.randint(0, len(numbers) - 1)   
        password += numbers[x]
        wanted_numbers -= 1

    elif char_type == 2 and wanted_symbols > 0: 
        x = random.randint(0, len(symbols) - 1)   
        password += symbols[x]
        wanted_symbols -= 1
print(password)
