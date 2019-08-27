sentence = input('What sentence would you like to convert to Pig Latin').lower().strip()
#sentence="My Name is Atul".lower().strip()
words = sentence.split(' ')
new_words = []
new_word = ''

for word in words:
    new_word = ''
    vowel_pos = 0
    if word[0] in 'aeiou':
       new_word = word + 'yay'
    else:
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos +=1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest+cons+'ay'
    new_words.append(new_word)
#print(new_words)
output = " ".join(new_words)
print(output)
#new_words.join(' ')