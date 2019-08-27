known_users = ['Girisha','Sonu','Atul','Ren','Rhea','Swati','Anshu']
print(len(known_users))

while True:
    print('Hi my name is Travis')
    name = input('What is your name?').strip().capitalize()

    if name in known_users:
        print('Hello',name)
        remove = input('Would you like to removed from the system y/n :').lower()
        if remove == 'y':
            known_users.remove(name)
        elif remove == 'n':
            print('Yay!! YOU ARE STAYING WITH MEEEEEE')
    else:
        print('Hmmm I don\'t think I have met you yet',name)
        add_me = input('would you like to be added to the system(y/n): ')
        if add_me == 'y':
            known_users.append(name)
        elif add_me == 'n':
            print('Oh why does no one want to be with poor old Travis...')
