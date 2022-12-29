#1.FOR SYNTAX ERROR, the there is an error regarding the semicolon because of which output does not appear.
age=15
if(age>21)
print("I am an adult now")
else
print("I am still underage")

#2.
import sys
try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("Incorrect name of the file please enter correct name")

#3.
try:
    num_1 = int(input("Enter number: "))
    if (num_1 > 9999 or num_1 < 1000):
        raise ValueError
except ValueError:
    print("The length is too short/long !!! Please provide only four digits")

#4.
print('Enter the username and password:')
chance = 0
username = ""
password = ""
while username != 'training_department' and password !='Consultadd' and chance < 3:
    username = input("Enter username:")
    password = input("Enter password:")
    if password=='Consultadd123' and username=='training_department':
     print("Access granted")
     break
    else:
        print("Access denied, kindly Try again")
        chance=chance+1
#5.
#Finally and Raise Concept-learn...

#6.
with open('doc.txt') as x:
    lines = x.readlines()   
print(lines)
line1 = ""
for str in lines:
    if(len(str)%2==1):
        line1 = str
print(line1)