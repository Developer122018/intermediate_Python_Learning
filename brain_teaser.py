#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix
# of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

print('Welcome to Random Password Generator')
#input('How strong would you like your password to be?')
while 1 + 2 == 3 :
    try:
        length_of_password = int(input('How Long would you like your password to be?'))
        break
    except Exception as error:
        print('Try again - as a number please')

import random

stuf
f = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password =  "".join(random.sample(stuff,length_of_password ))
print (password)