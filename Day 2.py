# Data Types

#---String--- 
#Text

# print("Hello"[1]) #"[]" lets you choose the position(index) of the string.

#---Integer---
#Whole Number

# print(3_000+30_000)
# while using large numbers, you can use "_" to represent ","
#example: 7,000,000 = 7_000_000 and Python will still see it as 7000000

#---Float---
# Decimal Numbers
# print(3.14159)

#---Boolean---
#True/False

# True
# False 

#---Maths---
# 6/3 # "/" will always return a float
# num**2 #power of 2 (exponent)
# round(8/3) #round number
# round(10/3, 2) #using "," then num can round number to selected decimal places.

#---f string---
# f"your score is {---}" #f-string lets you put all types together

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#Day 2 project. Tip calculator.

print("Welcome to the Tip calculator!")

bill = input("How much is your bill?\n")

tip_percent = input("What tip percentage would you like to give?\n")

tip_total = ((float(tip_percent)/100) * float(bill))

bill_total = float(tip_total) + float(bill)

people = input("How many people are splitting the bill?\n")

total_per_person = round(float(bill_total) / float(people),2)

print(f"Each person should pay £{total_per_person}")