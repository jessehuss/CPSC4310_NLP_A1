from nltk.corpus import brown, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk import WordNetLemmatizer

stopWords = set(stopwords.words('english'))
wln = WordNetLemmatizer()
lemmatizer = WordNetLemmatizer()
porter = PorterStemmer()
lancaster = LancasterStemmer()

for cat in brown.categories():
    words = brown.words(categories=cat)
    noStopWords = [nsw for nsw in words if nsw not in stopWords]
    lemmatizedWords = [wln.lemmatize(lw) for lw in words]
    pstemmedWords = [porter.stem(psw) for psw in words]
    lstemmedWords = [lancaster.stem(lsw) for lsw in words]
    print (cat.upper() + ':')
    print (f'Word Tokens:\n{str(len(words))} vanilla.\n{str(len(noStopWords))} no stop words.\n{str(len(lemmatizedWords))} lemmatized.\n{str(len(pstemmedWords))} porter stemmed.\n{str(len(lstemmedWords))} lancaster scanned.\n' )
    print (f'Word Types:\n{str(len(set(words)))} vanilla.\n{str(len(set(noStopWords)))} no stop words.\n{str(len(set(lemmatizedWords)))} lemmatized.\n{str(len(set(pstemmedWords)))} porter stemmed.\n{str(len(set(lstemmedWords)))} lancaster scanned.\n' )

print (f'Vocabulary Size:\n{str(len(brown.words()))} vanilla.\n{str(len([word for word in brown.words() if word not in stopWords]))} no stop words.\n{str(len([wln.lemmatize(w) for w in brown.words()]))} lemmatized.\n{str(len([porter.stem(w) for w in brown.words()]))} porter stemmed.\n{str(len([lancaster.stem(w) for w in brown.words()]))} lancaster scanned.' )