#Project -4 Rock paper sisscors
import random
user =int(input("what would you like to choose? 0 for rock, 1 for paper, 2 for scissors\n"))
computer=random.randint(0,2)
print(f"computer choose {computer} ")

if user>=3 or user<0:
    print("you have typed invalid number.you lose!")
elif user==0 and computer==2:
    print("You win!")
elif computer==0 and user==2:
    print("you lose!")
elif user==computer:
    print("its draw!")