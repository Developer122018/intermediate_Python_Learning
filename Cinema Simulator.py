films = {
    'Finding Dory':[3,6],
    'Bourne':[18,5],
    'Tarzan':[15,12],
    'Ghost Busters':[12,23],
}
list_of_films = 'Finding Dory','Bourne','Tarzan','Ghost Busters'
while True:
    print(list_of_films)
    choice = input('What film would you like to watch?').strip().title()
    num_of_peeps = int(input('How many people are coming?').strip())
    if choice in films:
        age = int(input('How old is the youngest person in your group?').strip())
        if age >= films[choice][0]:
            if films[choice][1]>num_of_peeps:
                print('Enjoy the fim!')
                films[choice][1] = films[choice][1] - num_of_peeps
            else:
                print('There aren\'t enough seats!')
        else:
            print('You are too young to see this film')
    else:
        print('We don\'t have that film...')