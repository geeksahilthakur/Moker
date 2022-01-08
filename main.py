import random
import pyttsx3
import pandas as pd
import json
import pickle
import speech_recognition as sr
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
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("user said: ", query)

        except Exception as e:
            # print(e)

            print("Can you say that again please..")
            return "None"
        return query


with open("D:\\Mocker\\Mocker\\mainques.json") as json_data:
    question = json.load(json_data)
    q = pd.DataFrame(question)
    x = random.randint(0, 7)
    y = x + 1
    print(x, y)

# intro of the mock interview
"""speak("Hey geek welcome to Mocker AI. Enter your name in oder to start your mock interview")
name = input("Enter your name :")
speak(("welcome", name, "to your first Mock Interview "))
speak("are you ready to start your mock interview")
query = takeCommand().lower()
if 'yes' in query:
    speak(("Great", name))

speak(
    "great, here is quick guide about this mock interview. I'll ask you 10 questions and it will include a coding "
    "problem to. And on the bases of your answers i'll give you marks")
speak("so let's start your interview with first question, your first question is ")"""

ques = (q['questions'][x]['%s' % (y)])
print(ques)
speak(ques)

print(q['questions'][x]['keywords'])

for i in range(len(q['questions'][x]['keywords'])):
    '''print(q['questions'][1]['keywords'][i])'''

keyword = (q['questions'][x]['keywords'][i])
keywords = keyword
keywords = str(keywords).lower()
answer = takeCommand().lower()
print("user said : ", answer)

x_list = word_tokenize(keywords)
print(x_list)
y_list = word_tokenize(answer)
print(y_list)

sw = stopwords.words('english')
l1 = []
l2 = []

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
cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
perc = round(cosine, 2) * 100
print("Answer matching percentage is:", perc, "%")
speak(("Answer matching percentage is", perc, "%"))

count = 0

while (count < 2):
    with open("D:\\Mocker\\Mocker\\mainques.json") as json_data:
        question = json.load(json_data)
        q = pd.DataFrame(question)
        x = random.randint(0, 7)
        y = x + 1
        print(x, y)
        ques = (q['questions'][x]['%s' % (y)])
        count = count + 1
        print(ques)
        speak(ques)

        print(q['questions'][x]['keywords'])

        for i in range(len(q['questions'][x]['keywords'])):
            '''print(q['questions'][1]['keywords'][i])'''

        keyword = (q['questions'][x]['keywords'][i])
        keywords = keyword
        keywords = str(keywords).lower()
        answer = takeCommand().lower()
        print("user said : ", answer)

        x_list = word_tokenize(keywords)
        print(x_list)
        y_list = word_tokenize(answer)
        print(y_list)

        sw = stopwords.words('english')
        l1 = []
        l2 = []

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
        cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
        perc = round(cosine, 2) * 100
        print("Answer matching percentage is:", perc, "%")
        speak(("Answer matching percentage is", perc, "%"))



