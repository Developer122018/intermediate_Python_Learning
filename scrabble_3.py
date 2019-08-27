import scrabble_script
#print all words containing 'aeiou'
vowels = 'aeiou'
def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True


for word in scrabble_script.wordlist:
    if has_all_vowels(word):
        print(word)
