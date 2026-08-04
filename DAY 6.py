#CONTROL STATEMENTS --> FLOW OF EXECUTION OF THE PROGRAM
#CONDITIONAL STATEMENTS --> if, elif,else...
#repetition statements (loops)--> for , while (for with else)&(while with else)
#jumping statements --> break ,continue ,pass

# LOOPS --> loops are helpful for repetition (automative tasks)
# for keyword will be helpful to iterate over a sequence / range
# syntax for (for keyword)
'''
for <temp_var> in sequence/range:
    statements...
#range (start,stop,step)
#by default range picks 0 as start value
for i in range(10):
    print(i)
#In above case we got 10 iterations
for i in range(1,10):
   # if i>5:
        #print(f"value of i is {i}")
   # Now i want to get only even numbers with above condition
    if i > 5 and i%2 == 0:
        print( f" Final value of i is {i}")

# range (start,stop,step)--> here step --> interval..
for i in range(1,10,-2):
    print(i)
    print("DONE")

for i in range(-10,0,1):
    print(i)
    print("DONE")

# []--> WE GENEALLY lists
names = ['raj','hemanth','srinu']
print(len(names)) #len(obj) --> returns the number of items in a container
for i in names:
   # print(i)
   # print(f"student name is {i}")
    if i == "raj":
        print(f"student name is {i}")

 
#calculate the sum of first 10 even numbers
result = 0
for i in range(0,41):
    if i%2 == 0:
        result= result + i

print(f"sum of numbers is {result}")
'''
#longest streak
work_log = [0,1,1,1,0,1,0]
longest = 0
current = 0
for i in work_log:
    if i == 1:
        current = current + 1
    
        if current > longest:
            longest = current
    else :
       current = 0
print(longest)
           
        







