# project-5 CREATE A PASSWORD
import random
letters=['a','b','c','d']
symbols=['!','@','#']
number=['1','2','3','4']
print("Welcome to password generator!\n")
user_letters=int(input("how many letters would you like to add in your password?\n"))
user_symbols=int(input(f"how many symbols would you like to add?{symbols}\n"))
user_numbers=int(input(f"how many numbers would you like?{number}\n"))
password=" "
for char in range(1,user_letters+1):
    random_char=random.choice(letters)
    password+=random.choice(letters)

for char in range(1,user_symbols+1):
    random_char=random.choice(symbols)
    password+=random.choice(symbols)
   
for char in range(1,user_numbers+1):
    random_char=random.choice(number)
    password+=random.choice(number)
   
print(password)