import nltk
nltk.download('punkt')
raw_text = "Leo was born in United States."
tokens = nltk.tokenize.word_tokenize(raw_text)
print('Token:')
for token in tokens:
    print(token)