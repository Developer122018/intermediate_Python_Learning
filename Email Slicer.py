user_email = input('What is your email address?: ').strip()
username = user_email[:user_email.index('@')-1]
user_domain_name = user_email[:user_email.index('@')+1:]
output = 'Your username is {} and your domain name is {}.'.format(username,user_domain_name)
print(output)
