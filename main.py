import csv
import random
from numpy import cos
import pyttsx3
import pandas as pd
import scipy as sp
import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()  as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print("user said: ",query)

        except Exception as e:
            #print(e)

            print("Can you say that again please..")
            return "None"
        return query


questions = pd.read_csv('C:\\Users\\hp\\Dropbox\\Mocker AI py files\\ques.csv', header = None)
questions = pd.DataFrame(questions)
print(questions)

question = ([])
for i in range(len(questions[0])):
    question.append(questions[0][i])
question.pop(0)

speak("hey geek Mocker this side, let's start your interview with first question, your first question is")

ques = random.sample(question,1)





print(ques)
speak(ques)

keywords = questions[1:2].iloc[:,1:][:].values
print("keywords : ", keywords)

keywords = keywords
keywords = str(keywords).lower()
answer = takeCommand().lower()
print("user said : ", answer)


x_list = word_tokenize(keywords)
print(x_list)
y_list = word_tokenize(answer)
print(y_list)

sw = stopwords.words('english')
l1 =[];l2 =[]


X_set = {w for w in x_list if not w in sw}
Y_set = {w for w in y_list if not w in sw}


rvector = X_set.union(Y_set)
for w in rvector:
    if w in X_set:
        l1.append(1)
    else:
        l1.append(0)
    if w in Y_set:
        l2.append(1)
    else:
        l2.append(0)
c = 0

for i in range(len(rvector)):
    c += l1[i] * l2[i]
cosine = c / float((sum(l1) * sum(l2)) ** 0.2)
perc = round(cosine,2)*100
print("cosine similarity:", perc,"%")
speak(("cosine similarity:",perc,"%"))







