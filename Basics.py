# first="popa"
# last="sebastian"
# long_name= f"{first} {last}"
# print(long_name.title())



# number1=int(input("What is the first number?"))
# number2=int(input("What is the second number?"))
# sum=number1 + number2
# product=number1 * number2

# print(f"The sum of the numbers: {sum}")
# print(f"The product of the numbers: {product}")


    # How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4


# students=int(input("How many students on the course?"))
# group_size=int(input("Desired group size?"))

# groups_rest=float(students%group_size)
# groups_number= int(students//group_size)

# if groups_rest==0:
#     print(f"Number of groups formed: {groups_number}")
# else:
#     print(f"Number of groups formed: {groups_number+1}")

# number1=int(input("First number:"))
# number2=int(input("The second number is:"))
# operation=input("Your operation wanted? (add, multiply or subtract)")

# if operation == "add":
#     print(f"{number1} + {number2} = {number1+number2}")

# if operation == "multiply":
#     print(f"{number1} * {number2} = {number1*number2}")

# if operation == "subtract":
#     print(f"{number1} * {number2} = {number1-number2}")


# faren=int(input("Temperature in Fahrenheit:"))
# celsius=(faren - 32)*(5/9)

# print(f"{faren} degrees Fahrenheit equals {celsius} degrees Celsius")

# if celsius<0:
#     print("Brr! It's cold in here!")

# hour_wage=float(input("Hourly wage:"))
# hour_work=float(input("Hours worked:"))
# today=input("Day of the week:")

# daily_wage=hour_wage*hour_work

# if today == "Sunday":
#     print(f"Daily wages: {daily_wage*2} euros")
# else:
#     print(f"Daily wages: {daily_wage} euros")

# number=int(input("choose your number: "))

# if number % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

# correct="Calarasi1@"
# password=input("Please type in your password: ")

# if password == correct:
#     print("Welcome!")
# else:
#     print("Try again")

# number=int(input("Number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 5 == 0:
#     print("Buzz")
# elif number % 3 == 0:
#     print("Fizz")

##                                                  Leap year problem
# year = int(input("Please type in a year: "))
 
# # First, we make assumption that a year is not a leap year
# leap_year = False
 
# if year % 100 == 0:
#     if year % 400 == 0:
#         leap_year = True
# elif year % 4 == 0:
#     leap_year = True
 
# if leap_year:
#     print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")

# if first > second:
#     if second > third:
#         print("The letter in the middle is", letter2)
#     else:
#         print("The letter in the middle is", letter3)
# else:
#     print("The letter in the middle is", letter1)

# gift=int(input("Value of gift: "))

# if gift < 5000:
#     print("No tax!")
# elif gift >= 5000 and gift <= 25000:
#     tax = 100 + (gift - 5000) * 0.08
#     print ("Amount of tax:", tax, "euros")
# elif gift >= 25_000 and gift <= 55_000:
#     tax = 1_700 + (gift - 25_000) * 0.1
#     print ("Amount of tax:", tax, "euros")
# elif gift >= 55_000 and gift <= 200_000:
#     tax = 4700 + (gift - 55_000) * 0.12
#     print ("Amount of tax:", tax, "euros")
# elif gift >= 200_000 and gift <= 1_000_000:
#     tax = 22_100 + (gift - 200_000) * 0.15
#     print ("Amount of tax:", tax, "euros")
# else:
#     tax = 142_100 + (gift - 1_000_000) * 0.17
#     print ("Amount of tax:", tax, "euros")


# while True:
#     number = int(input("Please type in a number, -1 to quit: "))

#     if number == -1:
#         break
#     print(number ** 2)

# print("Thanks and goodbye!")

# while True:
#     print("Hi")
#     answer = input("Shall we continue?")

#     if answer == "no":
#         break
# print("okay then")

# from math import sqrt

# while True:
#     number = int(input("Please type in a number: "))

#     if number < 0:
#         print("Invalid number")
#     elif number == 0:
#         break
#     else:
#         print(sqrt(number))

# password = input("Please type in the password: ")

# while True:
#     password2 = input("Please repeat the password: ")

#     if password == password2:
#         break
#     else:
#         print("They do not match!")
# print("User account created!")


attempts = 0
passpin = 4321

while True:
    pin = int(input("PIN: "))
    attempts += 1

    if pin == passpin:
        break        
    else:
        print("Wrong")
    
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print("Correct! It took you", attempts, "attempts")

