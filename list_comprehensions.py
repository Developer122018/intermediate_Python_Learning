my_list = ['my school books ', 'my rucksack ', 'my uniform ', 'my stationery ', 'a padlock ']
print([elt*2 for elt in my_list])
squares = [elt * elt for elt in range(10)]
print(squares)
word_list = [elt.strip()for elt in open('sowpods.txt').readlines()]
#[elt for elt in word_list if 'UU' in elt

word_list2 = [word for word in word_list]
print(word_list2)

[word for word in word_list if word == word[::-1]]