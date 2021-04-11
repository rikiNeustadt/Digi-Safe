from backend import TextCleaning
import pickle
import sys
import time

model_path = "model.sav"

prediction_dict = {
    0: "חריג",
    1: "נייטרלי",
}

class ParserModel(object):
    def __init__(self, hebrew_text):
        self.hebrew_text = hebrew_text
        self.clean_massage = hebrew_text
        self.numeric_prediction = -1
        self.prediction = None
        self.probabilty = None
        self.model = pickle.load(open(model_path, 'rb'))
        self.clean_data()
        self.get_probabilty()

    def clean_data(self):
        tc_functions_lst = [
            "rm_hashtags",
            "rm_punctuation",
            "rm_multiple_chars",
            "convert_emojis",
            "spell_corecction",
            "get_stemming",
            "rm_stop_words",
            "rm_short_words",
            "rm_unicode_non_char",
            "rm_white_spaces"
        ]
        for tc_function in tc_functions_lst:
            start = time.time()
            method_to_call = getattr(TextCleaning, tc_function)
            self.clean_massage = method_to_call(self.clean_massage)

    def get_probabilty(self):
        proba = self.model.predict_proba([self.clean_massage])[0]
        pred = max(proba)
        self.numeric_prediction = 0 if proba[0] == pred else 1
        self.prediction = prediction_dict[self.numeric_prediction]
        self.probabilty = "{:.2f}".format(round(pred*100, 2))
        
        
