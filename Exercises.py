import time
import random

Username = input('Choose a new username: ')

def loading(freq, duration):
    symbol = '.'
    for i in range(duration):
        time.sleep(freq)
        print('loading' + symbol) 
        symbol += '.'
        if symbol.count('.') == 4:
            symbol = '.'

def memcheck():
    time.sleep(1)
    print('memtest...')
    time.sleep(1)
    print('memory OK')
    time.sleep(1)

def welcome_user():
    time.sleep(1)
    print('Welcome Back', Username)
    time.sleep(1)

while True:
    Password = input('Choose a new password: ') 
    if len(Password) <6:
        print('The length of your password needs to be more than 5 characters')
        continue
    else:
        break

while True:
    username_input = input('Please enter your username: ')
    if username_input != Username :
        print('There is no such registered username')
        continue
    elif username_input == Username:
        break
while True:
    password_input = input('Please enter your password: ')
    if password_input != Password:
        print('Incorrect password, please try again')   
        continue
    elif password_input == Password:
        memcheck()
        loading(random.uniform(0.9, 2),6)
        welcome_user()
        break
  

print ('/////////////////////// SimpleCalc / Copyright 1979, Kyronsoft')
print ('/////////////////////// Version 2.0')
print ('/////////////////////// Copyright 1979, Kyrosoft')
 

        
   


