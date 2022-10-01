import pickle
from Bullying_Model import prep_data
import numpy
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')

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



def predict(sentence, model):
    model = pickle.load(open("model.pkl", "rb"))
    return model.predict(prep_data(sentence)[0])


def get_confidence(json_string):
    message = json.loads(json_string)
    model = pickle.load(open("model.pkl", "rb"))
    text= prep_data(json_string, model)
    return model.predict(text)