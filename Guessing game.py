import random
import time
import sys
number_of_goes = 0

#First stage of the program
print('Loading...')
time.sleep(3)
print('Welcome to The Guessing Game')
time.sleep(2)
print('What would you like the range of numbers to be?')
time.sleep(2)
num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
number_generated = random.randint(num1,num2)
number_generated = int(number_generated)
is_guess_correct = False

print('Loading...')
time.sleep(2)
print('The number has been generated!')


while 1 < 2:
    time.sleep(1)
    print('What\'s your guess?')
    while is_guess_correct == False:
        guess = int(input())
        if guess > number_generated:
            print('You are too high!')
            number_of_goes += 1
            continue
        elif guess < number_generated:
            print('You are too low!')
            number_of_goes += 1
            continue
        elif guess == number_generated:
            print('You got my number!')
            number_of_goes += 1
            is_guess_correct = True
            continue
        else:
            print('That number was not in the range you gave')


    print('You took %d goes'% (number_of_goes))
    time.sleep(1)
    print('Hope you had fun playing The Guessing Game')
    time.sleep(1)
    print('See you soon')
    sys.exit()