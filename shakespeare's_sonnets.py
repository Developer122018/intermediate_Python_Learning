import time
my_words = [elt.strip() for elt in open('sonnet_words.txt','r').readlines()]
word_list = [elt.strip() for elt in open('sowpods.txt','r').readlines()]
word_set = set(word_list)

counter = 0
my_words = [x.lower() for x in my_words]
start = time.time()

for word in my_words:
    if word not in word_set:
        print(word)
        counter += 1
stop = time.time()

print('Total new words : %d' % counter)
print('Time elasped = %.1f seconds' % (stop -start))