'''
Usage of else with for--> the else
'''
'''
#for with else...

#longest streak
work_log = [0,1,1,1,0,1,0]
longest = 0
current = 0
for i in work_log:
    if i == 1:
        current = current + 1
    
        if current > longest:
            longest = current
            print(longest)
            #break
    else :
       current = 0
else:
    print(f'longest streak is {longest}')
'''
#for - else with ph notification scenario
'''
notifications = [0,0,0,0]
for notification in notifications:
    if notification == 1:
        print("unread notification")
        break
else:
    print("all caught up")
'''
'''
notifications =list(map(int,input("enter the values as 0 or 1:").split(",")))
print(notifications)
for notification in notifications:
    if notification == 1:
        print("unread notification")
     break
else:
    print("all caught up")
'''
#while-->it relies on condition,it will completely executed until the condition satisfied
'''
syntax while:
while <condition>:
    statements(s)...
    ....
'''
'''
while True:
    print("yes")
#it runs an infinite loop we need press ctrl+c (keyboard interrupt)
'''
'''
i=1 #initialised statement
while i<=10:
    print(i)
    i=i+1 #counter
'''
'''
i=10 #initialised statement
while i<=10:
    print(i)

    i=i-1 #counter
    if i == 0:
     break
'''
'''
i=0 #initialised statement
while i<=10:
    print(10-i)
    i=i+1
'''
#banking scenario --> pin authentication attempts 3

pin = "2612"
max_attempts = 3
cur_attempts = 0
while cur_attempts< max_attempts:
    entered_pin = input("enter the pin:")
    cur_attempts = cur_attempts + 1
    if entered_pin == pin:
        print("login successfully ")
        break
    else :
        print("entered pin is wrong.. Try again carefully")
else:
    print("ACCOUNT LOACKED.. TRY AFTER 24 HOURS")






























