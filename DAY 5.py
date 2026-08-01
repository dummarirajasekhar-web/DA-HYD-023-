'''
#elif keyword --> if-elif-else
if <condition 1>:
    statements(s)
elif <condition 2>:
    statements(s)
elif <condition 3>:
    statements(s)
else :
    statements(s)
    
marks = int(input("enter the student marks : "))
if marks >= 100 :
    print ("entered values should be grwater than 1 and less than 100")
elif marks >= 90 and marks <= 100 :
    print("you got grade: A")
elif marks >= 80 and marks <= 89 :
    print("you got grade: B")
elif marks >= 70 and marks <= 79 :
    print("you got grade: c")
elif marks >= 60 and marks <= 69 :
    print("you got grade: D")
elif marks < 60 and marks >= 0 :
    print ("you got failed")
else:
    print ("No negative values")
   
#voter eligibility checkcase --> make sure to satisfy all possible conditions
#>=18 --> Access
#<18 --> no 0f years eligibility should tell
# negative values --> not acceptable
age = int(input("enter the age:"))
if age >=18 and age <= 100:
    print ("user has eligibility")
    print ("ACCESS GRANTED")
elif age < 18 and age>0:
    print("user has not eligible for vote")
    print("user need to wait for more",18-age,"years")
else:
    print("only positive values and less than 100 acceptable")


#output --> print() --> we can pass any pass any value also use sep and end 
#output formatting --> old style formatting (using commas)
# % usage (%f , %d), .format() usage, fstring notation

a,b = 7,9
print(a)
print(b)
print(a,b)
name = "codegnan"; course= "data analysis"
print(name,course,sep=",")
#end = '\n' , \t --> TAB SPACE
print(name,course,end="\t")
print(a,b, end=" ")
print ("hyderabad")

#USING COMMAS

name = "codegnan"; age=12; batch="DA-023"; place="hyderabad"
print(name,"is in", place, batch,"is running batch",)

#OLD STYLE FORMATTING --> %d--> integer, %s--> string, %f--> float
salary = 24234.1234
print("His salary is %d" %(salary))
print("His salary is %f" %(salary))
print("His sal
      ary is %.1f" %(salary))# --> %.1f --> rounded to 1 decimal 

# .format() usage

name = "codegnan"; place="hyderabad"
print("{} is in {}".format(name,place)) # order matters
'''
# fstring usage (MORE RECOMMENDED)
#print(f"{name} is in {place}")
#print(f"{"saketh"} is in {name}")
#example:
name = "RAJ"
score = 52
print(f"{name} scored {score} runs in yesterday match")














    
