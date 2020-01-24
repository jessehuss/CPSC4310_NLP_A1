from nltk.corpus import brown

count = 0

for cat in brown.categories():
    print (cat + ' has ' + str(len(brown.words(categories=cat))) + ' word tokens.')
    print (cat + ' has ' + str(len(set(brown.words(categories=cat)))) + ' word types.')
    count += len(brown.words(categories=cat))

print ('Vocabulary size of the entire corpus is: ' + str(len(brown.words())) - 1 + ' and the sum of words from each category is: ' + str(count) - 1)

# How many word tokens does each category/genre have?
# How many word types does each category/genre have?
# What is the vocabulary size of the whole corpus?

# Variation chooser:
# a) with/without stopwords
# b) with/without lemmatization
# c) with/without stemming