import re
 
with open('Eng.txt', 'r') as f:
    word_count = dict()
    words = re.split('[^a-zA-A]+', f.read())
    for word in words:
        word = word.lower()
        if not word:
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
print(word_count)