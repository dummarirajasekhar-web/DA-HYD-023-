'''
string --> CaseConversions, Searching & finding,string testing methods
replace , space removal
'''
#searching, finding, replacing,joining...
'''
a= 'rajasekhar'
print(len(a))
print(min(a))
print(max(a))
'''
# finding index
'''
b= a.index('a') #it returns the index position
print(b)
c= a.index('a', 2) #it returns the next oocurance
print(c)
d= a.index('a', 8)
print(d)
e = a.index('a',2,9)
print(e)
'''
#rindex()--> returns the last occurance
'''
b= a.rindex("a") #here 'a' is occuring at 8th index
print(b)
c= a.rindex("a",1,9)
'''
#count() --> returns the number of items object is repeating

#print('rajasekhar'.count('a'))

#find() --> first occurance but it avoid error returns -1 if substring is not found
'''
print('rajasekhar'.find('a'))
print('rajasekhar'.find('x')) #it returns -1
print('rajasekhar'.rfind('a')) # last occurance

a = "Data"
print(len(a))
for i in a:
    print(a.count(i),a.index(i))
'''
#replacing, splitting, joining
#REPLACE
#strings are immutable
'''
a = 'codegnan'
print(a.replace('n','r'))
print(a)
a = a.replace("n","r")
print(a)
b = "asdfghjk#wedfghgfnb".replace("#","")
print(b)
'''
#splitting
"""
a= 'raj shashank gowtham'
b= a.split(" ")
print(b)
#c = b.split(",")
#print(c)
"""
# JOIN()--> Its iterable. Concatenate any number of strings
'''
a = 'code'
b = 'gnan'
print(a.join(b))
print(b.join(a))
print(' '.join('raj'))
print('&'.join('raj'))
'''
#string testing methods (boolean)
#isalpha(), isalnum(), isdigit(), isupper(),islower()...

a = 'Codegnan123'
'''
print(a.isalnum())
print(a.isalpha()) #returns true nly for alphabets
print(a.isdigit()) #returns true nly for digits string
print('12345'.isnumeric()) #this has upper edge(num,frac,romans)
'''
print('codegnan'.startswith('c'))

print('codegnan'.startswith('g',4))

print('codegnan'.endswith('n'))

print('codegnan'.islower()) #it returns true for all lowercase

print('COdegnan'.isupper())

print('Codegnan Python'.istitle())

#Space removal --> strip() (removes leading and trailing spaces)
'''
a = "  codegnan"
print(a.strip())
b = input("enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zeros as per the given numeric string
print('234'.zfill(8))

#center(), ljust(), rjust()--> Alignment of strings (check length and then modify the width accordingly)

print('hai'.center(6))
print('hai'.center(6,"$"))

print('hai'.ljust(5,'@'))
print('hai'.rjust(5,'@'))









