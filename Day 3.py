# .count("#") - This method returns the number of times a specified value(#) appears in the string.
# e.g t = name.count("t") will check to see how many times "t" is in name.


# ------------------------------------------------------------------
#Day 3 project - Trease Island.

print('''
****************************  Treasure  Island  ********************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************      
     ''' )
print("Welcome to Treasure Island!\n Your mission, if you choose to accept, is to find the treasure of Black Beard!")
win = False
while win==False:
    cross_road =input('Your at a cross road do you go left or right?\nEnter left or right  ')
    road = cross_road.lower()


    if road == "right":
        print("You fell into a hole. !!GAME OVER!!")
    
    elif road == "left":
        print("You've arrived at the Islands port, You have two options.\nSwim or wait for a boat.")
       
        port = input("Are you going to swim or wait for the boat?\nEnter Swim or wait  ")
        option= port.lower()
       
        if option == "swim":
            print("You where eatting by a shark !!GAME OVER!!")
        if option =="wait":    
            print("You have arrived at a light house with 3 doors.\nRed, Yellow and Blue")

            door_selection = input("what door do you choose?\nEnter Red, Yellow or Blue  ")
            door=door_selection.lower()
       
            if door == "red":
                print("you were burned by fire. !!GAME OVER!!")

            if door =="blue":
                print("You were eaten by beasts. !!GAME OVER!!")
            if door == "yellow":
                print("You found the treasure!")
                win = True
    else:
        print("Please Enter left or right ")

     
   
   


    
