#EVEN OR ODD
'''num = int(input("enter the number:"))
if num > 0 and num%2 == 0:
     print("entered number is  positive even number")
    
elif num > 0 and num%2 == 1:
    print("entered number is positve odd number")
elif num < 0 and num%2 == 0:
    print("entered number is  negatove even number")
elif num < 0 and num%2 == 1:
    print("entered number is positve odd number")
else :
    print("0 neither even nor odd ")
'''
#Grade Checker
'''
marks = int(input('Enter marks:'))
if marks <0 or marks >100:
   print('Invalid marks enetred')
                  
elif marks >=90:
    print('Grade:A')
    print('Remark:Outstanding!')
elif marks >=80:
     print('Grade:B')
     print('Remark:Excellent')
elif marks >=70:
     print('Grade:C')
     print('Remark:Good')
elif marks >=60:
     print('Grade:D')
     print('Remark:Fair,need improvement')
elif marks >=50:
     print('Grade:E')
     print('Remark:Poor,needs serious improvement')
else:
    marks <50
    print('Grade:F')
    print('Remark:Failed,needs to reappear')
'''

#Season Identifier
'''
month = int(input('Enter the month number:'))
if month <1 or month>12:
    print('Invalid month entered')

elif month ==12 or month ==1 or month ==2:
     print('Season:Winter')

elif month ==3 or month ==4 or month ==5:
     print('Season:Spring')
     
elif month ==6 or month ==7 or month ==8:
    print('Season:Summer')
    
else:
    print('Season:Autumn')
'''



    
'''
user = "raj"
passw = "hr123"
username = input("enter the username:")
password = input("enter the password:")
if username == user and password == passw :
    print("LOGIN SUCCESSFULL")
else :
    print("LOGIN UNSUCCESSFULL  WRONG CREDENTIALS ENTERED")
'''
#positive and negative number code
'''
num = int(input("enter the number:"))
if num > 0:
    print("entered number is positive number ")
elif num < 0:
    print("entered number is negative number ")
else :
    print("entered number is 0 ")
   '''
#ATM CODE
'''
pin = 1018
acc_bal = 10000
uspin = int(input("enter the your pin:"))
if uspin == pin :
    print("entered pin is correct")
    withdraw = int(input("enter the amount:"))
    if withdraw <= acc_bal :
        print("amount debited successfully", "remaining balance is",acc_bal-withdraw)
    if withdraw > acc_bal:
        print("please check ur account balance ")
else:
    print ("entered wrong pin")
'''
# letter checking
'''
vowels = ["A","E","I","O","U","a","e","i","o","u"]
let = input("enter the letter:")
if let in vowels:
    print("entered letter is vowel")
else:
    print("entered letter is consonants")
'''









