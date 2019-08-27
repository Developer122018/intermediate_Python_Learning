#try_again = False


def add(*number):
    total = 0
    for numbers in number:
        total = total + numbers
    return (total)


def subtract(*number):
    total = 0
    for numbers in number:
     total = total - numbers
    return (total)


def multiply(*number):
    total = 0
    for numbers in number:
        total = total * numbers
    return (total)


def divide(*number):
    total = 0
    for numbers in number:
        total = total / numbers
    return (total)

choice = tuple(input('What is your calculation?').strip())
choice_len = len(choice) +1
OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}
choices = 0
list_of_odd_choices = []

while choices <  choice_len:

    choices = 0
    choices += 1

    for x in range(choice_len):
        if choices / 2 != 0:
            list_of_odd_choices.append(choices)
        else:
            pass