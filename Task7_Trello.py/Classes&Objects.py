#Q1.
import math
class SquareRoot:
    c = 50
    h = 30
    def __init__(self,D) -> None:
        self.d = D
    def square_root(self):
        value = []
        for m in self.d:
            Q = round(math.sqrt(2*50*int(m)/30))
            value.append(Q)       
        return value
if __name__ == "__main__":
    numbers = input("Provide D: ")
    d = SquareRoot(numbers.split(','))
    Q = d.square_root()
    print(Q)

#Q2.
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length
    def area(self):
        return self.length*self.length
sqr = Square(7)
print(sqr.area())

#3.
class Result:
    def findThreeElements(arr, n): 
        found = False
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (arr[i] + arr[j] + arr[k] == 0):
                        l1=[arr[i], arr[j], arr[k]]
                        print(l1)
                        found = True
        if (found == False):
            print("does not exist ")

arr = [-25,-10,-7,-3,2,4,8,10]
n = len(arr)
print(Result.findThreeElements(arr, n))

#4.
class Time():
    def __init__(self, hrs, mins):
        self.hrs=hrs
        self.mins=mins
    def addTime(t1, t2):
        t3=Time(0,0)
        if t1.mins+t2.mins > 60:
            t3.hrs=int((t1.mins + t2.mins)/60)
        t3.hrs=t3.hrs+t1.hrs+t2.hrs
        t3.mins=(t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
        return t3
    def displayTime(self):
        print("The calculated Time is",self.hrs,"hours and",self.mins,"minutes.")
    def displayMinute(self):
        print((self.hrs*60)+self.mins)

a=Time(2,70)
b=Time(1,20)
c=Time.addTime(a,b)
c.displayTime()
c.displayMinute()

#5.
class Person:
    # age = 0
    def __init__(self,initialAge):
        if (initialAge < 0):
            print("Age is not valid, setting age to 0")
            self.age=0
        else:
            self.age = initialAge
    def amIOld(self):
        if (self.age < 13):
            print("You are young")
        elif (self.age >= 13 and self.age < 19):
            print("You are a teenager")
        else:
            print("You are old")
    def yearPasses(self):
        self.age += 1
t=int(input())
for i in range(0,t):
    age=int(input())
    p=Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses()
    p.amIOld()
    print("")
