import random
exit = False

print('Welcome to baby translator. '
      'This baby will not be satisfied until you say a certain catchphrase'
      'ENJOYYYY')

while exit == False:
    list_of_questions = ['Why is the sky blue?','Why is chocolate so yummy?','Why is there a face on the moon?','Where are all the dinosaurs']
    question = random.choice(list_of_questions)
    answer = input(question).strip().lower()
    if answer == exit:
        break
    while answer != 'just because':
        answer = input('Why?').strip().lower()
    print('Oh....Ok')