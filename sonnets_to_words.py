import string
sonnets = open('shakespeares_sonnets.txt').readlines()
word_set = set([elt.strip() for elt in open('sowpods.txt')])
sonnet_words = set()

def strip_puncuation(word):
    word.replace('-',' ')
    apostrophe_index = word.find("'")
    if apostrophe_index != -1:
        return None
    return word.strip(string.punctuation)

for line in sonnets:
    line_words = line.replace('-',' ')
    if len(line_words) <= 1:
        continue
    for word in line_words.split():
        stripped = strip_puncuation(word)
        if stripped and len(stripped) >1:
            sonnet_words.add(stripped.upper())

sonnet_words = list(sonnet_words)
sonnet_words.sort()
file_handler = open('sonnet_words_2.txt','w')
for word in sonnet_words:
    file_handler.write(word + '\n')
file_handler.close()