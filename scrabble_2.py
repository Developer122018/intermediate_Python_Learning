import scrabble_script
import string
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble_script.wordlist:
        if letter *2 in word:
            exists = True
            break
    if not exists:
        print('There are no English words with a double of',letter)