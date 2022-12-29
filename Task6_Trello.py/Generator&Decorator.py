#1.
l = "abcdefgABCDEFGHIJKLMNOP"
new_str=''.join([c for c in l if c.isupper()])
print(new_str)

#2.
students = ["Smit","Jaya","Rayan"]
subjects = ["CSE","Networking","Operating System"]
print("The list of key is: " + str(students))
print("The list of value is: " + str(subjects))
output = dict(zip(students, subjects))
print("The new dictionary is: " + str(output))

#3.Learn't about Yield,next and Generators.
#A generator is a function that returns a value through the keyword yield instead of return. To get the next value of a generator, we use the same function as for an iterator: next().
#Every time we call next() on a generator, the generator must transfer a value and the control through yield. 

#4.
def string_reverse(str):
    length = len(str)
    for x in range(length-1, -1, -1):
        yield str[x]
for ch in string_reverse("Consultadd Training"):
    print(ch,end='')

#5.
#In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
