import scrabble_script
palindrome = False
list_of_lengths = []
palindrome_and_length_dict = {}
for word in scrabble_script.wordlist:
    word = word.rstrip()
    word_length = len(word)
    result = ''.join(reversed(word))
    if word == result:
        palindrome_and_length_dict [word] = word_length
        list_of_lengths.append(word_length)
    else:
        pass

longest_palindrome = max(list_of_lengths)
for key,value in palindrome_and_length_dict.items():
    if longest_palindrome == value:
        print(key)