# Snake water gun game

import random
#  Snake = 1
#  water = -1
#  gun = 0


computer = random.choice([-1,0,1])
youstr = input("Enter Your Choice: ")
youDict = {"s":1 , "w": -1 , "g": 0}
reverseDict = {1: "Snake" , -1: "Water" , 0: "Gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\n Computer Chose {reverseDict[computer]} ")

if(computer == you ):
    print("It's a draw")

else:    

    if(computer == -1 and you == 1):
        print("You Win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 1 and you == -1):
        print("You Lose!") 

    elif(computer == 0 and you == 1):
        print("You Lose!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    else:
        print("Something went wrong!")                      