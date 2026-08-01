#identity operators using list

a= [1,2,3,4,5]
b= a
print(id(a))
print(id(b))
c = [1,2,3,4,5]
print(id(c))
# As we have lists(Mutable collection) both c and a lists will have different
#ids wherears values are same
print(c is a) #output false because list have different reference ids no matter values are same
print(c == a)# output true because we use comparision operators
print(a is not c)

#Bitwise operators --> We performs bitwise operations over operands
# &(AND) , |(OR) , ^(xOR) , Shifting operators(<<,>>)
#number will be converted to binary format

print(5&3) #both 5 and 3 to be converted boinary and bitwise and is performed
print(5|3) #bitwise OR
print(5^3) #bitwise XOR
print(5 and 3) #here and is logicL OPerator checks for both existances
# returns 5 in above case

print(5 or 3) #returns 3 in this case

# left shift operator << , right shift operator >>

#left shift
print (5 << 1) #returns 10 shifts in binary format so output is 10

#right shift
print (5 >> 1) #returns 2

print (15 << 2 ) # convert 15 to binary and perform 2 times left shifting

print (15 >> 2 ) # same 2 times right shifting

#input formatting --> input(), int(input()) , float(input())
# you know --> single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split(",")))

names = input("enter the names:").split(",")
print(names)
name1,name2 = map(str,input("enter the names:").split(','))
print(name1,name2)

#tokens --> numeric datatypes--> operators --> flow of thw program
#control block statements
#conditional statements
#repetition statements

#conditional statements --> if usage

#syntax :

if <condition>:
    statement(s)

#age = 15
age = int(input("enter the age:"))
if age > 18:
    print("0your age is:",age)

age = int(input("enter the age:"))
if age >=18 and age in [19,20,21]:
    print("ur age is",age )
print (age)

#if else syntax

if <condition>:
    statement(d)

else:
    statement(d)

#vote eligibility --> to check his/her voter eligibility and give access

age = int(input("enter the age:"))
if age > 18:
    print("u have voter eligibility and age is",age)
    print("accesss granted")
else :
    age = 18-age
    print("u need to wait for more",age,"years")
    
#same case lets use only --> if, else
age = int(input("enter the age:"))
if age >0:
    if age > 18:
        print("u have voter eligibility and age is",age)
        print("accesss granted")
    else :
        age = 18-age
        print("u need to wait for more",age,"years")
else :
    print("you have entered -ve number/0")
    
#task : student marks and grade analyzer
90-100 --> "A"
80-89 --> "B"
70-79 --> "C"
60-69 --> "D"
>60 --> FAIL

#also -ve cases should not be allowed and marks should not be greater than 100
marks= int(input("enter the marks:"))
if marks < 101 :
    if marks >= 90 and marks <= 100 :
        print("you got grade: A")
    if marks >= 80 and marks <= 89 :
        print("you got grade: B")
    if marks >= 70 and marks <= 79 :
        print("you got grade: c")
    if marks >= 60 and marks <= 69 :
        print("you got grade: D")
    if marks < 60 :
        print ("you got failed")
else :
    print("you have entered -ve marks or greater than 100")













































