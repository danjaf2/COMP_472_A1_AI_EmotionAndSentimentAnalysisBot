import json
import gzip

import nltk
from pandas import DataFrame
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import matplotlib
from sklearn import preprocessing
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import gensim.downloader as gsm
from nltk.tokenize import word_tokenize
import nltk
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
#nltk.download('punkt')
def addMatrix(X, Y):

    result=np.zeros_like(X)
    for i in range(len(X)):
            print(X[0])
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]

    return result



data = gsm.load('word2vec-google-news-300')
with gzip.open("goemotions.json.gz", "rb") as f:
    fullData = json.loads(f.read().decode("ascii"))

length = len(fullData)
emotions = [None]*length
posts = [None]*length
sentiments = [None]*length



for i in range(length):
    emotions[i]=fullData[i][1]
    posts[i]=fullData[i][0]
    sentiments[i]= fullData[i][2]



#Basic Naive Bayes

print('--------------Word2Vec EMBEDDINGS------------------------')
vectorizer = CountVectorizer(stop_words='english')
sentiments_enconded= sentiments
posts_encoded =[None]*(len(posts))
for i in range (len(posts)):
    posts_encoded[i] = word_tokenize(posts[i])



X_train, X_test, y_train, y_test=train_test_split(posts_encoded,sentiments_enconded, stratify=sentiments_enconded, test_size=0.2, random_state=0)

numberOfTokens =0;
for i in range (len(X_train)):
    numberOfTokens += len(X_train[i])
print(numberOfTokens)


X_train_final= []
counter=0
for arr in X_train:
    posts_encoded_sum =[]
    loop=0
    for i in arr:
        try:
            posts_encoded_sum.append(np.array(data[str(i)]).tolist())
            posts_encoded_sum=np.array(posts_encoded_sum).tolist()
            counter= counter + 1
        except:
            counter=counter
    if counter>0:
        average= np.mean(posts_encoded_sum, axis=0)
        X_train_final.append(average)
        counter = 0
        loop=loop+1
    else:
        X_train_final.append(np.zeros_like(data['king']).tolist())
        counter = 0
        loop = loop + 1

X_test_final= []
counter=0
for arr in X_test:
    posts_encoded_sum =[]
    loop=0
    for i in arr:
        try:
            posts_encoded_sum.append(np.array(data[str(i)]).tolist())
            posts_encoded_sum = np.array(posts_encoded_sum).tolist()
            counter = counter + 1
        except:
            counter=counter
    if counter > 0:
        average= np.mean(posts_encoded_sum, axis=0)
        X_test_final.append(average)
        counter=0
        loop=loop+1
    else:
        X_test_final.append(np.zeros_like(data['king']).tolist())
        counter = 0
        loop = loop + 1

print(X_train_final)
print("Creating model")
classifier= MLPClassifier(max_iter=1)
modelBE= classifier.fit(X_train_final, y_train)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
predictions = classifier.predict(X_test_final)
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
print(accuracy_score(y_test, predictions))















#print("The length of the vocabulary is "+str(len(vectorizer.vocabulary_)) )



print('------------------------------------------------------------------')

