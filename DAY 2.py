'''
Tokens --. variables, punctuators

variable --> named memory location,its a placeholder for a data


#Multiassignments of variables

name,age,place="raj",21,"hyd"
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='----->')

#a,b=2,3,4  valueerror as too many values to unpack

#reassinging variAables

name="codegnan"
a,b=45,1.5
print(a,b,sep=",")

a,b=b,a #swapping
print(a,b,sep=",")

#a,b=b,c # Name error
#print(a,b)

#deleting the variable -->del
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators --> []Lists ,()tuples ,{}Dict,sets

name="raj";age=21;course="Data analytics"
print(name,age,course,sep=",")


#Datatypes --> Numeric (int,float,complex),boolean,none
#sequences --> lists,tuples,sets,strings,fozensets,mapping(dict)

#numeric --> int,float,complex

#int datatyp--> quantity,age..
age=21
print(age)
print(type(age))  #type--> returns the datatype of object
#quantity=03 #it is not allowed
#print (quantity)

#float datatype--> temp,salary,price,weight
price=780.18;discount=3.5
print(price,discount)
print(type(price))

#complex -->combinaton of real and imaginary
i2 = 4
data= 5 + i2
print(data)

data = 5+2j #j is imaginary representation
print (data)
print(type(data))


#Boolean --> True/False

valid = True
print(type(valid))

error = False
print(type(error))
'''
#Typecasting --> Comverting one type to another type

#PYTHON by default follow implicit type (we need not mention the datatype)

#we will go for explicit conversion

#every built-in datatype is a built-in function
#int,float,complex,bool

#typecasting float--> int,complex,bool
'''
weight=73.5
print(type(weight))
b=complex(weight)
print(b)
c=bool(weight)
print(c)
d=int(weight)
print(d)

#complex
hr=7+9j
print(type(hr))
#b=int(hr)
#print(b)
c=bool(hr)
print(c)
print(type(c))
'''

e = int(float(bool(45)))  #first converted into bool  bool(45) is true --> convert into float(true) is 1.0 -->  

print(e)

f = 47 + 7+ 1.8 + 4j + True
print(f)









