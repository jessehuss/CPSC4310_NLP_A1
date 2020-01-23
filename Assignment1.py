from nltk.corpus import brown

for cat in brown.categories():
    print (cat + ' has ' + str(len(brown.words(categories=cat))) + ' words.')

# How many word tokens does each category/genre have?
# How many word types does each category/genre have?
# What is the vocabulary size of the whole corpus?

# Variation chooser:
# a) with/without stopwords
# b) with/without lemmatization
# c) with/without stemming