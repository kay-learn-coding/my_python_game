'''
total=0
for number in range(1,101):
    total+=number
print(total)

#fizz_buzz challenege
for number in range(1,101):
    #if number divides 3 and 5 witout a remainder print(fizz_buzz)
    if number%3==0 and number%5==0:
        print("fizz_buzz")
    #if number divides 3 without a remainder print(fizz)
    elif number%3==0:
        print("fizz")
        #if number divides 5 witout a remainder print(buzz)
    elif number%5==0:
        print("buzz")
    else:
        print(number)
'''
#password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#simple version
'''
password_char=""
password_sym=""
password_num=""
for char in range(nr_letters):
    random_char=random.choice(letters)
    password_char+=random_char
for sym in range(nr_symbols):
    random_sym=random.choice(symbols)
    password_sym+=random_sym
for num in range(nr_numbers):
    random_num=random.choice(numbers)
    password_num+=random_num
total_password=password_char+password_sym+password_num
password_random=random.shuffle(total_password)
print(f"Your password is {password_random}")
'''
#more advance version
'''
password_list=[]
for char in range(nr_letters):
#use (.append) to add it all together
    password_list.append(random.choice(letters))
for sym in range(nr_symbols):
    password_list.append(random.choice(symbols))
for num in range(nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
final_password="".join(password_list)
print(f"Your Password is {final_password}")
'''