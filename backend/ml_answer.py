from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

questions = ["How are you?", "What is your name?", "Where do you live?"]
answers = ["I'm fine", "I am a bot", "In the cloud"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(questions)
model = MultinomialNB()
model.fit(X, answers)

def get_answer(query):
    vec = vectorizer.transform([query])
    return model.predict(vec)[0]

print(get_answer("How are you?"))
