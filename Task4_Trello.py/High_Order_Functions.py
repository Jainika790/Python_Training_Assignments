#1.
def reverse_a_string(s):
    reversed_string=[]
    for i in range(len(s)-1,-1,-1):
        reversed_string.append(s[i])
    return "".join(reversed_string)
print(reverse_a_string('1234abcd'))

#1(Other:Using Slicing)
str=input("Enter the string from user:")
print("The input string is:",str)
new_str=str[::-1]
print(new_str)

#2.
str_ch=input("Enter string to check no of upper and lowercases:")
uppercase=0
lowercase=0
for case in str:
    if case.isupper():
        uppercase+=1
    elif case.islower():
        lowercase+=1
    else:
        pass
print("Input String:",str_ch)
print("Nums of uppercase characters is:",uppercase)
print("Nums of lowercase characters is:",lowercase)

#3.
list=[1,2,4,5,2,8,4]
def unique(l):
    l=[]
    for x in list:
        if x not in l:
            l.append(x)
    return l
print("The input list is:",list)
l2=unique(list)
print("The unique elements in new list is:",l2)

#4.
items = [x for x in input().split('-')]
items.sort()
print('-'.join(items))

#5.
lines=input("Enter the lines to be capitalized:")
new_line=lines.upper()
print("The capitalized way of representing the sentence is:\n",new_line)

#6.
def sum(first,second):
    return int(first)+int(second)
first_num=input("Enter first number from user:")
second_num=input("Enter second number from user:")

print("The sum of integral no's in strings are:",sum(first_num,second_num))

#7.
def str(str1,str2):
    if (len(str_1)>len(str_2)):
        print("str_1 is maximum")
    elif (len(str_1)==len(str_2)):
        print(str_1,"\n",str_2)
    else:
        print("str_2 is maximum")
    
str_1=input("Enter first string from user:")
str_2=input("Enter second string from user:")
str(str_1,str_2)

#8.
t=[]
for i in range(1,21):
   t.append(i**2)
print(tuple(t))

#9.
def show_nums(limit):
   for i in range(limit+1):
     if i%2==0:
        print(i,"Even Number\n",end="")
     else:
        print(i,"Odd Number\n",end="")
print(show_nums(5))

#10.
new_list=list(filter(lambda x : (x%2==0) ,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print("The new list of even nos. are as:",new_list)

#11.
list1=map(lambda x : x**2 ,filter(lambda x : (x%2==0) ,[1,2,3,4,5,6,7,8,9,10]))
print("The new list of squared even nos. are as:",list(list1))

#12.
def compute():
    return 5/0
try:
    compute()
except ZeroDivisionError as zde:
    print("No. is divided by zero")
except:
    print("There is other exception that is occured.")

#13.
from functools import reduce
new_list=reduce(lambda x,y:10*x+y ,list(range(1,9)),0)
print(new_list)

#14.
l1=list(range(1,100))
list2=list(filter(lambda x : (x%3!=0 and x%7==0) ,l1))
print("The new list of nos. not divisible by 3 are as:",list2)

#15.
el_in_list=[1,2,3,4,5,6]
trad_func=map(lambda x:x*x, el_in_list)
print(list(trad_func))

#16.a)
def foo():
        try:
            return 1
        finally:
            return 2
k = foo()
print(k)
#Gives an output 2 as finally block executes

#16.b)
def a():
     try:
          f(x, 4)
     finally:
          print('after f')
          print('after f?')
     a()
#Raise an error