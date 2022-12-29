#1. Create three variables in a single line and assign values to them in such a manner that each one of
#   them belongs to a different data type.
x=1
y="jainika"
z=2.0
print(type(x))
print(type(y))
print(type(z))

#2. Create a variable of type complex and swap it with another variable of type integer.
a=2+3j
print(type(a))
b=5
print(type(b))
a,b=b,a
print("The new swapped variables are as: ")
print(type(a))
print(type(b))

#3. Swap two numbers using a third variable and do the same task without using any third variable.
# Without third variable
m=2
print(type(m))
n=5
print(type(n))
m,n=n,m
print("The new swapped variables are as: ")
print(m)
print(n)

# With third variable
y=2
z=5
temp=y
y=z
z=temp
print("The new swapped variables with third variable are as: ")
print(temp)
print(y)
print(z)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

# x=int(input("Enter number from user: "))
# print(x)

# def main():
#   print "Hi! This is Python 2" 
# if __name__== "__main__":
#   main()

def main():
  print ("Hi! This is Python 3")  
if __name__== "__main__":
  main()

#5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

num1=int(input("Enter number1 btwn 1-10: "))
num2=int(input("Enter number2 btwn 1-10: "))
z=num1+num2
res=z+30
print(res)

#6. Write a program to check the data type of the entered values.
a,b,c = 20, 2.2, "is or is not a string"
print("The data type of the input value a is:", type(a))
print("The data type of the input value b is:", type(b))
print("The data type of the input value c is:", type(c))

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
# a=input("Enter the variable to convert in Uppercase: ")
# print("The converted string in Uppercase is: ",a.upper())
# b=input("Enter the variable to convert in Snakecase: ")
# print("The converted string in Snakecase is: ",b.lower())

c="exam result"
#FOR UPPERCAMELCASE-
c="examResult"
#FOR LOWERCAMELCASE-
c="ExamResult"
#FOR SNAKECASE
c="exam_result"
#FOR UPPERCASE
c="EXAM RESULT"

# FOR SNAKECASE
space = "exam result"
x = space.replace(" ", "_")
print(x)

#8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
a=["practice","codes",2]
print(type(a))
a=("practice","codes")
print(type(a))
#Yes, it changes the value because the variable changes or overwrites the values


