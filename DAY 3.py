#Numeric datatype --> int,flost,complex along with boolean

#input formatting -->Accepting input from the user --> input()

#accepting integer input fron user
#by default input() accept any input --> str

#int(input())--> will accept only integers
'''
age = int(input('Enter the age:'))
print (age)
print(type(age))

#float(input())--> accepts integers,float values

age = float(input('Enter the age:'))
print (age)
print(type(age))

#accepting string input from user

name = input("enter the name:")
print (name)
print(type(name))
#accept group of values
marks = int(input("enter the marks:")).split()

a = input("enter the values:").split(",") #comma separated value
print (a)

#a = input("enter the values:").split() #space separated value 
#print (a)

#List of integers

marks =list(map(int,input("enter the marks:").split(','))) #map is used to map more values
print(marks) 
print(type(marks))

marks =list(map(float,input("enter the marks:").split(','))) #map is used to map more values
print(marks) 
print(type(marks))

#Now we want to accept 2 values from user

age,salary = map(int,input("enter the values:").split(','))
print(age)
print(salary)


age,salary = map(float,input("enter the values:").split(','))
print(age)
print(salary)
'''

#single input-->int(input())
#two inputs -->a,b = map(int,input().split(","))
#any number result as list --> a = list(map(int,input().split(',')))
#Accepting input from user --> int,float --> input formatting

#Operators --> operators perform operstions between values(operands)
#7 types --> arithmetic,assignment,comparison (relationship), membership, identity, logical, Bitwise
#arthmetic operators
'''
print(5+3)
print(5-3)
print(5/3)
#flooor division
print(5//3) #returns quotient
#modulus 
print(5%3)  # returns remainder
#power (exponential)
print(5**3)

#Task --> accept integer input as  length, breadth -->find the area of reactangle
length,breadth = map(float,input("enter the values:").split(","))
area= length*breadth
print(area)

#Assignment operators --> assign the values
# = , += , -=
a = 45
print(a)
#update the value of a
a = a+3
print(a)
a += 5
print(a)
b = 15
b += a
print(b)
b -= 2
print(b)
'''
#Task : *=, /=, //=, %=, **=  workout

#comparision operators --> we compare the values --> boolean
# ==(equal to), !=(not equal to), <(less than), >(greater than)
# <=(less than or equal to), >=(greater than or equal to)
'''
a = 24
print(a == 21)
print(a != 23)
print (a <= 21)
print (a >= 21)
print (a < 21)
'''
# MEMBERSHIP operators --> in , not in --> boolean
# it checks exiastance of object in a collection
'''
marks = [23,45,67,89,90]
print(45 not in marks)
print(23 in  marks)
#print(35 in 355) #DOES NOT WORK.
print('code' in 'codegnan') #it works because of string and symbols also work
'''
#Logical operators --> logical decision making --> and,or,not
#and --> all condition are satisfied
#or --> ant one condition
'''
a = (25 in [23,25,45,67] and 47>18)
print(a)
b = 23<12 or 7<18
print(b)
c = not(True)
print(c)
'''
#identity operators --> check for identity of an object --> id()
# is, is not
'''
a=35
b=35
print(id(a))
print(id(b))
print(a is b )
c = a
print(id(c))
print(c is a)
'''

a = [1,2,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)
b = [1,3,4,2,5]
print(id(b))











