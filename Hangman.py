import random

def choose_random_word():
    words=[]
    with open('sowpods.txt', 'r') as file:
        line = file.readline()
        while line:
            words.append(line.replace("\n","".strip()))
            line = file.readline()
    choice =words[random.randint(0,len(words)-1)]
    return choice

secret_word = choose_random_word()
#secret_word = 'autobiographies'

#print(secret_word)
list_of_letters = list(secret_word)
alphabet = list('abcdefghijklmnopqrstuvwxyz')
dashes = []
guess_count = 0
guess_list = []

finished = 0
print('Welcome to Hangman!')
len_of_word = len(secret_word)

for i in range(len_of_word):
    dashes += "_"
print(' '.join(dashes))

while finished != len_of_word:

  #  print(finished)
 #   print(len_of_word)
    guess = input('What is your guess? ').strip().lower()


    if len(guess) > 1:
        print('Please enter only one letter')

    if guess not in alphabet:
        print('That has been said already!')
        continue
    else:
        if guess in alphabet:
            alphabet.remove(guess)

    guess_count += 1
    x = None

    for index1, x in enumerate(list_of_letters):
        if x == guess:
            character_index = list_of_letters.index(x,index1)
            dashes[character_index] = guess
            finished += 1
            print(' '.join(dashes))

if finished == len_of_word:
    print('It took you ',guess_count,' goes to solve this word')