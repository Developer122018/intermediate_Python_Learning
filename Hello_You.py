#Ask user for name
user_name = input('What is your name?: ')
#Ask user for age
while 1 < 2:
    try:
        user_age = int(input('How old are you?: '))
        break
    except ValueError as a:
        print('Try again - as a number please')
user_city = input('What city do you live in?: ')
#Ask user what they enjoy
user_enjoyment= input('What do you enjoy?: ')
user_name = user_name.title()
user_city = user_city.title()
user_enjoyment = user_enjoyment.lower()
#Create output text
string = 'Your name is {} and you are {} years old. You live in {} and you enjoy {}'
output = string.format(user_name,user_age,user_city,user_enjoyment)
print(output)
#def a_sentence_about_you():
#    print('Your name is',user_name,',you are',user_age,'years old and you live in',user_city,'- you enjoy',user_enjoyment)
#Print output to screen
#a_sentence_about_you()