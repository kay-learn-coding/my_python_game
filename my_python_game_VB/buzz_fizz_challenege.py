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