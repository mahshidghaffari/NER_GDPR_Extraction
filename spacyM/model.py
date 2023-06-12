# # import lib
import spacy
from spacy import displacy
import pandas as pd

from spacy.matcher import Matcher
from spacy.tokens import Span


nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

class SpacyModel:
    def __init__(self, train_df, test_df):
        # self.doc_nlp = nlp(data)
        self.train_dat = train_df
        self.test_dat = test_df
        self.nlp = spacy.load("en_core_web_sm")
        self.ner = nlp.get_pipe("ner")


    def test(self):
        return "test"
