import pickle
import numpy
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
from model.preprocess import preprocess_input

import json

def prep_data(los):
    def convert_strings_to_nums(strings):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(strings)
        return tokenizer.texts_to_sequences(strings)

    for i,strings in enumerate(los):
        los[i] = convert_strings_to_nums(los[i])

    print(np.asarray(los[0]).shape, np.asarray(los[1]).shape)
    maximum_lens = [max([len(s) for s in strings]) for strings in los]
    max_size = max(maximum_lens)
    print(max_size)
    

    for i,strings in enumerate(los):

        los[i] = pad_sequences(los[i], maxlen=max_size, padding = 'post')

    print(np.asarray(los[0]).shape, np.asarray(los[1]).shape)


    return (los, max_size)
clf = pickle.load(open("model/clf.pkl", "rb"))
tf = pickle.load(open("model/tf_transformer.pkl", "rb"))
model = pickle.load(open("model/model.pkl", "rb"))

sentiments = ["religion","age","gender","ethnicity","not bullying"]
# predict one sentecn at a time
def predict(sentence, model=model , clf = clf, tf = tf):

    return sentiments[model.predict(preprocess_input(sentence, clf, tf))[0]]

model = pickle.load(open("model/model.pkl", "rb"))

# def get_confidence(json_string):
#     message = json.loads(json_string)
#     text= prep_data(json_string, model)
#     return model.predict(text)


print(predict("you are a fucking dumb bitch!", model))