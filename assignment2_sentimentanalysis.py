# -*- coding: utf-8 -*-
"""Assignment2_SentimentAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oZSyWWhRXxgPWJWJmNPIv3J9PP_Knbu9

#This notebook is used for IMDB Review Sentiment Analysis
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import time
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.svm import SVC

"""#Data Loading process"""

#Load Data and get all info

data=pd.read_csv('M:/navjeet/NLP/Assignment2_2316574_kaurn57801/IMDB Dataset.csv')
data.info()

"""#Data Prepocessing"""

lb = LabelEncoder()
data['sentiment'] = pd.Series(lb.fit_transform(data['sentiment']),dtype='int32')
data.info()

"""#Data Analysis"""

#Checking for data baising
data['sentiment'].value_counts().plot(kind='bar')

#Calculating the Frequency Distribution For the Positive Reviews ans Negative Reviews

negativeFD = nltk.FreqDist(word  for text in data[data["sentiment"] == 0]["review"] for word in text.lower().split())
positiveFD = nltk.FreqDist(word  for text in data[data["sentiment"] == 1]["review"] for word in text.lower().split())

plt.subplots(figsize=(8,6))
plt.title("Most Used Words in Positive Reviews")
positiveFD.plot(50)
plt.show()

plt.subplots(figsize=(8,6))
plt.title("Most Used Words in Negative Reviews")
negativeFD.plot(50)
plt.show()

"""#Converting Text To Vectors"""

cleanedData = []

lemma = WordNetLemmatizer()
swords = stopwords.words("english")
for text in data["review"]:
    # Cleaning links
    text = re.sub(r'http\S+', '', text)
    # Cleaning everything except alphabetical and numerical characters
    text = re.sub("[^a-zA-Z0-9]"," ",text)
    # Tokenizing and lemmatizing
    text = nltk.word_tokenize(text.lower())
    text = [lemma.lemmatize(word) for word in text]
    # Removing stopwords
    text = [word for word in text if word not in swords]
    # Joining
    text = " ".join(text)
    cleanedData.append(text)

vectorizer = CountVectorizer(max_features=10000)
BOW = vectorizer.fit_transform(cleanedData)

"""#Spliting Data Into Train and Test"""

x_train,x_test,y_train,y_test = train_test_split(BOW,np.asarray(data["sentiment"]))

start_time = time.time()
model = SVC(kernel='linear')
model.fit(x_train,y_train)
end_time = time.time()
process_time = round(end_time-start_time,2)
print("Fitting SVC took {} seconds for linear kernel".format(process_time))
predictions = model.predict(x_test)
print("Accuracy of model is {}%".format(accuracy_score(y_test,predictions) * 100))


start_time = time.time()
model = SVC(kernel='poly',degree=4)
model.fit(x_train,y_train)
end_time = time.time()
process_time = round(end_time-start_time,2)
print("Fitting SVC took {} seconds for Polynomial Kernel".format(process_time))
predictions = model.predict(x_test)
print("Accuracy of model is {}%".format(accuracy_score(y_test,predictions) * 100))


start_time = time.time()
model = SVC(kernel='rbf')
model.fit(x_train,y_train)
end_time = time.time()
process_time = round(end_time-start_time,2)
print("Fitting SVC took {} seconds for Radial Based Function Kernel".format(process_time))
predictions = model.predict(x_test)
print("Accuracy of model is {}%".format(accuracy_score(y_test,predictions) * 100))