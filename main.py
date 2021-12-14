import pyttsx3
import pandas as pd
import json
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


with open("D:\\Mocker AI Data\\Mocker NLP\\ques.json") as json_data:
    question = json.load(json_data)
    q = pd.DataFrame(question)
    print(q['questions'][1]['2'])
    speak(q['questions'][1]['2'])


print(q['questions'][1]['keywords'])

for i in range(len(q['questions'][1]['keywords'])):
    '''print(q['questions'][1]['keywords'][i])'''

keyword = (q['questions'][1]['keywords'][i])
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
cosine = c / float((sum(l1) * sum(l2)) ** 0.2)
perc = round(cosine, 2) * 100
print("Answer matching percentage is:", perc, "%")
speak(("Answer matching percentage is", perc, "%"))
