import random

#1.
def task1():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("Consultadd - Python Training")
    elif num % 3 == 0:
        print("Consultadd")
    elif num % 5 == 0:
        print("Python Training")
    else:
        print("Number is not divisible by 3 or 5")

#2.
def task2():
    operation = int(input("Enter 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication, 5 for Average: "))
    if operation == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif operation == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif operation == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif operation == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    elif operation == 5:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = (num1 + num2) / 2
        if result < 0:
            print("NEGATIVE")
        else:
            print(result)
    else:
        print("Invalid")

#4.
def task4():
    while True:
        num = int(input("Enter a number: "))
        if num < 0:
            print("It's Over")
            break
        else:
            print("Good Going")
            continue

#5.
def task5():
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5 != 0:
            print(num, end=",")

## --------Task 6 the output for -----------
##6.a)
# x=123
# i = 0
# count = 0
# for i in x:
# print(i)
# output :- 'int' object is not iterable

##6.b)
# i = 0
# while i < 5:
#  print(i)
#  i += 1
#  if i == 3:
#    break
#  else:
#   print("error")
#
#   Output:-
#   0
#   error
#   1
#   error
#   2

##6.c)
# count = 0
# while True:
#  print(count)
#  count += 1
#  if count >= 5:
#   break
#   output:-
#   0
#   1
#   2
#   3
#   4

#7.
def task6():
    for i in range(0, 7):
        if i == 3 or i == 6:
            continue
        else:
            print(i, end=" ")

#8.
def task7():
    string = input("Enter a string: ")
    letters = 0
    digits = 0
    for i in string:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digits += 1
    print("Letters", letters)
    print("Digits", digits)


#9.
def task8():
    lucky_number = 7
    while True:
        number = int(input("Guess the lucky number: "))
        if number == lucky_number:
            print("Congrats! You guessed it right.")
            break
        else:
            answer = input("Do you want to guess again? (yes/no): ")
            if answer == "no":
                print("It's Over")
                break
            else:
                continue


def task9():
    number =int(input("Guess the lucky number: "))
    lucky_number =random.randint(1, 10)
    while True:
        if number == lucky_number:
            print("Good guess!")
            break
        else:
            print("Try again!")
            continue
#10.
def taskk9():
    answer =random.randint(1, 10)
    print(answer)
    number = int(input("Guess the lucky number: "))
    while True:
        if number == answer:
            print("Good guess!")
            break
        else:
            print("Try again!")
        flag = str(input("Want to continue"))
        if flag == "no":
            print("Game over!")
            break
        else:
            continue


def task10():
    number = int(input("Guess the lucky number: "))
    lucky_number = random.randint(1, 10)
    counter=0
    while counter<5:
        counter+=1
        if number == lucky_number:
            print("Good guess!")

        else:
            print("Try again!")
            continue
    print("Game over!")

#11.
def task11():
    number = int(input("Guess the lucky number: "))
    lucky_number = random.randint(1, 10)
    counter=0
    while counter<5:
        counter+=1
        if number == lucky_number:
            print("Good guess!")
            break
        else:
            print("Try again!")
            continue
    print("Sorry but that was not very successful")
