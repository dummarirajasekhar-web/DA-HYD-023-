''' 
user = input("Enter a sentence: ")
methods = ["upper","lower","title","capitalize","swapcase"]
for i in methods:
    if i == 'upper':
        print("Upper :", user.upper())
    elif i == 'lower':
        print("lower :", user.lower())
    elif i == 'title':
        print("title :", user.title())
    elif i == 'capitalize':
        print("capitalize :", user.capitalize())
    elif i == 'swapcase':
        print("swapcase :", user.swapcase())
if user.isupper() :
    print("sentance is uppercase",True)
else:
    print("sentance is not uppercase",False)
if user.islower() :
    print("sentance is lowercase",True)
else:
    print("sentance is not lowercase",False)
if user.istitle() :
    print("sentance is title",True)
else: 
    print("sentance is not title",False)
'''
'''
# username
while (True):
    username = input("enter the username:")
    if username == "quit":
        break
    if username.isalnum():
        print("username contains letter and numbers")
    else :
        print("username doesn't contains letter and numbers")
    if username[0].isalpha():
        print("username begins with letter")
    else :
        print("username not start letter")
    if username.isidentifier():
        print("username contains valid python identifier")
    else :
        print("username contains invalid")
    if username.isascii():
        print("username contains ascii value")
    else:
        print("username doesn't contains ascii value")
'''



















