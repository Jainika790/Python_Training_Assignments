#1.
l1=[20,"str1", 10+5j, 10,"str2", 12, 20+2j, 2.2, 99, 8.6]
#print(type(l1))
#To check if it is a list

#2.
l2=[10,20,30,40,50]
print(l2[::])
print(l2[:])
print(l2[::1])
print(l2[::-1])
print(l2[1:4:])
print(l2[-1:-3:-1])

#3.
sum=0
product=1

for x in range(len(l2)):
    sum=sum+l2[x]
    product=product*l2[x]
print("The Sum is:",sum)
print("The Product is:",product)

#4.
l3=[1,5,9,23,64]
largest=max(l3)
smallest=min(l3)

print("The largest element in l3 is:",largest)
print("The smallest element in l3 is:",smallest)

#5.
l4=[1,2,3,4,5,6,7,8]
new_list=filter(lambda x : x%2!=0 ,l4)
print("The new list of odd nos. are as:",list(new_list))

#6.
l5=list()
for i in range(1,31):
    if (i<=5 or i>=25):
        l5.append(i**2)    
print(l5)

#7.
list7=[1,3,5,7,8]
list8=[2,4,6,9]
list7=list7[:4]+list8
print("The new list is:",list7)

#8.
dict_a={1:10,2:20}
dict_b={3:30,4:40}
dict_a.update(dict_b)
print("The new dictionary is:",dict_a)

#9.
dict_1=dict()
n=int(input("Enter input from user:"))
for x in range(1,n+1):
    dict_1[x]=x*x
print(dict_1)

#10.
nums=input("Enter comma separated numbers from user:")
list=nums.split(",")
print(list)
tuple=tuple(list)
print(tuple)


