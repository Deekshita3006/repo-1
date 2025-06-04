print("Welcome to tresure adventure\n")
print("Your misson is to find the treasure\n")


#choose the direction first
Way=input("you have entered into a dense forest,as you walk on you see different types creatures on your way.  as walk you on you find a crossroads with warning signs on it. on left direction it says no hurdles and the other one says full of snakes. so,which way would you like to go? left or right\n")
if Way=="left":
    print("SUCCESSFUL")
else:
    print("GAME OVER")

#swim or wait
choose=input("you have passed one biggest barrier. now you on a narrow road you've encountered a pond which leads to other side of the forest. bit the pond is full of crocodiles what will you do? are you gonna swim or wait?\n")
if choose=="wait":
    print("SUCCESSFUL")
else:
    print("GAME OVER")
#Direction
Door=input("succesfully you choose a correct decision. as you have travelled so far and you have reached to the end of the forest. there you are given to choose 3 of 1 safest door.which door do you wanna choose? red,blue,yellow\n")
if Door=="red":
     print("GAME OVER")
elif Door=="blue":
     print("GAME OVER")
elif Door=="yellow":
     print("SUCCESSFUL")
else:
    print("choose the right colour")


print("        ____________      ")
print("       |            |     ")
print("       |            |     ")
print("       |____________|     ")
print("      /____\|/_____  \    ")
print("     |                |   ")
print("     |                |   ")
print("     |________________|   ")