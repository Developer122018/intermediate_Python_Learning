# String.method()

print('hello'.count('l'))

text = 'happy birthday'
print(text.count('rt'))

x = 'Happy Birthday'
print(x.lower())
print(x.upper())
print(x)
#Strings are unchangable - they are overwritten

x = x.upper()
print(x)
x = x.lower()
print(x,'lower')
x = x .capitalize()
print(x,'Capitalized')
x = x .title()
print(x,'Title')

print( x.islower(),'x is lower?')
print(x.isupper(),'x is upper')
print(x.istitle(),'x is title')
print(x.isalpha(),'Are all charachters in x alphabets')
print('There is a space in "Happy Birthday" thus x is not alpha ')
